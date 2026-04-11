# Homepage Grid Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-extended-cc:subagent-driven-development (recommended) or superpowers-extended-cc:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a 3-column body-region grid to the homepage below the existing hero buttons, replacing the "What's Here" prose section.

**Architecture:** Pure static site changes — two files only. The CSS already has `.body-part-card` styles; Task 1 adjusts them for a fixed 3-column layout and adds a section heading style. Task 2 rewrites `docs/index.md` to use those classes.

**Tech Stack:** MkDocs Material theme, HTML-in-Markdown (`md_in_html` extension enabled), plain CSS custom properties.

---

### Task 1: Update CSS for 3-column grid

**Goal:** Adjust `.body-parts-grid` to use a fixed 3-column layout and add the section heading + last-card centering rules.

**Files:**
- Modify: `docs/custom_css/extra.css:111-116`

**Acceptance Criteria:**
- [ ] `.body-parts-grid` uses `repeat(3, 1fr)` columns (not `auto-fill minmax`)
- [ ] `.body-part-card.last` is defined and sets `grid-column: 2` to center it
- [ ] `.body-parts-section-heading` style exists with uppercase, light-color label appearance

**Verify:** `grep -n "repeat(3, 1fr)\|body-part-card.last\|body-parts-section-heading" docs/custom_css/extra.css` → 3 matches

**Steps:**

- [ ] **Step 1: Change `grid-template-columns` in `.body-parts-grid`**

  In `docs/custom_css/extra.css`, replace lines 111–116:

  ```css
  /* Body Parts Grid */
  .body-parts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.25rem;
    margin: 2rem 0;
  }
  ```

  With:

  ```css
  /* Body Parts Grid */
  .body-parts-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.25rem;
    margin: 1.5rem 0;
  }
  ```

- [ ] **Step 2: Add `.body-part-card.last` and `.body-parts-section-heading` rules**

  Immediately after the closing brace of the `.body-parts-grid` block (after the new line 116), insert:

  ```css
  .body-parts-grid .body-part-card.last {
    grid-column: 2;
  }

  .body-parts-section-heading {
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--md-default-fg-color--light);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0.5rem 0 0;
  }
  ```

- [ ] **Step 3: Verify the three rules exist**

  Run: `grep -n "repeat(3, 1fr)\|body-part-card.last\|body-parts-section-heading" docs/custom_css/extra.css`

  Expected: 3 lines printed, one for each pattern.

- [ ] **Step 4: Commit**

  ```bash
  git add docs/custom_css/extra.css
  git commit -m "style: update body-parts grid to 3-column fixed layout"
  ```

---

### Task 2: Rewrite homepage markup

**Goal:** Replace the "What's Here" prose section in `docs/index.md` with a divider, section heading, and 7-card region grid.

**Files:**
- Modify: `docs/index.md`

**Acceptance Criteria:**
- [ ] The `## What's Here` section and its three paragraphs are removed
- [ ] A `<p class="body-parts-section-heading">` label appears after the `---` divider
- [ ] A `<div class="body-parts-grid">` contains exactly 7 `<a class="body-part-card">` elements
- [ ] The Trauma card has class `body-part-card last`
- [ ] All 7 cards link to their correct absolute paths (matching the `/radiology-protocols/ct/<region>/` pattern used by existing hero buttons)

**Verify:** `mkdocs serve` → open http://127.0.0.1:8000/radiology-protocols/ → confirm grid renders with 3 columns, 7 cards, Trauma centered on last row. Hover a card to confirm border + lift animation.

**Steps:**

- [ ] **Step 1: Replace everything after the hero buttons block in `docs/index.md`**

  The current file ends with:

  ```markdown
  ---

  ## What's Here

  **Protocol pages** — One page per CT exam. Covers contrast agent, injection rate, volume, timing, kV/mAs, and each acquisition series. Includes an SVG phase diagram.

  **Comparison tool** — Select two or more protocols to view parameters side-by-side. URLs are deep-linkable, so comparisons can be bookmarked and shared.

  **Full-text search** — Use the search bar at the top right to find protocols by name, indication, or parameter.
  ```

  Replace it with:

  ```markdown
  ---

  <p class="body-parts-section-heading">Browse by Body Region</p>

  <div class="body-parts-grid" markdown="1">
    <a href="/radiology-protocols/ct/chest/" class="body-part-card">
      <span class="body-part-icon">🫁</span>
      <h3>Chest</h3>
    </a>
    <a href="/radiology-protocols/ct/abdomen/" class="body-part-card">
      <span class="body-part-icon">🫃</span>
      <h3>Abdomen</h3>
    </a>
    <a href="/radiology-protocols/ct/cardiac/" class="body-part-card">
      <span class="body-part-icon">❤️</span>
      <h3>Cardiac</h3>
    </a>
    <a href="/radiology-protocols/ct/neuro/" class="body-part-card">
      <span class="body-part-icon">🧠</span>
      <h3>Neuro</h3>
    </a>
    <a href="/radiology-protocols/ct/msk/" class="body-part-card">
      <span class="body-part-icon">🦴</span>
      <h3>MSK</h3>
    </a>
    <a href="/radiology-protocols/ct/vascular/" class="body-part-card">
      <span class="body-part-icon">🩸</span>
      <h3>Vascular</h3>
    </a>
    <a href="/radiology-protocols/ct/trauma/" class="body-part-card last">
      <span class="body-part-icon">🚑</span>
      <h3>Trauma</h3>
    </a>
  </div>
  ```

- [ ] **Step 2: Verify card count and Trauma class**

  Run:
  ```bash
  grep -c "body-part-card" docs/index.md
  grep "body-part-card last" docs/index.md
  ```

  Expected:
  - First command: `8` (7 anchor tags + 1 div class reference)
  - Second command: one line containing `trauma` and `last`

- [ ] **Step 3: Serve the site and visually verify**

  Run: `mkdocs serve`

  Open: http://127.0.0.1:8000/radiology-protocols/

  Check:
  - Grid renders below the hero buttons
  - 3 columns on the first two rows
  - Trauma card is alone on the third row, centered
  - Hovering a card shows blue border and lift effect
  - Each card navigates to its region index page

- [ ] **Step 4: Commit**

  ```bash
  git add docs/index.md
  git commit -m "feat: add body-region grid to homepage"
  ```
