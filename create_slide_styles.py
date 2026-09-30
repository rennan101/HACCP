import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "video_test/slide_styles"
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1920, 1080

def get_font(size, bold=False):
    # Try system fonts on macOS
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFPro.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

# 1. Style: Modern Corporate Dark Blue
def create_style_dark_blue():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0F172A") # Deep Navy / Slate
    draw = ImageDraw.Draw(img)
    
    # Header Accent bar
    draw.rectangle([(0, 0), (WIDTH, 12)], fill="#38BDF8") # Cyan / Sky Blue
    
    # Subtle Background glowing accents
    draw.ellipse([(-100, -100), (600, 600)], fill="#1E293B")
    draw.ellipse([(1400, 600), (2100, 1300)], fill="#1E293B")
    
    # Badge / Category
    draw.rounded_rectangle([(140, 180), (480, 235)], radius=12, fill="#1E293B", outline="#38BDF8", width=2)
    font_badge = get_font(22, bold=True)
    draw.text((165, 195), "HACCP LEVEL 2 TRAINING", fill="#38BDF8", font=font_badge)
    
    # Title
    font_title = get_font(58, bold=True)
    draw.text((140, 270), "Food Safety & Dairy Excellence", fill="#FFFFFF", font=font_title)
    
    # Subtitle
    font_sub = get_font(34)
    draw.text((140, 350), "Comprehensive Masterclass for Food & Dairy Professionals", fill="#94A3B8", font=font_sub)
    
    # Main Content Card
    draw.rounded_rectangle([(140, 440), (1200, 880)], radius=20, fill="#1E293B", outline="#334155", width=2)
    
    # Card Bullets
    bullets = [
        ("🥛", "Tailored for Liquid Milk, Cheese, Yogurt & Dairy Operations"),
        ("🛡️", "Prevent, Reduce & Eliminate Food Safety Hazards at Source"),
        ("📜", "Full UK Regulation (EC) 852/2004 & Codex Alimentarius Compliance"),
        ("⚡", "Practical CCP Monitoring & Operational Risk Management")
    ]
    
    font_bullet = get_font(28)
    font_icon = get_font(32)
    y = 490
    for icon, text in bullets:
        draw.text((180, y), icon, fill="#38BDF8", font=font_icon)
        draw.text((250, y + 2), text, fill="#F1F5F9", font=font_bullet)
        y += 90
        
    # Right Side Graphic Frame / Card
    draw.rounded_rectangle([(1260, 440), (1780, 880)], radius=20, fill="#0284C7", outline="#38BDF8", width=3)
    draw.text((1310, 520), "CORE MISSION", fill="#BAE6FD", font=font_badge)
    draw.text((1310, 570), "Safe Dairy Products.\nTrusted Brands.\nZero Compromise.", fill="#FFFFFF", font=get_font(42, bold=True))
    draw.text((1310, 750), "Speaker: Libby (en-GB)\nFormat: Video + Separate SRT", fill="#E0F2FE", font=get_font(24))
    
    # Footer
    draw.text((140, 980), "Dairy Manufacturing Compliance Programme", fill="#64748B", font=get_font(22))
    draw.text((1550, 980), "Slide 01 / 26", fill="#64748B", font=get_font(22))
    
    img.save(f"{OUTPUT_DIR}/style_1_modern_dark_blue.png")
    print("Saved Style 1: Modern Corporate Dark Blue")

# 2. Style: Modern Corporate Clean White
def create_style_clean_white():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC") # Crisp Clean Off-White
    draw = ImageDraw.Draw(img)
    
    # Top Bar
    draw.rectangle([(0, 0), (WIDTH, 14)], fill="#0284C7")
    
    # Category Pill
    draw.rounded_rectangle([(140, 160), (480, 215)], radius=25, fill="#E0F2FE", outline="#0284C7", width=1)
    draw.text((170, 175), "HACCP LEVEL 2 TRAINING", fill="#0369A1", font=get_font(22, bold=True))
    
    # Main Title
    draw.text((140, 250), "Food Safety & Dairy Excellence", fill="#0F172A", font=get_font(58, bold=True))
    draw.text((140, 330), "Professional Masterclass for Food & Dairy Operations", fill="#475569", font=get_font(34))
    
    # Card 1 (Left Key Features)
    draw.rounded_rectangle([(140, 420), (1180, 880)], radius=20, fill="#FFFFFF", outline="#E2E8F0", width=2)
    # Accent strip on left of card
    draw.rounded_rectangle([(140, 420), (155, 880)], radius=5, fill="#0284C7")
    
    bullets = [
        ("•", "Dairy Sector Focus: Liquid Milk, Cheese, Yogurts & Desserts"),
        ("•", "7 Codex Alimentarius Principles & Practical Implementation"),
        ("•", "UK Regulation (EC) 852/2004 Hygiene Standards"),
        ("•", "Zero Tolerance Contamination & Legal Responsibilities")
    ]
    
    y = 480
    for bullet, text in bullets:
        draw.text((190, y), bullet, fill="#0284C7", font=get_font(40, bold=True))
        draw.text((230, y + 8), text, fill="#1E293B", font=get_font(28))
        y += 90
        
    # Card 2 (Right Highlight Panel)
    draw.rounded_rectangle([(1230, 420), (1780, 880)], radius=20, fill="#F0F9FF", outline="#BAE6FD", width=2)
    draw.text((1280, 480), "DAIRY INDUSTRY STANDARD", fill="#0284C7", font=get_font(22, bold=True))
    draw.text((1280, 540), "Protecting Consumers,\nEnsuring Quality.", fill="#0F172A", font=get_font(40, bold=True))
    
    draw.rounded_rectangle([(1280, 680), (1730, 820)], radius=12, fill="#FFFFFF", outline="#E0F2FE", width=1)
    draw.text((1305, 710), "Certification Standard: Level 2", fill="#334155", font=get_font(22, bold=True))
    draw.text((1305, 750), "Voiceover: British English (Libby)", fill="#64748B", font=get_font(20))
    
    # Footer
    draw.line([(140, 940), (1780, 940)], fill="#E2E8F0", width=1)
    draw.text((140, 970), "HACCP Food Safety Management System", fill="#94A3B8", font=get_font(22))
    draw.text((1580, 970), "Slide 01 of 26", fill="#94A3B8", font=get_font(22))
    
    img.save(f"{OUTPUT_DIR}/style_2_modern_clean_white.png")
    print("Saved Style 2: Modern Corporate Clean White")

