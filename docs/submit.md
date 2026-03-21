---
title: Submit Protocol
---

# Submit Protocol

<div id="protocol-submit-page">

<div class="submit-layout">

<nav class="submit-anchor-nav" aria-label="Form sections">
  <a href="#section-metadata">Metadata</a>
  <a href="#section-clinical">Clinical Summary</a>
  <a href="#section-prep">Patient Prep</a>
  <a href="#section-contrast">IV Contrast</a>
  <a href="#section-notes">Special Notes</a>
  <a href="#section-gantt">Gantt Builder</a>
  <a href="#section-series">Series</a>
  <a href="#section-tech">Technical Params</a>
  <a href="#section-postproc">Post-Processing</a>
  <a href="#section-recons">Reconstructions</a>
</nav>

<!-- Left: Form -->
<div class="submit-form-col">

<div class="submit-base-off">
  <label class="submit-label" for="base-off-input">Base off existing protocol (optional)</label>
  <div class="searchable-select-container" id="base-off-container">
    <input type="text" id="base-off-input" class="searchable-input" placeholder="Search protocols..." autocomplete="off">
    <div class="searchable-dropdown" id="base-off-dropdown" style="display:none;"></div>
  </div>
</div>

<form id="protocol-submit-form" novalidate>

<section id="section-metadata" class="submit-section">
<h2>1. Metadata</h2>
<div class="submit-field"><label>Protocol Name *</label><input type="text" id="field-protocol-name" required></div>
<div class="submit-field"><label>Author</label><input type="text" id="field-author"></div>
<div class="submit-field"><label>Last Updated</label><input type="date" id="field-last-updated"></div>
<div class="submit-field">
  <label>Category</label>
  <select id="field-category">
    <option value="Cardiac">Cardiac</option>
    <option value="Vascular">Vascular</option>
    <option value="Chest">Chest</option>
    <option value="Abdomen">Abdomen</option>
    <option value="Neuro">Neuro</option>
    <option value="Msk">Msk</option>
    <option value="Trauma">Trauma</option>
  </select>
</div>
<div class="submit-field"><label>Protocol Type</label><input type="text" id="field-protocol-type"></div>
</section>

<section id="section-clinical" class="submit-section">
<h2>2. Clinical Summary</h2>
<div class="submit-field">
  <label>Acquisition Summary</label>
  <table class="dynamic-table" id="table-acquisition-summary">
    <thead><tr><th>Series</th><th>Phase</th><th>Coverage</th><th></th></tr></thead>
    <tbody></tbody>
  </table>
  <button type="button" class="add-row-btn" data-table="acquisition-summary">+ Add Row</button>
</div>
<div class="submit-field">
  <label>Clinical Indications (one per line)</label>
  <textarea id="field-indications" rows="4" placeholder="e.g. Pulmonary embolism&#10;Aortic dissection"></textarea>
</div>
</section>

<section id="section-prep" class="submit-section">
<h2>3. Patient Prep</h2>
<div class="submit-field"><label>Position</label><input type="text" id="field-position" placeholder="e.g. Supine, arms up"></div>
<div class="submit-field"><label>NPO Status</label><input type="text" id="field-npo" placeholder="e.g. None required"></div>
<div class="submit-field">
  <label><input type="checkbox" id="toggle-premedication"> Premedication required</label>
  <textarea id="field-premedication" rows="2" style="display:none;margin-top:8px;"></textarea>
</div>
</section>

<section id="section-contrast" class="submit-section">
<h2>4. IV Contrast &amp; Injection</h2>
<div class="submit-field"><label>Agent</label><input type="text" id="contrast-agent" placeholder="e.g. Isovue 370"></div>
<div class="submit-field"><label>Volume</label><input type="text" id="contrast-volume" placeholder="e.g. 80 mL"></div>
<div class="submit-field"><label>Flow Rate</label><input type="text" id="contrast-flow-rate" placeholder="e.g. 4 mL/s"></div>
<div class="submit-field"><label>Timing Method</label><input type="text" id="contrast-timing-method" placeholder="e.g. Bolus Tracking"></div>
<div class="submit-field"><label>ROI Placement</label><input type="text" id="contrast-roi" placeholder="e.g. Aorta at T4"></div>
<div class="submit-field"><label>Trigger (HU)</label><input type="text" id="contrast-trigger" placeholder="e.g. 150 HU"></div>
<div class="submit-field"><label>Lab Requirements</label><textarea id="contrast-lab" rows="2"></textarea></div>
</section>

