# Comparison Tool Deep Linking Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add shareable deep links to the CT Comparison Tool so users can share a URL that auto-populates selected protocols and runs the comparison on load.

**Architecture:** URL query params (`?p=<filepath>&p=<filepath>`) hold protocol identifiers. `history.replaceState` silently updates the address bar when selections change. On page load, `loadFromURL()` reads params, finds matching protocols in `protocolData`, sets select values, and triggers `displayComparison()`. A "Copy Link" button in the toolbar copies the current URL to clipboard.

**Tech Stack:** Vanilla JS, URLSearchParams, History API, Clipboard API, MkDocs Material

---

## File Map

| File | Change |
|---|---|
| `docs/compare.md` | Add `<button id="copy-link-btn">` after the Clear button |
| `docs/javascripts/protocol-compare.js` | Add `updateURL()`, `loadFromURL()`, copy handler; hook `updateURL()` into select change events and clear button |

> **No JS test framework is set up in this project.** Each task uses manual browser verification instead of automated tests. Start `mkdocs serve` and keep the browser open at `http://127.0.0.1:8000/radiology-protocols/compare/` for all verification steps.

---

### Task 1: Add Copy Link button to the comparison page HTML

**Files:**
- Modify: `docs/compare.md:246-248`

- [ ] **Step 1: Add the Copy Link button**

In `docs/compare.md`, find the button group (lines ~246–248):
```html
    <button id="add-protocol-btn" class="md-button">+ Add Protocol</button>
    <button id="compare-btn" class="md-button md-button--primary">Compare</button>
    <button id="clear-btn" class="md-button">Clear</button>
```
Replace with:
```html
    <button id="add-protocol-btn" class="md-button">+ Add Protocol</button>
    <button id="compare-btn" class="md-button md-button--primary">Compare</button>
    <button id="clear-btn" class="md-button">Clear</button>
    <button id="copy-link-btn" class="md-button" style="display:none;">🔗 Copy Link</button>
```

- [ ] **Step 2: Verify button renders (hidden)**

With `mkdocs serve` running, open `http://127.0.0.1:8000/radiology-protocols/compare/` and inspect the DOM (DevTools → Elements). Confirm `#copy-link-btn` exists with `display:none`. It should not be visible yet.

- [ ] **Step 3: Commit**

```bash
git add docs/compare.md
git commit -m "feat: add hidden Copy Link button to comparison toolbar"
```

---

### Task 2: Implement `updateURL()` and hook it into selection changes

**Files:**
- Modify: `docs/javascripts/protocol-compare.js`

`updateURL()` is called whenever a protocol selection changes. It:
- Rebuilds the URL query string from current selections
- Calls `history.replaceState` to silently update the address bar
- Shows or hides the Copy Link button based on selection count
- Auto-triggers `displayComparison()` when 2+ protocols are selected

- [ ] **Step 1: Add `updateURL()` function**

Add this function to `protocol-compare.js` immediately after the closing `}` of `populateSelectors()` (after line 74):

```js
function updateURL() {
  const params = new URLSearchParams();
  const filled = [];

  document.querySelectorAll('.protocol-select').forEach(select => {
    const idx = select.value;
    if (idx !== '' && protocolData[idx]) {
      params.append('p', protocolData[idx].filepath.replace('.md', ''));
      filled.push(protocolData[idx]);
    }
  });

  history.replaceState(null, '', filled.length ? '?' + params.toString() : window.location.pathname);

  const copyBtn = document.getElementById('copy-link-btn');
  if (copyBtn) copyBtn.style.display = filled.length >= 2 ? '' : 'none';

  if (filled.length >= 2) {
    selectedProtocols = filled;
    displayComparison();
  } else {
    document.getElementById('comparison-results').style.display = 'none';
  }
}
```

- [ ] **Step 2: Attach `updateURL` to each select's change event in `populateSelectors()`**

In `populateSelectors()`, the `selects.forEach` block ends with `createSearchableSelect(select);` at line 72. Add the listener guard immediately after it, before the closing `});` of the `forEach`:

```js
    // 4. Transform into searchable select
    createSearchableSelect(select);

    // Attach URL sync listener once per select element
    if (!select.dataset.urlListenerAttached) {
      select.addEventListener('change', updateURL);
      select.dataset.urlListenerAttached = 'true';
    }
  });
}
```

- [ ] **Step 3: Call `updateURL()` in the clear button handler**

The clear button programmatically sets `select.value = ''`, which does not dispatch a `change` event. Add an explicit `updateURL()` call at the end of the clear handler. Find the existing clear button handler (around line 255) and replace it:

```js
// Clear button
document.getElementById('clear-btn')?.addEventListener('click', () => {
  document.querySelectorAll('.protocol-select').forEach(select => {
    select.value = '';
    // Also sync the searchable UI
    createSearchableSelect(select);
  });
  document.getElementById('comparison-results').style.display = 'none';
  updateURL();
});
```

