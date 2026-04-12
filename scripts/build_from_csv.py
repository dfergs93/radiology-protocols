#!/usr/bin/env python3
"""
New hospital onboarding: generate CT protocol Markdown files with YAML front matter
from data/protocols.csv and data/protocol_series.csv.

Use this when forking the repo for a new institution. After filling in the two CSVs:
  python scripts/build_from_csv.py               # dry run — prints what would be created
  python scripts/build_from_csv.py --apply        # writes Markdown files

For the existing institution, the Markdown files are the living source of truth.
Use extract_to_frontmatter.py to add/update front matter on existing files instead.
"""

import argparse
import csv
import re
from pathlib import Path

import yaml


PROTOCOLS_CSV = Path('data/protocols.csv')
SERIES_CSV = Path('data/protocol_series.csv')
DOCS_CT_DIR = Path('docs/ct')


# ---------------------------------------------------------------------------
# CSV readers
# ---------------------------------------------------------------------------

def load_protocols():
    with open(PROTOCOLS_CSV, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def load_series():
    """Return dict: slug -> {'acquisition': [...], 'recon': [...]}"""
    series_map = {}
    with open(SERIES_CSV, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            slug = row['slug']
            if slug not in series_map:
                series_map[slug] = {'acquisition': [], 'recon': []}
            row_type = row.get('row_type', 'acquisition')
            series_map[slug][row_type].append(row)
    # Sort by order within each type
    for slug in series_map:
        for rtype in ('acquisition', 'recon'):
            series_map[slug][rtype].sort(key=lambda r: int(r.get('order') or 0))
    return series_map


# ---------------------------------------------------------------------------
# Front matter builder
# ---------------------------------------------------------------------------

def pipe_split(value):
    """Split a pipe-separated string into a list, stripping whitespace."""
    if not value:
        return []
    return [v.strip() for v in value.split('|') if v.strip()]


def build_frontmatter(row, series_data):
    slug = row['slug']
    acq_rows = series_data.get(slug, {}).get('acquisition', [])
    recon_rows = series_data.get(slug, {}).get('recon', [])

    contrast_agent = row.get('contrast_agent', 'N/A') or 'N/A'
    has_contrast = contrast_agent.upper() not in ('N/A', 'NONE', '')

    contrast = {'agent': contrast_agent}
    if has_contrast:
        for field in ('contrast_volume', 'contrast_flow_rate', 'contrast_duration',
                      'contrast_timing', 'contrast_roi', 'contrast_trigger'):
            key = field.replace('contrast_', '')
            # Map field names to front matter keys
            key_map = {
                'volume': 'volume', 'flow_rate': 'flow_rate', 'duration': 'duration',
                'timing': 'timing', 'roi': 'roi', 'trigger': 'trigger',
            }
            fm_key = key_map.get(key.replace('contrast_', ''), key)
            val = row.get(field, '')
            if val:
                contrast[fm_key] = val

    series_list = [
        {
            'name': r['series_name'],
            'start': r.get('start_location', ''),
            'end': r.get('end_location', ''),
            'delay': r.get('delay', ''),
            'thickness': r.get('slice_thickness', ''),
            'notes': r.get('notes', ''),
        }
        for r in acq_rows
    ]

    recons_list = [
        {
            'plane': r.get('plane', ''),
            'acquisition': r.get('acquisition', ''),
            'fov': r.get('fov', ''),
            'thickness_increment': r.get('thickness_increment', ''),
            'kernel': r.get('kernel', ''),
            'ir_strength': r.get('ir_strength', ''),
            'notes': r.get('notes', ''),
        }
        for r in recon_rows
    ]

    fm = {
        'title': row['title'],
        'slug': slug,
        'category': row.get('category', ''),
        'protocol_type': row.get('protocol_type', ''),
        'last_updated': row.get('last_updated', ''),
        'author': row.get('author', ''),
        'synonyms': pipe_split(row.get('synonyms', '')),
        'clinical_indications': pipe_split(row.get('clinical_indications', '')),
        'position': row.get('position', ''),
        'npo': row.get('npo', ''),
        'premedication': row.get('premedication', ''),
        'contrast': contrast,
        'tech_params': {
            'kv': row.get('kv', ''),
            'mas': row.get('mas', ''),
            'rotation_time': row.get('rotation_time', ''),
            'pitch': row.get('pitch', ''),
        },
        'series': series_list,
        'recons': recons_list,
        'notes': {
            'tech': row.get('tech_notes', ''),
            'nursing': row.get('nursing_notes', ''),
            'rad': row.get('rad_notes', ''),
            'tips': row.get('tips', ''),
        },
        'safety': {
            'renal': row.get('safety_renal', ''),
            'allergy': row.get('safety_allergy', ''),
        },
    }
    return yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)


# ---------------------------------------------------------------------------
# Markdown body renderer
# ---------------------------------------------------------------------------

def render_markdown_body(row, series_data):
    """Render the Markdown body sections from CSV fields."""
    slug = row['slug']
    title = row['title']
    last_updated = row.get('last_updated', '')
    author = row.get('author', '')
    acq_rows = series_data.get(slug, {}).get('acquisition', [])
    recon_rows = series_data.get(slug, {}).get('recon', [])

    contrast_agent = row.get('contrast_agent', 'N/A') or 'N/A'
    has_contrast = contrast_agent.upper() not in ('N/A', 'NONE', '')

    indications = [f'- {ind}' for ind in (row.get('clinical_indications', '') or '').split('|') if ind.strip()]

    # Acquisition summary
    acq_summary_rows = '\n'.join(
        f'        | {r["series_name"]} | {r.get("delay", "")} | {r.get("start_location", "")} → {r.get("end_location", "")} |'
        for r in acq_rows
    )

    # Contrast section
    if has_contrast:
        contrast_section = f'''
    ===   "Injection Parameters"

        | Parameter | Value |
        |-----------|-------|
        | Agent | {contrast_agent} |
        | Volume | {row.get("contrast_volume", "")} |
        | Flow Rate | {row.get("contrast_flow_rate", "")} |
        | Duration | {row.get("contrast_duration", "")} |
        | Timing Method | {row.get("contrast_timing", "")} |
        | ROI Placement | {row.get("contrast_roi", "")} |
        | Trigger (HU) | {row.get("contrast_trigger", "")} |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \\(2*\\left[\\frac{{\\text{{Patient Weight}}}}{{75 \\text{{ kg}}}} * \\text{{eGFR}}\\right]\\)
'''
    else:
        contrast_section = '''
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.
'''

    # Premedication
    premed = row.get('premedication', '') or ''
    if premed and premed.lower() not in ('none', 'none required', 'n/a', ''):
        premed_items = '\n'.join(f'        - {p.strip()}' for p in premed.split('|') if p.strip())
        premed_section = f'        - None required\n' if not premed_items else premed_items
    else:
        premed_section = '        - None required'

    # Series table
    series_header = '    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |\n    |:------------|:---------------|:-------------|:------|:----------------|:------|'
    series_rows_md = '\n'.join(
        f'    | {r["series_name"]} | {r.get("start_location", "")} | {r.get("end_location", "")} | {r.get("delay", "")} | {r.get("slice_thickness", "")} | {r.get("notes", "")} |'
        for r in acq_rows
    )

    # Post-processing table
    recon_header = '    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |\n    |:------|:------------|:----|:--------------------|:-------|:------------|:------|'
    recon_rows_md = '\n'.join(
        f'    | {r.get("plane", "")} | {r.get("acquisition", "")} | {r.get("fov", "")} | {r.get("thickness_increment", "")} | {r.get("kernel", "")} | {r.get("ir_strength", "")} | {r.get("notes", "")} |'
        for r in recon_rows
    )

    safety_renal = row.get('safety_renal', '') or 'N/A'
    safety_allergy = row.get('safety_allergy', '') or 'N/A'
    kv = row.get('kv', '')
    mas = row.get('mas', '')
    rotation = row.get('rotation_time', '')
    pitch = row.get('pitch', '')

    body = f'''# {title}

**Last Updated:** {last_updated}
**Author:** {author}

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
{acq_summary_rows}

    === "Clinical Indications"

{chr(10).join("        " + ind for ind in indications)}

-   __2. Patient Prep__

    ---

    - **Position:** {row.get("position", "")}
    - **NPO Status:** {row.get("npo", "")}
    - **Pre-Medication:**
{premed_section}

-   __3. IV Contrast & Injection__

    ---
    {contrast_section}

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - {row.get("tech_notes", "")}

    === "Nursing Notes"

        - {row.get("nursing_notes", "")}

        !!! warning "Safety First"
            - **Renal Function:** {safety_renal}
            - **Allergy:** {safety_allergy}

    === "Radiologist Notes"

        - {row.get("rad_notes", "")}

    === "Tips & Tricks"

        - {row.get("tips", "")}

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

{series_header}
{series_rows_md}

=== "Post-Processing"

{recon_header}
{recon_rows_md}

'''
    return body


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--apply', action='store_true', help='Write Markdown files')
    args = parser.parse_args()

    if not PROTOCOLS_CSV.exists():
        print(f'ERROR: {PROTOCOLS_CSV} not found. Fill in data/protocols.csv first.')
        return
    if not SERIES_CSV.exists():
        print(f'ERROR: {SERIES_CSV} not found. Fill in data/protocol_series.csv first.')
        return

    dry_run = not args.apply
    if dry_run:
        print('DRY RUN — no files will be written. Pass --apply to write.\n')

    protocols = load_protocols()
    series_data = load_series()

    for row in protocols:
        slug = row['slug']
        category = row.get('category', 'general').lower()
        out_dir = DOCS_CT_DIR / category
        out_path = out_dir / f'{slug}.md'

        fm = build_frontmatter(row, series_data)
        body = render_markdown_body(row, series_data)
        content = f'---\n{fm}---\n\n{body}'

        if dry_run:
            print(f'Would write: {out_path}')
        else:
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding='utf-8')
            print(f'[WRITE] {out_path}')

    print(f'\n{"Would generate" if dry_run else "Generated"} {len(protocols)} protocol files.')


if __name__ == '__main__':
    main()
