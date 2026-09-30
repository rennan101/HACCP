import os
import math
from PIL import Image, ImageDraw
import slide_render_modules as srm
import filled_vector_assets as fva
import layout_utils

WIDTH, HEIGHT = 1920, 1080

def render_slide_14(t, dur):  # Chemical Safety
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Chemical Controls", "Hazard Spotlight: Chemical Safety", "Strict CIP regimes, Cleaning Instruction Cards (CICs) and equipment standards")
    
    # Left Card: CIP & Approved Chemicals
    if t >= 2.0:
        draw.rounded_rectangle([(140, 300), (920, 720)], radius=18, fill="#FFFFFF", outline="#F59E0B", width=2)
        draw.rectangle([(140, 300), (920, 316)], fill="#F59E0B")
        fva.draw_filled_chemical_bottle(draw, 240, 420, scale=0.85)
        draw.text((340, 360), "CIP & APPROVED CHEMICALS", fill="#B45309", font=srm.get_font(24, bold=True))
        draw.text((340, 400), "Follow Cleaning Instruction Cards (CICs)", fill="#0F172A", font=srm.get_font(20, bold=True))
        draw.text((180, 520), "• Use only company-approved chemicals & suppliers\n• Verify chemical concentration with titration test kits\n• Maintain water temperature and minimum contact time\n• Full potable water final rinse to eliminate residue", fill="#334155", font=srm.get_font(21))

    # Right Card: Prohibited Equipment
    if t >= 20.0:
        draw.rounded_rectangle([(1000, 300), (1780, 720)], radius=18, fill="#FEF2F2", outline="#EF4444", width=2)
        draw.rectangle([(1000, 300), (1780, 316)], fill="#EF4444")
        draw.text((1040, 360), "PROHIBITED CLEANING TOOLS", fill="#DC2626", font=srm.get_font(24, bold=True))
        draw.text((1040, 400), "Zero Tolerance on Food Contact Surfaces", fill="#0F172A", font=srm.get_font(20, bold=True))
        draw.text((1040, 470), "• SPONGES ARE STRICTLY FORBIDDEN (harbor bacteria)\n• WIRE SCOURING PADS ARE STRICTLY BANNED\n  (metal wire fragments break off into dairy product)\n• Use only approved color-coded plastic brushes\n• Store chemicals in locked dedicated chemical stores", fill="#7F1D1D", font=srm.get_font(21))

    if t >= 38.0:
        layout_utils.draw_centered_box_text(draw, (140, 760, 1780, 870), "ALWAYS CONSULT MATERIAL SAFETY DATA SHEETS (MSDS) AND WEAR MANDATORY PPE", srm.get_font(24, bold=True), "#FFFFFF", "#0284C7", 14)

    srm.draw_footer(draw, 14)
    return img

def render_slide_15(t, dur):  # Physical Safety
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Physical Controls", "Hazard Spotlight: Physical Safety", "Eradicating foreign body contamination across processing and packaging")
    
    hazards = [
        ("COMMON PHYSICAL HAZARDS", "• Glass from bulbs or jars\n• Brittle hard plastics\n• Metal shavings and swarf\n• Screws, bolts and nuts\n• Hair, jewellery & pen tops", "#EF4444", 2.0),
        ("CONSUMER HARM & IMPACT", "• Choking and airway blockage\n• Mouth and throat lacerations\n• Broken teeth and dental trauma\n• Internal intestinal punctures\n• Catastrophic brand recall", "#DC2626", 14.0),
        ("SITE GLASS & BRITTLE POLICY", "• Strict glass ban in factory & canteen\n• Daily glass & perspex audit register\n• Shatterproof plastic film on lights\n• Metal-detectable blue pens only\n• Personal items left in lockers", "#0284C7", 26.0),
        ("EMERGENCY BREAKAGE ACTION", "• STOP THE LINE IMMEDIATELY\n• Quarantine 30m radius of product\n• Notify Shift Manager & QA at once\n• Thorough vacuum clean & swab\n• Sign formal breakage clearance", "#D97706", 34.0),
    ]
    
    card_w = 380
    for i, (title, desc, col, delay) in enumerate(hazards):
        if t >= delay:
            x = 140 + i * (card_w + 33)
            y = 310
            draw.rounded_rectangle([(x, y), (x + card_w, y + 460)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + card_w, y + 14)], fill=col)
            draw.text((x + 20, y + 35), title, fill=col, font=srm.get_font(18, bold=True))
            desc_y = y + 80
            for l in desc.split("\n"):
                draw.text((x + 20, desc_y), l, fill="#1E293B", font=srm.get_font(19))
                desc_y += 32
                
    if t >= 42.0:
        layout_utils.draw_centered_box_text(draw, (140, 800, 1780, 890), "NEVER ATTEMPT TO CONTINUE RUNNING AFTER A GLASS OR HARD PLASTIC BREAKAGE", srm.get_font(24, bold=True), "#DC2626", "#FEE2E2", 14, border_w=2)
        
    srm.draw_footer(draw, 15)
    return img

