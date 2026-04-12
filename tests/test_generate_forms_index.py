"""
Unit tests for generate_forms_index.py (TDD: written before implementation).
"""

import sys
from pathlib import Path

# Allow importing from scripts/ directory
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

import pytest
from generate_forms_index import parse_frontmatter, build_forms_entry

SAMPLE_FM_TEXT = """\
---
title: CT Pulmonary Embolism
slug: ct-pulmonary-embolism
category: chest
protocol_type: contrast-enhanced
last_updated: '2026-01-01'
author: ''
synonyms: []
clinical_indications:
- Suspected PE
position: Supine feet-first
npo: NPO 2 hours
premedication: None required
contrast:
  agent: Isovue 370
  volume: 1.3 mL/kg
  flow_rate: 5 mL/s
  duration: 15 - 20s
  timing: Bolus Tracking
  roi: Main Pulmonary Artery
  trigger: 100 HU
series:
- name: Pulmonary Angiogram
  start: Lung apices
  end: Costophrenic angles
  delay: Bolus tracked
  thickness: 0.625 mm
  notes: ''
recons:
- plane: Axial
  acquisition: Angiogram
  fov: Chest
  thickness_increment: 1.25 mm/1.25 mm
  kernel: Standard
  ir_strength: '3'
  notes: ''
notes:
  tech: Coach breath hold
  nursing: 20G IV preferred
  rad: Assess RV/LV ratio
  tips: Arms fully raised
safety:
  renal: Verify eGFR > 30
  allergy: Check iodine allergy
---
# CT Pulmonary Embolism

Protocol body text here.
"""

REQUIRED_FIELDS = [
    'filepath', 'slug', 'title', 'category', 'protocol_type',
    'last_updated', 'author', 'synonyms', 'clinical_indications',
    'position', 'npo', 'premedication', 'contrast', 'series',
    'recons', 'notes', 'safety',
]


# ---------------------------------------------------------------------------
# Test 1: parse_frontmatter returns dict with correct slug and category
# ---------------------------------------------------------------------------

def test_parse_frontmatter_returns_dict():
    fm = parse_frontmatter(SAMPLE_FM_TEXT)
    assert isinstance(fm, dict)
    assert fm['slug'] == 'ct-pulmonary-embolism'
    assert fm['category'] == 'chest'


# ---------------------------------------------------------------------------
# Test 2: no front matter returns empty dict
# ---------------------------------------------------------------------------

def test_parse_frontmatter_no_fm_returns_empty():
    content = "# Just a plain markdown file\n\nNo front matter here.\n"
    fm = parse_frontmatter(content)
    assert fm == {}


# ---------------------------------------------------------------------------
# Test 3: malformed YAML returns empty dict
# ---------------------------------------------------------------------------

def test_parse_frontmatter_malformed_returns_empty():
    content = "---\ntitle: [\nbad: yaml: here\n---\nBody\n"
    fm = parse_frontmatter(content)
    assert fm == {}


# ---------------------------------------------------------------------------
# Test 4: build_forms_entry includes all 17 required fields
# ---------------------------------------------------------------------------

def test_build_forms_entry_includes_all_required_fields():
    fm = parse_frontmatter(SAMPLE_FM_TEXT)
    entry = build_forms_entry(fm, Path('ct/chest/ct-pulmonary-embolism.md'))
    for field in REQUIRED_FIELDS:
        assert field in entry, f"Missing required field: {field}"


# ---------------------------------------------------------------------------
# Test 5: build_forms_entry values are correct
# ---------------------------------------------------------------------------

def test_build_forms_entry_values():
    fm = parse_frontmatter(SAMPLE_FM_TEXT)
    filepath = Path('ct/chest/ct-pulmonary-embolism.md')
    entry = build_forms_entry(fm, filepath)

    assert entry['contrast']['agent'] == 'Isovue 370'
    assert entry['series'][0]['name'] == 'Pulmonary Angiogram'
    assert entry['notes']['tech'] == 'Coach breath hold'
    assert entry['safety']['renal'] == 'Verify eGFR > 30'
    assert entry['filepath'] == str(filepath)


# ---------------------------------------------------------------------------
# Test 6: missing optional fields default to {}, [], or ''
# ---------------------------------------------------------------------------

def test_build_forms_entry_missing_optional_fields_default_empty():
    minimal_content = "---\ntitle: Minimal Protocol\nslug: minimal\ncategory: head\n---\nBody\n"
    fm = parse_frontmatter(minimal_content)
    entry = build_forms_entry(fm, Path('ct/head/minimal.md'))

    # Dict fields default to {}
    assert entry['contrast'] == {}
    assert entry['notes'] == {}
    assert entry['safety'] == {}

    # List fields default to []
    assert entry['synonyms'] == []
    assert entry['clinical_indications'] == []
    assert entry['series'] == []
    assert entry['recons'] == []

    # String fields default to ''
    assert entry['protocol_type'] == ''
    assert entry['last_updated'] == ''
    assert entry['author'] == ''
    assert entry['position'] == ''
    assert entry['npo'] == ''
    assert entry['premedication'] == ''
