#!/usr/bin/env python3
"""
Extract structured data from existing CT protocol Markdown files and:
  1. Prepend YAML front matter to each file
  2. Output data/protocols.csv and data/protocol_series.csv (new normalized schema)

Usage:
  python scripts/extract_to_frontmatter.py            # dry run - prints what would change
  python scripts/extract_to_frontmatter.py --apply    # writes front matter + CSVs
  python scripts/extract_to_frontmatter.py --file docs/ct/chest/ct-pulmonary-embolism.md
"""

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------

def extract_title(content):
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else ''


def extract_last_updated(content):
    m = re.search(r'\*\*Last Updated:\*\*\s*(.+)', content)
    return m.group(1).strip() if m else ''


def extract_author(content):
    # Use [^\S\n]* to avoid crossing newlines (plain \s* would grab next line)
    m = re.search(r'\*\*Author:\*\*[^\S\n]*(.*)', content)
    val = m.group(1).strip() if m else ''
    return val


def extract_category_and_type(content, filepath):
    """Read Category/Protocol Type from trailing lines, fallback to filepath."""
    category = ''
    protocol_type = ''
    for line in reversed(content.splitlines()):
        line = line.strip()
        if line.startswith('Category:'):
            category = line.split(':', 1)[1].strip().lower()
        elif line.startswith('Protocol Type:'):
            protocol_type = line.split(':', 1)[1].strip().lower()
        if category and protocol_type:
            break
    if not category:
        parts = Path(filepath).parts
        if len(parts) >= 2:
            category = parts[-2].lower()
    return category, protocol_type


def extract_clinical_indications(content):
    """Extract indications list from under === "Clinical Indications".

    Only picks up lines indented >= 6 spaces (tab content), stopping at
    card headers (-   __N.__) or the next === tab.
    """
    indications = []
    in_block = False
    for line in content.splitlines():
        stripped = line.strip()
        if '=== "Clinical Indications"' in line:
            in_block = True
            continue
        if in_block:
            # Next tab header
            if stripped.startswith('=== "'):
                break
            # Card item header pattern: "-   __N. ..."
            if re.match(r'^-\s{3,}__\d+\.', line):
                break
            # Real list items inside a tab are indented >= 6 spaces
            indent = len(line) - len(line.lstrip())
            if stripped.startswith('- ') and indent >= 6:
                indications.append(stripped[2:].strip())
    return indications


def extract_patient_prep(content):
    """Extract position, npo_status, and premedication from Patient Prep card."""
    position = ''
    npo = ''
    premedication_lines = []

    lines = content.splitlines()
    in_prep = False
    in_premed = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        if '__2. Patient Prep__' in stripped:
            in_prep = True
            continue

        if in_prep:
            # Stop when we hit the next card
            if re.match(r'-\s+__\d+\.', stripped) and '__2.' not in stripped:
                break

            if '**Position:**' in stripped:
                position = re.sub(r'\*\*Position:\*\*\s*', '', stripped).strip('- ').strip()
                in_premed = False

            elif '**NPO Status:**' in stripped:
                npo = re.sub(r'\*\*NPO Status:\*\*\s*', '', stripped).strip('- ').strip()
                in_premed = False

            elif '**Pre-Medication:**' in stripped:
                in_premed = True
                # inline content after the label
                inline = re.sub(r'\*\*Pre-Medication:\*\*\s*', '', stripped).strip('- ').strip()
                if inline:
                    premedication_lines.append(inline)

            elif in_premed:
                if stripped.startswith('- ') or stripped.startswith('* '):
                    premedication_lines.append(re.sub(r'\*\*', '', stripped.lstrip('- *')).strip())
                elif stripped == '' or stripped.startswith('**'):
                    in_premed = False

    premedication = ' | '.join(premedication_lines) if premedication_lines else ''
    return position, npo, premedication


def extract_contrast(content):
    """Extract Injection Parameters table. Returns dict or None if no-contrast."""
    contrast = {}
    in_table = False

    for line in content.splitlines():
        if '| Parameter | Value |' in line:
            in_table = True
            continue
        if in_table:
            if '|---' in line:
                continue
            if not line.strip() or not line.strip().startswith('|'):
                break
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) >= 2:
                param, value = cells[0].lower(), cells[1]
                if 'agent' in param:
                    contrast['agent'] = value
                elif 'volume' in param:
                    contrast['volume'] = value
                elif 'flow rate' in param:
                    contrast['flow_rate'] = value
                elif 'duration' in param:
                    contrast['duration'] = value
                elif 'timing' in param:
                    contrast['timing'] = value
                elif 'roi' in param:
                    contrast['roi'] = value
                elif 'trigger' in param:
                    contrast['trigger'] = value

    if not contrast:
        return None
    return contrast


