#!/usr/bin/env python3
"""
One-time migration script: reads existing protocol Markdown files and prepends
YAML front matter containing all structured data.

After running this, YAML front matter becomes the single source of truth for
machine-readable fields. The Markdown body is preserved exactly as-is.

Usage:
    python scripts/extract_to_frontmatter.py [--dry-run]
"""

import re
import sys
import argparse
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------

def extract_title(content: str) -> str:
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else ''


def extract_meta_field(content: str, label: str) -> str:
    """Extract value from lines like **Last Updated:** 2026-01-01"""
    m = re.search(rf'\*\*{re.escape(label)}:\*\*\s*(.+)', content)
    return m.group(1).strip() if m else ''


def extract_category(content: str) -> str:
    m = re.search(r'^Category:\s*(.+)$', content, re.MULTILINE)
    return m.group(1).strip().lower() if m else ''


def extract_protocol_type(content: str) -> str:
    m = re.search(r'^Protocol Type:\s*(.+)$', content, re.MULTILINE)
    return m.group(1).strip().lower() if m else ''


def extract_tab_content(content: str, tab_name: str) -> str:
    """Extract bullet-list content from a named === tab section."""
    pattern = rf'===\s+"{re.escape(tab_name)}"\s*\n(.*?)(?:===|\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return ''
    block = m.group(1)
    # Collect indented bullet lines and strip leading whitespace / dashes
    lines = []
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith('- ') or stripped.startswith('* '):
            lines.append(stripped[2:].strip())
        elif stripped and not stripped.startswith('!'):
            # plain text line (not admonition)
            lines.append(stripped)
    return '\n'.join(lines)


def extract_clinical_indications(content: str) -> list:
    block = extract_tab_content(content, 'Clinical Indications')
    if not block:
        return []
    return [line.strip() for line in block.splitlines() if line.strip()]


def extract_patient_field(content: str, label: str) -> str:
    m = re.search(rf'-\s+\*\*{re.escape(label)}:\*\*\s*(.+)', content)
    return m.group(1).strip() if m else ''


def extract_premedication(content: str) -> str:
    """Extract pre-medication block following the Pre-Medication label."""
    m = re.search(r'\*\*Pre-Medication:\*\*\s*\n((?:\s+- .+\n?)+)', content)
    if m:
        lines = [l.strip().lstrip('- ').strip() for l in m.group(1).splitlines() if l.strip()]
        return '; '.join(lines)
    # Inline value on same line
    m2 = re.search(r'\*\*Pre-Medication:\*\*\s*(.+)', content)
    return m2.group(1).strip() if m2 else ''


def extract_injection_table(content: str) -> dict:
    """Extract the Injection Parameters table into a dict."""
    params = {}
    pattern = r'===\s+"Injection Parameters"\s*\n(.*?)(?:===|\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return params
    for line in m.group(1).splitlines():
        if not line.strip().startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|') if c.strip()]
        if len(cells) < 2:
            continue
        key = cells[0].lower()
        val = cells[1]
        if 'agent' in key:
            params['agent'] = val
        elif 'volume' in key:
            params['volume'] = val
        elif 'flow rate' in key:
            params['flow_rate'] = val
        elif 'duration' in key:
            params['duration'] = val
        elif 'timing' in key:
            params['timing'] = val
        elif 'roi' in key:
            params['roi'] = val
        elif 'trigger' in key:
            params['trigger'] = val
    return params


def extract_technical_params(content: str) -> dict:
    """Extract the Technical Parameters table."""
    params = {}
    pattern = r'===\s+"Technical Parameters"\s*\n(.*?)(?:===|\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return params
    for line in m.group(1).splitlines():
        if not line.strip().startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|') if c.strip()]
        if len(cells) < 2:
            continue
        key = cells[0].lower()
        val = cells[1]
        if key == 'kv':
            params['kv'] = val
        elif key == 'mas':
            params['mas'] = val
        elif 'rotation' in key:
            # strip trailing 's' if present
            params['rotation_time'] = val.rstrip('s').strip()
        elif 'pitch' in key:
            params['pitch'] = val
    return params


def extract_series(content: str) -> list:
    """Extract acquisition series rows (excluding Scout)."""
    series = []
    pattern = r'===\s+"Series Acquisition"\s*\n(.*?)(?:===|\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return series
    order = 0
    for line in m.group(1).splitlines():
        if not line.strip().startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|') if c.strip()]
        if len(cells) < 5:
            continue
        name = cells[0].replace('**', '').strip()
        if name.lower() in ('series name', '---', ':---'):
            continue
        if name.lower().startswith('scout'):
            continue
        order += 1
        series.append({
            'slug': '',          # filled by caller
            'row_type': 'acquisition',
            'order': order,
            'name_or_plane': name,
            'start_location': cells[1] if len(cells) > 1 else '',
            'end_location': cells[2] if len(cells) > 2 else '',
            'delay': cells[3] if len(cells) > 3 else '',
            'slice_thickness': cells[4] if len(cells) > 4 else '',
            'acquisition': '',
            'fov': '',
            'thickness_increment': '',
            'kernel': '',
            'ir_strength': '',
            'notes': cells[5] if len(cells) > 5 else '',
        })
    return series


