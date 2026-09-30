import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont
import vector_assets

WIDTH, HEIGHT = 1920, 1080
FPS = 30
DURATION = 36.1
TOTAL_FRAMES = int(DURATION * FPS)
TEMP_FRAMES_DIR = "video_test/temp_explainer_frames"
OUTPUT_VIDEO = "video_test/rendered_videos/Slide_01_Explainer_2D_Motion.mp4"
AUDIO_FILE = "audio_output/libby_energetic_british/Slide_01_Welcome_Course_Title.mp3"
BG_MUSIC = "video_test/ambient_bg_music_long.wav"

def get_font(size, bold=False):
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
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

def render_explainer_frame(frame_idx):
    t = frame_idx / FPS
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    
    # Top Accent Bar
    draw.rectangle([(0, 0), (WIDTH, 12)], fill="#0284C7")
    
    # ==========================================
    # SCENE 1: 00:00 to 00:08.5 - WELCOME & DAIRY SECTOR
    # ==========================================
    if t < 8.5:
        p = min(1.0, t / 0.8)
        scale = ease_out_back(p)
        alpha = ease_out_cubic(min(1.0, t / 0.5))
        
        # Central Badge
        draw.rounded_rectangle([(700, 130), (1220, 180)], radius=6, fill="#E0F2FE", outline="#0284C7", width=2)
        draw.text((720, 145), "HACCP LEVEL 2 TRAINING : DAIRY SECTOR", fill="#0369A1", font=get_font(20, bold=True))
        
        # Main Title
        draw.text((360, 220), "Food Safety Management Excellence", fill="#0F172A", font=get_font(60, bold=True))
        draw.text((430, 305), "Tailored for Liquid Milk, Cheese, Yogurt & Dairy Operations", fill="#475569", font=get_font(30))
        
        # Central Dairy Tank Illustration (Scale Pop-in)
        tank_scale = 1.3 * scale
        vector_assets.draw_dairy_tank_icon(draw, 960, 560, scale=tank_scale)
        
        # Feature Highlights
        draw.rounded_rectangle([(320, 770), (760, 860)], radius=12, fill="#FFFFFF", outline="#E2E8F0", width=2)
        draw.rectangle([(320, 770), (330, 860)], fill="#0284C7")
        draw.text((350, 790), "REGULATION COMPLIANCE", fill="#0369A1", font=get_font(18, bold=True))
        draw.text((350, 820), "UK & EU Regulation (EC) 852/2004", fill="#1E293B", font=get_font(22, bold=True))
        
        draw.rounded_rectangle([(1160, 770), (1600, 860)], radius=12, fill="#FFFFFF", outline="#E2E8F0", width=2)
        draw.rectangle([(1160, 770), (1170, 860)], fill="#10B981")
        draw.text((1190, 790), "OPERATIONAL SCOPE", fill="#059669", font=get_font(18, bold=True))
        draw.text((1190, 820), "Intake, Pasteurisation & Packaging", fill="#1E293B", font=get_font(22, bold=True))

    # ==========================================
    # SCENE 2: 08.5 to 17.5 - THE 3 HAZARD PILLARS
    # ==========================================
    elif t < 17.5:
        st = t - 8.5
        # Slide Header
        draw.text((140, 130), "PROACTIVE FOOD SAFETY", fill="#0369A1", font=get_font(22, bold=True))
        draw.text((140, 170), "Prevent, Reduce & Eliminate Hazards at Source", fill="#0F172A", font=get_font(50, bold=True))
        draw.text((140, 240), "Targeting the three critical vectors in dairy processing lines", fill="#475569", font=get_font(28))
        
        # 3 Pillar Cards with Icons
        pillars = [
            ("BIOLOGICAL RISKS", "Pathogen Elimination\nListeria & Salmonella", vector_assets.draw_biohazard_microbe_icon, "#EF4444", 0.0),
            ("CHEMICAL RISKS", "CIP Chemical Control\nSanitiser Residues", vector_assets.draw_chemical_flask_icon, "#F59E0B", 1.2),
            ("PHYSICAL RISKS", "Foreign Body Control\nMetal & Fine Filtration", vector_assets.draw_metal_filter_gear_icon, "#0284C7", 2.4)
        ]
        
        card_w, card_h = 490, 480
        start_x = 140
        gap = 55
        
        for i, (title, desc, icon_func, col, delay) in enumerate(pillars):
            if st >= delay:
                p_prog = min(1.0, (st - delay) / 0.6)
                p_scale = ease_out_back(p_prog)
                x = start_x + i * (card_w + gap)
                y = 330
                
                # Card Background
                draw.rounded_rectangle([(x, y), (x + card_w, y + card_h)], radius=16, fill="#FFFFFF", outline=col, width=2)
                draw.rectangle([(x, y), (x + card_w, y + 12)], fill=col)
                
                # Icon Centered
                icon_func(draw, x + card_w // 2, y + 140, scale=1.0 * p_scale)
                
                # Text
                draw.text((x + 30, y + 260), title, fill=col, font=get_font(22, bold=True))
                # Multiline description
                desc_y = y + 310
                for line in desc.split("\n"):
                    draw.text((x + 30, desc_y), line, fill="#1E293B", font=get_font(24, bold=True))
                    desc_y += 35

    # ==========================================
    # SCENE 3: 17.5 to 26.0 - CONSUMER TRUST & LAW
    # ==========================================
    elif t < 26.0:
        st = t - 17.5
        p = min(1.0, st / 0.7)
        scale = ease_out_back(p)
        
        draw.text((140, 130), "CONSUMER TRUST & REGULATION", fill="#059669", font=get_font(22, bold=True))
        draw.text((140, 170), "Protecting Millions of Daily Consumers", fill="#0F172A", font=get_font(50, bold=True))
        
        # Left Side Big Shield
        vector_assets.draw_shield_badge_icon(draw, 450, 560, scale=2.2 * scale)
        draw.text((340, 760), "100% VERIFIED SAFETY", fill="#059669", font=get_font(22, bold=True))
        
        # Right Side 2 Big Value Cards
        draw.rounded_rectangle([(780, 310), (1780, 540)], radius=16, fill="#FFFFFF", outline="#10B981", width=2)
        draw.rectangle([(780, 310), (792, 540)], fill="#10B981")
        draw.text((820, 340), "PUBLIC HEALTH PROTECTION", fill="#059669", font=get_font(20, bold=True))
        draw.text((820, 380), "Zero Tolerated Outbreaks", fill="#0F172A", font=get_font(34, bold=True))
        draw.text((820, 440), "Preventing foodborne illnesses, severe allergic reactions,\nand maintaining absolute consumer confidence in the dairy brand.", fill="#475569", font=get_font(22))
        
        draw.rounded_rectangle([(780, 580), (1780, 810)], radius=16, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(780, 580), (792, 810)], fill="#0284C7")
        draw.text((820, 610), "STATUTORY COMPLIANCE", fill="#0369A1", font=get_font(20, bold=True))
        draw.text((820, 650), "UK Regulation (EC) No 852/2004", fill="#0F172A", font=get_font(34, bold=True))
        draw.text((820, 710), "Meeting strict Environmental Health standards.\nA validated HACCP system is our mandatory licence to trade.", fill="#475569", font=get_font(22))

    # ==========================================
    # SCENE 4: 26.0 to 36.1 - COMPLETE DAIRY FLOW
    # ==========================================
    else:
        st = t - 26.0
        draw.text((140, 130), "OPERATIONAL EXCELLENCE", fill="#4F46E5", font=get_font(22, bold=True))
        draw.text((140, 170), "End-to-End Safety Across Every Processing Bay", fill="#0F172A", font=get_font(50, bold=True))
        
        # 4 Horizontal Process Nodes
        nodes = [
            ("1. RAW INTAKE", "Milk Reception Deck\nFiltering & Testing", "#0284C7", 0.0),
            ("2. PASTEURISATION", "HTST Thermal Bays\n>72°C Continuous Kill", "#EF4444", 1.2),
            ("3. PACKAGING", "Cheese & Yogurt Lines\nMetal Detection", "#F59E0B", 2.4),
            ("4. QUALITY ASSURANCE", "Lab Verification\nBatch Release Standard", "#10B981", 3.6)
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
                
                # Connector Arrow before node (if not first)
                if i > 0 and st >= delay:
                    arr_x = x - gap + 15
                    draw.polygon([(arr_x, y + 210), (arr_x + 20, y + 200), (arr_x + 20, y + 220)], fill="#94A3B8")
                    
                draw.rounded_rectangle([(x, y), (x + node_w, y + node_h)], radius=16, fill="#FFFFFF", outline=col, width=2)
                draw.rectangle([(x, y), (x + node_w, y + 12)], fill=col)
                
                # Number Circle
                draw.ellipse([(x + 25, y + 40), (x + 75, y + 90)], fill=col)
                draw.text((x + 42, y + 48), str(i + 1), fill="#FFFFFF", font=get_font(26, bold=True))
                
                draw.text((x + 25, y + 120), title, fill=col, font=get_font(22, bold=True))
                
                desc_y = y + 175
                for line in desc.split("\n"):
                    draw.text((x + 25, desc_y), line, fill="#1E293B", font=get_font(22, bold=True))
                    desc_y += 35
                    
        # Bottom Big Banner
        if st >= 4.5:
            draw.rounded_rectangle([(140, 770), (1780, 860)], radius=12, fill="#0F172A")
            draw.text((780, 795), "LET'S GET STARTED WITH HACCP EXCELLENCE", fill="#38BDF8", font=get_font(26, bold=True))

    # Footer
    draw.line([(140, 940), (1780, 940)], fill="#E2E8F0", width=1)
    draw.text((140, 970), "HACCP Food Safety Masterclass • Module 01 : Welcome", fill="#64748B", font=get_font(22))
    draw.text((1600, 970), "Slide 01 / 26", fill="#64748B", font=get_font(22))
    
    return img

def main():
    os.makedirs(TEMP_FRAMES_DIR, exist_ok=True)
    os.makedirs("video_test/rendered_videos", exist_ok=True)
    
    print(f"Generating {TOTAL_FRAMES} Explainer Motion Graphics frames at {FPS} FPS...")
    for idx in range(TOTAL_FRAMES):
        if idx % 150 == 0 or idx == TOTAL_FRAMES - 1:
            print(f"Progress: {idx}/{TOTAL_FRAMES} ({(idx/TOTAL_FRAMES)*100:.1f}%)")
        f_img = render_explainer_frame(idx)
        f_img.save(os.path.join(TEMP_FRAMES_DIR, f"frame_{idx:05d}.jpg"), quality=90)
        
    print("\nEncoding Explainer video with FFmpeg & Seamless Audio...")
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
    
    print(f"\n✅ Explainer Motion 2D Video successfully generated: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    main()
