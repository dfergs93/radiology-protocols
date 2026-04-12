"""admin.py — Flask admin app for editing CT protocol Markdown files.

Run with:
    python scripts/admin.py
from the repo root.
"""

from __future__ import annotations

import base64
import json
import subprocess
import sys
import webbrowser
from datetime import date
from pathlib import Path

import yaml
from flask import Flask, jsonify, redirect, render_template_string, request, url_for

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
DOCS_CT = REPO_ROOT / "docs" / "ct"
SCRIPTS_DIR = REPO_ROOT / "scripts"

sys.path.insert(0, str(SCRIPTS_DIR))
from render_protocol import render_document  # noqa: E402

app = Flask(__name__)

CATEGORIES = ["abdomen", "cardiac", "chest", "msk", "neuro", "trauma", "vascular"]

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Return (fm_dict, body_str) or ({}, content) if no front matter."""
    if not content.startswith("---"):
        return {}, content
    # Find closing ---
    end = content.find("\n---\n", 3)
    if end == -1:
        # Try end of file variant
        end = content.find("\n---", 3)
        if end == -1:
            return {}, content
    yaml_str = content[3:end].strip()
    body = content[end + 4:]
    try:
        fm = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


def load_all_protocols() -> list[dict]:
    """Return [{filepath: Path, fm: dict}] sorted by (category, title)."""
    results = []
    for md_file in DOCS_CT.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            fm, _ = parse_frontmatter(content)
            if fm:
                results.append({"filepath": md_file, "fm": fm})
        except Exception:
            pass
    results.sort(key=lambda x: (x["fm"].get("category", ""), x["fm"].get("title", "")))
    return results


def find_protocol(slug: str) -> dict | None:
    """Find protocol by slug from load_all_protocols()."""
    for item in load_all_protocols():
        if item["fm"].get("slug") == slug:
            return item
    return None


def form_to_frontmatter(form) -> dict:
    """Parse Flask form POST data into YAML fm dict."""
    indications_raw = form.get("indications_json", "")
    indications = [line.strip() for line in indications_raw.splitlines() if line.strip()]

    series_raw = form.get("series_json", "[]")
    try:
        series = json.loads(series_raw)
    except (json.JSONDecodeError, ValueError):
        series = []

    recons_raw = form.get("recons_json", "[]")
    try:
        recons = json.loads(recons_raw)
    except (json.JSONDecodeError, ValueError):
        recons = []

    last_updated = form.get("last_updated", "").strip()
    if not last_updated:
        last_updated = str(date.today())

    synonyms_raw = form.get("synonyms", "")
    synonyms = [s.strip() for s in synonyms_raw.splitlines() if s.strip()]

    fm = {
        "title": form.get("title", "").strip(),
        "slug": form.get("slug", "").strip(),
        "category": form.get("category", "").strip(),
        "protocol_type": form.get("protocol_type", "").strip(),
        "last_updated": last_updated,
        "author": form.get("author", "").strip(),
        "synonyms": synonyms,
        "clinical_indications": indications,
        "position": form.get("position", "").strip(),
        "npo": form.get("npo", "").strip(),
        "premedication": form.get("premedication", "").strip(),
        "contrast": {
            "agent": form.get("contrast_agent", "").strip(),
            "volume": form.get("contrast_volume", "").strip(),
            "flow_rate": form.get("contrast_flow_rate", "").strip(),
            "duration": form.get("contrast_duration", "").strip(),
            "timing": form.get("contrast_timing", "").strip(),
            "roi": form.get("contrast_roi", "").strip(),
            "trigger": form.get("contrast_trigger", "").strip(),
        },
        "series": series,
        "recons": recons,
        "notes": {
            "tech": form.get("notes_tech", "").strip(),
            "nursing": form.get("notes_nursing", "").strip(),
            "rad": form.get("notes_rad", "").strip(),
            "tips": form.get("notes_tips", "").strip(),
        },
        "safety": {
            "renal": form.get("safety_renal", "").strip(),
            "allergy": form.get("safety_allergy", "").strip(),
        },
    }
    return fm


def apply_changes_to_fm(fm: dict, changes: dict) -> tuple[dict, set]:
    """Overlay a flat changesMap (field_name -> value) onto an fm dict.

    Returns (updated_fm, highlighted_fields) where highlighted_fields is the set
    of form field names that were changed.
    """
    CONTRAST_FIELDS = {
        "contrast_agent": "agent", "contrast_volume": "volume",
        "contrast_flow_rate": "flow_rate", "contrast_duration": "duration",
        "contrast_timing": "timing", "contrast_roi": "roi", "contrast_trigger": "trigger",
    }
    NOTES_FIELDS = {
        "notes_tech": "tech", "notes_nursing": "nursing",
        "notes_rad": "rad", "notes_tips": "tips",
    }
    SAFETY_FIELDS = {"safety_renal": "renal", "safety_allergy": "allergy"}

    highlighted = set()
    for key, value in changes.items():
        if key in CONTRAST_FIELDS:
            fm.setdefault("contrast", {})[CONTRAST_FIELDS[key]] = value
            highlighted.add(key)
        elif key in NOTES_FIELDS:
            fm.setdefault("notes", {})[NOTES_FIELDS[key]] = value
            highlighted.add(key)
        elif key in SAFETY_FIELDS:
            fm.setdefault("safety", {})[SAFETY_FIELDS[key]] = value
            highlighted.add(key)
        elif key == "indications_json":
            fm["clinical_indications"] = [l.strip() for l in value.splitlines() if l.strip()]
            highlighted.add(key)
        elif key == "series_json":
            try:
                fm["series"] = json.loads(value)
            except (json.JSONDecodeError, ValueError):
                pass
            highlighted.add(key)
        elif key in ("title", "category", "protocol_type", "position", "npo", "premedication", "author"):
            fm[key] = value
            highlighted.add(key)
    return fm, highlighted


def rebuild_indexes() -> list[str]:
    """Run index-generation scripts via subprocess. Returns list of failure messages."""
    scripts = [
        "generate_comparison_index.py",
        "generate_sitemap.py",
        "generate_forms_index.py",
    ]
    failures = []
    for script in scripts:
        script_path = SCRIPTS_DIR / script
        if script_path.exists():
            try:
                result = subprocess.run(
                    [sys.executable, str(script_path)],
                    cwd=str(REPO_ROOT),
                    timeout=30,
                    check=False,
                    capture_output=True,
                    text=True,
                )
                if result.returncode != 0:
                    failures.append(f"{script} failed: {result.stderr.strip() or 'non-zero exit'}")
            except Exception as exc:
                failures.append(f"{script} error: {exc}")
    return failures


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

LIST_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Protocol Manager Admin</title>
<style>
  *, *::before, *::after { box-sizing: border-box; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
         margin: 0; background: #f5f5f5; color: #222; }
  .navbar { background: #1a237e; color: white; padding: 0.75rem 1.5rem;
            display: flex; align-items: center; justify-content: space-between; }
  .navbar h1 { margin: 0; font-size: 1.25rem; font-weight: 600; }
  .btn { display: inline-block; padding: 0.45rem 1rem; border-radius: 4px;
         text-decoration: none; font-size: 0.9rem; cursor: pointer; border: none; }
  .btn-primary { background: #1565c0; color: white; }
  .btn-primary:hover { background: #0d47a1; }
  .btn-sm { padding: 0.3rem 0.7rem; font-size: 0.82rem; }
  .btn-outline { background: transparent; border: 1px solid #1565c0;
                 color: #1565c0; }
  .btn-outline:hover { background: #e3f2fd; }
  .content { max-width: 1100px; margin: 1.5rem auto; padding: 0 1rem; }
  .search-bar { margin-bottom: 1rem; }
  .search-bar input { width: 100%; padding: 0.5rem 0.75rem; border: 1px solid #ccc;
                      border-radius: 4px; font-size: 1rem; }
  table { width: 100%; border-collapse: collapse; background: white;
          border-radius: 6px; overflow: hidden;
          box-shadow: 0 1px 3px rgba(0,0,0,.1); }
  th { background: #e8eaf6; text-align: left; padding: 0.7rem 1rem;
       font-size: 0.85rem; text-transform: uppercase; letter-spacing: .04em; }
  td { padding: 0.65rem 1rem; border-bottom: 1px solid #f0f0f0; font-size: 0.95rem; }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #fafafa; }
  .badge { display: inline-block; padding: 0.2em 0.6em; border-radius: 3px;
           font-size: 0.78rem; font-weight: 600; background: #e8eaf6; color: #3949ab; }
  .count { color: #777; font-size: 0.9rem; margin-bottom: 0.5rem; }
</style>
</head>
<body>
<nav class="navbar">
  <h1>Protocol Manager Admin</h1>
  <a href="/new" class="btn btn-primary">+ New Protocol</a>
</nav>
<div class="content">
  <div class="search-bar">
    <input type="text" id="search" placeholder="Search protocols by title…" oninput="filterTable()">
  </div>
  <p class="count" id="count">{{ protocols|length }} protocols</p>
  <table id="proto-table">
    <thead>
      <tr>
        <th>Title</th>
        <th>Category</th>
        <th>Last Updated</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      {% for p in protocols %}
      <tr>
        <td>{{ p.fm.title }}</td>
        <td><span class="badge">{{ p.fm.category }}</span></td>
        <td>{{ p.fm.last_updated }}</td>
        <td>
          <a href="/edit/{{ p.fm.slug }}" class="btn btn-sm btn-outline">Edit</a>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
<script>
function filterTable() {
  const q = document.getElementById('search').value.toLowerCase();
  const rows = document.querySelectorAll('#proto-table tbody tr');
  let visible = 0;
  rows.forEach(row => {
    const title = row.cells[0].textContent.toLowerCase();
    const show = title.includes(q);
    row.style.display = show ? '' : 'none';
    if (show) visible++;
  });
  document.getElementById('count').textContent = visible + ' protocols';
}
</script>
</body>
</html>"""