# 3. Style: Presentation with Illustrated Topic Cards
def create_style_illustrated_cards():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0B132B") # Dark Midnight Theme
    draw = ImageDraw.Draw(img)
    
    # Header Section
    draw.rounded_rectangle([(140, 100), (380, 150)], radius=15, fill="#1C2541")
    draw.text((165, 115), "MODULE 1 : WELCOME", fill="#48CAE4", font=get_font(20, bold=True))
    
    draw.text((140, 180), "HACCP Level 2 : Dairy & Food Training", fill="#FFFFFF", font=get_font(52, bold=True))
    draw.text((140, 255), "Building safety directly into every processing stage", fill="#90E0EF", font=get_font(28))
    
    # 3 Illustrated Feature Cards side by side
    card_width = 490
    card_height = 500
    gap = 45
    start_x = 140
    y_card = 340
    
    cards_data = [
        {
            "tag": "PREVENTION",
            "title": "Hazard Control",
            "desc": "Identify and eliminate physical, chemical, biological and allergen risks in raw milk and dairy lines.",
            "color": "#0077B6",
            "border": "#0096C7"
        },
        {
            "tag": "COMPLIANCE",
            "title": "7 Principles",
            "desc": "Master Codex Alimentarius standards, CCP critical limits, automated divert valves and monitoring.",
            "color": "#1C2541",
            "border": "#48CAE4"
        },
        {
            "tag": "ACCOUNTABILITY",
            "title": "Food Safety Attitude",
            "desc": "Empower your team with personal hygiene, clean zoning and zero-tolerance cross-contamination.",
            "color": "#0077B6",
            "border": "#0096C7"
        }
    ]
    
    for i, c in enumerate(cards_data):
        x = start_x + i * (card_width + gap)
        # Card Body
        draw.rounded_rectangle([(x, y_card), (x + card_width, y_card + card_height)], radius=20, fill=c["color"], outline=c["border"], width=2)
        
        # Tag inside card
        draw.rounded_rectangle([(x + 35, y_card + 40), (x + 220, y_card + 85)], radius=10, fill="#0B132B")
        draw.text((x + 50, y_card + 52), c["tag"], fill="#48CAE4", font=get_font(18, bold=True))
        
        # Title inside card
        draw.text((x + 35, y_card + 115), c["title"], fill="#FFFFFF", font=get_font(36, bold=True))
        
        # Description (manual wrap)
        font_desc = get_font(24)
        words = c["desc"].split()
        lines = []
        cur_line = []
        for w in words:
            if len(" ".join(cur_line + [w])) > 28:
                lines.append(" ".join(cur_line))
                cur_line = [w]
            else:
                cur_line.append(w)
        if cur_line:
            lines.append(" ".join(cur_line))
            
        desc_y = y_card + 200
        for l in lines:
            draw.text((x + 35, desc_y), l, fill="#CAF0F8", font=font_desc)
            desc_y += 40
            
    # Footer
    draw.text((140, 960), "HACCP Food Safety Masterclass • Video Series", fill="#5BC0BE", font=get_font(22))
    draw.text((1600, 960), "Slide 01 / 26", fill="#5BC0BE", font=get_font(22))
    
    img.save(f"{OUTPUT_DIR}/style_3_illustrated_cards.png")
    print("Saved Style 3: Presentation with Illustrated Topic Cards")

if __name__ == "__main__":
    create_style_dark_blue()
    create_style_clean_white()
    create_style_illustrated_cards()