def extract_tech_params(content):
    """Extract Technical Parameters table."""
    params = {}
    in_table = False
    for line in content.splitlines():
        if '=== "Technical Parameters"' in line:
            in_table = True
            continue
        if in_table:
            if '| Parameter | Value |' in line:
                continue
            if '|---' in line:
                continue
            if not line.strip():
                continue
            if not line.strip().startswith('|'):
                break
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) >= 2:
                param, value = cells[0].lower(), cells[1]
                if 'kv' in param:
                    params['kv'] = value
                elif 'mas' in param:
                    params['mas'] = value
                elif 'rotation' in param:
                    params['rotation_time'] = value
                elif 'pitch' in param:
                    params['pitch'] = value
    return params


def extract_notes_section(content, section_name):
    """Extract bullet-point content from a named tab section.

    Stops at the next === tab or at a !!! warning/info admonition block.
    """
    lines_out = []
    in_section = False
    for line in content.splitlines():
        stripped = line.strip()
        if f'=== "{section_name}"' in line:
            in_section = True
            continue
        if in_section:
            if stripped.startswith('=== "'):
                break
            # Stop before safety admonition block (e.g. !!! warning "Safety First")
            if stripped.startswith('!!! warning') or stripped.startswith('!!! info'):
                break
            if stripped.startswith('- '):
                lines_out.append(stripped[2:].strip())
    return ' | '.join(lines_out) if lines_out else ''


def extract_safety(content):
    """Extract renal and allergy safety notes from Nursing Notes section."""
    renal = ''
    allergy = ''
    for line in content.splitlines():
        stripped = line.strip()
        if '**Renal Function:**' in stripped:
            renal = re.sub(r'.*\*\*Renal Function:\*\*\s*', '', stripped).strip('- ').strip()
        elif '**Allergy:**' in stripped:
            allergy = re.sub(r'.*\*\*Allergy:\*\*\s*', '', stripped).strip('- ').strip()
    return renal, allergy


def extract_additional_recons(content):
    """Extract text under ### Additional Reconstructions."""
    lines_out = []
    in_section = False
    for line in content.splitlines():
        stripped = line.strip()
        if stripped == '### Additional Reconstructions':
            in_section = True
            continue
        if in_section:
            if stripped.startswith('#') or stripped.startswith('Category:') or stripped.startswith('Protocol Type:'):
                break
            if stripped:
                lines_out.append(stripped)
    return ' '.join(lines_out) if lines_out else ''


def extract_series(content):
    """Extract rows from Series Acquisition table. Skips Scout rows."""
    series = []
    in_table = False
    for line in content.splitlines():
        if '| Series Name |' in line or '| **Series Name** |' in line:
            in_table = True
            continue
        if in_table:
            if '|:---' in line or '|---' in line:
                continue
            if not line.strip() or not line.strip().startswith('|'):
                in_table = False
                continue
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) >= 5:
                name = cells[0].replace('**', '').strip()
                if name.lower().startswith('scout'):
                    continue
                series.append({
                    'name': name,
                    'start': cells[1],
                    'end': cells[2],
                    'delay': cells[3],
                    'thickness': cells[4],
                    'notes': cells[5] if len(cells) > 5 else '',
                })
    return series


def extract_recons(content):
    """Extract rows from Post-Processing table."""
    recons = []
    in_section = False
    header_found = False
    for line in content.splitlines():
        if '=== "Post-Processing"' in line:
            in_section = True
            header_found = False
            continue
        if in_section:
            if '| Plane |' in line:
                header_found = True
                continue
            if '|:---' in line or '|---' in line:
                continue
            if not header_found:
                # Skip blank lines before table header arrives
                continue
            if not line.strip() or not line.strip().startswith('|'):
                break
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) >= 6:
                recons.append({
                    'plane': cells[0],
                    'acquisition': cells[1],
                    'fov': cells[2],
                    'thickness_increment': cells[3],
                    'kernel': cells[4],
                    'ir_strength': cells[5],
                    'notes': cells[6] if len(cells) > 6 else '',
                })
    return recons


# ---------------------------------------------------------------------------
# Front matter builder
# ---------------------------------------------------------------------------