<section id="section-notes" class="submit-section">
<h2>5. Special Notes</h2>
<div class="submit-field"><label>Technologist Notes</label><textarea id="notes-tech" rows="3"></textarea></div>
<div class="submit-field"><label>Nursing Notes</label><textarea id="notes-nursing" rows="3"></textarea></div>
<div class="submit-field"><label>Radiologist Notes</label><textarea id="notes-radiologist" rows="3"></textarea></div>
<div class="submit-field"><label>Tips &amp; Tricks</label><textarea id="notes-tips" rows="3"></textarea></div>
<div class="submit-field"><label>Safety — Renal Function</label><input type="text" id="safety-renal" placeholder="e.g. GFR > 30"></div>
<div class="submit-field"><label>Safety — Allergy Check</label><input type="text" id="safety-allergy" placeholder="e.g. Screen for iodine allergy"></div>
</section>

<section id="section-gantt" class="submit-section">
<h2>6. Gantt Builder</h2>
<p class="submit-hint">When cloning, the raw mermaid is shown below. Edit it directly, or clear it and use the builder above.</p>
<div class="submit-field">
  <label>Raw Mermaid (for cloned protocols)</label>
  <textarea id="gantt-raw" rows="6" placeholder="Paste or edit raw mermaid gantt content here..."></textarea>
</div>
<div id="gantt-rows-container"></div>
<button type="button" id="add-gantt-row-btn" class="add-row-btn">+ Add Gantt Row</button>
</section>

<section id="section-series" class="submit-section">
<h2>7. Series Acquisition</h2>
<table class="dynamic-table" id="table-series">
  <thead><tr><th>Name</th><th>Start</th><th>End</th><th>Delay</th><th>Thickness</th><th>Notes</th><th></th></tr></thead>
  <tbody></tbody>
</table>
<button type="button" class="add-row-btn" data-table="series">+ Add Row</button>
</section>

<section id="section-tech" class="submit-section">
<h2>8. Technical Parameters</h2>
<div class="submit-field"><label>kV</label><input type="text" id="tech-kv" placeholder="e.g. 120"></div>
<div class="submit-field"><label>mAs</label><input type="text" id="tech-mas" placeholder="e.g. Auto mA"></div>
<div class="submit-field"><label>Rotation Time (s)</label><input type="text" id="tech-rotation" placeholder="e.g. 0.5"></div>
<div class="submit-field"><label>Pitch</label><input type="text" id="tech-pitch" placeholder="e.g. 1.375"></div>
</section>

<section id="section-postproc" class="submit-section">
<h2>9. Post-Processing</h2>
<table class="dynamic-table" id="table-postproc">
  <thead><tr><th>Plane</th><th>Acquisition</th><th>FOV</th><th>Thickness/Increment</th><th>Kernel</th><th>IR Strength</th><th>Notes</th><th></th></tr></thead>
  <tbody></tbody>
</table>
<button type="button" class="add-row-btn" data-table="postproc">+ Add Row</button>
</section>

<section id="section-recons" class="submit-section">
<h2>10. Additional Reconstructions</h2>
<div class="submit-field"><textarea id="field-recons" rows="3" placeholder="e.g. Coronal and sagittal MPRs"></textarea></div>
</section>

<div class="submit-actions">
  <button type="button" id="generate-preview-btn" class="md-button md-button--primary">Generate &amp; Preview</button>
</div>

</form>
</div><!-- end submit-form-col -->

<!-- Right: Preview Panel -->
<div class="submit-preview-col" id="preview-panel">
<div class="preview-header">
  <span class="preview-title">Preview</span>
  <button type="button" id="copy-markdown-btn" class="md-button" style="display:none;">Copy Markdown</button>
  <button type="button" id="download-btn" class="md-button" style="display:none;">Download .md</button>
</div>
<div id="preview-content" class="preview-content">
  <p class="preview-placeholder">Fill in the form and click <strong>Generate &amp; Preview</strong> to see the rendered protocol here.</p>
</div>
</div><!-- end submit-preview-col -->

</div><!-- end submit-layout -->
</div><!-- end protocol-submit-page -->
