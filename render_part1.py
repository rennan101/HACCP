import os
import math
import subprocess
from PIL import Image, ImageDraw
import slide_render_modules as srm
import filled_vector_assets as fva
import layout_utils
from slides_metadata import SLIDES_DATA

WIDTH, HEIGHT = 1920, 1080
FPS = 25
OUTPUT_DIR = "video_test/master_clips"
BG_MUSIC = "video_test/ambient_bg_music_long.wav"

def get_audio_duration(audio_path):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", audio_path]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

# Custom Scene Renderers for Slides 1 to 6
def render_slide_01(t, dur): # Welcome
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "HACCP Level 2 Training", "Food Safety & Dairy Excellence", "Tailored for Liquid Milk, Cheese, Yogurt & Packing Halls")
    fva.draw_filled_dairy_tank(draw, 1420, 540, scale=1.4, float_offset=int(math.sin(t*3)*8))
    # 2 Big Cards
    if t >= 1.0:
        draw.rounded_rectangle([(140, 360), (940, 500)], radius=16, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(140, 360), (155, 500)], fill="#0284C7")
        draw.text((180, 390), "STATUTORY STANDARD", fill="#0369A1", font=srm.get_font(20, bold=True))
        draw.text((180, 425), "UK & EU Regulation (EC) No 852/2004", fill="#0F172A", font=srm.get_font(28, bold=True))
    if t >= 4.0:
        draw.rounded_rectangle([(140, 540), (940, 680)], radius=16, fill="#FFFFFF", outline="#10B981", width=2)
        draw.rectangle([(140, 540), (155, 680)], fill="#10B981")
        draw.text((180, 570), "PLANT OPERATIONS", fill="#059669", font=srm.get_font(20, bold=True))
        draw.text((180, 605), "Intake Decks, Pasteurisation & Packaging", fill="#0F172A", font=srm.get_font(28, bold=True))
    if t >= 25.0:
        layout_utils.draw_centered_box_text(draw, (140, 750, 1780, 850), "LET'S GET STARTED WITH HACCP EXCELLENCE", srm.get_font(30, bold=True), "#38BDF8", "#0F172A", 14)
    srm.draw_footer(draw, 1)
    return img

def render_slide_02(t, dur): # Agenda
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Course Agenda", "What Will You Learn Today?", "Aim: To summarise HACCP system and review the CCP concepts")
    topics = [
        "1. What is HACCP & Origins", "2. Food Hazards (Bio, Chem, Phys, Allergen)",
        "3. Regulations & Codex Standards", "4. The 7 Principles of HACCP",
        "5. Determining CCPs in Dairy", "6. Importance of HACCP for Your Business",
        "7. CCP Monitoring & Deviations", "8. Prerequisite Programmes (PRPs)",
        "9. Corrective Actions (PDCA)", "10. Responsibilities & Assessment Quiz"
    ]
    for i, top in enumerate(topics):
        delay = i * 2.5
        if t >= delay:
            col = i % 2
            row = i // 2
            x = 140 + col * 820
            y = 300 + row * 115
            draw.rounded_rectangle([(x, y), (x + 780, y + 95)], radius=12, fill="#FFFFFF", outline="#0284C7", width=2)
            draw.rectangle([(x, y), (x + 12, y + 95)], fill="#0284C7")
            draw.text((x + 35, y + 32), top, fill="#0F172A", font=srm.get_font(24, bold=True))
    srm.draw_footer(draw, 2)
    return img

def render_slide_03(t, dur): # What is HACCP
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Core System Definition", "What is HACCP?", "Hazard Analysis Critical Control Point: built-in prevention at source")
    # Comparison Boxes
    draw.rounded_rectangle([(140, 310), (920, 720)], radius=18, fill="#FEE2E2", outline="#EF4444", width=2)
    draw.text((180, 345), "OLD APPROACH : END INSPECTION", fill="#DC2626", font=srm.get_font(22, bold=True))
    draw.text((180, 395), "• Testing finished product at the end\n• High recall risk & delayed discovery\n• Cannot test 100% of manufactured units\n• Unsafe product already packaged", fill="#475569", font=srm.get_font(24))
    
    if t >= 8.0:
        draw.rounded_rectangle([(1000, 310), (1780, 720)], radius=18, fill="#ECFDF5", outline="#10B981", width=2)
        draw.text((1040, 345), "HACCP APPROACH : PROCESS CONTROL", fill="#059669", font=srm.get_font(22, bold=True))
        draw.text((1040, 395), "• Identifies hazards at each process stage\n• Real-time monitoring of critical limits\n• Immediate automated divert & correction\n• Prevents, reduces or eliminates risks at source", fill="#1E293B", font=srm.get_font(24))
    if t >= 25.0:
        layout_utils.draw_centered_box_text(draw, (140, 770, 1780, 870), "BUILT UPON 7 FUNDAMENTAL CODEX PRINCIPLES", srm.get_font(28, bold=True), "#FFFFFF", "#0284C7", 14)
    srm.draw_footer(draw, 3)
    return img

