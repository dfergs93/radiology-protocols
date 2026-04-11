# Radiology Protocol Manager

A static web platform for managing and comparing CT protocols, built with MkDocs (Material theme) and hosted on GitHub Pages.

![Status](https://img.shields.io/badge/Status-Active-success)
![Stack](https://img.shields.io/badge/Stack-MkDocs%20Material-blue)

## Overview

This repository serves as a CT protocol reference for a single institution. It provides:

- **Protocol pages** — Detailed CT protocol documentation with acquisition parameters, injection parameters, and SVG timing diagrams
- **Protocol Comparison** — Side-by-side comparison of any two CT protocols with shareable deep links

The site is a static MkDocs build deployed to GitHub Pages. There is no backend server.

## Project Structure

```
protocol_manager/
├── docs/                    # Content source files
│   ├── ct/                 # CT Protocols (Markdown + YAML front matter)
│   ├── javascripts/        # Custom frontend JS
│   │   ├── protocol-compare.js          # Side-by-side comparison tool
│   │   ├── acquisition-diagram.js       # SVG acquisition timeline diagrams
│   │   └── protocol-comparison-index.json  # Pre-generated index (auto-built by CI)
│   └── custom_css/extra.css
├── scripts/                 # Utility scripts (see scripts/scripts_summary.md)
├── data/                    # Normalized CSV exports of protocol data
├── config/
│   └── institution.yml     # Institution-specific config (used by generate_sitemap.py)
└── mkdocs.yml              # Site configuration
```

## Getting Started

**Prerequisites:** Python 3.9+

```bash
git clone https://github.com/dfergs93/protocol_manager.git
cd protocol_manager
python -m venv venv
source venv/bin/activate
pip install mkdocs-material pymdown-extensions mkdocs-awesome-pages-plugin pyyaml
mkdocs serve
# Site at http://127.0.0.1:8000/radiology-protocols/
```

## Adding or Editing Protocols

Protocol pages live in `docs/ct/<body_part>/<protocol_name>.md`. Each file has YAML front matter plus a rendered Markdown body.

**To update front matter on existing files:**
```bash
python scripts/extract_to_frontmatter.py          # dry run
python scripts/extract_to_frontmatter.py --apply  # writes changes
```

**To generate all protocol files from scratch (new institution fork):**
```bash
python scripts/build_from_csv.py          # dry run
python scripts/build_from_csv.py --apply  # writes Markdown files
```

After editing protocols, regenerate the comparison index before deploying:
```bash
python scripts/generate_comparison_index.py
```

## Deployment

CI (`.github/workflows/ci.yml`) runs on every push to `main`:
1. Generates `docs/javascripts/protocol-comparison-index.json`
2. Generates `docs/javascripts/sitemap.json`
3. Deploys to GitHub Pages via `mkdocs gh-deploy --force`

## Forking for Another Institution

1. Fork this repo
2. Fill in `config/institution.yml` with your institution details
3. Populate `data/protocols.csv` and `data/protocol_series.csv` with your protocol data
4. Run `python scripts/build_from_csv.py --apply` to generate protocol pages
5. Update `mkdocs.yml` `site_name` and `site_url`
6. Push to `main` — CI deploys automatically
