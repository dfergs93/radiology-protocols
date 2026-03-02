document.addEventListener('DOMContentLoaded', () => {
    const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
        ? 'http://localhost:8001'
        : 'https://radiology-protocols.onrender.com'; // Replace with your actual production backend URL

    const input = document.getElementById('protocoller-input');
    const btn = document.getElementById('protocoller-btn');
    const resultsContainer = document.getElementById('protocoller-results');
    const loading = document.getElementById('protocoller-loading');

    // Handle Enter key
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            btn.click();
        }
    });

    btn.addEventListener('click', async () => {
        const indication = input.value.trim();
        if (!indication) return;

        // UI State: Loading
        btn.disabled = true;
        loading.style.display = 'block';
        resultsContainer.style.display = 'none';
        resultsContainer.innerHTML = '';

        try {
            const response = await fetch(`${API_BASE_URL}/api/protocoller`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ indication })
            });

            if (!response.ok) {
                throw new Error(`API Error: ${response.status}`);
            }

            const data = await response.json();
            displayResults(data);

        } catch (error) {
            console.error('Protocoller error:', error);
            resultsContainer.innerHTML = `<div style="color: red; padding: 10px;">Error: ${error.message}</div>`;
            resultsContainer.style.display = 'block';
        } finally {
            btn.disabled = false;
            loading.style.display = 'none';
        }
    });

    function displayResults(data) {
        const wrapper = document.getElementById('protocol-suggestions-wrapper');
        resultsContainer.innerHTML = '';

        if (!data.recommended_protocols?.length && !data.custom_protocol) {
            wrapper.style.display = 'none';
            return;
        }

        // Show and auto-open results
        wrapper.style.display = 'block';
        wrapper.open = true;
        resultsContainer.style.display = 'flex';

        const allProtocols = [];

        // Add standard protocols
        if (data.recommended_protocols) {
            data.recommended_protocols.forEach(p => {
                allProtocols.push({ ...p, type: 'standard' });
            });
        }

        // Add custom protocol
        if (data.custom_protocol) {
            allProtocols.push({ ...data.custom_protocol, type: 'custom' });
        }

        // Limit to 3 (as requested, though backend usually only sends 3 standard + 1 custom max)
        allProtocols.slice(0, 3).forEach(protocol => {
            const card = document.createElement('div');
            card.className = 'protocol-rec-card';

            const isCustom = protocol.type === 'custom';
            const badgeClass = isCustom ? 'badge-custom' : 'badge-standard';
            const badgeLabel = isCustom ? 'Custom AI' : 'Standard';
            const icon = isCustom ? '✨ ' : '';

            card.innerHTML = `
                <div class="rec-badge ${badgeClass}">${badgeLabel}</div>
                <div class="rec-title">${icon}${protocol.title}</div>
                <div class="rec-reasoning">${protocol.reasoning || protocol.description || ''}</div>
                <div class="rec-action-hint">Click to compare →</div>
            `;

            card.addEventListener('click', () => {
                if (isCustom) {
                    addCustomProtocol(protocol);
                } else {
                    selectProtocol(protocol.title);
                }

                // Feedback animation
                card.style.borderColor = 'var(--md-accent-fg-color)';
                card.style.transform = 'scale(0.98)';
                setTimeout(() => {
                    card.style.borderColor = '';
                    card.style.transform = '';
                }, 200);
            });

            resultsContainer.appendChild(card);
        });
    }

    function selectProtocol(title) {
        // Find index in global protocolData
        if (typeof protocolData === 'undefined') {
            console.error('protocolData is undefined. Make sure protocol-compare.js is loaded.');
            return;
        }

        const index = protocolData.findIndex(p => p.title === title);
        if (index === -1) {
            alert(`Could not find protocol "${title}" in the database.`);
            return;
        }

        const selects = document.querySelectorAll('.protocol-select');
        let targetSelect = null;

        // 1. Check if already selected
        for (let select of selects) {
            if (select.value == index) { // Use == for string/number comparison
                console.log('Protocol already selected');
                document.getElementById('protocol-compare-container').scrollIntoView({ behavior: 'smooth' });
                return;
            }
        }

        // 2. Find first empty slot
        for (let select of selects) {
            if (select.value === "") {
                targetSelect = select;
                break;
            }
        }

        // 2. If no empty slots, add a new one
        if (!targetSelect) {
            if (typeof addProtocolSlot === 'function') {
                targetSelect = addProtocolSlot();
            } else {
                // Fallback to overwriting last if function missing
                targetSelect = selects[selects.length - 1];
            }
        }

        // 3. Set value
        if (targetSelect) {
            targetSelect.value = index;
            // Sync searchable UI
            if (typeof createSearchableSelect === 'function') {
                createSearchableSelect(targetSelect);
            }
        }

        // Scroll to selectors
        document.getElementById('protocol-compare-container').scrollIntoView({ behavior: 'smooth' });
    }

    function addCustomProtocol(custom) {
        if (typeof protocolData === 'undefined' || typeof populateSelectors === 'undefined') {
            console.error('Missing dependencies from protocol-compare.js');
            return;
        }

        // Ensure category is set
        custom.category = "Custom / AI Generated";
        custom.filepath = "custom_generated"; // Helper for uniqueness

        // Push to global data
        protocolData.push(custom);
        const newIndex = protocolData.length - 1;

        // Refresh dropdowns (selection is preserved by the new populateSelectors logic)
        populateSelectors();

        // Select it immediately using the same smart logic
        const selects = document.querySelectorAll('.protocol-select');
        let targetSelect = null;

        // 1. Check if already selected
        for (let select of selects) {
            if (select.value == newIndex) {
                document.getElementById('protocol-compare-container').scrollIntoView({ behavior: 'smooth' });
                return;
            }
        }

        // 2. Find first empty slot
        for (let select of selects) {
            if (select.value === "") {
                targetSelect = select;
                break;
            }
        }

        if (!targetSelect) {
            if (typeof addProtocolSlot === 'function') {
                targetSelect = addProtocolSlot();
            } else {
                targetSelect = selects[selects.length - 1];
            }
        }

        if (targetSelect) {
            targetSelect.value = newIndex;
            // Sync searchable UI
            if (typeof createSearchableSelect === 'function') {
                createSearchableSelect(targetSelect);
            }
        }

        document.getElementById('protocol-compare-container').scrollIntoView({ behavior: 'smooth' });
    }
});
