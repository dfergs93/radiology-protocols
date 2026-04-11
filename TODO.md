# Project TODO

## 1. CT Protocol Accuracy (Highest Priority)
Focus areas: **cardiac**, **vascular**, **chest**

- [ ] Fix acquisition series (series names, phases, coverage)
- [ ] Audit SVG timing diagrams for accuracy

---

## 2. Protocol Comparison UI

- [ ] Add diff/highlight view to surface differences between selected protocols
- [ ] Add "combination" view showing how two protocols could be merged or run together (see spec: `docs/superpowers/specs/2026-03-21-protocol-combination-view-design.md`)

---

## 3. Data Layer

- [ ] Validate that all protocol Markdown files have complete YAML front matter (run `extract_to_frontmatter.py` and check output)
- [ ] Ensure `data/protocols.csv` and `data/protocol_series.csv` stay in sync with `docs/ct/` files

---

## 4. Forking / Multi-Institution

- [ ] Validate `build_from_csv.py` produces a complete site from only the CSV files
