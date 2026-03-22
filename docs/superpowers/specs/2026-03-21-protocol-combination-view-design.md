# Protocol Combination View — Design Spec

**Date:** 2026-03-21
**Status:** Approved
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

## Architecture

All merge logic lives in an isolated `mergeProtocols(protocolA, protocolB)` function that returns a structured `mergedProtocol` object. The rendering functions consume this object. This separation allows the merge logic to be upgraded (toward smarter Option B behaviour) without touching the UI layer.

```
mergeProtocols(a, b) → mergedProtocol
  ├── mergeContrast(a.contrast, b.contrast) → mergedContrast + conflicts[]
  ├── mergeSeries(a.series, b.series, mergedContrast) → mergedSeries[] + conflicts[]
  └── mergeGantt(a, b, mergedContrast) → ganttString

displayCombinedProtocol(mergedProtocol)
  ├── renderCombinedGantt()
  ├── renderCombinedContrastTable()
  └── renderCombinedSeriesList()
```

---

## Sections

### 1. Combined Gantt Timeline

A single Mermaid Gantt showing:
- One contrast injection bar (duration = merged volume ÷ merged flow rate)
- One saline flush bar immediately after
- All scan series from both protocols ordered by timing:
  - Bolus-tracked series fire first (after trigger threshold is reached)
  - Fixed-delay series follow in ascending delay order

If the two protocols use different contrast agents, a **warning banner** appears above the Gantt noting the conflict and the assumption made.

### 2. Combined Contrast Table

A single-row table with these fields:

| Field | Merge Logic |
|---|---|
| Agent | Use Protocol A's agent; flag as conflict if different from B |
| Volume | Take the larger of the two volumes |
| Flow Rate | Take the higher of the two flow rates |
| Timing Method | Prefer "Bolus Tracking" if either protocol uses it |
| Trigger (HU) | From whichever protocol uses bolus tracking |

Any field where the two protocols disagreed is **highlighted yellow** with a short conflict note (e.g., "Isovue 370 vs Omnipaque 350 — verify with radiologist").

### 3. Combined Series List

All series from both protocols listed in a single table, ordered by timing (bolus-tracked first, then fixed delay ascending). Scout series are excluded (consistent with existing comparison behaviour).

**Body coverage conflict detection:** For each pair of series (one from each protocol), flag a conflict if:
- Their body coverage regions overlap (detected by string-matching anatomical landmarks: "chest", "thoracic", "abdomen", "pelvis", "diaphragm", "femoral", etc.)
- Their timing phase is the same or close (same delay value, or both bolus-tracked arterial)

Flagged conflicts appear as a warning row between the conflicting series, e.g.:
> "⚠ Overlap: Gated CTA Chest and CTA Chest both cover chest in arterial phase — consider collapsing into one acquisition."

---

## Conflict Flags Summary

A collapsible "Conflicts & Assumptions" panel above the combined sections lists all detected conflicts in one place, so the clinician doesn't have to hunt through the tables.

---

## UI Placement

```
[Existing: Timeline Comparison]
[Existing: Contrast Strategy Comparison]
[Existing: Acquisition Series Comparison]
─────────────────────────────────────────
[New: Combined Protocol]
  ⚠ Conflicts & Assumptions (collapsible)
  Combined Timeline
  Combined Contrast Strategy
  Combined Acquisition Series
```

The combined section is only rendered when exactly 2 protocols are selected.

---

## Implementation Notes

- The `mergeProtocols()` function is the only place merge logic lives — keep rendering functions dumb consumers of its output
- Body coverage conflict detection uses string matching for now; this is the most likely thing to be upgraded in Option B
- Yellow highlight on conflicting contrast fields reuses MkDocs Material's `--md-warning-fg-color` and `--md-warning-bg-color` CSS variables for theme compatibility
- No backend changes required — all data is already in `protocol-comparison-index.json`
