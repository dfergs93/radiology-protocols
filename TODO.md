# Project TODO

## 1. CT Protocol Accuracy (Highest Priority)
Focus areas: **cardiac**, **vascular**, **chest**

- [ ] Fix acquisition series (series names, phases, coverage)
- [ ] Audit SVG timing diagrams for accuracy

---

## 2. Protocol Comparison UI

- [ ] Add diff/highlight view to surface differences between selected protocols
- [ ] Add "combination" view showing how two protocols could be merged or run together (the original spec file is no longer in the repo; needs re-writing)

---

## 3. Data Layer

- [x] Validate that all protocol Markdown files have complete YAML front matter (`validate_protocols.py`, enforced in CI)
- [ ] Ensure `data/protocols.csv` and `data/protocol_series.csv` stay in sync with `docs/ct/` files

---

## 4. Forking / Multi-Institution

- [x] Validate `build_from_csv.py` produces a complete site from only the CSV files (87/87 valid, Oct 2026)
