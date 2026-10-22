"""Tests for scripts/admin.py merge_frontmatter: saving must not drop fields the form doesn't show."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

admin = pytest.importorskip('admin', reason='Flask not installed')


def test_merge_keeps_fields_not_in_form():
    original = {
        'title': 'Old', 'modality': 'MR', 'last_reviewed': '2026-01-01',
        'tech_params': {'kv': '100'},
        'contrast': {'agent': 'X', 'type': 'IV'},
        'notes': {'tech': 'old', 'additional_recons': 'MIPs'},
    }
    edited = {'title': 'New', 'contrast': {'agent': 'Y'}, 'notes': {'tech': 'new'}}
    merged = admin.merge_frontmatter(original, edited)
    assert merged['title'] == 'New'
    assert merged['modality'] == 'MR'
    assert merged['last_reviewed'] == '2026-01-01'
    assert merged['tech_params'] == {'kv': '100'}
    assert merged['contrast'] == {'agent': 'Y', 'type': 'IV'}
    assert merged['notes'] == {'tech': 'new', 'additional_recons': 'MIPs'}


def test_merge_form_value_wins_even_when_empty():
    merged = admin.merge_frontmatter({'author': 'A', 'reviewed_by': ['x']}, {'author': '', 'reviewed_by': []})
    assert merged['author'] == ''
    assert merged['reviewed_by'] == []
