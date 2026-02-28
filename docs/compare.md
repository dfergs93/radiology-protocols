# CT Protocolizer Tool

Compare multiple CT protocols side-by-side to understand differences in contrast strategies, timing, and acquisition parameters.

<style>
.protocoller-box {
  background: var(--md-code-bg-color);
  padding: 24px;
  border-radius: 8px;
  margin-bottom: 32px;
  border: 1px solid var(--md-default-fg-color--lightest);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}
.protocoller-input-group {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}
.protocoller-input {
  flex: 1;
  padding: 12px;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 4px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  font-size: 1rem;
}
.protocoller-results {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.protocol-rec-card {
  padding: 16px;
  border: 1px solid var(--md-accent-fg-color);
  background: var(--md-default-bg-color);
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  border-left-width: 4px;
}
.protocol-rec-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.rec-title {
  font-weight: bold;
  font-size: 1.1em;
  color: var(--md-primary-fg-color);
}
.rec-reasoning {
  font-size: 0.9em;
  margin-top: 4px;
  opacity: 0.9;
}
</style>

<div class="protocoller-box">
  <h3 style="margin-top: 0; display: flex; align-items: center; gap: 8px;">
    <span>⚡</span> AI Protocolizer
  </h3>
  <p style="opacity: 0.8; margin-bottom: 0;">
    Describe the clinical indication (e.g., "Hematuria in 35F pregnant patient") to get AI-powered recommendations.
  </p>
  
  <div class="protocoller-input-group">
    <input type="text" id="protocoller-input" class="protocoller-input" placeholder="Enter clinical history/indication">
    <button id="protocoller-btn" class="md-button md-button--primary">Submit</button>
  </div>
  
  <div id="protocoller-loading" style="display: none; margin-top: 16px; color: var(--md-default-fg-color--light);">
    <em>Analyzing clinical indications...</em>
  </div>

  <div id="protocoller-results" class="protocoller-results" style="display: none;"></div>
</div>

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