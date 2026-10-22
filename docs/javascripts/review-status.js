// Review Status page: lists every protocol with its last review date and flags
// ones that are overdue, due soon, or never reviewed. Data comes from
// protocol-comparison-index.json (built by scripts/generate_comparison_index.py).
(function () {
  var SCRIPT_URL = (document.currentScript && document.currentScript.src) || window.location.href;
  var INDEX_URL = new URL('protocol-comparison-index.json', SCRIPT_URL).href;
  var CONFIG_URL = new URL('institution-config.json', SCRIPT_URL).href;
  var SITE_ROOT_URL = new URL('../', SCRIPT_URL).href;

  var STATUS = {
    overdue: { label: 'Overdue', order: 0 },
    never: { label: 'Never reviewed', order: 1 },
    soon: { label: 'Due soon', order: 2 },
    current: { label: 'Current', order: 3 }
  };

  function todayISO() {
    var d = new Date();
    var pad = function (n) { return (n < 10 ? '0' : '') + n; };
    return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
  }

  function daysBetween(fromISO, toISO) {
    return Math.round((Date.parse(toISO) - Date.parse(fromISO)) / 86400000);
  }

  function statusFor(p, today, dueSoonDays) {
    if (!p.next_review_due) return 'never';
    var days = daysBetween(today, p.next_review_due);
    if (days < 0) return 'overdue';
    if (days <= dueSoonDays) return 'soon';
    return 'current';
  }

  function el(tag, attrs, text) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) { node.setAttribute(k, attrs[k]); });
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function render(app, protocols, config) {
    var today = todayISO();
    var dueSoonDays = config.review_due_soon_days || 60;
    var rows = protocols.map(function (p) {
      return { p: p, status: statusFor(p, today, dueSoonDays) };
    });
    rows.sort(function (a, b) {
      return STATUS[a.status].order - STATUS[b.status].order ||
        (a.p.next_review_due || '').localeCompare(b.p.next_review_due || '') ||
        a.p.title.localeCompare(b.p.title);
    });

    var counts = { all: rows.length };
    rows.forEach(function (r) { counts[r.status] = (counts[r.status] || 0) + 1; });

    app.innerHTML = '';
    var intro = el('p', {}, 'Default review interval: every ' + (config.review_interval_months || 12) +
      ' months. "Due soon" means within ' + dueSoonDays + ' days. Today: ' + today + '.');
    app.appendChild(intro);

    var filters = el('div', { class: 'rs-filters', role: 'group', 'aria-label': 'Filter by status' });
    var active = 'all';
    var keys = ['all', 'overdue', 'never', 'soon', 'current'];
    keys.forEach(function (key) {
      var label = key === 'all' ? 'All' : STATUS[key].label;
      var btn = el('button', { type: 'button', 'data-filter': key, class: 'rs-filter rs-' + key },
        label + ' (' + (counts[key] || 0) + ')');
      btn.addEventListener('click', function () { active = key; draw(); });
      filters.appendChild(btn);
    });
    app.appendChild(filters);

    var wrap = el('div', { class: 'rs-table-wrap' });
    var table = el('table', { class: 'rs-table' });
    var head = el('tr');
    ['Protocol', 'Modality', 'Category', 'Status', 'Last reviewed', 'Next due', 'Reviewed by'].forEach(function (h) {
      head.appendChild(el('th', {}, h));
    });
    var thead = el('thead'); thead.appendChild(head); table.appendChild(thead);
    var tbody = el('tbody'); table.appendChild(tbody);
    wrap.appendChild(table);
    app.appendChild(wrap);

    function draw() {
      filters.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.getAttribute('data-filter') === active));
      });
      tbody.innerHTML = '';
      rows.filter(function (r) { return active === 'all' || r.status === active; }).forEach(function (r) {
        var tr = el('tr');
        var nameCell = el('td');
        nameCell.appendChild(el('a', { href: SITE_ROOT_URL + r.p.filepath.replace(/\.md$/, '/') }, r.p.title));
        tr.appendChild(nameCell);
        tr.appendChild(el('td', {}, r.p.modality || ''));
        tr.appendChild(el('td', {}, r.p.category || ''));
        var st = el('td'); st.appendChild(el('span', { class: 'rs-badge rs-' + r.status }, STATUS[r.status].label));
        tr.appendChild(st);
        tr.appendChild(el('td', {}, r.p.last_reviewed || '—'));
        tr.appendChild(el('td', {}, r.p.next_review_due || '—'));
        tr.appendChild(el('td', {}, (r.p.reviewed_by || []).join(', ') || '—'));
        tbody.appendChild(tr);
      });
    }
    draw();
  }

  function init() {
    var app = document.getElementById('review-status-app');
    if (!app || app.getAttribute('data-ready')) return;
    app.setAttribute('data-ready', '1');
    Promise.all([
      fetch(INDEX_URL).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }),
      fetch(CONFIG_URL).then(function (r) { return r.ok ? r.json() : {}; }).catch(function () { return {}; })
    ]).then(function (res) {
      render(app, res[0], res[1]);
    }).catch(function (err) {
      app.textContent = 'Could not load protocol data (' + err.message + ').';
    });
  }

  init();
  if (typeof document$ !== 'undefined') document$.subscribe(init);
})();
