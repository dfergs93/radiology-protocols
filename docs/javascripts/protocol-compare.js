let protocolData = [];
let selectedProtocols = [];
let selectorCount = 2;

// Wait for page to load, then fetch protocol data
document.addEventListener('DOMContentLoaded', function () {
  console.log('Page loaded, fetching protocol data...');

  fetch('/radiology-protocols/javascripts/protocol-comparison-index.json')
    .then(response => {
      console.log('Fetch response status:', response.status);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.text();
    })
    .then(text => {
      console.log('Received data, length:', text.length);
      return JSON.parse(text);
    })
    .then(data => {
      console.log('Successfully parsed', data.length, 'protocols');
      protocolData = data;
      populateSelectors();
      loadFromURL();
    })
    .catch(error => {
      console.error('Error loading protocols:', error);
      alert('Failed to load protocol data. Check console for details.');
    });
});
function populateSelectors() {
  const selects = document.querySelectorAll('.protocol-select');

  selects.forEach(select => {
    // 1. Save current selection
    const currentValue = select.value;

    // 2. Clear and rebuild options (still good to have the select populated as fallback/source)
    select.innerHTML = '<option value="">-- Select Protocol --</option>';

    // Group by category
    const byCategory = {};
    protocolData.forEach((protocol, index) => {
      const category = protocol.category || 'Other';
      if (!byCategory[category]) {
        byCategory[category] = [];
      }
      byCategory[category].push({ ...protocol, index });
    });

    // Add optgroups
    Object.keys(byCategory).sort().forEach(category => {
      const optgroup = document.createElement('optgroup');
      optgroup.label = category;

      byCategory[category].forEach(protocol => {
        const option = document.createElement('option');
        option.value = protocol.index;
        option.textContent = protocol.title;
        optgroup.appendChild(option);
      });

      select.appendChild(optgroup);
    });

    // 3. Restore selection if it still exists in the new data
    if (currentValue !== "") {
      select.value = currentValue;
    }

    // 4. Transform into searchable select
    createSearchableSelect(select);

    // Attach URL sync listener once per select element
    if (!select.dataset.urlListenerAttached) {
      select.addEventListener('change', updateURL);
      select.dataset.urlListenerAttached = 'true';
    }
  });
}

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
    const results = document.getElementById('comparison-results');
    if (results) results.style.display = 'none';
  }
}

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

function createSearchableSelect(select) {
  // If already initialized, we might just need to update the display if value changed externally
  let container = select.closest('.searchable-select-container');
  let input;

  if (!container) {
    container = document.createElement('div');
    container.className = 'searchable-select-container';
    select.parentNode.insertBefore(container, select);
    container.appendChild(select);

    // Hide the original select
    select.style.display = 'none';

    input = document.createElement('input');
    input.type = 'text';
    input.className = 'search-select-input';
    input.placeholder = '-- Type to search protocol --';
    container.appendChild(input);

    const results = document.createElement('div');
    results.className = 'search-select-results';
    container.appendChild(results);

    // Search logic
    input.addEventListener('input', () => {
      const query = input.value.toLowerCase().trim();
      renderResults(query, results, select, input);
    });

    input.addEventListener('focus', () => {
      const query = input.value.toLowerCase().trim();
      renderResults(query, results, select, input);
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!container.contains(e.target)) {
        results.classList.remove('active');
      }
    });
  } else {
    input = container.querySelector('.search-select-input');
  }

  // Sync input text with current select value
  if (select.value !== "" && protocolData[select.value]) {
    input.value = protocolData[select.value].title;
  } else {
    input.value = "";
  }
}

