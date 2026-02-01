let protocolData = [];
let selectedProtocols = [];
let selectorCount = 2;

// Wait for page to load, then fetch protocol data
document.addEventListener('DOMContentLoaded', function() {
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
    // Clear existing options except first
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
  });
}

// Add protocol selector
document.getElementById('add-protocol-btn')?.addEventListener('click', () => {
  selectorCount++;
  const container = document.getElementById('protocol-selectors');
  
  const select = document.createElement('select');
  select.id = `protocol-select-${selectorCount}`;
  select.className = 'protocol-select';
  
  container.appendChild(select);
  populateSelectors();
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
    title.textContent = protocol.title;
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
  
  // Find max rows
  const maxRows = Math.max(...selectedProtocols.map(p => (p.summary || []).length));
  
  for (let i = 0; i < maxRows; i++) {
    html += '<tr>';
    html += `<td><strong>Acquisition ${i + 1}</strong></td>`;
    
    selectedProtocols.forEach(protocol => {
      const item = (protocol.summary || [])[i];
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

function displayDetailedSeriesComparison(container) {
  // Your existing series comparison code
  let html = '<table><thead><tr>';
  html += '<th>Phase</th>';
  selectedProtocols.forEach(protocol => {
    html += `<th>${protocol.title}</th>`;
  });
  html += '</tr></thead><tbody>';
  
  const maxSeries = Math.max(...selectedProtocols.map(p => (p.series || []).length));
  
  for (let i = 0; i < maxSeries; i++) {
    html += '<tr>';
    html += `<td><strong>Series ${i + 1}</strong></td>`;
    
    selectedProtocols.forEach(protocol => {
      const series = (protocol.series || [])[i];
      if (series) {
        html += '<td>';
        html += `<strong>${series.name}</strong><br>`;
        html += `Coverage: ${series.coverage}<br>`;
        html += `Delay: ${series.delay}<br>`;
        html += `Thickness: ${series.thickness}`;
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
