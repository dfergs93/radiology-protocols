# Protocol Editing & Change Request Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-extended-cc:subagent-driven-development (recommended) or superpowers-extended-cc:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a static change request form for website users, a local Flask admin app for the protocol lead, and a pre-commit hook to keep derived JSON indexes in sync.

**Architecture:** A new `generate_forms_index.py` script produces a full-YAML JSON index used by the static form JS. A shared `render_protocol.py` module converts YAML front matter dicts to Markdown documents, used by both the admin app (on save) and as documentation of the canonical rendering logic. The Flask admin app (`scripts/admin.py`) reads/writes MD files directly and runs all three index scripts after each save.

**Tech Stack:** Python 3.x, Flask, PyYAML (already installed), vanilla JS (no framework), MkDocs Material, GitHub Actions.

---

## File Map

| Path | Action | Responsibility |
|---|---|---|
| `scripts/generate_forms_index.py` | Create | Full YAML → JSON for form pre-population; also writes institution-config.json |
| `docs/javascripts/protocol-forms-index.json` | Generated | Client-side protocol data for change request form |
| `docs/javascripts/institution-config.json` | Generated | feedback_url and institution name for JS routing |
| `scripts/render_protocol.py` | Create | Shared renderer: YAML front matter dict → full Markdown document |
| `scripts/admin.py` | Create | Flask admin app: list / edit / create protocols |
| `docs/request-change.md` | Create | Change request form page (static MkDocs page) |
| `docs/javascripts/request-change.js` | Create | Form population, diff logic, submission routing, protocol page button injection |
| `scripts/install_hooks.py` | Create | Copies pre-commit hook to .git/hooks/ |
| `scripts/hooks/pre-commit` | Create | Bash hook: regenerates indexes when docs/ct/ files are staged |
| `tests/test_generate_forms_index.py` | Create | Tests for forms index parsing and output shape |
| `tests/test_render_protocol.py` | Create | Tests for markdown renderer correctness |
| `.github/workflows/ci.yml` | Modify | Add generate_forms_index.py step before deploy |
| `docs/.pages` | Modify | Add request-change.md to nav |
| `mkdocs.yml` | Modify | Add request-change.js and protocol-forms-index.json to extra_javascript |
| `docs/for-institutions/adoption-guide.md` | Modify | Add install_hooks.py step to setup |

---

## Task 1: Forms Index and Institution Config Generator

**Goal:** Script that reads all protocol YAML front matter and outputs `protocol-forms-index.json` (full data for form pre-population) and `institution-config.json` (feedback_url for JS routing). Added to CI.

**Files:**
- Create: `scripts/generate_forms_index.py`
- Create (generated): `docs/javascripts/protocol-forms-index.json`
- Create (generated): `docs/javascripts/institution-config.json`
- Create: `tests/test_generate_forms_index.py`
- Modify: `.github/workflows/ci.yml`

**Acceptance Criteria:**
- [ ] Script runs from repo root without error
- [ ] Output JSON contains one entry per protocol with all YAML front matter fields
- [ ] Each entry has: filepath, slug, title, category, protocol_type, last_updated, author, synonyms, clinical_indications, position, npo, premedication, contrast, series, recons, notes, safety
- [ ] institution-config.json has: feedback_url, institution_name, site_url, base_path
- [ ] CI runs script before deploy
- [ ] All tests pass

**Verify:** `cd /path/to/protocol_manager && python scripts/generate_forms_index.py && python -m pytest tests/test_generate_forms_index.py -v` → no errors, 87 protocols in output

**Steps:**

- [ ] **Step 1: Write failing tests**

Create `tests/test_generate_forms_index.py`:

```python
import json
import sys
import textwrap
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))
from generate_forms_index import parse_frontmatter, build_forms_entry

SAMPLE_FM_TEXT = textwrap.dedent("""\
    ---
    title: CT PE
    slug: ct-pe
    category: chest
    protocol_type: contrast-enhanced
    last_updated: '2026-01-01'
    author: ''
    synonyms: []
    clinical_indications:
    - Suspected PE
    - Acute dyspnea
    position: Supine feet-first with arms raised
    npo: NPO 2 hours recommended
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
    - name: PA Phase
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
      notes: Mediastinal window
    notes:
      tech: Coach breath hold
      nursing: 20G IV
      rad: Assess RV/LV
      tips: Arms raised
    safety:
      renal: eGFR > 30
      allergy: Check iodine
    ---
    # CT PE
""")


def test_parse_frontmatter_returns_dict():
    fm = parse_frontmatter(SAMPLE_FM_TEXT)
    assert fm['slug'] == 'ct-pe'
    assert fm['category'] == 'chest'
    assert fm['clinical_indications'] == ['Suspected PE', 'Acute dyspnea']


def test_parse_frontmatter_no_fm_returns_empty():
    fm = parse_frontmatter('# No front matter here\nsome content')
    assert fm == {}


def test_parse_frontmatter_malformed_returns_empty():
    fm = parse_frontmatter('---\nnot: valid: yaml:\n---\n')
    assert fm == {}


def test_build_forms_entry_includes_all_required_fields():
    fm = parse_frontmatter(SAMPLE_FM_TEXT)
    entry = build_forms_entry(fm, Path('ct/chest/ct-pe.md'))
    required = [
        'filepath', 'slug', 'title', 'category', 'protocol_type',
        'last_updated', 'author', 'synonyms', 'clinical_indications',
        'position', 'npo', 'premedication', 'contrast', 'series',
        'recons', 'notes', 'safety',
    ]
    for field in required:
        assert field in entry, f'Missing field: {field}'


def test_build_forms_entry_values():
    fm = parse_frontmatter(SAMPLE_FM_TEXT)
    entry = build_forms_entry(fm, Path('ct/chest/ct-pe.md'))
    assert entry['filepath'] == 'ct/chest/ct-pe.md'
    assert entry['contrast']['agent'] == 'Isovue 370'
    assert len(entry['series']) == 1
    assert entry['series'][0]['name'] == 'PA Phase'
    assert len(entry['recons']) == 1
    assert entry['notes']['tech'] == 'Coach breath hold'
    assert entry['safety']['renal'] == 'eGFR > 30'


def test_build_forms_entry_missing_optional_fields_default_empty():
    fm = {'title': 'Test', 'slug': 'test'}
    entry = build_forms_entry(fm, Path('ct/test.md'))
    assert entry['contrast'] == {}
    assert entry['series'] == []
    assert entry['notes'] == {}
    assert entry['safety'] == {}
    assert entry['clinical_indications'] == []
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /path/to/protocol_manager && python -m pytest tests/test_generate_forms_index.py -v
```

Expected: `ModuleNotFoundError: No module named 'generate_forms_index'`

- [ ] **Step 3: Write the script**

Create `scripts/generate_forms_index.py`:

```python
#!/usr/bin/env python3
"""
Generate protocol forms index for the change request form.

Outputs:
  docs/javascripts/protocol-forms-index.json  — full YAML front matter for all protocols
  docs/javascripts/institution-config.json    — feedback_url and site metadata from institution.yml

Run by CI alongside generate_comparison_index.py. Safe to re-run at any time.
"""

import json
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Front matter parsing (same pattern as generate_comparison_index.py)
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str) -> dict:
    """Return front matter dict from Markdown content, or empty dict on failure."""
    if not content.startswith('---\n'):
        return {}
    end = content.find('\n---\n', 4)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(content[4:end]) or {}
    except yaml.YAMLError:
        return {}


# ---------------------------------------------------------------------------
# Entry builder
# ---------------------------------------------------------------------------

def build_forms_entry(fm: dict, filepath: Path) -> dict:
    """Build a forms index entry from a front matter dict."""
    return {
        'filepath': str(filepath),
        'slug': fm.get('slug', ''),
        'title': fm.get('title', ''),
        'category': fm.get('category', ''),
        'protocol_type': fm.get('protocol_type', ''),
        'last_updated': str(fm.get('last_updated', '')),
        'author': fm.get('author', '') or '',
        'synonyms': fm.get('synonyms') or [],
        'clinical_indications': fm.get('clinical_indications') or [],
        'position': fm.get('position', '') or '',
        'npo': fm.get('npo', '') or '',
        'premedication': fm.get('premedication', '') or '',
        'contrast': fm.get('contrast') or {},
        'series': fm.get('series') or [],
        'recons': fm.get('recons') or [],
        'notes': fm.get('notes') or {},
        'safety': fm.get('safety') or {},
    }


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def generate_forms_index():
    """Write docs/javascripts/protocol-forms-index.json."""
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

    protocols.sort(key=lambda x: (x['category'], x['title']))

    output = Path('docs/javascripts/protocol-forms-index.json')
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(protocols, f, indent=2)

    print(f'Generated forms index: {len(protocols)} protocols → {output}')


def generate_institution_config():
    """Write docs/javascripts/institution-config.json from config/institution.yml."""
    config_path = Path('config/institution.yml')
    with open(config_path, encoding='utf-8') as f:
        config = yaml.safe_load(f) or {}

    institution = config.get('institution') or {}
    contact = config.get('contact') or {}

    output = {
        'feedback_url': contact.get('feedback_url', '') or '',
        'institution_name': institution.get('name', '') or '',
        'site_url': institution.get('site_url', '') or '',
        'base_path': institution.get('base_path', '') or '',
    }

    out_path = Path('docs/javascripts/institution-config.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)

    print(f'Generated institution config → {out_path}')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    generate_forms_index()
    generate_institution_config()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_generate_forms_index.py -v
```

Expected: 6 tests pass

- [ ] **Step 5: Run script against real data and verify output**

