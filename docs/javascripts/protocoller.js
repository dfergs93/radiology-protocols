document.addEventListener('DOMContentLoaded', () => {
    const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
        ? 'http://localhost:8001'
        : 'https://protocol-manager-backend.onrender.com'; // Replace with your actual production backend URL

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
        resultsContainer.innerHTML = '';
        resultsContainer.style.display = 'flex';

        // 1. Recommended Standard Protocols
        if (data.recommended_protocols && data.recommended_protocols.length > 0) {
            const header = document.createElement('h4');
            header.textContent = 'Recommended Standard Protocols';
            resultsContainer.appendChild(header);

            data.recommended_protocols.forEach(rec => {
                const card = document.createElement('div');
                card.className = 'protocol-rec-card';
                card.innerHTML = `
                    <div class="rec-title">${rec.title}</div>
                    <div class="rec-reasoning">${rec.reasoning}</div>
                    <div style="margin-top: 8px; font-size: 0.8em; color: var(--md-primary-fg-color);">
                        Click to Select for Comparison
                    </div>
                `;

                card.addEventListener('click', () => {
                    selectProtocol(rec.title);
                    card.style.borderColor = 'green';
                    card.style.backgroundColor = 'rgba(0, 255, 0, 0.05)';
                    setTimeout(() => {
                        card.style.borderColor = '';
                        card.style.backgroundColor = '';
                    }, 500);
                });

                resultsContainer.appendChild(card);
            });
        }

        // 2. Custom Protocol
        if (data.custom_protocol) {
            const header = document.createElement('h4');
            header.textContent = 'Custom Protocol Suggestions';
            header.style.marginTop = '16px';
            resultsContainer.appendChild(header);

            const custom = data.custom_protocol;
            const card = document.createElement('div');
            card.className = 'protocol-rec-card';
            card.style.borderLeftColor = '#e91e63'; // Pink for custom
            card.innerHTML = `
                <div class="rec-title">✨ ${custom.title}</div>
                <div class="rec-reasoning">${custom.description || 'Customized protocol based on specific requirements.'}</div>
                <div style="margin-top: 8px; font-size: 0.8em; color: #e91e63;">
                    Click to Add & Compare
                </div>
            `;

            card.addEventListener('click', () => {
                addCustomProtocol(custom);
                card.style.borderColor = 'green';
                card.innerHTML += '<div style="color: green; font-weight: bold; margin-top: 5px;">Added to Selector!</div>';
            });

            resultsContainer.appendChild(card);
        }
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

        // Find match score if needed, but for now just fill next empty slot
        const selects = document.querySelectorAll('.protocol-select');
        let filled = false;

        // Strategy: Fill first empty, or overwrite the last one if both full
        for (let select of selects) {
            if (select.value === "") {
                select.value = index;
                filled = true;
                break;
            }
        }

        if (!filled && selects.length >= 2) {
            // Overwrite the last one (usually the comparison target)
            selects[selects.length - 1].value = index;
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

        // Refresh dropdowns
        populateSelectors();

        // Select it immediately
        const selects = document.querySelectorAll('.protocol-select');
        // Prefer slot 2 for custom items, or first empty
        if (selects[1].value === "") {
            selects[1].value = newIndex;
        } else if (selects[0].value === "") {
            selects[0].value = newIndex;
        } else {
            selects[1].value = newIndex; // Overwrite 2
        }

        document.getElementById('protocol-compare-container').scrollIntoView({ behavior: 'smooth' });
    }
});
