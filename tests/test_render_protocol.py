"""Unit tests for scripts/render_protocol.py — written before implementation (TDD)."""
import sys
import os
import copy

import pytest
import yaml

# Allow importing from scripts/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from render_protocol import render_document


# ---------------------------------------------------------------------------
# Shared fixture — a complete, valid front matter dict
# ---------------------------------------------------------------------------

@pytest.fixture
def base_fm():
    return {
        'title': 'CT PE',
        'slug': 'ct-pe',
        'category': 'chest',
        'protocol_type': 'contrast-enhanced',
        'last_updated': '2026-01-01',
        'author': 'Dr. Smith',
        'synonyms': [],
        'clinical_indications': ['Suspected PE', 'Acute dyspnea'],
        'position': 'Supine feet-first',
        'npo': 'NPO 2 hours',
        'premedication': 'Metoprolol 5mg IV',
        'contrast': {
            'agent': 'Isovue 370',
            'volume': '1.3 mL/kg',
            'flow_rate': '5 mL/s',
            'duration': '15 - 20s',
            'timing': 'Bolus Tracking',
            'roi': 'Main PA',
            'trigger': '100 HU',
        },
        'series': [
            {
                'name': 'PA Phase',
                'start': 'Lung apices',
                'end': 'Costophrenic angles',
                'delay': 'Bolus tracked',
                'thickness': '0.625 mm',
                'notes': '',
            }
        ],
        'recons': [
            {
                'plane': 'Axial',
                'acquisition': 'Angiogram',
                'fov': 'Chest',
                'thickness_increment': '1.25 mm/1.25 mm',
                'kernel': 'Standard',
                'ir_strength': '3',
                'notes': '',
            }
        ],
        'notes': {
            'tech': 'Coach breath hold',
            'nursing': '20G IV',
            'rad': 'Assess RV/LV',
            'tips': 'Arms raised',
        },
        'safety': {
            'renal': 'eGFR > 30',
            'allergy': 'Check iodine',
        },
    }


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_document_starts_with_frontmatter_fence(base_fm):
    """Document must start with --- YAML fence."""
    doc = render_document(base_fm)
    assert doc.startswith('---\n')


def test_document_contains_closing_fence_and_title(base_fm):
    """Document must contain closing YAML fence and H1 title."""
    doc = render_document(base_fm)
    assert '\n---\n' in doc
    assert '# CT PE' in doc


def test_frontmatter_roundtrips_through_yaml(base_fm):
    """YAML front matter block must round-trip: slug and contrast.agent preserved."""
    doc = render_document(base_fm)
    # Extract the YAML block between the first --- and the closing ---
    parts = doc.split('---\n', 2)
    # parts[0] == '' (before first ---\n), parts[1] == yaml text, parts[2] == rest
    assert len(parts) >= 3, 'Expected at least two --- fences'
    parsed = yaml.safe_load(parts[1])
    assert parsed['slug'] == 'ct-pe'
    assert parsed['contrast']['agent'] == 'Isovue 370'


def test_contrast_section_rendered_when_present(base_fm):
    """When contrast agent is present, Injection Parameters table must appear."""
    doc = render_document(base_fm)
    assert 'Injection Parameters' in doc
    assert 'Isovue 370' in doc
    assert '5 mL/s' in doc


def test_no_contrast_message_when_agent_is_na(base_fm):
    """When contrast.agent == 'N/A', render no-contrast info block."""
    fm = copy.deepcopy(base_fm)
    fm['contrast']['agent'] = 'N/A'
    doc = render_document(fm)
    assert 'No Intravenous Contrast' in doc
    assert 'Injection Parameters' not in doc


def test_series_table_row_present(base_fm):
    """Series table row must contain series name and start location."""
    doc = render_document(base_fm)
    assert 'PA Phase' in doc
    assert 'Lung apices' in doc


def test_recons_table_row_present(base_fm):
    """Recons table row must contain thickness/increment and notes when provided."""
    fm = copy.deepcopy(base_fm)
    fm['recons'][0]['notes'] = 'Mediastinal window'
    doc = render_document(fm)
    assert '1.25 mm/1.25 mm' in doc
    assert 'Mediastinal window' in doc


def test_clinical_indications_rendered(base_fm):
    """All clinical indications must appear as list items."""
    doc = render_document(base_fm)
    assert 'Suspected PE' in doc
    assert 'Acute dyspnea' in doc


def test_notes_sections_rendered(base_fm):
    """All four notes fields must appear in the document."""
    doc = render_document(base_fm)
    assert 'Coach breath hold' in doc
    assert '20G IV' in doc
    assert 'Assess RV/LV' in doc
    assert 'Arms raised' in doc


def test_safety_in_nursing_tab(base_fm):
    """Safety renal and allergy fields must appear in the document."""
    doc = render_document(base_fm)
    assert 'eGFR > 30' in doc
    assert 'Check iodine' in doc


def test_premedication_pipe_separated_renders_as_bullets(base_fm):
    """Pipe-separated premedication string must be split into individual bullets."""
    fm = copy.deepcopy(base_fm)
    fm['premedication'] = 'Metoprolol 5mg IV | Check contraindications'
    doc = render_document(fm)
    assert 'Metoprolol 5mg IV' in doc
    assert 'Check contraindications' in doc


def test_empty_premedication_renders_none_required(base_fm):
    """Empty premedication field must render as 'None required'."""
    fm = copy.deepcopy(base_fm)
    fm['premedication'] = ''
    doc = render_document(fm)
    assert 'None required' in doc
