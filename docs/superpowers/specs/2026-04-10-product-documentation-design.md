# Product Documentation Design

**Date:** 2026-04-10
**Status:** Approved

---

## Goal

Document Protocol Manager as an open-source product that any radiology department can fork and deploy at their institution. Documentation serves two audiences: clinical staff evaluating the tool (radiologists, physicists) and the developer or IT person who will set it up.

---

## What Is Being Built

Two documentation surfaces:

1. **`README.md` rewrite** — A standalone 2–3 page document on the GitHub repo. Readable without visiting the site. Covers what Protocol Manager is, how it works architecturally, what a new institution needs to adopt it, and a pointer to the full adoption guide on the deployed site.

2. **`For Institutions` section in the MkDocs site** — A new top-level nav section with four sub-pages. Same visual style as the rest of the site. No hero banners, no call-to-action elements.

---

## README.md Structure

Sections in order:

- **What it is** — 1–2 sentences. Factual description, no marketing language.
- **Live demo** — Link to `https://dfergs93.github.io/radiology-protocols/`
- **What you get** — Factual feature list: protocol pages, comparison tool, SVG acquisition diagrams, sitemap for Chrome extension integration, CI auto-deploy.
- **How it works** — Architecture in plain terms: Markdown files with YAML front matter, MkDocs Material build, GitHub Pages or internal web server hosting, vanilla JS comparison tool, CI pipeline that regenerates indexes on every push to `main`.
- **Prerequisites** — What the IT/developer needs before starting: GitHub account, Python 3.x, familiarity with the command line, existing protocol documentation to migrate.
- **Quick start** — Fork the repo → configure `config/institution.yml` → migrate protocols → deploy. ~5 steps, each linking to the full adoption guide on the site for detail.

---

## For Institutions Site Section — Pages

### 1. Overview (`for-institutions/index.md`)

One paragraph on the clinical workflow the tool supports: a single source of truth for department CT protocols, accessible from any browser, with a side-by-side comparison tool for protocol selection and planning.

One paragraph on the technical model: a static site generated from Markdown files, deployed to GitHub Pages or an internal web server, with no backend server or database to maintain.

Explicitly states constraints:
- Requires a developer or IT person to set up and maintain
- Protocols must be authored or migrated into a specific Markdown + YAML format
- Protocol editing workflow (in-browser or form-based editing) is not yet implemented — editing is done by modifying Markdown files directly

### 2. How It Works (`for-institutions/how-it-works.md`)

Technical walkthrough of the system components:

- **Protocol pages** — Each protocol is a Markdown file under `docs/ct/<body-area>/`. YAML front matter stores structured data (contrast parameters, series list, technical parameters). The Markdown body is the human-readable protocol document.
- **Comparison tool** — A pre-generated JSON index (`protocol-comparison-index.json`) is built by CI from all YAML front matter. The comparison UI reads this index at runtime. No server required.
- **SVG acquisition diagrams** — `acquisition-diagram.js` reads the series data from YAML front matter and renders inline SVG timelines. Supports multi-phase protocols and split boluses.
- **CI pipeline** — GitHub Actions runs on every push to `main`: regenerates the comparison index, regenerates the sitemap, builds and deploys the site via `mkdocs gh-deploy`.
- **Chrome extension integration** (brief) — `generate_sitemap.py` outputs a `sitemap.json` used by the `radiology-agent` Chrome extension to discover protocol URLs. This is optional; institutions not using the extension can ignore it.

### 3. Adoption Guide (`for-institutions/adoption-guide.md`)

Written for the developer or IT person doing the setup. Step-by-step, imperative style.

**Step 1 — Fork and configure**
- Fork the repository on GitHub
- Edit `config/institution.yml`: set `institution.name`, `site_url`, `base_path`, and optionally `contact` and `branding` fields
- Update `mkdocs.yml` `site_url` to match

**Step 2 — Migrate existing protocols**

Two paths:

*Path A — CSV bulk import (recommended for 10+ protocols):*
1. Export or transcribe existing protocols into `data/protocols.csv` and `data/protocol_series.csv`. Column schema is documented in the header rows of those files and in an example protocol file.
2. Run `python scripts/build_from_csv.py` (dry-run by default) to preview generated files.
3. Run `python scripts/build_from_csv.py --apply` to write Markdown files.
4. Review generated files and adjust body text as needed.

*Path B — Manual authoring (for small sets or one-offs):*
1. Copy an existing protocol Markdown file as a template.
2. Edit the YAML front matter (series, contrast, technical parameters) and the Markdown body sections.
3. Run `python scripts/generate_comparison_index.py` locally to update the comparison index before committing.

**Step 3 — Deploy**

See the Hosting page.

**Note on protocol editing:** Updating an existing protocol currently requires editing the Markdown file directly and re-running `generate_comparison_index.py`. A pipeline to automate YAML updates and index regeneration is planned but not yet implemented.

### 4. Hosting (`for-institutions/hosting.md`)

Two hosting options:

**Option A — GitHub Pages (zero server infrastructure)**
- Enable GitHub Pages on the forked repository (source: `gh-pages` branch)
- The CI workflow (`deploy.yml`) runs `mkdocs gh-deploy --force` on every push to `main`, which builds the site and pushes to the `gh-pages` branch automatically
- Free for public repositories
- Custom domain: add a `CNAME` file to `docs/` with the custom domain, then configure DNS per GitHub's documentation

**Option B — Local / intranet hosting**
- Run `mkdocs build` to generate the static `site/` directory
- Copy the contents of `site/` to any web server directory (nginx, Apache, IIS, internal file share)
- No special server configuration required — all files are static HTML/CSS/JS
- If hosted in a subdirectory (e.g. `https://intranet.hospital.org/radiology/protocols/`), set `base_path` in `config/institution.yml` and `site_url` in `mkdocs.yml` to match the subdirectory path
- Re-run `mkdocs build` and redeploy whenever protocols are updated

---

## Tone & Style Rules

- No superlatives: "powerful", "seamless", "robust", "comprehensive" are banned
- No calls to action: "Get started today", "Transform your workflow" etc.
- Feature descriptions state what something does, not the benefit it delivers
- Acknowledge constraints honestly — the tool has an opinionated data model, requires developer setup, and has known gaps (editing pipeline WIP)
- Imperative voice for procedural steps ("Fork the repo", "Edit `config/institution.yml`")
- Consistent with the existing writing style in `architecture-decisions.md` and `scripts/scripts_summary.md`

---

## Files to Create or Modify

| File | Action |
|------|--------|
| `README.md` | Rewrite |
| `docs/for-institutions/index.md` | Create |
| `docs/for-institutions/how-it-works.md` | Create |
| `docs/for-institutions/adoption-guide.md` | Create |
| `docs/for-institutions/hosting.md` | Create |
| `mkdocs.yml` | Add `for-institutions/` to nav |
| `docs/.pages` (if used by awesome-pages) | Add `for-institutions` section |

---

## Out of Scope

- In-browser protocol editing UI (planned separately)
- Automated protocol migration tooling beyond `build_from_csv.py`
- Full `radiology-agent` Chrome extension documentation (separate repo)
- MRI or other modality protocol support
