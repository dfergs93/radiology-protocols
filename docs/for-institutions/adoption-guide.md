---
title: Adoption Guide
---

# Adoption Guide

This guide is written for the developer or IT person setting up Protocol Manager for a new institution.

## Step 1 — Fork and Configure

Fork the repository on GitHub, then clone your fork locally.

Edit `config/institution.yml`:

```yaml
institution:
  name: "Your Department Name"
  short_name: "Radiology"
  site_url: "https://your-org.github.io/radiology-protocols"
  base_path: "/radiology-protocols"

contact:
  department_email: ""
  feedback_url: ""

branding:
  logo: ""
  favicon: ""
```

Update `site_url` in `mkdocs.yml` to match the value you set above.

If you are hosting in a subdirectory on an internal server (e.g. `https://intranet.hospital.org/radiology/`), set `base_path` to `/radiology` and `site_url` to `https://intranet.hospital.org/radiology`.

## Step 2 — Install Dependencies

```bash
pip install mkdocs-material pymdown-extensions mkdocs-awesome-pages-plugin pyyaml flask
```

Install the pre-commit hook so indexes are regenerated automatically whenever you commit protocol changes:

```bash
python scripts/install_hooks.py
```

## Step 3 — Migrate Existing Protocols

Choose one of the two paths below based on your starting point.

### Path A — CSV Bulk Import (recommended for 10+ protocols)

Use this path when you have existing protocol documentation in Word, PDF, or spreadsheet format that can be transcribed to CSV.

1. Open `data/protocols.csv`. The header row documents all columns. Each row is one protocol. Key columns:

   | Column | Description |
   |--------|-------------|
   | `slug` | URL-safe identifier, e.g. `ct-pulmonary-embolism` |
   | `title` | Display name, e.g. `CT Pulmonary Embolism` |
   | `category` | Body area: `abdomen`, `chest`, `cardiac`, `neuro`, `msk`, `vascular`, `trauma` |
   | `contrast_agent` | e.g. `Isovue 370` |
   | `contrast_volume` | e.g. `1.5 mL/kg` |
   | `contrast_flow_rate` | e.g. `4 mL/s` |
   | `kv` | e.g. `120` |
   | `mas` | e.g. `Auto (reference 200)` |
   | `clinical_indications` | Pipe-separated list |

   Refer to the existing rows in `data/protocols.csv` as examples.

2. Open `data/protocol_series.csv`. Each row is one acquisition series within a protocol. Key columns:

   | Column | Description |
   |--------|-------------|
   | `protocol_slug` | Must match a `slug` value in `protocols.csv` |
   | `series_name` | e.g. `Portal Venous Phase` |
   | `phase_start_s` | Seconds after injection start |
   | `phase_duration_s` | Duration of the acquisition in seconds |
   | `coverage` | e.g. `Diaphragm to pubic symphysis` |

3. Preview the generated files (dry run):

   ```bash
   python scripts/build_from_csv.py
   ```

4. Write the Markdown files:

   ```bash
   python scripts/build_from_csv.py --apply
   ```

   Files are written to `docs/ct/<category>/<slug>.md`.

5. Review the generated files and adjust the Markdown body text as needed. The body sections (patient prep, nursing notes, radiologist notes) are populated from the CSV but may need editing for your institution's conventions.

### Path B — Manual Authoring (for small sets or one-offs)

Use this path for a small number of protocols or when adding protocols one at a time.

1. Copy an existing protocol file as a template:

   ```bash
   cp docs/ct/chest/ct-pulmonary-embolism.md docs/ct/chest/my-new-protocol.md
   ```

2. Edit the YAML front matter at the top of the file — update all parameter values for the new protocol.

3. Edit the Markdown body sections below the front matter.

4. Regenerate the comparison index:

   ```bash
   python scripts/generate_comparison_index.py
   ```

   Commit the updated index file along with the new protocol.

## Step 4 — Deploy

See [Hosting](hosting.md) for GitHub Pages and local/intranet deployment options.

---

## Updating Protocols

The **recommended approach** for editing protocols is the Flask admin app:

```bash
python scripts/admin.py
```

The admin app auto-regenerates all indexes on save, so you never need to run index scripts manually.

If you edit protocol Markdown files directly instead, the pre-commit hook (installed via `python scripts/install_hooks.py`) acts as a safety net: it detects staged changes under `docs/ct/` and regenerates all indexes before the commit lands.

For direct file edits without the hook, regenerate indexes manually:

1. Update the YAML front matter if any structured parameters changed
2. Run `python scripts/generate_comparison_index.py`, `python scripts/generate_sitemap.py`, and `python scripts/generate_forms_index.py`
3. Commit all changed files and push (CI handles deployment)
