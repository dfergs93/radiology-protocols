# Protocol Submission Form Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a MkDocs-embedded form that lets the author create or clone CT protocols, generates the `.md` file, and shows a live preview — no backend filesystem writes.

**Architecture:** Two new FastAPI endpoints (`GET /api/protocols/{filepath:path}` to parse an existing protocol for cloning, `POST /api/protocols/generate` to render the filled form into markdown). A new `docs/submit.md` page hosts the form. `docs/javascripts/protocol-submit.js` handles all form logic, Gantt building, and preview rendering.

**Tech Stack:** FastAPI + Pydantic (backend), vanilla JS + marked.js + mermaid@10 (frontend), Material MkDocs theme, pytest + httpx (tests)

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Create | `tests/test_protocols.py` | Tests for all new API endpoints |
| Modify | `backend/app.py` | Add Pydantic models + 3 new endpoints |
| Modify | `backend/requirements.txt` | Add `pytest`, `httpx` |
| Create | `docs/submit.md` | MkDocs page with form HTML scaffold |
| Create | `docs/javascripts/protocol-submit.js` | All form logic, Gantt builder, preview |
| Modify | `docs/.pages` | Add `submit.md` to nav |
| Modify | `mkdocs.yml` | Add `protocol-submit.js` to `extra_javascript` |

---

## Task 1: Test Infrastructure + Protocol List Endpoint

**Files:**
- Create: `tests/test_protocols.py`
- Modify: `backend/requirements.txt`

- [ ] **Step 1: Add test dependencies to requirements**

  Edit `backend/requirements.txt` to add:
  ```
  pytest
  httpx
  ```

- [ ] **Step 2: Install them**

  ```bash
  source venv/bin/activate
  pip install pytest httpx
  ```

- [ ] **Step 3: Create test file with TestClient fixture**

  Create `tests/__init__.py` (empty file) and `tests/test_protocols.py`:

  ```python
  import pytest
  import sys
  import os
  sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

  from fastapi.testclient import TestClient
  from app import app

  client = TestClient(app)


  def test_health():
      response = client.get("/api/health")
      assert response.status_code == 200
      assert response.json()["status"] == "ok"


  def test_protocols_list_returns_list():
      response = client.get("/api/protocols")
      assert response.status_code == 200
      data = response.json()
      assert isinstance(data, list)


  def test_protocols_list_entries_have_required_fields():
      response = client.get("/api/protocols")
      assert response.status_code == 200
      data = response.json()
      if data:  # Skip if index is empty
          entry = data[0]
          assert "title" in entry
          assert "filepath" in entry
  ```

- [ ] **Step 4: Run tests — expect health to pass, list tests to fail (endpoint not yet built)**

  ```bash
  cd /Users/duncanferguson/Code/protocol_manager
  source venv/bin/activate
  python -m pytest tests/test_protocols.py::test_health tests/test_protocols.py::test_protocols_list_returns_list -v
  ```
  Expected: `test_health` passes, `test_protocols_list_*` fail with 404 or similar.

- [ ] **Step 5: Add `GET /api/protocols` endpoint to `backend/app.py`**

  After the `PROTOCOL_INDEX` loading block (around line 58), add:

  ```python
  @app.get("/api/protocols")
  async def list_protocols():
      """Return protocol list for submission form dropdown"""
      return PROTOCOL_INDEX
  ```

- [ ] **Step 6: Run list tests — expect pass**

  ```bash
  python -m pytest tests/test_protocols.py::test_protocols_list_returns_list tests/test_protocols.py::test_protocols_list_entries_have_required_fields -v
  ```
  Expected: both PASS.

- [ ] **Step 7: Commit**

  ```bash
  git add tests/__init__.py tests/test_protocols.py backend/requirements.txt backend/app.py
  git commit -m "Add pytest infrastructure and GET /api/protocols list endpoint"
  ```

---

## Task 2: `GET /api/protocols/{filepath:path}` — Parse Protocol for Cloning

**Files:**
- Modify: `backend/app.py` (add endpoint + parser helpers)
- Modify: `tests/test_protocols.py` (add tests)

The endpoint reads a protocol markdown file and returns structured JSON to pre-populate the submission form. It uses regex parsing (same approach as `scripts/generate_comparison_index.py`).

**Note on path handling:** `filepath` comes in as e.g. `ct/cardiac/coronary-cta.md` (relative to `docs/`). The backend resolves it to an absolute path and validates it starts within `docs/ct/` before reading.

**Note on Gantt:** Rather than fully parsing Gantt syntax into rows (which is brittle), the endpoint returns the raw mermaid gantt content as `gantt_raw`. The frontend pre-fills a "raw mermaid" text area when cloning; the user switches to the builder for new row additions.

- [ ] **Step 1: Write failing tests**

  Add to `tests/test_protocols.py`:

  ```python
  def test_load_protocol_path_traversal_blocked():
      response = client.get("/api/protocols/../../backend/app.py")
      assert response.status_code == 403


  def test_load_protocol_not_found():
      response = client.get("/api/protocols/ct/cardiac/nonexistent-protocol.md")
      assert response.status_code == 404


  def test_load_protocol_returns_structured_data():
      # Use a known protocol that exists in the index
      from app import PROTOCOL_INDEX
      if not PROTOCOL_INDEX:
          pytest.skip("No protocols in index")
      filepath = PROTOCOL_INDEX[0]["filepath"]
      response = client.get(f"/api/protocols/{filepath}")
      assert response.status_code == 200
      data = response.json()
      # Required top-level keys
      for key in ["protocol_name", "author", "last_updated", "category", "protocol_type",
                  "clinical_indications", "gantt_raw", "series", "kv", "mas"]:
          assert key in data, f"Missing key: {key}"
  ```

- [ ] **Step 2: Run tests — expect all three to fail (404 on all)**

  ```bash
  python -m pytest tests/test_protocols.py::test_load_protocol_path_traversal_blocked tests/test_protocols.py::test_load_protocol_not_found tests/test_protocols.py::test_load_protocol_returns_structured_data -v
  ```