def render_slide_04(t, dur): # History Timeline
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Historical Origins", "Where Does HACCP Come From?", "From 1960s NASA Space Missions to Mandated Statutory Food Law")
    eras = [
        ("1960s : NASA & PILLSBURY", "Astronaut food: 100% safe & pathogen-free", srm.draw_nasa_rocket, "#0284C7", 0.0),
        ("1970s : US FDA ADOPTION", "Adopted for commercial canned manufacturing", srm.draw_canned_food, "#F59E0B", 12.0),
        ("1990s : CODEX STANDARD", "Codex Alimentarius global safety guidelines", srm.draw_codex_book, "#8B5CF6", 24.0),
        ("2000s : UK/EU MANDATORY LAW", "Regulation (EC) 852/2004 statutory mandate", srm.draw_law_seal, "#059669", 36.0)
    ]
    card_w = 380
    for i, (title, desc, draw_func, col, delay) in enumerate(eras):
        if t >= delay:
            x = 140 + i * (card_w + 33)
            y = 320
            draw.rounded_rectangle([(x, y), (x + card_w, y + 490)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + card_w, y + 14)], fill=col)
            draw_func(draw, x + card_w // 2, y + 160, scale=0.9)
            draw.text((x + 20, y + 280), title, fill=col, font=srm.get_font(20, bold=True))
            desc_y = y + 330
            for l in desc.split("\n"):
                draw.text((x + 20, desc_y), l, fill="#1E293B", font=srm.get_font(22, bold=True))
                desc_y += 35
    srm.draw_footer(draw, 4)
    return img

def render_slide_05(t, dur): # 4 Hazards
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Hazard Identification", "What Are the Hazards in Food?", "A hazard is anything dangerous that could make food unsafe or unfit to eat")
    quads = [
        ("1. BIOLOGICAL HAZARDS", "Pathogenic bacteria & viruses\nListeria, Salmonella, E. coli & B. cereus", fva.draw_filled_microbe, "#EF4444", 0.0),
        ("2. CHEMICAL HAZARDS", "Detergent residues, sanitisers & lubricants\nImproper CIP rinse & dosing", fva.draw_filled_chemical_bottle, "#F59E0B", 12.0),
        ("3. PHYSICAL HAZARDS", "Foreign objects: glass, metal shavings,\nplastic, hair, insects & screws", fva.draw_filled_filter_gear, "#0284C7", 24.0),
        ("4. ALLERGEN HAZARDS", "The 14 major recognized allergens\nSevere cross-contact risks", fva.draw_filled_quality_shield, "#10B981", 36.0)
    ]
    for i, (title, desc, draw_func, col, delay) in enumerate(quads):
        if t >= delay:
            col_idx = i % 2
            row_idx = i // 2
            x = 140 + col_idx * 830
            y = 300 + row_idx * 270
            draw.rounded_rectangle([(x, y), (x + 800, y + 245)], radius=16, fill="#FFFFFF", outline=col, width=2)
            draw.rectangle([(x, y), (x + 14, y + 245)], fill=col)
            draw_func(draw, x + 100, y + 120, scale=0.8)
            draw.text((x + 200, y + 35), title, fill=col, font=srm.get_font(24, bold=True))
            desc_y = y + 85
            for l in desc.split("\n"):
                draw.text((x + 200, desc_y), l, fill="#1E293B", font=srm.get_font(22, bold=True))
                desc_y += 35
    srm.draw_footer(draw, 5)
    return img

def render_slide_06(t, dur): # Regulations & EHO
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    srm.draw_header(draw, "Statutory Compliance", "Regulations & Legal Guidelines", "Codex Alimentarius baseline & UK Regulation (EC) 852/2004 enforcement")
    draw.rounded_rectangle([(140, 310), (920, 520)], radius=18, fill="#FFFFFF", outline="#0284C7", width=2)
    draw.rectangle([(140, 310), (155, 520)], fill="#0284C7")
    draw.text((180, 345), "CODEX ALIMENTARIUS (FAO / WHO)", fill="#0369A1", font=srm.get_font(22, bold=True))
    draw.text((180, 395), "• International benchmark food safety code\n• Defines WHAT general safety requirements are\n• HACCP acts as the operational HOW-TO guide", fill="#1E293B", font=srm.get_font(24))
    
    if t >= 15.0:
        draw.rounded_rectangle([(1000, 310), (1780, 520)], radius=18, fill="#FFFFFF", outline="#059669", width=2)
        draw.rectangle([(1000, 310), (1015, 520)], fill="#059669")
        draw.text((1040, 345), "REGULATION (EC) NO 852/2004", fill="#059669", font=srm.get_font(22, bold=True))
        draw.text((1040, 395), "• Mandatory UK statutory food hygiene law\n• Compulsory permanent HACCP-based system\n• Legal obligation on all food business operators", fill="#1E293B", font=srm.get_font(24))
    if t >= 30.0:
        layout_utils.draw_centered_box_text(draw, (140, 580, 1780, 830), "ENVIRONMENTAL HEALTH OFFICER (EHO) ENFORCEMENT:\nEHOs inspect food sites regularly. Failure to implement HACCP can result\nin immediate site closure, heavy statutory fines, and criminal prosecution.", srm.get_font(26, bold=True), "#DC2626", "#FEE2E2", 18, border_w=2)
    srm.draw_footer(draw, 6)
    return img

RENDERERS_PART1 = {
    1: render_slide_01,
    2: render_slide_02,
    3: render_slide_03,
    4: render_slide_04,
    5: render_slide_05,
    6: render_slide_06
}
