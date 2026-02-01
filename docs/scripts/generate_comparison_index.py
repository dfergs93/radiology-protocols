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

def extract_series_info(content):
    """Extract acquisition series information from table"""
    series = []
    
    # Split content into lines
    lines = content.split('\n')
    
    in_series_table = False
    
    for i, line in enumerate(lines):
        # Look for the Series Acquisition table header
        if '| Series Name |' in line or '| **Series Name** |' in line:
            in_series_table = True
            print(f"  Found series table header at line {i}")
            continue
        
        # Skip separator line
        if in_series_table and '|:---' in line:
            continue
        
        # End of table (empty line or start of new section)
        if in_series_table and (not line.strip() or (line.strip() and not line.strip().startswith('|'))):
            in_series_table = False
            print(f"  End of series table at line {i}")
            break
        
        # Process data rows
        if in_series_table and line.strip().startswith('|'):
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c]  # Remove empty elements
            
            if len(cells) >= 5:
                series_name = cells[0].replace('**', '').strip()
                
                # Skip scout
                if series_name.lower() != 'scout':
                    series_info = {
                        'name': series_name,
                        'start': cells[1],
                        'end': cells[2],
                        'delay': cells[3],
                        'thickness': cells[4],
                        'notes': cells[5] if len(cells) > 5 else ''
                    }
                    series_info['coverage'] = f"{series_info['start']} → {series_info['end']}"
                    series.append(series_info)
                    print(f"    Added series: {series_name}")
    
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
        protocol['contrast'] = extract_contrast_info(content)
        protocol['series'] = extract_series_info(content)
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