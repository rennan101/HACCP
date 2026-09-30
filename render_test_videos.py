import subprocess
import os

AUDIO_FILE = "audio_output/libby_energetic_british/Slide_01_Welcome_Course_Title.mp3"
BG_MUSIC = "video_test/ambient_bg_music.wav"
OUTPUT_DIR = "video_test/rendered_videos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

STYLES = [
    ("style_1_dark_blue", "video_test/slide_styles/style_1_modern_dark_blue.png"),
    ("style_2_clean_white", "video_test/slide_styles/style_2_modern_clean_white.png"),
    ("style_3_illustrated_cards", "video_test/slide_styles/style_3_illustrated_cards.png")
]

def render():
    for name, img_path in STYLES:
        out_video = os.path.join(OUTPUT_DIR, f"Slide_01_{name}.mp4")
        print(f"Rendering Video: {out_video}...")
        
        # FFmpeg command:
        # 1. Loop slide image
        # 2. Input Libby voiceover audio
        # 3. Input background music (lowered volume to 0.12)
        # 4. Mix voiceover (1.0) + background music (0.12)
        # 5. Output 1080p MP4 synced to exact audio duration
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", img_path,
            "-i", AUDIO_FILE,
            "-i", BG_MUSIC,
            "-filter_complex", "[1:a]volume=1.0[v_speech];[2:a]volume=0.12[v_music];[v_speech][v_music]amix=inputs=2:duration=first:dropout_transition=2[a_out]",
            "-map", "0:v", "-map", "[a_out]",
            "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            out_video
        ]
        
        subprocess.run(cmd, check=True)
        print(f"✅ Rendered: {out_video}")

if __name__ == "__main__":
    render()
