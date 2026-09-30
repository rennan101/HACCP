import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont
import filled_vector_assets

WIDTH, HEIGHT = 1920, 1080
FPS = 30
DURATION = 36.1
TOTAL_FRAMES = int(DURATION * FPS)
TEMP_FRAMES_DIR = "video_test/temp_squideo_frames"
OUTPUT_VIDEO = "video_test/rendered_videos/Slide_01_Squideo_Praise_Edition.mp4"
AUDIO_FILE = "audio_output/libby_energetic_british/Slide_01_Welcome_Course_Title.mp3"
BG_MUSIC = "video_test/ambient_bg_music_long.wav"

def get_font(size, bold=False):
    # Premium system fonts with high legibility & elegance
    if bold:
        font_paths = [
            "/System/Library/Fonts/HelveticaNeue.ttc",
            "/System/Library/Fonts/SFPro.ttf",
            "/Library/Fonts/Arial.ttf"
        ]
    else:
        font_paths = [
            "/System/Library/Fonts/HelveticaNeue.ttc",
            "/System/Library/Fonts/SFPro.ttf",
            "/Library/Fonts/Arial.ttf"
        ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def ease_out_back(t, s=1.70158):
    t = max(0.0, min(1.0, t))
    t = t - 1
    return (t * t * ((s + 1) * t + s) + 1)

def ease_out_cubic(t):
    t = max(0.0, min(1.0, t))
    return 1 - pow(1 - t, 3)

def render_squideo_frame(frame_idx):
    t = frame_idx / FPS
    # Clean warm executive studio background
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    
    # Elegant top brand bar
    draw.rectangle([(0, 0), (WIDTH, 14)], fill="#0284C7")
    
    # Idle floating animation offset (Gentle sine motion for living graphics)
    idle_float = int(math.sin(t * 3.0) * 8)
    
    # ==========================================
    # SCENE 1: 00:00 to 00:08.5 - WELCOME & DAIRY SECTOR
    # ==========================================
    if t < 8.5:
        p = min(1.0, t / 0.7)
        scale = ease_out_back(p)
        
        # Subtitle category tag
        draw.text((160, 150), "HACCP LEVEL 2 TRAINING : DAIRY SECTOR", fill="#0284C7", font=get_font(24, bold=True))
        # Elegant bold headline
        draw.text((160, 200), "Food Safety & Quality Excellence", fill="#0F172A", font=get_font(64, bold=True))
        draw.text((160, 285), "Dedicated operational training for liquid milk, cheese, yogurt & dairy teams", fill="#475569", font=get_font(30))
        
        # Right Side Big Filled Dairy Processing Tank (with lighting & idle float)
        filled_vector_assets.draw_filled_dairy_tank(draw, 1420, 560, scale=1.4 * scale, float_offset=idle_float)
        
        # Left Side Value Cards (Staggered Entrance)
        if t >= 1.0:
            p1 = min(1.0, (t - 1.0) / 0.6)
            s1 = ease_out_back(p1)
            y_c1 = 400
            draw.rounded_rectangle([(160, y_c1), (920, y_c1 + 140)], radius=18, fill="#FFFFFF", outline="#E2E8F0", width=2)
            draw.rectangle([(160, y_c1), (175, y_c1 + 140)], fill="#0284C7")
            draw.text((205, y_c1 + 25), "REGULATION COMPLIANCE", fill="#0369A1", font=get_font(20, bold=True))
            draw.text((205, y_c1 + 65), "UK & EU Regulation (EC) No 852/2004", fill="#0F172A", font=get_font(28, bold=True))
            
        if t >= 2.5:
            p2 = min(1.0, (t - 2.5) / 0.6)
            s2 = ease_out_back(p2)
            y_c2 = 580
            draw.rounded_rectangle([(160, y_c2), (920, y_c2 + 140)], radius=18, fill="#FFFFFF", outline="#E2E8F0", width=2)
            draw.rectangle([(160, y_c2), (175, y_c2 + 140)], fill="#10B981")
            draw.text((205, y_c2 + 25), "PLANT OPERATIONS", fill="#059669", font=get_font(20, bold=True))
            draw.text((205, y_c2 + 65), "Intake Decks, Pasteurisation & Packaging", fill="#0F172A", font=get_font(28, bold=True))

    # ==========================================
    # SCENE 2: 08.5 to 17.5 - THE 3 FILLED HAZARD PILLARS
    # ==========================================
    elif t < 17.5:
        st = t - 8.5
        draw.text((140, 130), "PREVENTIVE CONTROLS", fill="#0284C7", font=get_font(24, bold=True))
        draw.text((140, 175), "Prevent, Reduce & Eliminate Hazards at Source", fill="#0F172A", font=get_font(56, bold=True))
        draw.text((140, 255), "Managing the three critical vectors across all dairy processing stages", fill="#475569", font=get_font(28))
        
        # 3 Rich Filled Cards with 2D Visuals
        pillars = [
            ("BIOLOGICAL RISKS", "Pathogen Elimination\nListeria & Salmonella", filled_vector_assets.draw_filled_microbe, "#EF4444", 0.0),
            ("CHEMICAL RISKS", "CIP Chemical Control\nSanitiser Residues", filled_vector_assets.draw_filled_chemical_bottle, "#F59E0B", 1.2),
            ("PHYSICAL RISKS", "Foreign Body Control\nMetal & Fine Filtration", filled_vector_assets.draw_filled_filter_gear, "#0284C7", 2.4)
        ]
        
        card_w, card_h = 490, 500
        start_x = 140
        gap = 55
        
        for i, (title, desc, draw_func, col, delay) in enumerate(pillars):
            if st >= delay:
                p_prog = min(1.0, (st - delay) / 0.6)
                p_scale = ease_out_back(p_prog)
                x = start_x + i * (card_w + gap)
                y = 330
                
                # Card Body with shadow
                draw.rounded_rectangle([(x, y), (x + card_w, y + card_h)], radius=20, fill="#FFFFFF", outline=col, width=2)
                draw.rectangle([(x, y), (x + card_w, y + 14)], fill=col)
                
                # Filled Graphic Icon with dynamic floating
                item_float = int(math.sin((t + i) * 3.0) * 6)
                draw_func(draw, x + card_w // 2, y + 150, scale=1.0 * p_scale, float_offset=item_float)
                
                # Typography inside card
                draw.text((x + 35, y + 270), title, fill=col, font=get_font(24, bold=True))
                desc_y = y + 325
                for line in desc.split("\n"):
                    draw.text((x + 35, desc_y), line, fill="#0F172A", font=get_font(26, bold=True))
                    desc_y += 38

    # ==========================================
    # SCENE 3: 17.5 to 26.0 - CONSUMER TRUST & GOLDEN SHIELD
    # ==========================================
    elif t < 26.0:
        st = t - 17.5
        p = min(1.0, st / 0.7)
        scale = ease_out_back(p)
        
        draw.text((140, 130), "CONSUMER TRUST & REPUTATION", fill="#059669", font=get_font(24, bold=True))
        draw.text((140, 175), "Protecting Millions of Daily Consumers", fill="#0F172A", font=get_font(56, bold=True))
        
        # Left Side Big Emerald & Gold Shield
        shield_float = int(math.sin(t * 3.0) * 8)
        filled_vector_assets.draw_filled_quality_shield(draw, 450, 560, scale=1.5 * scale, float_offset=shield_float)
        draw.text((310, 750), "VERIFIED FOOD SAFETY", fill="#059669", font=get_font(24, bold=True))
        
        # Right Side 2 Big Value Cards
        draw.rounded_rectangle([(780, 310), (1780, 540)], radius=18, fill="#FFFFFF", outline="#10B981", width=2)
        draw.rectangle([(780, 310), (795, 540)], fill="#10B981")
        draw.text((830, 345), "PUBLIC HEALTH PROTECTION", fill="#059669", font=get_font(22, bold=True))
        draw.text((830, 385), "Zero Tolerated Outbreaks", fill="#0F172A", font=get_font(36, bold=True))
        draw.text((830, 445), "Preventing foodborne illnesses, severe allergic reactions,\nand maintaining absolute consumer confidence in the brand.", fill="#475569", font=get_font(24))
        
        draw.rounded_rectangle([(780, 580), (1780, 810)], radius=18, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(780, 580), (795, 810)], fill="#0284C7")
        draw.text((830, 615), "STATUTORY COMPLIANCE", fill="#0369A1", font=get_font(22, bold=True))
        draw.text((830, 655), "UK Regulation (EC) No 852/2004", fill="#0F172A", font=get_font(36, bold=True))
        draw.text((830, 715), "Meeting strict Environmental Health standards.\nA validated HACCP system is our mandatory licence to trade.", fill="#475569", font=get_font(24))

    # ==========================================
    # SCENE 4: 26.0 to 36.1 - COMPLETE DAIRY PROCESSING FLOW
    # ==========================================
    else:
        st = t - 26.0
        draw.text((140, 130), "END-TO-END OPERATIONAL RIGOUR", fill="#4F46E5", font=get_font(24, bold=True))
        draw.text((140, 175), "Safety Built into Every Processing Stage", fill="#0F172A", font=get_font(56, bold=True))
        
        # 4 Filled Process Nodes
        nodes = [
            ("1. RAW INTAKE", "Milk Reception Deck\nFine 1000µm Filtration", "#0284C7", 0.0),
            ("2. PASTEURISATION", "HTST Thermal Bays\n>72°C Continuous Kill", "#EF4444", 1.0),
            ("3. PACKAGING", "Cheese & Yogurt Lines\nMetal Detection", "#F59E0B", 2.0),
            ("4. QUALITY LAB", "Batch KPI Testing\nTotal Verification", "#10B981", 3.0)
        ]
        
        node_w = 360
        node_h = 420
        start_x = 140
        gap = 53
        y = 310
        
        for i, (title, desc, col, delay) in enumerate(nodes):
            if st >= delay:
                p_prog = min(1.0, (st - delay) / 0.5)
                scale = ease_out_back(p_prog)
                x = start_x + i * (node_w + gap)
                
                # Connector Arrow
                if i > 0 and st >= delay:
                    arr_x = x - gap + 15
                    draw.polygon([(arr_x, y + 210), (arr_x + 20, y + 200), (arr_x + 20, y + 220)], fill="#94A3B8")
                    
                draw.rounded_rectangle([(x, y), (x + node_w, y + node_h)], radius=18, fill="#FFFFFF", outline=col, width=2)
                draw.rectangle([(x, y), (x + node_w, y + 14)], fill=col)
                
                # Filled Badge Number
                draw.ellipse([(x + 30, y + 35), (x + 85, y + 90)], fill=col)
                draw.text((x + 47, y + 43), str(i + 1), fill="#FFFFFF", font=get_font(30, bold=True))
                
                draw.text((x + 30, y + 120), title, fill=col, font=get_font(24, bold=True))
                
                desc_y = y + 180
                for line in desc.split("\n"):
                    draw.text((x + 30, desc_y), line, fill="#0F172A", font=get_font(24, bold=True))
                    desc_y += 38
                    
        # Bottom Call to Action
        if st >= 4.0:
            draw.rounded_rectangle([(140, 780), (1780, 870)], radius=14, fill="#0F172A")
            draw.text((750, 805), "LET'S GET STARTED WITH HACCP EXCELLENCE", fill="#38BDF8", font=get_font(28, bold=True))

    # Clean bottom footer
    draw.line([(140, 940), (1780, 940)], fill="#E2E8F0", width=1)
    draw.text((140, 970), "HACCP Food Safety Masterclass • Module 01 : Welcome", fill="#64748B", font=get_font(22))
    draw.text((1600, 970), "Slide 01 / 26", fill="#64748B", font=get_font(22))
    
    return img

def main():
    os.makedirs(TEMP_FRAMES_DIR, exist_ok=True)
    os.makedirs("video_test/rendered_videos", exist_ok=True)
    
    print(f"Generating {TOTAL_FRAMES} Squideo Praise Edition frames at {FPS} FPS...")
    for idx in range(TOTAL_FRAMES):
        if idx % 150 == 0 or idx == TOTAL_FRAMES - 1:
            print(f"Progress: {idx}/{TOTAL_FRAMES} ({(idx/TOTAL_FRAMES)*100:.1f}%)")
        f_img = render_squideo_frame(idx)
        f_img.save(os.path.join(TEMP_FRAMES_DIR, f"frame_{idx:05d}.jpg"), quality=92)
        
    print("\nEncoding Squideo Edition Video with FFmpeg & Seamless Audio...")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", os.path.join(TEMP_FRAMES_DIR, "frame_%05d.jpg"),
        "-i", AUDIO_FILE,
        "-stream_loop", "-1", "-i", BG_MUSIC,
        "-filter_complex", "[1:a]volume=1.0[v_speech];[2:a]volume=0.10[v_music];[v_speech][v_music]amix=inputs=2:duration=first:dropout_transition=2[a_out]",
        "-map", "0:v", "-map", "[a_out]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        OUTPUT_VIDEO
    ]
    subprocess.run(cmd, check=True)
    
    # Cleanup temp frames
    for f in os.listdir(TEMP_FRAMES_DIR):
        os.remove(os.path.join(TEMP_FRAMES_DIR, f))
    os.rmdir(TEMP_FRAMES_DIR)
    
    print(f"\n✅ Squideo Edition Video successfully rendered: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    main()
