"""Tests for scripts/validate_protocols.py."""
import datetime as dt
import json
import os
import sys
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import validate_protocols as vp  # noqa: E402

VALIDATOR = Draft202012Validator(json.loads(vp.SCHEMA_PATH.read_text(encoding='utf-8')))
TODAY = dt.date(2026, 10, 22)


def minimal_fm(**overrides):
    fm = {
        'title': 'CT Test',
        'slug': 'ct-test',
        'modality': 'CT',
        'category': 'chest',
        'protocol_type': 'contrast-enhanced',
        'last_updated': '2026-01-01',
        'clinical_indications': ['Something'],
        'contrast': {'agent': 'N/A'},
        'series': [{'name': 'Chest'}],
        'recons': [],
        'notes': {},
        'safety': {},
    }
    fm.update(overrides)
    return fm


def write_protocol(docs_dir: Path, rel: str, fm: dict) -> Path:
    path = docs_dir / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('---\n' + yaml.dump(fm, sort_keys=False) + '---\n\n# Body\n', encoding='utf-8')
    return path


def errors_for(tmp_path, rel, fm):
    path = write_protocol(tmp_path, rel, fm)
    errors, _ = vp.validate_file(path, VALIDATOR, docs_dir=tmp_path, today=TODAY)
    return errors


def test_minimal_protocol_is_valid(tmp_path):
    assert errors_for(tmp_path, 'ct/chest/ct-test.md', minimal_fm()) == []


def test_review_fields_are_valid(tmp_path):
    fm = minimal_fm(last_reviewed='2026-06-01', reviewed_by=['Dr A (Radiologist)'], review_interval_months=24)
    assert errors_for(tmp_path, 'ct/chest/ct-test.md', fm) == []


def test_unquoted_yaml_date_is_accepted(tmp_path):
    fm = minimal_fm(last_updated=dt.date(2026, 1, 1))
    assert errors_for(tmp_path, 'ct/chest/ct-test.md', fm) == []


@pytest.mark.parametrize('override, expected', [
    ({'modality': 'PET'}, 'modality'),
    ({'category': 'head'}, 'category'),
    ({'series': []}, 'series'),
    ({'last_updated': '1/1/2026'}, 'last_updated'),
    ({'unknown_field': 'x'}, 'unknown_field'),
    ({'contrast': {'agent': 'X', 'speed': 'fast'}}, 'speed'),
])
def test_schema_rejects_bad_values(tmp_path, override, expected):
    errors = errors_for(tmp_path, 'ct/chest/ct-test.md', minimal_fm(**override))
    assert any(expected in e for e in errors), errors


def test_missing_required_field(tmp_path):
    fm = minimal_fm()
    del fm['title']
    errors = errors_for(tmp_path, 'ct/chest/ct-test.md', fm)
    assert any("'title' is a required property" in e for e in errors)


def test_slug_must_match_filename(tmp_path):
    errors = errors_for(tmp_path, 'ct/chest/other-name.md', minimal_fm())
    assert any('does not match file name' in e for e in errors)


def test_category_must_match_folder(tmp_path):
    errors = errors_for(tmp_path, 'ct/vascular/ct-test.md', minimal_fm())
    assert any("does not match folder 'vascular'" in e for e in errors)


def test_modality_must_match_folder(tmp_path):
    errors = errors_for(tmp_path, 'mr/chest/ct-test.md', minimal_fm())
    assert any('expected MR' in e for e in errors)


def test_future_review_date_rejected(tmp_path):
    errors = errors_for(tmp_path, 'ct/chest/ct-test.md', minimal_fm(last_reviewed='2027-01-01'))
    assert any('in the future' in e for e in errors)


def test_missing_front_matter(tmp_path):
    path = tmp_path / 'ct' / 'chest' / 'x.md'
    path.parent.mkdir(parents=True)
    path.write_text('# No front matter\n')
    errors, _ = vp.validate_file(path, VALIDATOR, docs_dir=tmp_path, today=TODAY)
    assert errors == ['missing YAML front matter']


def test_duplicate_slugs_detected(tmp_path):
    a = write_protocol(tmp_path, 'ct/chest/ct-test.md', minimal_fm())
    b = write_protocol(tmp_path, 'ct/vascular/ct-test.md', minimal_fm(category='vascular'))
    problems = vp.validate_all([a, b], docs_dir=tmp_path)
    assert any('duplicate slug' in e for e in problems.get(b, []))


def test_all_repo_protocols_valid():
    """Every protocol in the repo passes validation."""
    files = vp.protocol_files()
    assert files, 'no protocols found'
    assert vp.validate_all(files) == {}
