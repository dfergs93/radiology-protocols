# Protocol Submission Form — Design Spec

**Date:** 2026-03-19
**Status:** Approved
**Todo reference:** Item 5 — Protocol Submission Form (New Feature)

---

## Overview

A web form embedded in the MkDocs site that allows the author to create or clone CT protocols. The form covers the full protocol structure, pre-populates from an existing protocol to speed up authoring, and generates a `.md` file for manual placement into `docs/ct/`. No filesystem writes from the backend — the author copies the output into the repo themselves.

---

## Architecture

### New Files

| File | Purpose |
|------|---------|
| `docs/submit.md` | MkDocs page hosting the submission form |
| `docs/javascripts/protocol-submit.js` | All form logic, API calls, preview rendering |

`docs/submit.md` must be added to the root `docs/.pages` file (used by the `awesome-pages` MkDocs plugin) to appear in site navigation.

### New API Endpoints (in `backend/app.py`)

| Endpoint | Purpose |
|----------|---------|
| `GET /api/protocols/{filepath}` | Reads and parses a protocol markdown file; returns structured JSON for pre-populating the form. Backend must validate that the resolved path is within `docs/ct/` to prevent path traversal. |
| `POST /api/protocols/generate` | Accepts all form fields as JSON; renders and returns `{ markdown: string }` using the existing protocol template |

### Existing Resources Used

- `backend/protocol_index.json` — drives the "Base off existing protocol" dropdown (already contains title + filepath for all protocols)
- `docs/javascripts/protocol-comparison-index.json` — not used directly, but rebuilt after the new protocol is added
- `marked.js` — already loaded on MkDocs pages; used for markdown → HTML in the preview panel
- `mermaid@10` — already loaded; used to render the Gantt diagram in the preview
- Material theme CSS variables — form and preview styled to match the existing site

---

## Form Structure

Single scrollable form with a sticky left anchor nav linking to each section. Ten sections:

### 1. Metadata
- Protocol Name (text)
- Author (text)
- Last Updated (date picker, defaults to today)
- Category (dropdown: Cardiac, Vascular, Chest, Abdomen, Neuro, Msk, Trauma) — values match the `docs/ct/` subdirectory names exactly
- Protocol Type (text)

### 2. Clinical Summary
- Acquisition Summary table — add/remove rows: Series | Phase | Coverage
- Clinical Indications — freetext list (one indication per line)

### 3. Patient Prep
- Position (text)
- NPO Status (text)
- Premedication toggle + freetext (shown when toggled on)

### 4. IV Contrast & Injection
- Injection Parameters table — fixed rows matching the actual protocol template: Agent, Volume, Flow Rate, Timing Method, ROI Placement, Trigger (HU) (each with a value field). These align with the fields parsed by `generate_comparison_index.py` (`timing`, `trigger`, `roi`).
- Lab Requirements (freetext)

### 5. Special Notes
- Technologist Notes (freetext)
- Nursing Notes (freetext)
- Radiologist Notes (freetext)
- Tips & Tricks (freetext)
- Safety — Renal Function (text), Allergy Check (text)

### 6. Gantt Builder
- Add/remove rows; each row has:
  - Label (text) — displayed in the Gantt title; also auto-slugified to generate a unique Mermaid task ID (e.g., "Contrast Injection" → `contrast_injection`). If two rows produce the same slug, a numeric suffix is appended (`contrast_injection_2`).
  - Duration in seconds (number). The frontend converts the integer to `mm:ss` format before generating the Mermaid block (e.g., `30` → `00:30`, `90` → `01:30`).
  - Type (dropdown: contrast, saline, scan, other) — maps to Mermaid task class for styling (`active` for contrast/saline, `crit` for scan)
  - Start (dropdown: "at 00:00" maps to an absolute `00:00` start time, or "after [row label]" maps to Mermaid `after <id>` syntax using the slugified ID of the referenced row)
- Generates mermaid `gantt` block automatically using `dateFormat mm:ss` and the slugified IDs

### 7. Series Acquisition
- Add/remove rows: Series Name | Start | End | Delay | Thickness | Notes

### 8. Technical Parameters
- kV (text)
- mAs (text)
- Rotation Time in seconds (number)
- Pitch (text)

### 9. Post-Processing
- Add/remove rows: Plane | Acquisition | FOV | Thickness/Increment | Kernel | IR Strength | Notes

### 10. Additional Reconstructions
- Freetext. The backend wraps this content in `{additional_recons_section}` as a plain markdown paragraph (no tab header). If empty, the placeholder is replaced with an empty string.

---

## "Base Off Existing Protocol" Feature

At the top of the form, a searchable dropdown (same pattern as `protocol-compare.js`) populated from `protocol_index.json`. On selection:

1. Frontend passes the filepath string as-is from `protocol_index.json` (e.g., `ct/cardiac/coronary-cta.md`, relative to `docs/`). The backend resolves it against the project root `docs/` directory and validates the resolved absolute path starts with the `docs/ct/` absolute path before reading.
2. Frontend calls `GET /api/protocols/{filepath}`
2. Backend reads the markdown file, parses all sections (reusing regex logic from `generate_comparison_index.py` where applicable), and returns structured JSON
3. Frontend populates all form fields from the response
4. The author edits only what differs — title, indications, parameters, etc.

---

## Live Preview & Output

### Layout
- Desktop: two-column — form at ~60% left, sticky preview panel at ~40% right
- Mobile: preview collapses below the form

### Preview Rendering
- "Generate & Preview" button calls `POST /api/protocols/generate`
- Backend returns `{ markdown: string }`
- Frontend renders markdown → HTML via `marked.js`, then calls `mermaid.run()` to render the Gantt
- Preview panel styled with Material theme variables to match the live protocol pages

### Output Actions (in preview panel header)
- **Copy Markdown** — copies raw markdown to clipboard
- **Download** — saves `<protocol-name>.md` to downloads

### After Download
The author manually places the file in the appropriate `docs/ct/<category>/` subdirectory, then runs:
```bash
python scripts/build_vectordb.py
python scripts/generate_comparison_index.py
```

---

## Markdown Generation

`POST /api/protocols/generate` uses `scripts/protocol_template.py` (which already defines `PROTOCOL_TEMPLATE` as a Python format string). The backend adapts this template by substituting all form fields. Sections with no content (e.g., empty Post-Processing table) are rendered as empty tables rather than omitted, to keep the markdown structure consistent for later parsing.

The generated file ends with these two plain-text footer lines (outside any header or table), required by `build_vectordb.py` for indexing:

```
Category: {category}

Protocol Type: {protocol_type}
```

The `GET /api/protocols/{filepath}` parser must extract these footer lines in addition to parsing the tabbed sections.

---

## Validation

Server-side validation in `POST /api/protocols/generate`:
- Protocol name is required and non-empty
- Category must be one of: Cardiac, Vascular, Chest, Abdomen, Neuro, Msk, Trauma
- At least one clinical indication required
- Gantt rows must have label and duration > 0
- Returns `422` with field-level errors on failure

Client-side: required fields highlighted before form submission.

---

## Out of Scope

- Filesystem writes from the backend
- Authentication / access control (covered in Todo #7)
- Editing existing protocols via the form (the clone workflow covers the main use case; direct editing deferred)
- Auto-triggering index rebuilds after submission
