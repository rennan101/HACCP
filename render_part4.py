import os
import math
from PIL import Image, ImageDraw
import slide_render_modules as srm
import filled_vector_assets as fva
import layout_utils

WIDTH, HEIGHT = 1920, 1080

def render_slide_20(t, dur):  # Personal Hygiene & Handwashing
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Personal Hygiene", "Personal Hygiene & 20-Second Handwashing", "The primary frontline defence protecting open dairy products from contamination")
    
    steps = [
        ("Step 1: Wet Hands & Apply Soap", "Warm water with approved antibacterial soap", "#0284C7", 2.0),
        ("Step 2: Scrub for 20 Seconds", "Wash palms, fingers, fingernails, thumbs & wrists", "#0369A1", 12.0),
        ("Step 3: Complete Rinse", "Rinse thoroughly with clean running warm water", "#059669", 20.0),
        ("Step 4: Dry & Sanitise", "Dry with single-use paper towels & apply alcohol gel", "#D97706", 30.0),
    ]
    
    card_w = 380
    for i, (title, desc, col, delay) in enumerate(steps):
        if t >= delay:
            x = 140 + i * (card_w + 33)
            y = 310
            draw.rounded_rectangle([(x, y), (x + card_w, y + 430)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + card_w, y + 14)], fill=col)
            draw.rounded_rectangle([(x + 25, y + 40), (x + 105, y + 85)], radius=8, fill=col)
            draw.text((x + 38, y + 50), f"0{i+1}", fill="#FFFFFF", font=srm.get_font(24, bold=True))
            draw.text((x + 25, y + 120), title, fill=col, font=srm.get_font(20, bold=True))
            desc_y = y + 190
            for l in desc.split("\n"):
                draw.text((x + 25, desc_y), l, fill="#1E293B", font=srm.get_font(20))
                desc_y += 32
                
    if t >= 36.0:
        layout_utils.draw_centered_box_text(draw, (140, 780, 1780, 880), "MANDATORY: WASH HANDS BEFORE PRODUCTION ENTRY, AFTER TOILETS, EATING OR TOUCHING WASTE", srm.get_font(23, bold=True), "#FFFFFF", "#0284C7", 14)
        
    srm.draw_footer(draw, 20)
    return img

def render_slide_21(t, dur):  # Factory Zoning & Pen Colour Coding
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Zoning & Access", "Factory Hygiene Zoning & Stationery Coding", "Strict barrier controls between raw intake, intermediate processing and packing halls")
    
    zones = [
        ("HIGH-RISK (ASEPTIC)", "GREEN PEN & STATIONERY\n• Open ready-to-eat dairy filling\n• Full dedicated captive footwear & PPE\n• Aseptic air filtration and overpressure", "#059669", 2.0),
        ("HIGH-CARE AREA", "RED PEN & STATIONERY\n• Pasteurised cheese curds & yogurt tanks\n• Footwear sanitising barrier and coats\n• Strict utensil and tool quarantine", "#DC2626", 14.0),
        ("LOW-RISK / INTAKE", "BLUE PEN & STATIONERY\n• Raw tanker intake deck & chemical store\n• Outer packaging storage & pallet bay\n• General site access corridor", "#0284C7", 24.0),
    ]
    
    card_w = 515
    for i, (title, desc, col, delay) in enumerate(zones):
        if t >= delay:
            x = 140 + i * (card_w + 25)
            y = 310
            draw.rounded_rectangle([(x, y), (x + card_w, y + 430)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + card_w, y + 14)], fill=col)
            draw.text((x + 25, y + 45), title, fill=col, font=srm.get_font(24, bold=True))
            desc_y = y + 110
            for l in desc.split("\n"):
                draw.text((x + 25, desc_y), l, fill="#1E293B", font=srm.get_font(21))
                desc_y += 34
                
    if t >= 34.0:
        layout_utils.draw_centered_box_text(draw, (140, 770, 1780, 870), "NEVER CROSS HYGIENE BARRIERS WITHOUT RE-WASHING HANDS AND CHANGING ZONE BOOTS", srm.get_font(24, bold=True), "#DC2626", "#FEE2E2", 14, border_w=2)
        
    srm.draw_footer(draw, 21)
    return img

