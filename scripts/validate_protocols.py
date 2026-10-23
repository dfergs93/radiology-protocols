#!/usr/bin/env python3
"""
Validate protocol front matter against schema/protocol.schema.json.

Also checks things a schema can't express:
  - slug matches the file name
  - category matches the folder the file lives in
  - modality matches the top-level folder (docs/ct -> CT, docs/mr -> MR)
  - slugs are unique within a modality
  - last_reviewed is not in the future

Usage:
    python scripts/validate_protocols.py            # all protocols
    python scripts/validate_protocols.py FILE ...   # specific files

Exits 1 if any protocol is invalid (used by CI).
"""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / 'docs'
SCHEMA_PATH = REPO_ROOT / 'schema' / 'protocol.schema.json'

# Top-level docs folder -> modality value
MODALITY_DIRS = {'ct': 'CT', 'mr': 'MR'}


def parse_frontmatter(content: str):
    """Return the front matter dict, or None if the file has none."""
    if not content.startswith('---\n'):
        return None
    end = content.find('\n---\n', 4)
    if end == -1:
        return None
    return yaml.safe_load(content[4:end]) or {}


def _stringify_dates(value):
    """YAML turns unquoted 2026-01-01 into a date object; treat it as the string the schema expects."""
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _stringify_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_stringify_dates(v) for v in value]
    return value


def protocol_files(docs_dir: Path = DOCS_DIR) -> list[Path]:
    files = []
    for folder in MODALITY_DIRS:
        root = docs_dir / folder
        if root.is_dir():
            files.extend(p for p in sorted(root.rglob('*.md')) if p.name != 'index.md')
    return files


def validate_file(path: Path, validator: Draft202012Validator, docs_dir: Path = DOCS_DIR,
                  today: dt.date | None = None) -> tuple[list[str], dict | None]:
    """Return (errors, front_matter) for one protocol file."""
    today = today or dt.date.today()
    try:
        fm = parse_frontmatter(path.read_text(encoding='utf-8'))
    except yaml.YAMLError as exc:
        return [f'YAML error: {exc}'], None
    if fm is None:
        return ['missing YAML front matter'], None

    fm = _stringify_dates(fm)
    errors = []
    for err in sorted(validator.iter_errors(fm), key=lambda e: list(e.path)):
        where = '.'.join(str(p) for p in err.path) or '(top level)'
        errors.append(f'{where}: {err.message}')

    rel = path.relative_to(docs_dir)
    modality_dir = rel.parts[0]
    if fm.get('slug') and fm['slug'] != path.stem:
        errors.append(f"slug '{fm['slug']}' does not match file name '{path.stem}'")
    if len(rel.parts) >= 3 and fm.get('category') and fm['category'] != rel.parts[1]:
        errors.append(f"category '{fm['category']}' does not match folder '{rel.parts[1]}'")
    expected_modality = MODALITY_DIRS.get(modality_dir)
    if fm.get('modality') and expected_modality and fm['modality'] != expected_modality:
        errors.append(f"modality '{fm['modality']}' does not match folder '{modality_dir}/' (expected {expected_modality})")
    reviewed = fm.get('last_reviewed')
    if isinstance(reviewed, str):
        try:
            if dt.date.fromisoformat(reviewed) > today:
                errors.append(f'last_reviewed {reviewed} is in the future')
        except ValueError:
            errors.append(f'last_reviewed {reviewed} is not a real date')
    return errors, fm


def validate_all(paths: list[Path], docs_dir: Path = DOCS_DIR) -> dict[Path, list[str]]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
    validator = Draft202012Validator(schema)
    problems: dict[Path, list[str]] = {}
    seen: dict[tuple, Path] = {}
    for path in paths:
        errors, fm = validate_file(path, validator, docs_dir)
        if fm and fm.get('slug'):
            key = (path.relative_to(docs_dir).parts[0], fm['slug'])
            if key in seen:
                errors.append(f"duplicate slug '{fm['slug']}' (also in {seen[key].relative_to(docs_dir)})")
            seen.setdefault(key, path)
        if errors:
            problems[path] = errors
    return problems


def main(argv: list[str]) -> int:
    paths = [Path(a).resolve() for a in argv] if argv else protocol_files()
    problems = validate_all(paths)
    for path, errors in problems.items():
        print(f'\n{path.relative_to(REPO_ROOT)}')
        for e in errors:
            print(f'  - {e}')
    if problems:
        print(f'\n{len(problems)} of {len(paths)} protocol(s) invalid.')
        return 1
    print(f'All {len(paths)} protocols valid.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
