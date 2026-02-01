# Protocol Comparison Tool

Compare multiple CT protocols side-by-side to understand differences in contrast strategies, timing, and acquisition parameters.

<div id="protocol-compare-container">
  <div class="protocol-selector">
    <h3>Select Protocols to Compare</h3>
    <div id="protocol-selectors">
      <select id="protocol-select-1" class="protocol-select">
        <option value="">-- Select Protocol 1 --</option>
      </select>
      <select id="protocol-select-2" class="protocol-select">
        <option value="">-- Select Protocol 2 --</option>
      </select>
    </div>
    <button id="add-protocol-btn" class="md-button">+ Add Protocol</button>
    <button id="compare-btn" class="md-button md-button--primary">Compare</button>
    <button id="clear-btn" class="md-button">Clear</button>
  </div>

  <div id="comparison-results" style="display: none;">
    <!-- Gantt Diagrams -->
    <div id="gantt-comparison" class="gantt-grid">
      <h3>Timeline Comparison</h3>
      <div id="gantt-container" class="gantt-container"></div>
    </div>

    <!-- Contrast Comparison -->
    <div id="contrast-comparison">
      <h3>Contrast Strategy Comparison</h3>
      <div id="contrast-table-container"></div>
    </div>

    <!-- Series Comparison -->
    <div id="series-comparison">
      <h3>Acquisition Series Comparison</h3>
      <div id="series-table-container"></div>
    </div>
  </div>
</div>