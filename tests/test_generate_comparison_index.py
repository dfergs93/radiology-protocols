"""Tests for review-date logic in scripts/generate_comparison_index.py."""
import datetime as dt
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from generate_comparison_index import add_months, build_protocol_entry, next_review_due  # noqa: E402


def test_add_months_simple():
    assert add_months(dt.date(2026, 3, 15), 12) == dt.date(2027, 3, 15)


def test_add_months_clamps_to_month_end():
    assert add_months(dt.date(2026, 1, 31), 1) == dt.date(2026, 2, 28)
    assert add_months(dt.date(2027, 1, 31), 13) == dt.date(2028, 2, 29)


def test_next_review_due():
    assert next_review_due('2026-01-10', 12) == '2027-01-10'
    assert next_review_due(dt.date(2026, 1, 10), 6) == '2026-07-10'
    assert next_review_due('', 12) == ''
    assert next_review_due(None, 12) == ''
    assert next_review_due('not a date', 12) == ''


def test_entry_includes_review_fields_and_override():
    fm = {
        'title': 'T', 'slug': 't', 'category': 'chest', 'modality': 'CT',
        'last_updated': dt.date(2026, 1, 1),
        'last_reviewed': '2026-02-01', 'reviewed_by': ['Dr A'], 'review_interval_months': 6,
        'contrast': {'agent': 'N/A'}, 'series': [{'name': 'Chest'}],
    }
    entry = build_protocol_entry(fm, Path('ct/chest/t.md'), default_review_interval=12)
    assert entry['modality'] == 'CT'
    assert entry['last_updated'] == '2026-01-01'
    assert entry['last_reviewed'] == '2026-02-01'
    assert entry['reviewed_by'] == ['Dr A']
    assert entry['review_interval_months'] == 6
    assert entry['next_review_due'] == '2026-08-01'


def test_entry_never_reviewed():
    fm = {'title': 'T', 'slug': 't', 'category': 'chest', 'contrast': {'agent': 'N/A'}, 'series': []}
    entry = build_protocol_entry(fm, Path('ct/chest/t.md'))
    assert entry['last_reviewed'] == ''
    assert entry['next_review_due'] == ''
    assert entry['reviewed_by'] == []