def build_frontmatter(title, slug, category, protocol_type, last_updated, author,
                      indications, position, npo, premedication,
                      contrast, tech_params, series_list, recons_list,
                      tech_notes, nursing_notes, rad_notes, tips,
                      additional_recons, safety_renal, safety_allergy):
    data = {
        'title': title,
        'slug': slug,
        'category': category,
        'protocol_type': protocol_type,
        'last_updated': last_updated,
        'author': author,
        'synonyms': [],
        'clinical_indications': indications,
        'position': position,
        'npo': npo,
        'premedication': premedication,
    }

    if contrast:
        data['contrast'] = contrast
    else:
        data['contrast'] = {'agent': 'N/A', 'type': 'non-contrast'}

    data['tech_params'] = tech_params

    data['series'] = series_list
    data['recons'] = recons_list

    data['notes'] = {
        'tech': tech_notes,
        'nursing': nursing_notes,
        'rad': rad_notes,
        'tips': tips,
        'additional_recons': additional_recons,
    }

    data['safety'] = {
        'renal': safety_renal,
        'allergy': safety_allergy,
    }

    return yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False)


# ---------------------------------------------------------------------------
# CSV row builders
# ---------------------------------------------------------------------------

def protocol_csv_row(slug, title, category, protocol_type, last_updated, author,
                     indications, position, npo, premedication,
                     contrast, tech_params,
                     tech_notes, nursing_notes, rad_notes, tips,
                     additional_recons, safety_renal, safety_allergy):
    c = contrast or {}
    t = tech_params or {}
    return {
        'slug': slug,
        'title': title,
        'category': category,
        'protocol_type': protocol_type,
        'last_updated': last_updated,
        'author': author,
        'synonyms': '',
        'clinical_indications': ' | '.join(indications),
        'position': position,
        'npo': npo,
        'premedication': premedication,
        'contrast_agent': c.get('agent', 'N/A'),
        'contrast_volume': c.get('volume', ''),
        'contrast_flow_rate': c.get('flow_rate', ''),
        'contrast_duration': c.get('duration', ''),
        'contrast_timing': c.get('timing', ''),
        'contrast_roi': c.get('roi', ''),
        'contrast_trigger': c.get('trigger', ''),
        'kv': t.get('kv', ''),
        'mas': t.get('mas', ''),
        'rotation_time': t.get('rotation_time', ''),
        'pitch': t.get('pitch', ''),
        'tech_notes': tech_notes,
        'nursing_notes': nursing_notes,
        'rad_notes': rad_notes,
        'tips': tips,
        'additional_recons': additional_recons,
        'safety_renal': safety_renal,
        'safety_allergy': safety_allergy,
    }


PROTOCOLS_CSV_FIELDS = [
    'slug', 'title', 'category', 'protocol_type', 'last_updated', 'author',
    'synonyms', 'clinical_indications', 'position', 'npo', 'premedication',
    'contrast_agent', 'contrast_volume', 'contrast_flow_rate', 'contrast_duration',
    'contrast_timing', 'contrast_roi', 'contrast_trigger',
    'kv', 'mas', 'rotation_time', 'pitch',
    'tech_notes', 'nursing_notes', 'rad_notes', 'tips', 'additional_recons',
    'safety_renal', 'safety_allergy',
]

SERIES_CSV_FIELDS = [
    'slug', 'row_type', 'order',
    'series_name', 'start_location', 'end_location', 'delay', 'slice_thickness',  # acquisition
    'plane', 'acquisition', 'fov', 'thickness_increment', 'kernel', 'ir_strength',  # recon
    'notes',
]


def series_csv_rows(slug, series_list, recons_list):
    rows = []
    for i, s in enumerate(series_list, 1):
        rows.append({
            'slug': slug,
            'row_type': 'acquisition',
            'order': i,
            'series_name': s.get('name', ''),
            'start_location': s.get('start', ''),
            'end_location': s.get('end', ''),
            'delay': s.get('delay', ''),
            'slice_thickness': s.get('thickness', ''),
            'plane': '',
            'acquisition': '',
            'fov': '',
            'thickness_increment': '',
            'kernel': '',
            'ir_strength': '',
            'notes': s.get('notes', ''),
        })
    for i, r in enumerate(recons_list, 1):
        rows.append({
            'slug': slug,
            'row_type': 'recon',
            'order': i,
            'series_name': '',
            'start_location': '',
            'end_location': '',
            'delay': '',
            'slice_thickness': '',
            'plane': r.get('plane', ''),
            'acquisition': r.get('acquisition', ''),
            'fov': r.get('fov', ''),
            'thickness_increment': r.get('thickness_increment', ''),
            'kernel': r.get('kernel', ''),
            'ir_strength': r.get('ir_strength', ''),
            'notes': r.get('notes', ''),
        })
    return rows