- [ ] **Step 3: Add the parser helpers and endpoint to `backend/app.py`**

  Add after the existing imports at the top of `app.py`:
  ```python
  import re
  from pathlib import Path
  ```

  Add these constants after `BASE_DIR`:
  ```python
  PROJECT_ROOT = os.path.dirname(BASE_DIR)
  DOCS_CT_DIR = os.path.realpath(os.path.join(PROJECT_ROOT, 'docs', 'ct'))
  ```

  Add parser helpers and endpoint after the `list_protocols` endpoint:

  ```python
  def _parse_protocol_file(content: str) -> dict:
      """Parse a protocol markdown file into structured form data."""
      result = {}

      # Title
      m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
      result['protocol_name'] = m.group(1).strip() if m else ''

      # Author and last updated
      m = re.search(r'\*\*Author:\*\*\s*(.+)', content)
      result['author'] = m.group(1).strip() if m else ''
      m = re.search(r'\*\*Last Updated:\*\*\s*(.+)', content)
      result['last_updated'] = m.group(1).strip() if m else ''

      # Footer: Category and Protocol Type
      m = re.search(r'^Category:\s*(.+)$', content, re.MULTILINE)
      result['category'] = m.group(1).strip() if m else ''
      m = re.search(r'^Protocol Type:\s*(.+)$', content, re.MULTILINE)
      result['protocol_type'] = m.group(1).strip() if m else ''

      # Patient prep
      m = re.search(r'\*\*Position:\*\*\s*(.+)', content)
      result['patient_positioning'] = m.group(1).strip() if m else ''
      m = re.search(r'\*\*NPO Status:\*\*\s*(.+)', content)
      result['npo_status'] = m.group(1).strip() if m else ''

      # Premedication: extract the premedication section if present
      m = re.search(r'\*\*Premedication[^:]*:\*\*\s*(.+?)(?=\n\s*[-*]|\n\n)', content, re.DOTALL)
      result['premedication'] = m.group(1).strip() if m else ''

      # Clinical indications: lines under === "Clinical Indications" tab
      m = re.search(r'=== "Clinical Indications"\s*\n(.*?)(?====|\Z)', content, re.DOTALL)
      if m:
          # Strip leading dashes/bullets and whitespace from each line
          lines = [ln.strip().lstrip('- ').strip() for ln in m.group(1).split('\n')
                   if ln.strip() and not ln.strip().startswith('===')]
          result['clinical_indications'] = '\n'.join(lines)
      else:
          result['clinical_indications'] = ''

      # Acquisition summary table (Series | Phase | Coverage)
      summary = []
      in_table = False
      for line in content.split('\n'):
          if '| Series | Phase | Coverage |' in line:
              in_table = True
              continue
          if in_table and '|:---' in line:
              continue
          if in_table and line.strip() and line.strip().startswith('|'):
              cells = [c.strip() for c in line.split('|') if c.strip()]
              if len(cells) >= 3:
                  summary.append({'series': cells[0], 'phase': cells[1], 'coverage': cells[2]})
          elif in_table:
              break
      result['acquisition_summary'] = summary

      # Injection parameters table
      contrast = {}
      in_table = False
      for line in content.split('\n'):
          if '| Parameter | Value |' in line:
              in_table = True
              continue
          if in_table and '|---' in line:
              continue
          if in_table and line.strip() and line.strip().startswith('|'):
              cells = [c.strip() for c in line.split('|') if c.strip()]
              if len(cells) >= 2:
                  param, value = cells[0].lower(), cells[1]
                  if 'agent' in param:
                      contrast['agent'] = value
                  elif 'volume' in param:
                      contrast['volume'] = value
                  elif 'flow rate' in param:
                      contrast['flow_rate'] = value
                  elif 'timing' in param:
                      contrast['timing_method'] = value
                  elif 'roi' in param:
                      contrast['roi_placement'] = value
                  elif 'trigger' in param:
                      contrast['trigger'] = value
          elif in_table:
              break
      result['contrast_agent'] = contrast.get('agent', '')
      result['contrast_volume'] = contrast.get('volume', '')
      result['contrast_flow_rate'] = contrast.get('flow_rate', '')
      result['contrast_timing_method'] = contrast.get('timing_method', '')
      result['contrast_roi_placement'] = contrast.get('roi_placement', '')
      result['contrast_trigger'] = contrast.get('trigger', '')

      # Lab requirements: content after === "Lab Requirements" tab
      m = re.search(r'=== "Lab Requirements"\s*\n(.*?)(?====|\Z)', content, re.DOTALL)
      result['lab_requirements'] = m.group(1).strip() if m else ''

      # Special notes tabs
      for tab_name, key in [
          ("Technologist Notes", "tech_notes"),
          ("Nursing Notes", "nursing_notes"),
          ("Radiologist Notes", "radiologist_notes"),
          ("Tips & Tricks", "tips_tricks"),
      ]:
          m = re.search(rf'=== "{re.escape(tab_name)}"\s*\n(.*?)(?====|\Z)', content, re.DOTALL)
          result[key] = m.group(1).strip() if m else ''

      # Safety fields from the warning admonition
      m = re.search(r'\*\*Renal Function:\*\*\s*(.+)', content)
      result['safety_renal_function'] = m.group(1).strip() if m else ''
      m = re.search(r'\*\*Allergy[^:]*:\*\*\s*(.+)', content)
      result['safety_allergy'] = m.group(1).strip() if m else ''

      # Gantt: return raw mermaid content string (between gantt keyword and closing ```)
      m = re.search(r'```mermaid\s*\n(.*?)```', content, re.DOTALL)
      result['gantt_raw'] = m.group(1).strip() if m else ''

      # Series acquisition table
      series = []
      in_table = False
      for line in content.split('\n'):
          if '| Series Name |' in line or '| **Series Name** |' in line:
              in_table = True
              continue
          if in_table and '|:---' in line:
              continue
          if in_table and line.strip() and line.strip().startswith('|'):
              cells = [c.strip().replace('**', '') for c in line.split('|') if c.strip()]
              if len(cells) >= 5:
                  series.append({
                      'name': cells[0], 'start': cells[1], 'end': cells[2],
                      'delay': cells[3], 'thickness': cells[4],
                      'notes': cells[5] if len(cells) > 5 else ''
                  })
          elif in_table:
              in_table = False
      result['series'] = series

      # Technical parameters
      tech = {}
      in_table = False
      for line in content.split('\n'):
          if '=== "Technical Parameters"' in line:
              in_table = True
              continue
          if in_table and '| Parameter | Value |' in line:
              continue
          if in_table and '|---' in line:
              continue
          if in_table and line.strip().startswith('|'):
              cells = [c.strip() for c in line.split('|') if c.strip()]
              if len(cells) >= 2:
                  tech[cells[0].lower()] = cells[1]
          elif in_table and line.strip() and not line.strip().startswith('|'):
              in_table = False
      result['kv'] = tech.get('kv', '')
      result['mas'] = tech.get('mas', '')
      result['rotation_time'] = tech.get('rotation time', '').replace('s', '').strip()
      result['pitch'] = tech.get('pitch', '')

      # Post-processing table
      post_proc = []
      in_table = False
      for line in content.split('\n'):
          if '=== "Post-Processing"' in line:
              in_table = True
              continue
          if in_table and '| Plane |' in line:
              continue
          if in_table and '|---' in line:
              continue
          if in_table and line.strip().startswith('|'):
              cells = [c.strip() for c in line.split('|') if c.strip()]
              if len(cells) >= 6:
                  post_proc.append({
                      'plane': cells[0], 'acquisition': cells[1], 'fov': cells[2],
                      'thickness_increment': cells[3], 'kernel': cells[4],
                      'ir_strength': cells[5], 'notes': cells[6] if len(cells) > 6 else ''
                  })
          elif in_table and line.strip() and not line.strip().startswith('|'):
              in_table = False
      result['post_processing'] = post_proc

      # Additional reconstructions: text after the post-processing section
      m = re.search(r'\{additional_recons_section\}|(?<=Post-Processing\n\n)(.*?)(?=\nCategory:)', content, re.DOTALL)
      result['additional_recons'] = ''  # Best effort; hard to extract reliably

      return result


  @app.get("/api/protocols/{filepath:path}")
  async def load_protocol(filepath: str):
      """Load and parse a protocol file for form pre-population"""
      # Resolve and validate path is inside docs/ct/
      candidate = os.path.realpath(os.path.join(PROJECT_ROOT, 'docs', filepath))
      if not candidate.startswith(DOCS_CT_DIR + os.sep) and candidate != DOCS_CT_DIR:
          raise HTTPException(status_code=403, detail="Access denied")
      if not os.path.isfile(candidate):
          raise HTTPException(status_code=404, detail="Protocol not found")

      with open(candidate, 'r', encoding='utf-8') as f:
          content = f.read()

      return _parse_protocol_file(content)
  ```

- [ ] **Step 4: Run the three tests — expect all to pass**

  ```bash
  python -m pytest tests/test_protocols.py::test_load_protocol_path_traversal_blocked tests/test_protocols.py::test_load_protocol_not_found tests/test_protocols.py::test_load_protocol_returns_structured_data -v
  ```
  Expected: all PASS.

- [ ] **Step 5: Commit**

  ```bash
  git add backend/app.py tests/test_protocols.py
  git commit -m "Add GET /api/protocols/{filepath} endpoint with path-traversal protection"
  ```

---

## Task 3: `POST /api/protocols/generate` — Generate Protocol Markdown

**Files:**
- Modify: `backend/app.py` (Pydantic models + endpoint + template helper)
- Modify: `tests/test_protocols.py` (add tests)

Accepts all form fields and renders the `PROTOCOL_TEMPLATE` string from `scripts/protocol_template.py`.

- [ ] **Step 1: Write failing tests**

  Add to `tests/test_protocols.py`:

  ```python
  def test_generate_missing_protocol_name_returns_422():
      response = client.post("/api/protocols/generate", json={})
      assert response.status_code == 422


  def test_generate_invalid_category_returns_422():
      response = client.post("/api/protocols/generate", json={
          "protocol_name": "Test Protocol",
          "author": "Test",
          "last_updated": "2026-03-19",
          "category": "InvalidCategory",
          "protocol_type": "CT",
          "clinical_indications": "Test indication",
          "acquisition_summary": [],
          "patient_positioning": "Supine",
          "npo_status": "None",
          "premedication": "",
          "contrast_agent": "Isovue 370",
          "contrast_volume": "80 mL",
          "contrast_flow_rate": "4 mL/s",
          "contrast_timing_method": "Bolus Tracking",
          "contrast_roi_placement": "Aorta",
          "contrast_trigger": "150 HU",
          "lab_requirements": "",
          "tech_notes": "",
          "nursing_notes": "",
          "radiologist_notes": "",
          "tips_tricks": "",
          "safety_renal_function": "GFR > 30",
          "safety_allergy": "Screen for iodine allergy",
          "gantt_rows": [],
          "gantt_raw": "",
          "series": [],
          "kv": "120",
          "mas": "Auto",
          "rotation_time": "0.5",
          "pitch": "1.375",
          "post_processing": [],
          "additional_recons": ""
      })
      assert response.status_code == 422


  VALID_GENERATE_PAYLOAD = {
      "protocol_name": "Test CTA Chest",
      "author": "Test Author",
      "last_updated": "2026-03-19",
      "category": "Chest",
      "protocol_type": "CTA",
      "clinical_indications": "Pulmonary embolism\nAortic dissection",
      "acquisition_summary": [{"series": "CTA Chest", "phase": "Arterial", "coverage": "Thoracic inlet to diaphragm"}],
      "patient_positioning": "Supine, arms up",
      "npo_status": "None required",
      "premedication": "",
      "contrast_agent": "Isovue 370",
      "contrast_volume": "80 mL",
      "contrast_flow_rate": "4 mL/s",
      "contrast_timing_method": "Bolus Tracking",
      "contrast_roi_placement": "Main pulmonary artery",
      "contrast_trigger": "100 HU",
      "lab_requirements": "GFR if renal history",
      "tech_notes": "Breath hold instructions",
      "nursing_notes": "IV access 20g or larger",
      "radiologist_notes": "Review for PE and aorta",
      "tips_tricks": "Increase flow rate if poor IV access",
      "safety_renal_function": "GFR > 30",
      "safety_allergy": "Screen for iodine allergy",
      "gantt_rows": [
          {"label": "Contrast Injection", "duration_seconds": 20, "type": "contrast", "start": "00:00"},
          {"label": "Saline Chase", "duration_seconds": 8, "type": "saline", "start": "after:contrast_injection"},
          {"label": "CTA Chest", "duration_seconds": 8, "type": "scan", "start": "after:contrast_injection"}
      ],
      "gantt_raw": "",
      "series": [
          {"name": "CTA Chest", "start": "Thoracic inlet", "end": "Diaphragm",
           "delay": "Bolus track 100HU", "thickness": "0.625mm", "notes": ""}
      ],
      "kv": "100",
      "mas": "Auto mA",
      "rotation_time": "0.5",
      "pitch": "1.375",
      "post_processing": [
          {"plane": "Axial", "acquisition": "CTA Chest", "fov": "36cm",
           "thickness_increment": "1.25/1.25", "kernel": "Standard", "ir_strength": "3", "notes": ""}
      ],
      "additional_recons": "Coronal and sagittal MPRs"
  }


  def test_generate_returns_markdown():
      response = client.post("/api/protocols/generate", json=VALID_GENERATE_PAYLOAD)
      assert response.status_code == 200
      data = response.json()
      assert "markdown" in data
      md = data["markdown"]
      assert "# Test CTA Chest" in md
      assert "Category: Chest" in md
      assert "Protocol Type: CTA" in md


  def test_generate_markdown_contains_gantt():
      response = client.post("/api/protocols/generate", json=VALID_GENERATE_PAYLOAD)
      md = response.json()["markdown"]
      assert "gantt" in md
      assert "contrast_injection" in md  # slugified label


  def test_generate_markdown_contains_series_table():
      response = client.post("/api/protocols/generate", json=VALID_GENERATE_PAYLOAD)
      md = response.json()["markdown"]
      assert "CTA Chest" in md
      assert "Thoracic inlet" in md


  def test_generate_empty_clinical_indications_returns_422():
      payload = {**VALID_GENERATE_PAYLOAD, "clinical_indications": ""}
      response = client.post("/api/protocols/generate", json=payload)
      assert response.status_code == 422


  def test_generate_gantt_row_zero_duration_returns_422():
      payload = {**VALID_GENERATE_PAYLOAD, "gantt_rows": [
          {"label": "Contrast", "duration_seconds": 0, "type": "contrast", "start": "00:00"}
      ]}
      response = client.post("/api/protocols/generate", json=payload)
      assert response.status_code == 422


  def test_generate_gantt_no_duplicate_section_scan():
      """Multiple scan rows should only produce one 'section Scan' header"""
      payload = {**VALID_GENERATE_PAYLOAD, "gantt_rows": [
          {"label": "Contrast", "duration_seconds": 20, "type": "contrast", "start": "00:00"},
          {"label": "Scan Phase 1", "duration_seconds": 8, "type": "scan", "start": "after:contrast"},
          {"label": "Scan Phase 2", "duration_seconds": 8, "type": "scan", "start": "after:scan_phase_1"},
      ]}
      response = client.post("/api/protocols/generate", json=payload)
      md = response.json()["markdown"]
      assert md.count("section Scan") == 1
  ```

- [ ] **Step 2: Run tests — expect all to fail**

  ```bash
  python -m pytest tests/test_protocols.py -k "generate" -v
  ```

- [ ] **Step 3: Add Pydantic models and generate endpoint to `backend/app.py`**

  Add imports at top of `app.py` (after existing imports):
  ```python
  import sys
  from typing import Literal, Optional
  from pydantic import Field
  sys.path.insert(0, os.path.join(PROJECT_ROOT, 'scripts'))
  from protocol_template import PROTOCOL_TEMPLATE
  ```

  Add Pydantic models before the endpoints:

  > **Route ordering note:** `GET /api/protocols` (list) must be defined **before** `GET /api/protocols/{filepath:path}` in the file. FastAPI matches routes top-to-bottom and the `{filepath:path}` pattern will match any path including an empty one. Keep this ordering or the list endpoint will be unreachable.

  ```python
  VALID_CATEGORIES = {"Cardiac", "Vascular", "Chest", "Abdomen", "Neuro", "Msk", "Trauma"}

  class AcquisitionSummaryRow(BaseModel):
      series: str
      phase: str
      coverage: str

  class GanttRow(BaseModel):
      label: str
      duration_seconds: int = Field(gt=0)  # spec requires duration > 0
      type: Literal["contrast", "saline", "scan", "other"]
      start: str  # "00:00" for absolute, "after:<slug>" for dependency

  class SeriesRow(BaseModel):
      name: str
      start: str
      end: str
      delay: str
      thickness: str
      notes: str

  class PostProcRow(BaseModel):
      plane: str
      acquisition: str
      fov: str
      thickness_increment: str
      kernel: str
      ir_strength: str
      notes: str

  class ProtocolGenerateRequest(BaseModel):
      protocol_name: str
      author: str
      last_updated: str
      category: str
      protocol_type: str
      clinical_indications: str
      acquisition_summary: list[AcquisitionSummaryRow]
      patient_positioning: str
      npo_status: str
      premedication: str
      contrast_agent: str
      contrast_volume: str
      contrast_flow_rate: str
      contrast_timing_method: str
      contrast_roi_placement: str
      contrast_trigger: str
      lab_requirements: str
      tech_notes: str
      nursing_notes: str
      radiologist_notes: str
      tips_tricks: str
      safety_renal_function: str
      safety_allergy: str
      gantt_rows: list[GanttRow]
      gantt_raw: str  # Used when gantt_rows is empty (cloned raw mermaid)
      series: list[SeriesRow]
      kv: str
      mas: str
      rotation_time: str
      pitch: str
      post_processing: list[PostProcRow]
      additional_recons: str
  ```

  Add template helper functions (add before the generate endpoint):

  ```python
  def _slugify(text: str) -> str:
      """Convert label to mermaid-safe ID"""
      return re.sub(r'[^a-z0-9]+', '_', text.lower()).strip('_')


  def _unique_slugs(rows: list[GanttRow]) -> list[str]:
      """Generate unique slugs for gantt rows, appending numeric suffix on collision"""
      slugs = []
      seen: dict[str, int] = {}
      for row in rows:
          base = _slugify(row.label)
          if base in seen:
              seen[base] += 1
              slugs.append(f"{base}_{seen[base]}")
          else:
              seen[base] = 1
              slugs.append(base)
      return slugs


  def _seconds_to_mmss(seconds: int) -> str:
      return f"{seconds // 60:02d}:{seconds % 60:02d}"


  def _build_gantt_content(rows: list[GanttRow], gantt_raw: str) -> str:
      """Build mermaid gantt task lines. Falls back to gantt_raw if no rows."""
      if not rows:
          return gantt_raw  # raw mermaid content (cloned protocol)
      slugs = _unique_slugs(rows)
      type_to_class = {"contrast": "active", "saline": "active", "scan": "crit", "other": ""}
      lines = ["section Injection"]
      scan_section_added = False  # ensure section header is only inserted once
      for row, slug in zip(rows, slugs):
          cls = type_to_class.get(row.type, "")
          duration_str = _seconds_to_mmss(row.duration_seconds)
          start_str = row.start.replace("after:", "after ") if row.start.startswith("after:") else row.start
          cls_part = f"{cls}, " if cls else ""
          if row.type == "scan" and not scan_section_added:
              lines.append("    section Scan")
              scan_section_added = True
          lines.append(f"      {row.label} :{cls_part}{slug}, {start_str}, {duration_str}")
      return "\n    ".join(lines)


  def _build_acquisition_summary_table(rows: list[AcquisitionSummaryRow]) -> str:
      if not rows:
          return "        | Series | Phase | Coverage |\n        |:---|:---|:---|\n"
      header = "        | Series | Phase | Coverage |\n        |:---|:---|:---|\n"
      body = "".join(f"        | {r.series} | {r.phase} | {r.coverage} |\n" for r in rows)
      return header + body


  def _build_series_table(rows: list[SeriesRow]) -> str:
      header = "    | Series Name | Start | End | Delay | Thickness | Notes |\n    |:---|:---|:---|:---|:---|:---|\n"
      if not rows:
          return header
      body = "".join(
          f"    | **{r.name}** | {r.start} | {r.end} | {r.delay} | {r.thickness} | {r.notes} |\n"
          for r in rows
      )
      return header + body


  def _build_contrast_section(req: 'ProtocolGenerateRequest') -> str:
      # IMPORTANT: The template has 4 spaces before {contrast_section}.
      # Python's .format() prepends those 4 spaces to the FIRST line only.
      # So this function uses 0 spaces on the first line and 4 spaces on all
      # subsequent lines to produce correct and consistent indentation.
      lab = req.lab_requirements or "N/A"
      return (
          '=== "Injection Parameters"\n\n'
          '        | Parameter | Value |\n'
          '        |-----------|-------|\n'
          f'        | Agent | {req.contrast_agent} |\n'
          f'        | Volume | {req.contrast_volume} |\n'
          f'        | Flow Rate | {req.contrast_flow_rate} |\n'
          f'        | Timing Method | {req.contrast_timing_method} |\n'
          f'        | ROI Placement | {req.contrast_roi_placement} |\n'
          f'        | Trigger (HU) | {req.contrast_trigger} |\n\n'
          '    === "Lab Requirements"\n\n'
          f'        {lab}'
      )


  def _build_postproc_table(rows: list[PostProcRow]) -> str:
      header = "    | Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes |\n    |:---|:---|:---|:---|:---|:---|:---|\n"
      if not rows:
          return header
      body = "".join(
          f"    | {r.plane} | {r.acquisition} | {r.fov} | {r.thickness_increment} | {r.kernel} | {r.ir_strength} | {r.notes} |\n"
          for r in rows
      )
      return header + body


  def _format_notes(text: str, indent: str = "        ") -> str:
      if not text:
          return f"{indent}N/A"
      return "\n".join(f"{indent}{line}" for line in text.split('\n'))


  def _format_indications(text: str) -> str:
      if not text:
          return "        - N/A"
      return "\n".join(f"        - {line.strip()}" for line in text.split('\n') if line.strip())


  def _format_premedication(text: str) -> str:
      if not text:
          return ""
      return f"    - **Premedication:** {text}"
  ```

  Add the endpoint (after the helpers):

  ```python
  @app.post("/api/protocols/generate")
  async def generate_protocol(req: ProtocolGenerateRequest):
      """Generate protocol markdown from form fields"""
      # Validate category
      if req.category not in VALID_CATEGORIES:
          raise HTTPException(
              status_code=422,
              detail=[{"loc": ["body", "category"], "msg": f"Must be one of {sorted(VALID_CATEGORIES)}", "type": "value_error"}]
          )
      # Validate clinical indications (spec requirement)
      if not req.clinical_indications.strip():
          raise HTTPException(
              status_code=422,
              detail=[{"loc": ["body", "clinical_indications"], "msg": "At least one clinical indication required", "type": "value_error"}]
          )

      gantt_content = _build_gantt_content(req.gantt_rows, req.gantt_raw)
      additional_recons_section = req.additional_recons.strip() if req.additional_recons.strip() else ""

      markdown = PROTOCOL_TEMPLATE.format(
          protocol_name=req.protocol_name,
          last_updated=req.last_updated,
          author=req.author,
          acquisition_summary_table=_build_acquisition_summary_table(req.acquisition_summary),
          clinical_indications_formatted=_format_indications(req.clinical_indications),
          patient_positioning=req.patient_positioning,
          npo_status=req.npo_status,
          premedication_section=_format_premedication(req.premedication),
          contrast_section=_build_contrast_section(req),
          tech_notes_formatted=_format_notes(req.tech_notes),
          nursing_notes_formatted=_format_notes(req.nursing_notes),
          safety_renal_function=req.safety_renal_function,
          safety_allergy_check=req.safety_allergy,
          radiologist_notes_formatted=_format_notes(req.radiologist_notes),
          artifact_tip_formatted=_format_notes(req.tips_tricks),
          gantt_content=gantt_content,
          series_table=_build_series_table(req.series),
          kv=req.kv,
          mas=req.mas,
          rotation_time=req.rotation_time,
          pitch=req.pitch,
          postproc_table=_build_postproc_table(req.post_processing),
          additional_recons_section=additional_recons_section,
          category=req.category,
          protocol_type=req.protocol_type,
      )

      return {"markdown": markdown}
  ```

- [ ] **Step 4: Run generate tests — expect all to pass**

  ```bash
  python -m pytest tests/test_protocols.py -k "generate" -v
  ```
  Expected: all 5 generate tests PASS.

- [ ] **Step 5: Run full test suite**

  ```bash
  python -m pytest tests/ -v
  ```
  Expected: all tests pass.

- [ ] **Step 6: Commit**

  ```bash
  git add backend/app.py tests/test_protocols.py
  git commit -m "Add POST /api/protocols/generate endpoint with Pydantic validation and template rendering"
  ```

---

## Task 4: MkDocs Page and Nav Registration

**Files:**
- Create: `docs/submit.md`
- Modify: `docs/.pages`
- Modify: `mkdocs.yml`

- [ ] **Step 1: Create `docs/submit.md`**

  ```markdown
  ---
  title: Submit Protocol
  ---

  # Submit Protocol

  <div id="protocol-submit-page">

  <div class="submit-layout">

  <!-- Left: Form -->
  <div class="submit-form-col">

  <div class="submit-base-off">
    <label class="submit-label" for="base-off-input">Base off existing protocol (optional)</label>
    <div class="searchable-select-container" id="base-off-container">
      <input type="text" id="base-off-input" class="searchable-input" placeholder="Search protocols..." autocomplete="off">
      <div class="searchable-dropdown" id="base-off-dropdown" style="display:none;"></div>
    </div>
  </div>

  <nav class="submit-anchor-nav" aria-label="Form sections">
    <a href="#section-metadata">Metadata</a>
    <a href="#section-clinical">Clinical Summary</a>
    <a href="#section-prep">Patient Prep</a>
    <a href="#section-contrast">IV Contrast</a>
    <a href="#section-notes">Special Notes</a>
    <a href="#section-gantt">Gantt Builder</a>
    <a href="#section-series">Series</a>
    <a href="#section-tech">Technical Params</a>
    <a href="#section-postproc">Post-Processing</a>
    <a href="#section-recons">Reconstructions</a>
  </nav>

  <form id="protocol-submit-form" novalidate>

  <section id="section-metadata" class="submit-section">
  <h2>1. Metadata</h2>
  <div class="submit-field"><label>Protocol Name *</label><input type="text" id="field-protocol-name" required></div>
  <div class="submit-field"><label>Author</label><input type="text" id="field-author"></div>
  <div class="submit-field"><label>Last Updated</label><input type="date" id="field-last-updated"></div>
  <div class="submit-field">
    <label>Category</label>
    <select id="field-category">
      <option value="Cardiac">Cardiac</option>
      <option value="Vascular">Vascular</option>
      <option value="Chest">Chest</option>
      <option value="Abdomen">Abdomen</option>
      <option value="Neuro">Neuro</option>
      <option value="Msk">Msk</option>
      <option value="Trauma">Trauma</option>
    </select>
  </div>
  <div class="submit-field"><label>Protocol Type</label><input type="text" id="field-protocol-type"></div>
  </section>

  <section id="section-clinical" class="submit-section">
  <h2>2. Clinical Summary</h2>
  <div class="submit-field">
    <label>Acquisition Summary</label>
    <table class="dynamic-table" id="table-acquisition-summary">
      <thead><tr><th>Series</th><th>Phase</th><th>Coverage</th><th></th></tr></thead>
      <tbody></tbody>
    </table>
    <button type="button" class="add-row-btn" data-table="acquisition-summary">+ Add Row</button>
  </div>
  <div class="submit-field">
    <label>Clinical Indications (one per line)</label>
    <textarea id="field-indications" rows="4" placeholder="e.g. Pulmonary embolism&#10;Aortic dissection"></textarea>
  </div>
  </section>

  <section id="section-prep" class="submit-section">
  <h2>3. Patient Prep</h2>
  <div class="submit-field"><label>Position</label><input type="text" id="field-position" placeholder="e.g. Supine, arms up"></div>
  <div class="submit-field"><label>NPO Status</label><input type="text" id="field-npo" placeholder="e.g. None required"></div>
  <div class="submit-field">
    <label><input type="checkbox" id="toggle-premedication"> Premedication required</label>
    <textarea id="field-premedication" rows="2" style="display:none;margin-top:8px;"></textarea>
  </div>
  </section>

  <section id="section-contrast" class="submit-section">
  <h2>4. IV Contrast &amp; Injection</h2>
  <div class="submit-field"><label>Agent</label><input type="text" id="contrast-agent" placeholder="e.g. Isovue 370"></div>
  <div class="submit-field"><label>Volume</label><input type="text" id="contrast-volume" placeholder="e.g. 80 mL"></div>
  <div class="submit-field"><label>Flow Rate</label><input type="text" id="contrast-flow-rate" placeholder="e.g. 4 mL/s"></div>
  <div class="submit-field"><label>Timing Method</label><input type="text" id="contrast-timing-method" placeholder="e.g. Bolus Tracking"></div>
  <div class="submit-field"><label>ROI Placement</label><input type="text" id="contrast-roi" placeholder="e.g. Aorta at T4"></div>
  <div class="submit-field"><label>Trigger (HU)</label><input type="text" id="contrast-trigger" placeholder="e.g. 150 HU"></div>
  <div class="submit-field"><label>Lab Requirements</label><textarea id="contrast-lab" rows="2"></textarea></div>
  </section>

  <section id="section-notes" class="submit-section">
  <h2>5. Special Notes</h2>
  <div class="submit-field"><label>Technologist Notes</label><textarea id="notes-tech" rows="3"></textarea></div>
  <div class="submit-field"><label>Nursing Notes</label><textarea id="notes-nursing" rows="3"></textarea></div>
  <div class="submit-field"><label>Radiologist Notes</label><textarea id="notes-radiologist" rows="3"></textarea></div>
  <div class="submit-field"><label>Tips &amp; Tricks</label><textarea id="notes-tips" rows="3"></textarea></div>
  <div class="submit-field"><label>Safety — Renal Function</label><input type="text" id="safety-renal" placeholder="e.g. GFR > 30"></div>
  <div class="submit-field"><label>Safety — Allergy Check</label><input type="text" id="safety-allergy" placeholder="e.g. Screen for iodine allergy"></div>
  </section>

  <section id="section-gantt" class="submit-section">
  <h2>6. Gantt Builder</h2>
  <p class="submit-hint">When cloning, the raw mermaid is shown below. Edit it directly, or clear it and use the builder above.</p>
  <div class="submit-field">
    <label>Raw Mermaid (for cloned protocols)</label>
    <textarea id="gantt-raw" rows="6" placeholder="Paste or edit raw mermaid gantt content here..."></textarea>
  </div>
  <div id="gantt-rows-container"></div>
  <button type="button" id="add-gantt-row-btn" class="add-row-btn">+ Add Gantt Row</button>
  </section>

  <section id="section-series" class="submit-section">
  <h2>7. Series Acquisition</h2>
  <table class="dynamic-table" id="table-series">
    <thead><tr><th>Name</th><th>Start</th><th>End</th><th>Delay</th><th>Thickness</th><th>Notes</th><th></th></tr></thead>
    <tbody></tbody>
  </table>
  <button type="button" class="add-row-btn" data-table="series">+ Add Row</button>
  </section>

  <section id="section-tech" class="submit-section">
  <h2>8. Technical Parameters</h2>
  <div class="submit-field"><label>kV</label><input type="text" id="tech-kv" placeholder="e.g. 120"></div>
  <div class="submit-field"><label>mAs</label><input type="text" id="tech-mas" placeholder="e.g. Auto mA"></div>
  <div class="submit-field"><label>Rotation Time (s)</label><input type="text" id="tech-rotation" placeholder="e.g. 0.5"></div>
  <div class="submit-field"><label>Pitch</label><input type="text" id="tech-pitch" placeholder="e.g. 1.375"></div>
  </section>

  <section id="section-postproc" class="submit-section">
  <h2>9. Post-Processing</h2>
  <table class="dynamic-table" id="table-postproc">
    <thead><tr><th>Plane</th><th>Acquisition</th><th>FOV</th><th>Thickness/Increment</th><th>Kernel</th><th>IR Strength</th><th>Notes</th><th></th></tr></thead>
    <tbody></tbody>
  </table>
  <button type="button" class="add-row-btn" data-table="postproc">+ Add Row</button>
  </section>

  <section id="section-recons" class="submit-section">
  <h2>10. Additional Reconstructions</h2>
  <div class="submit-field"><textarea id="field-recons" rows="3" placeholder="e.g. Coronal and sagittal MPRs"></textarea></div>
  </section>

  <div class="submit-actions">
    <button type="button" id="generate-preview-btn" class="md-button md-button--primary">Generate &amp; Preview</button>
  </div>

  </form>
  </div><!-- end submit-form-col -->

  <!-- Right: Preview Panel -->
  <div class="submit-preview-col" id="preview-panel">
  <div class="preview-header">
    <span class="preview-title">Preview</span>
    <button type="button" id="copy-markdown-btn" class="md-button" style="display:none;">Copy Markdown</button>
    <button type="button" id="download-btn" class="md-button" style="display:none;">Download .md</button>
  </div>
  <div id="preview-content" class="preview-content">
    <p class="preview-placeholder">Fill in the form and click <strong>Generate &amp; Preview</strong> to see the rendered protocol here.</p>
  </div>
  </div><!-- end submit-preview-col -->

  </div><!-- end submit-layout -->
  </div><!-- end protocol-submit-page -->
  ```

- [ ] **Step 2: Add `submit.md` to `docs/.pages`**

  First verify the current contents of `docs/.pages` (run `cat docs/.pages`) to ensure no other root-level pages exist beyond `index.md`, `compare.md`, and `CT Protocols: ct`. Then update it to:
  ```yaml
  nav:
    - index.md
    - compare.md
    - submit.md
    - CT Protocols: ct
  ```

- [ ] **Step 3: Add `protocol-submit.js` to `mkdocs.yml`**

  In `mkdocs.yml`, add to `extra_javascript` after `protocoller.js`:
  ```yaml
    - javascripts/protocol-submit.js
  ```

- [ ] **Step 4: Create empty `docs/javascripts/protocol-submit.js` placeholder**

  ```javascript
  // protocol-submit.js — placeholder
  ```

- [ ] **Step 5: Verify MkDocs serves without error**

  ```bash
  cd /Users/duncanferguson/Code/protocol_manager
  source venv/bin/activate
  mkdocs serve &
  sleep 3
  curl -s http://127.0.0.1:8000/submit/ | grep -c "Submit Protocol"
  kill %1
  ```
  Expected: outputs `1` (page found).

- [ ] **Step 6: Commit**

  ```bash
  git add docs/submit.md docs/.pages mkdocs.yml docs/javascripts/protocol-submit.js
  git commit -m "Add submit.md page scaffold and register in nav and mkdocs.yml"
  ```

---

## Task 5: JS — Form Foundation (Base-Off Dropdown + API Base URL)

**Files:**
- Modify: `docs/javascripts/protocol-submit.js`

- [ ] **Step 1: Add form foundation to `protocol-submit.js`**

  Replace the placeholder with:

  ```javascript
  document.addEventListener('DOMContentLoaded', () => {
      // Only run on the submit page
      if (!document.getElementById('protocol-submit-form')) return;

      const API_BASE_URL = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
          ? 'http://localhost:8001'
          : 'https://radiology-protocols.onrender.com';

      // ── Helpers ──────────────────────────────────────────────────────────────

      function slugify(text) {
          return text.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '');
      }

      function secondsToMmss(seconds) {
          const m = Math.floor(seconds / 60);
          const s = seconds % 60;
          return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
      }

      function getVal(id) {
          const el = document.getElementById(id);
          return el ? el.value.trim() : '';
      }

      // ── Set default date ──────────────────────────────────────────────────────
      const dateField = document.getElementById('field-last-updated');
      if (dateField) dateField.value = new Date().toISOString().split('T')[0];

      // ── Base-off searchable dropdown ──────────────────────────────────────────
      let protocolList = [];

      async function loadProtocolList() {
          try {
              const res = await fetch(`${API_BASE_URL}/api/protocols`);
              if (!res.ok) return;
              protocolList = await res.json();
              buildBaseOffDropdown(protocolList);
          } catch (e) {
              console.warn('Could not load protocol list:', e);
          }
      }

      function buildBaseOffDropdown(list) {
          const input = document.getElementById('base-off-input');
          const dropdown = document.getElementById('base-off-dropdown');
          if (!input || !dropdown) return;

          function renderDropdown(filter) {
              const filtered = filter
                  ? list.filter(p => p.title.toLowerCase().includes(filter.toLowerCase()))
                  : list;
              dropdown.innerHTML = filtered.slice(0, 20).map(p =>
                  `<div class="searchable-option" data-filepath="${p.filepath}">${p.title}</div>`
              ).join('');
              dropdown.style.display = filtered.length ? 'block' : 'none';
          }

          input.addEventListener('input', () => renderDropdown(input.value));
          input.addEventListener('focus', () => renderDropdown(input.value));
          input.addEventListener('blur', () => setTimeout(() => { dropdown.style.display = 'none'; }, 150));

          dropdown.addEventListener('click', async (e) => {
              const opt = e.target.closest('.searchable-option');
              if (!opt) return;
              input.value = opt.textContent;
              dropdown.style.display = 'none';
              await loadProtocol(opt.dataset.filepath);
          });
      }

      async function loadProtocol(filepath) {
          try {
              const res = await fetch(`${API_BASE_URL}/api/protocols/${filepath}`);
              if (!res.ok) throw new Error(`HTTP ${res.status}`);
              const data = await res.json();
              populateForm(data);
          } catch (e) {
              console.error('Failed to load protocol:', e);
              alert('Could not load protocol. Is the backend running?');
          }
      }

      loadProtocolList();

      // Populate all form fields from a parsed protocol object
      function populateForm(data) {
          const set = (id, val) => { const el = document.getElementById(id); if (el) el.value = val || ''; };
          set('field-protocol-name', data.protocol_name);
          set('field-author', data.author);
          set('field-last-updated', data.last_updated);
          set('field-category', data.category);
          set('field-protocol-type', data.protocol_type);
          set('field-indications', data.clinical_indications);
          set('field-position', data.patient_positioning);
          set('field-npo', data.npo_status);
          set('field-premedication', data.premedication);
          if (data.premedication) {
              document.getElementById('toggle-premedication').checked = true;
              document.getElementById('field-premedication').style.display = 'block';
          }
          set('contrast-agent', data.contrast_agent);
          set('contrast-volume', data.contrast_volume);
          set('contrast-flow-rate', data.contrast_flow_rate);
          set('contrast-timing-method', data.contrast_timing_method);
          set('contrast-roi', data.contrast_roi_placement);
          set('contrast-trigger', data.contrast_trigger);
          set('contrast-lab', data.lab_requirements);
          set('notes-tech', data.tech_notes);
          set('notes-nursing', data.nursing_notes);
          set('notes-radiologist', data.radiologist_notes);
          set('notes-tips', data.tips_tricks);
          set('safety-renal', data.safety_renal_function);
          set('safety-allergy', data.safety_allergy);
          set('gantt-raw', data.gantt_raw);
          set('tech-kv', data.kv);
          set('tech-mas', data.mas);
          set('tech-rotation', data.rotation_time);
          set('tech-pitch', data.pitch);
          set('field-recons', data.additional_recons);

          // Repopulate dynamic tables
          populateDynamicTable('acquisition-summary',
              (data.acquisition_summary || []).map(r => [r.series, r.phase, r.coverage]));
          populateDynamicTable('series',
              (data.series || []).map(r => [r.name, r.start, r.end, r.delay, r.thickness, r.notes]));
          populateDynamicTable('postproc',
              (data.post_processing || []).map(r => [r.plane, r.acquisition, r.fov, r.thickness_increment, r.kernel, r.ir_strength, r.notes]));
      }

      // ── Premedication toggle ──────────────────────────────────────────────────
      document.getElementById('toggle-premedication').addEventListener('change', function () {
          document.getElementById('field-premedication').style.display = this.checked ? 'block' : 'none';
      });

      // ── Dynamic table rows ────────────────────────────────────────────────────
      const TABLE_COLS = {
          'acquisition-summary': ['Series', 'Phase', 'Coverage'],
          'series': ['Name', 'Start', 'End', 'Delay', 'Thickness', 'Notes'],
          'postproc': ['Plane', 'Acquisition', 'FOV', 'Thickness/Increment', 'Kernel', 'IR Strength', 'Notes'],
      };

      function addTableRow(tableId, values = []) {
          const tbody = document.querySelector(`#table-${tableId} tbody`);
          if (!tbody) return;
          const cols = TABLE_COLS[tableId] || [];
          const tr = document.createElement('tr');
          tr.innerHTML = cols.map((_, i) =>
              `<td><input type="text" value="${(values[i] || '').replace(/"/g, '&quot;')}"></td>`
          ).join('') + '<td><button type="button" class="remove-row-btn" title="Remove">✕</button></td>';
          tr.querySelector('.remove-row-btn').addEventListener('click', () => tr.remove());
          tbody.appendChild(tr);
      }

      function populateDynamicTable(tableId, rows) {
          const tbody = document.querySelector(`#table-${tableId} tbody`);
          if (tbody) tbody.innerHTML = '';
          rows.forEach(r => addTableRow(tableId, r));
      }

      document.querySelectorAll('.add-row-btn[data-table]').forEach(btn => {
          btn.addEventListener('click', () => addTableRow(btn.dataset.table));
      });

      function getTableRows(tableId) {
          const rows = [];
          document.querySelectorAll(`#table-${tableId} tbody tr`).forEach(tr => {
              const cells = [...tr.querySelectorAll('input')].map(i => i.value.trim());
              rows.push(cells);
          });
          return rows;
      }

      // ── Gantt builder ─────────────────────────────────────────────────────────
      let ganttRows = [];

      function addGanttRow(data = {}) {
          const container = document.getElementById('gantt-rows-container');
          const idx = container.children.length;
          const row = document.createElement('div');
          row.className = 'gantt-builder-row';
          row.dataset.idx = idx;

          row.innerHTML = `
              <input type="text" class="gantt-label" placeholder="Label" value="${data.label || ''}">
              <input type="number" class="gantt-duration" placeholder="Duration (s)" min="1" value="${data.duration_seconds || ''}">
              <select class="gantt-type">
                  <option value="contrast" ${data.type === 'contrast' ? 'selected' : ''}>Contrast</option>
                  <option value="saline" ${data.type === 'saline' ? 'selected' : ''}>Saline</option>
                  <option value="scan" ${data.type === 'scan' ? 'selected' : ''}>Scan</option>
                  <option value="other" ${data.type === 'other' ? 'selected' : ''}>Other</option>
              </select>
              <select class="gantt-start">
                  <option value="00:00">At 00:00</option>
              </select>
              <button type="button" class="remove-row-btn" title="Remove">✕</button>
          `;
          row.querySelector('.remove-row-btn').addEventListener('click', () => {
              row.remove();
              refreshGanttStartOptions();
          });
          container.appendChild(row);
          refreshGanttStartOptions();
      }

      function refreshGanttStartOptions() {
          const rows = [...document.querySelectorAll('.gantt-builder-row')];
          rows.forEach((row, i) => {
              const startSelect = row.querySelector('.gantt-start');
              const currentVal = startSelect.value;
              const labels = rows.slice(0, i).map(r => r.querySelector('.gantt-label').value.trim()).filter(Boolean);
              startSelect.innerHTML = '<option value="00:00">At 00:00</option>' +
                  labels.map(l => `<option value="after:${slugify(l)}" ${currentVal === `after:${slugify(l)}` ? 'selected' : ''}>After: ${l}</option>`).join('');
              if (currentVal) startSelect.value = currentVal;
          });
      }

      function getGanttRows() {
          return [...document.querySelectorAll('.gantt-builder-row')].map(row => ({
              label: row.querySelector('.gantt-label').value.trim(),
              duration_seconds: parseInt(row.querySelector('.gantt-duration').value) || 0,
              type: row.querySelector('.gantt-type').value,
              start: row.querySelector('.gantt-start').value,
          })).filter(r => r.label && r.duration_seconds > 0);
      }

      document.getElementById('add-gantt-row-btn').addEventListener('click', () => addGanttRow());

      // Also refresh start options when a label changes
      document.getElementById('gantt-rows-container').addEventListener('input', (e) => {
          if (e.target.classList.contains('gantt-label')) refreshGanttStartOptions();
      });

      // ── Collect all form data into API payload ────────────────────────────────
      function collectFormData() {
          const acqRows = getTableRows('acquisition-summary');
          const seriesRows = getTableRows('series');
          const postprocRows = getTableRows('postproc');

          return {
              protocol_name: getVal('field-protocol-name'),
              author: getVal('field-author'),
              last_updated: getVal('field-last-updated'),
              category: getVal('field-category'),
              protocol_type: getVal('field-protocol-type'),
              clinical_indications: document.getElementById('field-indications').value.trim(),
              acquisition_summary: acqRows.map(r => ({ series: r[0], phase: r[1], coverage: r[2] })),
              patient_positioning: getVal('field-position'),
              npo_status: getVal('field-npo'),
              premedication: document.getElementById('toggle-premedication').checked ? getVal('field-premedication') : '',
              contrast_agent: getVal('contrast-agent'),
              contrast_volume: getVal('contrast-volume'),
              contrast_flow_rate: getVal('contrast-flow-rate'),
              contrast_timing_method: getVal('contrast-timing-method'),
              contrast_roi_placement: getVal('contrast-roi'),
              contrast_trigger: getVal('contrast-trigger'),
              lab_requirements: document.getElementById('contrast-lab').value.trim(),
              tech_notes: document.getElementById('notes-tech').value.trim(),
              nursing_notes: document.getElementById('notes-nursing').value.trim(),
              radiologist_notes: document.getElementById('notes-radiologist').value.trim(),
              tips_tricks: document.getElementById('notes-tips').value.trim(),
              safety_renal_function: getVal('safety-renal'),
              safety_allergy: getVal('safety-allergy'),
              gantt_rows: getGanttRows(),
              gantt_raw: document.getElementById('gantt-raw').value.trim(),
              series: seriesRows.map(r => ({ name: r[0], start: r[1], end: r[2], delay: r[3], thickness: r[4], notes: r[5] || '' })),
              kv: getVal('tech-kv'),
              mas: getVal('tech-mas'),
              rotation_time: getVal('tech-rotation'),
              pitch: getVal('tech-pitch'),
              post_processing: postprocRows.map(r => ({ plane: r[0], acquisition: r[1], fov: r[2], thickness_increment: r[3], kernel: r[4], ir_strength: r[5], notes: r[6] || '' })),
              additional_recons: document.getElementById('field-recons').value.trim(),
          };
      }

      // ── Generate & Preview ────────────────────────────────────────────────────
      let lastMarkdown = '';

      async function generatePreview() {
          const payload = collectFormData();
          if (!payload.protocol_name) {
              alert('Protocol Name is required.');
              document.getElementById('field-protocol-name').focus();
              return;
          }

          const btn = document.getElementById('generate-preview-btn');
          btn.disabled = true;
          btn.textContent = 'Generating…';

          try {
              const res = await fetch(`${API_BASE_URL}/api/protocols/generate`, {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify(payload),
              });
              if (!res.ok) {
                  const err = await res.json().catch(() => ({}));
                  throw new Error(err.detail ? JSON.stringify(err.detail) : `HTTP ${res.status}`);
              }
              const data = await res.json();
              lastMarkdown = data.markdown;
              renderPreview(lastMarkdown, payload.protocol_name);
          } catch (e) {
              console.error('Generate error:', e);
              document.getElementById('preview-content').innerHTML =
                  `<p style="color:red">Error: ${e.message}</p>`;
          } finally {
              btn.disabled = false;
              btn.textContent = 'Generate & Preview';
          }
      }

      function renderPreview(markdown, protocolName) {
          const content = document.getElementById('preview-content');
          // Render markdown to HTML
          content.innerHTML = typeof marked !== 'undefined'
              ? marked.parse(markdown)
              : `<pre>${markdown}</pre>`;

          // Re-render mermaid diagrams
          if (typeof mermaid !== 'undefined') {
              content.querySelectorAll('code.language-mermaid').forEach(block => {
                  const wrapper = document.createElement('div');
                  wrapper.className = 'mermaid';
                  wrapper.textContent = block.textContent;
                  block.parentElement.replaceWith(wrapper);
              });
              mermaid.run({ nodes: content.querySelectorAll('.mermaid') });
          }

          // Show copy/download buttons
          document.getElementById('copy-markdown-btn').style.display = 'inline-block';
          document.getElementById('download-btn').style.display = 'inline-block';
          document.getElementById('download-btn').dataset.name = `${slugify(protocolName)}.md`;
      }

      document.getElementById('generate-preview-btn').addEventListener('click', generatePreview);

      document.getElementById('copy-markdown-btn').addEventListener('click', () => {
          navigator.clipboard.writeText(lastMarkdown).then(() => {
              const btn = document.getElementById('copy-markdown-btn');
              btn.textContent = 'Copied!';
              setTimeout(() => { btn.textContent = 'Copy Markdown'; }, 2000);
          });
      });

      document.getElementById('download-btn').addEventListener('click', () => {
          const filename = document.getElementById('download-btn').dataset.name || 'protocol.md';
          const blob = new Blob([lastMarkdown], { type: 'text/markdown' });
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = filename;
          a.click();
          URL.revokeObjectURL(a.href);
      });

  }); // end DOMContentLoaded
  ```

- [ ] **Step 2: Verify no JS syntax errors**

  ```bash
  node --check docs/javascripts/protocol-submit.js
  ```
  Expected: no output (no errors).

- [ ] **Step 3: Commit**

  ```bash
  git add docs/javascripts/protocol-submit.js
  git commit -m "Add protocol-submit.js with form logic, Gantt builder, and generate/preview"
  ```

---

## Task 6: CSS for Two-Column Layout and Form Styling

**Files:**
- Modify: `docs/custom_css/extra.css`

- [ ] **Step 1: Add submit form styles to the end of `docs/custom_css/extra.css`**

  Append to `docs/custom_css/extra.css`:

  ```css
  /* ── Protocol Submit Form ──────────────────────────────────────────────────── */

  .submit-layout {
      display: flex;
      gap: 24px;
      align-items: flex-start;
  }

  .submit-form-col {
      flex: 0 0 60%;
      min-width: 0;
  }

  .submit-preview-col {
      flex: 0 0 38%;
      position: sticky;
      top: 80px;
      max-height: calc(100vh - 100px);
      overflow-y: auto;
      border: 1px solid var(--md-default-fg-color--lightest);
      border-radius: 8px;
      background: var(--md-default-bg-color);
  }

  .submit-anchor-nav {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 24px;
      padding: 12px;
      background: var(--md-default-fg-color--lightest);
      border-radius: 6px;
  }

  .submit-anchor-nav a {
      font-size: 0.75rem;
      padding: 4px 10px;
      border-radius: 4px;
      background: var(--md-default-bg-color);
      color: var(--md-primary-fg-color);
      text-decoration: none;
      border: 1px solid var(--md-primary-fg-color);
      transition: background 0.15s;
  }

  .submit-anchor-nav a:hover {
      background: var(--md-primary-fg-color);
      color: var(--md-primary-bg-color);
  }

  .submit-section {
      margin-bottom: 32px;
      padding: 20px;
      border: 1px solid var(--md-default-fg-color--lightest);
      border-radius: 8px;
  }

  .submit-section h2 {
      margin-top: 0;
      font-size: 1rem;
      color: var(--md-primary-fg-color);
      border-bottom: 1px solid var(--md-default-fg-color--lightest);
      padding-bottom: 8px;
      margin-bottom: 16px;
  }

  .submit-field {
      margin-bottom: 14px;
  }

  .submit-field label {
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      margin-bottom: 4px;
      color: var(--md-default-fg-color);
  }

  .submit-field input[type="text"],
  .submit-field input[type="date"],
  .submit-field input[type="number"],
  .submit-field select,
  .submit-field textarea {
      width: 100%;
      padding: 8px 10px;
      border: 1px solid var(--md-default-fg-color--lighter);
      border-radius: 4px;
      background: var(--md-default-bg-color);
      color: var(--md-default-fg-color);
      font-size: 0.9rem;
      font-family: inherit;
      box-sizing: border-box;
  }

  .submit-field input:focus,
  .submit-field select:focus,
  .submit-field textarea:focus {
      outline: 2px solid var(--md-primary-fg-color);
      outline-offset: 1px;
  }

  .submit-base-off {
      margin-bottom: 24px;
      padding: 16px;
      background: var(--md-accent-fg-color--transparent, rgba(var(--md-accent-fg-color--rgb), 0.1));
      border-radius: 8px;
      border: 1px dashed var(--md-primary-fg-color);
  }

  .submit-label {
      display: block;
      font-weight: 700;
      margin-bottom: 8px;
  }

  .dynamic-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      margin-bottom: 8px;
  }

  .dynamic-table th {
      background: var(--md-default-fg-color--lightest);
      padding: 6px 8px;
      text-align: left;
      font-weight: 600;
  }

  .dynamic-table td {
      padding: 4px;
      border-bottom: 1px solid var(--md-default-fg-color--lightest);
  }

  .dynamic-table td input {
      width: 100%;
      padding: 4px 6px;
      border: 1px solid var(--md-default-fg-color--lighter);
      border-radius: 3px;
      background: var(--md-default-bg-color);
      color: var(--md-default-fg-color);
      font-size: 0.85rem;
      box-sizing: border-box;
  }

  .add-row-btn, .remove-row-btn {
      cursor: pointer;
      border: none;
      border-radius: 4px;
      font-size: 0.8rem;
      padding: 4px 10px;
  }

  .add-row-btn {
      background: var(--md-primary-fg-color);
      color: var(--md-primary-bg-color);
      margin-top: 4px;
  }

  .remove-row-btn {
      background: transparent;
      color: var(--md-default-fg-color--light);
      font-size: 1rem;
      line-height: 1;
  }

  .remove-row-btn:hover { color: red; }

  .gantt-builder-row {
      display: flex;
      gap: 8px;
      align-items: center;
      margin-bottom: 8px;
      padding: 8px;
      border: 1px solid var(--md-default-fg-color--lightest);
      border-radius: 4px;
  }

  .gantt-builder-row input[type="text"],
  .gantt-builder-row input[type="number"],
  .gantt-builder-row select {
      padding: 6px 8px;
      border: 1px solid var(--md-default-fg-color--lighter);
      border-radius: 4px;
      background: var(--md-default-bg-color);
      color: var(--md-default-fg-color);
      font-size: 0.85rem;
  }

  .gantt-builder-row .gantt-label { flex: 2; }
  .gantt-builder-row .gantt-duration { flex: 0 0 90px; }
  .gantt-builder-row .gantt-type,
  .gantt-builder-row .gantt-start { flex: 1; }

  .submit-hint {
      font-size: 0.8rem;
      color: var(--md-default-fg-color--light);
      margin-bottom: 8px;
  }

  .submit-actions {
      margin-top: 24px;
      padding: 16px 0;
  }

  .submit-actions button {
      font-size: 1rem;
      padding: 10px 28px;
  }

  .preview-header {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 12px 16px;
      border-bottom: 1px solid var(--md-default-fg-color--lightest);
      background: var(--md-primary-fg-color);
      color: var(--md-primary-bg-color);
      border-radius: 8px 8px 0 0;
  }

  .preview-title {
      font-weight: 700;
      flex: 1;
  }

  .preview-content {
      padding: 16px;
      font-size: 0.9rem;
  }

  .preview-placeholder {
      color: var(--md-default-fg-color--light);
      text-align: center;
      padding: 40px 20px;
  }

  /* Dark mode adjustments */
  [data-md-color-scheme="slate"] .submit-section,
  [data-md-color-scheme="slate"] .submit-preview-col {
      border-color: rgba(255,255,255,0.1);
  }

  /* Mobile: stack columns */
  @media (max-width: 900px) {
      .submit-layout {
          flex-direction: column;
      }
      .submit-form-col,
      .submit-preview-col {
          flex: none;
          width: 100%;
      }
      .submit-preview-col {
          position: static;
          max-height: 600px;
      }
  }
  ```

- [ ] **Step 2: Commit**

  ```bash
  git add docs/custom_css/extra.css
  git commit -m "Add two-column layout and form styling for protocol submit page"
  ```

- [ ] **Step 3: Serve the site and verify the submit page renders correctly**

  ```bash
  cd /Users/duncanferguson/Code/protocol_manager
  source venv/bin/activate
  mkdocs serve
  ```
  Open `http://127.0.0.1:8000/submit/` in browser. Verify:
  - Two-column layout (form left, preview panel right)
  - Anchor nav visible with all 10 section links
  - "Base off existing protocol" search box visible at top
  - All 10 form sections visible and styled

