document.addEventListener('DOMContentLoaded', () => {
    // Only run on the submit page
    if (!document.getElementById('protocol-submit-form')) return;

    const API_BASE_URL = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
        ? 'http://localhost:8001'
        : 'https://radiology-protocols.onrender.com';

    // ── Helpers ──────────────────────────────────────────────────────────────

    function slugify(text) {
        return text.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '');
    }

    function secondsToMmss(seconds) {
        const m = Math.floor(seconds / 60);
        const s = seconds % 60;
        return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    function getVal(id) {
        const el = document.getElementById(id);
        return el ? el.value.trim() : '';
    }

    // ── Set default date ──────────────────────────────────────────────────────
    const dateField = document.getElementById('field-last-updated');
    if (dateField) dateField.value = new Date().toISOString().split('T')[0];

    // ── Base-off searchable dropdown ──────────────────────────────────────────
    let protocolList = [];

    async function loadProtocolList() {
        try {
            const res = await fetch(`${API_BASE_URL}/api/protocols`);
            if (!res.ok) return;
            protocolList = await res.json();
            buildBaseOffDropdown(protocolList);
        } catch (e) {
            console.warn('Could not load protocol list:', e);
        }
    }

    function buildBaseOffDropdown(list) {
        const input = document.getElementById('base-off-input');
        const dropdown = document.getElementById('base-off-dropdown');
        if (!input || !dropdown) return;

        function renderDropdown(filter) {
            const filtered = filter
                ? list.filter(p => p.title.toLowerCase().includes(filter.toLowerCase()))
                : list;
            dropdown.innerHTML = filtered.slice(0, 20).map(p =>
                `<div class="searchable-option" data-filepath="${p.filepath}">${p.title}</div>`
            ).join('');
            dropdown.style.display = filtered.length ? 'block' : 'none';
        }

        input.addEventListener('input', () => renderDropdown(input.value));
        input.addEventListener('focus', () => renderDropdown(input.value));
        input.addEventListener('blur', () => setTimeout(() => { dropdown.style.display = 'none'; }, 150));

        dropdown.addEventListener('click', async (e) => {
            const opt = e.target.closest('.searchable-option');
            if (!opt) return;
            input.value = opt.textContent;
            dropdown.style.display = 'none';
            await loadProtocol(opt.dataset.filepath);
        });
    }

    async function loadProtocol(filepath) {
        try {
            const res = await fetch(`${API_BASE_URL}/api/protocols/${filepath}`);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const data = await res.json();
            populateForm(data);
        } catch (e) {
            console.error('Failed to load protocol:', e);
            alert('Could not load protocol. Is the backend running?');
        }
    }

    loadProtocolList();

    // Populate all form fields from a parsed protocol object
    function populateForm(data) {
        const set = (id, val) => { const el = document.getElementById(id); if (el) el.value = val || ''; };
        set('field-protocol-name', data.protocol_name);
        set('field-author', data.author);
        set('field-last-updated', data.last_updated);
        set('field-category', data.category);
        set('field-protocol-type', data.protocol_type);
        set('field-indications', data.clinical_indications);
        set('field-position', data.patient_positioning);
        set('field-npo', data.npo_status);
        set('field-premedication', data.premedication);
        if (data.premedication) {
            document.getElementById('toggle-premedication').checked = true;
            document.getElementById('field-premedication').style.display = 'block';
        }
        set('contrast-agent', data.contrast_agent);
        set('contrast-volume', data.contrast_volume);
        set('contrast-flow-rate', data.contrast_flow_rate);
        set('contrast-timing-method', data.contrast_timing_method);
        set('contrast-roi', data.contrast_roi_placement);
        set('contrast-trigger', data.contrast_trigger);
        set('contrast-lab', data.lab_requirements);
        set('notes-tech', data.tech_notes);
        set('notes-nursing', data.nursing_notes);
        set('notes-radiologist', data.radiologist_notes);
        set('notes-tips', data.tips_tricks);
        set('safety-renal', data.safety_renal_function);
        set('safety-allergy', data.safety_allergy);
        set('gantt-raw', data.gantt_raw);
        set('tech-kv', data.kv);
        set('tech-mas', data.mas);
        set('tech-rotation', data.rotation_time);
        set('tech-pitch', data.pitch);
        set('field-recons', data.additional_recons);

        // Repopulate dynamic tables
        populateDynamicTable('acquisition-summary',
            (data.acquisition_summary || []).map(r => [r.series, r.phase, r.coverage]));
        populateDynamicTable('series',
            (data.series || []).map(r => [r.name, r.start, r.end, r.delay, r.thickness, r.notes]));
        populateDynamicTable('postproc',
            (data.post_processing || []).map(r => [r.plane, r.acquisition, r.fov, r.thickness_increment, r.kernel, r.ir_strength, r.notes]));
    }

    // ── Premedication toggle ──────────────────────────────────────────────────
    document.getElementById('toggle-premedication').addEventListener('change', function () {
        document.getElementById('field-premedication').style.display = this.checked ? 'block' : 'none';
    });

    // ── Dynamic table rows ────────────────────────────────────────────────────
    const TABLE_COLS = {
        'acquisition-summary': ['Series', 'Phase', 'Coverage'],
        'series': ['Name', 'Start', 'End', 'Delay', 'Thickness', 'Notes'],
        'postproc': ['Plane', 'Acquisition', 'FOV', 'Thickness/Increment', 'Kernel', 'IR Strength', 'Notes'],
    };

    function addTableRow(tableId, values = []) {
        const tbody = document.querySelector(`#table-${tableId} tbody`);
        if (!tbody) return;
        const cols = TABLE_COLS[tableId] || [];
        const tr = document.createElement('tr');
        tr.innerHTML = cols.map((_, i) =>
            `<td><input type="text" value="${(values[i] || '').replace(/"/g, '&quot;')}"></td>`
        ).join('') + '<td><button type="button" class="remove-row-btn" title="Remove">✕</button></td>';
        tr.querySelector('.remove-row-btn').addEventListener('click', () => tr.remove());
        tbody.appendChild(tr);
    }

    function populateDynamicTable(tableId, rows) {
        const tbody = document.querySelector(`#table-${tableId} tbody`);
        if (tbody) tbody.innerHTML = '';
        rows.forEach(r => addTableRow(tableId, r));
    }

    document.querySelectorAll('.add-row-btn[data-table]').forEach(btn => {
        btn.addEventListener('click', () => addTableRow(btn.dataset.table));
    });

    function getTableRows(tableId) {
        const rows = [];
        document.querySelectorAll(`#table-${tableId} tbody tr`).forEach(tr => {
            const cells = [...tr.querySelectorAll('input')].map(i => i.value.trim());
            rows.push(cells);
        });
        return rows;
    }

    // ── Gantt builder ─────────────────────────────────────────────────────────

    function addGanttRow(data = {}) {
        const container = document.getElementById('gantt-rows-container');
        const row = document.createElement('div');
        row.className = 'gantt-builder-row';

        row.innerHTML = `
            <input type="text" class="gantt-label" placeholder="Label" value="${data.label || ''}">
            <input type="number" class="gantt-duration" placeholder="Duration (s)" min="1" value="${data.duration_seconds || ''}">
            <select class="gantt-type">
                <option value="contrast" ${data.type === 'contrast' ? 'selected' : ''}>Contrast</option>
                <option value="saline" ${data.type === 'saline' ? 'selected' : ''}>Saline</option>
                <option value="scan" ${data.type === 'scan' ? 'selected' : ''}>Scan</option>
                <option value="other" ${data.type === 'other' ? 'selected' : ''}>Other</option>
            </select>
            <select class="gantt-start">
                <option value="00:00">At 00:00</option>
            </select>
            <button type="button" class="remove-row-btn" title="Remove">✕</button>
        `;
        row.querySelector('.remove-row-btn').addEventListener('click', () => {
            row.remove();
            refreshGanttStartOptions();
        });
        container.appendChild(row);
        refreshGanttStartOptions();
    }

    function refreshGanttStartOptions() {
        const rows = [...document.querySelectorAll('.gantt-builder-row')];
        rows.forEach((row, i) => {
            const startSelect = row.querySelector('.gantt-start');
            const currentVal = startSelect.value;
            const labels = rows.slice(0, i).map(r => r.querySelector('.gantt-label').value.trim()).filter(Boolean);
            startSelect.innerHTML = '<option value="00:00">At 00:00</option>' +
                labels.map(l => `<option value="after ${slugify(l)}" ${currentVal === `after ${slugify(l)}` ? 'selected' : ''}>After: ${l}</option>`).join('');
            if (currentVal) startSelect.value = currentVal;
        });
    }

    function getGanttRows() {
        return [...document.querySelectorAll('.gantt-builder-row')].map(row => ({
            label: row.querySelector('.gantt-label').value.trim(),
            duration_seconds: parseInt(row.querySelector('.gantt-duration').value) || 0,
            type: row.querySelector('.gantt-type').value,
            start: row.querySelector('.gantt-start').value,
        })).filter(r => r.label && r.duration_seconds > 0);
    }

    document.getElementById('add-gantt-row-btn').addEventListener('click', () => addGanttRow());

    document.getElementById('gantt-rows-container').addEventListener('input', (e) => {
        if (e.target.classList.contains('gantt-label')) refreshGanttStartOptions();
    });

    // ── Collect all form data into API payload ────────────────────────────────
    function collectFormData() {
        const acqRows = getTableRows('acquisition-summary');
        const seriesRows = getTableRows('series');
        const postprocRows = getTableRows('postproc');

        return {
            protocol_name: getVal('field-protocol-name'),
            author: getVal('field-author'),
            last_updated: getVal('field-last-updated'),
            category: getVal('field-category'),
            protocol_type: getVal('field-protocol-type'),
            clinical_indications: document.getElementById('field-indications').value.trim(),
            acquisition_summary: acqRows.map(r => ({ series: r[0], phase: r[1], coverage: r[2] })),
            patient_positioning: getVal('field-position'),
            npo_status: getVal('field-npo'),
            premedication: document.getElementById('toggle-premedication').checked ? getVal('field-premedication') : '',
            contrast_agent: getVal('contrast-agent'),
            contrast_volume: getVal('contrast-volume'),
            contrast_flow_rate: getVal('contrast-flow-rate'),
            contrast_timing_method: getVal('contrast-timing-method'),
            contrast_roi_placement: getVal('contrast-roi'),
            contrast_trigger: getVal('contrast-trigger'),
            lab_requirements: document.getElementById('contrast-lab').value.trim(),
            tech_notes: document.getElementById('notes-tech').value.trim(),
            nursing_notes: document.getElementById('notes-nursing').value.trim(),
            radiologist_notes: document.getElementById('notes-radiologist').value.trim(),
            tips_tricks: document.getElementById('notes-tips').value.trim(),
            safety_renal_function: getVal('safety-renal'),
            safety_allergy: getVal('safety-allergy'),
            gantt_rows: getGanttRows(),
            gantt_raw: document.getElementById('gantt-raw').value.trim(),
            series: seriesRows.map(r => ({ name: r[0], start: r[1], end: r[2], delay: r[3], thickness: r[4], notes: r[5] || '' })),
            kv: getVal('tech-kv'),
            mas: getVal('tech-mas'),
            rotation_time: getVal('tech-rotation'),
            pitch: getVal('tech-pitch'),
            post_processing: postprocRows.map(r => ({ plane: r[0], acquisition: r[1], fov: r[2], thickness_increment: r[3], kernel: r[4], ir_strength: r[5], notes: r[6] || '' })),
            additional_recons: document.getElementById('field-recons').value.trim(),
        };
    }

    // ── Generate & Preview ────────────────────────────────────────────────────
    let lastMarkdown = '';

    function validateForm(payload) {
        const failures = [];

        const nameEl = document.getElementById('field-protocol-name');
        if (!payload.protocol_name) {
            failures.push('Protocol Name');
            if (nameEl) nameEl.style.border = '2px solid #e53935';
        } else {
            if (nameEl) nameEl.style.border = '';
        }

        const categoryEl = document.getElementById('field-category');
        if (!payload.category) {
            failures.push('Category');
            if (categoryEl) categoryEl.style.border = '2px solid #e53935';
        } else {
            if (categoryEl) categoryEl.style.border = '';
        }

        const indicationsEl = document.getElementById('field-indications');
        const hasIndications = payload.clinical_indications
            .split('\n').some(line => line.trim().length > 0);
        if (!hasIndications) {
            failures.push('Clinical Indications');
            if (indicationsEl) indicationsEl.style.border = '2px solid #e53935';
        } else {
            if (indicationsEl) indicationsEl.style.border = '';
        }

        return failures;
    }

    async function generatePreview() {
        const payload = collectFormData();
        const failures = validateForm(payload);
        if (failures.length > 0) {
            alert(`The following required fields are missing or incomplete:\n• ${failures.join('\n• ')}`);
            return;
        }

        const btn = document.getElementById('generate-preview-btn');
        btn.disabled = true;
        btn.textContent = 'Generating…';

        try {
            const res = await fetch(`${API_BASE_URL}/api/protocols/generate`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload),
            });
            if (!res.ok) {
                const err = await res.json().catch(() => ({}));
                throw new Error(err.detail ? JSON.stringify(err.detail) : `HTTP ${res.status}`);
            }
            const data = await res.json();
            lastMarkdown = data.markdown;
            renderPreview(lastMarkdown, payload.protocol_name);
        } catch (e) {
            console.error('Generate error:', e);
            document.getElementById('preview-content').innerHTML =
                `<p style="color:red">Error: ${e.message}</p>`;
        } finally {
            btn.disabled = false;
            btn.textContent = 'Generate & Preview';
        }
    }

    function renderPreview(markdown, protocolName) {
        const content = document.getElementById('preview-content');
        content.innerHTML = typeof marked !== 'undefined'
            ? marked.parse(markdown)
            : `<pre>${markdown}</pre>`;

        if (typeof mermaid !== 'undefined') {
            content.querySelectorAll('code.language-mermaid').forEach(block => {
                const wrapper = document.createElement('div');
                wrapper.className = 'mermaid';
                wrapper.textContent = block.textContent;
                block.parentElement.replaceWith(wrapper);
            });
            mermaid.run({ nodes: content.querySelectorAll('.mermaid') });
        }

        document.getElementById('copy-markdown-btn').style.display = 'inline-block';
        document.getElementById('download-btn').style.display = 'inline-block';
        document.getElementById('download-btn').dataset.name = `${slugify(protocolName)}.md`;
    }

    document.getElementById('generate-preview-btn').addEventListener('click', generatePreview);

    document.getElementById('copy-markdown-btn').addEventListener('click', () => {
        navigator.clipboard.writeText(lastMarkdown).then(() => {
            const btn = document.getElementById('copy-markdown-btn');
            btn.textContent = 'Copied!';
            setTimeout(() => { btn.textContent = 'Copy Markdown'; }, 2000);
        });
    });

    document.getElementById('download-btn').addEventListener('click', () => {
        const filename = document.getElementById('download-btn').dataset.name || 'protocol.md';
        const blob = new Blob([lastMarkdown], { type: 'text/markdown' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = filename;
        a.click();
        URL.revokeObjectURL(a.href);
    });

}); // end DOMContentLoaded
