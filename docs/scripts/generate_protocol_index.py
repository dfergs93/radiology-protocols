
"""
Generate protocol index JSON from markdown files
"""

import re
import json
from pathlib import Path


def extract_gantt_from_md(md_path):
    """Extract Gantt diagram and title from markdown file"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {md_path}: {e}")
        return None
    
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else md_path.stem
    
    gantt_match = re.search(r'```mermaid\n(gantt[\s\S]*?)```', content)
    gantt = gantt_match.group(1).strip() if gantt_match else None
    
    return {
        'title': title,
        'gantt': gantt,
        'file_path': str(md_path.relative_to('docs'))
    }


def generate_protocol_index():
    """Generate JSON index of all protocols with Gantt diagrams"""
    protocols = {}
    
    protocol_dir = Path('docs/protocols')
    
    if not protocol_dir.exists():
        print(f"Warning: {protocol_dir} does not exist. Creating it.")
        protocol_dir.mkdir(parents=True, exist_ok=True)
        return protocols
    
    for md_file in protocol_dir.rglob('*.md'):
        if md_file.name.startswith('_') or md_file.name == 'index.md':
            continue
        
        protocol_id = md_file.stem
        protocol_data = extract_gantt_from_md(md_file)
        
        if protocol_data and protocol_data['gantt']:
            protocols[protocol_id] = protocol_data
    
    output_path = Path('docs/javascripts/protocol-index.json')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(protocols, f, indent=2)
    
    print(f"✅ Generated protocol index with {len(protocols)} protocols")
    print(f"   Output: {output_path}")
    
    return protocols


if __name__ == '__main__':
    generate_protocol_index()