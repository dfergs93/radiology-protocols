# Protocol Editing & Change Request Design

**Date:** 2026-04-11
**Status:** Approved

## Overview

Two interfaces for managing protocol updates, plus auto-sync tooling to keep derived JSON files current.

| Component | User | Entry Point |
|---|---|---|
| Change request form | Non-technical staff (website access only) | Protocol page → "Request a Change" button |
| New protocol request | Non-technical staff | Same form, "New Protocol" mode |
| Admin app — edit | Protocol lead | `python scripts/admin.py` |
| Admin app — new | Protocol lead | Admin app → "New Protocol" |
| Auto-sync hook | Developer / lead | One-time `python scripts/install_hooks.py` |

---

## Component 1 — Static Change Request Form

### Location

A dedicated MkDocs page at `docs/request-change.md`. Each protocol page links to it via a "Request a Change" button in the page header, passing the slug as a query param (e.g., `?protocol=ct-pulmonary-embolism`).

### Two modes on the same page

**Mode A — Request a change to an existing protocol**

- URL param `?protocol=<slug>` identifies the target protocol.
- On load, JS fetches the slug's entry from `protocol-forms-index.json` (a new full-data index, see below) and pre-fills all form fields with current values.
- User edits only the fields they want changed. Untouched fields are excluded from the submission payload.

**Mode B — Request a new protocol**

- URL param `?mode=new` (or no param).
- User picks a base protocol from a searchable dropdown populated from `protocol-forms-index.json`.
- Selecting a base pre-fills all fields from that protocol.
- User provides a new title (required) and slug (auto-generated from title, editable).
- Submission payload includes all new values plus a header identifying the base protocol.

### Fields

Both modes expose the same field groups:

| Group | Fields |
|---|---|
| Identity | Title, Slug (new protocol only), Category |
| Clinical | Indications, Patient Position, NPO Status |
| Preparation | Premedication |
| Contrast | Agent, Volume, Flow Rate, Duration, Timing, ROI, Trigger |
| Series | One row per acquisition series (free-text) |
| Notes | Technologist, Nursing, Radiologist, Tips |
| Safety | Renal, Allergy |
| Other | Optional free-text "Reason / additional notes" |

### Protocol forms index

The existing `protocol-comparison-index.json` only includes contrast, series, and gantt fields — not the full YAML front matter. The change request form needs all fields.

A new script `scripts/generate_forms_index.py` generates `docs/javascripts/protocol-forms-index.json`, which includes the complete YAML front matter for every protocol: title, slug, category, protocol_type, clinical_indications, position, npo, premedication, contrast, series, recons, tech_notes, nursing_notes, rad_notes, tips, safety_renal, safety_allergy, author, last_updated.

This script is added to the CI pipeline alongside the existing index scripts, and to the pre-commit hook.

### Submission routing

Driven by `feedback_url` in `config/institution.yml`, exposed to JavaScript via MkDocs `extra:` config.

| `feedback_url` value | Behaviour |
|---|---|
| `mailto:...` | Generates formatted email body listing only changed fields; opens mail client |
| GitHub Issues URL | Appends pre-formatted issue body as query param; opens GitHub in a new tab |
| Blank / missing | Shows "Contact your protocol lead directly" message |

### What it does not do

Does not write to any file. Produces a human-readable change request for the lead to action through the admin app.

---

## Component 2 — Local Flask Admin App

### Running it

```bash
python scripts/admin.py
```

Starts Flask on `localhost:5173` and opens the browser automatically.

**Dependency added:** `flask` only. All other dependencies already required by the project.

### Pages

**Protocol list (`/`)**

- Searchable, filterable table: title, category, last updated.
- Per-row actions: Edit, View live page (link).
- "New Protocol" button in header.

**Edit protocol (`/edit/<slug>`)**

Form populated from the protocol's YAML front matter, grouped into sections matching the live page:

| Section | Fields |
|---|---|
| Clinical | Indications (dynamic list), Position, NPO |
| Preparation | Premedication |
| Contrast | Agent, Volume, Flow Rate, Duration, Timing, ROI, Trigger |
| Series | Dynamic list — add / remove rows (name, start, end, delay, thickness, notes) |
| Post-Processing | Dynamic list for recon rows (plane, acquisition, FOV, thickness/increment, kernel, IR strength, notes) |
| Notes | Technologist, Nursing, Radiologist, Tips |
| Safety | Renal, Allergy |
| Metadata | Last Updated (auto-set to today on save), Author |

On save:
1. Rewrites the YAML front matter block in the MD file.
2. Regenerates the markdown body from the YAML using the same template as `build_from_csv.py`.
3. Runs `generate_comparison_index.py` and `generate_sitemap.py`.
4. Returns success with a link to the updated file.

**New protocol (`/new`)**

- Same form as Edit, initially blank.
- "Base on existing protocol" dropdown pre-fills all fields from a chosen protocol.
- Title and slug are required; slug auto-generated from title, editable.
- On save: creates `docs/ct/<category>/<slug>.md`, then runs index scripts.

### Source of truth

YAML front matter is the canonical data source. The markdown body is always regenerated from YAML on save. Direct edits to the markdown body below the front matter will be overwritten on the next admin save — this is intentional and documented in the adoption guide.

---

## Component 3 — Auto-sync Pre-commit Hook

### Purpose

Safety net for direct MD file edits made outside the admin app. Ensures `protocol-comparison-index.json` and `sitemap.json` are never stale in a commit.

### Behaviour

- Triggers only when files under `docs/ct/` are staged.
- Runs `generate_comparison_index.py` and `generate_sitemap.py`.
- Stages the resulting JSON files so they're included in the same commit.
- If either script fails, blocks the commit with an error message.

### Installation

```bash
python scripts/install_hooks.py
```

Copies the hook to `.git/hooks/pre-commit` and makes it executable. One-time setup per clone. The adoption guide references this step. Since `.git/hooks/` is not committed, each contributor runs it once.

### Relationship to admin app

The admin app runs the index scripts on every save — the pre-commit hook is a fallback for direct file edits, not a replacement.

---

## Files Created / Modified

| Path | Action |
|---|---|
| `docs/request-change.md` | Create — change request form page |
| `docs/javascripts/request-change.js` | Create — form logic (populate, submit routing) |
| `docs/javascripts/protocol-forms-index.json` | Create — full front matter index for form pre-population (generated) |
| `scripts/generate_forms_index.py` | Create — generates protocol-forms-index.json |
| `scripts/admin.py` | Create — Flask admin app |
| `scripts/install_hooks.py` | Create — pre-commit hook installer |
| `scripts/hooks/pre-commit` | Create — hook script (copied by installer) |
| `mkdocs.yml` | Modify — add `extra.feedback_url` from `institution.yml`, add request-change page to nav |
| `.github/workflows/ci.yml` | Modify — add `generate_forms_index.py` step before deploy |
| `docs/for-institutions/adoption-guide.md` | Modify — add install_hooks step to setup instructions |
| `config/institution.yml` | Modify — add `feedback_url` field with documentation comment |

---

## Out of Scope

- Authentication for the admin app (local use only, no auth needed).
- Approval workflow — change requests are handled out-of-band (email / GitHub Issues).
- Real-time collaboration or conflict resolution.
- Editing the markdown body directly through the admin UI (YAML fields cover all structured content).