def render_slide_22(t, dur):  # Prerequisite Programmes (7 PRPs)
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Foundational Hygiene", "Prerequisite Programmes (PRPs)", "The 7 structural pillars supporting the entire dairy HACCP food safety framework")
    
    prps = [
        ("1. Cleaning & CIP", "Validated automated wash cycles & titration logs", 2.0),
        ("2. Personal Hygiene", "PPE, handwashing, illness reporting & hairnets", 8.0),
        ("3. Pest Control", "Preventative bait stations, insect screens & audits", 15.0),
        ("4. Maintenance", "Planned preventative servicing & food-grade grease", 22.0),
        ("5. Supplier Approval", "BRCGS certified ingredients & raw milk testing", 29.0),
        ("6. Allergen Control", "Dedicated lines, color-coded scoops & clean-downs", 36.0),
        ("7. Staff Training", "Ongoing competence assessments & HACCP refreshers", 44.0),
    ]
    
    pillar_w = 215
    for i, (title, desc, delay) in enumerate(prps):
        if t >= delay:
            x = 140 + i * (pillar_w + 19)
            y = 310
            col = "#0284C7" if i % 2 == 0 else "#0369A1"
            draw.rounded_rectangle([(x, y), (x + pillar_w, y + 430)], radius=12, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + pillar_w, y + 14)], fill=col)
            draw.text((x + 15, y + 35), title, fill=col, font=srm.get_font(20, bold=True))
            desc_y = y + 100
            for l in desc.split("\n"):
                draw.text((x + 15, desc_y), l, fill="#1E293B", font=srm.get_font(18))
                desc_y += 30
                
    if t >= 48.0:
        layout_utils.draw_centered_box_text(draw, (140, 770, 1780, 870), "WITHOUT STRONG PRPs, CRITICAL CONTROL POINTS CANNOT FUNCTION RELIABLY", srm.get_font(26, bold=True), "#FFFFFF", "#0284C7", 14)
        
    srm.draw_footer(draw, 22)
    return img

def render_slide_23(t, dur):  # Food Safety Attitude & 4-Point Label
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Culture & Storage", "Cross-Contamination & 4-Point Labelling", "Segregation rules and the mandatory open ingredient container labelling system")
    
    # Left: Segregation Rules
    if t >= 2.0:
        draw.rounded_rectangle([(140, 300), (860, 720)], radius=18, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(140, 300), (860, 316)], fill="#0284C7")
        draw.text((180, 345), "STORAGE & SEGREGATION RULES", fill="#0369A1", font=srm.get_font(24, bold=True))
        draw.text((180, 410), "• Keep raw and pasteurised products strictly separated\n• Store all ingredients in sealed, dedicated containers\n• Never place ingredient containers directly on the floor\n• Use designated colour-coded scoops for each recipe\n• Wipe down external packaging before warehouse transfer", fill="#334155", font=srm.get_font(21))

    # Right: 4-Point Label Template Mockup
    if t >= 18.0:
        draw.rounded_rectangle([(920, 300), (1780, 720)], radius=18, fill="#FEFCE8", outline="#EAB308", width=2)
        draw.rectangle([(920, 300), (1780, 316)], fill="#EAB308")
        draw.text((960, 345), "MANDATORY 4-POINT CONTAINER LABEL", fill="#854D0E", font=srm.get_font(24, bold=True))
        
        fields = [
            ("1. INGREDIENT NAME & BATCH :", "Organic Strawberry Puree (Batch #ST-9042)"),
            ("2. DATE OPENED / THAWED :", "29 September 2026 - 06:30 AM"),
            ("3. SECONDARY USE-BY DATE :", "02 October 2026 - 06:30 AM (72h Max)"),
            ("4. OPERATOR SIGNATURE / ID :", "John Smith (Op ID #8841)"),
        ]
        f_y = 410
        for f_title, f_val in fields:
            draw.text((960, f_y), f_title, fill="#0F172A", font=srm.get_font(20, bold=True))
            draw.text((960, f_y + 28), f_val, fill="#0369A1", font=srm.get_font(19))
            f_y += 65

    if t >= 35.0:
        layout_utils.draw_centered_box_text(draw, (140, 760, 1780, 870), "UNLABELLED INGREDIENTS ARE AN IMMEDIATE FOOD SAFETY RISK: REPORT TO QA AT ONCE", srm.get_font(24, bold=True), "#DC2626", "#FEE2E2", 14, border_w=2)

    srm.draw_footer(draw, 23)
    return img

