# CLAUDE.md

## Protocol Manager Platform

A MkDocs (Material theme) static site serving CT protocol documentation with interactive protocol comparison, available via GitHub Pages at https://dfergs93.github.io/radiology-protocols/

There is no backend server. See `docs/architecture-decisions.md` for decisions about what was built, what was abandoned (and why), and what is in progress.

## Architecture

```
radiology-protocols/
├── docs/                    # Content source files
│   ├── ct/                 # CT Protocols (Markdown + YAML front matter); MR will live in docs/mr/
│   ├── review-status.md    # Review Status page (overdue / due soon / never reviewed)
│   ├── javascripts/        # Custom frontend logic
│   │   ├── protocol-compare.js          # Side-by-side comparison tool
│   │   ├── acquisition-diagram.js       # SVG acquisition timeline diagrams
│   │   ├── review-status.js             # Review Status page logic
│   │   └── protocol-comparison-index.json  # Pre-generated index (auto-built by CI)
│   └── custom_css/extra.css # styling overrides
├── scripts/                 # Utility scripts (see scripts/scripts_summary.md)
│   ├── extract_to_frontmatter.py    # add/update YAML front matter on existing protocol files
│   ├── build_from_csv.py            # generate protocol files from CSV (new institution onboarding)
│   ├── generate_comparison_index.py # build comparison index JSON (run by CI)
│   ├── generate_sitemap.py          # build sitemap JSON for radiology-agent extension (run by CI)
│   ├── validate_protocols.py        # validate front matter against schema/ (CI + pre-commit)
│   └── admin.py                     # local Flask editor
├── schema/protocol.schema.json  # allowed protocol fields — update it when adding a field
├── tests/                   # pytest suite (python -m pytest -q tests)
├── data/                    # Normalized CSV exports of protocol data
│   ├── protocols.csv        # one row per protocol
│   └── protocol_series.csv  # one row per acquisition series
├── config/
│   └── institution.yml      # institution-specific config
└── mkdocs.yml              # Site configuration
```

## Conventions

- **No external network requests from the site.** It must run on internal hospital networks: no CDN scripts, no web fonts (`theme.font: false`). Vendor any new JS library into `docs/javascripts/`.
- **No hard-coded base path** (`/radiology-protocols/`). Resolve URLs relative to the script (`document.currentScript.src`) or use relative links.
- **Vendor-neutral fields.** Field names stay generic (kernel: Standard/Bone/Lung); scanner-specific details go in free-text values.
- **Every new front matter field must be added to `schema/protocol.schema.json`**, or validation fails. `slug` must equal the file name; `category` the folder; `modality` the top-level folder (`ct` → CT, `mr` → MR).
- Before pushing: `python scripts/validate_protocols.py && python -m pytest -q tests && mkdocs build --strict`.
