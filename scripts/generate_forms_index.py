#!/usr/bin/env python3
"""
Generate protocol forms index and institution config JSON files.

Reads all docs/ct/**/*.md files (skipping index.md), parses YAML front matter,
and outputs:
  - docs/javascripts/protocol-forms-index.json  — one entry per protocol with all FM fields
  - docs/javascripts/institution-config.json     — institution config from config/institution.yml
"""

import json
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Front matter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str) -> dict:
    """Return front matter dict from a Markdown file with YAML front matter.

    Returns {} if no front matter is present or if YAML is malformed.
    """
    if not content.startswith('---\n'):
        return {}
    end = content.find('\n---\n', 4)
    if end == -1:
        return {}
    fm_text = content[4:end]
    try:
        return yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return {}


# ---------------------------------------------------------------------------
# Protocol entry builder
# ---------------------------------------------------------------------------

def build_forms_entry(fm: dict, filepath: Path) -> dict:
    """Build a protocol dict for the forms index from front matter.

    All 17 required fields are always present. Missing fields use empty defaults:
      - dict fields: {}
      - list fields: []
      - string fields: ''
    None values are never passed through.
    """
    return {
        'filepath': str(filepath),
        'slug': fm.get('slug') or '',
        'title': fm.get('title') or '',
        'category': fm.get('category') or '',
        'protocol_type': fm.get('protocol_type') or '',
        'last_updated': fm.get('last_updated') or '',
        'author': fm.get('author') or '',
        'synonyms': fm.get('synonyms') or [],
        'clinical_indications': fm.get('clinical_indications') or [],
        'position': fm.get('position') or '',
        'npo': fm.get('npo') or '',
        'premedication': fm.get('premedication') or '',
        'contrast': fm.get('contrast') or {},
        'series': fm.get('series') or [],
        'recons': fm.get('recons') or [],
        'notes': fm.get('notes') or {},
        'safety': fm.get('safety') or {},
    }


# ---------------------------------------------------------------------------
# Institution config builder
# ---------------------------------------------------------------------------

def build_institution_config(config_path: Path) -> dict:
    """Read institution.yml and return the institution-config dict."""
    try:
        with open(config_path, encoding='utf-8') as f:
            cfg = yaml.safe_load(f) or {}
    except (FileNotFoundError, yaml.YAMLError):
        cfg = {}

    institution = cfg.get('institution') or {}
    contact = cfg.get('contact') or {}

    return {
        'feedback_url': contact.get('feedback_url') or '',
        'institution_name': institution.get('name') or '',
        'site_url': institution.get('site_url') or '',
        'base_path': institution.get('base_path') or '',
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def generate_forms_index():
    docs_dir = Path('docs/ct')
    protocols = []

    for md_file in sorted(docs_dir.rglob('*.md')):
        if md_file.name == 'index.md':
            continue

        content = md_file.read_text(encoding='utf-8')
        fm = parse_frontmatter(content)

        if not fm:
            print(f'WARNING: No front matter in {md_file} — skipping')
            continue

        entry = build_forms_entry(fm, md_file.relative_to('docs'))
        protocols.append(entry)

    protocols.sort(key=lambda x: (x.get('category', ''), x.get('title', '')))

    # Write protocol forms index
    forms_index_path = Path('docs/javascripts/protocol-forms-index.json')
    with open(forms_index_path, 'w', encoding='utf-8') as f:
        json.dump(protocols, f, indent=2)

    print(f'Generated forms index with {len(protocols)} protocols')
    print(f'Saved to: {forms_index_path}')

    # Write institution config
    institution_config = build_institution_config(Path('config/institution.yml'))
    config_output_path = Path('docs/javascripts/institution-config.json')
    with open(config_output_path, 'w', encoding='utf-8') as f:
        json.dump(institution_config, f, indent=2)

    print(f'Saved institution config to: {config_output_path}')


if __name__ == '__main__':
    generate_forms_index()
