// Showtime-inspired Dynamic Motion Graphics & Explainer Canvases for HACCP Masterclass
// Pure professional motion design: Zero emojis, high-fidelity real PNG assets & SVG technical vector elements
window.HACCP_GRAPHICS = {
  // 1. Slide 11: Full Explainer Motion Canvas (Zero "slide feel", 100% explainer video)
  renderPasteurizationExplainer() {
    return `
      <div class="showtime-explainer-stage" id="explainer-s11">
        <!-- Progress Pipeline Tracker (Top) -->
        <div class="explainer-pipe-progress">
          <div class="step-pip pip-active" data-phase="1">
            <img src="assets/images/foods/milk.png" class="pip-real-icon" alt="Raw milk">
            <span class="pip-label">Intake &amp; Silos</span>
          </div>
          <div class="pipe-arrow">/</div>
          <div class="step-pip" data-phase="2">
            <span class="pip-num-badge">01</span>
            <span class="pip-label">1000µm Filtration</span>
          </div>
          <div class="pipe-arrow">/</div>
          <div class="step-pip" data-phase="3">
            <span class="pip-num-badge">02</span>
            <span class="pip-label">HTST 72°C Thermal Kill</span>
          </div>
          <div class="pipe-arrow">/</div>
          <div class="step-pip" data-phase="4">
            <img src="assets/images/foods/dessert.png" class="pip-real-icon" alt="Dessert base">
            <span class="pip-label">Cook Vat 86°C</span>
          </div>
        </div>

        <!-- Central Explainer Viewport -->
        <div class="explainer-cinematic-canvas">

          <!-- ACT 1: Physical Hazard Filtration (0.0s - 25.0s) -->
          <div class="explainer-act act-1 is-current" data-start="0.0" data-end="25.0">
            <div class="act-visual">
              <div class="milk-pipe-graphic">
                <div class="pipe-header-bar">
                  <span class="pipe-id">FLOW STREAM // INTAKE LINE A</span>
                  <span class="pipe-flow-rate">25,000 L/HR</span>
                </div>
                <div class="flowing-milk-stream"></div>
                <div class="filter-mesh-barrier">
                  <div class="mesh-grid"></div>
                  <div class="mesh-tag">1000 µm SCREEN</div>
                </div>
                <div class="pure-milk-flow"></div>
              </div>
            </div>
            <div class="act-narrative">
              <span class="act-badge c-blue">CCP 01 · PHYSICAL SEPARATION</span>
              <h2 class="act-title">In-line Raw Milk Filtration</h2>
              <p class="act-lead">Intercepting extraneous farm sediment, straw, and foreign particulate at tanker intake before milk enters storage silos.</p>
              <div class="act-metric-card">
                <span class="metric-num">1,000 µm</span>
                <span class="metric-desc">Certified stainless aperture with verified differential pressure logs</span>
              </div>
            </div>
          </div>

          <!-- ACT 2: HTST Pasteurisation (>72°C / 15s) (25.0s - 50.0s) -->
          <div class="explainer-act act-2" data-start="25.0" data-end="50.0">
            <div class="act-visual">
              <div class="htst-heat-exchanger">
                <div class="heat-plates">
                  <span class="plate"></span><span class="plate"></span><span class="plate"></span><span class="plate"></span>
                </div>
                <div class="digital-gauge">
                  <div class="gauge-temp-display">
                    <span class="temp-val" id="s11-temp-val">72.4</span><span class="temp-unit">°C</span>
                  </div>
                  <div class="target-status">
                    <span class="pulse-dot"></span> CRITICAL LIMIT MAINTAINED
                  </div>
                </div>
                <div class="holding-tube-timer">
                  <div class="timer-ring">
                    <svg viewBox="0 0 100 100">
                      <circle cx="50" cy="50" r="42" class="ring-bg"></circle>
                      <circle cx="50" cy="50" r="42" class="ring-fill"></circle>
                    </svg>
                    <span class="timer-seconds">15s</span>
                  </div>
                  <span class="timer-label">Holding Tube Validation</span>
                </div>
              </div>
            </div>
            <div class="act-narrative">
              <span class="act-badge c-red">CCP 02 · PATHOGEN ELIMINATION</span>
              <h2 class="act-title">Continuous HTST Pasteuriser</h2>
              <p class="act-lead">Whole and skimmed milk must achieve &gt;72°C for at least 15 seconds. If temperature drops below 72.0°C, the flow diversion valve triggers immediately.</p>
              <div class="pathogen-kill-tags">
                <span class="kill-tag">Listeria monocytogenes</span>
                <span class="kill-tag">Salmonella spp.</span>
                <span class="kill-tag">Escherichia coli</span>
              </div>
            </div>
          </div>

          <!-- ACT 3: Dessert & Curd Thermal Cook (>86°C / 20 min) (50.0s - 75.0s) -->
          <div class="explainer-act act-3" data-start="50.0" data-end="75.0">
            <div class="act-visual">
              <div class="cook-vat-chamber">
                <div class="steaming-vat">
                  <div class="vat-body">
                    <img src="assets/images/foods/dessert.png" class="vat-real-img" alt="Dessert batch">
                    <span class="vat-product">Cultured Dairy &amp; Curd Recipe</span>
                  </div>
                </div>
                <div class="thermal-kill-badge">
                  <div class="thermal-level">&gt; 86.0°C</div>
                  <div class="thermal-duration">20 MIN HOLD</div>
                </div>
              </div>
            </div>
            <div class="act-narrative">
              <span class="act-badge c-green">CCP 03 · RECIPE THERMAL STEP</span>
              <h2 class="act-title">Batch Dessert &amp; Curd Thermal Cook</h2>
              <p class="act-lead">Validated cooking profiles for cultured dessert bases and cheese curd formulas, destroying vegetative pathogens prior to cold packing.</p>
              <div class="act-metric-card green-tint">
                <span class="metric-num">86°C · 20m</span>
                <span class="metric-desc">Automated chart recorder logging every batch for statutory compliance</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    `;
  },

  // 2. Animated Codex CCP Decision Tree (Slide 08 & Slide 12)
  renderCCPDecisionTree() {
    return `
      <div class="motion-widget ccp-tree-box">
        <div class="tree-header">
          <span class="tree-badge">CODEX ALIMENTARIUS DECISION TREE</span>
          <span class="tree-sub">Principle 2 · Critical Control Points</span>
        </div>
        <div class="tree-flow-row">
          <div class="tree-node node-q1">
            <div class="q-tag">Question 01</div>
            <div class="q-text">Do preventive control measures exist at this processing step?</div>
            <div class="node-arrow-out yes">YES ➔</div>
          </div>
          <div class="tree-node node-q2">
            <div class="q-tag">Question 02</div>
            <div class="q-text">Does this step specifically eliminate or reduce the hazard to an acceptable level?</div>
            <div class="node-arrow-out yes">YES ➔</div>
          </div>
          <div class="tree-node node-ccp-result">
            <div class="ccp-res-title">CRITICAL CONTROL POINT</div>
            <div class="ccp-res-sub">Establish Critical Limits, Continuous Monitoring &amp; Corrective Actions</div>
          </div>
        </div>
      </div>
    `;
  },

  // 3. Orbital Animated PDCA Cycle (Slide 25)
  renderPDCALoop() {
    return `
      <div class="motion-widget pdca-wheel-box">
        <div class="pdca-central-glow"></div>
        <div class="pdca-quadrant-circle">
          <div class="pdca-quarter plan">
            <span class="pq-letter">P</span>
            <span class="pq-label">PLAN</span>
            <small>Hazard &amp; CCP Setup</small>
          </div>
          <div class="pdca-quarter do">
            <span class="pq-letter">D</span>
            <span class="pq-label">DO</span>
            <small>Daily SOPs &amp; PRPs</small>
          </div>
          <div class="pdca-quarter check">
            <span class="pq-letter">C</span>
            <span class="pq-label">CHECK</span>
            <small>Audits &amp; QA Logs</small>
          </div>
          <div class="pdca-quarter act">
            <span class="pq-letter">A</span>
            <span class="pq-label">ACT</span>
            <small>Continuous Review</small>
          </div>
        </div>
        <div class="pdca-center-core">
          <div class="core-haccp-text">HACCP<br>ASSURANCE</div>
        </div>
      </div>
    `;
  },

  // 4. Interactive 5x5 Hazard Risk Matrix (Slide 07 & Slide 10)
  renderRiskMatrix() {
    return `
      <div class="motion-widget risk-matrix-box">
        <div class="risk-matrix-header">
          <span>SEVERITY &times; PROBABILITY MATRIX</span>
          <span class="high-risk-badge">CCP Threshold: Score &ge; 15</span>
        </div>
        <div class="risk-grid-5x5">
          <div class="risk-cell c-low">1</div><div class="risk-cell c-low">2</div><div class="risk-cell c-med">3</div><div class="risk-cell c-med">4</div><div class="risk-cell c-high">5</div>
          <div class="risk-cell c-low">2</div><div class="risk-cell c-med">4</div><div class="risk-cell c-med">6</div><div class="risk-cell c-high">8</div><div class="risk-cell c-high">10</div>
          <div class="risk-cell c-med">3</div><div class="risk-cell c-med">6</div><div class="risk-cell c-high">9</div><div class="risk-cell c-high">12</div><div class="risk-cell c-critical">15 CCP</div>
          <div class="risk-cell c-med">4</div><div class="risk-cell c-high">8</div><div class="risk-cell c-high">12</div><div class="risk-cell c-critical">16 CCP</div><div class="risk-cell c-critical">20 CCP</div>
          <div class="risk-cell c-high">5</div><div class="risk-cell c-high">10</div><div class="risk-cell c-critical">15 CCP</div><div class="risk-cell c-critical">20 CCP</div><div class="risk-cell c-critical active-pulse">25 MAX</div>
        </div>
      </div>
    `;
  }
};