```bash
cd /path/to/protocol_manager
python scripts/generate_forms_index.py
python -c "
import json
data = json.load(open('docs/javascripts/protocol-forms-index.json'))
print(f'Protocols: {len(data)}')
print('Sample keys:', list(data[0].keys()))
cfg = json.load(open('docs/javascripts/institution-config.json'))
print('Institution config:', cfg)
"
```

Expected: 87 protocols, all required keys present, institution config has `feedback_url`.

- [ ] **Step 6: Update CI**

Edit `.github/workflows/ci.yml` — add `generate_forms_index.py` step after the existing `generate_sitemap.py` line:

```yaml
      - run: python scripts/generate_comparison_index.py
      - run: python scripts/generate_sitemap.py
      - run: python scripts/generate_forms_index.py
      - run: mkdocs gh-deploy --force
```

- [ ] **Step 7: Commit**

```bash
git add scripts/generate_forms_index.py tests/test_generate_forms_index.py \
    docs/javascripts/protocol-forms-index.json \
    docs/javascripts/institution-config.json \
    .github/workflows/ci.yml
git commit -m "feat: add forms index and institution config generators"
```

---

## Task 2: Shared Protocol Renderer

**Goal:** `scripts/render_protocol.py` — takes a YAML front matter dict and returns the complete Markdown document (front matter + rendered body). Used by the admin app on save so the body is always regenerated from YAML.

**Files:**
- Create: `scripts/render_protocol.py`
- Create: `tests/test_render_protocol.py`

**Acceptance Criteria:**
- [ ] `render_document(fm)` returns a string starting with `---\n`
- [ ] Returned document contains the title as `# Title`
- [ ] Contrast section appears when contrast agent is not N/A
- [ ] No-contrast message appears when contrast agent is N/A
- [ ] Series table rows match fm['series'] list
- [ ] Recons table rows match fm['recons'] list
- [ ] Notes sections contain fm['notes'] values
- [ ] All tests pass

**Verify:** `python -m pytest tests/test_render_protocol.py -v` → all pass

**Steps:**

- [ ] **Step 1: Write failing tests**

Create `tests/test_render_protocol.py`:

```python
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))
from render_protocol import render_document

BASE_FM = {
    'title': 'CT Pulmonary Embolism',
    'slug': 'ct-pulmonary-embolism',
    'category': 'chest',
    'protocol_type': 'contrast-enhanced',
    'last_updated': '2026-01-01',
    'author': '',
    'synonyms': [],
    'clinical_indications': ['Suspected PE', 'Acute dyspnea'],
    'position': 'Supine feet-first',
    'npo': 'NPO 2 hours',
    'premedication': 'None required',
    'contrast': {
        'agent': 'Isovue 370',
        'volume': '1.3 mL/kg',
        'flow_rate': '5 mL/s',
        'duration': '15 - 20s',
        'timing': 'Bolus Tracking',
        'roi': 'Main Pulmonary Artery',
        'trigger': '100 HU',
    },
    'series': [
        {
            'name': 'Pulmonary Angiogram',
            'start': 'Lung apices',
            'end': 'Costophrenic angles',
            'delay': 'Bolus tracked',
            'thickness': '0.625 mm',
            'notes': 'Caudocranial',
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
            'notes': 'Mediastinal window',
        }
    ],
    'notes': {
        'tech': 'Coach breath hold',
        'nursing': '20G IV preferred',
        'rad': 'Assess RV/LV ratio',
        'tips': 'Arms fully raised',
    },
    'safety': {
        'renal': 'Verify eGFR > 30',
        'allergy': 'Check iodine allergy',
    },
}


def test_document_starts_with_frontmatter_fence():
    doc = render_document(BASE_FM)
    assert doc.startswith('---\n')


def test_document_contains_closing_fence_and_body():
    doc = render_document(BASE_FM)
    assert '\n---\n' in doc
    _, body = doc.split('\n---\n', 1)
    assert '# CT Pulmonary Embolism' in body


def test_frontmatter_roundtrips_through_yaml():
    doc = render_document(BASE_FM)
    fm_text = doc.split('\n---\n')[0][4:]  # strip leading '---\n'
    parsed = yaml.safe_load(fm_text)
    assert parsed['slug'] == 'ct-pulmonary-embolism'
    assert parsed['contrast']['agent'] == 'Isovue 370'


def test_contrast_section_rendered_when_present():
    doc = render_document(BASE_FM)
    assert 'Injection Parameters' in doc
    assert 'Isovue 370' in doc
    assert '5 mL/s' in doc


def test_no_contrast_message_when_agent_is_na():
    fm = {**BASE_FM, 'contrast': {'agent': 'N/A'}}
    doc = render_document(fm)
    assert 'No Intravenous Contrast' in doc
    assert 'Injection Parameters' not in doc


def test_series_table_row_present():
    doc = render_document(BASE_FM)
    assert 'Pulmonary Angiogram' in doc
    assert 'Lung apices' in doc


def test_recons_table_row_present():
    doc = render_document(BASE_FM)
    assert '1.25 mm/1.25 mm' in doc
    assert 'Mediastinal window' in doc


def test_clinical_indications_rendered():
    doc = render_document(BASE_FM)
    assert 'Suspected PE' in doc
    assert 'Acute dyspnea' in doc


def test_notes_sections_rendered():
    doc = render_document(BASE_FM)
    assert 'Coach breath hold' in doc
    assert '20G IV preferred' in doc
    assert 'Assess RV/LV ratio' in doc
    assert 'Arms fully raised' in doc


def test_safety_in_nursing_tab():
    doc = render_document(BASE_FM)
    assert 'Verify eGFR > 30' in doc
    assert 'Check iodine allergy' in doc


def test_premedication_pipe_separated_renders_as_bullets():
    fm = {**BASE_FM, 'premedication': 'Metoprolol 5mg IV | Check contraindications'}
    doc = render_document(fm)
    assert 'Metoprolol 5mg IV' in doc
    assert 'Check contraindications' in doc


def test_empty_premedication_renders_none_required():
    fm = {**BASE_FM, 'premedication': ''}
    doc = render_document(fm)
    assert 'None required' in doc
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_render_protocol.py -v
```

Expected: `ModuleNotFoundError: No module named 'render_protocol'`

- [ ] **Step 3: Write the renderer**

Create `scripts/render_protocol.py`:

```python
#!/usr/bin/env python3
"""
Shared Markdown renderer for CT protocol files.

render_document(fm) takes a YAML front matter dict and returns the
complete Markdown document string (YAML front matter block + rendered body).

Used by scripts/admin.py when saving a protocol via the admin UI.
The markdown body is always regenerated from YAML on save — direct
edits to the body below the front matter are overwritten by admin saves.
"""

import yaml


def render_document(fm: dict) -> str:
    """Return full Markdown document (front matter + body) from a YAML fm dict."""
    fm_yaml = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    body = _render_body(fm)
    return f'---\n{fm_yaml}---\n\n{body}'


# ---------------------------------------------------------------------------
# Body renderer
# ---------------------------------------------------------------------------

def _render_body(fm: dict) -> str:
    title = fm.get('title', '')
    last_updated = str(fm.get('last_updated', ''))
    author = fm.get('author', '') or ''
    contrast = fm.get('contrast') or {}
    series_list = fm.get('series') or []
    recons_list = fm.get('recons') or []
    notes = fm.get('notes') or {}
    safety = fm.get('safety') or {}
    indications = fm.get('clinical_indications') or []

    contrast_agent = contrast.get('agent', 'N/A') or 'N/A'
    has_contrast = contrast_agent.upper() not in ('N/A', 'NONE', '')

    # Acquisition summary (compact view in Clinical Summary card)
    acq_summary = '\n'.join(
        f'        | {s.get("name", "")} | {s.get("delay", "")} | {s.get("start", "")} \u2192 {s.get("end", "")} |'
        for s in series_list
    )

    # Clinical indications
    ind_lines = '\n'.join(f'        - {ind}' for ind in indications)

    # Premedication — pipe-separated string → bullet list
    premed_raw = fm.get('premedication', '') or ''
    if premed_raw and premed_raw.lower() not in ('none', 'none required', 'n/a'):
        items = [p.strip() for p in premed_raw.split('|') if p.strip()]
        premed_section = '\n'.join(f'        - {item}' for item in items) if items else '        - None required'
    else:
        premed_section = '        - None required'

    # Contrast section
    if has_contrast:
        contrast_section = f'''
    ===   "Injection Parameters"

        | Parameter | Value |
        |-----------|-------|
        | Agent | {contrast_agent} |
        | Volume | {contrast.get("volume", "")} |
        | Flow Rate | {contrast.get("flow_rate", "")} |
        | Duration | {contrast.get("duration", "")} |
        | Timing Method | {contrast.get("timing", "")} |
        | ROI Placement | {contrast.get("roi", "")} |
        | Trigger (HU) | {contrast.get("trigger", "")} |

    ===   "Lab Requirements"
        Use full dose if GFR > 30
        !!! warning "If GFR < 30"
            **Max Contrast** = \\(2*\\left[\\frac{{\\text{{Patient Weight}}}}{{75 \\text{{ kg}}}} * \\text{{eGFR}}\\right]\\)
'''
    else:
        contrast_section = '''
    !!! info "No Intravenous Contrast"
    This protocol does not require IV contrast administration.
'''

    # Series acquisition table
    series_header = (
        '    | Series Name | Start Location | End Location | Delay | Slice Thickness | Notes |\n'
        '    |:------------|:---------------|:-------------|:------|:----------------|:------|'
    )
    series_rows = '\n'.join(
        f'    | {s.get("name", "")} | {s.get("start", "")} | {s.get("end", "")} '
        f'| {s.get("delay", "")} | {s.get("thickness", "")} | {s.get("notes", "")} |'
        for s in series_list
    )

    # Post-processing table
    recon_header = (
        '    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |\n'
        '    |:------|:------------|:----|:--------------------|:-------|:------------|:------|'
    )
    recon_rows = '\n'.join(
        f'    | {r.get("plane", "")} | {r.get("acquisition", "")} | {r.get("fov", "")} '
        f'| {r.get("thickness_increment", "")} | {r.get("kernel", "")} '
        f'| {r.get("ir_strength", "")} | {r.get("notes", "")} |'
        for r in recons_list
    )

    safety_renal = safety.get('renal', '') or 'N/A'
    safety_allergy = safety.get('allergy', '') or 'N/A'

    return f'''# {title}

**Last Updated:** {last_updated}  
**Author:** {author}

---

<div class="grid cards" markdown>

-   __1. Clinical Summary__

    ---

    === "Acquisition Summary"

        | Series | Phase | Coverage |
        |:-------|:------|:---------|
{acq_summary}

    === "Clinical Indications"

{ind_lines}

-   __2. Patient Prep__

    ---

    - **Position:** {fm.get("position", "")}
    - **NPO Status:** {fm.get("npo", "")}
    - **Pre-Medication:**
{premed_section}

-   __3. IV Contrast & Injection__    

    ---
    {contrast_section}

-   __4. Special Notes__

    ---

    === "Technologist Notes"

        - {notes.get("tech", "")}

    === "Nursing Notes"

        - {notes.get("nursing", "")}

        !!! warning "Safety First"
            - **Renal Function:** {safety_renal}
            - **Allergy:** {safety_allergy}

    === "Radiologist Notes"

        - {notes.get("rad", "")}

    === "Tips & Tricks"

        - {notes.get("tips", "")}

</div>

<div class="acquisition-diagram"></div>

=== "Series Acquisition"

{series_header}
{series_rows}

=== "Post-Processing"

{recon_header}
{recon_rows}

'''
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_render_protocol.py -v
```

