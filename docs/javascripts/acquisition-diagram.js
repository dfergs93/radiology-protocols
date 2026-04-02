/**
 * acquisition-diagram.js
 * Custom SVG acquisition diagram renderer for CT protocol pages.
 * Exposed as globals on window for use in MkDocs Material pages.
 */

(function () {
  'use strict';

  // ─── 1. parseDelaySeconds ────────────────────────────────────────────────────

  /**
   * Parse the delay string from the series table into a number of seconds.
   *
   * @param {string|null} delayStr
   * @param {number} injectionDurationSeconds  - used for bolus-track fallback
   * @returns {number}
   */
  function parseDelaySeconds(delayStr, injectionDurationSeconds) {
    if (delayStr == null || delayStr === '' || /^n\/a$/i.test(delayStr.trim())) {
      return 0;
    }

    const s = delayStr.trim();

    // Bolus track
    if (/bolus[\s-]*track(ed)?/i.test(s)) {
      const dur = injectionDurationSeconds && injectionDurationSeconds > 0
        ? injectionDurationSeconds
        : 30;
      return dur;
    }

    // Immediate
    if (/immediate/i.test(s)) {
      return 0;
    }

    // First integer
    const match = s.match(/(\d+)/);
    if (match) {
      return parseInt(match[1], 10);
    }

    return 0;
  }

  // ─── 2. inferPhaseType ───────────────────────────────────────────────────────

  /**
   * Infer the phase type from the series name.
   *
   * @param {string} seriesName
   * @returns {'non-contrast'|'arterial'|'portal'|'delayed'|'other'}
   */
  function inferPhaseType(seriesName) {
    const s = seriesName || '';

    if (
      /non[\s-]contrast/i.test(s) ||
      /without/i.test(s) ||
      /unenhanced/i.test(s) ||
      /\bnc\b/i.test(s) ||
      /\bpre\b/i.test(s)
    ) {
      return 'non-contrast';
    }

    if (/arterial/i.test(s)) {
      return 'arterial';
    }

    if (/portal|venous|\bpv\b/i.test(s)) {
      return 'portal';
    }

    if (/delayed|delay|nephrographic|excretory|equilibrium/i.test(s)) {
      return 'delayed';
    }

    return 'other';
  }

  // ─── 3. parseProtocolFromDOM ─────────────────────────────────────────────────

  /**
   * Parse injection and series data from the rendered MkDocs page DOM.
   *
   * @param {Document|Element} pageRoot
   * @returns {{ contrast: object|null, saline: object|null, phases: object[] }}
   */
  function parseProtocolFromDOM(pageRoot) {
    const root = pageRoot || document;

    function findTabContent(labelText) {
      const labels = Array.from(root.querySelectorAll('label'));
      const label = labels.find(l => l.textContent.trim() === labelText);
      if (!label) return null;

      const forAttr = label.getAttribute('for');
      if (!forAttr) return null;

      const input = root.querySelector(`input#${CSS.escape(forAttr)}`);
      if (!input) return null;

      const tabSet = input.closest('.tabbed-set');
      if (!tabSet) return null;

      // More reliable: get all inputs that are direct-ish children in order
      const tabSetInputs = Array.from(tabSet.children).filter(el => el.tagName === 'INPUT');
      const idx = tabSetInputs.indexOf(input);
      if (idx === -1) return null;

      const tabContent = tabSet.querySelector('.tabbed-content');
      if (!tabContent) return null;

      const blocks = Array.from(tabContent.children).filter(el => el.classList.contains('tabbed-block'));
      return blocks[idx] || null;
    }

    function parseTable(block) {
      if (!block) return [];
      const rows = Array.from(block.querySelectorAll('tr'));
      if (rows.length === 0) return [];

      // Find header row
      const headerRow = rows.find(r => r.querySelector('th'));
      const headers = headerRow
        ? Array.from(headerRow.querySelectorAll('th')).map(th => th.textContent.trim().toLowerCase())
        : [];

      const dataRows = rows.filter(r => !r.querySelector('th') && r.querySelector('td'));
      return dataRows.map(row => {
        const cells = Array.from(row.querySelectorAll('td')).map(td => td.textContent.trim());
        if (headers.length > 0) {
          const obj = {};
          headers.forEach((h, i) => { obj[h] = cells[i] || ''; });
          return obj;
        }
        // Fallback: treat as key-value pairs
        return { key: cells[0] || '', value: cells[1] || '' };
      });
    }

    // ── Parse Injection Parameters ──────────────────────────────────────────
    const injBlock = findTabContent('Injection Parameters');
    let contrast = null;
    let saline = null;

    if (injBlock) {
      const rows = parseTable(injBlock);

      function getVal(paramName) {
        // Try header-based lookup first
        for (const row of rows) {
          if (row.parameter != null) {
            if (row.parameter.toLowerCase() === paramName.toLowerCase()) return row.value || '';
          } else if (row.key != null) {
            if (row.key.toLowerCase() === paramName.toLowerCase()) return row.value || '';
          }
        }
        return '';
      }

      const agent = getVal('Agent');
      const volume = getVal('Volume');
      const flowRate = getVal('Flow Rate');
      const durationRaw = getVal('Duration');
      const timingMethod = getVal('timing method') || getVal('timing');

      // Parse duration seconds from e.g. "40s", "40 sec", "40 seconds"
      let durationSeconds = 0;
      const durMatch = durationRaw.match(/(\d+(?:\.\d+)?)/);
      if (durMatch) durationSeconds = parseFloat(durMatch[1]);

      if (agent && !/^n\/a$/i.test(agent.trim())) {
        // Default to 30s if Duration row is missing from the protocol
        contrast = { volume, flowRate, durationSeconds: durationSeconds || 30, timingMethod };
      }

      // Saline
      for (const row of rows) {
        const paramKey = (row.parameter || row.key || '').toLowerCase();
        if (paramKey.includes('saline')) {
          const salineRaw = row.value || '';
          const salineMatch = salineRaw.match(/(\d+(?:\.\d+)?)/);
          const salineDuration = salineMatch ? parseFloat(salineMatch[1]) : 0;
          saline = { durationSeconds: salineDuration };
          break;
        }
      }
    }

    // ── Parse Series Acquisition ────────────────────────────────────────────
    const seriesBlock = findTabContent('Series Acquisition');
    const phases = [];

    if (seriesBlock) {
      const rows = parseTable(seriesBlock);
      const injDur = contrast ? contrast.durationSeconds : 0;
      let lastPhaseEndTime = 0;

      for (const row of rows) {
        // Normalize column access (headers may vary in casing)
        function col(names) {
          for (const n of names) {
            for (const [k, v] of Object.entries(row)) {
              if (k.toLowerCase().includes(n.toLowerCase())) return v || '';
            }
          }
          return '';
        }

        const seriesName = col(['series name', 'series', 'name']);
        if (!seriesName) continue;
        if (/^scout/i.test(seriesName.trim())) continue;

        const start = col(['start location', 'start']);
        const end = col(['end location', 'end']);
        const delay = col(['delay']);

        const type = inferPhaseType(seriesName);
        let delaySeconds;

        if (type === 'non-contrast' && contrast !== null) {
          // NC phase in a contrast study: offset before injection
          delaySeconds = -20;
        } else if (/immediate/i.test(delay.trim())) {
          // "Immediate" means start right after the previous scan ends
          delaySeconds = lastPhaseEndTime;
        } else {
          delaySeconds = parseDelaySeconds(delay, injDur);
        }

        const phaseDuration = 5;
        lastPhaseEndTime = Math.max(lastPhaseEndTime, delaySeconds + phaseDuration);

        phases.push({
          name: seriesName,
          range: `${start} → ${end}`,
          delaySeconds,
          durationSeconds: phaseDuration,
          type,
        });
      }
    }

    return { contrast, saline, phases };
  }

  // ─── 4. renderAcquisitionDiagram ─────────────────────────────────────────────

  const PHASE_COLORS = {
    'non-contrast': '#9e9e9e',
    'arterial':     '#f44336',
    'portal':       '#2196f3',
    'delayed':      '#1565c0',
    'other':        '#9e9e9e',
  };

  const DARK_PHASES = new Set(['arterial', 'portal', 'delayed']);

  const ROW_HEIGHT   = 28;
  const BAR_HEIGHT   = 18;
  const BAR_Y_OFFSET = 5;
  const LEFT_PAD     = 8;
  const RIGHT_PAD    = 8;
  const TOP_PAD      = 20;
  const BOTTOM_PAD   = 30;
  const LABEL_WIDTH  = 160;
  const SVG_TOTAL_WIDTH = 800;

  const SVG_NS = 'http://www.w3.org/2000/svg';

  function createSVGEl(tag, attrs) {
    const el = document.createElementNS(SVG_NS, tag);
    if (attrs) {
      for (const [k, v] of Object.entries(attrs)) {
        el.setAttribute(k, v);
      }
    }
    return el;
  }

  function truncate(str, maxLen) {
    if (!str) return '';
    if (str.length <= maxLen) return str;
    return str.slice(0, maxLen) + '\u2026'; // …
  }

  /**
   * Render an SVG acquisition diagram into `container`.
   *
   * @param {Element} container
   * @param {{ contrast: object|null, saline: object|null, phases: object[] }} data
   */
  function renderAcquisitionDiagram(container, data) {
    // Clear container
    while (container.firstChild) container.removeChild(container.firstChild);

    const { contrast, saline, phases } = data;
    const ncOnly = contrast === null;

    if (!phases || phases.length === 0) {
      const msg = document.createElement('p');
      msg.textContent = 'No acquisition data available';
      msg.style.color = 'var(--md-default-fg-color--light, #888)';
      msg.style.fontStyle = 'italic';
      container.appendChild(msg);
      return;
    }

    // ── Determine rows ──────────────────────────────────────────────────────
    // Group phases by range for row grouping
    const rangeOrder = [];
    const rangeMap = {}; // range -> [phases]
    for (const ph of phases) {
      if (!rangeMap[ph.range]) {
        rangeOrder.push(ph.range);
        rangeMap[ph.range] = [];
      }
      rangeMap[ph.range].push(ph);
    }

    const hasInjection = !ncOnly;
    const injectionRowCount = hasInjection ? 1 : 0;
    const phaseRowCount = rangeOrder.length;
    const totalRows = injectionRowCount + phaseRowCount;

    // ── Time extents ────────────────────────────────────────────────────────
    let minTime, maxTime;

    if (ncOnly) {
      minTime = 0;
      maxTime = 30; // default minimum
      for (const ph of phases) {
        maxTime = Math.max(maxTime, ph.delaySeconds + ph.durationSeconds);
      }
      maxTime += 20; // buffer
    } else {
      const hasNC = phases.some(p => p.type === 'non-contrast');
      minTime = hasNC ? -20 : 0;

      // Also consider injection starts at 0
      maxTime = contrast.durationSeconds + (saline ? saline.durationSeconds : 0) + 10;
      for (const ph of phases) {
        if (ph.type !== 'non-contrast') {
          maxTime = Math.max(maxTime, ph.delaySeconds + ph.durationSeconds);
        }
      }
      maxTime += 20; // buffer
    }

    const timeRange = maxTime - minTime;
    const svgContentWidth = SVG_TOTAL_WIDTH - LEFT_PAD - LABEL_WIDTH - RIGHT_PAD;
    const pixelsPerSecond = svgContentWidth / timeRange;

    function xAtTime(t) {
      return LEFT_PAD + LABEL_WIDTH + (t - minTime) * pixelsPerSecond;
    }

    // ── SVG dimensions ──────────────────────────────────────────────────────
    const totalHeight = TOP_PAD + totalRows * ROW_HEIGHT + BOTTOM_PAD;

    const svg = createSVGEl('svg', {
      viewBox: `0 0 ${SVG_TOTAL_WIDTH} ${totalHeight}`,
      width: '100%',
      preserveAspectRatio: 'xMinYMin meet',
      'aria-label': 'Protocol acquisition diagram',
      role: 'img',
    });

    // ── Helper: render a bar with optional label ────────────────────────────
    function renderBar(parentEl, x, y, width, height, fill, labelText, labelColor) {
      if (width <= 0) return;

      const rect = createSVGEl('rect', {
        x, y, width, height,
        rx: 4, ry: 4,
        fill,
      });
      parentEl.appendChild(rect);

      if (labelText) {
        const inside = width >= 40;
        const textX = inside ? x + width / 2 : x + width + 4;
        const textAnchor = inside ? 'middle' : 'start';
        const textFill = labelColor || '#fff';

        const text = createSVGEl('text', {
          x: textX,
          y: y + height / 2 + 4, // vertical center
          'text-anchor': textAnchor,
          'font-size': 10,
          fill: textFill,
          'font-family': 'inherit',
        });
        text.textContent = truncate(labelText, 20);

        // Clip text to bar if inside
        if (inside) {
          const clipId = `clip-${Math.random().toString(36).slice(2)}`;
          const clipPath = createSVGEl('clipPath', { id: clipId });
          const clipRect = createSVGEl('rect', { x, y: y - 2, width, height: height + 4 });
          clipPath.appendChild(clipRect);
          parentEl.appendChild(clipPath);
          text.setAttribute('clip-path', `url(#${clipId})`);
        }

        parentEl.appendChild(text);
      }
    }

    // ── Helper: render row label ────────────────────────────────────────────
    function renderRowLabel(parentEl, rowIndex, labelText) {
      const y = TOP_PAD + rowIndex * ROW_HEIGHT + ROW_HEIGHT / 2 + 4;
      const text = createSVGEl('text', {
        x: LEFT_PAD + LABEL_WIDTH - 8,
        y,
        'text-anchor': 'end',
        'font-size': 11,
        fill: 'currentColor',
        'font-family': 'inherit',
      });
      text.textContent = truncate(labelText, 22);
      parentEl.appendChild(text);
    }

    // ── Row 0: Injection ────────────────────────────────────────────────────
    let currentRow = 0;

    if (hasInjection) {
      renderRowLabel(svg, currentRow, 'Injection');

      const rowY = TOP_PAD + currentRow * ROW_HEIGHT + BAR_Y_OFFSET;

      // Contrast bar
      const contrastStart = xAtTime(0);
      const contrastWidth = contrast.durationSeconds * pixelsPerSecond;
      renderBar(svg, contrastStart, rowY, contrastWidth, BAR_HEIGHT, '#4caf50', 'Contrast', '#fff');

      // Saline bar
      if (saline && saline.durationSeconds > 0) {
        const salineStart = xAtTime(contrast.durationSeconds);
        const salineWidth = saline.durationSeconds * pixelsPerSecond;
        renderBar(svg, salineStart, rowY, salineWidth, BAR_HEIGHT, '#4ed5ff', 'Saline', '#333');
      }

      currentRow++;
    }

    // ── Phase rows ──────────────────────────────────────────────────────────
    for (const range of rangeOrder) {
      const phasesInRow = rangeMap[range];
      renderRowLabel(svg, currentRow, range);

      const rowY = TOP_PAD + currentRow * ROW_HEIGHT + BAR_Y_OFFSET;

      for (const ph of phasesInRow) {
        const barX = xAtTime(ph.delaySeconds);
        const barW = ph.durationSeconds * pixelsPerSecond;
        const fill = PHASE_COLORS[ph.type] || PHASE_COLORS.other;
        const textColor = DARK_PHASES.has(ph.type) ? '#fff' : '#333';
        renderBar(svg, barX, rowY, barW, BAR_HEIGHT, fill, ph.name, textColor);
      }

      currentRow++;
    }

    // ── Axis ────────────────────────────────────────────────────────────────
    const axisY = TOP_PAD + totalRows * ROW_HEIGHT;
    const axisXStart = xAtTime(minTime);
    const axisXEnd = xAtTime(maxTime);

    // Horizontal axis line
    const axisLine = createSVGEl('line', {
      x1: axisXStart, y1: axisY,
      x2: axisXEnd,   y2: axisY,
      stroke: 'currentColor',
      'stroke-width': 1,
      opacity: 0.4,
    });
    svg.appendChild(axisLine);

    // Tick interval
    const tickInterval = timeRange > 300 ? 60 : 30;

    // Ticks and labels
    const firstTick = Math.ceil(minTime / tickInterval) * tickInterval;
    for (let t = firstTick; t <= maxTime; t += tickInterval) {
      const tx = xAtTime(t);

      const tick = createSVGEl('line', {
        x1: tx, y1: axisY,
        x2: tx, y2: axisY + 5,
        stroke: 'currentColor',
        'stroke-width': 1,
        opacity: 0.4,
      });
      svg.appendChild(tick);

      const tickLabel = createSVGEl('text', {
        x: tx,
        y: axisY + 14,
        'text-anchor': 'middle',
        'font-size': 9,
        fill: 'currentColor',
        opacity: 0.6,
        'font-family': 'inherit',
      });
      tickLabel.textContent = t;
      svg.appendChild(tickLabel);
    }

    // t=0 vertical milestone line (only if not NC-only, where t=0 has meaning)
    if (!ncOnly) {
      const zeroX = xAtTime(0);
      const zeroLine = createSVGEl('line', {
        x1: zeroX, y1: TOP_PAD,
        x2: zeroX, y2: axisY,
        stroke: '#555',
        'stroke-dasharray': '4,3',
        'stroke-width': 1,
        opacity: 0.7,
      });
      svg.appendChild(zeroLine);
    }

    // Axis label
    const axisLabelText = ncOnly
      ? 'Time (seconds from scan start)'
      : 'Time (seconds from injection start)';

    const axisLabel = createSVGEl('text', {
      x: LEFT_PAD + LABEL_WIDTH + svgContentWidth / 2,
      y: axisY + 26,
      'text-anchor': 'middle',
      'font-size': 9,
      fill: 'currentColor',
      opacity: 0.5,
      'font-family': 'inherit',
    });
    axisLabel.textContent = axisLabelText;
    svg.appendChild(axisLabel);

    container.appendChild(svg);
  }

  // ─── Expose globals ───────────────────────────────────────────────────────────

  window.parseDelaySeconds       = parseDelaySeconds;
  window.inferPhaseType          = inferPhaseType;
  window.parseProtocolFromDOM    = parseProtocolFromDOM;
  window.renderAcquisitionDiagram = renderAcquisitionDiagram;

})();
