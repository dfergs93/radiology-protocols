# Scripts Summary
Description of each script, organized by their purpose

## Data Layer & Migration

1. `extract_to_frontmatter.py`
- **Primary migration script.** Reads all `docs/ct/**/*.md` files, extracts structured protocol data (contrast, series, tech params, notes, safety), and prepends YAML front matter to each file — leaving the Markdown body unchanged.
- Also outputs `data/protocols.csv` and `data/protocol_series.csv` as normalized exports.
- Run with `--apply` to write; default is dry-run.
- **Run this once** when adding front matter to existing Markdown files.

2. `build_from_csv.py`
- **New hospital onboarding script.** Reads `data/protocols.csv` + `data/protocol_series.csv` and generates complete Markdown files with YAML front matter + rendered body sections.
- Use this when forking the repo for a new institution starting from scratch.
- Run with `--apply` to write; default is dry-run.

## Protocol Indexing

1. `generate_comparison_index.py`
- Reads YAML front matter from all `docs/ct/**/*.md` files and outputs `docs/javascripts/protocol-comparison-index.json`.
- Powers the Protocol Comparison UI (`protocol-compare.js`).
- Run automatically by CI before `mkdocs gh-deploy`.

2. `generate_sitemap.py`
- Reads YAML front matter and `config/institution.yml` and outputs `docs/javascripts/sitemap.json`.
- Used by the radiology-agent Chrome extension to discover protocols without cross-repo pushes.
- Run automatically by CI before `mkdocs gh-deploy`.
