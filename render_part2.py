import os
import math
from PIL import Image, ImageDraw
import slide_render_modules as srm
import filled_vector_assets as fva
import layout_utils

WIDTH, HEIGHT = 1920, 1080

def render_slide_07(t, dur):  # 7 HACCP Principles
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Codex Methodology", "The 7 Principles of HACCP", "Systematic international standard for biological, chemical and physical safety")
    
    principles = [
        ("1. Conduct Hazard Analysis", "Identify biological, chemical, allergen & physical risks", "#0284C7", 2.0),
        ("2. Determine CCPs", "Apply Codex Decision Tree to establish control points", "#0369A1", 10.0),
        ("3. Establish Critical Limits", "Define exact safety boundaries (e.g., >72°C / 15s)", "#059669", 20.0),
        ("4. Establish Monitoring", "Real-time observation & logging of all CCP parameters", "#10B981", 30.0),
        ("5. Corrective Actions", "Pre-planned immediate action when a critical limit is breached", "#D97706", 40.0),
        ("6. Establish Verification", "Audits, calibration & micro testing to verify system works", "#4F46E5", 50.0),
        ("7. Documented Records", "Full traceability, calibration logs & due-diligence records", "#7C3AED", 60.0),
    ]
    
    y_start = 300
    for i, (title, desc, col, delay) in enumerate(principles):
        if t >= delay:
            y = y_start + i * 85
            draw.rounded_rectangle([(140, y), (1780, y + 74)], radius=12, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(140, y), (155, y + 74)], fill=col)
            draw.text((180, y + 12), title, fill=col, font=srm.get_font(22, bold=True))
            draw.text((180, y + 42), desc, fill="#1E293B", font=srm.get_font(18))
            draw.rounded_rectangle([(1660, y + 15), (1750, y + 59)], radius=8, fill=col)
            draw.text((1678, y + 24), f"P0{i+1}", fill="#FFFFFF", font=srm.get_font(18, bold=True))
            
    srm.draw_footer(draw, 7)
    return img

def render_slide_08(t, dur):  # Determine CCPs
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Methodology & Flow", "Determining Critical Control Points", "A CCP is a step essential to prevent, eliminate or reduce a hazard to safe levels")
    
    steps = [
        ("Step 1: Process Flow Diagram", "Map every processing stage from raw milk intake to packing", "#0284C7", 2.0),
        ("Step 2: Hazard Analysis", "Assess severity and likelihood of hazards at each step", "#0369A1", 14.0),
        ("Step 3: Codex Decision Tree", "Apply the 4 standard questions to identify genuine CCPs", "#059669", 27.0),
        ("Step 4: Establish Critical Limits", "Define measurable pass/fail parameters (Time, Temp, Mesh Size)", "#D97706", 39.0),
    ]
    
    card_w = 380
    for i, (title, desc, col, delay) in enumerate(steps):
        if t >= delay:
            x = 140 + i * (card_w + 33)
            y = 320
            draw.rounded_rectangle([(x, y), (x + card_w, y + 420)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + card_w, y + 14)], fill=col)
            draw.rounded_rectangle([(x + 25, y + 40), (x + 95, y + 80)], radius=8, fill=col)
            draw.text((x + 38, y + 48), f"0{i+1}", fill="#FFFFFF", font=srm.get_font(22, bold=True))
            draw.text((x + 25, y + 120), title, fill=col, font=srm.get_font(22, bold=True))
            desc_y = y + 200
            for l in desc.split("\n"):
                draw.text((x + 25, desc_y), l, fill="#1E293B", font=srm.get_font(20))
                desc_y += 32
                
    if t >= 45.0:
        layout_utils.draw_centered_box_text(draw, (140, 780, 1780, 880), "NOT EVERY STEP IS A CCP: GENERAL HYGIENE IS CONTROLLED BY PRPs", srm.get_font(26, bold=True), "#FFFFFF", "#0284C7", 14)
        
    srm.draw_footer(draw, 8)
    return img