Expected: 12 tests pass

- [ ] **Step 5: Smoke test render against a real protocol**

```bash
python -c "
import sys, yaml
sys.path.insert(0, 'scripts')
from render_protocol import render_document

content = open('docs/ct/chest/ct-pulmonary-embolism.md').read()
fm_text = content.split('\n---\n')[0][4:]
fm = yaml.safe_load(fm_text)
doc = render_document(fm)
print(doc[:500])
"
```

Expected: valid Markdown document with front matter block and rendered body.

- [ ] **Step 6: Commit**

```bash
git add scripts/render_protocol.py tests/test_render_protocol.py
git commit -m "feat: add shared protocol markdown renderer"
```

---

## Task 3: Static Change Request Form

**Goal:** A static MkDocs page at `/request-change/` with JS that pre-populates from the forms index (Mode A: change existing, Mode B: new from base), tracks which fields differ, and routes submission to email or GitHub Issues based on `institution-config.json`.

**Files:**
- Create: `docs/request-change.md`
- Create: `docs/javascripts/request-change.js`
- Modify: `docs/.pages` — add `request-change.md` to nav
- Modify: `mkdocs.yml` — add JS files to `extra_javascript`

**Acceptance Criteria:**
- [ ] Page loads at `/request-change/` on the built site
- [ ] `?protocol=ct-pulmonary-embolism` pre-fills all form fields from the forms index
- [ ] `?mode=new` shows base protocol dropdown; selecting a base fills all fields
- [ ] Fields not modified by the user are excluded from the submission payload
- [ ] Mailto routing: if `feedback_url` starts with `mailto:`, clicking submit opens mail client with formatted body
- [ ] GitHub routing: if `feedback_url` starts with `https://github.com`, clicking submit opens GitHub issues/new with pre-filled body
- [ ] Empty `feedback_url`: shows "Contact your protocol lead directly" instead of submit button
- [ ] "Request a Change" button appears on protocol pages (URLs matching `/ct/*/`)

**Verify:** `mkdocs serve` → navigate to `/request-change/?protocol=ct-pulmonary-embolism` → all fields pre-filled. Change one field → submit → mail client or GitHub opens with only the changed field listed.

**Steps:**

- [ ] **Step 1: Create the form page**

Create `docs/request-change.md`:

```markdown
---
title: Request a Protocol Change
---

# Request a Protocol Change

Use this form to request changes to an existing protocol or to propose a new protocol. Your request will be sent to the protocol lead for review.

<div id="rc-app">
  <div id="rc-loading">Loading protocol data…</div>
</div>

<script>
// Bootstrapped by request-change.js — loaded via extra_javascript
</script>
```

- [ ] **Step 2: Add page to nav**

Edit `docs/.pages` — add `request-change.md` after `compare.md`:

```yaml
nav:
  - compare.md
  - request-change.md
  - CT Protocols: ct
```

- [ ] **Step 3: Add JS to mkdocs.yml**

Edit `mkdocs.yml` — add to `extra_javascript` list (after the existing protocol-comparison-index.json line):

```yaml
extra_javascript:
  - javascripts/acquisition-diagram.js
  - javascripts/acquisition-diagram-init.js
  - https://cdn.jsdelivr.net/npm/marked/marked.min.js
  - javascripts/protocol-compare.js
  - javascripts/protocol-comparison-index.json
  - javascripts/protocol-forms-index.json
  - javascripts/institution-config.json
  - javascripts/request-change.js
  - javascripts/mathjax.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

**Note:** MkDocs treats JSON files in `extra_javascript` as `<script src="...">` tags, which causes a parse error for JSON files. Instead, the JS should fetch the JSON files at runtime. Remove `protocol-forms-index.json` and `institution-config.json` from `extra_javascript` — they are fetched via JS fetch() calls, not script tags. The final extra_javascript should be:

```yaml
extra_javascript:
  - javascripts/acquisition-diagram.js
  - javascripts/acquisition-diagram-init.js
  - https://cdn.jsdelivr.net/npm/marked/marked.min.js
  - javascripts/protocol-compare.js
  - javascripts/protocol-comparison-index.json
  - javascripts/request-change.js
  - javascripts/mathjax.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

- [ ] **Step 4: Create the JS — protocol page button injection**

Create `docs/javascripts/request-change.js`. Start with the protocol-page button injection (runs on every page):