function renderResults(query, resultsDiv, select, input) {
  resultsDiv.innerHTML = '';

  // Track indexed results for navigation
  const filtered = protocolData
    .map((p, originalIndex) => ({ ...p, originalIndex }))
    .filter(p =>
      p.title.toLowerCase().includes(query) ||
      (p.category && p.category.toLowerCase().includes(query))
    );

  if (filtered.length === 0) {
    const noMatch = document.createElement('div');
    noMatch.className = 'search-select-item';
    noMatch.textContent = 'No matching protocols';
    noMatch.style.fontStyle = 'italic';
    noMatch.style.pointerEvents = 'none';
    resultsDiv.appendChild(noMatch);
  } else {
    filtered.forEach((p, i) => {
      const item = document.createElement('div');
      item.className = 'search-select-item';
      item.dataset.index = p.originalIndex;

      const title = document.createElement('span');
      title.textContent = p.title;
      item.appendChild(title);

      if (p.category) {
        const cat = document.createElement('span');
        cat.className = 'category';
        cat.textContent = p.category;
        item.appendChild(cat);
      }

      item.addEventListener('click', () => {
        select.value = p.originalIndex;
        input.value = p.title;
        resultsDiv.classList.remove('active');
        select.dispatchEvent(new Event('change'));
      });

      resultsDiv.appendChild(item);
    });
  }

  resultsDiv.classList.add('active');

  // Keyboard navigation
  let currentFocus = -1;
  const items = resultsDiv.getElementsByClassName('search-select-item');

  const onKeyDown = (e) => {
    if (e.key === 'ArrowDown') {
      currentFocus++;
      addActive(items);
    } else if (e.key === 'ArrowUp') {
      currentFocus--;
      addActive(items);
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (currentFocus > -1 && items[currentFocus]) {
        items[currentFocus].click();
      }
    }
  };

  input.removeEventListener('keydown', input._keydownHandler);
  input._keydownHandler = onKeyDown;
  input.addEventListener('keydown', onKeyDown);

  function addActive(x) {
    if (!x) return false;
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = x.length - 1;
    x[currentFocus].classList.add('highlighted');
    x[currentFocus].scrollIntoView({ block: 'nearest' });
  }

  function removeActive(x) {
    for (let i = 0; i < x.length; i++) {
      x[i].classList.remove('highlighted');
    }
  }
}

// Function to add a new slot - exported for use by protocoller.js
function addProtocolSlot() {
  selectorCount++;
  const container = document.getElementById('protocol-selectors');

  const select = document.createElement('select');
  select.id = `protocol-select-${selectorCount}`;
  select.className = 'protocol-select';

  container.appendChild(select);
  populateSelectors();
  return select;
}

// Add protocol selector
document.getElementById('add-protocol-btn')?.addEventListener('click', () => {
  addProtocolSlot();
});

// Compare button
document.getElementById('compare-btn')?.addEventListener('click', () => {
  selectedProtocols = [];

  document.querySelectorAll('.protocol-select').forEach(select => {
    const index = select.value;
    if (index !== '') {
      selectedProtocols.push(protocolData[index]);
    }
  });

  if (selectedProtocols.length < 2) {
    alert('Please select at least 2 protocols to compare');
    return;
  }

  displayComparison();
});

// Clear button
document.getElementById('clear-btn')?.addEventListener('click', () => {
  document.querySelectorAll('.protocol-select').forEach(select => {
    select.value = '';
    // Also sync the searchable UI
    createSearchableSelect(select);
  });
  const results = document.getElementById('comparison-results');
  if (results) results.style.display = 'none';
  updateURL();
});

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

function displayComparison() {
  const results = document.getElementById('comparison-results');
  if (results) results.style.display = 'block';

  displayGanttComparison();
  displayContrastComparison();
  displaySeriesComparison();
}

function displayGanttComparison() {
  const container = document.getElementById('gantt-container');
  container.innerHTML = '';

  const grid = document.createElement('div');
  grid.style.display = 'flex';
  grid.style.flexDirection = 'column';
  grid.style.gap = '30px';

  selectedProtocols.forEach(function(protocol) {
    const col = document.createElement('div');

    // Title with link
    const title = document.createElement('h4');
    const link = document.createElement('a');
    const url = protocol.filepath.replace('.md', '/');
    link.href = '/radiology-protocols/' + url;
    link.textContent = protocol.title;
    link.style.textDecoration = 'none';
    link.style.color = 'inherit';
    link.addEventListener('mouseenter', function() { link.style.textDecoration = 'underline'; });
    link.addEventListener('mouseleave', function() { link.style.textDecoration = 'none'; });
    title.appendChild(link);
    col.appendChild(title);

    // Build data object for renderer
    const isNC = !protocol.contrast || protocol.contrast.type === 'Non-contrast' || protocol.contrast.agent === 'N/A';
    const contrastDurationSeconds = isNC ? 0 : (parseInt(protocol.contrast.duration) || 30);

    const data = {
      contrast: isNC ? null : {
        volume: protocol.contrast.volume || '',
        flowRate: protocol.contrast.flow_rate || '',
        durationSeconds: contrastDurationSeconds
      },
      saline: null,
      phases: (protocol.series || []).map(function(s) {
        return {
          name: s.name || '',
          range: s.coverage || ((s.start || '') + ' \u2192 ' + (s.end || '')),
          delaySeconds: typeof s.delay_seconds === 'number' ? s.delay_seconds : 0,
          durationSeconds: 30,
          type: s.phase_type || 'other'
        };
      })
    };

    // Render diagram
    const diagramContainer = document.createElement('div');
    col.appendChild(diagramContainer);

    if (typeof window.renderAcquisitionDiagram === 'function') {
      window.renderAcquisitionDiagram(diagramContainer, data);
    } else {
      diagramContainer.textContent = 'Diagram renderer not available';
      diagramContainer.style.fontStyle = 'italic';
    }

    grid.appendChild(col);
  });

  container.appendChild(grid);
}

