#!/usr/bin/env python3
"""
Generate protocol comparison index from all protocol markdown files
"""

import os
import json
import re
from pathlib import Path

def extract_gantt_diagram(content):
    """Extract mermaid gantt diagram from markdown"""
    # Match the entire mermaid code block including config
    pattern = r'```mermaid\s*\n(.*?)```'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(0)  # Return full block with ```mermaid markers
    return None


def extract_contrast_info(content):
    """Extract contrast information from Injection Parameters table"""
    contrast = {}

    lines = content.split('\n')
    in_contrast_table = False

    for i, line in enumerate(lines):
        # Look for Injection Parameters table
        if '| Parameter | Value |' in line:
            in_contrast_table = True
            print(f"  Found injection parameters table at line {i}")
            continue

        # Skip separator
        if in_contrast_table and '|---' in line:
            continue

        # End of table
        if in_contrast_table and (not line.strip() or (line.strip() and not line.strip().startswith('|'))):
            break

        # Process rows
        if in_contrast_table and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c]

            if len(cells) >= 2:
                param = cells[0].lower().strip()
                value = cells[1].strip()

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

                print(f"    Extracted {param}: {value}")

    # Determine contrast type
    if not contrast or contrast.get('agent', '').upper() in ['N/A', 'NONE', '']:
        contrast['type'] = 'Non-contrast'
    else:
        contrast['type'] = 'IV Contrast'

    print(f"  Contrast type: {contrast.get('type', 'Unknown')}")
    return contrast


def parse_duration_seconds(duration_str):
    """Parse a duration string like '40s' or '40 sec' into integer seconds. Returns None if unparseable."""
    if not duration_str:
        return None
    m = re.search(r'(\d+)', duration_str)
    if m:
        return int(m.group(1))
    return None


def is_nc_phase(series_name):
    """Return True if the series name indicates a non-contrast phase."""
    name_lower = series_name.lower()
    nc_keywords = ['non-contrast', 'non contrast', ' nc ', 'nc ', ' nc', 'without contrast',
                   'unenhanced', 'without', 'pre-contrast', 'pre contrast']
    # Also check if name starts with or equals 'pre' or 'nc'
    for kw in nc_keywords:
        if kw in name_lower:
            return True
    # Check word-boundary matches for short keywords
    if re.search(r'\bpre\b', name_lower):
        return True
    if re.search(r'\bnc\b', name_lower):
        return True
    return False


def infer_phase_type(series_name):
    """Infer phase type string from series name."""
    name_lower = series_name.lower()

    # Non-contrast checks
    if is_nc_phase(series_name):
        return 'non-contrast'

    if 'arterial' in name_lower:
        return 'arterial'

    if any(kw in name_lower for kw in ['portal', 'venous', 'pv']):
        return 'portal'

    if any(kw in name_lower for kw in ['delayed', 'delay', 'nephrographic', 'excretory', 'equilibrium']):
        return 'delayed'

    return 'other'


def extract_gantt_durations(content):
    """Extract contrast and saline durations (seconds) from the mermaid gantt source.
    Returns (contrast_seconds, saline_seconds).
    """
    gantt_match = re.search(r'```mermaid(.*?)```', content, re.DOTALL)
    if not gantt_match:
        return 0, 0
    contrast_secs = 0
    saline_secs = 0
    for line in gantt_match.group(1).split('\n'):
        stripped = line.strip()
        if ':' not in stripped:
            continue
        m = re.search(r',\s*(\d+(?:\.\d+)?)s\s*$', stripped, re.IGNORECASE)
        if not m:
            continue
        dur = float(m.group(1))
        if re.match(r'contrast\b', stripped, re.IGNORECASE):
            contrast_secs = dur
        elif 'saline' in stripped.lower():
            saline_secs = dur
    return contrast_secs, saline_secs


def compute_delay_seconds(delay_str, series_name, contrast, saline_seconds=0, last_phase_end=0):
    """Compute delay_seconds for a series entry.

    NC phases in contrast protocols: bar ends 5s before injection (offset = -(5+5) = -10).
    Bolus track → injection duration + saline flush duration.
    Immediate → end time of the previous phase (sequential).
    N/A or empty → 0.
    Otherwise extract first integer from delay string.
    """
    PHASE_DURATION = 5  # assumed bar duration for sequential tracking
    NC_END_GAP = 5      # seconds NC phase ends before injection start

    if is_nc_phase(series_name):
        if contrast and contrast.get('type', '').lower() != 'non-contrast' and contrast.get('agent', '').upper() not in ('N/A', 'NONE', ''):
            return -(PHASE_DURATION + NC_END_GAP)
        return 0

    if not delay_str or delay_str.strip().upper() == 'N/A':
        return 0

    delay_lower = delay_str.lower()

    if re.search(r'bolus[\s-]*track', delay_lower):
        inj_dur = parse_duration_seconds(contrast.get('duration', '')) or contrast.get('gantt_duration', 0) or 30
        return inj_dur + saline_seconds

    if 'immediate' in delay_lower:
        return last_phase_end

    m = re.search(r'(\d+)', delay_str)
    if m:
        return int(m.group(1))

    return 0


