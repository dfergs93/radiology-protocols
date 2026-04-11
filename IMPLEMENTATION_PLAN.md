# Workflow Redesign: Plug-and-Play Protocol Platform

## Context

The current CSV → Markdown pipeline has diverged. The `batch_create_from_csv.py` script and `csv/` directory no longer exist; the Markdown files are the living source of truth. Structured data is embedded in Markdown body text, parsed at build time via fragile regex. This makes onboarding a new hospital hard because there is no clean data layer to "swap out." The goal is to redesign the data model and workflows so any hospital can fork, fill in their data, and deploy — and so Rads can safely update protocols without breaking site structure.

---

## Proposed Architecture

### The Core Change: YAML Front Matter as the Data Layer

Every Markdown file gains a YAML front matter block. This becomes the **single source of truth for all structured/machine-readable data**. The Markdown body remains the **display layer** — human-edited rich content that doesn't need to be round-tripped through a script.

This solves the current tension: the CSV/script owns the data, Markdown owns the formatting — they can each evolve independently.

```
docs/ct/chest/ct-pulmonary-embolism.md
┌─────────────────────────────────────────────────────────────┐
│ ---                                                         │  ← YAML front matter
│ title: CT Pulmonary Embolism                                │    (structured, machine-readable)
│ slug: ct-pe                                                 │    generated from CSV initially,
│ synonyms: [CTPA, PE protocol, pulmonary angiography]        │    editable directly afterward
│ category: chest                                             │
│ protocol_type: contrast-enhanced                            │
│ contrast:                                                   │
│   agent: Isovue 370                                         │
│   volume: 1.3 mL/kg                                         │
│   flow_rate: 5 mL/s                                         │
│ series: [...]                                               │
│ ---                                                         │
│                                                             │
│ # CT Pulmonary Embolism                                     │  ← Markdown body
│                                                             │    (rich, display content)
│ ...tabs, tables, admonitions...                             │
└─────────────────────────────────────────────────────────────┘
```

### Why Not Keep CSV as Ongoing Source of Truth?

CSV is great for a one-time bulk load but a poor ongoing format because:
- Multi-valued fields (series list, indications list) are awkward to encode
- A Rad editing contrast dose shouldn't need to know which CSV row maps to which file
- The display/editorial content (notes, tips) doesn't belong in a spreadsheet

**The proposed role of CSV changes**: it becomes a *migration/onboarding tool only*, not an ongoing master. After import, YAML front matter *is* the CSV.

---

## Recommended CSV Structure

### Two files: `protocols.csv` + `protocol_series.csv`

Splitting series into a second file avoids the "encode a list in a cell" problem and keeps the main CSV readable in Excel.

#### `protocols.csv`

| Column | Example | Notes |
|--------|---------|-------|
| `slug` | `ct-pe` | URL-safe, unique ID. Also the filename root |
| `title` | `CT Pulmonary Embolism` | Display title |
| `category` | `chest` | Folder under `docs/ct/` |
| `protocol_type` | `contrast-enhanced` | For filtering/display |
| `last_updated` | `2026-01-01` | |
| `author` | `Dr. Smith` | Optional |
| `synonyms` | `CTPA\|PE protocol\|pulmonary angiography` | Pipe-separated |
| `clinical_indications` | `Suspected PE\|Acute dyspnea\|Elevated D-dimer` | Pipe-separated |
| `position` | `Supine feet-first, arms raised` | |
| `npo` | `NPO 2 hours` | |
| `premedication` | `` | Empty if none |
| `contrast_agent` | `Isovue 370` | `N/A` for non-contrast |
| `contrast_volume` | `1.3 mL/kg` | |
| `contrast_flow_rate` | `5 mL/s` | |
| `contrast_duration` | `15-20s` | **New field you added** |
| `contrast_timing` | `Bolus Tracking` | |
| `contrast_roi` | `Main Pulmonary Artery` | |
| `contrast_trigger` | `100 HU` | |
| `kv` | `100` | |
| `mas` | `Auto (ref 200)` | |
| `rotation_time` | `0.5` | |
| `pitch` | `1.0-1.2` | |
| `tech_notes` | `Caudocranial scan direction...` | |
| `nursing_notes` | `20G or larger IV...` | |
| `rad_notes` | `Assess RV/LV ratio...` | |
| `tips` | `Arms fully raised...` | |
| `additional_recons` | `MIP reconstructions of PA` | |
| `safety_renal` | `Verify eGFR > 30` | |
| `safety_allergy` | `Check iodine allergy history` | |

#### `protocol_series.csv`

One file covers both acquisition series and post-processing recons, distinguished by `row_type`.

| Column | Example (acquisition) | Example (recon) | Notes |
|--------|-----------------------|-----------------|-------|
| `slug` | `ct-pe` | `ct-pe` | FK to protocols.csv |
| `row_type` | `acquisition` | `recon` | Drives which template section this row populates |
| `order` | `1` | `1` | Row order within type |
| `series_name` / `plane` | `Pulmonary Angiogram` | `Axial` | Column shared, role differs by row_type |
| `start_location` | `Lung apices` | _(blank)_ | Acquisition only |
| `end_location` | `Adrenal glands` | _(blank)_ | Acquisition only |
| `delay` | `Bolus tracked` | _(blank)_ | Acquisition only |
| `slice_thickness` | `0.625 mm` | _(blank)_ | Acquisition only |
| `acquisition` | _(blank)_ | `Angiogram` | Recon only |
| `fov` | _(blank)_ | `Chest` | Recon only |
| `thickness_increment` | _(blank)_ | `1.25 mm/1.25 mm` | Recon only |
| `kernel` | _(blank)_ | `Standard` | Recon only |
| `ir_strength` | _(blank)_ | `3` | Recon only |
| `notes` | `Caudocranial direction` | `Mediastinal window` | Both types |

