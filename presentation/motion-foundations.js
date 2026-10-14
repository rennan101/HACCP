// Motion Graphics Engine - Block 1: Foundations & Legal Scope (Slides 01 to 06)
// Zero emojis: Pure industrial vectors, high-fidelity real PNG assets, timeline-synced kinetic animation
window.HACCP_FOUNDATIONS = {
  // Slide 01: Welcome & Course Overview
  renderSlide01() {
    return `
      <div class="explainer-scene scene-s01">
        <div class="s01-stage-layout">
          <!-- Left: Narrative & Real Product Cascade -->
          <div class="s01-info-panel">
            <span class="scene-kicker">UK &amp; EU FOOD SAFETY DIRECTIVE</span>
            <h1 class="scene-headline">HACCP Level 2 Training</h1>
            <p class="scene-subhead">Essential hygiene management standards engineered for food and dairy processing facilities.</p>
            
            <div class="s01-products-stream">
              <div class="prod-item p1" data-t="18.0">
                <img src="assets/images/foods/milk.png" class="prod-png" alt="Raw milk">
                <div class="prod-meta">
                  <span class="p-title">Milk Intake &amp; Silos</span>
                  <span class="p-spec">Reg. (EC) 852/2004</span>
                </div>
              </div>
              <div class="prod-item p2" data-t="21.0">
                <img src="assets/images/foods/cheese.png" class="prod-png" alt="Cheese processing">
                <div class="prod-meta">
                  <span class="p-title">Cheese &amp; Curd Vats</span>
                  <span class="p-spec">Fermentation Hygiene</span>
                </div>
              </div>
              <div class="prod-item p3" data-t="24.0">
                <img src="assets/images/foods/dessert.png" class="prod-png" alt="Dairy desserts">
                <div class="prod-meta">
                  <span class="p-title">Cooked Dairy &amp; Pack</span>
                  <span class="p-spec">Terminal Safety</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Right: Animated Plant Safety Shield & Nodes -->
          <div class="s01-visual-panel">
            <div class="plant-shield-network">
              <svg class="shield-vector" viewBox="0 0 400 400">
                <defs>
                  <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#0284c7" />
                    <stop offset="100%" stop-color="#38bdf8" />
                  </linearGradient>
                </defs>
                <circle cx="200" cy="200" r="160" class="shield-outer-orbit" />
                <circle cx="200" cy="200" r="120" class="shield-inner-orbit" />
                <path d="M 200 80 L 300 130 L 300 240 Q 200 330 200 330 Q 100 240 100 240 L 100 130 Z" class="shield-crest" fill="none" stroke="url(#shieldGrad)" stroke-width="4"/>
                <circle cx="200" cy="80" r="6" class="node-dot nd-top" />
                <circle cx="300" cy="180" r="6" class="node-dot nd-right" />
                <circle cx="100" cy="180" r="6" class="node-dot nd-left" />
                <circle cx="200" cy="330" r="6" class="node-dot nd-bottom" />
              </svg>
              <div class="shield-center-core">
                <span class="core-label">VERIFIED</span>
                <span class="core-val">SAFETY</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 02: Course Aim & Learning Syllabus
  renderSlide02() {
    return `
      <div class="explainer-scene scene-s02">
        <div class="s02-timeline-flow">
          <div class="s02-header-block">
            <span class="scene-kicker">SYLLABUS ARCHITECTURE</span>
            <h2 class="scene-headline">Five Core Competency Modules</h2>
          </div>
          <div class="s02-track">
            <div class="track-step ts-1" data-t="6.5">
              <span class="step-num">01</span>
              <div class="step-card">
                <span class="sc-tag">ORIGINS</span>
                <h4 class="sc-title">What is HACCP?</h4>
                <p class="sc-desc">From NASA space flights to modern global food legislation.</p>
              </div>
            </div>
            <div class="track-step ts-2" data-t="12.0">
              <span class="step-num">02</span>
              <div class="step-card">
                <span class="sc-tag">HAZARDS</span>
                <h4 class="sc-title">4 Safety Vectors</h4>
                <p class="sc-desc">Biological, chemical, physical, and allergen risk factors.</p>
              </div>
            </div>
            <div class="track-step ts-3" data-t="17.5">
              <span class="step-num">03</span>
              <div class="step-card">
                <span class="sc-tag">STANDARDS</span>
                <h4 class="sc-title">Codex &amp; Laws</h4>
                <p class="sc-desc">Statutory requirements under Regulation (EC) No 852/2004.</p>
              </div>
            </div>
            <div class="track-step ts-4" data-t="23.0">
              <span class="step-num">04</span>
              <div class="step-card">
                <span class="sc-tag">CONTROL</span>
                <h4 class="sc-title">The 7 Principles</h4>
                <p class="sc-desc">Systematic hazard analysis and validated critical control.</p>
              </div>
            </div>
            <div class="track-step ts-5" data-t="29.0">
              <span class="step-num">05</span>
              <div class="step-card">
                <span class="sc-tag">EXECUTION</span>
                <h4 class="sc-title">Dairy CCP Limits</h4>
                <p class="sc-desc">Filtration, pasteurisation, chilling, and metal detection.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 03: What is HACCP? (Reactive vs Preventive Split)
  renderSlide03() {
    return `
      <div class="explainer-scene scene-s03">
        <div class="s03-split-arena">
          <!-- Left: Traditional Reactive Testing -->
          <div class="arena-side side-reactive">
            <div class="arena-badge b-red">TRADITIONAL END-POINT TESTING // REACTION</div>
            <h3 class="arena-title">Testing Finished Batches</h3>
            <div class="reactive-conveyor">
              <div class="conveyor-line"></div>
              <div class="conveyor-product prod-defective">
                <img src="assets/images/foods/cheese.png" class="side-prod-img" alt="Batch">
                <span class="defect-cross">&#10005;</span>
              </div>
            </div>
            <p class="arena-desc">Catastrophic batch recall: contamination discovered only after production is finished.</p>
          </div>

          <!-- Divider -->
          <div class="arena-vs-divider">VS</div>

          <!-- Right: HACCP Preventive System -->
          <div class="arena-side side-preventive">
            <div class="arena-badge b-blue">HACCP METHODOLOGY // PREVENTION</div>
            <h3 class="arena-title">In-line Systematic Controls</h3>
            <div class="preventive-pipeline">
              <div class="pipeline-node pn1 active-node"><span>RECEIVE</span></div>
              <div class="pipeline-connector"></div>
              <div class="pipeline-node pn2 active-node"><span>FILTER</span></div>
              <div class="pipeline-connector"></div>
              <div class="pipeline-node pn3 active-node"><span>72°C KILL</span></div>
            </div>
            <p class="arena-desc">Identifies hazards and locks critical limits before contamination can occur.</p>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 04: NASA Space Mission Origins
  renderSlide04() {
    return `
      <div class="explainer-scene scene-s04">
        <div class="s04-space-layout">
          <div class="space-visual-canvas">
            <div class="rocket-orbit-wrapper">
              <svg class="orbit-path-svg" viewBox="0 0 500 300">
                <path d="M 50 250 Q 250 50 450 150" fill="none" stroke="rgba(56, 189, 248, 0.4)" stroke-width="2" stroke-dasharray="6 6" />
                <circle cx="50" cy="250" r="14" fill="#0284c7" />
                <circle cx="450" cy="150" r="28" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
              </svg>
              <div class="space-capsule-marker">
                <span class="capsule-id">APOLLO PROJECT</span>
                <span class="capsule-sub">NASA &times; PILLSBURY (1960s)</span>
              </div>
            </div>
          </div>
          <div class="space-intel-box">
            <span class="scene-kicker">HISTORICAL FOUNDATION</span>
            <h2 class="scene-headline">Engineered for Zero Failure</h2>
            <p class="scene-subhead">Astronauts in deep space could not risk foodborne illness. Testing samples was not enough—100% process assurance was born.</p>
            <div class="nasa-spec-pill">
              <span class="spec-label">Codex Alimentarius Adoption:</span>
              <span class="spec-highlight">Global Food Standard Standardized</span>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 05: The 4 Food Safety Hazards
  renderSlide05() {
    return `
      <div class="explainer-scene scene-s05">
        <div class="s05-hazards-grid">
          <div class="hazard-quad q-bio" data-t="5.0">
            <span class="quad-num">01</span>
            <span class="quad-cat">BIOLOGICAL</span>
            <h3 class="quad-title">Pathogenic Microbes</h3>
            <p class="quad-lead">Listeria monocytogenes, Salmonella, Escherichia coli.</p>
            <div class="hazard-vector-indicator bio-pulse"></div>
          </div>
          <div class="hazard-quad q-chem" data-t="16.0">
            <span class="quad-num">02</span>
            <span class="quad-cat">CHEMICAL</span>
            <h3 class="quad-title">Process &amp; CIP Residues</h3>
            <p class="quad-lead">Caustic detergents, sterilants, and veterinary residues.</p>
            <div class="hazard-vector-indicator chem-pulse"></div>
          </div>
          <div class="hazard-quad q-phys" data-t="27.0">
            <span class="quad-num">03</span>
            <span class="quad-cat">PHYSICAL</span>
            <h3 class="quad-title">Foreign Matter</h3>
            <p class="quad-lead">Glass shards, metal shavings, plastic fragments, straw.</p>
            <div class="hazard-vector-indicator phys-pulse"></div>
          </div>
          <div class="hazard-quad q-allergen" data-t="38.0">
            <span class="quad-num">04</span>
            <span class="quad-cat">ALLERGENIC</span>
            <h3 class="quad-title">Specific Proteins</h3>
            <p class="quad-lead">The 14 statutory allergens including nuts, gluten, and eggs.</p>
            <div class="hazard-vector-indicator allergen-pulse"></div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 06: Regulations & EC 852/2004 Framework
  renderSlide06() {
    return `
      <div class="explainer-scene scene-s06">
        <div class="s06-legal-layout">
          <div class="legal-card-main">
            <span class="scene-kicker">STATUTORY COMPLIANCE</span>
            <h2 class="legal-title">Regulation (EC) No 852/2004</h2>
            <p class="legal-lead">Mandates that every food and dairy business operator must put in place, implement and maintain a permanent procedure based on HACCP principles.</p>
            
            <div class="legal-pillars-row">
              <div class="lp-col">
                <span class="lp-label">LEGAL STATUS</span>
                <span class="lp-val">Mandatory by Law</span>
              </div>
              <div class="lp-col">
                <span class="lp-label">AUDIT BODY</span>
                <span class="lp-val">FSA / Local Authority</span>
              </div>
              <div class="lp-col">
                <span class="lp-label">CONSEQUENCE</span>
                <span class="lp-val c-red">Closure / Prosecution</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }
};