def render_slide_24(t, dur):  # Corrective Actions & PDCA Cycle
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Continuous Improvement", "Corrective Actions & The PDCA Quality Cycle", "Regaining control, investigating root causes, and standardising permanent fixes")
    
    stages = [
        ("1. PLAN", "• Define hazard analysis\n• Establish critical limits\n• Prepare SOPs and CICs", "#0284C7", 2.0),
        ("2. DO", "• Execute HACCP procedures\n• Monitor CCPs real-time\n• Log data accurately", "#059669", 14.0),
        ("3. CHECK", "• Audit shift logs & CCPs\n• Calibrate thermometers\n• Review lab micro reports", "#D97706", 26.0),
        ("4. ACT", "• Investigate deviations\n• Update HACCP plan\n• Train staff on solutions", "#7C3AED", 38.0),
    ]
    
    card_w = 380
    for i, (title, desc, col, delay) in enumerate(stages):
        if t >= delay:
            x = 140 + i * (card_w + 33)
            y = 310
            draw.rounded_rectangle([(x, y), (x + card_w, y + 430)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + card_w, y + 14)], fill=col)
            draw.text((x + 25, y + 40), title, fill=col, font=srm.get_font(26, bold=True))
            desc_y = y + 110
            for l in desc.split("\n"):
                draw.text((x + 25, desc_y), l, fill="#1E293B", font=srm.get_font(21))
                desc_y += 35
                
    if t >= 46.0:
        layout_utils.draw_centered_box_text(draw, (140, 770, 1780, 870), "CORRECTIVE ACTION EXAMPLE: PASTEURISER DIVERT ACTIVATION -> QUARANTINE LOT -> ADJUST STEAM", srm.get_font(23, bold=True), "#FFFFFF", "#0284C7", 14)

    srm.draw_footer(draw, 24)
    return img