def render_slide_16(t, dur):  # The 14 Major Food Allergens
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Allergen Compliance", "The 14 Major Recognized Food Allergens", "Statutory mandatory declaration under UK and EU Food Law: even trace amounts can be fatal")
    
    allergens = [
        "1. Celery", "2. Cereals with Gluten", "3. Crustaceans", "4. Eggs",
        "5. Fish", "6. Lupin", "7. Milk & Dairy", "8. Molluscs",
        "9. Mustard", "10. Peanuts", "11. Sesame Seeds", "12. Soya & Soya Lecithin",
        "13. Sulphites (>10mg/kg)", "14. Tree Nuts (Almonds, Hazelnuts, Cashews, etc.)"
    ]
    
    for i, item in enumerate(allergens):
        delay = (i // 4) * 18.0
        if t >= delay:
            col_idx = i % 4
            row_idx = i // 4
            x = 140 + col_idx * 415
            y = 300 + row_idx * 115
            card_w = 390
            col = "#0284C7" if i == 6 else ("#DC2626" if i in [9, 13] else "#059669")
            draw.rounded_rectangle([(x, y), (x + card_w, y + 95)], radius=12, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + 12, y + 95)], fill=col)
            draw.text((x + 25, y + 32), item, fill="#0F172A", font=srm.get_font(20, bold=True))
            
    if t >= 58.0:
        layout_utils.draw_centered_box_text(draw, (140, 780, 1780, 880), "ALLERGENS CAN CAUSE ANAPHYLACTIC SHOCK: PREVENT CROSS-CONTACT AT ALL COSTS", srm.get_font(24, bold=True), "#FFFFFF", "#DC2626", 14)
        
    srm.draw_footer(draw, 16)
    return img

def render_slide_17(t, dur):  # Allergens on Our Site
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Allergen Management", "Allergens on Our Dairy Processing Site", "Managing site-specific allergen profiles across liquid milk, yogurt, desserts and cheese")
    
    site_allergens = [
        ("MILK & DAIRY (CORE ALLERGEN)", "Present across all standard liquid milk, cheese, cream, butter and yogurt manufacturing lines.", "#0284C7", 2.0),
        ("CEREALS CONTAINING GLUTEN", "Used in dessert crumb bases, cheesecake biscuit layers, and specific yogurt crunchy toppers.", "#D97706", 14.0),
        ("EGG INGREDIENTS", "Used in specialized chilled custard preparations, baked dairy puddings, and sauce formulations.", "#EAB308", 20.0),
        ("SOYA & SULPHUR DIOXIDE", "Soya lecithin in chocolate coatings; Sulphites (>10ppm) in preserved fruit preparations & jams.", "#059669", 26.0),
    ]
    
    for i, (title, desc, col, delay) in enumerate(site_allergens):
        if t >= delay:
            col_idx = i % 2
            row_idx = i // 2
            x = 140 + col_idx * 830
            y = 300 + row_idx * 210
            draw.rounded_rectangle([(x, y), (x + 800, y + 180)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + 14, y + 180)], fill=col)
            draw.text((x + 35, y + 25), title, fill=col, font=srm.get_font(22, bold=True))
            draw.text((x + 35, y + 75), desc, fill="#1E293B", font=srm.get_font(21))
            
    if t >= 32.0:
        layout_utils.draw_centered_box_text(draw, (140, 740, 1780, 860), "ALLERGEN CLEAN-DOWN PROTOCOL: FULL CIP & VALIDATED RAPID PROTEIN SWAB TEST REQUIRED BETWEEN CHANGEOVERS", srm.get_font(23, bold=True), "#FFFFFF", "#0284C7", 14)
        
    srm.draw_footer(draw, 17)
    return img