FORM_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ page_title }} — Protocol Manager</title>
<style>
  *, *::before, *::after { box-sizing: border-box; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
         margin: 0; background: #f5f5f5; color: #222; }
  .navbar { background: #1a237e; color: white; padding: 0.75rem 1.5rem;
            display: flex; align-items: center; gap: 1rem; }
  .navbar h1 { margin: 0; font-size: 1.15rem; font-weight: 600; }
  .navbar a { color: rgba(255,255,255,.75); text-decoration: none; font-size: 0.9rem; }
  .navbar a:hover { color: white; }
  .content { max-width: 920px; margin: 1.5rem auto; padding: 0 1rem 3rem; }
  .section { background: white; border-radius: 6px; padding: 1.25rem 1.5rem;
             margin-bottom: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,.08); }
  .section h2 { margin: 0 0 1rem; font-size: 1rem; font-weight: 700;
                color: #1a237e; text-transform: uppercase; letter-spacing: .04em;
                border-bottom: 2px solid #e8eaf6; padding-bottom: 0.5rem; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem 1rem; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.75rem 1rem; }
  .grid-4 { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 0.75rem 1rem; }
  .span-full { grid-column: 1 / -1; }
  label { display: block; font-size: 0.82rem; font-weight: 600; color: #555;
          margin-bottom: 0.25rem; }
  input[type=text], input[type=date], select, textarea {
    width: 100%; padding: 0.4rem 0.6rem; border: 1px solid #d0d0d0;
    border-radius: 4px; font-size: 0.92rem; font-family: inherit;
    background: white; transition: border-color .15s; }
  input:focus, select:focus, textarea:focus {
    outline: none; border-color: #1565c0; box-shadow: 0 0 0 2px rgba(21,101,192,.15); }
  input[readonly] { background: #f5f5f5; color: #777; }
  textarea { resize: vertical; }
  /* Dynamic rows */
  .dynamic-row { border: 1px solid #e0e0e0; border-radius: 4px; padding: 0.75rem;
                 margin-bottom: 0.6rem; background: #fafafa; position: relative; }
  .dynamic-row .row-grid { display: grid; gap: 0.5rem 0.75rem; }
  .series-row-grid { grid-template-columns: 2fr 1fr 1fr 1fr 1fr; }
  .recon-row-grid { grid-template-columns: 1fr 1fr 1fr 1fr 1fr; }
  .recon-row-grid2 { grid-template-columns: 1fr 1fr 1fr; margin-top: 0.5rem; }
  .remove-btn { position: absolute; top: 0.5rem; right: 0.5rem;
                background: #fbe9e7; color: #c62828; border: 1px solid #ef9a9a;
                border-radius: 3px; padding: 0.15rem 0.5rem; cursor: pointer;
                font-size: 0.78rem; }
  .remove-btn:hover { background: #ffcdd2; }
  .add-btn { background: #e8f5e9; color: #2e7d32; border: 1px solid #a5d6a7;
             border-radius: 4px; padding: 0.35rem 0.85rem; cursor: pointer;
             font-size: 0.85rem; margin-top: 0.4rem; }
  .add-btn:hover { background: #c8e6c9; }
  .action-bar { display: flex; align-items: center; gap: 1rem; }
  .btn-save { background: #1565c0; color: white; border: none; border-radius: 4px;
              padding: 0.6rem 1.5rem; font-size: 1rem; cursor: pointer; font-weight: 600; }
  .btn-save:hover { background: #0d47a1; }
  #status { font-size: 0.92rem; font-weight: 500; }
  .ok { color: #2e7d32; }
  .err { color: #c62828; }
  /* Base protocol picker */
  .base-picker { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; }
  .base-picker select { flex: 1; }
  .base-picker button { white-space: nowrap; background: #e3f2fd; color: #1565c0;
                        border: 1px solid #90caf9; border-radius: 4px;
                        padding: 0.4rem 0.85rem; cursor: pointer; font-size: 0.88rem; }
  /* Change request review */
  .apply-highlight { background: #fffbe6 !important; border-color: #f0ad00 !important; }
  .review-banner { background: #fff8e1; border: 1px solid #f0ad00; border-radius: 6px;
                   padding: 0.75rem 1.25rem; margin-bottom: 1.25rem; font-size: 0.92rem;
                   color: #5c4000; }
  .review-banner strong { color: #3d2a00; }
</style>
</head>
<body>
<nav class="navbar">
  <a href="/">← Back</a>
  <h1>{{ page_title }}</h1>
</nav>
<div class="content">

{% if reviewing_request %}
<div class="review-banner">
  <strong>Reviewing change request</strong> — highlighted fields contain the proposed values. Review and click Save to apply.
</div>
{% endif %}

{% if is_new %}
<div class="section">
  <h2>Base Protocol (optional)</h2>
  <div class="base-picker">
    <select id="base-select">
      <option value="">— start from scratch —</option>
      {% for p in all_protocols %}
      <option value="{{ p.fm.slug }}" data-fm="{{ p.fm | tojson | e }}">{{ p.fm.title }}</option>
      {% endfor %}
    </select>
    <button type="button" onclick="loadBase()">Load</button>
  </div>
</div>
{% endif %}

<form id="proto-form">

<div class="section">
  <h2>Identity</h2>
  <div class="grid-2">
    <div>
      <label for="title">Title</label>
      <input type="text" id="title" name="title" value="{{ fm.title }}"
             class="{{ 'apply-highlight' if 'title' in highlighted else '' }}"
             oninput="{% if is_new %}autoSlug(){% endif %}">
    </div>
    <div>
      <label for="slug">Slug</label>
      <input type="text" id="slug" name="slug" value="{{ fm.slug }}"
             {% if not is_new %}readonly{% endif %}>
    </div>
    <div>
      <label for="category">Category</label>
      <select id="category" name="category" class="{{ 'apply-highlight' if 'category' in highlighted else '' }}">
        {% for cat in categories %}
        <option value="{{ cat }}" {% if fm.category == cat %}selected{% endif %}>{{ cat }}</option>
        {% endfor %}
      </select>
    </div>
    <div>
      <label for="protocol_type">Protocol Type</label>
      <input type="text" id="protocol_type" name="protocol_type" value="{{ fm.protocol_type }}">
    </div>
    <div>
      <label for="last_updated">Last Updated</label>
      <input type="date" id="last_updated" name="last_updated" value="{{ fm.last_updated }}">
    </div>
    <div>
      <label for="author">Author</label>
      <input type="text" id="author" name="author" value="{{ fm.author }}">
    </div>
    <div class="span-full">
      <label for="synonyms">Synonyms (one per line)</label>
      <textarea id="synonyms" name="synonyms" rows="2">{{ fm.synonyms | join('\n') }}</textarea>
    </div>
  </div>
</div>

<div class="section">
  <h2>Clinical</h2>
  <div class="grid-2">
    <div class="span-full">
      <label for="indications_json">Clinical Indications (one per line)</label>
      <textarea id="indications_json" name="indications_json" rows="4" class="{{ 'apply-highlight' if 'indications_json' in highlighted else '' }}">{{ fm.clinical_indications | join('\n') }}</textarea>
    </div>
    <div>
      <label for="position">Position</label>
      <input type="text" id="position" name="position" value="{{ fm.position }}" class="{{ 'apply-highlight' if 'position' in highlighted else '' }}">
    </div>
    <div>
      <label for="npo">NPO Status</label>
      <input type="text" id="npo" name="npo" value="{{ fm.npo }}" class="{{ 'apply-highlight' if 'npo' in highlighted else '' }}">
    </div>
  </div>
</div>

<div class="section">
  <h2>Preparation</h2>
  <div>
    <label for="premedication">Premedication</label>
    <textarea id="premedication" name="premedication" rows="3" class="{{ 'apply-highlight' if 'premedication' in highlighted else '' }}">{{ fm.premedication }}</textarea>
  </div>
</div>

<div class="section">
  <h2>IV Contrast</h2>
  <div class="grid-4">
    <div>
      <label>Agent</label>
      <input type="text" name="contrast_agent" value="{{ fm.contrast.agent }}" class="{{ 'apply-highlight' if 'contrast_agent' in highlighted else '' }}">
    </div>
    <div>
      <label>Volume</label>
      <input type="text" name="contrast_volume" value="{{ fm.contrast.volume }}" class="{{ 'apply-highlight' if 'contrast_volume' in highlighted else '' }}">
    </div>
    <div>
      <label>Flow Rate</label>
      <input type="text" name="contrast_flow_rate" value="{{ fm.contrast.flow_rate }}" class="{{ 'apply-highlight' if 'contrast_flow_rate' in highlighted else '' }}">
    </div>
    <div>
      <label>Duration</label>
      <input type="text" name="contrast_duration" value="{{ fm.contrast.duration }}" class="{{ 'apply-highlight' if 'contrast_duration' in highlighted else '' }}">
    </div>
    <div>
      <label>Timing Method</label>
      <input type="text" name="contrast_timing" value="{{ fm.contrast.timing }}" class="{{ 'apply-highlight' if 'contrast_timing' in highlighted else '' }}">
    </div>
    <div>
      <label>ROI</label>
      <input type="text" name="contrast_roi" value="{{ fm.contrast.roi }}" class="{{ 'apply-highlight' if 'contrast_roi' in highlighted else '' }}">
    </div>
    <div>
      <label>Trigger (HU)</label>
      <input type="text" name="contrast_trigger" value="{{ fm.contrast.trigger }}" class="{{ 'apply-highlight' if 'contrast_trigger' in highlighted else '' }}">
    </div>
  </div>
</div>

<div class="section">
  <h2>Series Acquisition</h2>
  <div id="series-container"></div>
  <button type="button" class="add-btn" onclick="addSeriesRow({})">+ Add Series</button>
  <input type="hidden" name="series_json" id="series_json">
</div>

<div class="section">
  <h2>Post-Processing (Recons)</h2>
  <div id="recon-container"></div>
  <button type="button" class="add-btn" onclick="addReconRow({})">+ Add Recon</button>
  <input type="hidden" name="recons_json" id="recons_json">
</div>

<div class="section">
  <h2>Notes</h2>
  <div class="grid-2">
    <div>
      <label>Tech Notes</label>
      <textarea name="notes_tech" rows="3" class="{{ 'apply-highlight' if 'notes_tech' in highlighted else '' }}">{{ fm.notes.tech }}</textarea>
    </div>
    <div>
      <label>Nursing Notes</label>
      <textarea name="notes_nursing" rows="3" class="{{ 'apply-highlight' if 'notes_nursing' in highlighted else '' }}">{{ fm.notes.nursing }}</textarea>
    </div>
    <div>
      <label>Radiologist Notes</label>
      <textarea name="notes_rad" rows="3" class="{{ 'apply-highlight' if 'notes_rad' in highlighted else '' }}">{{ fm.notes.rad }}</textarea>
    </div>
    <div>
      <label>Tips &amp; Tricks</label>
      <textarea name="notes_tips" rows="3" class="{{ 'apply-highlight' if 'notes_tips' in highlighted else '' }}">{{ fm.notes.tips }}</textarea>
    </div>
  </div>
</div>

<div class="section">
  <h2>Safety</h2>
  <div class="grid-2">
    <div>
      <label>Renal Considerations</label>
      <input type="text" name="safety_renal" value="{{ fm.safety.renal }}" class="{{ 'apply-highlight' if 'safety_renal' in highlighted else '' }}">
    </div>
    <div>
      <label>Allergy Considerations</label>
      <input type="text" name="safety_allergy" value="{{ fm.safety.allergy }}" class="{{ 'apply-highlight' if 'safety_allergy' in highlighted else '' }}">
    </div>
  </div>
</div>

<div class="action-bar">
  <button type="button" class="btn-save" onclick="submitForm()">Save Protocol</button>
  <span id="status"></span>
</div>

</form>
</div>

<script>
// ---- Initial data ----
const INITIAL_SERIES = {{ series_json | safe }};
const INITIAL_RECONS = {{ recons_json | safe }};
const IS_NEW = {{ 'true' if is_new else 'false' }};
const SAVE_URL = {{ save_url | tojson }};

// ---- Dynamic row builders ----
function addSeriesRow(s) {
  s = s || {};
  const container = document.getElementById('series-container');
  const div = document.createElement('div');
  div.className = 'dynamic-row series-row';
  div.innerHTML = `
    <button type="button" class="remove-btn" onclick="this.parentElement.remove()">Remove</button>
    <div class="row-grid series-row-grid">
      <div><label>Name</label><input type="text" data-field="name" value="${esc(s.name)}"></div>
      <div><label>Start</label><input type="text" data-field="start" value="${esc(s.start)}"></div>
      <div><label>End</label><input type="text" data-field="end" value="${esc(s.end)}"></div>
      <div><label>Delay</label><input type="text" data-field="delay" value="${esc(s.delay)}"></div>
      <div><label>Thickness</label><input type="text" data-field="thickness" value="${esc(s.thickness)}"></div>
    </div>
    <div style="margin-top:0.5rem">
      <label>Notes</label>
      <input type="text" data-field="notes" value="${esc(s.notes)}" style="width:100%">
    </div>`;
  container.appendChild(div);
}

function addReconRow(r) {
  r = r || {};
  const container = document.getElementById('recon-container');
  const div = document.createElement('div');
  div.className = 'dynamic-row recon-row';
  div.innerHTML = `
    <button type="button" class="remove-btn" onclick="this.parentElement.remove()">Remove</button>
    <div class="row-grid recon-row-grid">
      <div><label>Plane</label><input type="text" data-field="plane" value="${esc(r.plane)}"></div>
      <div><label>Acquisition</label><input type="text" data-field="acquisition" value="${esc(r.acquisition)}"></div>
      <div><label>FOV</label><input type="text" data-field="fov" value="${esc(r.fov)}"></div>
      <div><label>Thickness/Inc</label><input type="text" data-field="thickness_increment" value="${esc(r.thickness_increment)}"></div>
      <div><label>Kernel</label><input type="text" data-field="kernel" value="${esc(r.kernel)}"></div>
    </div>
    <div class="row-grid recon-row-grid2" style="margin-top:0.5rem">
      <div><label>IR Strength</label><input type="text" data-field="ir_strength" value="${esc(r.ir_strength)}"></div>
      <div class="span-full"><label>Notes</label><input type="text" data-field="notes" value="${esc(r.notes)}" style="width:100%"></div>
    </div>`;
  container.appendChild(div);
}

function esc(v) {
  if (v == null) return '';
  return String(v).replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function collectRows(containerSelector, rowClass) {
  const rows = document.querySelectorAll(containerSelector + ' .' + rowClass);
  return Array.from(rows).map(row => {
    const obj = {};
    row.querySelectorAll('[data-field]').forEach(inp => {
      obj[inp.dataset.field] = inp.value;
    });
    return obj;
  });
}

function submitForm() {
  // Collect dynamic rows into hidden inputs
  const series = collectRows('#series-container', 'series-row');
  const recons = collectRows('#recon-container', 'recon-row');
  document.getElementById('series_json').value = JSON.stringify(series);
  document.getElementById('recons_json').value = JSON.stringify(recons);

  const formEl = document.getElementById('proto-form');
  const data = new FormData(formEl);

  const statusEl = document.getElementById('status');
  statusEl.textContent = 'Saving…';
  statusEl.className = '';

  fetch(SAVE_URL, { method: 'POST', body: data })
    .then(r => r.json())
    .then(res => {
      if (res.success) {
        statusEl.textContent = 'Saved successfully.';
        statusEl.className = 'ok';
        if (res.redirect) {
          setTimeout(() => { window.location.href = res.redirect; }, 800);
        }
      } else {
        statusEl.textContent = 'Error: ' + (res.error || 'Unknown error');
        statusEl.className = 'err';
      }
    })
    .catch(e => {
      statusEl.textContent = 'Network error: ' + e;
      statusEl.className = 'err';
    });
}

// ---- Slug auto-generation (new only) ----
function autoSlug() {
  if (!IS_NEW) return;
  const title = document.getElementById('title').value;
  document.getElementById('slug').value = title.toLowerCase()
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}

// ---- Load base protocol (new only) ----
function loadBase() {
  const sel = document.getElementById('base-select');
  const opt = sel.options[sel.selectedIndex];
  if (!opt || !opt.dataset.fm) return;
  let fm;
  try { fm = JSON.parse(opt.dataset.fm); } catch(e) { return; }

  // Fill scalar fields
  const setVal = (id, val) => { const el = document.getElementById(id); if (el) el.value = val || ''; };
  setVal('title', '');  // Don't copy title
  setVal('slug', '');
  document.getElementById('category').value = fm.category || 'abdomen';
  setVal('protocol_type', fm.protocol_type);
  setVal('position', fm.position);
  setVal('npo', fm.npo);
  setVal('premedication', fm.premedication);

  // Contrast
  const c = fm.contrast || {};
  document.querySelector('[name=contrast_agent]').value = c.agent || '';
  document.querySelector('[name=contrast_volume]').value = c.volume || '';
  document.querySelector('[name=contrast_flow_rate]').value = c.flow_rate || '';
  document.querySelector('[name=contrast_duration]').value = c.duration || '';
  document.querySelector('[name=contrast_timing]').value = c.timing || '';
  document.querySelector('[name=contrast_roi]').value = c.roi || '';
  document.querySelector('[name=contrast_trigger]').value = c.trigger || '';

  // Indications
  document.getElementById('indications_json').value = (fm.clinical_indications || []).join('\\n');

  // Notes
  const n = fm.notes || {};
  document.querySelector('[name=notes_tech]').value = n.tech || '';
  document.querySelector('[name=notes_nursing]').value = n.nursing || '';
  document.querySelector('[name=notes_rad]').value = n.rad || '';
  document.querySelector('[name=notes_tips]').value = n.tips || '';

  // Safety
  const s = fm.safety || {};
  document.querySelector('[name=safety_renal]').value = s.renal || '';
  document.querySelector('[name=safety_allergy]').value = s.allergy || '';

  // Series
  document.getElementById('series-container').innerHTML = '';
  (fm.series || []).forEach(row => addSeriesRow(row));

  // Recons
  document.getElementById('recon-container').innerHTML = '';
  (fm.recons || []).forEach(row => addReconRow(row));
}

// ---- Init ----
document.addEventListener('DOMContentLoaded', () => {
  INITIAL_SERIES.forEach(s => addSeriesRow(s));
  INITIAL_RECONS.forEach(r => addReconRow(r));
});
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Empty FM template
# ---------------------------------------------------------------------------

EMPTY_FM: dict = {
    "title": "",
    "slug": "",
    "category": "abdomen",
    "protocol_type": "",
    "last_updated": str(date.today()),
    "author": "",
    "synonyms": [],
    "clinical_indications": [],
    "position": "",
    "npo": "",
    "premedication": "",
    "contrast": {
        "agent": "", "volume": "", "flow_rate": "",
        "duration": "", "timing": "", "roi": "", "trigger": "",
    },
    "series": [],
    "recons": [],
    "notes": {"tech": "", "nursing": "", "rad": "", "tips": ""},
    "safety": {"renal": "", "allergy": ""},
}


def _ensure_fm_keys(fm: dict) -> dict:
    """Merge fm with EMPTY_FM defaults so templates never get KeyError."""
    result = {}
    for key, default in EMPTY_FM.items():
        val = fm.get(key, default)
        if isinstance(default, dict) and not isinstance(val, dict):
            val = default.copy()
        result[key] = val
    # Ensure nested contrast keys
    for k, v in EMPTY_FM["contrast"].items():
        result["contrast"].setdefault(k, v)
    for k, v in EMPTY_FM["notes"].items():
        result["notes"].setdefault(k, v)
    for k, v in EMPTY_FM["safety"].items():
        result["safety"].setdefault(k, v)
    return result


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.route("/")
def index():
    protocols = load_all_protocols()
    return render_template_string(LIST_TEMPLATE, protocols=protocols)


@app.route("/edit/<slug>", methods=["GET", "POST"])
def edit(slug: str):
    item = find_protocol(slug)
    if item is None:
        return f"Protocol '{slug}' not found.", 404

    if request.method == "POST":
        try:
            original_fm = item["fm"]
            fm = form_to_frontmatter(request.form)
            # Preserve slug (readonly on edit)
            fm["slug"] = slug
            # Preserve fields not exposed in the form to avoid silent data loss
            if "tech_params" in original_fm:
                fm["tech_params"] = original_fm["tech_params"]
            if original_fm.get("notes", {}).get("additional_recons"):
                fm.setdefault("notes", {})["additional_recons"] = original_fm["notes"]["additional_recons"]
            md_content = render_document(fm)
            item["filepath"].write_text(md_content, encoding="utf-8")
            failures = rebuild_indexes()
            if failures:
                return jsonify({"success": True, "warnings": failures})
            return jsonify({"success": True})
        except Exception as exc:
            return jsonify({"success": False, "error": str(exc)})

    fm = _ensure_fm_keys(item["fm"])
    highlighted = set()
    apply_param = request.args.get("apply", "")
    if apply_param:
        try:
            # Pad to multiple of 4 for standard base64 decode
            padding = "=" * ((4 - len(apply_param) % 4) % 4)
            apply_changes = json.loads(base64.b64decode(apply_param + padding))
            fm, highlighted = apply_changes_to_fm(fm, apply_changes)
        except Exception:
            pass  # Malformed apply param — ignore, show unmodified form

    return render_template_string(
        FORM_TEMPLATE,
        page_title=f"Edit: {fm['title']}",
        fm=fm,
        categories=CATEGORIES,
        is_new=False,
        save_url=url_for("edit", slug=slug),
        series_json=json.dumps(fm.get("series", [])),
        recons_json=json.dumps(fm.get("recons", [])),
        all_protocols=[],
        highlighted=highlighted,
        reviewing_request=bool(highlighted),
    )


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        import re as _re
        try:
            fm = form_to_frontmatter(request.form)
            slug = fm.get("slug", "").strip()
            if not slug:
                return jsonify({"success": False, "error": "Slug is required."})
            if not _re.fullmatch(r'[a-z0-9][a-z0-9-]*', slug):
                return jsonify({"success": False, "error": "Slug must contain only lowercase letters, digits, and hyphens."})
            category = fm.get("category", "abdomen")
            if category not in CATEGORIES:
                return jsonify({"success": False, "error": f"Invalid category: {category}"})
            target_path = DOCS_CT / category / f"{slug}.md"
            if not str(target_path.resolve()).startswith(str(DOCS_CT.resolve())):
                return jsonify({"success": False, "error": "Invalid path."})
            if target_path.exists():
                return jsonify({"success": False, "error": f"File already exists: {target_path.relative_to(REPO_ROOT)}"})
            target_path.parent.mkdir(parents=True, exist_ok=True)
            md_content = render_document(fm)
            target_path.write_text(md_content, encoding="utf-8")
            failures = rebuild_indexes()
            if failures:
                return jsonify({"success": True, "redirect": url_for("edit", slug=slug), "warnings": failures})
            return jsonify({"success": True, "redirect": url_for("edit", slug=slug)})
        except Exception as exc:
            return jsonify({"success": False, "error": str(exc)})

    fm = _ensure_fm_keys({})
    all_protocols = load_all_protocols()
    return render_template_string(
        FORM_TEMPLATE,
        page_title="New Protocol",
        fm=fm,
        categories=CATEGORIES,
        is_new=True,
        save_url=url_for("new"),
        series_json="[]",
        recons_json="[]",
        all_protocols=all_protocols,
        highlighted=set(),
        reviewing_request=False,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = 5173
    url = f"http://localhost:{port}"
    print(f"Starting Protocol Manager Admin at {url}")
    # Open browser after a short delay so Flask is ready
    import threading
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(host="127.0.0.1", port=port, debug=False)
