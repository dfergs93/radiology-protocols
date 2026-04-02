# CLAUDE.md

## Protocol Manager Platform

A MkDocs (Material theme) static site serving CT protocol documentation with interactive protocol comparison, available via github pages at https://dfergs93.github.io/radiology-protocols/
Previously, a backend for protocol help was developed, but removed for now.

## Architecture

```
protocol_manager/
├── docs/                    # Content source files
│   ├── ct/                 # CT Protocols (Markdown)
│   ├── guidelines/         # Clinical Guidelines (Markdown)
│   ├── javascripts/        # Custom frontend logic
│   ├──── protocol-compare.js # Side-by-side protocol comparison tool
│   ├──── protocol-comparison-index.json # Pre-generated index read by protocol-compare.js
│   └── custom_css/extra.css # styling overrides
├── scripts/                 # Utility scripts
|   └── scripts_summary.md # summary of scripts
│   └── generate_comparison_index.py # generate comparison index for protocol comparison tool
|   └── batch_create_from_csv.py # batch create protocol markdown files from csv
|   └── protocol_template.py # template for protocol markdown files
├── csv/                 # csv files for batch creation
│   └── protocols.csv # CT protocol master list              
└── mkdocs.yml              # Site configuration
```

