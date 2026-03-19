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
  });
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
  document.getElementById('comparison-results').style.display = 'none';
});

function displayComparison() {
  document.getElementById('comparison-results').style.display = 'block';

  displayGanttComparison();
  displayContrastComparison();
  displaySeriesComparison();

  // Reinitialize Mermaid for new diagrams
  if (typeof mermaid !== 'undefined') {
    mermaid.init(undefined, '.mermaid');
  }
}

function displayGanttComparison() {
  const container = document.getElementById('gantt-container');
  container.innerHTML = '';

  // Find the maximum duration across all protocols
  const maxDuration = findMaxProtocolDuration();
  console.log('Max protocol duration:', maxDuration);

  const grid = document.createElement('div');
  grid.style.display = 'flex';
  grid.style.flexDirection = 'column';
  grid.style.gap = '30px';

  selectedProtocols.forEach(protocol => {
    const col = document.createElement('div');

    const title = document.createElement('h4');
    const link = document.createElement('a');

    let url = protocol.filepath.replace('.md', '/');
    link.href = `/radiology-protocols/${url}`;  // Leading slash makes it absolute

    link.textContent = protocol.title;
    link.style.textDecoration = 'none';
    link.style.color = 'inherit';
    link.addEventListener('mouseenter', () => {
      link.style.textDecoration = 'underline';
    });
    link.addEventListener('mouseleave', () => {
      link.style.textDecoration = 'none';
    });
    title.appendChild(link);
    col.appendChild(title);

    if (protocol.gantt) {
      const ganttDiv = document.createElement('div');
      ganttDiv.className = 'mermaid';

      // Normalize the gantt diagram
      let ganttContent = protocol.gantt.replace(/```mermaid\n?/, '').replace(/```$/, '');
      ganttContent = normalizeGanttTimeline(ganttContent, maxDuration);

      ganttDiv.textContent = ganttContent;
      col.appendChild(ganttDiv);
    } else {
      const noGantt = document.createElement('p');
      noGantt.textContent = 'No timeline available';
      noGantt.style.fontStyle = 'italic';
      col.appendChild(noGantt);
    }

    grid.appendChild(col);
  });

  container.appendChild(grid);
}

function findMaxProtocolDuration() {
  let maxSeconds = 0;

  selectedProtocols.forEach(protocol => {
    if (!protocol.gantt) return;

    // Extract all time values (mm:ss)
    const timePattern = /(\d{1,2}):(\d{2})/g;
    let match;

    while ((match = timePattern.exec(protocol.gantt)) !== null) {
      const minutes = parseInt(match[1]);
      const seconds = parseInt(match[2]);
      const totalSeconds = minutes * 60 + seconds;
      maxSeconds = Math.max(maxSeconds, totalSeconds);
    }
  });

  // Add small buffer (20 seconds) and convert to minutes, rounding up
  const totalSeconds = maxSeconds + 20;
  return Math.ceil(totalSeconds / 60);
}

function normalizeGanttTimeline(ganttContent, maxDuration) {
  // Add a transparent spacer task at the end to extend timeline
  const lines = ganttContent.split('\n');

  // Find where to insert (before the closing, after last section)
  const lastSectionIndex = lines.findLastIndex(line => line.trim().startsWith('section'));

  if (lastSectionIndex !== -1) {
    // Insert after the last task in the last section
    const formattedTime = `${maxDuration.toString().padStart(2, '0')}:00`;
    const spacerLine = `      Timeline end    :milestone, end, ${formattedTime}, 0s`;

    // Find the end of gantt content (before closing)
    lines.push(spacerLine);
  }

  return lines.join('\n');
}

function displayContrastComparison() {
  const container = document.getElementById('contrast-table-container');

  let html = '<table><thead><tr>';
  html += '<th>Protocol</th>';
  html += '<th>Type</th>';
  html += '<th>Agent</th>';
  html += '<th>Volume</th>';
  html += '<th>Flow Rate</th>';
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
    html += `<td>${contrast.flow_rate || 'N/A'}</td>`;
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
