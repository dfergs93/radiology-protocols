# Custom Acquisition Diagram Design Spec

Date: 2026-03-31

## Overview

A custom SVG acquisition diagram renderer that replaces Mermaid Gantt diagrams for visualizing CT/MRI protocol injection and acquisition sequences. The renderer visualizes contrast injection timelines, saline administration, and phase acquisition windows in a clear, medical-context-aware format.

## Renderer Interface

### Function Signature

```javascript
renderAcquisitionDiagram(container, data)
```

**Parameters:**
- `container` (HTMLElement): Target DOM element to render into
- `data` (Object): Acquisition timeline data object

### Data Shape

```javascript
{
  contrast: {
    volume,           // mL (number)
    flowRate,         // mL/s (number)
    durationSeconds   // seconds (number)
  } | null,           // null = non-contrast only protocol
  
  saline: {
    durationSeconds   // seconds (number)
  } | null,           // null = no saline administration
  
  phases: [
    {
      name,             // string: phase name (e.g., "Arterial", "Portal")
      range,            // string: acquisition window range (e.g., "liver", "kidney")
      delaySeconds,     // seconds from injection start (number)
      durationSeconds,  // acquisition window duration in seconds (number)
      type              // enum: 'non-contrast' | 'arterial' | 'portal' | 'venous' | 'delayed' | 'other'
    },
    // ... additional phases
  ]
}
```

## Layout Specification

### Row Structure

- **Row 0 (top):** Contrast injection bar + Saline bar (omitted entirely for non-contrast-only protocols)
- **Rows 1–N:** One row per unique `phase.range` value
  - All phases (non-contrast and contrast) sharing the same range value share a single row
  - Rows are separated by consistent spacing

### Time Axis

- **Horizontal axis:** Time in seconds, starting at t=0 (injection start)
- **Visual representation:** Second labels displayed below axis
- **Non-contrast protocols:** Axis labeled "Scan start" at t=0 (instead of "Injection start")
- **Non-contrast phase positioning:** Rendered at a fixed visual offset of –20 seconds for visual separation (not clinically accurate; purely for UI clarity)

### SVG Dimensions

- **Bar height:** 18px with 4px rounded corners
- **Row height:** 28px (includes bar + spacing)
- **Total height:** (numRows × rowHeight) + axisHeight
- **Responsive:** SVG uses `viewBox` scaling; width set to 100%
- **Axis components:**
  - Horizontal line at bottom
  - Tick marks at regular intervals
  - Second label annotations

### Visual Elements

- Vertical milestone line at t=0 for injection start / scan start reference
- Clear visual distinction between rows via row height spacing

## Color Scheme

| Component | Type | Color Code | Hex |
|-----------|------|-----------|-----|
| Contrast Injection | Injection | Green | `#4caf50` |
| Saline | Injection | Light Blue | `#4ed5ff` |
| Non-Contrast Phase | Phase | Gray | `#9e9e9e` |
| Arterial Phase | Phase | Red | `#f44336` |
| Portal / Venous Phase | Phase | Blue | `#2196f3` |
| Delayed Phase | Phase | Dark Blue | `#1565c0` |
| Other Phase | Phase | Gray | `#9e9e9e` |

**Application:**
- Contrast and saline bars use their respective colors
- Phase acquisition bars use the color corresponding to their `type` field

## Data Adapters

Two adapters provide protocol data to the renderer. Both call the same `renderAcquisitionDiagram()` function; they differ only in data source.

### 1. DOM Adapter: `parseProtocolFromDOM(pageContainer)`

**Source:** Individual protocol page HTML tables

**Extraction:**
- Reads "Injection Parameters" table (contrast volume, flow rate)
- Reads "Series Acquisition" table (phase names, ranges, delays, durations)

**Usage:** Called on individual protocol documentation pages to extract and render acquisition diagrams directly from the page structure.

**Output:** Returns data object ready for renderer

### 2. JSON Adapter

**Source:** Comparison index JSON entries (already pre-computed)

**Extraction:**
- Comparison index JSON contains pre-extracted injection and phase fields
- `protocol-compare.js` and `protocoller.js` build data objects from JSON

**Usage:**
- `protocol-compare.js` (side-by-side protocol comparison)
- `protocoller.js` (protocol recommendation tool)

**Output:** Data object built from JSON; passed directly to renderer

## Delay Parsing Rules

The `delaySeconds` value is extracted from the series acquisition table "Delay" column. The following rules apply:

| Input Value | Parsed Result |
|-------------|---------------|
| Numeric string (e.g., `"70 sec"`) | Parse as integer seconds (e.g., 70) |
| `"Bolus tracked"` or `"Bolus tracking"` | Use injection duration (end of contrast bar) as delay |
| `"Immediate"` | 0 seconds (same as injection start) |
| `"N/A"` or empty string | 0 seconds (treat as non-contrast or immediate) |
| Numeric strings (e.g., `"70"`) | Parse as integer |

**Special Cases:**

- **Non-contrast phases:** Where `contrast_agent` is "N/A" or series row indicates no contrast dependency, set `delaySeconds = -20` for rendering (visual offset only; not clinically accurate)
- **Non-contrast-only protocols:** No injection row rendered; axis labeled "Scan start"

## Implementation Notes

### File Location

New file: `docs/javascripts/acquisition-diagram.js`

### Dependencies

- No external visualization library dependencies (SVG native)
- Supports rendering into any HTMLElement container

### Responsive Behavior

- SVG viewBox scales content
- Container width set to 100% of parent
- Maintains aspect ratio based on data dimensions

### Error Handling

- Missing or malformed data fields should gracefully degrade (omit rows/components rather than fail)
- Null `contrast` field → omit injection row
- Null `saline` field → omit saline bar
- Empty `phases` array → render only axis

---

## Version History

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| 1.0 | 2026-03-31 | Draft | Initial design specification |