# ---------------------------------------------------------------------------
# Per-file processing
# ---------------------------------------------------------------------------

def process_file(md_path, dry_run=True):
    """Parse a protocol Markdown file and return (frontmatter_yaml, protocol_row, series_rows)."""
    content = md_path.read_text(encoding='utf-8')

    # Skip files that already have front matter
    if content.startswith('---\n'):
        print(f'  [SKIP] Already has front matter: {md_path}')
        return None, None, None

    slug = md_path.stem  # filename without .md
    title = extract_title(content)
    last_updated = extract_last_updated(content)
    author = extract_author(content)

    rel_path = md_path.relative_to(Path('docs'))
    category, protocol_type = extract_category_and_type(content, rel_path)

    indications = extract_clinical_indications(content)
    position, npo, premedication = extract_patient_prep(content)
    contrast = extract_contrast(content)
    tech_params = extract_tech_params(content)
    series_list = extract_series(content)
    recons_list = extract_recons(content)

    tech_notes = extract_notes_section(content, 'Technologist Notes')
    nursing_notes = extract_notes_section(content, 'Nursing Notes')
    rad_notes = extract_notes_section(content, 'Radiologist Notes')
    tips = extract_notes_section(content, 'Tips & Tricks')
    additional_recons = extract_additional_recons(content)
    safety_renal, safety_allergy = extract_safety(content)

    fm = build_frontmatter(
        title, slug, category, protocol_type, last_updated, author,
        indications, position, npo, premedication,
        contrast, tech_params, series_list, recons_list,
        tech_notes, nursing_notes, rad_notes, tips,
        additional_recons, safety_renal, safety_allergy,
    )

    proto_row = protocol_csv_row(
        slug, title, category, protocol_type, last_updated, author,
        indications, position, npo, premedication,
        contrast, tech_params,
        tech_notes, nursing_notes, rad_notes, tips,
        additional_recons, safety_renal, safety_allergy,
    )

    s_rows = series_csv_rows(slug, series_list, recons_list)

    if dry_run:
        print(f'\n{"="*60}')
        print(f'FILE: {md_path}')
        print(f'{"="*60}')
        print('--- (front matter preview) ---')
        print(fm)
        print(f'  series rows: {len(series_list)} acquisition, {len(recons_list)} recon')
    else:
        new_content = f'---\n{fm}---\n\n{content}'
        md_path.write_text(new_content, encoding='utf-8')
        print(f'  [WRITE] {md_path}')

    return fm, proto_row, s_rows


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--apply', action='store_true', help='Write front matter to files and output CSVs')
    parser.add_argument('--file', help='Process a single file only (useful for testing)')
    args = parser.parse_args()

    dry_run = not args.apply

    if dry_run:
        print('DRY RUN — no files will be written. Pass --apply to write changes.\n')

    docs_dir = Path('docs/ct')
    if args.file:
        md_files = [Path(args.file)]
    else:
        md_files = sorted(f for f in docs_dir.rglob('*.md') if f.name != 'index.md')

    all_proto_rows = []
    all_series_rows = []
    skipped = 0
    processed = 0

    for md_path in md_files:
        fm, proto_row, s_rows = process_file(md_path, dry_run=dry_run)
        if proto_row is None:
            skipped += 1
            continue
        processed += 1
        all_proto_rows.append(proto_row)
        all_series_rows.extend(s_rows)

    print(f'\nSummary: {processed} processed, {skipped} skipped (already have front matter)')

    if args.apply and all_proto_rows:
        data_dir = Path('data')
        data_dir.mkdir(exist_ok=True)

        proto_csv = data_dir / 'protocols.csv'
        with open(proto_csv, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=PROTOCOLS_CSV_FIELDS)
            w.writeheader()
            w.writerows(all_proto_rows)
        print(f'\n[WRITE] {proto_csv} ({len(all_proto_rows)} rows)')

        series_csv = data_dir / 'protocol_series.csv'
        with open(series_csv, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=SERIES_CSV_FIELDS)
            w.writeheader()
            w.writerows(all_series_rows)
        print(f'[WRITE] {series_csv} ({len(all_series_rows)} rows)')

    elif dry_run and all_proto_rows:
        print(f'\nWould write data/protocols.csv ({len(all_proto_rows)} rows)')
        print(f'Would write data/protocol_series.csv ({len(all_series_rows)} rows)')


if __name__ == '__main__':
    main()