def render_slide_25(t, dur):  # HACCP Team & Legal Accountability
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Shared Accountability", "The HACCP Team & Individual Legal Liability", "Multidisciplinary ownership, quarantine protocols and personal statutory responsibility")
    
    # Left: Multidisciplinary Team & ON-HOLD
    if t >= 2.0:
        draw.rounded_rectangle([(140, 300), (920, 720)], radius=18, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(140, 300), (920, 316)], fill="#0284C7")
        draw.text((180, 345), "MULTIDISCIPLINARY HACCP TEAM", fill="#0369A1", font=srm.get_font(24, bold=True))
        draw.text((180, 400), "• Operations, Engineering, QA, Hygiene & Warehousing\n• Reviews HACCP plan annually or on recipe change\n• Validates all critical limits and monitoring routines", fill="#334155", font=srm.get_font(21))
        
        # ON-HOLD Tag Mockup
        draw.rounded_rectangle([(180, 520), (880, 680)], radius=12, fill="#FEF2F2", outline="#EF4444", width=2)
        draw.text((210, 545), "ON-HOLD QUARANTINE PROCEDURE", fill="#DC2626", font=srm.get_font(22, bold=True))
        draw.text((210, 585), "• Immediately attach physical Yellow/Red ON-HOLD tag\n• Lock batch electronically in ERP / Warehouse system\n• Only designated Quality Manager can release lot", fill="#7F1D1D", font=srm.get_font(19))

    # Right: Personal & Legal Liability
    if t >= 22.0:
        draw.rounded_rectangle([(1000, 300), (1780, 720)], radius=18, fill="#FFFFFF", outline="#D97706", width=2)
        draw.rectangle([(1000, 300), (1780, 316)], fill="#D97706")
        draw.text((1040, 345), "PERSONAL LEGAL ACCOUNTABILITY", fill="#B45309", font=srm.get_font(24, bold=True))
        draw.text((1040, 400), "• UK Regulation (EC) 852/2004 & Food Safety Act 1990\n• Falsifying records or concealing breaches is a crime\n• Individuals can face personal prosecution & fines\n• Food safety is EVERYONE'S personal daily responsibility\n• If you see something wrong: speak up and act immediately", fill="#334155", font=srm.get_font(21))

    if t >= 38.0:
        layout_utils.draw_centered_box_text(draw, (140, 760, 1780, 870), "YOU ARE PERSONALLY EMPOWERED TO STOP ANY UNSAFE PROCESS OR LINE OPERATION", srm.get_font(25, bold=True), "#FFFFFF", "#059669", 14)

    srm.draw_footer(draw, 25)
    return img

def render_slide_26(t, dur):  # References & Knowledge Assessment
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Assessment & Close", "Course References & 10-Question Knowledge Assessment", "Official statutory guidance links and final certification walkthrough")
    
    # Left: Official References
    if t >= 2.0:
        draw.rounded_rectangle([(140, 300), (800, 700)], radius=18, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(140, 300), (800, 316)], fill="#0284C7")
        draw.text((180, 345), "OFFICIAL STATUTORY REFERENCES", fill="#0369A1", font=srm.get_font(24, bold=True))
        draw.text((180, 410), "1. Food Standards Agency (FSA): food.gov.uk\n2. Codex Alimentarius: General Principles of Food Hygiene\n3. UK Statutory Instrument No. 14 / Regulation (EC) 852/2004\n4. Chartered Institute of Environmental Health (CIEH)\n5. Dairy UK Industry Code of Practice", fill="#334155", font=srm.get_font(20))

    # Right: 10-Question Assessment Overview
    if t >= 16.0:
        draw.rounded_rectangle([(860, 300), (1780, 700)], radius=18, fill="#FFFFFF", outline="#059669", width=2)
        draw.rectangle([(860, 300), (1780, 316)], fill="#059669")
        draw.text((900, 345), "10-QUESTION ASSESSMENT CHECKLIST", fill="#059669", font=srm.get_font(24, bold=True))
        draw.text((900, 410), "Q1: What does HACCP stand for? (Hazard Analysis Critical Control Point)\nQ2: What is the purpose of HACCP? (Prevent food safety hazards)\nQ3: Name the 4 main hazards (Bio, Chem, Phys, Allergen)\nQ4: HTST Pasteurisation limit? (>72°C for 15s)\nQ5: Chilling critical limit? (<8°C within 90 min, target <4°C)\nQ6-Q10: Metal detection, handwashing, allergens, ON-HOLD & reporting", fill="#334155", font=srm.get_font(19))

    if t >= 52.0:
        layout_utils.draw_centered_box_text(draw, (140, 730, 1780, 850), "CONGRATULATIONS ON COMPLETING HACCP LEVEL 2 FOOD & DAIRY EXCELLENCE!", srm.get_font(26, bold=True), "#FFFFFF", "#0284C7", 14)

    srm.draw_footer(draw, 26)
    return img

RENDERERS_PART4 = {
    20: render_slide_20,
    21: render_slide_21,
    22: render_slide_22,
    23: render_slide_23,
    24: render_slide_24,
    25: render_slide_25,
    26: render_slide_26
}
