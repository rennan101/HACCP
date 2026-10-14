// Motion Graphics Engine - Block 3: Hazard Spotlight & Allergen Controls (Slides 14 to 20)
// Zero emojis: Pure industrial vectors, high-fidelity real PNG assets, timeline-synced kinetic animation
window.HACCP_HAZARDS = {
  // Slide 14: Hazard Spotlight: Chemical Safety & CIP
  renderSlide14() {
    return `
      <div class="explainer-scene scene-s14">
        <div class="s14-cip-layout">
          <div class="cip-stages-bar">
            <div class="cip-step"><span class="cs-num">01</span><span class="cs-name">Pre-Rinse (Ambient)</span></div>
            <div class="cip-step"><span class="cs-num">02</span><span class="cs-name">Caustic Wash (1.5-2.0%)</span></div>
            <div class="cip-step"><span class="cs-num">03</span><span class="cs-name">Acid Descale (0.8-1.2%)</span></div>
            <div class="cip-step active-cip"><span class="cs-num">04</span><span class="cs-name">Final Water Flush &amp; pH</span></div>
          </div>
          <div class="cip-intel-grid">
            <div class="cip-metric-box">
              <span class="metric-title">FINAL FLUSH SPECIFICATION</span>
              <span class="metric-huge">pH 6.8 - 7.2</span>
              <span class="metric-status">ZERO CHEMICAL CARRYOVER</span>
            </div>
            <div class="cip-rule-box">
              <h3 class="rule-title">Chemical Segregation &amp; Dosing Safety</h3>
              <p class="rule-p">All cleaning chemicals stored in bunded chemical rooms. Automated dosing pumps prevent manual overdosing into product zones.</p>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 15: Hazard Spotlight: Physical Safety
  renderSlide15() {
    return `
      <div class="explainer-scene scene-s15">
        <div class="s15-physical-grid">
          <div class="xray-scanner-view">
            <div class="xray-screen-frame">
              <span class="xray-status">SCANNER SPECTRUM // ACTIVE HIGH SENSITIVITY</span>
              <div class="xray-visual-beam">
                <div class="scanned-pack">
                  <img src="assets/images/foods/cheese.png" class="xray-pack-img" alt="Scanned cheese">
                  <span class="target-reticle"></span>
                </div>
              </div>
            </div>
          </div>
          <div class="physical-policies">
            <span class="scene-kicker">FOREIGN BODY PREVENTION</span>
            <h2 class="scene-headline">Factory Physical Controls</h2>
            <div class="policy-list">
              <div class="pol-item"><span class="pol-tag">GLASS</span><span>Strict glass and brittle plastic register with audit frequency</span></div>
              <div class="pol-item"><span class="pol-tag">BLADES</span><span>Zero snap-off blades permitted on site (enclosed safety cutters only)</span></div>
              <div class="pol-item"><span class="pol-tag">JEWELLERY</span><span>Plain wedding band only; zero stones, watches, or piercings allowed</span></div>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 16: The 14 Major Food Allergens (Orbital Real PNG Grid)
  renderSlide16() {
    const allergens = [
      { name: "Gluten / Cereals", img: "assets/images/foods/gluten.png" },
      { name: "Crustaceans", img: "assets/images/foods/crustaceans.png" },
      { name: "Eggs", img: "assets/images/foods/eggs.png" },
      { name: "Fish", img: "assets/images/foods/fish.png" },
      { name: "Peanuts", img: "assets/images/foods/peanuts.png" },
      { name: "Soybeans", img: "assets/images/foods/soya.png" },
      { name: "Milk / Dairy", img: "assets/images/foods/milk.png" },
      { name: "Tree Nuts", img: "assets/images/foods/treenuts.png" },
      { name: "Celery", img: "assets/images/foods/celery.png" },
      { name: "Mustard", img: "assets/images/foods/mustard.png" },
      { name: "Sesame Seeds", img: "assets/images/foods/sesame.png" },
      { name: "Sulphur Dioxide", img: "assets/images/foods/sulphites.png" },
      { name: "Lupin", img: "assets/images/foods/lupin.png" },
      { name: "Molluscs", img: "assets/images/foods/molluscs.png" }
    ];
    const cards = allergens.map((a, i) => `
      <div class="allergen-grid-tile" data-idx="${i}">
        <img src="${a.img}" class="agt-img" alt="${a.name}">
        <span class="agt-name">${a.name}</span>
      </div>
    `).join("");

    return `
      <div class="explainer-scene scene-s16">
        <div class="s16-allergens-showcase">
          <div class="s16-header-row">
            <span class="scene-kicker">ANNEX II // STATUTORY LIST</span>
            <h2 class="scene-headline">The 14 Mandatory UK &amp; EU Allergens</h2>
          </div>
          <div class="allergens-matrix-14">${cards}</div>
        </div>
      </div>
    `;
  },

  // Slide 17: Allergens on Our Dairy Site
  renderSlide17() {
    return `
      <div class="explainer-scene scene-s17">
        <div class="s17-site-allergens">
          <div class="site-profile-card">
            <span class="scene-kicker">PRIMARY SITE ALLERGEN</span>
            <h2 class="site-title">Milk &amp; Dairy Proteins</h2>
            <p class="site-desc">Milk is our core processing matrix. Cross-contact between lactose-free lines and standard dairy lines must be validated through ELISA testing.</p>
          </div>
          <div class="site-controls-card">
            <span class="scene-kicker">SECONDARY ALLERGEN INTAKE</span>
            <h3 class="site-sub">Gluten &amp; Inclusions</h3>
            <p class="site-desc">Used strictly in dedicated dessert cooking bays. Dedicated colour-coded scoops and sealed ingredient bins required.</p>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 18: Strict Nut-Free Site Facility Policy
  renderSlide18() {
    return `
      <div class="explainer-scene scene-s18">
        <div class="s18-policy-banner">
          <div class="nut-free-shield">
            <span class="nf-label">STRICT POLICY // 100% NUT-FREE FACILITY</span>
            <h2 class="nf-title">Zero Peanuts or Tree Nuts Permitted on Site</h2>
            <p class="nf-text">Applies to all production bays, warehouses, packaging halls, staff canteen meals, and personal locker storage.</p>
            <div class="nf-rule-chips">
              <span class="chip">Zero Peanuts</span>
              <span class="chip">Zero Almonds / Walnuts</span>
              <span class="chip">Zero Nut Oils in Personal Care</span>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 19: Biological Safety & Dairy Microbial KPIs
  renderSlide19() {
    return `
      <div class="explainer-scene scene-s19">
        <div class="s19-hud-microbial">
          <div class="hud-header">
            <span class="scene-kicker">LABORATORY RELEASE SPECIFICATION</span>
            <h2 class="scene-headline">Microbial Target Standards</h2>
          </div>
          <div class="hud-metrics-grid">
            <div class="hm-tile">
              <span class="hm-pathogen">Listeria monocytogenes</span>
              <span class="hm-target c-green">NOT DETECTED in 25g</span>
              <span class="hm-action">Immediate quarantine if present</span>
            </div>
            <div class="hm-tile">
              <span class="hm-pathogen">Salmonella spp.</span>
              <span class="hm-target c-green">ABSENT in 25g</span>
              <span class="hm-action">Batch destruction protocol</span>
            </div>
            <div class="hm-tile">
              <span class="hm-pathogen">Enterobacteriaceae</span>
              <span class="hm-target c-amber">&lt; 10 CFU/g</span>
              <span class="hm-action">Hygiene swab investigation</span>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Slide 20: Personal Hygiene & 20-Second Handwashing
  renderSlide20() {
    return `
      <div class="explainer-scene scene-s20">
        <div class="s20-hygiene-layout">
          <div class="s20-timer-wheel">
            <div class="timer-20s-circle">
              <span class="t-huge">20s</span>
              <span class="t-sub">MANDATORY WASH TIME</span>
            </div>
          </div>
          <div class="s20-steps-list">
            <span class="scene-kicker">WHO PROTOCOL</span>
            <h3 class="scene-headline">6-Step Technical Wash</h3>
            <div class="wash-steps">
              <div class="ws-item"><span class="ws-n">1</span><span>Palms together with soap &amp; warm water</span></div>
              <div class="ws-item"><span class="ws-n">2</span><span>Back of hands and interdigital webbing</span></div>
              <div class="ws-item"><span class="ws-n">3</span><span>Base of thumbs and rotational wrist rub</span></div>
              <div class="ws-item"><span class="ws-n">4</span><span>Rinse clean and dry with single-use paper</span></div>
            </div>
          </div>
        </div>
      </div>
    `;
  }
};