def render_slide_09(t, dur):  # Your Work Area CCPs
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Interactive Reflection", "Your Work Area CCPs", "Do you know the exact Critical Control Points in your daily operational area?")
    
    areas = [
        ("PASTEURISATION BAY", "CCP: Heat Treatment\n• Min >72°C for 15s\n• Automated divert valve\n• Continuous chart logger", fva.draw_filled_dairy_tank, "#0284C7", 2.0),
        ("CHILLING & STORAGE", "CCP: Rapid Temperature Pull-down\n• Chill to <8°C in 90 mins\n• Target cold store <4°C\n• Inhibits spore growth", fva.draw_filled_quality_shield, "#059669", 12.0),
        ("PACKAGING HALL", "CCP: Metal Detection\n• 100% finished pack test\n• Ferrous / Non-Ferrous / SS\n• Auto-reject bin fail-safe", fva.draw_filled_filter_gear, "#D97706", 22.0),
    ]
    
    card_w = 515
    for i, (title, desc, draw_func, col, delay) in enumerate(areas):
        if t >= delay:
            x = 140 + i * (card_w + 25)
            y = 310
            draw.rounded_rectangle([(x, y), (x + card_w, y + 430)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + card_w, y + 14)], fill=col)
            draw_func(draw, x + card_w // 2, y + 130, scale=0.75)
            draw.text((x + 25, y + 230), title, fill=col, font=srm.get_font(22, bold=True))
            desc_y = y + 275
            for l in desc.split("\n"):
                draw.text((x + 25, desc_y), l, fill="#1E293B", font=srm.get_font(20))
                desc_y += 32
                
    if t >= 28.0:
        layout_utils.draw_centered_box_text(draw, (140, 770, 1780, 870), "IF IN DOUBT: STOP THE LINE AND CONSULT YOUR SHIFT SUPERVISOR IMMEDIATELY", srm.get_font(24, bold=True), "#DC2626", "#FEE2E2", 14, border_w=2)
        
    srm.draw_footer(draw, 9)
    return img

def render_slide_10(t, dur):  # Importance of HACCP (8 Reasons)
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Business Value", "8 Reasons Why HACCP is Essential", "Safeguarding consumers, protecting brand equity, and fulfilling statutory requirements")
    
    reasons = [
        ("1. Identifies Hazard Risks", "Systematic risk mapping across milk intake, process & pack", 2.0),
        ("2. Prevents Foodborne Illness", "Eliminates pathogens like Listeria, Salmonella & E. coli", 8.0),
        ("3. Addresses Root Causes", "Fixes root causes rather than reacting to finished spoilage", 14.0),
        ("4. Protects Public Health", "Guarantees safe nutrition for millions of daily consumers", 20.0),
        ("5. Retailer & Customer Trust", "Meets strict BRCGS, retailer codes and consumer expectations", 26.0),
        ("6. Brand & Recall Protection", "Avoids devastating product recalls, fines and reputational loss", 32.0),
        ("7. Demonstrates Compliance", "Proves due diligence and compliance during EHO audits", 38.0),
        ("8. Mandatory Licence to Trade", "Statutory requirement: plant cannot legally operate without it", 44.0),
    ]
    
    for i, (title, desc, delay) in enumerate(reasons):
        if t >= delay:
            col_idx = i % 2
            row_idx = i // 2
            x = 140 + col_idx * 830
            y = 300 + row_idx * 135
            draw.rounded_rectangle([(x, y), (x + 800, y + 115)], radius=12, fill="#FFFFFF", outline="#0284C7", width=2)
            draw.rectangle([(x, y), (x + 14, y + 115)], fill="#0284C7")
            draw.text((x + 35, y + 20), title, fill="#0369A1", font=srm.get_font(22, bold=True))
            draw.text((x + 35, y + 58), desc, fill="#1E293B", font=srm.get_font(19))
            
    srm.draw_footer(draw, 10)
    return img

def render_slide_11(t, dur):  # CCP Examples: Filtration & HTST
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Dairy Operations", "Production CCPs: Filtration & Heat Treatment", "Physical debris elimination and validated thermal kill steps")
    
    # Left Card: CCP 1
    if t >= 2.0:
        draw.rounded_rectangle([(140, 300), (920, 720)], radius=18, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(140, 300), (920, 316)], fill="#0284C7")
        fva.draw_filled_filter_gear(draw, 240, 420, scale=0.9)
        draw.text((340, 360), "CCP 1 : RAW MILK FILTRATION", fill="#0369A1", font=srm.get_font(24, bold=True))
        draw.text((340, 400), "Critical Limit: 1000 µm In-Line Filter", fill="#0F172A", font=srm.get_font(20, bold=True))
        draw.text((180, 520), "• Removes physical debris, straw & sediment\n• Inspected before & after every tanker discharge\n• Filter integrity log signed by intake operator", fill="#334155", font=srm.get_font(21))

    # Right Card: CCP 2
    if t >= 18.0:
        draw.rounded_rectangle([(1000, 300), (1780, 720)], radius=18, fill="#FFFFFF", outline="#EF4444", width=2)
        draw.rectangle([(1000, 300), (1780, 316)], fill="#EF4444")
        fva.draw_filled_dairy_tank(draw, 1100, 420, scale=0.8)
        draw.text((1200, 360), "CCP 2 : HTST PASTEURISATION", fill="#DC2626", font=srm.get_font(24, bold=True))
        draw.text((1200, 400), "Critical Limit: > 72.0°C for 15 Seconds", fill="#0F172A", font=srm.get_font(20, bold=True))
        draw.text((1040, 520), "• Thermal kill step for Listeria, Salmonella & E. coli\n• Automated flow divert valve diverts milk if < 72°C\n• Continuous chart recording and hourly verification", fill="#334155", font=srm.get_font(21))
        
    if t >= 48.0:
        layout_utils.draw_centered_box_text(draw, (140, 760, 1780, 870), "THERMAL COOK CCP: DESSERT BASES & CURDS COOKED AT >86°C / >88°C FOR 20 MINS", srm.get_font(24, bold=True), "#FFFFFF", "#059669", 14)
        
    srm.draw_footer(draw, 11)
    return img

