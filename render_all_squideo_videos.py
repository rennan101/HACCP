import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont
import filled_vector_assets
import layout_utils
from slides_metadata import SLIDES_DATA

WIDTH, HEIGHT = 1920, 1080
FPS = 30
OUTPUT_DIR = "video_test/all_slides_squideo"
SRT_DIR = "video_test/all_slides_subtitles"
BG_MUSIC = "video_test/ambient_bg_music_long.wav"

def get_font(size, bold=False):
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

def get_audio_duration(audio_path):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", audio_path]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

def render_dynamic_scene(slide, t, duration):
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (WIDTH, 14)], fill="#0284C7")
    
    idle_float = int(math.sin(t * 3.0) * 8)
    cards = slide["cards"]
    
    # 4 Dynamic Scenes based on exact card timings
    # Scene 1: 0.0 to Card 1 start + duration
    t1_end = cards[1]["start"] if len(cards) > 1 else duration * 0.25
    t2_end = cards[2]["start"] if len(cards) > 2 else duration * 0.50
    t3_end = cards[3]["start"] if len(cards) > 3 else duration * 0.75
    
    # ==========================================
    # SCENE 1: Intro & Scope
    # ==========================================
    if t < t1_end:
        p = min(1.0, t / 0.7)
        scale = ease_out_back(p)
        
        draw.text((160, 140), slide["category"], fill="#0284C7", font=get_font(24, bold=True))
        draw.text((160, 190), slide["title"], fill="#0F172A", font=get_font(60, bold=True))
        draw.text((160, 275), slide["subtitle"], fill="#475569", font=get_font(28))
        
        # Centered Tank
        filled_vector_assets.draw_filled_dairy_tank(draw, 1420, 560, scale=1.4 * scale, float_offset=idle_float)
        
        # Card 1 Staggered Entrance
        c1 = cards[0]
        if t >= c1["start"]:
            p1 = min(1.0, (t - c1["start"]) / 0.6)
            s1 = ease_out_back(p1)
            y_c1 = 390
            draw.rounded_rectangle([(160, y_c1), (960, y_c1 + 140)], radius=18, fill="#FFFFFF", outline="#0284C7", width=2)
            draw.rectangle([(160, y_c1), (175, y_c1 + 140)], fill="#0284C7")
            draw.text((205, y_c1 + 25), c1["tag"], fill="#0369A1", font=get_font(20, bold=True))
            draw.text((205, y_c1 + 65), c1["text"], fill="#0F172A", font=get_font(24, bold=True))

    # ==========================================
    # SCENE 2: Core Hazard & Control
    # ==========================================
    elif t < t2_end:
        st = t - t1_end
        c2 = cards[1] if len(cards) > 1 else cards[0]
        draw.text((140, 130), "KEY CONTROL FOCUS", fill="#0284C7", font=get_font(24, bold=True))
        draw.text((140, 175), c2["text"], fill="#0F172A", font=get_font(52, bold=True))
        
        # 3 Pillar Cards with Icons
        pillars = [
            ("BIOLOGICAL RISKS", "Pathogen Elimination\nListeria & Salmonella", filled_vector_assets.draw_filled_microbe, "#EF4444", 0.0),
            ("CHEMICAL RISKS", "CIP Chemical Control\nSanitiser Residues", filled_vector_assets.draw_filled_chemical_bottle, "#F59E0B", 1.0),
            ("PHYSICAL RISKS", "Foreign Body Control\nMetal & Fine Filtration", filled_vector_assets.draw_filled_filter_gear, "#0284C7", 2.0)
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
                draw.rounded_rectangle([(x, y), (x + card_w, y + card_h)], radius=20, fill="#FFFFFF", outline=col, width=2)
                draw.rectangle([(x, y), (x + card_w, y + 14)], fill=col)
                item_float = int(math.sin((t + i) * 3.0) * 6)
                draw_func(draw, x + card_w // 2, y + 150, scale=1.0 * p_scale, float_offset=item_float)
                draw.text((x + 35, y + 270), title, fill=col, font=get_font(24, bold=True))
                desc_y = y + 325
                for line in desc.split("\n"):
                    draw.text((x + 35, desc_y), line, fill="#0F172A", font=get_font(26, bold=True))
                    desc_y += 38

    # ==========================================
    # SCENE 3: Consumer Protection & Standards
    # ==========================================
    elif t < t3_end:
        st = t - t2_end
        p = min(1.0, st / 0.7)
        scale = ease_out_back(p)
        c3 = cards[2] if len(cards) > 2 else cards[-1]
        
        draw.text((140, 130), "STANDARDS & VALUE", fill="#059669", font=get_font(24, bold=True))
        draw.text((140, 175), c3["text"], fill="#0F172A", font=get_font(52, bold=True))
        
        shield_float = int(math.sin(t * 3.0) * 8)
        filled_vector_assets.draw_filled_quality_shield(draw, 450, 560, scale=1.5 * scale, float_offset=shield_float)
        
        # Perfectly Centered Text below shield
        layout_utils.draw_centered_text(draw, "VERIFIED FOOD SAFETY", 450, 750, get_font(24, bold=True), "#059669")
        
        hero = slide["hero"]
        draw.rounded_rectangle([(780, 310), (1780, 540)], radius=18, fill="#FFFFFF", outline="#10B981", width=2)
        draw.rectangle([(780, 310), (795, 540)], fill="#10B981")
        draw.text((830, 345), "OPERATIONAL MISSION", fill="#059669", font=get_font(22, bold=True))
        draw.text((830, 395), hero["mission"], fill="#0F172A", font=get_font(34, bold=True))
        
        draw.rounded_rectangle([(780, 580), (1780, 810)], radius=18, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(780, 580), (795, 810)], fill="#0284C7")
        draw.text((830, 615), "REGULATORY FRAMEWORK", fill="#0369A1", font=get_font(22, bold=True))
        draw.text((830, 665), hero["meta"], fill="#0F172A", font=get_font(26, bold=True))

    # ==========================================
    # SCENE 4: End-to-End Operational Flow & Perfectly Centered Close
    # ==========================================
    else:
        st = t - t3_end
        draw.text((140, 130), "OPERATIONAL RIGOUR", fill="#4F46E5", font=get_font(24, bold=True))
        draw.text((140, 175), "Safety Built into Every Processing Stage", fill="#0F172A", font=get_font(52, bold=True))
        
        nodes = [
            ("1. RAW INTAKE", "Milk Reception Deck\nFine 1000µm Filtration", "#0284C7", 0.0),
            ("2. PASTEURISATION", "HTST Thermal Bays\n>72°C Continuous Kill", "#EF4444", 0.8),
            ("3. PACKAGING", "Cheese & Yogurt Lines\nMetal Detection", "#F59E0B", 1.6),
            ("4. QUALITY LAB", "Batch KPI Testing\nTotal Verification", "#10B981", 2.4)
        ]
        
        node_w = 360
        node_h = 390
        start_x = 140
        gap = 53
        y = 290
        
        for i, (title, desc, col, delay) in enumerate(nodes):
            if st >= delay:
                p_prog = min(1.0, (st - delay) / 0.5)
                scale = ease_out_back(p_prog)
                x = start_x + i * (node_w + gap)
                
                if i > 0 and st >= delay:
                    arr_x = x - gap + 15
                    draw.polygon([(arr_x, y + 195), (arr_x + 20, y + 185), (arr_x + 20, y + 205)], fill="#94A3B8")
                    
                draw.rounded_rectangle([(x, y), (x + node_w, y + node_h)], radius=18, fill="#FFFFFF", outline=col, width=2)
                draw.rectangle([(x, y), (x + node_w, y + 14)], fill=col)
                
                draw.ellipse([(x + 30, y + 30), (x + 85, y + 85)], fill=col)
                draw.text((x + 47, y + 38), str(i + 1), fill="#FFFFFF", font=get_font(28, bold=True))
                draw.text((x + 30, y + 110), title, fill=col, font=get_font(22, bold=True))
                
                desc_y = y + 165
                for line in desc.split("\n"):
                    draw.text((x + 30, desc_y), line, fill="#0F172A", font=get_font(22, bold=True))
                    desc_y += 35
                    
        # Perfectly Centered Bottom Call to Action Box
        if st >= 3.2:
            box_coords = (140, 750, 1780, 850)
            layout_utils.draw_centered_box_text(
                draw, box_coords,
                "LET'S GET STARTED WITH HACCP EXCELLENCE",
                get_font(30, bold=True),
                fill_text="#38BDF8",
                box_bg="#0F172A",
                radius=14
            )

    # Footer with perfect right alignment
    draw.line([(140, 940), (1780, 940)], fill="#E2E8F0", width=1)
    draw.text((140, 970), f"HACCP Food Safety Masterclass • Module {slide['number']:02d}", fill="#64748B", font=get_font(22))
    draw.text((1600, 970), f"Slide {slide['number']:02d} / 26", fill="#64748B", font=get_font(22))
    
    return img

def render_all_squideo_slides():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(SRT_DIR, exist_ok=True)
    
    cumulative_offset = 0.0
    
    for slide in SLIDES_DATA:
        audio_path = slide["audio"]
        duration = get_audio_duration(audio_path)
        total_frames = int(duration * FPS)
        s_num = f"Slide_{slide['number']:02d}"
        
        out_video = os.path.join(OUTPUT_DIR, f"{s_num}.mp4")
        temp_dir = f"video_test/temp_squideo_{s_num}"
        os.makedirs(temp_dir, exist_ok=True)
        
        print(f"[{slide['number']:02d}/26] Rendering: {slide['title']} (Duration: {duration:.1f}s, Audio Offset: {cumulative_offset:.1f}s)...")
        
        for idx in range(total_frames):
            t = idx / FPS
            f_img = render_dynamic_scene(slide, t, duration)
            f_img.save(os.path.join(temp_dir, f"frame_{idx:05d}.jpg"), quality=90)
            
        cmd = [
            "ffmpeg", "-y",
            "-framerate", str(FPS),
            "-i", os.path.join(temp_dir, "frame_%05d.jpg"),
            "-i", audio_path,
            "-ss", str(cumulative_offset), "-stream_loop", "-1", "-i", BG_MUSIC,
            "-filter_complex", "[1:a]volume=1.0[v_speech];[2:a]volume=0.10[v_music];[v_speech][v_music]amix=inputs=2:duration=first:dropout_transition=2[a_out]",
            "-map", "0:v", "-map", "[a_out]",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            out_video
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        for f in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, f))
        os.rmdir(temp_dir)
        print(f"✅ Generated: {out_video}")
        
        cumulative_offset += duration

    print("\n🎉 ALL 26 SQUIDEO PRAISE EDITION VIDEOS RENDERED WITH PERFECT SYNC & SEAMLESS AUDIO!")

if __name__ == "__main__":
    render_all_squideo_slides()
