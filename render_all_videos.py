import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont
from slides_metadata import SLIDES_DATA

WIDTH, HEIGHT = 1920, 1080
FPS = 25
BG_MUSIC = "video_test/ambient_bg_music_long.wav"
OUTPUT_DIR = "video_test/all_slides_videos"
SRT_DIR = "video_test/all_slides_subtitles"

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

def get_audio_duration(audio_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        audio_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

def typewriter_text(full_text, current_time, start_time, end_time):
    if current_time < start_time:
        return ""
    if current_time >= end_time:
        return full_text
    prog = (current_time - start_time) / max(0.1, (end_time - start_time))
    visible_chars = int(len(full_text) * prog)
    return full_text[:visible_chars]

def render_slide_frame(slide, t, duration):
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    
    # Top Accent Bar
    draw.rectangle([(0, 0), (WIDTH, 12)], fill="#0284C7")
    
    # Category & Title
    cat_text = typewriter_text(slide["category"], t, 0.0, 1.2)
    title_text = typewriter_text(slide["title"], t, 0.5, 2.5)
    sub_text = typewriter_text(slide["subtitle"], t, 1.5, 4.0)
    
    if cat_text:
        draw.text((140, 140), cat_text, fill="#0369A1", font=get_font(22, bold=True))
    if title_text:
        draw.text((140, 180), title_text, fill="#0F172A", font=get_font(48, bold=True))
    if sub_text:
        draw.text((140, 245), sub_text, fill="#475569", font=get_font(26))
        
    # 4 Structured Left Cards
    y_card = 315
    for i, c in enumerate(slide["cards"]):
        card_start = c["start"]
        card_end = c["end"]
        
        if t >= card_start:
            draw.rounded_rectangle([(140, y_card), (140 + 1040, y_card + 115)], radius=12, fill="#FFFFFF", outline="#E2E8F0", width=2)
            colors = ["#0284C7", "#0EA5E9", "#10B981", "#6366F1"]
            draw.rectangle([(140, y_card), (152, y_card + 115)], fill=colors[i % len(colors)])
            
            tag_typed = typewriter_text(c["tag"], t, card_start, card_start + 0.8)
            draw.text((175, y_card + 18), tag_typed, fill=colors[i % len(colors)], font=get_font(18, bold=True))
            
            text_typed = typewriter_text(c["text"], t, card_start + 0.4, card_end)
            draw.text((175, y_card + 52), text_typed, fill="#1E293B", font=get_font(24, bold=True))
            
        y_card += 135
        
    # Right Hero Highlight Panel
    hero = slide["hero"]
    h_start = hero["start"]
    if t >= h_start:
        draw.rounded_rectangle([(1230, 315), (1780, 850)], radius=16, fill="#F0F9FF", outline="#0284C7", width=2)
        draw.rectangle([(1230, 315), (1780, 330)], fill="#0284C7")
        
        draw.text((1275, 370), "KEY TAKEAWAY", fill="#0369A1", font=get_font(20, bold=True))
        
        m_typed = typewriter_text(hero["mission"], t, h_start + 0.4, h_start + 4.0)
        draw.text((1275, 420), m_typed, fill="#0F172A", font=get_font(36, bold=True))
        
        draw.line([(1275, 560), (1735, 560)], fill="#BAE6FD", width=1)
        
        meta_typed = typewriter_text(hero["meta"], t, h_start + 2.0, h_start + 6.0)
        draw.text((1275, 600), meta_typed, fill="#334155", font=get_font(22))
        
    # Footer
    draw.line([(140, 940), (1780, 940)], fill="#E2E8F0", width=1)
    draw.text((140, 970), f"HACCP Food Safety Masterclass • Module {slide['number']:02d}", fill="#64748B", font=get_font(22))
    draw.text((1600, 970), f"Slide {slide['number']:02d} / 26", fill="#64748B", font=get_font(22))
    
    # Ultra-smooth continuous slow zoom - Zero Shake
    zoom = 1.0 + 0.025 * (t / max(1.0, duration))
    crop_w = int(WIDTH / zoom)
    crop_h = int(HEIGHT / zoom)
    left = (WIDTH - crop_w) // 2
    top = (HEIGHT - crop_h) // 2
    
    img_zoomed = img.crop((left, top, left + crop_w, top + crop_h)).resize((WIDTH, HEIGHT), Image.Resampling.BILINEAR)
    return img_zoomed

def generate_srt_file(slide, duration, srt_path):
    with open(srt_path, "w", encoding="utf-8") as f:
        block_idx = 1
        f.write(f"{block_idx}\n00:00:00,000 --> 00:00:03,500\n{slide['title']} - {slide['subtitle']}\n\n")
        block_idx += 1
        
        for c in slide["cards"]:
            s_sec = int(c["start"])
            s_ms = int((c["start"] - s_sec) * 1000)
            e_sec = int(min(duration, c["end"]))
            e_ms = int((min(duration, c["end"]) - e_sec) * 1000)
            f.write(f"{block_idx}\n{s_sec//3600:02d}:{(s_sec%3600)//60:02d}:{s_sec%60:02d},{s_ms:03d} --> {e_sec//3600:02d}:{(e_sec%3600)//60:02d}:{e_sec%60:02d},{e_ms:03d}\n{c['text']}\n\n")
            block_idx += 1

def render_single_slide(slide):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(SRT_DIR, exist_ok=True)
    
    audio_path = slide["audio"]
    duration = get_audio_duration(audio_path)
    total_frames = int(duration * FPS)
    slide_num_str = f"Slide_{slide['number']:02d}"
    out_video = os.path.join(OUTPUT_DIR, f"{slide_num_str}.mp4")
    out_srt = os.path.join(SRT_DIR, f"{slide_num_str}.srt")
    
    if os.path.exists(out_video) and os.path.getsize(out_video) > 100000:
        print(f"[{slide['number']:02d}/26] Already rendered: {slide['title']}. Skipping to next...")
        return
        
    temp_frames_dir = f"video_test/temp_frames_{slide_num_str}"
    os.makedirs(temp_frames_dir, exist_ok=True)
    
    print(f"[{slide['number']:02d}/26] Rendering: {slide['title']} (Duration: {duration:.1f}s, Frames: {total_frames})...")
    generate_srt_file(slide, duration, out_srt)
    
    for idx in range(total_frames):
        t = idx / FPS
        f_img = render_slide_frame(slide, t, duration)
        f_img.save(os.path.join(temp_frames_dir, f"frame_{idx:05d}.jpg"), quality=88)
        
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", os.path.join(temp_frames_dir, "frame_%05d.jpg"),
        "-i", audio_path,
        "-stream_loop", "-1", "-i", BG_MUSIC,
        "-filter_complex", "[1:a]volume=1.0[v_speech];[2:a]volume=0.10[v_music];[v_speech][v_music]amix=inputs=2:duration=first:dropout_transition=2[a_out]",
        "-map", "0:v", "-map", "[a_out]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "ultrafast", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        out_video
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    for f in os.listdir(temp_frames_dir):
        os.remove(os.path.join(temp_frames_dir, f))
    os.rmdir(temp_frames_dir)
    print(f"✅ Finished: {out_video}")

if __name__ == "__main__":
    for s in SLIDES_DATA:
        render_single_slide(s)
    print("\n🎉 ALL 26 VIDEOS AND SUBTITLES RENDERED SUCCESSFULLY!")
