// Motion Graphics Engine - Block 2: Principles & CCP Operations (Slides 07 to 13)
// Zero emojis: Pure industrial vectors, high-fidelity real PNG assets, timeline-synced kinetic animation
window.HACCP_PRINCIPLES = {
  // Slide 07: The 7 Principles of HACCP
  renderSlide07() {
    return `
      <div class="explainer-scene scene-s07">
        <div class="s07-pillar-layout">
          <div class="s07-header">
            <span class="scene-kicker">CODEX ALIMENTARIUS STANDARD</span>
            <h2 class="scene-headline">The 7 Principles of HACCP</h2>
          </div>
          <div class="principles-grid">
            <div class="principle-cell" data-t="5.0"><span class="p-num">01</span><span class="p-name">Hazard Analysis</span></div>
            <div class="principle-cell" data-t="12.0"><span class="p-num">02</span><span class="p-name">Identify CCPs</span></div>
            <div class="principle-cell" data-t="19.0"><span class="p-num">03</span><span class="p-name">Critical Limits</span></div>
            <div class="principle-cell" data-t="26.0"><span class="p-num">04</span><span class="p-name">Monitoring</span></div>
            <div class="principle-cell" data-t="33.0"><span class="p-num">05</span><span class="p-name">Corrective Action</span></div>
            <div class="principle-cell" data-t="40.0"><span class="p-num">06</span><span class="p-name">Verification</span></div>
            <div class="principle-cell p-final" data-t="46.0"><span class="p-num">07</span><span class="p-name">Documentation</span></div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 08: Determining Critical Control Points (Codex Tree)
  renderSlide08() {
    return window.HACCP_GRAPHICS.renderCCPDecisionTree();
  },

  // Slide 09: Your Work Area CCPs (Interactive Reflection)
  renderSlide09() {
    return `
      <div class="explainer-scene scene-s09">
        <div class="s09-radar-layout">
          <div class="radar-hud-circle">
            <div class="radar-sweep-beam"></div>
            <div class="radar-target tg-1"><span class="tg-label">INTAKE</span></div>
            <div class="radar-target tg-2"><span class="tg-label">PASTEURISER</span></div>
            <div class="radar-target tg-3"><span class="tg-label">CHEESE VATS</span></div>
            <div class="radar-target tg-4"><span class="tg-label">PACKAGING</span></div>
          </div>
          <div class="s09-prompt-intel">
            <span class="scene-kicker">OPERATIONAL AWARENESS</span>
            <h2 class="scene-headline">Where is Your Critical Step?</h2>
            <p class="scene-subhead">Every dairy operative holds direct responsibility for monitoring and safeguarding the CCP parameters in their station.</p>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 10: Importance of HACCP for Our Company
  renderSlide10() {
    return `
      <div class="explainer-scene scene-s10">
        <div class="s10-pillars-grid">
          <div class="value-pillar" data-t="5.0">
            <span class="vp-index">PILLAR 01</span>
            <h3 class="vp-title">Consumer Protection</h3>
            <p class="vp-desc">Ensures millions of families consume dairy products safe from micro, chemical or physical harm.</p>
          </div>
          <div class="value-pillar" data-t="22.0">
            <span class="vp-index">PILLAR 02</span>
            <h3 class="vp-title">Brand Integrity</h3>
            <p class="vp-desc">Avoids devastating multi-million pound product recalls and commercial reputation damage.</p>
          </div>
          <div class="value-pillar" data-t="42.0">
            <span class="vp-index">PILLAR 03</span>
            <h3 class="vp-title">Statutory License</h3>
            <p class="vp-desc">Mandatory requirement to legally trade and manufacture food across the UK and European Union.</p>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 11: Production CCPs: Filtration & Heat Treatment (Pilot)
  renderSlide11() {
    return window.HACCP_GRAPHICS.renderPasteurizationExplainer();
  },

  // Slide 12: Production CCPs: Chilling & Metal Detection
  renderSlide12() {
    return `
      <div class="explainer-scene scene-s12">
        <div class="s12-conveyor-layout">
          <!-- Left: Chilling CCP (<4°C) -->
          <div class="s12-chilling-zone">
            <div class="zone-tag">CCP // COLD CHAIN RETENTION</div>
            <h3 class="zone-title">Continuous Chilling (&lt; 4.0°C)</h3>
            <div class="cryo-meter">
              <span class="cryo-val">3.4°C</span>
              <span class="cryo-status">TARGET MAINTAINED</span>
            </div>
            <p class="zone-desc">Rapid thermal drawdown prevents germination of psychrotrophic spore-formers.</p>
          </div>

          <!-- Right: Metal Detection & Rejection Conveyor -->
          <div class="s12-metal-detector-zone">
            <div class="zone-tag">CCP // IN-LINE METAL DETECTION</div>
            <h3 class="zone-title">Automated Rejection Conveyor</h3>
            <div class="conveyor-rig">
              <div class="conveyor-belt">
                <div class="moving-pack pack-clean">
                  <img src="assets/images/foods/cheese.png" class="conveyor-png" alt="Cheese pack">
                </div>
                <div class="detector-aperture">
                  <span class="aperture-beam"></span>
                  <span class="aperture-lbl">TEST 1.5mm Fe</span>
                </div>
              </div>
              <div class="reject-divert-bin">
                <span class="bin-status">SECURE REJECT BIN // KEY LOCKED</span>
              </div>
            </div>
            <p class="zone-desc">Continuous search coils detect ferrous, non-ferrous and stainless steel contamination.</p>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 13: Monitoring Procedures & Deviation Management
  renderSlide13() {
    return `
      <div class="explainer-scene scene-s13">
        <div class="s13-deviation-grid">
          <div class="dev-chart-card">
            <span class="scene-kicker">REAL-TIME MONITORING</span>
            <h3 class="card-heading">Parameter Telemetry &amp; Critical Limits</h3>
            <div class="telemetry-chart">
              <svg viewBox="0 0 500 160" class="telemetry-svg">
                <line x1="20" y1="40" x2="480" y2="40" stroke="#f87171" stroke-width="2" stroke-dasharray="4 4"/>
                <line x1="20" y1="120" x2="480" y2="120" stroke="#f87171" stroke-width="2" stroke-dasharray="4 4"/>
                <path d="M 20 80 Q 140 75 220 85 T 380 78 T 480 82" fill="none" stroke="#38bdf8" stroke-width="3" />
                <text x="25" y="32" fill="#f87171" font-size="11" font-weight="700">Upper Critical Limit</text>
                <text x="25" y="145" fill="#f87171" font-size="11" font-weight="700">Lower Critical Limit</text>
              </svg>
            </div>
          </div>
          <div class="dev-protocol-card">
            <span class="scene-kicker">DEVIATION WORKFLOW</span>
            <h3 class="card-heading">Instant Action Protocol</h3>
            <div class="protocol-steps">
              <div class="proto-step"><span class="ps-n">1</span><span>Halt Line &amp; Segregate Lot</span></div>
              <div class="proto-step"><span class="ps-n">2</span><span>Identify Equipment Root Cause</span></div>
              <div class="proto-step"><span class="ps-n">3</span><span>Document in QA Non-Conformance Log</span></div>
            </div>
          </div>
        </div>
      </div>
    `;
  }
};