```javascript
// =============================================================================
// request-change.js
// Handles:
//   1. "Request a Change" button injection on protocol pages
//   2. Change request form logic on /request-change/
// =============================================================================

(function () {
  'use strict';

  // ---------------------------------------------------------------------------
  // 1. Protocol page button injection
  //    Injects a "Request a Change" link on any page whose URL path contains /ct/
  // ---------------------------------------------------------------------------

  function injectProtocolPageButton() {
    const path = window.location.pathname;
    // Match protocol pages: path contains /ct/ and ends with a slug segment
    if (!/\/ct\/[^/]+\/[^/]+\/?$/.test(path)) return;

    // Extract slug from URL: last non-empty path segment
    const slug = path.replace(/\/$/, '').split('/').pop();
    if (!slug) return;

    // Find the page h1 to insert button after
    const h1 = document.querySelector('article h1');
    if (!h1) return;

    const btn = document.createElement('a');
    btn.href = resolveRequestChangePath(slug);
    btn.textContent = 'Request a Change';
    btn.className = 'md-button md-button--primary rc-request-btn';
    btn.style.cssText = 'margin-top: 0.5rem; margin-bottom: 1rem; display: inline-block; font-size: 0.75rem; padding: 0.3rem 0.8rem;';
    h1.after(btn);
  }

  function resolveRequestChangePath(slug) {
    // Build absolute path to /request-change/?protocol=<slug>
    // Works under any base_path (e.g. /radiology-protocols/)
    const base = window.location.pathname.split('/ct/')[0];
    return `${base}/request-change/?protocol=${slug}`;
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectProtocolPageButton);
  } else {
    injectProtocolPageButton();
  }

  // ---------------------------------------------------------------------------
  // 2. Change request form — only runs on /request-change/ page
  // ---------------------------------------------------------------------------

  const RC_APP_ID = 'rc-app';

  function isRequestChangePage() {
    return !!document.getElementById(RC_APP_ID);
  }

  if (!isRequestChangePage()) return;

  // --- State ---
  let protocolsIndex = [];    // from protocol-forms-index.json
  let institutionConfig = {}; // from institution-config.json
  let baseProtocol = null;    // the protocol used to pre-fill the form
  let mode = 'change';        // 'change' | 'new'

  // --- Bootstrap ---
  async function init() {
    const params = new URLSearchParams(window.location.search);
    mode = params.get('mode') === 'new' ? 'new' : 'change';
    const slugParam = params.get('protocol');

    try {
      [protocolsIndex, institutionConfig] = await Promise.all([
        fetchJSON(resolveJsonPath('protocol-forms-index.json')),
        fetchJSON(resolveJsonPath('institution-config.json')),
      ]);
    } catch (e) {
      showError('Could not load protocol data. Please try refreshing the page.');
      return;
    }

    if (mode === 'change' && slugParam) {
      baseProtocol = protocolsIndex.find(p => p.slug === slugParam) || null;
      if (!baseProtocol) {
        showError(`Protocol "${slugParam}" not found. <a href="?mode=new">Request a new protocol instead?</a>`);
        return;
      }
      renderChangeForm(baseProtocol);
    } else {
      renderNewForm();
    }
  }

  function resolveJsonPath(filename) {
    // Resolve relative to the javascripts directory based on current URL
    const base = window.location.pathname.split('/request-change')[0];
    return `${base}/javascripts/${filename}`;
  }

  async function fetchJSON(url) {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`HTTP ${r.status} fetching ${url}`);
    return r.json();
  }

  function showError(html) {
    document.getElementById(RC_APP_ID).innerHTML =
      `<div class="admonition failure"><p class="admonition-title">Error</p><p>${html}</p></div>`;
  }

  // ---------------------------------------------------------------------------
  // Form rendering — Mode A (change existing)
  // ---------------------------------------------------------------------------

  function renderChangeForm(protocol) {
    const app = document.getElementById(RC_APP_ID);
    app.innerHTML = `
      <p><strong>Protocol:</strong> ${escHtml(protocol.title)}</p>
      <p style="color: var(--md-default-fg-color--light); font-size: 0.85rem;">
        Edit the fields you want changed. Unchanged fields will not be included in the request.
      </p>
      ${buildFormHTML(protocol)}
      ${buildSubmitSection()}
    `;
    attachFormHandlers(protocol);
  }

  // ---------------------------------------------------------------------------
  // Form rendering — Mode B (new protocol)
  // ---------------------------------------------------------------------------

  function renderNewForm() {
    const app = document.getElementById(RC_APP_ID);
    const options = protocolsIndex
      .map(p => `<option value="${escHtml(p.slug)}">${escHtml(p.title)} (${escHtml(p.category)})</option>`)
      .join('');

    app.innerHTML = `
      <div style="margin-bottom: 1.5rem;">
        <label><strong>Base this on an existing protocol:</strong></label><br>
        <select id="rc-base-select" style="margin-top: 0.4rem; width: 100%; max-width: 480px; padding: 0.4rem;">
          <option value="">— Select a base protocol —</option>
          ${options}
        </select>
      </div>
      <div id="rc-new-form-container"></div>
    `;

    document.getElementById('rc-base-select').addEventListener('change', function () {
      const slug = this.value;
      if (!slug) {
        document.getElementById('rc-new-form-container').innerHTML = '';
        return;
      }
      baseProtocol = protocolsIndex.find(p => p.slug === slug);
      const emptyProtocol = JSON.parse(JSON.stringify(baseProtocol));
      emptyProtocol.title = '';
      emptyProtocol.slug = '';
      document.getElementById('rc-new-form-container').innerHTML = `
        <p style="color: var(--md-default-fg-color--light); font-size: 0.85rem;">
          Pre-filled from <strong>${escHtml(baseProtocol.title)}</strong>. Edit fields for the new protocol.
          Title and slug are required.
        </p>
        ${buildFormHTML(emptyProtocol, { showIdentity: true, isNew: true })}
        ${buildSubmitSection()}
      `;
      attachFormHandlers(baseProtocol, { isNew: true });
    });
  }

  // ---------------------------------------------------------------------------
  // Form HTML builder
  // ---------------------------------------------------------------------------

  function buildFormHTML(protocol, opts = {}) {
    const showIdentity = opts.showIdentity || false;
    const isNew = opts.isNew || false;
    const p = protocol;

    const identitySection = showIdentity ? `
      <fieldset class="rc-section">
        <legend>Identity</legend>
        <label>Title <span style="color:red">*</span><br>
          <input type="text" name="title" value="${escHtml(p.title)}" required style="${inputStyle}">
        </label>
        <label>Slug (URL identifier) <span style="color:red">*</span><br>
          <input type="text" name="slug" id="rc-slug" value="${escHtml(p.slug)}" required pattern="[a-z0-9-]+" style="${inputStyle}">
        </label>
        <label>Category<br>
          <select name="category" style="${inputStyle}">
            ${['abdomen','cardiac','chest','msk','neuro','trauma','vascular']
              .map(c => `<option value="${c}" ${p.category === c ? 'selected' : ''}>${c}</option>`).join('')}
          </select>
        </label>
      </fieldset>` : '';

    const contrastAgent = (p.contrast || {}).agent || '';
    const contrast = p.contrast || {};

    return `
      <form id="rc-form" style="max-width: 760px;">
        ${identitySection}

        <fieldset class="rc-section">
          <legend>Clinical</legend>
          <label>Clinical Indications (one per line)<br>
            <textarea name="clinical_indications" rows="4" style="${inputStyle}">${escHtml((p.clinical_indications || []).join('\n'))}</textarea>
          </label>
          <label>Patient Position<br>
            <input type="text" name="position" value="${escHtml(p.position || '')}" style="${inputStyle}">
          </label>
          <label>NPO Status<br>
            <input type="text" name="npo" value="${escHtml(p.npo || '')}" style="${inputStyle}">
          </label>
        </fieldset>

        <fieldset class="rc-section">
          <legend>Preparation</legend>
          <label>Premedication (use | to separate multiple items)<br>
            <textarea name="premedication" rows="3" style="${inputStyle}">${escHtml(p.premedication || '')}</textarea>
          </label>
        </fieldset>

        <fieldset class="rc-section">
          <legend>Contrast</legend>
          <label>Agent<br><input type="text" name="contrast_agent" value="${escHtml(contrastAgent)}" style="${inputStyle}"></label>
          <label>Volume<br><input type="text" name="contrast_volume" value="${escHtml(contrast.volume || '')}" style="${inputStyle}"></label>
          <label>Flow Rate<br><input type="text" name="contrast_flow_rate" value="${escHtml(contrast.flow_rate || '')}" style="${inputStyle}"></label>
          <label>Duration<br><input type="text" name="contrast_duration" value="${escHtml(contrast.duration || '')}" style="${inputStyle}"></label>
          <label>Timing Method<br><input type="text" name="contrast_timing" value="${escHtml(contrast.timing || '')}" style="${inputStyle}"></label>
          <label>ROI Placement<br><input type="text" name="contrast_roi" value="${escHtml(contrast.roi || '')}" style="${inputStyle}"></label>
          <label>Trigger (HU)<br><input type="text" name="contrast_trigger" value="${escHtml(contrast.trigger || '')}" style="${inputStyle}"></label>
        </fieldset>

        <fieldset class="rc-section">
          <legend>Acquisition Series</legend>
          <div id="rc-series-rows">
            ${(p.series || []).map((s, i) => seriesRowHTML(i, s)).join('')}
          </div>
          <button type="button" onclick="rcAddSeriesRow()" style="${btnSecondaryStyle}">+ Add Series</button>
        </fieldset>

        <fieldset class="rc-section">
          <legend>Notes</legend>
          <label>Technologist Notes<br>
            <textarea name="notes_tech" rows="3" style="${inputStyle}">${escHtml((p.notes || {}).tech || '')}</textarea>
          </label>
          <label>Nursing Notes<br>
            <textarea name="notes_nursing" rows="3" style="${inputStyle}">${escHtml((p.notes || {}).nursing || '')}</textarea>
          </label>
          <label>Radiologist Notes<br>
            <textarea name="notes_rad" rows="3" style="${inputStyle}">${escHtml((p.notes || {}).rad || '')}</textarea>
          </label>
          <label>Tips &amp; Tricks<br>
            <textarea name="notes_tips" rows="3" style="${inputStyle}">${escHtml((p.notes || {}).tips || '')}</textarea>
          </label>
        </fieldset>

        <fieldset class="rc-section">
          <legend>Safety</legend>
          <label>Renal<br><input type="text" name="safety_renal" value="${escHtml((p.safety || {}).renal || '')}" style="${inputStyle}"></label>
          <label>Allergy<br><input type="text" name="safety_allergy" value="${escHtml((p.safety || {}).allergy || '')}" style="${inputStyle}"></label>
        </fieldset>

        <fieldset class="rc-section">
          <legend>Additional Notes <span style="font-weight:normal;font-size:0.85rem">(optional)</span></legend>
          <label>Reason / context for this change<br>
            <textarea name="free_text" rows="4" style="${inputStyle}" placeholder="Optional — explain why this change is needed"></textarea>
          </label>
        </fieldset>
      </form>
    `;
  }

  const inputStyle = 'width:100%;max-width:600px;padding:0.4rem;margin-top:0.25rem;box-sizing:border-box;';
  const btnSecondaryStyle = 'margin-top:0.5rem;padding:0.3rem 0.8rem;cursor:pointer;';

  function seriesRowHTML(index, series = {}) {
    return `
      <div class="rc-series-row" data-index="${index}" style="border:1px solid #ddd;padding:0.75rem;margin-bottom:0.5rem;border-radius:4px;">
        <div style="display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:0.5rem;margin-bottom:0.4rem;">
          <input placeholder="Series Name" value="${escHtml(series.name || '')}" style="padding:0.3rem;" data-field="name">
          <input placeholder="Start" value="${escHtml(series.start || '')}" style="padding:0.3rem;" data-field="start">
          <input placeholder="End" value="${escHtml(series.end || '')}" style="padding:0.3rem;" data-field="end">
          <input placeholder="Delay" value="${escHtml(series.delay || '')}" style="padding:0.3rem;" data-field="delay">
          <input placeholder="Thickness" value="${escHtml(series.thickness || '')}" style="padding:0.3rem;" data-field="thickness">
        </div>
        <input placeholder="Notes" value="${escHtml(series.notes || '')}" style="padding:0.3rem;width:100%;" data-field="notes">
        <button type="button" onclick="this.closest('.rc-series-row').remove()" style="margin-top:0.4rem;color:red;background:none;border:none;cursor:pointer;">✕ Remove</button>
      </div>
    `;
  }

  // Make addSeriesRow global so inline onclick can find it
  window.rcAddSeriesRow = function () {
    const container = document.getElementById('rc-series-rows');
    if (!container) return;
    const index = container.querySelectorAll('.rc-series-row').length;
    container.insertAdjacentHTML('beforeend', seriesRowHTML(index));
  };

  // ---------------------------------------------------------------------------
  // Submit section
  // ---------------------------------------------------------------------------

  function buildSubmitSection() {
    const feedbackUrl = institutionConfig.feedback_url || '';
    if (!feedbackUrl) {
      return `<p style="margin-top:1.5rem;"><em>To request a change, contact your protocol lead directly.</em></p>`;
    }
    return `
      <div style="margin-top:1.5rem;">
        <button type="button" id="rc-submit-btn" class="md-button md-button--primary">
          Submit Change Request
        </button>
        <p id="rc-submit-status" style="margin-top:0.5rem;font-size:0.85rem;"></p>
      </div>
    `;
  }

  // ---------------------------------------------------------------------------
  // Form handlers and diff logic
  // ---------------------------------------------------------------------------

  function attachFormHandlers(originalProtocol, opts = {}) {
    const isNew = opts.isNew || false;
    const submitBtn = document.getElementById('rc-submit-btn');
    if (!submitBtn) return;

    submitBtn.addEventListener('click', function () {
      const payload = isNew
        ? buildNewProtocolPayload()
        : buildChangedFieldsPayload(originalProtocol);
      if (!payload) return;
      routeSubmission(payload, isNew);
    });

    // Auto-generate slug from title for new protocols
    if (isNew) {
      const titleInput = document.querySelector('[name="title"]');
      const slugInput = document.getElementById('rc-slug');
      if (titleInput && slugInput) {
        titleInput.addEventListener('input', function () {
          if (!slugInput.dataset.manuallyEdited) {
            slugInput.value = this.value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
          }
        });
        slugInput.addEventListener('input', function () {
          this.dataset.manuallyEdited = 'true';
        });
      }
    }
  }

  function collectSeriesRows() {
    return Array.from(document.querySelectorAll('#rc-series-rows .rc-series-row')).map(row => ({
      name: row.querySelector('[data-field="name"]').value.trim(),
      start: row.querySelector('[data-field="start"]').value.trim(),
      end: row.querySelector('[data-field="end"]').value.trim(),
      delay: row.querySelector('[data-field="delay"]').value.trim(),
      thickness: row.querySelector('[data-field="thickness"]').value.trim(),
      notes: row.querySelector('[data-field="notes"]').value.trim(),
    }));
  }

  function collectFormValues() {
    const form = document.getElementById('rc-form');
    if (!form) return {};
    const fd = new FormData(form);
    return {
      title: fd.get('title') || '',
      slug: fd.get('slug') || '',
      category: fd.get('category') || '',
      position: fd.get('position') || '',
      npo: fd.get('npo') || '',
      premedication: fd.get('premedication') || '',
      clinical_indications: (fd.get('clinical_indications') || '').split('\n').map(s => s.trim()).filter(Boolean),
      contrast: {
        agent: fd.get('contrast_agent') || '',
        volume: fd.get('contrast_volume') || '',
        flow_rate: fd.get('contrast_flow_rate') || '',
        duration: fd.get('contrast_duration') || '',
        timing: fd.get('contrast_timing') || '',
        roi: fd.get('contrast_roi') || '',
        trigger: fd.get('contrast_trigger') || '',
      },
      series: collectSeriesRows(),
      notes: {
        tech: fd.get('notes_tech') || '',
        nursing: fd.get('notes_nursing') || '',
        rad: fd.get('notes_rad') || '',
        tips: fd.get('notes_tips') || '',
      },
      safety: {
        renal: fd.get('safety_renal') || '',
        allergy: fd.get('safety_allergy') || '',
      },
      free_text: fd.get('free_text') || '',
    };
  }

  function buildChangedFieldsPayload(original) {
    const current = collectFormValues();
    const changes = [];

    const flatOriginal = flattenForDiff(original);
    const flatCurrent = flattenForDiff(current);

    for (const [key, originalVal] of Object.entries(flatOriginal)) {
      const currentVal = flatCurrent[key] ?? '';
      const origStr = Array.isArray(originalVal) ? originalVal.join(', ') : String(originalVal);
      const currStr = Array.isArray(currentVal) ? currentVal.join(', ') : String(currentVal);
      if (origStr !== currStr) {
        changes.push({ field: key, from: origStr, to: currStr });
      }
    }

    // Check series diff (simplified: compare JSON)
    const origSeries = JSON.stringify(original.series || []);
    const currSeries = JSON.stringify(current.series || []);
    if (origSeries !== currSeries) {
      changes.push({
        field: 'Series',
        from: formatSeriesSummary(original.series || []),
        to: formatSeriesSummary(current.series || []),
      });
    }

    const freeText = current.free_text.trim();

    if (changes.length === 0 && !freeText) {
      document.getElementById('rc-submit-status').textContent = 'No changes detected.';
      return null;
    }

    return {
      protocol: original.title,
      slug: original.slug,
      isNew: false,
      changes,
      freeText,
    };
  }

  function buildNewProtocolPayload() {
    const current = collectFormValues();
    if (!current.title.trim()) {
      document.getElementById('rc-submit-status').textContent = 'Title is required for a new protocol.';
      return null;
    }
    if (!current.slug.trim()) {
      document.getElementById('rc-submit-status').textContent = 'Slug is required for a new protocol.';
      return null;
    }
    return {
      protocol: current.title,
      slug: current.slug,
      isNew: true,
      basedOn: baseProtocol ? baseProtocol.title : null,
      values: current,
      freeText: current.free_text,
    };
  }

  function flattenForDiff(p) {
    const contrast = p.contrast || {};
    const notes = p.notes || {};
    const safety = p.safety || {};
    return {
      'Clinical Indications': p.clinical_indications || [],
      'Position': p.position || '',
      'NPO': p.npo || '',
      'Premedication': p.premedication || '',
      'Contrast Agent': contrast.agent || '',
      'Contrast Volume': contrast.volume || '',
      'Contrast Flow Rate': contrast.flow_rate || '',
      'Contrast Duration': contrast.duration || '',
      'Contrast Timing': contrast.timing || '',
      'Contrast ROI': contrast.roi || '',
      'Contrast Trigger': contrast.trigger || '',
      'Tech Notes': notes.tech || '',
      'Nursing Notes': notes.nursing || '',
      'Radiologist Notes': notes.rad || '',
      'Tips': notes.tips || '',
      'Safety – Renal': safety.renal || '',
      'Safety – Allergy': safety.allergy || '',
    };
  }

  function formatSeriesSummary(series) {
    return series.map(s => `${s.name} (${s.delay || 'no delay'})`).join('; ') || '(none)';
  }

  // ---------------------------------------------------------------------------
  // Submission routing
  // ---------------------------------------------------------------------------

  function routeSubmission(payload, isNew) {
    const feedbackUrl = institutionConfig.feedback_url || '';
    const body = isNew ? formatNewProtocolBody(payload) : formatChangesBody(payload);

    if (feedbackUrl.startsWith('mailto:')) {
      const subject = isNew
        ? `New Protocol Request: ${payload.protocol}`
        : `Protocol Change Request: ${payload.protocol}`;
      const mailto = `${feedbackUrl}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      window.location.href = mailto;
    } else if (feedbackUrl.includes('github.com')) {
      const title = isNew
        ? `New Protocol Request: ${payload.protocol}`
        : `Protocol Change Request: ${payload.protocol}`;
      const url = `${feedbackUrl}?title=${encodeURIComponent(title)}&body=${encodeURIComponent(body)}`;
      window.open(url, '_blank');
    }
  }

  function formatChangesBody(payload) {
    const lines = [
      `**Protocol:** ${payload.protocol}`,
      `**Slug:** ${payload.slug}`,
      '',
      '## Requested Changes',
      '',
    ];
    for (const ch of payload.changes) {
      lines.push(`**${ch.field}**`);
      lines.push(`- Current: ${ch.from}`);
      lines.push(`- Proposed: ${ch.to}`);
      lines.push('');
    }
    if (payload.freeText) {
      lines.push('## Additional Notes', '', payload.freeText);
    }
    return lines.join('\n');
  }

  function formatNewProtocolBody(payload) {
    const v = payload.values;
    const lines = [
      `**New Protocol Request**`,
      payload.basedOn ? `**Based on:** ${payload.basedOn}` : '',
      '',
      `## Protocol Details`,
      '',
      `**Title:** ${v.title}`,
      `**Slug:** ${v.slug}`,
      `**Category:** ${v.category}`,
      `**Clinical Indications:** ${(v.clinical_indications || []).join(', ')}`,
      `**Position:** ${v.position}`,
      `**NPO:** ${v.npo}`,
      `**Premedication:** ${v.premedication}`,
      '',
      `## Contrast`,
      `Agent: ${v.contrast.agent}, Volume: ${v.contrast.volume}, Flow Rate: ${v.contrast.flow_rate}`,
      `Timing: ${v.contrast.timing}, ROI: ${v.contrast.roi}, Trigger: ${v.contrast.trigger}`,
      '',
      `## Series`,
      formatSeriesSummary(v.series || []),
      '',
      `## Notes`,
      `Tech: ${v.notes.tech}`,
      `Nursing: ${v.notes.nursing}`,
      `Rad: ${v.notes.rad}`,
      `Tips: ${v.notes.tips}`,
      '',
      `## Safety`,
      `Renal: ${v.safety.renal}`,
      `Allergy: ${v.safety.allergy}`,
    ].filter(l => l !== null);

    if (payload.freeText) {
      lines.push('', '## Additional Notes', '', payload.freeText);
    }
    return lines.join('\n');
  }

  // ---------------------------------------------------------------------------
  // Utility
  // ---------------------------------------------------------------------------

  function escHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // Boot
  init();

}());
```

- [ ] **Step 5: Verify form builds and loads**

```bash
cd /path/to/protocol_manager
mkdocs serve
# Open: http://127.0.0.1:8000/radiology-protocols/request-change/?protocol=ct-pulmonary-embolism
# Verify: all fields pre-filled from the protocol
# Open: http://127.0.0.1:8000/radiology-protocols/request-change/?mode=new
# Verify: base protocol dropdown appears; selecting one fills fields
# Open any protocol page (e.g., /ct/chest/ct-pulmonary-embolism/)
# Verify: "Request a Change" button appears below the title
```

- [ ] **Step 6: Commit**

```bash
git add docs/request-change.md docs/javascripts/request-change.js \
    docs/.pages mkdocs.yml
