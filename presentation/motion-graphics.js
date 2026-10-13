// Showtime-inspired Dynamic Motion Graphics & Interactive Infographics for HACCP Masterclass
window.HACCP_GRAPHICS = {
  // 1. Pasteurization Curve & Safety Gauge (Slide 11 & Dairy Process)
  renderPasteurizationWidget(startTime = 5.0) {
    return `
      <div class="motion-widget pasteurization-gauge-box">
        <div class="gauge-header">
          <div class="gauge-title-badge">⚡ CRITICAL CONTROL POINT: THERMAL PROFILE</div>
          <div class="live-target-pill">Target: 72°C · Hold: 15s</div>
        </div>
        <div class="gauge-display-area">
          <div class="thermometer-track">
            <div class="thermometer-fill"></div>
            <div class="thermometer-bubble">72°C</div>
          </div>
          <div class="gauge-graph-container">
            <svg class="temp-curve-svg" viewBox="0 0 400 140">
              <defs>
                <linearGradient id="tempGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#38bdf8" />
                  <stop offset="50%" stop-color="#f59e0b" />
                  <stop offset="100%" stop-color="#10b981" />
                </linearGradient>
                <linearGradient id="areaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stop-color="rgba(16, 185, 129, 0.35)" />
                  <stop offset="100%" stop-color="rgba(16, 185, 129, 0.0)" />
                </linearGradient>
              </defs>
              <line x1="30" y1="40" x2="380" y2="40" stroke="rgba(239, 68, 68, 0.5)" stroke-dasharray="4 4" stroke-width="2"/>
              <text x="35" y="32" fill="#ef4444" font-size="11" font-weight="700">Critical Limit: 72°C</text>
              <path d="M 30 120 Q 120 115 180 40 L 320 40 Q 350 40 380 90 L 380 120 L 30 120 Z" fill="url(#areaGrad)" />
              <path d="M 30 120 Q 120 115 180 40 L 320 40 Q 350 40 380 90" fill="none" stroke="url(#tempGrad)" stroke-width="4" stroke-linecap="round" class="animated-curve-line" />
              <circle cx="250" cy="40" r="7" fill="#10b981" class="pulse-point" />
              <text x="262" y="44" fill="#34d399" font-size="12" font-weight="800">SAFE HOLD (15s)</text>
            </svg>
          </div>
        </div>
        <div class="gauge-footer-stats">
          <div class="stat-pill"><span class="stat-dot green"></span> Divert Valve: <strong>Active Auto-Recirculate</strong></div>
          <div class="stat-pill"><span class="stat-dot blue"></span> Pathogen Kill: <strong>Coxiella / L. monocytogenes</strong></div>
        </div>
      </div>
    `;
  },

  // 2. Animated Codex CCP Decision Tree (Slide 08 & Slide 12)
  renderCCPDecisionTree() {
    return `
      <div class="motion-widget ccp-tree-box">
        <div class="tree-header">
          <span class="tree-badge">🌿 CODEX ALIMENTARIUS DECISION TREE</span>
          <span class="tree-sub">Principle 2: Critical Control Points</span>
        </div>
        <div class="tree-flow-row">
          <div class="tree-node node-q1">
            <div class="q-tag">Q1: Preventive Control?</div>
            <div class="q-text">Is there a preventive control measure at this step?</div>
            <div class="node-arrow-out yes">YES ➔</div>
          </div>
          <div class="tree-node node-q2">
            <div class="q-tag">Q2: Eliminate Hazard?</div>
            <div class="q-text">Does this step specifically eliminate or reduce hazard?</div>
            <div class="node-arrow-out yes">YES ➔</div>
          </div>
          <div class="tree-node node-ccp-result">
            <div class="ccp-lock-icon">🔒</div>
            <div class="ccp-res-title">CRITICAL CONTROL POINT</div>
            <div class="ccp-res-sub">Apply Critical Limits, Monitoring & Corrective Action</div>
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
          <div class="core-haccp-icon">🛡️</div>
          <div class="core-haccp-text">HACCP<br>EXCELLENCE</div>
        </div>
      </div>
    `;
  },

  // 4. Interactive 5x5 Hazard Risk Matrix (Slide 07 & Slide 10)
  renderRiskMatrix() {
    return `
      <div class="motion-widget risk-matrix-box">
        <div class="risk-matrix-header">
          <span>🎯 HAZARD SEVERITY &times; PROBABILITY MATRIX</span>
          <span class="high-risk-badge">CCP Threshold: Score &ge; 15</span>
        </div>
        <div class="risk-grid-5x5">
          <div class="risk-cell c-low">1</div><div class="risk-cell c-low">2</div><div class="risk-cell c-med">3</div><div class="risk-cell c-med">4</div><div class="risk-cell c-high">5</div>
          <div class="risk-cell c-low">2</div><div class="risk-cell c-med">4</div><div class="risk-cell c-med">6</div><div class="risk-cell c-high">8</div><div class="risk-cell c-high">10</div>
          <div class="risk-cell c-med">3</div><div class="risk-cell c-med">6</div><div class="risk-cell c-high">9</div><div class="risk-cell c-high">12</div><div class="risk-cell c-critical">15 (CCP)</div>
          <div class="risk-cell c-med">4</div><div class="risk-cell c-high">8</div><div class="risk-cell c-high">12</div><div class="risk-cell c-critical">16 (CCP)</div><div class="risk-cell c-critical">20 (CCP)</div>
          <div class="risk-cell c-high">5</div><div class="risk-cell c-high">10</div><div class="risk-cell c-critical">15 (CCP)</div><div class="risk-cell c-critical">20 (CCP)</div><div class="risk-cell c-critical active-pulse">25 (MAX)</div>
        </div>
      </div>
    `;
  }
};
