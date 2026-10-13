// HTML Renderers for HACCP Level 2 Slide Layouts with Showtime Motion Enhancements
window.HACCP_RENDERERS = {
  renderCard(el, extraClass = "") {
    const colorClass = el.color ? `color-${el.color}` : "color-primary";
    const foodBadge = el.food_icon
      ? `<div class="food-badge-wrapper"><img src="${el.food_icon}" class="food-badge-icon" alt="Food example"></div>`
      : "";
    return `
      <div class="sync-card ${colorClass} ${extraClass}" id="${el.id}" data-start-time="${el.start_time}" data-end-time="${el.end_time || 999}">
        <div class="sync-card-header-row">
          <div class="sync-card-tag">${el.tag || "Key Concept"}</div>
          ${foodBadge}
        </div>
        <div class="sync-card-heading">${el.heading}</div>
        <div class="sync-card-desc">${el.description || ""}</div>
      </div>
    `;
  },

  renderBanner(el) {
    return `
      <div class="sync-banner" id="${el.id}" data-start-time="${el.start_time}" data-end-time="${el.end_time || 999}">
        <div class="sync-banner-text">
          <h4>${el.heading}</h4>
          <p>${el.description}</p>
        </div>
      </div>
    `;
  },

  renderContent(slide) {
    const mode = slide.layout_mode || "split_photo";
    const sNum = slide.slide_num;
    const G = window.HACCP_GRAPHICS;

    // 1. Slide 11 Custom Pasteurization Thermal & Flow Profile
    if (sNum === 11 && G) {
      const cards = slide.elements.map(el => this.renderCard(el)).join("");
      return `
        <div class="layout-split-photo layout-pasteurization-pro">
          <div class="cards-container">${cards}</div>
          <div class="visual-container">${G.renderPasteurizationWidget()}</div>
        </div>
      `;
    }

    // 2. Slide 08 Custom Codex Decision Tree
    if (sNum === 8 && G) {
      const cards = slide.elements.map(el => this.renderCard(el)).join("");
      return `
        <div class="layout-decision-tree-pro">
          <div class="cards-container grid-2col">${cards}</div>
          <div class="tree-widget-area">${G.renderCCPDecisionTree()}</div>
        </div>
      `;
    }

    // 3. Slide 25 Custom Continuous PDCA Wheel
    if (sNum === 25 && G) {
      const cards = slide.elements.map(el => this.renderCard(el)).join("");
      return `
        <div class="layout-pdca-pro">
          <div class="pdca-quadrants-grid">${cards}</div>
          <div class="pdca-wheel-side">${G.renderPDCALoop()}</div>
        </div>
      `;
    }

    // 4. Slide 07 Custom Hazard & Risk Matrix
    if (sNum === 7 && G) {
      const cards = slide.elements.map(el => this.renderCard(el)).join("");
      return `
        <div class="layout-risk-matrix-pro">
          <div class="cards-container grid-2col">${cards}</div>
          <div class="matrix-widget-area">${G.renderRiskMatrix()}</div>
        </div>
      `;
    }

    // 5. Standard Split Photo
    if (mode === "split_photo") {
      let cards = "";
      let banner = "";
      slide.elements.forEach(el => {
        if (el.type === "banner") banner += this.renderBanner(el);
        else cards += this.renderCard(el);
      });
      return `
        <div class="layout-split-photo">
          <div class="cards-container">${cards}${banner}</div>
          <div class="visual-container">
            <div class="hero-image-box">
              <img src="${slide.image_file}" alt="${slide.title}">
            </div>
          </div>
        </div>
      `;
    }

    // 6. Allergens 14 Grid (Slide 16)
    if (mode === "allergens_grid_7x2") {
      const cards = slide.elements.map(el => {
        const colorClass = el.color ? `color-${el.color}` : "color-primary";
        const iconHtml = el.food_icon
          ? `<div class="allergen-icon-bubble"><img src="${el.food_icon}" class="allergen-food-icon" alt="${el.heading}"></div>`
          : "";
        return `
          <div class="sync-card allergen-card ${colorClass}" id="${el.id}" data-start-time="${el.start_time}" data-end-time="${el.end_time || 999}">
            ${iconHtml}
            <div class="sync-card-tag">${el.tag || "Allergen"}</div>
            <div class="sync-card-heading">${el.heading}</div>
            <div class="sync-card-desc">${el.description || ""}</div>
          </div>
        `;
      }).join("");
      return `<div class="layout-allergens-grid">${cards}</div>`;
    }

    const simpleGridModes = {
      "full_width_grid_2col": "layout-full-width-2col",
      "horizontal_timeline": "layout-horizontal-timeline",
      "horizontal_flow": "layout-horizontal-timeline",
      "full_width_grid_2x4": "layout-full-width-2x4",
      "full_width_grid_4col": "layout-full-width-4col",
      "pillar_architecture": "layout-pillar-architecture",
      "pdca_quadrants": "layout-pdca-quadrants"
    };

    if (simpleGridModes[mode]) {
      const cards = slide.elements.map(el => this.renderCard(el)).join("");
      return `<div class="${simpleGridModes[mode]}">${cards}</div>`;
    }

    if (mode === "comparison_split") {
      const oldCard = slide.elements.find(el => el.id.includes("old"));
      const newCard = slide.elements.find(el => el.id.includes("new"));
      const banner = slide.elements.find(el => el.type === "banner");
      return `
        <div class="layout-comparison">
          <div class="comparison-grid">
            ${oldCard ? this.renderCard(oldCard, "comparison-card") : ""}
            ${newCard ? this.renderCard(newCard, "comparison-card") : ""}
          </div>
          ${banner ? this.renderBanner(banner) : ""}
        </div>
      `;
    }

    if (mode === "full_width_alert_split") {
      const cards = slide.elements.filter(el => el.type !== "warning_box").map(el => this.renderCard(el)).join("");
      const alert = slide.elements.find(el => el.type === "warning_box");
      return `
        <div class="layout-comparison">
          <div class="comparison-grid">${cards}</div>
          ${alert ? this.renderCard(alert, "comparison-card color-danger") : ""}
        </div>
      `;
    }

    if (mode === "lab_table") {
      const rows = slide.elements.map(el => {
        const iconHtml = el.food_icon
          ? `<img src="${el.food_icon}" style="width:28px;height:28px;vertical-align:middle;margin-right:10px;" alt="Food">`
          : "";
        return `
          <div class="lab-table-row" id="${el.id}" data-start-time="${el.start_time}" data-end-time="${el.end_time || 999}">
            <div style="font-weight:700; color:var(--text-main); display:flex; align-items:center;">
              ${iconHtml}<span>${el.param}</span>
            </div>
            <div class="target-badge">${el.target}</div>
            <div class="action-badge">${el.action}</div>
            <div class="reject-badge">${el.reject}</div>
          </div>
        `;
      }).join("");
      return `
        <div class="layout-lab-table">
          <div class="lab-table-header">
            <div>TEST PARAMETER</div>
            <div>TARGET SPECIFICATION</div>
            <div>ACTION LIMIT</div>
            <div>REJECT THRESHOLD</div>
          </div>
          ${rows}
        </div>
      `;
    }

    if (mode === "assessment_checklist") {
      const refCard = slide.elements.find(el => el.id === "s26_ref");
      const quizCard = slide.elements.find(el => el.id === "s26_quiz");
      const banner = slide.elements.find(el => el.type === "banner");
      return `
        <div class="layout-assessment">
          <div class="assessment-split">
            ${refCard ? this.renderCard(refCard) : ""}
            ${quizCard ? this.renderCard(quizCard) : ""}
          </div>
          ${banner ? this.renderBanner(banner) : ""}
        </div>
      `;
    }

    return "";
  }
};