git commit -m "feat: add static change request form and protocol page button"
```

---

## Task 4: Flask Admin App

**Goal:** `scripts/admin.py` — local web app for the protocol lead to list, edit, and create protocols. Reads YAML front matter, presents form-based editor, writes back using `render_document`, runs all index scripts on save.

**Files:**
- Create: `scripts/admin.py`

**Acceptance Criteria:**
- [ ] `python scripts/admin.py` starts Flask on port 5173 and opens browser
- [ ] Protocol list page shows all protocols with title, category, last updated
- [ ] Edit page pre-fills all form fields from the protocol's YAML front matter
- [ ] Saving a protocol rewrites the MD file and runs all three index scripts
- [ ] New protocol page shows base protocol dropdown; selecting base fills all fields
- [ ] Saving a new protocol creates the MD file in the correct `docs/ct/<category>/` directory
- [ ] Slug field on new protocol form auto-generates from title

**Verify:** `python scripts/admin.py` → browser opens → select any protocol → edit a field → save → verify MD file front matter and body are updated → verify `protocol-forms-index.json` is updated.

**Steps:**

- [ ] **Step 1: Create the admin app**

Create `scripts/admin.py`:

```python
#!/usr/bin/env python3
"""
Local admin web app for editing CT protocols.

Usage:
    python scripts/admin.py

Opens http://localhost:5173 automatically.
All changes write to docs/ct/**/*.md and regenerate the index JSON files.
"""

