#!/usr/bin/env python3
"""
Generate protocol comparison index from YAML front matter in protocol Markdown files
(docs/ct and docs/mr). Also carries review dates used by the Review Status page.

Reads front matter written by extract_to_frontmatter.py and outputs
docs/javascripts/protocol-comparison-index.json in the format consumed by
protocol-compare.js.
"""

import calendar
import datetime as dt
import json
from pathlib import Path

import yaml

# Top-level docs folders that hold protocols
PROTOCOL_DIRS = ['docs/ct', 'docs/mr']
DEFAULT_REVIEW_INTERVAL_MONTHS = 12


# ---------------------------------------------------------------------------
# Front matter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(content):
    """Return (frontmatter_dict, body_text) from a Markdown file with YAML front matter."""
    if not content.startswith('---\n'):
        return {}, content
    end = content.find('\n---\n', 4)
    if end == -1:
        return {}, content
    fm_text = content[4:end]
    body = content[end + 5:]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


# ---------------------------------------------------------------------------
# Timing / delay helpers (kept from original for acquisition diagram support)
# ---------------------------------------------------------------------------

def parse_duration_seconds(duration_str):
    """Parse a duration string like '40s' or '40 sec' into integer seconds."""
    import re
    if not duration_str:
        return None
    m = re.search(r'(\d+)', str(duration_str))
    return int(m.group(1)) if m else None


def is_nc_phase(series_name):
    """Return True if the series name indicates a non-contrast phase."""
    import re
    name_lower = str(series_name).lower()
    nc_keywords = ['non-contrast', 'non contrast', ' nc ', 'nc ', ' nc', 'without contrast',
                   'unenhanced', 'without', 'pre-contrast', 'pre contrast']
    for kw in nc_keywords:
        if kw in name_lower:
            return True
    if re.search(r'\bpre\b', name_lower):
        return True
    if re.search(r'\bnc\b', name_lower):
        return True
    return False


def infer_phase_type(series_name):
    """Infer phase type string from series name."""
    name_lower = str(series_name).lower()
    if is_nc_phase(series_name):
        return 'non-contrast'
    if 'arterial' in name_lower:
        return 'arterial'
    if any(kw in name_lower for kw in ['portal', 'venous', 'pv']):
        return 'portal'
    if any(kw in name_lower for kw in ['delayed', 'delay', 'nephrographic', 'excretory', 'equilibrium']):
        return 'delayed'
    return 'other'


def compute_delay_seconds(delay_str, series_name, contrast_duration_secs, saline_seconds=0, last_phase_end=0):
    """Compute delay_seconds for a series entry."""
    import re
    PHASE_DURATION = 5
    NC_END_GAP = 5

    if is_nc_phase(series_name):
        if contrast_duration_secs and contrast_duration_secs > 0:
            return -(PHASE_DURATION + NC_END_GAP)
        return 0

    if not delay_str or str(delay_str).strip().upper() == 'N/A':
        return 0

    delay_lower = str(delay_str).lower()

    if re.search(r'bolus[\s-]*track', delay_lower):
        inj_dur = contrast_duration_secs or 30
        return inj_dur + saline_seconds

    if 'immediate' in delay_lower:
        return last_phase_end

    m = re.search(r'(\d+)', delay_str)
    if m:
        return int(m.group(1))

    return 0


# ---------------------------------------------------------------------------
# Review dates
# ---------------------------------------------------------------------------

def load_review_interval(config_path=Path('config/institution.yml')):
    """Default review interval (months) from institution.yml."""
    try:
        cfg = yaml.safe_load(config_path.read_text(encoding='utf-8')) or {}
    except (FileNotFoundError, yaml.YAMLError):
        cfg = {}
    return (cfg.get('review') or {}).get('interval_months') or DEFAULT_REVIEW_INTERVAL_MONTHS


def add_months(day, months):
    """Return *day* plus *months*, clamped to the end of the month (Jan 31 + 1 month = Feb 28/29)."""
    month_index = day.month - 1 + months
    year = day.year + month_index // 12
    month = month_index % 12 + 1
    return dt.date(year, month, min(day.day, calendar.monthrange(year, month)[1]))


def next_review_due(last_reviewed, interval_months):
    """ISO date the next review is due, or '' if never reviewed or the date is unreadable."""
    if not last_reviewed:
        return ''
    try:
        day = last_reviewed if isinstance(last_reviewed, dt.date) else dt.date.fromisoformat(str(last_reviewed))
    except ValueError:
        return ''
    return add_months(day, interval_months).isoformat()