---

## Task 7: End-to-End Manual Smoke Test

**No code changes — verify the full flow works.**

- [ ] **Step 1: Start the backend**

  ```bash
  cd /Users/duncanferguson/Code/protocol_manager
  source venv/bin/activate
  python backend/app.py
  ```

- [ ] **Step 2: Start MkDocs (separate terminal)**

  ```bash
  cd /Users/duncanferguson/Code/protocol_manager
  source venv/bin/activate
  mkdocs serve
  ```

- [ ] **Step 3: Open `http://127.0.0.1:8000/submit/` and verify:**

  - [ ] "Base off existing protocol" dropdown populates with protocol list on focus
  - [ ] Selecting a protocol fills all form fields
  - [ ] Gantt raw mermaid text area is populated from the loaded protocol
  - [ ] "Add Gantt Row" adds a row; row removal works; start options update when labels change
  - [ ] Dynamic table rows add/remove correctly for Acquisition Summary, Series, Post-Processing
  - [ ] "Generate & Preview" with an empty protocol name shows an alert
  - [ ] "Generate & Preview" with valid data calls the API and renders markdown in the preview panel
  - [ ] Gantt diagram renders via Mermaid in the preview
  - [ ] "Copy Markdown" copies to clipboard
  - [ ] "Download .md" triggers a file download

- [ ] **Step 4: Run full test suite one final time**

  ```bash
  python -m pytest tests/ -v
  ```
  Expected: all tests pass.

- [ ] **Step 5: Update `TODO.md` to mark item 5 tasks as complete**

  In `TODO.md`, mark all five sub-items under section 5 as `[x]`.

- [ ] **Step 6: Final commit**

  ```bash
  git add TODO.md
  git commit -m "Mark protocol submission form todos as complete after smoke test"
  ```