def render_slide_18(t, dur):  # Strict Nut-Free Policy
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Site Safety Policy", "Strict Nut-Free Site Facility Policy", "Mandatory zero-tolerance prohibition of peanuts, tree nuts, and sesame seeds across the facility")
    
    # Left: Big Stop Shield
    draw.rounded_rectangle([(140, 300), (800, 720)], radius=20, fill="#FEF2F2", outline="#EF4444", width=3)
    draw.text((220, 340), "100% NUT-FREE ZONE", fill="#DC2626", font=srm.get_font(32, bold=True))
    draw.text((180, 410), "STRICTLY PROHIBITED ON SITE:\n• Peanuts & Peanut Butter\n• Almonds, Hazelnuts, Walnuts\n• Cashews, Pecans, Pistachios\n• Brazil nuts & Macadamias\n• Sesame seeds & Sesame oil", fill="#7F1D1D", font=srm.get_font(24, bold=True))
    
    if t >= 12.0:
        draw.rounded_rectangle([(860, 300), (1780, 720)], radius=20, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(860, 300), (875, 720)], fill="#0284C7")
        draw.text((910, 340), "PERSONAL RESPONSIBILITIES & SCOPE", fill="#0369A1", font=srm.get_font(28, bold=True))
        draw.text((910, 410), "1. Check your snacks, cereal bars, chocolates, and bakery lunches\n2. Never bring prohibited items into staff canteens or lockers\n3. Applies strictly to all employees, agency staff, contractors & visitors\n4. Report any accidental introduction immediately to HR & QA", fill="#1E293B", font=srm.get_font(22))
        
    if t >= 28.0:
        layout_utils.draw_centered_box_text(draw, (140, 760, 1780, 870), "PROTECT ALLERGIC CONSUMERS: ZERO NUTS PERMITTED ON SITE AT ANY TIME", srm.get_font(26, bold=True), "#DC2626", "#FEE2E2", 14, border_w=2)
        
    srm.draw_footer(draw, 18)
    return img

def render_slide_19(t, dur):  # Microbiological KPIs
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Microbial Specifications", "Biological Safety & Dairy Microbiological KPIs", "Finished product batch release criteria and regulatory testing limits")
    
    headers = ["TEST PARAMETER", "TARGET LIMIT", "ACTION LIMIT", "REJECT LIMIT"]
    x_offsets = [140, 680, 1060, 1440]
    col_w = [520, 360, 360, 340]
    
    # Draw Header Row
    y_table = 300
    draw.rounded_rectangle([(140, y_table), (1780, y_table + 55)], radius=8, fill="#0F172A")
    for idx, h in enumerate(headers):
        draw.text((x_offsets[idx] + 20, y_table + 16), h, fill="#FFFFFF", font=srm.get_font(20, bold=True))
        
    rows = [
        ("Total Viable Count (TVC)", "< 5,000 cfu/g", "5,000 - 10,000 cfu/g", "> 10,000 cfu/g", 2.0),
        ("Enterobacteriaceae", "< 10 cfu/g", "10 - 20 cfu/g", "≥ 20 cfu/g", 12.0),
        ("Staphylococcus aureus", "< 20 cfu/g", "20 - 50 cfu/g", "> 50 cfu/g", 24.0),
        ("Bacillus cereus", "< 100 cfu/g", "100 - 500 cfu/g", "> 500 cfu/g", 34.0),
        ("Salmonella spp.", "ABSENT / 25g", "N/A (Zero Tolerance)", "DETECTED", 44.0),
        ("Listeria monocytogenes", "ABSENT / 25g", "N/A (Zero Tolerance)", "DETECTED", 52.0),
    ]
    
    for r_idx, (param, targ, act, rej, delay) in enumerate(rows):
        if t >= delay:
            row_y = y_table + 65 + r_idx * 65
            bg_col = "#FEF2F2" if "ABSENT" in targ else ("#FFFFFF" if r_idx % 2 == 0 else "#F1F5F9")
            draw.rounded_rectangle([(140, row_y), (1780, row_y + 55)], radius=6, fill=bg_col, outline="#CBD5E1", width=1)
            draw.text((x_offsets[0] + 20, row_y + 16), param, fill="#0F172A", font=srm.get_font(20, bold=True))
            draw.text((x_offsets[1] + 20, row_y + 16), targ, fill="#059669" if "ABSENT" not in targ else "#DC2626", font=srm.get_font(20, bold=True))
            draw.text((x_offsets[2] + 20, row_y + 16), act, fill="#D97706", font=srm.get_font(20))
            draw.text((x_offsets[3] + 20, row_y + 16), rej, fill="#DC2626", font=srm.get_font(20, bold=True))
            
    if t >= 60.0:
        layout_utils.draw_centered_box_text(draw, (140, 780, 1780, 880), "ZERO TOLERANCE: ANY DETECTION OF SALMONELLA OR LISTERIA RESULTS IN IMMEDIATE LOT CONDEMNATION", srm.get_font(23, bold=True), "#FFFFFF", "#DC2626", 14)
        
    srm.draw_footer(draw, 19)
    return img

RENDERERS_PART3 = {
    14: render_slide_14,
    15: render_slide_15,
    16: render_slide_16,
    17: render_slide_17,
    18: render_slide_18,
    19: render_slide_19
}