def extract_series_info(content, contrast, saline_seconds=0):
    """Extract acquisition series information from table"""
    series = []
    lines = content.split('\n')
    in_series_table = False
    last_phase_end = 0
    phase_duration = 5  # default bar duration for sequential timing

    for i, line in enumerate(lines):
        if '| Series Name |' in line or '| **Series Name** |' in line:
            in_series_table = True
            print(f"  Found series table header at line {i}")
            continue

        if in_series_table and '|:---' in line:
            continue

        if in_series_table and (not line.strip() or (line.strip() and not line.strip().startswith('|'))):
            in_series_table = False
            print(f"  End of series table at line {i}")
            break

        if in_series_table and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c]

            if len(cells) >= 5:
                series_name = cells[0].replace('**', '').strip()

                if not series_name.lower().startswith('scout'):
                    delay_str = cells[3]
                    delay_secs = compute_delay_seconds(
                        delay_str, series_name, contrast,
                        saline_seconds=saline_seconds,
                        last_phase_end=last_phase_end,
                    )
                    last_phase_end = max(last_phase_end, delay_secs + phase_duration)

                    series_info = {
                        'name': series_name,
                        'start': cells[1],
                        'end': cells[2],
                        'delay': delay_str,
                        'thickness': cells[4],
                        'notes': cells[5] if len(cells) > 5 else '',
                        'delay_seconds': delay_secs,
                        'phase_type': infer_phase_type(series_name),
                    }
                    series_info['coverage'] = f"{series_info['start']} → {series_info['end']}"
                    series.append(series_info)
                    print(f"    Added series: {series_name} (delay_seconds={series_info['delay_seconds']}, phase_type={series_info['phase_type']})")

    print(f"  Total series extracted: {len(series)}")
    return series

def extract_acquisition_summary(content):
    """Extract the acquisition summary table from Clinical Summary"""
    summary = []

    lines = content.split('\n')
    in_summary = False

    for i, line in enumerate(lines):
        # Look for Acquisition Summary table
        if '| Series | Phase | Coverage |' in line:
            in_summary = True
            print(f"  Found acquisition summary at line {i}")
            continue

        # Skip separator
        if in_summary and '|:---' in line:
            continue

        # End of table
        if in_summary and (not line.strip() or (line.strip() and not line.strip().startswith('|'))):
            break

        # Process rows
        if in_summary and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c]

            if len(cells) >= 3:
                summary.append({
                    'series': cells[0],
                    'phase': cells[1],
                    'coverage': cells[2]
                })
                print(f"    Added: {cells[0]}")

    return summary

def extract_protocol_metadata(content, filepath):
    """Extract basic protocol metadata"""
    metadata = {
        'filepath': str(filepath)
    }

    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip()

    # Extract category from filepath
    parts = filepath.parts
    if len(parts) >= 3:
        metadata['category'] = parts[-2].replace('_', ' ').title()

    return metadata

def generate_comparison_index():
    """Generate comprehensive comparison index"""
    protocols = []

    docs_dir = Path('docs/ct')

    # Scan all protocol markdown files
    for md_file in docs_dir.rglob('*.md'):
        if md_file.name == 'index.md':
            continue

        print(f"Processing: {md_file}")

        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        protocol = extract_protocol_metadata(content, md_file.relative_to('docs'))
        protocol['gantt'] = extract_gantt_diagram(content)
        contrast = extract_contrast_info(content)
        gantt_contrast_secs, saline_seconds = extract_gantt_durations(content)
        # Supplement injection table duration with gantt value if table row is absent
        if gantt_contrast_secs and not contrast.get('duration'):
            contrast['gantt_duration'] = gantt_contrast_secs
        protocol['contrast'] = contrast
        protocol['series'] = extract_series_info(content, contrast, saline_seconds=saline_seconds)
        protocol['summary'] = extract_acquisition_summary(content)

        protocols.append(protocol)

    # Sort by category then title
    protocols.sort(key=lambda x: (x.get('category', ''), x.get('title', '')))

    # Save to JSON
    output_file = Path('docs/javascripts/protocol-comparison-index.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(protocols, f, indent=2)

    print(f"\nGenerated comparison index with {len(protocols)} protocols")
    print(f"Saved to: {output_file}")

if __name__ == '__main__':
    generate_comparison_index()
