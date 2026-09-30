import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1920, 1080
FPS = 30
DURATION = 36.1 # Seconds (Slide 1 audio length)
TOTAL_FRAMES = int(DURATION * FPS)
FRAMES_DIR = "video_test/dynamic_frames"
OUTPUT_VIDEO = "video_test/rendered_videos/Slide_01_Dynamic_Clean_White.mp4"
AUDIO_FILE = "audio_output/libby_energetic_british/Slide_01_Welcome_Course_Title.mp3"
BG_MUSIC = "video_test/ambient_bg_music.wav"

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

def ease_out_cubic(t):
    return 1 - pow(1 - t, 3)

def render_frame(frame_idx):
    t = frame_idx / FPS
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    
    # Top Accent Bar
    draw.rectangle([(0, 0), (WIDTH, 12)], fill="#0284C7")
    
    # Header reveal (0.0 to 1.5s)
    h_alpha = min(1.0, max(0.0, t / 1.0))
    if h_alpha > 0:
        h_offset = int((1 - ease_out_cubic(h_alpha)) * -30)
        draw.text((140, 150 + h_offset), "HACCP LEVEL 2 TRAINING", fill="#0369A1", font=get_font(24, bold=True))
        draw.text((140, 195 + h_offset), "Food Safety & Dairy Processing Excellence", fill="#0F172A", font=get_font(52, bold=True))
        draw.text((140, 265 + h_offset), "Essential standards for liquid milk, cheese, yogurt and dairy manufacturing", fill="#475569", font=get_font(28))

    # Card 1: Tailored for Dairy (04.0s)
    c1_start = 3.5
    if t >= c1_start:
        c1_prog = min(1.0, (t - c1_start) / 0.6)
        c1_e = ease_out_cubic(c1_prog)
        c1_x = int(140 - (1 - c1_e) * 40)
        # Highlight pulse if just entered
        shake = int(math.sin(c1_prog * math.pi * 4) * 3) if c1_prog < 0.8 else 0
        draw.rounded_rectangle([(c1_x, 340 + shake), (c1_x + 1040, 445 + shake)], radius=12, fill="#FFFFFF", outline="#0284C7", width=2)
        draw.rectangle([(c1_x, 340 + shake), (c1_x + 12, 445 + shake)], fill="#0284C7")
        draw.text((c1_x + 40, 360 + shake), "DAIRY INDUSTRY ADAPTATION", fill="#0369A1", font=get_font(18, bold=True))
        draw.text((c1_x + 40, 390 + shake), "Tailored for Liquid Milk, Cheese, Yogurt & Packing Halls", fill="#1E293B", font=get_font(24, bold=True))

    # Card 2: Hazard Prevention (08.5s)
    c2_start = 8.2
    if t >= c2_start:
        c2_prog = min(1.0, (t - c2_start) / 0.6)
        c2_e = ease_out_cubic(c2_prog)
        c2_x = int(140 - (1 - c2_e) * 40)
        draw.rounded_rectangle([(c2_x, 470), (c2_x + 1040, 575)], radius=12, fill="#FFFFFF", outline="#E2E8F0", width=2)
        draw.rectangle([(c2_x, 470), (c2_x + 12, 575)], fill="#0EA5E9")
        draw.text((c2_x + 40, 490), "PROACTIVE HAZARD CONTROL", fill="#0369A1", font=get_font(18, bold=True))
        draw.text((c2_x + 40, 520), "Prevent, Reduce & Eliminate Biological, Physical & Chemical Risks", fill="#1E293B", font=get_font(24, bold=True))

    # Card 3: Consumer Protection & Law (16.5s)
    c3_start = 16.0
    if t >= c3_start:
        c3_prog = min(1.0, (t - c3_start) / 0.6)
        c3_e = ease_out_cubic(c3_prog)
        c3_x = int(140 - (1 - c3_e) * 40)
        draw.rounded_rectangle([(c3_x, 600), (c3_x + 1040, 705)], radius=12, fill="#FFFFFF", outline="#E2E8F0", width=2)
        draw.rectangle([(c3_x, 600), (c3_x + 12, 705)], fill="#10B981")
        draw.text((c3_x + 40, 620), "CONSUMER TRUST & STATUTORY LAW", fill="#059669", font=get_font(18, bold=True))
        draw.text((c3_x + 40, 650), "Guaranteed Safety for Millions of Daily Consumers Across the UK", fill="#1E293B", font=get_font(24, bold=True))

    # Card 4: Shared Responsibility & Across Plant (23.5s)
    c4_start = 23.0
    if t >= c4_start:
        c4_prog = min(1.0, (t - c4_start) / 0.6)
        c4_e = ease_out_cubic(c4_prog)
        c4_x = int(140 - (1 - c4_e) * 40)
        draw.rounded_rectangle([(c4_x, 730), (c4_x + 1040, 835)], radius=12, fill="#FFFFFF", outline="#E2E8F0", width=2)
        draw.rectangle([(c4_x, 730), (c4_x + 12, 835)], fill="#6366F1")
        draw.text((c4_x + 40, 750), "END-TO-END OPERATIONAL ENGAGEMENT", fill="#4F46E5", font=get_font(18, bold=True))
        draw.text((c4_x + 40, 780), "From Raw Milk Intake & Pasteurisation to Lab Quality Assurance", fill="#1E293B", font=get_font(24, bold=True))

    # Right Hero Highlight Card (Reveals at 20.0s with zoom bump)
    r_start = 19.5
    if t >= r_start:
        r_prog = min(1.0, (t - r_start) / 0.7)
        r_e = ease_out_cubic(r_prog)
        scale = 0.95 + 0.05 * r_e
        r_x = int(1230 + (1 - r_e) * 50)
        draw.rounded_rectangle([(r_x, 340), (r_x + 550, 835)], radius=16, fill="#F0F9FF", outline="#0284C7", width=2)
        draw.rectangle([(r_x, 340), (r_x + 550, 355)], fill="#0284C7")
        draw.text((r_x + 45, 395), "OPERATIONAL MISSION", fill="#0369A1", font=get_font(20, bold=True))
        draw.text((r_x + 45, 445), "Zero Contamination.", fill="#0F172A", font=get_font(38, bold=True))
        draw.text((r_x + 45, 495), "100% Compliance.", fill="#0284C7", font=get_font(38, bold=True))
        draw.line([(r_x + 45, 575), (r_x + 505, 575)], fill="#BAE6FD", width=1)
        draw.text((r_x + 45, 610), "Certification Standard: Level 2", fill="#334155", font=get_font(22, bold=True))
        draw.text((r_x + 45, 650), "Regulation: (EC) No 852/2004", fill="#475569", font=get_font(20))
        draw.text((r_x + 45, 690), "Voice Narration: Libby (en-GB)", fill="#475569", font=get_font(20))
        draw.text((r_x + 45, 730), "Industry: Food & Dairy Processing", fill="#0369A1", font=get_font(20, bold=True))

    # Footer Progress & Info
    draw.line([(140, 940), (1780, 940)], fill="#E2E8F0", width=1)
    draw.text((140, 970), "HACCP Food Safety Masterclass • Module 1 : Welcome", fill="#64748B", font=get_font(22))
    draw.text((1600, 970), "Slide 01 / 26", fill="#64748B", font=get_font(22))
    
    # Apply continuous camera zoom (from 1.0 to 1.05)
    zoom = 1.0 + 0.04 * (t / DURATION)
    # Apply subtle camera shake/emphasis at entry points (e.g. 4.0s, 16.5s, 24s)
    shake_x = 0
    shake_y = 0
    for burst in [4.0, 8.5, 16.5, 23.5]:
        if 0 <= (t - burst) < 0.35:
            d_t = (t - burst) / 0.35
            shake_x = int(math.sin(d_t * math.pi * 6) * 4 * (1 - d_t))
            shake_y = int(math.cos(d_t * math.pi * 6) * 3 * (1 - d_t))

    # Crop and rescale for smooth continuous zoom
    crop_w = int(WIDTH / zoom)
    crop_h = int(HEIGHT / zoom)
    left = (WIDTH - crop_w) // 2 + shake_x
    top = (HEIGHT - crop_h) // 2 + shake_y
    right = left + crop_w
    bottom = top + crop_h
    
    img_zoomed = img.crop((left, top, right, bottom)).resize((WIDTH, HEIGHT), Image.Resampling.BILINEAR)
    return img_zoomed

def main():
    os.makedirs(FRAMES_DIR, exist_ok=True)
    os.makedirs("video_test/rendered_videos", exist_ok=True)
    
    print(f"Generating {TOTAL_FRAMES} dynamic motion frames at {FPS} FPS...")
    for idx in range(TOTAL_FRAMES):
        if idx % 150 == 0 or idx == TOTAL_FRAMES - 1:
            print(f"Progress: frame {idx}/{TOTAL_FRAMES} ({(idx/TOTAL_FRAMES)*100:.1f}%)")
        frame_img = render_frame(idx)
        frame_img.save(os.path.join(FRAMES_DIR, f"frame_{idx:05d}.jpg"), quality=90)
        
    print("\nEncoding dynamic video with FFmpeg...")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", os.path.join(FRAMES_DIR, "frame_%05d.jpg"),
        "-i", AUDIO_FILE,
        "-i", BG_MUSIC,
        "-filter_complex", "[1:a]volume=1.0[v_speech];[2:a]volume=0.12[v_music];[v_speech][v_music]amix=inputs=2:duration=first:dropout_transition=2[a_out]",
        "-map", "0:v", "-map", "[a_out]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        OUTPUT_VIDEO
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ Dynamic video rendered: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    main()
