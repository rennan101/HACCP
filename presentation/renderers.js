// Unified Scene Router for HACCP Masterclass Motion Engines
window.HACCP_RENDERERS = {
  renderContent(slide) {
    const s = slide.slide_num;
    const F = window.HACCP_FOUNDATIONS;
    const P = window.HACCP_PRINCIPLES;
    const H = window.HACCP_HAZARDS;
    const O = window.HACCP_OPERATIONS;

    // Block 1: Foundations (Slides 01 to 06)
    if (s === 1 && F) return F.renderSlide01();
    if (s === 2 && F) return F.renderSlide02();
    if (s === 3 && F) return F.renderSlide03();
    if (s === 4 && F) return F.renderSlide04();
    if (s === 5 && F) return F.renderSlide05();
    if (s === 6 && F) return F.renderSlide06();

    // Block 2: Principles & CCPs (Slides 07 to 13)
    if (s === 7 && P) return P.renderSlide07();
    if (s === 8 && P) return P.renderSlide08();
    if (s === 9 && P) return P.renderSlide09();
    if (s === 10 && P) return P.renderSlide10();
    if (s === 11 && P) return P.renderSlide11();
    if (s === 12 && P) return P.renderSlide12();
    if (s === 13 && P) return P.renderSlide13();

    // Block 3: Hazards & Allergens (Slides 14 to 20)
    if (s === 14 && H) return H.renderSlide14();
    if (s === 15 && H) return H.renderSlide15();
    if (s === 16 && H) return H.renderSlide16();
    if (s === 17 && H) return H.renderSlide17();
    if (s === 18 && H) return H.renderSlide18();
    if (s === 19 && H) return H.renderSlide19();
    if (s === 20 && H) return H.renderSlide20();

    // Block 4: Operations, PRPs & Closing (Slides 21 to 26)
    if (s === 21 && O) return O.renderSlide21();
    if (s === 22 && O) return O.renderSlide22();
    if (s === 23 && O) return O.renderSlide23();
    if (s === 24 && O) return O.renderSlide24();
    if (s === 25 && O) return O.renderSlide25();
    if (s === 26 && O) return O.renderSlide26();

    return `<div class="explainer-fallback"><p>Slide ${s}</p></div>`;
  }
};
