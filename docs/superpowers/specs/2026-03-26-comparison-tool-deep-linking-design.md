# Deep Linking for Protocol Comparison Tool

**Date:** 2026-03-26
**Status:** Approved

## Overview

Add the ability to share a link to the CT Comparison Tool with protocols pre-populated and the comparison auto-running on load. The URL updates automatically as the user changes protocol selections, and a "Copy Link" button in the toolbar makes sharing explicit.

## URL Format

```
/radiology-protocols/compare/?p=ct/abdomen/ct-abdomen-pelvis-with-contrast&p=ct/vascular/cta-chest
```

- One `p=` query parameter per selected protocol
- Value is the protocol's `filepath` from `protocol-comparison-index.json`, with the `.md` extension stripped
- `history.replaceState` updates the address bar silently — no page reload, no navigation event

Filepaths are used (not numeric indices or titles) because they are stable across index rebuilds and human-readable in the URL.

## Behaviour

### On selection change

Any time a `.protocol-select` element fires a `change` event, call `updateURL()`:
1. Collect filepaths for all selects that have a non-empty value
2. Build `URLSearchParams` with one `p=` per filepath (`.md` stripped)
3. Call `history.replaceState(null, '', '?' + params.toString())`
4. If 2 or more protocols are selected, auto-trigger `displayComparison()`
5. Show the Copy Link button if 2+ protocols are selected; hide it otherwise

### On page load

After `protocolData` is fetched and `populateSelectors()` runs, call `loadFromURL()`:
1. Parse `p=` params from `window.location.search` using `URLSearchParams`
2. For each param value, find the matching protocol in `protocolData` where `protocol.filepath.replace('.md', '') === paramValue`
3. If the number of params exceeds the default 2 selector slots, call `addProtocolSlot()` for each additional protocol
4. For each slot, set `select.value` to the protocol's index, then call `createSearchableSelect(select)` to sync the visible input
5. If 2 or more protocols were loaded from the URL, trigger `displayComparison()`

### Copy Link button

- Rendered in `compare.md` alongside the Add Protocol / Compare / Clear buttons
- Hidden by default (`display: none`); shown when 2+ protocols are selected
- On click: calls `navigator.clipboard.writeText(window.location.href)`, then temporarily changes button text to "Copied ✓" for 2 seconds before reverting
- Falls back gracefully if clipboard API is unavailable (button does nothing visible — URL is still in the address bar)

## Files Changed

| File | Change |
|---|---|
| `docs/javascripts/protocol-compare.js` | Add `updateURL()`, `loadFromURL()`, copy button visibility logic, copy-to-clipboard handler; hook `updateURL()` into existing select `change` events |
| `docs/compare.md` | Add `<button id="copy-link-btn">` to the selector toolbar HTML |

No other files are affected. The `protocol-comparison-index.json` and MkDocs configuration are unchanged.

## Edge Cases

- **Protocol not found in index**: If a `p=` param doesn't match any protocol filepath, it is silently skipped. The remaining valid protocols still load.
- **Only 1 valid protocol in URL**: Selectors are populated but `displayComparison()` is not called — user must select a second protocol manually.
- **More than 2 protocols in URL**: `addProtocolSlot()` is called as needed; the existing dynamic slot logic handles this.
- **Clipboard API unavailable**: Copy button is shown but silently fails; the URL is still present in the address bar for manual copying.
