# CLAUDE.md

## Protocol Manager Platform

A MkDocs (Material theme) static site serving CT protocol documentation with interactive protocol comparison, available via GitHub Pages at https://dfergs93.github.io/radiology-protocols/

There is no backend server. See `docs/architecture-decisions.md` for decisions about what was built, what was abandoned (and why), and what is in progress.

## Architecture

```
protocol_manager/
├── docs/                    # Content source files
│   ├── ct/                 # CT Protocols (Markdown + YAML front matter)
│   ├── javascripts/        # Custom frontend logic
│   │   ├── protocol-compare.js          # Side-by-side comparison tool
│   │   ├── acquisition-diagram.js       # SVG acquisition timeline diagrams
│   │   └── protocol-comparison-index.json  # Pre-generated index (auto-built by CI)
│   └── custom_css/extra.css # styling overrides
├── scripts/                 # Utility scripts (see scripts/scripts_summary.md)
│   ├── extract_to_frontmatter.py    # add/update YAML front matter on existing protocol files
│   ├── build_from_csv.py            # generate protocol files from CSV (new institution onboarding)
│   ├── generate_comparison_index.py # build comparison index JSON (run by CI)
│   └── generate_sitemap.py          # build sitemap JSON for radiology-agent extension (run by CI)
├── data/                    # Normalized CSV exports of protocol data
│   ├── protocols.csv        # one row per protocol
│   └── protocol_series.csv  # one row per acquisition series
├── config/
│   └── institution.yml      # institution-specific config
└── mkdocs.yml              # Site configuration
```