---

## Migration Workflow (New Hospital Onboarding)

```
1. Fork repo
2. Edit config/institution.yml   ← name, site_url, logo, contact info
3. Fill in data/protocols.csv
         data/protocol_series.csv
4. python scripts/build_from_csv.py   ← generates Markdown files with YAML front matter
5. Review generated files, make any editorial edits
6. git push → GitHub Actions builds & deploys to GitHub Pages
```

`build_from_csv.py` would:
- Read `protocols.csv` and `protocol_series.csv`
- For each row: generate a Markdown file using the template
- Embed all structured data as YAML front matter
- Render human-readable sections (notes, tables) in the body
- Regenerate `protocol-comparison-index.json`
- Regenerate `sitemap.json` → written to `docs/javascripts/sitemap.json`

**For the existing/your institution**: a one-time `scripts/extract_to_frontmatter.py` script reads the existing Markdown files, extracts structured data via the current regex logic, and writes it back as front matter. This is a one-time migration.

---

## Ongoing Upkeep Workflow (Rads)

**Near-term (no CMS):**
- Rads request changes via email/ticket to IT
- IT edits YAML front matter directly and pushes → CI rebuilds
- Small change (contrast dose) = 2-line YAML edit, no Markdown knowledge needed

**Later (Decap CMS option):**
- Decap CMS configured to expose front matter fields as form inputs
- Rads log in at `https://<hospital>.github.io/<repo>/admin`
- Change a field → submits a GitHub commit → CI rebuilds
- No GitHub knowledge required for Rads

---

## Sitemap Generation

Once front matter is in place, `scripts/generate_sitemap.py`:
- Scans all `docs/ct/**/*.md` front matter
- Uses `slug` as the URL path key (no more manual editing or regex slug inference)
- Includes `synonyms` as match aliases
- Includes `clinical_indications` for query matching
- Outputs `sitemap.json` to a configurable path in this repo (e.g., `docs/javascripts/sitemap.json` so it's available at the deployed Pages URL)

The **extension/aggregator repo** then polls or pulls this URL to incorporate it alongside sitemaps from other institutions. No cross-repo push needed; the extension generates or merges them at query time.

Sitemap entry shape:
```json
{
  "slug": "ct-pe",
  "title": "CT Pulmonary Embolism",
  "url": "https://hospital.github.io/radiology-protocols/ct/chest/ct-pe/",
  "synonyms": ["CTPA", "PE protocol", "pulmonary angiography"],
  "clinical_indications": ["suspected PE", "acute dyspnea"],
  "category": "chest"
}
```

---

## Files to Create / Modify

| File | Action | Purpose |
|------|--------|---------|
| `config/institution.yml` | **Create** | Institution-specific settings (name, URL, logo) |
| `data/protocols.csv` | **Create** | Master protocol data for onboarding |
| `data/protocol_series.csv` | **Create** | Series acquisition data |
| `scripts/build_from_csv.py` | **Create** | CSV → Markdown + front matter generator |
| `scripts/extract_to_frontmatter.py` | **Create** | One-time migration: existing Md → add front matter |
| `scripts/generate_sitemap.py` | **Create** | Front matter → sitemap.json |
| `scripts/generate_comparison_index.py` | **Modify** | Read front matter instead of regex-parsing body |
| `docs/ct/**/*.md` | **Modify** (via script) | Add YAML front matter |
| `.github/workflows/ci.yml` | **Modify** | Add steps: run comparison index + sitemap generation |
| `scripts/scripts_summary.md` | **Modify** | Update documentation |

---

## Resolved Design Decisions

| Question | Decision |
|----------|----------|
| Series vs recon CSV | Both rows in `protocol_series.csv`, distinguished by `row_type` |
| Sitemap delivery | Generated locally to `docs/javascripts/sitemap.json`; extension repo polls the Pages URL |
| Post-processing recons | Captured in `protocol_series.csv` (recon rows), not a third file |
| Backward compatibility during migration | `extract_to_frontmatter.py` migrates existing files first; `generate_comparison_index.py` is then updated to read front matter only (no regex fallback needed since migration runs before the switch) |

---

## Verification

- Run `python scripts/build_from_csv.py` on a sample CSV with 3-5 protocols → inspect generated Markdown for correct front matter + body structure
- Run `python scripts/generate_comparison_index.py` → verify it reads from front matter and output JSON matches current structure consumed by `protocol-compare.js`
- Run `python scripts/generate_sitemap.py` → verify slugs/synonyms land correctly, no manual edits needed
- Deploy the site (`mkdocs serve`) and confirm comparison tool still works
- Verify GitHub Actions CI pipeline runs all scripts before `mkdocs gh-deploy`