import json
import subprocess
import sys
import webbrowser
from datetime import date
from pathlib import Path
from threading import Timer

import yaml
from flask import Flask, jsonify, redirect, render_template_string, request, url_for

# Import shared renderer — scripts/ is this file's directory
sys.path.insert(0, str(Path(__file__).parent))
from render_protocol import render_document

REPO_ROOT = Path(__file__).parent.parent
DOCS_CT = REPO_ROOT / 'docs' / 'ct'
PORT = 5173

app = Flask(__name__)

CATEGORIES = ['abdomen', 'cardiac', 'chest', 'msk', 'neuro', 'trauma', 'vascular']
INDEX_SCRIPTS = [
    'generate_comparison_index.py',
    'generate_sitemap.py',
    'generate_forms_index.py',
]


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str) -> tuple:
    """Return (fm_dict, body_str) from a Markdown file."""
    if not content.startswith('---\n'):
        return {}, content
    end = content.find('\n---\n', 4)
    if end == -1:
        return {}, content
    try:
        fm = yaml.safe_load(content[4:end]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, content[end + 5:]


def load_all_protocols() -> list:
    """Return list of {filepath: Path, fm: dict} sorted by category then title."""
    protocols = []
    for md_file in sorted(DOCS_CT.rglob('*.md')):
        if md_file.name == 'index.md':
            continue
        fm, _ = parse_frontmatter(md_file.read_text(encoding='utf-8'))
        if not fm:
            continue
        protocols.append({'filepath': md_file, 'fm': fm})
    protocols.sort(key=lambda p: (p['fm'].get('category', ''), p['fm'].get('title', '')))
    return protocols


def find_protocol(slug: str) -> dict | None:
    for p in load_all_protocols():
        if p['fm'].get('slug') == slug:
            return p
    return None


def form_to_frontmatter(form) -> dict:
    """Parse Flask form POST data into a YAML front matter dict."""
    indications = [s.strip() for s in (form.get('indications_json') or '').split('\n') if s.strip()]
    try:
        series = json.loads(form.get('series_json') or '[]')
    except (json.JSONDecodeError, TypeError):
        series = []
    try:
        recons = json.loads(form.get('recons_json') or '[]')
    except (json.JSONDecodeError, TypeError):
        recons = []

    return {
        'title': form.get('title', '').strip(),
        'slug': form.get('slug', '').strip(),
        'category': form.get('category', '').strip(),
        'protocol_type': form.get('protocol_type', '').strip(),
        'last_updated': form.get('last_updated') or str(date.today()),
        'author': form.get('author', '').strip(),
        'synonyms': [],
        'clinical_indications': indications,
        'position': form.get('position', '').strip(),
        'npo': form.get('npo', '').strip(),
        'premedication': form.get('premedication', '').strip(),
        'contrast': {
            'agent': form.get('contrast_agent', '').strip(),
            'volume': form.get('contrast_volume', '').strip(),
            'flow_rate': form.get('contrast_flow_rate', '').strip(),
            'duration': form.get('contrast_duration', '').strip(),
            'timing': form.get('contrast_timing', '').strip(),
            'roi': form.get('contrast_roi', '').strip(),
            'trigger': form.get('contrast_trigger', '').strip(),
        },
        'series': series,
        'recons': recons,
        'notes': {
            'tech': form.get('notes_tech', '').strip(),
            'nursing': form.get('notes_nursing', '').strip(),
            'rad': form.get('notes_rad', '').strip(),
            'tips': form.get('notes_tips', '').strip(),
        },
        'safety': {
            'renal': form.get('safety_renal', '').strip(),
            'allergy': form.get('safety_allergy', '').strip(),
        },
    }


def rebuild_indexes():
    """Run all index generators. Raises subprocess.CalledProcessError on failure."""
    for script in INDEX_SCRIPTS:
        subprocess.run(
            [sys.executable, str(REPO_ROOT / 'scripts' / script)],
            check=True,
            cwd=str(REPO_ROOT),
        )


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

BASE_STYLE = """
<style>
  body { font-family: system-ui, sans-serif; max-width: 960px; margin: 2rem auto; padding: 0 1rem; }
  h1 { font-size: 1.4rem; }
  table { width: 100%; border-collapse: collapse; }
  th, td { text-align: left; padding: 0.5rem 0.75rem; border-bottom: 1px solid #ddd; }
  th { background: #f5f5f5; }
  a { color: #4a6fd4; }
  input, textarea, select { width: 100%; padding: 0.4rem; box-sizing: border-box; margin-top: 0.2rem; }
  label { display: block; margin-bottom: 0.75rem; font-size: 0.9rem; }
  fieldset { border: 1px solid #ddd; padding: 1rem; margin-bottom: 1.5rem; border-radius: 4px; }
  legend { font-weight: bold; padding: 0 0.5rem; }
  .btn { padding: 0.45rem 1rem; background: #4a6fd4; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 0.9rem; }
  .btn-secondary { background: #888; }
  .btn-danger { background: #d44; }
  .row-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 0.5rem; margin-bottom: 0.3rem; }
  .series-row, .recon-row { border: 1px solid #eee; padding: 0.75rem; margin-bottom: 0.5rem; border-radius: 4px; }
  #status-msg { margin-top: 1rem; padding: 0.75rem; border-radius: 4px; display: none; }
  .success { background: #d4edda; color: #155724; }
  .error { background: #f8d7da; color: #721c24; }
  nav { margin-bottom: 1.5rem; font-size: 0.9rem; }
  nav a { margin-right: 1rem; }
</style>
"""

LIST_TEMPLATE = BASE_STYLE + """
<nav><a href="/">Protocol List</a> | <a href="/new">+ New Protocol</a></nav>
<h1>Protocol Manager Admin</h1>
<input type="text" id="search" placeholder="Search protocols…" oninput="filterTable(this.value)"
  style="max-width:400px;margin-bottom:1rem;">
<table id="proto-table">
  <thead><tr><th>Title</th><th>Category</th><th>Last Updated</th><th>Actions</th></tr></thead>
  <tbody>
  {% for p in protocols %}
  <tr data-title="{{ p.fm.title | lower }}">
    <td>{{ p.fm.title }}</td>
    <td>{{ p.fm.category }}</td>
    <td>{{ p.fm.last_updated }}</td>
    <td><a href="/edit/{{ p.fm.slug }}">Edit</a></td>
  </tr>
  {% endfor %}
  </tbody>
</table>
<script>
function filterTable(q) {
  document.querySelectorAll('#proto-table tbody tr').forEach(row => {
    row.style.display = row.dataset.title.includes(q.toLowerCase()) ? '' : 'none';
  });
}
</script>
"""

EDIT_TEMPLATE = BASE_STYLE + """
<nav><a href="/">← Back to List</a></nav>
<h1>Edit: {{ fm.title }}</h1>
<div id="status-msg"></div>
""" + _FORM_TEMPLATE_BODY + """
<script>
""" + _ADMIN_FORM_JS + """
</script>
"""

NEW_TEMPLATE = BASE_STYLE + """
<nav><a href="/">← Back to List</a></nav>
<h1>New Protocol</h1>
<div style="margin-bottom:1.5rem;">
  <label><strong>Base on existing protocol:</strong><br>
    <select id="base-select" onchange="loadBase(this.value)" style="max-width:400px;margin-top:0.4rem;">
      <option value="">— Select a base (optional) —</option>
      {% for p in protocols %}
      <option value="{{ p.fm.slug }}">{{ p.fm.title }} ({{ p.fm.category }})</option>
      {% endfor %}
    </select>
  </label>
</div>
<div id="status-msg"></div>
""" + _FORM_TEMPLATE_BODY + """
<script>
const ALL_PROTOCOLS = {{ protocols_json | safe }};
function loadBase(slug) {
  if (!slug) return;
  const p = ALL_PROTOCOLS.find(x => x.fm.slug === slug);
  if (!p) return;
  const fm = p.fm;
  // Fill identity
  document.getElementById('f-title').value = '';
  document.getElementById('f-slug').value = '';
  document.getElementById('f-category').value = fm.category || '';
  document.getElementById('f-protocol-type').value = fm.protocol_type || '';
  document.getElementById('f-author').value = fm.author || '';
  // Fill clinical
  document.getElementById('f-indications').value = (fm.clinical_indications || []).join('\\n');
  document.getElementById('f-position').value = fm.position || '';
  document.getElementById('f-npo').value = fm.npo || '';
  document.getElementById('f-premed').value = fm.premedication || '';
  // Fill contrast
  const c = fm.contrast || {};
  ['agent','volume','flow_rate','duration','timing','roi','trigger'].forEach(k => {
    const el = document.getElementById('f-contrast-' + k.replace('_','-'));
    if (el) el.value = c[k] || '';
  });
  // Fill series
  renderSeriesRows(fm.series || []);
  renderReconRows(fm.recons || []);
  // Fill notes
  const n = fm.notes || {};
  ['tech','nursing','rad','tips'].forEach(k => {
    const el = document.getElementById('f-notes-' + k);
    if (el) el.value = n[k] || '';
  });
  const s = fm.safety || {};
  document.getElementById('f-safety-renal').value = s.renal || '';
  document.getElementById('f-safety-allergy').value = s.allergy || '';
}
""" + _ADMIN_FORM_JS + """
// Auto-generate slug from title
document.getElementById('f-title').addEventListener('input', function() {
  const slugEl = document.getElementById('f-slug');
  if (!slugEl.dataset.manual) {
    slugEl.value = this.value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/, '');
  }
});
document.getElementById('f-slug').addEventListener('input', function() {
  this.dataset.manual = 'true';
});
</script>
"""
```

Because the templates share form HTML and JS, define them as Python string constants before the templates. Add these constants right after the `CATEGORIES` list:

```python
# Shared form body template (used in both EDIT and NEW pages)
_FORM_TEMPLATE_BODY = """
<form id="admin-form">
  <input type="hidden" id="series_json" name="series_json">
  <input type="hidden" id="recons_json" name="recons_json">

  <fieldset>
    <legend>Identity</legend>
    <label>Title<br><input id="f-title" name="title" value="{{ fm.title }}"></label>
    <label>Slug<br><input id="f-slug" name="slug" value="{{ fm.slug }}"></label>
    <label>Category<br>
      <select id="f-category" name="category">
        {% for cat in categories %}
        <option value="{{ cat }}" {{ 'selected' if fm.category == cat else '' }}>{{ cat }}</option>
        {% endfor %}
      </select>
    </label>
    <label>Protocol Type<br><input id="f-protocol-type" name="protocol_type" value="{{ fm.protocol_type }}"></label>
    <label>Last Updated<br><input id="f-last-updated" name="last_updated" type="date" value="{{ fm.last_updated }}"></label>
    <label>Author<br><input id="f-author" name="author" value="{{ fm.author }}"></label>
  </fieldset>

  <fieldset>
    <legend>Clinical</legend>
    <label>Clinical Indications (one per line)<br>
      <textarea id="f-indications" name="indications_json" rows="4">{{ fm.clinical_indications | join('\n') }}</textarea>
    </label>
    <label>Position<br><input id="f-position" name="position" value="{{ fm.position }}"></label>
    <label>NPO Status<br><input id="f-npo" name="npo" value="{{ fm.npo }}"></label>
  </fieldset>

  <fieldset>
    <legend>Preparation</legend>
    <label>Premedication (use | to separate items)<br>
      <textarea id="f-premed" name="premedication" rows="3">{{ fm.premedication }}</textarea>
    </label>
  </fieldset>

  <fieldset>
    <legend>Contrast</legend>
    {% set c = fm.contrast or {} %}
    <label>Agent<br><input id="f-contrast-agent" name="contrast_agent" value="{{ c.get('agent','') }}"></label>
    <label>Volume<br><input id="f-contrast-volume" name="contrast_volume" value="{{ c.get('volume','') }}"></label>
    <label>Flow Rate<br><input id="f-contrast-flow-rate" name="contrast_flow_rate" value="{{ c.get('flow_rate','') }}"></label>
    <label>Duration<br><input id="f-contrast-duration" name="contrast_duration" value="{{ c.get('duration','') }}"></label>
    <label>Timing Method<br><input id="f-contrast-timing" name="contrast_timing" value="{{ c.get('timing','') }}"></label>
    <label>ROI Placement<br><input id="f-contrast-roi" name="contrast_roi" value="{{ c.get('roi','') }}"></label>
    <label>Trigger (HU)<br><input id="f-contrast-trigger" name="contrast_trigger" value="{{ c.get('trigger','') }}"></label>
  </fieldset>

  <fieldset>
    <legend>Acquisition Series</legend>
    <div id="series-container"></div>
    <button type="button" class="btn btn-secondary" onclick="addSeriesRow()">+ Add Series</button>
  </fieldset>

  <fieldset>
    <legend>Post-Processing (Recons)</legend>
    <div id="recon-container"></div>
    <button type="button" class="btn btn-secondary" onclick="addReconRow()">+ Add Recon</button>
  </fieldset>

  <fieldset>
    <legend>Notes</legend>
    {% set n = fm.notes or {} %}
    <label>Technologist Notes<br><textarea id="f-notes-tech" name="notes_tech" rows="3">{{ n.get('tech','') }}</textarea></label>
    <label>Nursing Notes<br><textarea id="f-notes-nursing" name="notes_nursing" rows="3">{{ n.get('nursing','') }}</textarea></label>
    <label>Radiologist Notes<br><textarea id="f-notes-rad" name="notes_rad" rows="3">{{ n.get('rad','') }}</textarea></label>
    <label>Tips & Tricks<br><textarea id="f-notes-tips" name="notes_tips" rows="3">{{ n.get('tips','') }}</textarea></label>
  </fieldset>

  <fieldset>
    <legend>Safety</legend>
    {% set s = fm.safety or {} %}
    <label>Renal<br><input id="f-safety-renal" name="safety_renal" value="{{ s.get('renal','') }}"></label>
    <label>Allergy<br><input id="f-safety-allergy" name="safety_allergy" value="{{ s.get('allergy','') }}"></label>
  </fieldset>

  <button type="button" class="btn" onclick="submitForm()">Save Protocol</button>
  <a href="/" style="margin-left:1rem;">Cancel</a>
</form>
"""

_ADMIN_FORM_JS = """
// Populate series rows on page load
const INITIAL_SERIES = {{ fm.series | tojson }};
const INITIAL_RECONS = {{ fm.recons | tojson }};
renderSeriesRows(INITIAL_SERIES);
renderReconRows(INITIAL_RECONS);

function renderSeriesRows(series) {
  const c = document.getElementById('series-container');
  c.innerHTML = '';
  (series || []).forEach((s, i) => addSeriesRow(s));
}

function renderReconRows(recons) {
  const c = document.getElementById('recon-container');
  c.innerHTML = '';
  (recons || []).forEach((r, i) => addReconRow(r));
}

function addSeriesRow(s) {
  s = s || {};
  const div = document.createElement('div');
  div.className = 'series-row';
  div.innerHTML = `
    <div class="row-grid">
      <input placeholder="Series Name" value="${esc(s.name||'')}" data-field="name">
      <input placeholder="Start" value="${esc(s.start||'')}" data-field="start">
      <input placeholder="End" value="${esc(s.end||'')}" data-field="end">
      <input placeholder="Delay" value="${esc(s.delay||'')}" data-field="delay">
      <input placeholder="Thickness" value="${esc(s.thickness||'')}" data-field="thickness">
    </div>
    <input placeholder="Notes" value="${esc(s.notes||'')}" data-field="notes" style="width:100%">
    <button type="button" class="btn btn-danger" style="margin-top:0.4rem;padding:0.2rem 0.6rem;"
      onclick="this.closest('.series-row').remove()">Remove</button>
  `;
  document.getElementById('series-container').appendChild(div);
}

function addReconRow(r) {
  r = r || {};
  const div = document.createElement('div');
  div.className = 'recon-row';
  div.innerHTML = `
    <div class="row-grid">
      <input placeholder="Plane" value="${esc(r.plane||'')}" data-field="plane">
      <input placeholder="Acquisition" value="${esc(r.acquisition||'')}" data-field="acquisition">
      <input placeholder="FOV" value="${esc(r.fov||'')}" data-field="fov">
      <input placeholder="Thickness/Inc" value="${esc(r.thickness_increment||'')}" data-field="thickness_increment">
      <input placeholder="Kernel" value="${esc(r.kernel||'')}" data-field="kernel">
    </div>
    <div style="display:grid;grid-template-columns:1fr 2fr;gap:0.5rem;margin-top:0.3rem;">
      <input placeholder="IR Strength" value="${esc(r.ir_strength||'')}" data-field="ir_strength">
      <input placeholder="Notes" value="${esc(r.notes||'')}" data-field="notes">
    </div>
    <button type="button" class="btn btn-danger" style="margin-top:0.4rem;padding:0.2rem 0.6rem;"
      onclick="this.closest('.recon-row').remove()">Remove</button>
  `;
  document.getElementById('recon-container').appendChild(div);
}

function collectRows(containerID, rowClass, fields) {
  return Array.from(document.querySelectorAll('#' + containerID + ' .' + rowClass)).map(row => {
    const obj = {};
    fields.forEach(f => {
      const el = row.querySelector('[data-field="' + f + '"]');
      obj[f] = el ? el.value.trim() : '';
    });
    return obj;
  });
}

function submitForm() {
  const seriesFields = ['name','start','end','delay','thickness','notes'];
  const reconFields = ['plane','acquisition','fov','thickness_increment','kernel','ir_strength','notes'];
  document.getElementById('series_json').value =
    JSON.stringify(collectRows('series-container', 'series-row', seriesFields));
  document.getElementById('recons_json').value =
    JSON.stringify(collectRows('recon-container', 'recon-row', reconFields));

  const form = document.getElementById('admin-form');
  const data = new FormData(form);

  fetch(window.location.pathname, { method: 'POST', body: data })
    .then(r => r.json())
    .then(result => {
      const msg = document.getElementById('status-msg');
      msg.style.display = 'block';
      if (result.success) {
        msg.className = 'success';
        msg.textContent = result.redirect
          ? 'Protocol created successfully! Redirecting…'
          : 'Saved successfully. Indexes regenerated.';
        if (result.redirect) setTimeout(() => window.location.href = result.redirect, 1200);
      } else {
        msg.className = 'error';
        msg.textContent = 'Error: ' + (result.error || 'Unknown error');
      }
    })
    .catch(e => {
      const msg = document.getElementById('status-msg');
      msg.style.display = 'block';
      msg.className = 'error';
      msg.textContent = 'Network error: ' + e.message;
    });
}

function esc(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
"""
```

Continue `admin.py` with the Flask routes:

```python
# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route('/')
def index():
    protocols = load_all_protocols()
    return render_template_string(
        LIST_TEMPLATE,
        protocols=protocols,
    )


@app.route('/edit/<slug>', methods=['GET', 'POST'])
def edit(slug):
    protocol = find_protocol(slug)
    if not protocol:
        return f'Protocol "{slug}" not found.', 404

    if request.method == 'POST':
        fm = form_to_frontmatter(request.form)
        doc = render_document(fm)
        protocol['filepath'].write_text(doc, encoding='utf-8')
        try:
            rebuild_indexes()
            return jsonify({'success': True})
        except subprocess.CalledProcessError as e:
            return jsonify({'success': False, 'error': str(e)})

    fm = protocol['fm']
    return render_template_string(
        EDIT_TEMPLATE,
        fm=fm,
        categories=CATEGORIES,
    )


@app.route('/new', methods=['GET', 'POST'])
def new_protocol():
    protocols = load_all_protocols()

    if request.method == 'POST':
        fm = form_to_frontmatter(request.form)
        slug = fm.get('slug', '').strip()
        category = fm.get('category', '').strip()

        if not slug:
            return jsonify({'success': False, 'error': 'Slug is required'})
        if not category:
            return jsonify({'success': False, 'error': 'Category is required'})

        target_dir = DOCS_CT / category
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / f'{slug}.md'

        if target_path.exists():
            return jsonify({'success': False, 'error': f'Protocol "{slug}" already exists'})

        doc = render_document(fm)
        target_path.write_text(doc, encoding='utf-8')

        try:
            rebuild_indexes()
            return jsonify({'success': True, 'redirect': url_for('edit', slug=slug)})
        except subprocess.CalledProcessError as e:
            return jsonify({'success': False, 'error': str(e)})

    empty_fm = {
        'title': '', 'slug': '', 'category': 'chest', 'protocol_type': '',
        'last_updated': str(date.today()), 'author': '', 'synonyms': [],
        'clinical_indications': [], 'position': '', 'npo': '', 'premedication': '',
        'contrast': {}, 'series': [], 'recons': [],
        'notes': {'tech': '', 'nursing': '', 'rad': '', 'tips': ''},
        'safety': {'renal': '', 'allergy': ''},
    }
    protocols_json = json.dumps([
        {'fm': {k: p['fm'].get(k, '') for k in ['slug', 'title', 'category', 'protocol_type',
          'last_updated', 'author', 'clinical_indications', 'position', 'npo', 'premedication',
          'contrast', 'series', 'recons', 'notes', 'safety']}}
        for p in protocols
    ])
    return render_template_string(
        NEW_TEMPLATE,
        fm=empty_fm,
        categories=CATEGORIES,
        protocols=protocols,
        protocols_json=protocols_json,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def open_browser():
    webbrowser.open(f'http://localhost:{PORT}')


if __name__ == '__main__':
    Timer(0.5, open_browser).start()
    app.run(port=PORT, debug=False)
```

- [ ] **Step 2: Install flask if not present**

```bash
pip show flask || pip install flask
```

- [ ] **Step 3: Smoke test the admin app**

```bash
cd /path/to/protocol_manager
python scripts/admin.py
# Browser opens at http://localhost:5173
# 1. Verify protocol list shows all protocols
# 2. Click Edit on ct-pulmonary-embolism
# 3. Change the NPO field text
# 4. Click Save Protocol
# 5. Verify status shows "Saved successfully"
# 6. Verify docs/ct/chest/ct-pulmonary-embolism.md has the updated NPO value in YAML
# 7. Click "+ New Protocol", select a base, verify fields fill
```

- [ ] **Step 4: Commit**

```bash
git add scripts/admin.py
git commit -m "feat: add Flask admin app for protocol editing"
```

---

## Task 5: Pre-commit Hook and Adoption Guide Update

**Goal:** A shell script hook that auto-regenerates indexes when `docs/ct/` files are staged, a Python installer that installs it to `.git/hooks/pre-commit`, and updated adoption guide docs.

**Files:**
- Create: `scripts/hooks/pre-commit`
- Create: `scripts/install_hooks.py`
- Modify: `docs/for-institutions/adoption-guide.md`

**Acceptance Criteria:**
- [ ] `python scripts/install_hooks.py` copies hook to `.git/hooks/pre-commit` and makes it executable
- [ ] Staging a `docs/ct/*.md` file and running `git commit` triggers the hook
- [ ] Hook runs all three index generators and stages the output JSON files
- [ ] Staging non-protocol files skips the hook silently
- [ ] Adoption guide documents the `install_hooks.py` step

**Verify:** `python scripts/install_hooks.py` → `Installed pre-commit hook`. Then: `touch docs/ct/chest/ct-pulmonary-embolism.md && git add docs/ct/chest/ct-pulmonary-embolism.md && git commit -m "test" --dry-run` → hook output shows "Protocol files changed — regenerating indexes…"

**Steps:**

- [ ] **Step 1: Create the hooks directory and hook script**

```bash
mkdir -p scripts/hooks
```

Create `scripts/hooks/pre-commit`:

```bash
#!/usr/bin/env bash
# Pre-commit hook: regenerates protocol indexes when docs/ct/ files are staged.
# Installed by: python scripts/install_hooks.py

set -e

# Only run if protocol Markdown files are staged
if ! git diff --cached --name-only | grep -q '^docs/ct/.*\.md$'; then
  exit 0
fi

echo "Protocol files changed — regenerating indexes..."

python scripts/generate_comparison_index.py
python scripts/generate_sitemap.py
python scripts/generate_forms_index.py

git add docs/javascripts/protocol-comparison-index.json
git add docs/javascripts/sitemap.json
git add docs/javascripts/protocol-forms-index.json
git add docs/javascripts/institution-config.json

echo "Indexes updated and staged."
```

- [ ] **Step 2: Create the installer**

Create `scripts/install_hooks.py`:

```python
#!/usr/bin/env python3
"""
Install the pre-commit hook for protocol index auto-sync.

Run once after cloning the repo:
    python scripts/install_hooks.py
"""

import shutil
import stat
from pathlib import Path


def install():
    src = Path(__file__).parent / 'hooks' / 'pre-commit'
    dst = Path(__file__).parent.parent / '.git' / 'hooks' / 'pre-commit'

    if not src.exists():
        print(f'ERROR: Hook source not found at {src}')
        return

    if not dst.parent.exists():
        print(f'ERROR: .git/hooks/ not found — are you in a git repository?')
        return

    shutil.copy(src, dst)
    # Make executable for owner, group, other
    current = dst.stat().st_mode
    dst.chmod(current | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    print(f'Installed pre-commit hook → {dst}')
    print('The hook will auto-regenerate JSON indexes when protocol .md files are staged.')


if __name__ == '__main__':
    install()
```

- [ ] **Step 3: Update adoption guide**

Edit `docs/for-institutions/adoption-guide.md` — replace the existing Step 2 "Install Dependencies" section:

```markdown
## Step 2 — Install Dependencies

```bash
pip install mkdocs-material pymdown-extensions mkdocs-awesome-pages-plugin pyyaml flask
```

Then install the pre-commit hook (one-time setup per clone):

```bash
python scripts/install_hooks.py
```

This installs a hook that automatically regenerates the protocol comparison index, sitemap, and forms index whenever you commit changes to `docs/ct/` files. The generated JSON files are staged and included in the same commit automatically.
```

Also update the "Updating Protocols" section at the bottom to replace the note:

```markdown
## Updating Protocols

**Option A — Admin app (recommended):** Run `python scripts/admin.py`. The browser-based interface reads existing protocols, lets you edit all fields through a form, and automatically regenerates all indexes on save.

**Option B — Direct file edit:** Edit the Markdown file at `docs/ct/<category>/<slug>.md` directly. The YAML front matter is the source of truth. If you have the pre-commit hook installed (see Step 2), indexes are regenerated automatically on commit. If not, run:

```bash
python scripts/generate_comparison_index.py
python scripts/generate_sitemap.py
python scripts/generate_forms_index.py
```

Note: Saving via the admin app regenerates the markdown body from YAML. Any manual edits to the body below the front matter will be overwritten on the next admin save.
```

- [ ] **Step 4: Commit**

```bash
git add scripts/hooks/ scripts/install_hooks.py docs/for-institutions/adoption-guide.md
git commit -m "feat: add pre-commit hook, installer, and update adoption guide"
```