def _date_str(value):
    return value.isoformat() if isinstance(value, dt.date) else (str(value) if value else '')


# ---------------------------------------------------------------------------
# Protocol builder
# ---------------------------------------------------------------------------

def build_protocol_entry(fm, filepath, default_review_interval=DEFAULT_REVIEW_INTERVAL_MONTHS):
    """Build a protocol dict for the comparison index from front matter."""
    contrast = fm.get('contrast') or {}
    series_list = fm.get('series') or []
    recons_list = fm.get('recons') or []
    review_interval = fm.get('review_interval_months') or default_review_interval

    # Contrast info in the format protocol-compare.js expects
    contrast_entry = {
        'agent': contrast.get('agent', 'N/A'),
        'volume': contrast.get('volume', ''),
        'flow_rate': contrast.get('flow_rate', ''),
        'duration': contrast.get('duration', ''),
        'timing': contrast.get('timing', ''),
        'roi': contrast.get('roi', ''),
        'trigger': contrast.get('trigger', ''),
        'type': 'Non-contrast' if contrast.get('agent', 'N/A').upper() in ('N/A', 'NONE', '') else 'IV Contrast',
    }

    # Compute delay_seconds for each acquisition series (needed by acquisition diagram)
    contrast_dur_secs = parse_duration_seconds(contrast.get('duration'))
    saline_secs = 0  # saline not in front matter; default to 0
    last_phase_end = 0
    phase_duration = 5

    series_entries = []
    for s in series_list:
        name = s.get('name', '')
        delay_str = s.get('delay', '')
        delay_secs = compute_delay_seconds(
            delay_str, name, contrast_dur_secs,
            saline_seconds=saline_secs,
            last_phase_end=last_phase_end,
        )
        last_phase_end = max(last_phase_end, delay_secs + phase_duration)
        series_entries.append({
            'name': name,
            'start': s.get('start', ''),
            'end': s.get('end', ''),
            'delay': delay_str,
            'thickness': s.get('thickness', ''),
            'notes': s.get('notes', ''),
            'delay_seconds': delay_secs,
            'phase_type': infer_phase_type(name),
            'coverage': f"{s.get('start', '')} → {s.get('end', '')}",
        })

    # Acquisition summary (from series list, excluding non-data series)
    summary = [
        {
            'series': s.get('name', ''),
            'phase': s.get('delay', ''),
            'coverage': f"{s.get('start', '')} → {s.get('end', '')}",
        }
        for s in series_list
    ]

    return {
        'filepath': str(filepath),
        'title': fm.get('title', ''),
        'category': fm.get('category', '').title(),
        'slug': fm.get('slug', ''),
        'modality': fm.get('modality') or 'CT',
        'last_updated': _date_str(fm.get('last_updated')),
        'last_reviewed': _date_str(fm.get('last_reviewed')),
        'reviewed_by': fm.get('reviewed_by') or [],
        'review_interval_months': review_interval,
        'next_review_due': next_review_due(fm.get('last_reviewed'), review_interval),
        'contrast': contrast_entry,
        'series': series_entries,
        'summary': summary,
        'gantt': None,  # Gantt diagrams removed from site
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def generate_comparison_index():
    protocols = []
    review_interval = load_review_interval()
    md_files = [f for d in PROTOCOL_DIRS if Path(d).is_dir() for f in sorted(Path(d).rglob('*.md'))]

    for md_file in md_files:
        if md_file.name == 'index.md':
            continue

        content = md_file.read_text(encoding='utf-8')
        fm, _ = parse_frontmatter(content)

        if not fm:
            print(f'WARNING: No front matter in {md_file} — skipping')
            continue

        print(f'Processing: {md_file}')
        entry = build_protocol_entry(fm, md_file.relative_to('docs'), review_interval)
        protocols.append(entry)

    protocols.sort(key=lambda x: (x.get('category', ''), x.get('title', '')))

    output_file = Path('docs/javascripts/protocol-comparison-index.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(protocols, f, indent=2)

    print(f'\nGenerated comparison index with {len(protocols)} protocols')
    print(f'Saved to: {output_file}')


if __name__ == '__main__':
    generate_comparison_index()