function displayContrastComparison() {
  const container = document.getElementById('contrast-table-container');

  let html = '<table><thead><tr>';
  html += '<th>Protocol</th>';
  html += '<th>Type</th>';
  html += '<th>Agent</th>';
  html += '<th>Volume</th>';
  html += '<th>Duration</th>';
  html += '<th>Timing Method</th>';
  html += '<th>Trigger</th>';
  html += '</tr></thead><tbody>';

  selectedProtocols.forEach(protocol => {
    const contrast = protocol.contrast || {};
    html += '<tr>';
    html += `<td><strong>${protocol.title}</strong></td>`;
    html += `<td>${contrast.type || 'N/A'}</td>`;
    html += `<td>${contrast.agent || 'N/A'}</td>`;
    html += `<td>${contrast.volume || 'N/A'}</td>`;
    html += `<td>${contrast.duration || 'N/A'}</td>`;
    html += `<td>${contrast.timing || 'N/A'}</td>`;
    html += `<td>${contrast.trigger || 'N/A'}</td>`;
    html += '</tr>';
  });

  html += '</tbody></table>';
  container.innerHTML = html;
}

function displaySeriesComparison() {
  const container = document.getElementById('series-table-container');

  // Check if we should use series or summary
  const useSummary = selectedProtocols.every(p =>
    (!p.series || p.series.length === 0) && p.summary && p.summary.length > 0
  );

  if (useSummary) {
    displaySummaryComparison(container);
  } else {
    displayDetailedSeriesComparison(container);
  }
}

function displaySummaryComparison(container) {
  let html = '<table><thead><tr>';
  html += '<th>Series</th>';
  selectedProtocols.forEach(protocol => {
    html += `<th>${protocol.title}</th>`;
  });
  html += '</tr></thead><tbody>';

  const filteredSummary = selectedProtocols.map(p =>
    (p.summary || []).filter(s => !isScoutSeries(s.series))
  );

  const maxRows = Math.max(...filteredSummary.map(s => s.length));

  for (let i = 0; i < maxRows; i++) {
    html += '<tr>';
    html += `<td><strong>Acquisition ${i + 1}</strong></td>`;

    filteredSummary.forEach(summary => {
      const item = summary[i];
      if (item) {
        html += '<td>';
        html += `<strong>${item.series}</strong><br>`;
        html += `Phase: ${item.phase}<br>`;
        html += `Coverage: ${item.coverage}`;
        html += '</td>';
      } else {
        html += '<td style="color: #999;">—</td>';
      }
    });

    html += '</tr>';
  }

  html += '</tbody></table>';
  container.innerHTML = html;
}

function isScoutSeries(name) {
  if (!name) return false;
  const lower = name.toLowerCase();
  return lower.includes('scout') || lower.includes('topogram') || lower.includes('localizer');
}

function displayDetailedSeriesComparison(container) {
  let html = '<table><thead><tr>';
  html += '<th>Phase</th>';
  selectedProtocols.forEach(protocol => {
    html += `<th>${protocol.title}</th>`;
  });
  html += '</tr></thead><tbody>';

  const filteredSeries = selectedProtocols.map(p =>
    (p.series || []).filter(s => !isScoutSeries(s.name))
  );

  const maxSeries = Math.max(...filteredSeries.map(s => s.length));

  for (let i = 0; i < maxSeries; i++) {
    html += '<tr>';
    html += `<td><strong>Series ${i + 1}</strong></td>`;

    filteredSeries.forEach(series => {
      const item = series[i];
      if (item) {
        html += '<td>';
        html += `<strong>${item.name}</strong><br>`;
        html += `Coverage: ${item.coverage}<br>`;
        html += `Delay: ${item.delay}<br>`;
        html += `Thickness: ${item.thickness}`;
        html += '</td>';
      } else {
        html += '<td style="color: #999;">—</td>';
      }
    });

    html += '</tr>';
  }

  html += '</tbody></table>';
  container.innerHTML = html;
}
