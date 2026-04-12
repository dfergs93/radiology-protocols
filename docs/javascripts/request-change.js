(function () {
  'use strict';

  // ─── Helpers ────────────────────────────────────────────────────────────────

  function getBasePath(pathname) {
    // From any URL, derive the base_path by splitting on /request-change
    // e.g. /radiology-protocols/request-change/ → /radiology-protocols
    var parts = pathname.split('/request-change');
    return parts[0] || '';
  }

  function getParam(name) {
    var params = new URLSearchParams(window.location.search);
    return params.get(name);
  }

  function slugify(text) {
    return text
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-|-$/g, '');
  }

  function arrayToLines(arr) {
    if (!arr || !Array.isArray(arr)) return '';
    return arr.join('\n');
  }

  function linesToArray(str) {
    return str
      .split('\n')
      .map(function (s) { return s.trim(); })
      .filter(function (s) { return s.length > 0; });
  }

  function val(id) {
    var el = document.getElementById(id);
    return el ? el.value : '';
  }

  function setVal(id, value) {
    var el = document.getElementById(id);
    if (el) el.value = value || '';
  }

  // ─── Button injection on protocol pages ─────────────────────────────────────

  function injectProtocolButton() {
    // Only run if we are NOT on the request-change page
    if (document.getElementById('rc-app')) return;

    var path = window.location.pathname;
    // Match /ct/<category>/<slug>/ (two segments after /ct/)
    var match = path.match(/^(.*\/ct\/[^/]+\/)([^/]+)\/?$/);
    if (!match) return;

    var beforeSlug = match[1]; // everything up to and including second segment
    var slug = match[2];

    // Derive base: everything before /ct/
    var ctIdx = beforeSlug.indexOf('/ct/');
    var base = ctIdx >= 0 ? beforeSlug.substring(0, ctIdx) : '';

    var h1 = document.querySelector('article h1');
    if (!h1) return;

    var link = document.createElement('a');
    link.href = base + '/request-change/?protocol=' + encodeURIComponent(slug);
    link.textContent = 'Request a Change';
    link.className = 'rc-request-btn';
    link.style.cssText = [
      'display:inline-block',
      'flex-shrink:0',
      'margin-left:1rem',
      'padding:0.25rem 0.75rem',
      'border:1px solid',
      'border-radius:4px',
      'font-size:0.75rem',
      'font-weight:normal',
      'text-decoration:none',
      'white-space:nowrap',
      'align-self:center',
    ].join(';');

    h1.style.cssText = 'display:flex;align-items:center;justify-content:space-between;';
    h1.appendChild(link);
  }

  // ─── Series row helpers ──────────────────────────────────────────────────────

  function makeSeriesRow(s) {
    s = s || {};
    var row = document.createElement('div');
    row.className = 'rc-series-row';
    row.style.cssText = 'display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr 2fr auto;gap:0.4rem;margin-bottom:0.4rem;align-items:center;';

    var fields = [
      { name: 'name', placeholder: 'Series name', value: s.name || '' },
      { name: 'start', placeholder: 'Start', value: s.start || '' },
      { name: 'end', placeholder: 'End', value: s.end || '' },
      { name: 'delay', placeholder: 'Delay', value: s.delay || '' },
      { name: 'thickness', placeholder: 'Thickness', value: s.thickness || '' },
      { name: 'notes', placeholder: 'Notes', value: s.notes || '' },
    ];

    fields.forEach(function (f) {
      var input = document.createElement('input');
      input.type = 'text';
      input.placeholder = f.placeholder;
      input.value = f.value;
      input.dataset.field = f.name;
      input.className = 'rc-series-field';
      input.style.cssText = 'width:100%;padding:0.3rem;font-size:0.85rem;border:1px solid #ccc;border-radius:3px;';
      row.appendChild(input);
    });

    var removeBtn = document.createElement('button');
    removeBtn.type = 'button';
    removeBtn.textContent = '✕';
    removeBtn.title = 'Remove row';
    removeBtn.style.cssText = 'padding:0.25rem 0.5rem;cursor:pointer;background:#e57373;color:#fff;border:none;border-radius:3px;';
    removeBtn.addEventListener('click', function () { row.parentNode.removeChild(row); });
    row.appendChild(removeBtn);

    return row;
  }

  function getSeriesRows() {
    var rows = document.querySelectorAll('#rc-series-container .rc-series-row');
    var result = [];
    rows.forEach(function (row) {
      var obj = {};
      row.querySelectorAll('.rc-series-field').forEach(function (input) {
        obj[input.dataset.field] = input.value.trim();
      });
      result.push(obj);
    });
    return result;
  }

  function populateSeries(seriesArr) {
    var container = document.getElementById('rc-series-container');
    if (!container) return;
    container.innerHTML = '';
    (seriesArr || []).forEach(function (s) {
      container.appendChild(makeSeriesRow(s));
    });
  }

  // ─── Form population ─────────────────────────────────────────────────────────

  function populateForm(protocol) {
    setVal('rc-title', protocol.title || '');
    setVal('rc-slug', protocol.slug || '');
    setVal('rc-category', protocol.category || '');
    setVal('rc-position', protocol.position || '');
    setVal('rc-npo', protocol.npo || '');
    setVal('rc-indications', arrayToLines(protocol.clinical_indications));
    setVal('rc-premedication', protocol.premedication || '');

    var contrast = protocol.contrast || {};
    setVal('rc-agent', contrast.agent || '');
    setVal('rc-volume', contrast.volume || '');
    setVal('rc-flow-rate', contrast.flow_rate || '');
    setVal('rc-duration', contrast.duration || '');
    setVal('rc-timing', contrast.timing || '');
    setVal('rc-roi', contrast.roi || '');
    setVal('rc-trigger', contrast.trigger || '');

    populateSeries(protocol.series || []);

    var notes = protocol.notes || {};
    setVal('rc-tech', notes.tech || '');
    setVal('rc-nursing', notes.nursing || '');
    setVal('rc-rad', notes.rad || '');
    setVal('rc-tips', notes.tips || '');

    var safety = protocol.safety || {};
    setVal('rc-renal', safety.renal || '');
    setVal('rc-allergy', safety.allergy || '');
  }

  function readFormValues() {
    return {
      title: val('rc-title'),
      slug: val('rc-slug'),
      category: val('rc-category'),
      position: val('rc-position'),
      npo: val('rc-npo'),
      clinical_indications: linesToArray(val('rc-indications')),
      premedication: val('rc-premedication'),
      contrast: {
        agent: val('rc-agent'),
        volume: val('rc-volume'),
        flow_rate: val('rc-flow-rate'),
        duration: val('rc-duration'),
        timing: val('rc-timing'),
        roi: val('rc-roi'),
        trigger: val('rc-trigger'),
      },
      series: getSeriesRows(),
      notes: {
        tech: val('rc-tech'),
        nursing: val('rc-nursing'),
        rad: val('rc-rad'),
        tips: val('rc-tips'),
      },
      safety: {
        renal: val('rc-renal'),
        allergy: val('rc-allergy'),
      },
      free_text: val('rc-free-text'),
    };
  }

  // ─── Diff logic ──────────────────────────────────────────────────────────────

  var FIELD_KEYS = {
    'Title': 'title', 'Category': 'category', 'Position': 'position',
    'NPO': 'npo', 'Clinical Indications': 'indications_json',
    'Premedication': 'premedication',
    'Contrast Agent': 'contrast_agent', 'Contrast Volume': 'contrast_volume',
    'Flow Rate': 'contrast_flow_rate', 'Duration': 'contrast_duration',
    'Timing': 'contrast_timing', 'ROI': 'contrast_roi', 'Trigger': 'contrast_trigger',
    'Series': 'series_json',
    'Tech Notes': 'notes_tech', 'Nursing Notes': 'notes_nursing',
    'Radiologist Notes': 'notes_rad', 'Tips': 'notes_tips',
    'Renal': 'safety_renal', 'Allergy': 'safety_allergy'
  };

  function diffValues(original, current) {
    var changes = [];

    function addChange(label, origVal, newVal) {
      var o = (origVal === undefined || origVal === null) ? '' : String(origVal);
      var n = (newVal === undefined || newVal === null) ? '' : String(newVal);
      if (o !== n) {
        changes.push({ label: label, key: FIELD_KEYS[label] || label, original: o, proposed: n });
      }
    }

    addChange('Title', original.title, current.title);
    addChange('Category', original.category, current.category);
    addChange('Position', original.position, current.position);
    addChange('NPO', original.npo, current.npo);

    var origIndic = arrayToLines(original.clinical_indications || []);
    addChange('Clinical Indications', origIndic, val('rc-indications'));

    addChange('Premedication', original.premedication, current.premedication);

    var oc = original.contrast || {};
    addChange('Contrast Agent', oc.agent, current.contrast.agent);
    addChange('Contrast Volume', oc.volume, current.contrast.volume);
    addChange('Flow Rate', oc.flow_rate, current.contrast.flow_rate);
    addChange('Duration', oc.duration, current.contrast.duration);
    addChange('Timing', oc.timing, current.contrast.timing);
    addChange('ROI', oc.roi, current.contrast.roi);
    addChange('Trigger', oc.trigger, current.contrast.trigger);

    var origSeries = JSON.stringify(original.series || []);
    var newSeries = JSON.stringify(current.series || []);
    if (origSeries !== newSeries) {
      changes.push({ label: 'Series', key: 'series_json', original: origSeries, proposed: newSeries });
    }

    var on = original.notes || {};
    addChange('Tech Notes', on.tech, current.notes.tech);
    addChange('Nursing Notes', on.nursing, current.notes.nursing);
    addChange('Radiologist Notes', on.rad, current.notes.rad);
    addChange('Tips', on.tips, current.notes.tips);

    var os = original.safety || {};
    addChange('Renal', os.renal, current.safety.renal);
    addChange('Allergy', os.allergy, current.safety.allergy);

    return changes;
  }

  // ─── Body formatting ─────────────────────────────────────────────────────────

  function formatChangeBody(protocol, changes, freeText) {
    var lines = [
      '**Protocol:** ' + protocol.title,
      '**Slug:** ' + protocol.slug,
      '',
      '## Requested Changes',
      '',
    ];

    changes.forEach(function (c) {
      lines.push('**' + c.label + '**');
      lines.push('- Current: ' + (c.original || '(empty)'));
      lines.push('- Proposed: ' + (c.proposed || '(empty)'));
      lines.push('');
    });

    if (freeText) {
      lines.push('## Additional Notes', '', freeText);
    }

    return lines.join('\n');
  }

  function formatNewProtocolBody(baseProtocol, current) {
    var lines = [
      '**New Protocol Request**',
      '**Based on:** ' + (baseProtocol ? baseProtocol.title : '(none)'),
      '',
      '## Protocol Details',
      '',
      '**Title:** ' + current.title,
      '**Slug:** ' + current.slug,
      '**Category:** ' + current.category,
      '**Clinical Indications:** ' + (current.clinical_indications || []).join(', '),
      '**Position:** ' + current.position,
      '**NPO:** ' + current.npo,
      '**Premedication:** ' + current.premedication,
      '',
      '## Contrast',
      '**Agent:** ' + current.contrast.agent,
      '**Volume:** ' + current.contrast.volume,
      '**Flow Rate:** ' + current.contrast.flow_rate,
      '**Duration:** ' + current.contrast.duration,
      '**Timing:** ' + current.contrast.timing,
      '**ROI:** ' + current.contrast.roi,
      '**Trigger:** ' + current.contrast.trigger,
      '',
      '## Series',
      JSON.stringify(current.series, null, 2),
      '',
      '## Notes',
      '**Tech:** ' + current.notes.tech,
      '**Nursing:** ' + current.notes.nursing,
      '**Radiologist:** ' + current.notes.rad,
      '**Tips:** ' + current.notes.tips,
      '',
      '## Safety',
      '**Renal:** ' + current.safety.renal,
      '**Allergy:** ' + current.safety.allergy,
    ];

    if (current.free_text) {
      lines.push('', '## Additional Notes', '', current.free_text);
    }

    return lines.join('\n');
  }

  // ─── Submission ──────────────────────────────────────────────────────────────

  function submitRequest(feedbackUrl, title, slug, body) {
    var subject = 'Protocol Change Request: ' + title + ' (' + slug + ')';

    if (!feedbackUrl) {
      showMessage('Contact your protocol lead directly.', 'info');
      return;
    }

    if (feedbackUrl.startsWith('mailto:')) {
      var mailUrl = feedbackUrl +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);
      window.location.href = mailUrl;
    } else if (feedbackUrl.indexOf('github.com') !== -1) {
      var issueUrl = feedbackUrl +
        '?title=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);
      window.open(issueUrl, '_blank');
    } else {
      showMessage('Contact your protocol lead directly.', 'info');
    }
  }

  function showMessage(msg, type) {
    var el = document.getElementById('rc-message');
    if (!el) return;
    el.textContent = msg;
    el.style.display = 'block';
    el.className = 'rc-message rc-message--' + (type || 'info');
  }

  // ─── Form builder ────────────────────────────────────────────────────────────

  function buildForm(protocols, config, isNewMode, preselectedProtocol) {
    var app = document.getElementById('rc-app');
    app.innerHTML = '';

    var style = document.createElement('style');
    style.textContent = [
      '.rc-form { max-width: 860px; }',
      '.rc-fieldset { border: 1px solid var(--md-default-fg-color--lightest, #ddd); border-radius: 6px; padding: 1rem 1.25rem; margin-bottom: 1.25rem; }',
      '.rc-fieldset legend { font-weight: 600; padding: 0 0.5rem; }',
      '.rc-field-group { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-bottom: 0.5rem; }',
      '.rc-field-group.single { grid-template-columns: 1fr; }',
      '.rc-field { display: flex; flex-direction: column; gap: 0.25rem; }',
      '.rc-field label { font-size: 0.8rem; font-weight: 500; }',
      '.rc-field input, .rc-field textarea, .rc-field select { padding: 0.4rem 0.6rem; border: 1px solid #ccc; border-radius: 4px; font-size: 0.9rem; width: 100%; box-sizing: border-box; background: var(--md-default-bg-color, #fff); color: var(--md-default-fg-color, #000); }',
      '.rc-field textarea { resize: vertical; min-height: 80px; }',
      '.rc-series-header { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr 2fr auto; gap: 0.4rem; margin-bottom: 0.3rem; }',
      '.rc-series-header span { font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light, #555); }',
      '.rc-add-series-btn { margin-top: 0.5rem; padding: 0.3rem 0.75rem; background: var(--md-primary-fg-color, #3f51b5); color: #fff; border: none; border-radius: 4px; cursor: pointer; font-size: 0.85rem; }',
      '.rc-submit-btn { padding: 0.5rem 1.5rem; background: var(--md-primary-fg-color, #3f51b5); color: #fff; border: none; border-radius: 4px; cursor: pointer; font-size: 1rem; }',
      '.rc-submit-btn:hover { opacity: 0.9; }',
      '.rc-message { display: none; padding: 0.75rem 1rem; border-radius: 4px; margin-top: 1rem; }',
      '.rc-message--info { background: #e3f2fd; color: #1565c0; border: 1px solid #90caf9; }',
      '.rc-message--error { background: #ffebee; color: #b71c1c; border: 1px solid #ef9a9a; }',
      '.rc-protocol-info { background: var(--md-default-bg-color, #f5f5f5); border: 1px solid #ddd; border-radius: 4px; padding: 0.5rem 0.75rem; margin-bottom: 1rem; font-size: 0.9rem; }',
    ].join('\n');
    app.appendChild(style);

    var form = document.createElement('form');
    form.className = 'rc-form';
    form.id = 'rc-form';

    // ── Mode B: protocol selector ────────────────────────────────────────────
    if (isNewMode) {
      var selectFS = document.createElement('fieldset');
      selectFS.className = 'rc-fieldset';
      var selectLeg = document.createElement('legend');
      selectLeg.textContent = 'Base Protocol (optional)';
      selectFS.appendChild(selectLeg);

      var selectField = document.createElement('div');
      selectField.className = 'rc-field';
      var selectLabel = document.createElement('label');
      selectLabel.textContent = 'Select a protocol to pre-fill fields';
      selectLabel.htmlFor = 'rc-base-select';
      var select = document.createElement('select');
      select.id = 'rc-base-select';

      var defaultOpt = document.createElement('option');
      defaultOpt.value = '';
      defaultOpt.textContent = '-- None (start blank) --';
      select.appendChild(defaultOpt);

      // Group by category
      var byCategory = {};
      protocols.forEach(function (p) {
        var cat = p.category || 'Other';
        if (!byCategory[cat]) byCategory[cat] = [];
        byCategory[cat].push(p);
      });

      Object.keys(byCategory).sort().forEach(function (cat) {
        var optgroup = document.createElement('optgroup');
        optgroup.label = cat.charAt(0).toUpperCase() + cat.slice(1);
        byCategory[cat].forEach(function (p) {
          var opt = document.createElement('option');
          opt.value = p.slug;
          opt.textContent = p.title;
          optgroup.appendChild(opt);
        });
        select.appendChild(optgroup);
      });

      select.addEventListener('change', function () {
        if (!this.value) return;
        var found = protocols.find(function (p) { return p.slug === select.value; });
        if (found) populateForm(found);
        // Auto-clear title and slug so user must provide new ones
        setVal('rc-title', '');
        setVal('rc-slug', '');
      });

      selectField.appendChild(selectLabel);
      selectField.appendChild(select);
      selectFS.appendChild(selectField);
      form.appendChild(selectFS);
    } else {
      // Mode A: show protocol info bar
      if (preselectedProtocol) {
        var infoDiv = document.createElement('div');
        infoDiv.className = 'rc-protocol-info';
        infoDiv.innerHTML = 'Requesting change for: <strong>' + preselectedProtocol.title + '</strong>';
        form.appendChild(infoDiv);
      }
    }

    // ── Clinical fieldset ────────────────────────────────────────────────────
    form.appendChild(makeFieldset('Clinical', [
      makeField('rc-indications', 'Clinical Indications (one per line)', 'textarea'),
      makeField('rc-position', 'Patient Position'),
      makeField('rc-npo', 'NPO Instructions'),
    ]));

    // ── Preparation fieldset ─────────────────────────────────────────────────
    form.appendChild(makeFieldset('Preparation', [
      makeField('rc-premedication', 'Premedication / Oral Contrast', 'textarea', true),
    ]));

    // ── Contrast fieldset ────────────────────────────────────────────────────
    form.appendChild(makeFieldset('Contrast', [
      makeField('rc-agent', 'Agent'),
      makeField('rc-volume', 'Volume'),
      makeField('rc-flow-rate', 'Flow Rate'),
      makeField('rc-duration', 'Duration'),
      makeField('rc-timing', 'Timing'),
      makeField('rc-roi', 'ROI'),
      makeField('rc-trigger', 'Trigger'),
    ]));

    // ── Series fieldset ──────────────────────────────────────────────────────
    var seriesFS = document.createElement('fieldset');
    seriesFS.className = 'rc-fieldset';
    var seriesLeg = document.createElement('legend');
    seriesLeg.textContent = 'Series';
    seriesFS.appendChild(seriesLeg);

    var headerDiv = document.createElement('div');
    headerDiv.className = 'rc-series-header';
    ['Name', 'Start', 'End', 'Delay', 'Thickness', 'Notes', ''].forEach(function (h) {
      var span = document.createElement('span');
      span.textContent = h;
      headerDiv.appendChild(span);
    });
    seriesFS.appendChild(headerDiv);

    var container = document.createElement('div');
    container.id = 'rc-series-container';
    seriesFS.appendChild(container);

    var addBtn = document.createElement('button');
    addBtn.type = 'button';
    addBtn.className = 'rc-add-series-btn';
    addBtn.textContent = '+ Add Series';
    addBtn.addEventListener('click', function () {
      container.appendChild(makeSeriesRow({}));
    });
    seriesFS.appendChild(addBtn);
    form.appendChild(seriesFS);

    // ── Notes fieldset ───────────────────────────────────────────────────────
    form.appendChild(makeFieldset('Notes', [
      makeField('rc-tech', 'Technologist Notes', 'textarea'),
      makeField('rc-nursing', 'Nursing Notes', 'textarea'),
      makeField('rc-rad', 'Radiologist Notes', 'textarea'),
      makeField('rc-tips', 'Tips', 'textarea'),
    ]));

    // ── Safety fieldset ──────────────────────────────────────────────────────
    form.appendChild(makeFieldset('Safety', [
      makeField('rc-renal', 'Renal Guidance'),
      makeField('rc-allergy', 'Allergy Guidance'),
    ]));

    // ── Metadata (title/slug/category) ───────────────────────────────────────
    var metaFS = makeFieldset('Protocol Identity', [
      makeField('rc-title', 'Protocol Title' + (isNewMode ? ' (required)' : '')),
      makeField('rc-slug', 'Slug' + (isNewMode ? ' (auto-generated, editable)' : '')),
      makeField('rc-category', 'Category'),
    ]);
    // Insert at top of form (after selector or info bar)
    form.insertBefore(metaFS, form.children[isNewMode ? 1 : (preselectedProtocol ? 1 : 0)]);

    // ── Free text ────────────────────────────────────────────────────────────
    form.appendChild(makeFieldset('Additional Notes / Reason for Change', [
      makeField('rc-free-text', 'Optional notes or context for reviewers', 'textarea', true),
    ]));

    // ── Title auto-slug (Mode B only) ────────────────────────────────────────
    if (isNewMode) {
      var titleInput = document.getElementById('rc-title');
      if (titleInput) {
        titleInput.addEventListener('input', function () {
          var slugInput = document.getElementById('rc-slug');
          if (slugInput && !slugInput.dataset.userEdited) {
            slugInput.value = slugify(this.value);
          }
        });
        var slugInput = document.getElementById('rc-slug');
        if (slugInput) {
          slugInput.addEventListener('input', function () {
            this.dataset.userEdited = 'true';
          });
        }
      }
    }

    // ── Message area ─────────────────────────────────────────────────────────
    var msg = document.createElement('div');
    msg.id = 'rc-message';
    msg.className = 'rc-message';
    form.appendChild(msg);

    // ── Submit button or no-feedback message ─────────────────────────────────
    var feedbackUrl = config.feedback_url || '';
    if (!feedbackUrl) {
      var noFeedback = document.createElement('p');
      noFeedback.style.cssText = 'color:var(--md-default-fg-color--light,#555);font-style:italic;';
      noFeedback.textContent = 'Contact your protocol lead directly.';
      form.appendChild(noFeedback);
    } else {
      var submitBtn = document.createElement('button');
      submitBtn.type = 'submit';
      submitBtn.className = 'rc-submit-btn';
      submitBtn.textContent = 'Submit Request';
      form.appendChild(submitBtn);
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      handleSubmit(protocols, config, isNewMode, preselectedProtocol);
    });

    app.appendChild(form);

    // ── Pre-fill if Mode A ───────────────────────────────────────────────────
    if (!isNewMode && preselectedProtocol) {
      populateForm(preselectedProtocol);
    }
  }

  function makeFieldset(legend, fields) {
    var fs = document.createElement('fieldset');
    fs.className = 'rc-fieldset';
    var leg = document.createElement('legend');
    leg.textContent = legend;
    fs.appendChild(leg);
    fields.forEach(function (f) { fs.appendChild(f); });
    return fs;
  }

  function makeField(id, labelText, type, fullWidth) {
    var wrapper = document.createElement('div');
    wrapper.className = 'rc-field-group' + (fullWidth || type === 'textarea' ? ' single' : '');

    var field = document.createElement('div');
    field.className = 'rc-field';

    var label = document.createElement('label');
    label.htmlFor = id;
    label.textContent = labelText;

    var input;
    if (type === 'textarea') {
      input = document.createElement('textarea');
    } else {
      input = document.createElement('input');
      input.type = 'text';
    }
    input.id = id;
    input.name = id;

    field.appendChild(label);
    field.appendChild(input);
    wrapper.appendChild(field);
    return wrapper;
  }

  // ─── Submit handler ──────────────────────────────────────────────────────────

  function handleSubmit(protocols, config, isNewMode, preselectedProtocol) {
    var current = readFormValues();
    var feedbackUrl = config.feedback_url || '';

    if (isNewMode) {
      // Mode B: new protocol
      if (!current.title) {
        showMessage('Please provide a protocol title.', 'error');
        return;
      }
      var baseProt = null;
      var baseSelect = document.getElementById('rc-base-select');
      if (baseSelect && baseSelect.value) {
        baseProt = protocols.find(function (p) { return p.slug === baseSelect.value; }) || null;
      }
      var body = formatNewProtocolBody(baseProt, current);
      var title = 'New Protocol Request: ' + current.title;
      var slug = current.slug || slugify(current.title);
      submitRequest(feedbackUrl, title, slug, body);
    } else {
      // Mode A: change request
      var original = preselectedProtocol || {};
      var changes = diffValues(original, current);
      var freeText = current.free_text;

      if (changes.length === 0 && !freeText) {
        showMessage('No changes detected. Edit at least one field before submitting.', 'info');
        return;
      }

      var body = formatChangeBody(original, changes, freeText);
      if (changes.length > 0) {
        var changesMap = {};
        changes.forEach(function (c) { if (c.key) { changesMap[c.key] = c.proposed; } });
        var encoded = encodeURIComponent(btoa(JSON.stringify(changesMap)));
        var slug = original.slug || '';
        body += '\n---\nApply in Admin App: http://localhost:5173/edit/' + slug + '?apply=' + encoded;
      }
      submitRequest(feedbackUrl, original.title || 'Unknown', original.slug || '', body);
    }
  }

  // ─── Main form initializer ───────────────────────────────────────────────────

  function initForm() {
    var app = document.getElementById('rc-app');
    if (!app) return;

    var pathname = window.location.pathname;
    var base = getBasePath(pathname);

    var formsUrl = base + '/javascripts/protocol-forms-index.json';
    var configUrl = base + '/javascripts/institution-config.json';

    Promise.all([
      fetch(formsUrl).then(function (r) { return r.json(); }),
      fetch(configUrl).then(function (r) { return r.json(); }),
    ]).then(function (results) {
      var protocols = results[0];
      var config = results[1];

      var protocolSlug = getParam('protocol');
      var modeParam = getParam('mode');
      var isNewMode = (modeParam === 'new') || (!protocolSlug && !modeParam);

      var preselectedProtocol = null;
      if (protocolSlug) {
        preselectedProtocol = protocols.find(function (p) { return p.slug === protocolSlug; }) || null;
        if (!preselectedProtocol) {
          app.innerHTML = '<p>Protocol "' + protocolSlug + '" not found. <a href="' + base + '/request-change/?mode=new">Request a new protocol</a>.</p>';
          return;
        }
      }

      buildForm(protocols, config, isNewMode, preselectedProtocol);
    }).catch(function (err) {
      console.error('rc: failed to load data', err);
      app.innerHTML = '<p>Failed to load form data. Please try again later.</p>';
    });
  }

  // ─── Entry point ─────────────────────────────────────────────────────────────

  document.addEventListener('DOMContentLoaded', function () {
    injectProtocolButton();
    initForm();
  });

})();