- [ ] **Step 4: Verify URL updates on selection**

In the browser, open the compare page and select two protocols using the searchable dropdowns. Confirm:
1. The address bar updates to `?p=ct/...&p=ct/...` as each protocol is selected
2. The comparison results appear automatically after both are selected
3. The 🔗 Copy Link button becomes visible
4. Clicking Clear resets the URL back to the base path and hides the button

- [ ] **Step 5: Commit**

```bash
git add docs/javascripts/protocol-compare.js
git commit -m "feat: auto-update URL query params when protocol selections change"
```

---

### Task 3: Implement `loadFromURL()` to pre-populate on page load

**Files:**
- Modify: `docs/javascripts/protocol-compare.js`

`loadFromURL()` is called once after `protocolData` is fetched and `populateSelectors()` runs. It reads `?p=` params, finds matching protocols by filepath, sets select values, syncs the searchable UI, and triggers comparison if 2+ valid protocols were found.

- [ ] **Step 1: Add `loadFromURL()` function**

Add this function immediately after `updateURL()`:

```js
function loadFromURL() {
  const filepaths = new URLSearchParams(window.location.search).getAll('p');
  if (filepaths.length === 0) return;

  // Add extra selector slots if URL has more protocols than the default 2
  const existingSelects = document.querySelectorAll('.protocol-select');
  const extraNeeded = filepaths.length - existingSelects.length;
  for (let i = 0; i < extraNeeded; i++) {
    addProtocolSlot();
  }

  const selects = document.querySelectorAll('.protocol-select');
  filepaths.forEach((filepath, i) => {
    const index = protocolData.findIndex(p => p.filepath.replace('.md', '') === filepath);
    if (index === -1 || !selects[i]) return; // silently skip unrecognised protocols
    selects[i].value = index;
    createSearchableSelect(selects[i]); // sync the visible search input to show the title
  });

  const filled = [...document.querySelectorAll('.protocol-select')]
    .map(s => protocolData[s.value])
    .filter(Boolean);

  const copyBtn = document.getElementById('copy-link-btn');
  if (copyBtn && filled.length >= 2) copyBtn.style.display = '';

  if (filled.length >= 2) {
    selectedProtocols = filled;
    displayComparison();
  }
}
```

- [ ] **Step 2: Call `loadFromURL()` after `populateSelectors()` in the fetch handler**

Find the `.then` block that calls `populateSelectors()` (around line 22–25):

```js
    .then(data => {
      console.log('Successfully parsed', data.length, 'protocols');
      protocolData = data;
      populateSelectors();
    })
```

Replace with:

```js
    .then(data => {
      console.log('Successfully parsed', data.length, 'protocols');
      protocolData = data;
      populateSelectors();
      loadFromURL();
    })
```

- [ ] **Step 3: Verify deep link loading**

1. On the compare page, select two protocols (e.g. CT Abdomen Pelvis and CTA Chest). The URL should update.
2. Copy the URL from the address bar.
3. Open a new tab, paste the URL, and navigate to it.
4. Confirm: both protocol dropdowns are pre-filled with the correct protocol names, and the comparison results are displayed automatically.
5. Test with a URL containing a non-existent filepath (e.g., `?p=ct/fake/protocol`). Confirm the page loads without errors and the unrecognised protocol is silently skipped.
6. Test with only one valid `?p=` param. Confirm the selector is pre-filled but the comparison does **not** auto-run.

- [ ] **Step 4: Commit**

```bash
git add docs/javascripts/protocol-compare.js
git commit -m "feat: pre-populate comparison tool from URL query params on load"
```

---

### Task 4: Wire up the Copy Link button

**Files:**
- Modify: `docs/javascripts/protocol-compare.js`

- [ ] **Step 1: Add copy-to-clipboard event handler**

Add this block after the existing clear button handler (after line ~262):

```js
// Copy Link button
document.getElementById('copy-link-btn')?.addEventListener('click', () => {
  navigator.clipboard.writeText(window.location.href).then(() => {
    const btn = document.getElementById('copy-link-btn');
    btn.textContent = 'Copied ✓';
    setTimeout(() => { btn.textContent = '🔗 Copy Link'; }, 2000);
  }).catch(() => {
    // Clipboard API unavailable — URL is still in the address bar
  });
});
```

- [ ] **Step 2: Verify copy behaviour**

1. Select two protocols on the compare page. The 🔗 Copy Link button should be visible.
2. Click the button. Confirm the button text changes to "Copied ✓" for ~2 seconds then reverts to "🔗 Copy Link".
3. Paste into a text editor and confirm the pasted URL matches the address bar.

- [ ] **Step 3: Commit**

```bash
git add docs/javascripts/protocol-compare.js
git commit -m "feat: copy-to-clipboard for comparison tool share link"
```