def extract_recons(content: str) -> list:
    """Extract post-processing reconstruction rows."""
    recons = []
    pattern = r'===\s+"Post-Processing"\s*\n(.*?)(?:===|\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return recons
    order = 0
    for line in m.group(1).splitlines():
        if not line.strip().startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|') if c.strip()]
        if len(cells) < 3:
            continue
        plane = cells[0].replace('**', '').strip()
        if plane.lower() in ('plane', '---', ':---'):
            continue
        order += 1
        recons.append({
            'slug': '',
            'row_type': 'recon',
            'order': order,
            'name_or_plane': plane,
            'start_location': '',
            'end_location': '',
            'delay': '',
            'slice_thickness': '',
            'acquisition': cells[1] if len(cells) > 1 else '',
            'fov': cells[2] if len(cells) > 2 else '',
            'thickness_increment': cells[3] if len(cells) > 3 else '',
            'kernel': cells[4] if len(cells) > 4 else '',
            'ir_strength': cells[5] if len(cells) > 5 else '',
            'notes': cells[6] if len(cells) > 6 else '',
        })
    return recons


def extract_additional_recons(content: str) -> str:
    m = re.search(r'### Additional Reconstructions\s*\n(.+?)(?:\n\n|\Z)', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ''


def extract_notes_tab(content: str, tab_name: str) -> str:
    """Extract plain-text notes from a named tab (strips admonitions)."""
    pattern = rf'===\s+"{re.escape(tab_name)}"\s*\n(.*?)(?:===|\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return ''
    block = m.group(1)
    lines = []
    in_admonition = False
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith('!!!'):
            in_admonition = True
            continue
        if in_admonition:
            if not line.startswith(' ') and stripped:
                in_admonition = False
            else:
                # Capture safety lines
                if '**Renal Function:**' in stripped or '**Allergy:**' in stripped:
                    lines.append(stripped.lstrip('- ').strip())
                continue
        if stripped.startswith('- ') or stripped.startswith('* '):
            lines.append(stripped[2:].strip())
        elif stripped:
            lines.append(stripped)
    return '\n'.join(lines)


def extract_safety(content: str) -> tuple:
    """Return (renal_text, allergy_text) from Safety First admonition."""
    renal = ''
    allergy = ''
    m = re.search(r'!!! warning "Safety First"\s*\n(.*?)(?:\n\n|\Z)', content, re.DOTALL)
    if m:
        block = m.group(1)
        rm = re.search(r'\*\*Renal Function:\*\*\s*(.+)', block)
        am = re.search(r'\*\*Allergy:\*\*\s*(.+)', block)
        renal = rm.group(1).strip() if rm else ''
        allergy = am.group(1).strip() if am else ''
    return renal, allergy


# ---------------------------------------------------------------------------
# Front matter builder
# ---------------------------------------------------------------------------

def build_frontmatter(filepath: Path, content: str) -> dict:
    slug = filepath.stem
    injection = extract_injection_table(content)
    tech = extract_technical_params(content)
    renal, allergy = extract_safety(content)

    fm = {
        'title': extract_title(content),
        'slug': slug,
        'synonyms': [],
        'category': extract_category(content),
        'protocol_type': extract_protocol_type(content),
        'last_updated': extract_meta_field(content, 'Last Updated'),
        'author': extract_meta_field(content, 'Author'),
        'clinical_indications': extract_clinical_indications(content),
        'patient': {
            'position': extract_patient_field(content, 'Position'),
            'npo': extract_patient_field(content, 'NPO Status'),
            'premedication': extract_premedication(content),
        },
        'contrast': {
            'agent': injection.get('agent', ''),
            'volume': injection.get('volume', ''),
            'flow_rate': injection.get('flow_rate', ''),
            'duration': injection.get('duration', ''),
            'timing': injection.get('timing', ''),
            'roi': injection.get('roi', ''),
            'trigger': injection.get('trigger', ''),
        },
        'technical': {
            'kv': tech.get('kv', ''),
            'mas': tech.get('mas', ''),
            'rotation_time': tech.get('rotation_time', ''),
            'pitch': tech.get('pitch', ''),
        },
        'notes': {
            'tech': extract_notes_tab(content, 'Technologist Notes'),
            'nursing': extract_notes_tab(content, 'Nursing Notes'),
            'radiologist': extract_notes_tab(content, 'Radiologist Notes'),
            'tips': extract_notes_tab(content, 'Tips & Tricks'),
        },
        'safety': {
            'renal': renal,
            'allergy': allergy,
        },
        'additional_recons': extract_additional_recons(content),
    }
    return fm


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_file(md_file: Path, dry_run: bool) -> bool:
    content = md_file.read_text(encoding='utf-8')

    # Skip files that already have front matter
    if content.startswith('---'):
        print(f'  SKIP (already has front matter): {md_file}')
        return False

    fm = build_frontmatter(md_file, content)

    # Render front matter — use default_flow_style=False for block style,
    # allow_unicode for clean output, sort_keys=False to preserve insertion order
    fm_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content = f'---\n{fm_str}---\n\n{content}'

    if dry_run:
        print(f'  DRY RUN: {md_file}')
        print('  Front matter keys:', list(fm.keys()))
    else:
        md_file.write_text(new_content, encoding='utf-8')
        print(f'  UPDATED: {md_file}')

    return True


def main():
    parser = argparse.ArgumentParser(description='Add YAML front matter to existing protocol Markdown files.')
    parser.add_argument('--dry-run', action='store_true', help='Print what would be done without writing files')
    parser.add_argument('--path', default='docs/ct', help='Root path to scan (default: docs/ct)')
    args = parser.parse_args()

    root = Path(args.path)
    if not root.exists():
        print(f'ERROR: path {root} does not exist', file=sys.stderr)
        sys.exit(1)

    updated = 0
    skipped = 0
    for md_file in sorted(root.rglob('*.md')):
        if md_file.name == 'index.md':
            continue
        print(f'Processing: {md_file}')
        if process_file(md_file, args.dry_run):
            updated += 1
        else:
            skipped += 1

    print(f'\nDone. Updated: {updated}, Skipped (already had front matter): {skipped}')


if __name__ == '__main__':
    main()
