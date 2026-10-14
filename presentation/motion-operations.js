// Motion Graphics Engine - Block 4: Operations, PRPs & Closing (Slides 21 to 26)
// Zero emojis: Pure industrial vectors, high-fidelity real PNG assets, timeline-synced kinetic animation
window.HACCP_OPERATIONS = {
  // Slide 21: Factory Hygiene Zoning & Stationery Coding
  renderSlide21() {
    return `
      <div class="explainer-scene scene-s21">
        <div class="s21-zoning-map">
          <div class="zone-box zb-low">
            <span class="zb-badge">LOW RISK ZONE</span>
            <h4 class="zb-title">Intake &amp; Dry Goods</h4>
            <p class="zb-desc">Street clothing barrier; blue factory coats and dedicated blue stationery only.</p>
          </div>
          <div class="zone-barrier">
            <span class="barrier-line"></span>
            <span class="barrier-text">HYGIENE BARRIER // BOOT WASH &amp; AIR SHOWER</span>
            <span class="barrier-line"></span>
          </div>
          <div class="zone-box zb-high">
            <span class="zb-badge c-green">HIGH CARE // HIGH RISK ZONE</span>
            <h4 class="zb-title">Pasteurised Filling &amp; Packing</h4>
            <p class="zb-desc">Full captive footwear change, beard nets, sanitisation airlocks and red stationery.</p>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 22: Prerequisite Programmes (PRPs)
  renderSlide22() {
    return `
      <div class="explainer-scene scene-s22">
        <div class="s22-prp-foundation">
          <div class="prp-top-roof">
            <span class="roof-label">HACCP SYSTEM // SPECIFIC CCP CONTROLS</span>
          </div>
          <div class="prp-pillars-base">
            <div class="prp-col"><span class="pc-t">Pest Control</span></div>
            <div class="prp-col"><span class="pc-t">CIP Sanitation</span></div>
            <div class="prp-col"><span class="pc-t">Water Potability</span></div>
            <div class="prp-col"><span class="pc-t">Staff Training</span></div>
            <div class="prp-col"><span class="pc-t">Supplier Approval</span></div>
            <div class="prp-col"><span class="pc-t">Waste Removal</span></div>
          </div>
          <div class="prp-bedrock">
            <span>PREREQUISITE PROGRAMMES (PRPs) // FOUNDATIONAL HYGIENE BASELINE</span>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 23: Cross-Contamination & 4-Point Labelling
  renderSlide23() {
    return `
      <div class="explainer-scene scene-s23">
        <div class="s23-label-rig">
          <div class="label-demo-card">
            <div class="ld-header">
              <span class="ld-brand">DAIRY OPERATIONS QA // 4-POINT TRACEABILITY LABEL</span>
            </div>
            <div class="ld-fields-grid">
              <div class="ld-field"><span class="ld-k">1. MATERIAL NAME</span><span class="ld-v">Whole Milk Curd Batch A</span></div>
              <div class="ld-field"><span class="ld-k">2. DATE &amp; TIME OPENED</span><span class="ld-v">14/10/2026 // 06:30 GMT</span></div>
              <div class="ld-field"><span class="ld-k">3. USE-BY / EXPIRY DATE</span><span class="ld-v">17/10/2026 // 06:30 GMT</span></div>
              <div class="ld-field"><span class="ld-k">4. OPERATOR INITIALS</span><span class="ld-v">RL / QA-TECH-04</span></div>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 24: Corrective Actions & The PDCA Quality Cycle
  renderSlide24() {
    return `
      <div class="explainer-scene scene-s24">
        <div class="s24-corrective-trio">
          <div class="action-card ac-1">
            <span class="ac-num">01</span>
            <h3 class="ac-title">Isolate &amp; Quarantine</h3>
            <p class="ac-desc">Immediately place affected product on hold. Tag with red physical hold tape and system lock.</p>
          </div>
          <div class="action-card ac-2">
            <span class="ac-num">02</span>
            <h3 class="ac-title">Determine Root Cause</h3>
            <p class="ac-desc">Investigate why critical limit was breached (sensor failure, operator error, flow valve stuck).</p>
          </div>
          <div class="action-card ac-3">
            <span class="ac-num">03</span>
            <h3 class="ac-title">Prevent Recurrence</h3>
            <p class="ac-desc">Implement mechanical calibration, SOP revisions or re-training before restarting the production line.</p>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 25: The HACCP Team & Individual Legal Liability
  renderSlide25() {
    return `
      <div class="explainer-scene scene-s25">
        <div class="s25-split-layout">
          <div class="team-governance-side">
            <span class="scene-kicker">CROSS-FUNCTIONAL HACCP TEAM</span>
            <h2 class="scene-headline">Multi-Disciplinary Accountability</h2>
            <div class="team-roles-list">
              <div class="tr-role"><span>Operations &amp; Production Management</span></div>
              <div class="tr-role"><span>Technical &amp; Quality Assurance</span></div>
              <div class="tr-role"><span>Engineering &amp; Maintenance</span></div>
              <div class="tr-role"><span>Microbiology &amp; Hygiene Lead</span></div>
            </div>
          </div>
          <div class="team-wheel-side">
            ${window.HACCP_GRAPHICS.renderPDCALoop()}
          </div>
        </div>
      </div>
    `;
  },

  // Slide 26: Course References & Assessment Review
  renderSlide26() {
    return `
      <div class="explainer-scene scene-s26">
        <div class="s26-closing-card">
          <span class="scene-kicker">MODULE COMPLETION</span>
          <h2 class="scene-headline">HACCP Level 2 Knowledge Assessment</h2>
          <p class="scene-subhead">You have covered all fundamental statutory requirements, CCP monitoring criteria, hazard vectors, and allergen safety policies.</p>
          
          <div class="closing-summary-pills">
            <span class="pill-check">7 Codex Principles Mastered</span>
            <span class="pill-check">Allergen Annex II Verified</span>
            <span class="pill-check">Thermal Pasteurisation Compliant</span>
            <span class="pill-check">100% Nut-Free Site Policy Acknowledged</span>
          </div>
        </div>
      </div>
    `;
  }
};