def render_slide_12(t, dur):  # CCP Examples: Chilling & Metal Detection
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Dairy Operations", "Production CCPs: Chilling & Metal Detection", "Spore growth prevention and final finished packaging physical inspection")
    
    # Left: Rapid Chilling
    if t >= 2.0:
        draw.rounded_rectangle([(140, 300), (920, 730)], radius=18, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(140, 300), (920, 316)], fill="#0284C7")
        fva.draw_filled_quality_shield(draw, 240, 420, scale=0.8)
        draw.text((340, 360), "CCP 3 : RAPID CHILLING", fill="#0369A1", font=srm.get_font(24, bold=True))
        draw.text((340, 400), "Critical Limit: < 8.0°C within 90 mins", fill="#0F172A", font=srm.get_font(20, bold=True))
        draw.text((180, 510), "• Prevents germination of Bacillus cereus spores\n• Finished milk transferred to silos at < 4.0°C\n• Logged automatically via SCADA temperature sensors", fill="#334155", font=srm.get_font(21))

    # Right: Metal Detection
    if t >= 26.0:
        draw.rounded_rectangle([(1000, 300), (1780, 730)], radius=18, fill="#FFFFFF", outline="#D97706", width=2)
        draw.rectangle([(1000, 300), (1780, 316)], fill="#D97706")
        fva.draw_filled_filter_gear(draw, 1100, 420, scale=0.8)
        draw.text((1200, 360), "CCP 4 : METAL DETECTION", fill="#D97706", font=srm.get_font(24, bold=True))
        draw.text((1200, 400), "Critical Limit: 100% Pack Detection", fill="#0F172A", font=srm.get_font(20, bold=True))
        draw.text((1040, 510), "• In-line inspection for cheese, yogurt & dessert packs\n• Calibrated with Ferrous, Non-Ferrous & SS 316 wands\n• Auto-reject arm diverts contaminated packs to locked bin", fill="#334155", font=srm.get_font(21))

    if t >= 36.0:
        layout_utils.draw_centered_box_text(draw, (140, 770, 1780, 870), "TEST METAL DETECTOR WITH CERTIFIED TEST PIECES AT START, HOURLY & SHIFT END", srm.get_font(24, bold=True), "#FFFFFF", "#0284C7", 14)
        
    srm.draw_footer(draw, 12)
    return img

def render_slide_13(t, dur):  # Monitoring & Deviation Management
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Monitoring & GMP", "Monitoring Procedures & Deviation Management", "Live recording, automated divert triggers and risk-based environmental swabbing")
    
    cards = [
        ("1. Real-Time Logging", "Observations must match live physical gauges.\nNo delayed back-filling of paperwork.", "#0284C7", 2.0),
        ("2. Automated Flow Divert", "If pasteuriser temp < 72°C, automated divert valve\nimmediately returns milk to balance tank.", "#EF4444", 14.0),
        ("3. Incident & NCR Report", "Raise a Non-Conformance Report immediately\nwhenever a critical limit is breached.", "#D97706", 28.0),
        ("4. Environmental Swabs", "Daily swabs of drains, floors & equipment\nto verify zero Listeria monocytogenes harborage.", "#059669", 36.0),
    ]
    
    for i, (title, desc, col, delay) in enumerate(cards):
        if t >= delay:
            col_idx = i % 2
            row_idx = i // 2
            x = 140 + col_idx * 830
            y = 300 + row_idx * 270
            draw.rounded_rectangle([(x, y), (x + 800, y + 240)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + 14, y + 240)], fill=col)
            draw.text((x + 40, y + 35), title, fill=col, font=srm.get_font(24, bold=True))
            desc_y = y + 90
            for l in desc.split("\n"):
                draw.text((x + 40, desc_y), l, fill="#1E293B", font=srm.get_font(22))
                desc_y += 38
                
    srm.draw_footer(draw, 13)
    return img

RENDERERS_PART2 = {
    7: render_slide_07,
    8: render_slide_08,
    9: render_slide_09,
    10: render_slide_10,
    11: render_slide_11,
    12: render_slide_12,
    13: render_slide_13
}
