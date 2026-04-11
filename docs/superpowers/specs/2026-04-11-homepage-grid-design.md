# Homepage Grid Redesign

**Date:** 2026-04-11  
**Status:** Approved

## Summary

Redesign the CT Protocol Reference homepage to add a body-region grid below the existing hero buttons, giving users a fast visual path to any region without removing the existing navigation affordances.

## Design

### Page Structure

The homepage keeps its existing shape at the top and adds a grid section below the hero buttons:

1. **Title** — "CT Protocol Reference" (unchanged)
2. **Tagline** — one-line description (unchanged)
3. **Hero buttons** — "Compare Protocols" (primary) + "Browse Protocols" (secondary) (unchanged)
4. **Divider** — `<hr>` separator
5. **Section heading** — "Browse by Body Region" (small uppercase label)
6. **Region grid** — 3-column grid of region cards (new)

The existing "What's Here" prose section (`## What's Here`) is removed. The grid replaces it as the body of the page.

### Region Grid

Seven cards, one per body region, in a 3-column CSS grid:

| Row | Cards |
|-----|-------|
| 1 | Chest, Abdomen, Cardiac |
| 2 | Neuro, MSK, Vascular |
| 3 | Trauma (centered via `grid-column: 2`) |

**Card content:** Icon (emoji) + region name only. No protocol count, no description text.

**Card behavior:**
- Links to the region index page (e.g. `/ct/chest/`)
- Hover: border turns primary blue, card lifts 4px, soft blue glow shadow

**Icons:**
- Chest — 🫁
- Abdomen — 🫃
- Cardiac — ❤️
- Neuro — 🧠
- MSK — 🦴
- Vascular — 🩸
- Trauma — 🚑

### Implementation Approach

The existing `extra.css` already contains `.body-parts-grid` and `.body-part-card` styles. These will be reused with minor adjustments:

- Override `grid-template-columns` to `repeat(3, 1fr)` (existing rule uses `auto-fill minmax(280px)`)
- Add `grid-column: 2` on the Trauma card to center it in the last row
- Add a `.body-parts-section-heading` style for the small uppercase label

Changes are confined to:
- `docs/index.md` — replace "What's Here" section with grid markup
- `docs/custom_css/extra.css` — add/adjust grid and heading styles

No JavaScript required.

## Out of Scope

- Protocol count badges on cards
- Keyword summaries on cards
- Any changes to region index pages (`docs/ct/*/index.md`)
- Any changes to the comparison tool or nav structure
