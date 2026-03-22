# Protocol Combination View — Design Spec

**Date:** 2026-03-21
**Status:** Draft
**Feature:** Protocol Comparison UI — Combination View

---

## Overview

Add a "Combined Protocol" section to the CT Comparison Tool (`docs/compare.md` + `docs/javascripts/protocol-compare.js`). When two protocols are selected and compared, this section shows what a merged single-session scan would look like: one contrast injection, all acquisition series sequenced against it, and clear conflict flags where the clinician must make a judgment call.

The goal is to give clinicians a starting point for planning a combined scan — not to produce an authoritative protocol automatically.

---

## Scope

- Supports combining **exactly 2 protocols** (3+ is out of scope for this iteration)
- Displayed automatically below the existing comparison sections when 2 protocols are compared
- Informational only — no saving, exporting, or document generation

---

## Prerequisites

The current `protocol-comparison-index.json` does not include `timing` or `trigger` fields on the `contrast` object. Before implementing the combination view, `scripts/generate_comparison_index.py` must be updated to parse and emit these two fields from each protocol's markdown (`Timing Method` and `Trigger (HU)` rows in the injection parameters table). Without this, bolus-tracking detection and trigger merge logic will have no data to operate on.

---

## Data Model

Each protocol object from `protocol-comparison-index.json` currently has:
- `title`, `category`, `filepath`
- `gantt` — pre-rendered Mermaid string (not parsed; the combined Gantt is reconstructed from fields)
- `contrast` — object with: `agent`, `volume`, `flow_rate`, `type` (currently). After the prerequisite above: also `timing`, `trigger`. Any field may be null; the entire object may be null for non-contrast protocols.
- `series` — array of objects with: `name`, `start`, `end`, `delay`, `thickness`, `notes`, `coverage`. Coverage strings use `→` format (e.g., `"Thoracic inlet → Diaphragm"`). Array may be empty.
- `summary` — array of objects with: `series` (the name), `phase`, `coverage`. Coverage strings use `to` format (e.g., `"Thoracic inlet to Diaphragm"`). Fallback when `series` is empty.

**Field formats:**
- `volume` may be a fixed string (`"140 mL"`) or weight-based (`"1.1 mL/kg"`)
- `flow_rate` may be a single value (`"4 mL/s"`) or a range (`"3-4 mL/s"`)
- `delay` may be a duration string (`"70 sec"`), `"N/A"`, `"Bolus tracked"`, or null
- `trigger` may be a freeform string (`"200 HU"`, `"150 HU at aorta"`) or null
- `timing` may be a freeform string (`"Bolus Tracking"`, `"Fixed delay"`) or null

All merge logic operates on these fields. The existing `gantt` string is **not parsed**.

---

## Architecture

All merge logic lives in an isolated `mergeProtocols(protocolA, protocolB)` function that returns a structured `mergedProtocol` object. The rendering functions consume this object. This separation allows the merge logic to be upgraded (toward smarter Option B behaviour) without touching the UI layer.

```
mergeProtocols(a, b) → mergedProtocol
  ├── mergeContrast(a.contrast, b.contrast) → mergedContrast + conflicts[]
  ├── mergeSeries(seriesA, seriesB) → mergedSeries[] + conflicts[]
  └── buildCombinedGantt(mergedContrast, mergedSeries) → ganttString | null

  where seriesA = a.series.length > 0 ? a.series : a.summary
        seriesB = b.series.length > 0 ? b.series : b.summary

displayCombinedProtocol(mergedProtocol)
  ├── renderConflictsPanel()
  ├── renderCombinedGantt()
  ├── renderCombinedContrastTable()
  └── renderCombinedSeriesList()
```

---

## Helper Definitions

**Detecting bolus tracking:** A contrast `timing` field counts as bolus-tracked if it contains "bolus" (case-insensitive). A series `delay` field counts as bolus-tracked if it is null, `"N/A"`, or contains "bolus" (case-insensitive).

**Parsing volume (mL):** Extract the leading number from the volume string (`"140 mL"` → 140, `"1.1 mL/kg"` → 1.1). Weight-based volumes cannot be numerically compared with fixed volumes — treat as non-comparable and fall back to Protocol A's volume and flow rate, with a conflict flag. If both are weight-based, use Protocol A's throughout.

**Parsing flow rate (mL/s):** For ranges (`"3-4 mL/s"`), use the lower bound for injection duration calculations and the upper bound for comparison. Flow rate always comes from the same protocol as volume (the one with the larger fixed volume, or Protocol A as fallback).

**Parsing trigger HU:** Extract the leading integer (`"200 HU"` → 200, `"150 HU at aorta"` → 150). If the anatomical site text after the number differs between protocols, flag as a site mismatch conflict.

**Identifying scout series:** For `series`-sourced entries, pass `item.name` to the existing `isScoutSeries()` function. For `summary`-sourced entries, pass `item.series` (the name field on summary objects is called `series`, not `name`).

**Normalizing coverage strings:** Strip `→` and `to` connectors and normalize to lowercase for comparison. Used for de-duplication and landmark matching. Example: `"Thoracic inlet → Diaphragm"` and `"Thoracic inlet to Diaphragm"` are treated as equal.

