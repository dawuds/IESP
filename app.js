/**
 * IESP Toolkit — Single Page Application
 * BNM RMiT Nov 2025 Independent External Service Provider Review Framework
 */

(async function () {
  'use strict';

  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

  // State
  let clauseMap = null;
  let controlDomains = null;
  let decisionTree = null;
  let inventory = null;
  let controlMapping = null;
  let currentSection = 'overview';
  let decisionPath = [];

  // Caching layer
  var cache = new Map();

  // Load data
  async function loadJSON(path) {
    if (cache.has(path)) return cache.get(path);
    try {
      var res = await fetch(path);
      if (!res.ok) throw new Error(res.status);
      var data = await res.json();
      cache.set(path, data);
      return data;
    } catch (e) {
      console.error('Failed to load ' + path, e);
      return null;
    }
  }

  // Visual error handler
  function renderError(msg) {
    return '<div class="error-state"><h3>Error</h3><p>' + msg + '</p></div>';
  }

  // HTML escape utility
  function escHtml(s) {
    var d = document.createElement('div');
    d.textContent = s;
    return d.innerHTML;
  }

  // Export functions
  function exportToPDF() {
    window.print();
  }

  function exportToCSV() {
    var rows = [['Domain', 'Part D Ref', 'Description']];
    if (window._controlDomains && window._controlDomains.domains) {
      window._controlDomains.domains.forEach(function(d) {
        rows.push([d.name, d.partDRef || d.appendixRef || '', d.description]);
      });
    }
    var csv = rows.map(function(r) { return r.map(function(c) { return '"' + String(c).replace(/"/g, '""') + '"'; }).join(','); }).join('\n');
    var blob = new Blob([csv], { type: 'text/csv' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'iesp-controls.csv';
    a.click();
  }

  async function init() {
    [clauseMap, controlDomains, decisionTree, inventory, controlMapping] = await Promise.all([
      loadJSON('artifacts/clause-map.json'),
      loadJSON('controls/control-domains.json'),
      loadJSON('decision-tree/decision-tree.json'),
      loadJSON('artifacts/inventory.json'),
      loadJSON('controls/control-mapping.json'),
    ]);

    // Store control domains globally for export
    if (controlDomains) window._controlDomains = controlDomains;

    // Nav handling
    $$('.nav-link').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const section = link.dataset.section;
        navigateTo(section);
      });
    });

    // Search
    const searchInput = $('#search');
    if (searchInput) {
      searchInput.addEventListener('input', debounce((e) => {
        const q = e.target.value.trim().toLowerCase();
        if (q.length >= 2) {
          renderSearch(q);
        } else {
          renderSection(currentSection);
        }
      }, 300));
    }

    // Initial render
    const hash = location.hash.replace('#', '') || 'overview';
    navigateTo(hash);

    // Dark mode
    var darkToggle = document.createElement('button');
    darkToggle.className = 'dark-toggle';
    darkToggle.setAttribute('aria-label', 'Toggle dark mode');
    darkToggle.textContent = '\u{1F319}';
    darkToggle.onclick = function() {
      document.body.classList.toggle('dark');
      var isDark = document.body.classList.contains('dark');
      localStorage.setItem('darkMode', isDark ? 'on' : 'off');
      darkToggle.textContent = isDark ? '\u{2600}\u{FE0F}' : '\u{1F319}';
    };
    var headerEl = document.querySelector('.header-controls') || document.querySelector('header');
    if (headerEl) headerEl.appendChild(darkToggle);
    // Restore preference
    if (localStorage.getItem('darkMode') === 'on' || (!localStorage.getItem('darkMode') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.body.classList.add('dark');
      darkToggle.textContent = '\u{2600}\u{FE0F}';
    }
  }

  function navigateTo(section) {
    currentSection = section;
    location.hash = section;

    $$('.nav-link').forEach(l => l.classList.toggle('active', l.dataset.section === section));
    renderSection(section);
  }

  function renderSection(section) {
    const app = $('#app');
    switch (section) {
      case 'overview': app.innerHTML = renderOverview(); break;
      case 'decision-tree': app.innerHTML = renderDecisionTree(); break;
      case 'engagements': app.innerHTML = renderEngagements(); break;
      case 'controls': app.innerHTML = renderControls(); break;
      case 'work-programs': app.innerHTML = renderWorkPrograms(); break;
      case 'templates': app.innerHTML = renderTemplates(); break;
      case 'evidence': app.innerHTML = renderEvidence(); break;
      default: app.innerHTML = renderOverview();
    }
    bindEventHandlers();
  }

  // ==================== RENDERERS ====================

  function renderOverview() {
    const engagements = clauseMap?.mappings || [];
    const domains = controlDomains?.domains || [];
    const awps = inventory?.categories?.['audit-work-programs']?.items || [];
    const templates = inventory?.categories?.templates?.items || [];
    const evidenceItems = inventory?.categories?.evidence?.items || [];

    return `
      <div class="section-header">
        <h2>IESP Toolkit Overview</h2>
        <p>Independent External Service Provider review framework for BNM RMiT compliance</p>
      </div>

      <div class="stats">
        <div class="stat">
          <div class="stat-value">${engagements.length}</div>
          <div class="stat-label">Engagement Types</div>
        </div>
        <div class="stat">
          <div class="stat-value">${domains.length}</div>
          <div class="stat-label">Control Domains</div>
        </div>
        <div class="stat">
          <div class="stat-value">${awps.length}</div>
          <div class="stat-label">Audit Work Programs</div>
        </div>
        <div class="stat">
          <div class="stat-value">${templates.length}</div>
          <div class="stat-label">Templates</div>
        </div>
        <div class="stat">
          <div class="stat-value">${evidenceItems.length}</div>
          <div class="stat-label">Evidence Checklists</div>
        </div>
      </div>

      <h3 style="margin-bottom:1rem">Core Engagement Types</h3>
      <div class="grid">
        ${engagements.slice(0, 5).map(e => `
          <div class="card">
            <h3>${e.name}</h3>
            <p>${e.frequency}</p>
            <div style="margin-top:0.75rem">
              ${e.triggerClauses.map(c => `<span class="clause-ref">${c}</span>`).join(' ')}
              <span class="tag tag-s" style="margin-left:0.5rem">${e.marker}</span>
              ${e.boardDeliberation ? '<span class="tag tag-engagement" style="margin-left:0.25rem">Board</span>' : ''}
              ${e.bnmConsultation ? '<span class="tag tag-engagement" style="margin-left:0.25rem">BNM Consultation</span>' : ''}
            </div>
          </div>
        `).join('')}
      </div>

      <h3 style="margin:2rem 0 1rem">Appendix 7 Reporting Framework</h3>
      <table>
        <thead><tr><th>Part</th><th>Title</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td><strong>Part A</strong></td><td>Risk Assessment Report</td><td>6-section report: FI details, ESP details, application, risk assessment, quality assurance, signatory</td></tr>
          <tr><td><strong>Part B</strong></td><td>Format of Confirmation</td><td>9-point attestation by CISO/board/senior management</td></tr>
          <tr><td><strong>Part C</strong></td><td>Requirements on External Party Assurance</td><td>6 requirements the independent ESP must follow</td></tr>
          <tr><td><strong>Part D</strong></td><td>Minimum Controls</td><td>Control domains: access, physical, operations, comms, incident, BCP, online transactions, mobile</td></tr>
        </tbody>
      </table>

      <h3 style="margin:2rem 0 1rem">Quick Links</h3>
      <div class="grid">
        <a href="decision-tree/when-iesp-required.md" class="card" style="text-decoration:none">
          <h3>Decision Tree Guide</h3>
          <p>When is an IESP review required? Flowchart and criteria.</p>
        </a>
        <a href="requirements/regulatory-requirements.md" class="card" style="text-decoration:none">
          <h3>Regulatory Requirements</h3>
          <p>All RMIT clauses that trigger or relate to IESP reviews.</p>
        </a>
        <a href="https://github.com/dawuds/RMIT" class="card" style="text-decoration:none">
          <h3>RMIT Compliance Database</h3>
          <p>Full 121-clause structured extraction with 365 templates.</p>
        </a>
      </div>
    `;
  }

  function renderDecisionTree() {
    if (!decisionTree) return '<p>Decision tree data not available.</p>';

    const root = decisionTree.rootNode;
    return `
      <div class="section-header">
        <h2>IESP Decision Tree</h2>
        <p>Determine whether an Independent External Service Provider review is required</p>
      </div>

      <div id="decision-container">
        <div class="decision-node active">
          <div class="decision-question">${root.question}</div>
          ${root.options.map((opt, i) => `
            <div class="decision-option" data-next="${opt.nextNode || ''}" data-idx="${i}">
              ${opt.label}
            </div>
          `).join('')}
        </div>
        <div id="decision-result"></div>
      </div>

      <div style="margin-top:2rem">
        <a href="decision-tree/when-iesp-required.md">View full decision tree documentation</a>
      </div>
    `;
  }

  function renderEngagements() {
    if (!clauseMap) return '<p>Engagement data not available.</p>';

    return `
      <div class="section-header">
        <h2>IESP Engagement Types</h2>
        <p>${clauseMap.mappings.length} engagement types defined under BNM RMiT</p>
      </div>

      <div class="grid-2">
        ${clauseMap.mappings.map(e => `
          <div class="card">
            <h3>${e.name}</h3>
            <table style="margin-top:0.75rem">
              <tr><td style="width:140px;font-weight:600">Type</td><td><code>${e.engagementType}</code></td></tr>
              <tr><td style="font-weight:600">Trigger</td><td>${e.triggerClauses.map(c => `<span class="clause-ref">${c}</span>`).join(' ')}</td></tr>
              <tr><td style="font-weight:600">Frequency</td><td>${e.frequency}</td></tr>
              <tr><td style="font-weight:600">Marker</td><td><span class="tag tag-s">${e.marker}</span></td></tr>
              <tr><td style="font-weight:600">Scope</td><td>${e.scopeClauses.length ? e.scopeClauses.map(c => `<span class="clause-ref">${c}</span>`).join(' ') : 'As directed'}</td></tr>
              <tr><td style="font-weight:600">Reporting</td><td>${(e.reportingRequirements || []).join(', ')}</td></tr>
              ${e.appendixScope ? `<tr><td style="font-weight:600">Appendix</td><td>${e.appendixScope.join(', ')}</td></tr>` : ''}
              <tr><td style="font-weight:600">Board</td><td>${e.boardDeliberation ? 'Required' : 'Not required'}</td></tr>
              ${e.bnmConsultation ? '<tr><td style="font-weight:600">BNM</td><td>Consultation required</td></tr>' : ''}
              ${e.prerequisites ? `<tr><td style="font-weight:600">Prerequisites</td><td><ul style="margin:0;padding-left:1.2rem">${e.prerequisites.map(p => `<li style="font-size:0.8rem">${p}</li>`).join('')}</ul></td></tr>` : ''}
              ${e.notes ? `<tr><td style="font-weight:600">Notes</td><td style="font-size:0.8rem">${e.notes}</td></tr>` : ''}
            </table>
          </div>
        `).join('')}
      </div>
    `;
  }

  function renderControls() {
    if (!controlDomains) return '<p>Control data not available.</p>';

    const domains = controlDomains.domains || [];
    return `
      <div class="section-header">
        <h2>IESP Control Domains</h2>
        <p>${domains.length} control domains from Appendix 7 Part D — minimum controls the IESP must assess</p>
      </div>

      ${domains.map(d => `
        <div class="card">
          <h3>${d.name}</h3>
          <p>${d.description}</p>
          <div style="margin-top:0.5rem">
            ${d.rmitClauses ? d.rmitClauses.map(c => `<span class="clause-ref">${c}</span>`).join(' ') : ''}
            ${d.appendixRef ? `<span class="tag tag-engagement">${d.appendixRef}</span>` : ''}
            ${d.partDRef ? `<span class="tag tag-g" style="margin-left:0.5rem">Part D: ${d.partDRef}</span>` : ''}
          </div>
          ${d.subControls ? `
            <ul style="margin-top:0.75rem;padding-left:1.2rem;font-size:0.85rem;color:var(--text-secondary)">
              ${d.subControls.map(s => `<li>${s}</li>`).join('')}
            </ul>
          ` : ''}
          ${d.subDomains ? `
            <div style="margin-top:0.75rem;display:flex;flex-wrap:wrap;gap:0.25rem">
              ${d.subDomains.map(s => `<span class="tag tag-engagement">${s}</span>`).join('')}
            </div>
          ` : ''}
          ${d.riskCategories ? `
            ${d.riskCategories.map(rc => `
              <div style="margin-top:0.5rem">
                <strong style="font-size:0.85rem">${rc.category}:</strong>
                <span style="font-size:0.8rem;color:var(--text-secondary)">${rc.areas.join(', ')}</span>
              </div>
            `).join('')}
          ` : ''}
        </div>
      `).join('')}

      ${controlMapping ? `
        <h3 style="margin:2rem 0 1rem">Cross-Framework Mapping</h3>
        <div style="overflow-x:auto">
          <table>
            <thead><tr><th>IESP Domain</th><th>RMIT Clauses</th><th>ISO 27001:2022</th><th>NIST CSF 2.0</th></tr></thead>
            <tbody>
              ${controlMapping.mappings.map(m => `
                <tr>
                  <td><strong>${m.iespDomain}</strong></td>
                  <td>${m.rmitClauses.map(c => `<span class="clause-ref">${c}</span>`).join(' ')}</td>
                  <td style="font-size:0.8rem">${m.iso27001.join(', ')}</td>
                  <td style="font-size:0.8rem">${m.nistCsf.join(', ')}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      ` : ''}
    `;
  }

  function renderWorkPrograms() {
    const items = inventory?.categories?.['audit-work-programs']?.items || [];
    return `
      <div class="section-header">
        <h2>Audit Work Programs</h2>
        <p>Step-by-step review procedures with test objectives, steps, expected evidence, and pass/fail criteria</p>
      </div>
      <div class="grid">
        ${items.map(item => `
          <a href="audit-work-programs/${item.slug}.md" class="card" style="text-decoration:none">
            <h3>${item.name}</h3>
          </a>
        `).join('')}
      </div>
    `;
  }

  function renderTemplates() {
    const items = inventory?.categories?.templates?.items || [];
    return `
      <div class="section-header">
        <h2>Engagement & Reporting Templates</h2>
        <p>BNM Appendix 7 formats and practitioner templates</p>
      </div>
      <div class="grid">
        ${items.map(item => `
          <a href="templates/${item.slug}.md" class="card" style="text-decoration:none">
            <h3>${item.name}</h3>
          </a>
        `).join('')}
      </div>
    `;
  }

  function renderEvidence() {
    const items = inventory?.categories?.evidence?.items || [];
    return `
      <div class="section-header">
        <h2>Evidence Checklists</h2>
        <p>Evidence collection guides by engagement type</p>
      </div>
      <div class="grid">
        <a href="evidence/evidence-requirements.md" class="card" style="text-decoration:none">
          <h3>Evidence Requirements Overview</h3>
          <p>Cross-engagement evidence requirements</p>
        </a>
        ${items.map(item => `
          <a href="evidence/${item.slug}.md" class="card" style="text-decoration:none">
            <h3>${item.name}</h3>
          </a>
        `).join('')}
      </div>
    `;
  }

  function renderSearch(query) {
    const app = $('#app');
    const results = [];

    // Search engagements
    if (clauseMap) {
      clauseMap.mappings.forEach(e => {
        const text = `${e.name} ${e.engagementType} ${e.triggerClauses.join(' ')} ${e.frequency}`.toLowerCase();
        if (text.includes(query)) {
          results.push({ type: 'Engagement', name: e.name, detail: e.frequency, section: 'engagements' });
        }
      });
    }

    // Search controls
    if (controlDomains) {
      controlDomains.domains.forEach(d => {
        const text = `${d.name} ${d.description} ${(d.subControls || []).join(' ')} ${(d.subDomains || []).join(' ')}`.toLowerCase();
        if (text.includes(query)) {
          results.push({ type: 'Control Domain', name: d.name, detail: d.description, section: 'controls' });
        }
      });
    }

    // Search inventory
    if (inventory) {
      Object.values(inventory.categories).forEach(cat => {
        cat.items.forEach(item => {
          if (item.name.toLowerCase().includes(query) || item.slug.includes(query)) {
            results.push({ type: cat.name, name: item.name, detail: item.slug, section: '' });
          }
        });
      });
    }

    app.innerHTML = `
      <div class="section-header">
        <h2>Search Results</h2>
        <p>${results.length} result${results.length !== 1 ? 's' : ''} for "${query}"</p>
      </div>
      ${results.length === 0 ? '<p>No results found.</p>' : ''}
      ${results.map(r => `
        <div class="card" ${r.section ? `onclick="location.hash='${r.section}'" style="cursor:pointer"` : ''}>
          <span class="tag tag-engagement">${r.type}</span>
          <h3 style="margin-top:0.5rem">${r.name}</h3>
          <p>${r.detail}</p>
        </div>
      `).join('')}
    `;
  }

  // ==================== EVENT HANDLERS ====================

  function bindEventHandlers() {
    // Decision tree interactions
    $$('.decision-option').forEach(opt => {
      opt.addEventListener('click', () => handleDecisionClick(opt));
    });
  }

  function handleDecisionClick(opt) {
    const nextId = opt.dataset.next;
    const resultDiv = $('#decision-result');
    if (!resultDiv || !decisionTree) return;

    if (!nextId) return;

    const node = decisionTree.nodes[nextId];
    if (!node) return;

    // Mark selected
    opt.style.background = 'var(--accent-light)';
    opt.style.borderColor = 'var(--accent)';
    opt.style.fontWeight = '600';

    if (node.outcome) {
      const outcome = decisionTree.outcomes[node.outcome];
      const isRequired = node.outcome === 'iesp-required';
      resultDiv.innerHTML = `
        <div class="${isRequired ? 'outcome-required' : 'outcome-not-required'}" style="margin-top:1rem">
          <h3>${outcome.label}</h3>
          ${node.engagementType ? `<p style="margin-top:0.5rem"><strong>Engagement:</strong> ${node.engagementType}</p>` : ''}
          ${node.clause ? `<p><strong>Clause:</strong> <span class="clause-ref">${node.clause}</span></p>` : ''}
          ${node.note ? `<p style="margin-top:0.5rem;font-size:0.85rem">${node.note}</p>` : ''}
          <ul style="margin-top:0.75rem;padding-left:1.2rem;font-size:0.85rem">
            ${outcome.actions.map(a => `<li>${a}</li>`).join('')}
          </ul>
        </div>
      `;
    } else if (node.question) {
      resultDiv.innerHTML = `
        <div class="decision-node active" style="margin-top:1rem">
          <div class="decision-question">${node.question}</div>
          ${node.options.map((nopt, i) => `
            <div class="decision-option" data-next="${nopt.nextNode || ''}" data-outcome="${nopt.outcome || ''}" data-engagement="${nopt.engagementType || ''}" data-clause="${nopt.clause || ''}" data-note="${nopt.note || ''}" data-idx="${i}">
              ${nopt.label}
            </div>
          `).join('')}
        </div>
        <div id="decision-result-nested"></div>
      `;

      // Bind nested options
      $$('.decision-option', resultDiv).forEach(nestedOpt => {
        nestedOpt.addEventListener('click', () => {
          const nestedNext = nestedOpt.dataset.next;
          const nestedOutcome = nestedOpt.dataset.outcome;
          const nestedResultDiv = $('#decision-result-nested') || resultDiv;

          nestedOpt.style.background = 'var(--accent-light)';
          nestedOpt.style.borderColor = 'var(--accent)';
          nestedOpt.style.fontWeight = '600';

          if (nestedOutcome) {
            const outcome = decisionTree.outcomes[nestedOutcome];
            const isReq = nestedOutcome === 'iesp-required';
            nestedResultDiv.innerHTML = `
              <div class="${isReq ? 'outcome-required' : 'outcome-not-required'}" style="margin-top:1rem">
                <h3>${outcome.label}</h3>
                ${nestedOpt.dataset.engagement ? `<p style="margin-top:0.5rem"><strong>Engagement:</strong> ${nestedOpt.dataset.engagement}</p>` : ''}
                ${nestedOpt.dataset.clause ? `<p><strong>Clause:</strong> <span class="clause-ref">${nestedOpt.dataset.clause}</span></p>` : ''}
                ${nestedOpt.dataset.note ? `<p style="margin-top:0.5rem;font-size:0.85rem">${nestedOpt.dataset.note}</p>` : ''}
                <ul style="margin-top:0.75rem;padding-left:1.2rem;font-size:0.85rem">
                  ${outcome.actions.map(a => `<li>${a}</li>`).join('')}
                </ul>
              </div>
            `;
          } else if (nestedNext) {
            handleDecisionClick(nestedOpt);
          }
        });
      });
    }
  }

  // ==================== UTILITIES ====================

  function debounce(fn, ms) {
    let timer;
    return (...args) => {
      clearTimeout(timer);
      timer = setTimeout(() => fn(...args), ms);
    };
  }

  // Boot
  init();
})();