---

## Sections

### 1. Combined Gantt Timeline

A single Mermaid Gantt built from scratch:

- **Contrast injection bar:** duration = merged volume (fixed mL) ÷ flow rate lower bound.
- **Saline flush bar:** hardcoded at 30 mL ÷ same flow rate, immediately after contrast.
- **Scan series bars:** bolus-tracked series after contrast trigger, fixed-delay series at their specified times.

**If volume is weight-based:** omit the entire Gantt and render: *"Timeline cannot be computed — one or both protocols use weight-based contrast volumes."* Add this as a conflict in the `conflicts[]` array (so the Conflicts panel will render even if no other conflicts exist).

After injecting the combined Gantt div, call `mermaid.run({ nodes: [ganttElement] })` (Mermaid v10 API — the site loads `mermaid@10`). Do not use the deprecated `mermaid.init()`.

### 2. Combined Contrast Table

A single-row table. Volume and flow rate always come from the same protocol (the one with the larger fixed volume, or Protocol A if non-comparable) to keep injection duration internally consistent.

| Field | Merge Logic |
|---|---|
| Agent | Protocol A's agent; conflict note inline if different from B (e.g., `"Isovue 370 — ⚠ B uses Omnipaque 350, verify with radiologist"`) |
| Volume | Larger fixed volume; fall back to Protocol A if weight-based vs fixed |
| Flow Rate | Upper bound from whichever protocol has the larger volume |
| Timing Method | Prefer "Bolus Tracking" if either uses it; conflict note if methods differ |
| Trigger (HU) | Higher HU if both use bolus tracking; from the bolus-tracking protocol if only one does; conflict note if HU values or sites differ |

All conflicting fields: highlighted yellow (background `--md-warning-bg-color`, fallback `#fff3cd`; text `--md-warning-fg-color`, fallback `#856404`) with an inline conflict note.

**Non-contrast protocol:** If one or both `contrast` objects are null, all fields render as "N/A" with a conflict note naming which protocol has no contrast.

### 3. Combined Series List

All series from both protocols in a single table, ordered by timing. Scout series excluded (using `isScoutSeries()` with the correct field per data source — see Helper Definitions).

**Ordering:**
1. Bolus-tracked series first
2. Fixed-delay series in ascending numeric delay order
3. `summary`-sourced series (no delay field) placed after all `series`-sourced entries
4. Tiebreaker within same group: Protocol A before Protocol B

**De-duplication:** Before ordering, normalize both `name`/`series` and `coverage` fields (see Helper Definitions). If a `series`-sourced and `summary`-sourced entry resolve to the same name and normalized coverage, keep the `series`-sourced entry.

**Empty state:** If no series remain after filtering and de-duplication, render: *"No acquisition series available for combined view."*

**Body coverage conflict detection** (after de-duplication, for pairs where at least one entry is `series`-sourced with a `delay` field):
- **Coverage overlap:** case-insensitive substring match of the normalized coverage string against: `chest`, `thoracic`, `abdomen`, `pelvis`, `diaphragm`, `femoral`, `heart`, `aorta`, `neck`, `head`. Multiple landmark matches in one pair → one conflict raised, using the first matched landmark in the warning message.
- **Timing overlap:** both are bolus-tracked, OR both have the same exact numeric delay value (exact equality is intentional).

When both overlap conditions are met:
> "⚠ Overlap: [Series A name] and [Series B name] both cover [landmark] at similar timing — consider collapsing into one acquisition."

Fixed-delay vs bolus-tracked pairs are never flagged as overlapping. Null `coverage` or `delay` skips detection for that pair.

---

### 4. Conflicts & Assumptions Panel

A collapsible `<details>` element rendered **inside the Combined Protocol block, directly below the section header and above the three sub-sections**. Lists all items in the `conflicts[]` arrays from `mergeContrast` and `mergeSeries`. Rendered whenever `conflicts.length > 0` — including when the only conflict is the Gantt omission notice.

---

## UI Placement

```
[Existing: Timeline Comparison]
[Existing: Contrast Strategy Comparison]
[Existing: Acquisition Series Comparison]
─────────────────────────────────────────
[New: Combined Protocol]
  ⚠ Conflicts & Assumptions (collapsible <details>, if conflicts.length > 0)
  Combined Timeline (or omission message)
  Combined Contrast Strategy
  Combined Acquisition Series
```

Rendered only when exactly 2 protocols are selected.

---

## Implementation Notes

- `mergeProtocols()` is the only place merge logic lives — rendering functions are dumb consumers of its output
- `generate_comparison_index.py` must be updated to emit `timing` and `trigger` fields before this feature works end-to-end
- Body coverage conflict detection uses string matching for now — most likely upgrade point for Option B
- Use `mermaid.run({ nodes: [element] })` (Mermaid v10) scoped to the new Gantt element only
- CSS: background `--md-warning-bg-color` (fallback `#fff3cd`), text `--md-warning-fg-color` (fallback `#856404`)
- No additional backend changes required beyond the index generator update
