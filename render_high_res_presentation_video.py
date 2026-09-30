import os
import json
import math
import subprocess
from PIL import Image
from video_layout_engine import WIDTH, HEIGHT, render_slide_frame, fit_image_contain

FPS = 25
OUTPUT_DIR = "video_test/master_v2_clips"
FINAL_OUTPUT = "video_test/HACCP_Level_2_Masterclass_Complete.mp4"
BG_MUSIC = "video_test/upbeat_bg_music.wav"

def get_audio_duration(audio_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        audio_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

def render_slide_clip(slide, clip_out_path):
    num = slide["slide_num"]
    audio_path = os.path.join("presentation", slide["audio_file"])
    dur = get_audio_duration(audio_path)
    total_frames = int(math.ceil(dur * FPS))
    clip_dur = total_frames / FPS

    hero_img = None
    if slide.get("image_file"):
        image_path = os.path.join("presentation", slide["image_file"])
        if os.path.isfile(image_path):
            raw = Image.open(image_path).convert("RGB")
            hero_img = fit_image_contain(raw, 820, 500)

    print(f"--> Rendering Slide {num:02d}: {slide['title']} ({total_frames} frames, {clip_dur:.2f}s)")

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-i", audio_path,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "veryfast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        clip_out_path
    ]

    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    try:
        for frame_idx in range(total_frames):
            t = frame_idx / FPS
            frame_img = render_slide_frame(slide, t, clip_dur, hero_img)
            proc.stdin.write(frame_img.tobytes())
    except (BrokenPipeError, IOError):
        pass
    finally:
        try:
            proc.stdin.close()
        except Exception:
            pass
        proc.wait()

    return get_audio_duration(clip_out_path)

def concatenate_and_mix(clip_paths, output_master_path):
    print(f"--> Assembling {len(clip_paths)} clips into Master Course Video...")
    concat_list_file = "video_test/master_v2_concat_list.txt"
    with open(concat_list_file, "w") as f:
        for p in clip_paths:
            f.write(f"file '{os.path.abspath(p)}'\n")

    temp_concat = "video_test/temp_master_v2_concat.mp4"
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list_file, "-c", "copy", temp_concat], check=True)

    print("--> Mixing Upbeat Background Music seamlessly...")
    mix_cmd = [
        "ffmpeg", "-y",
        "-i", temp_concat,
        "-stream_loop", "-1",
        "-i", BG_MUSIC,
        "-filter_complex",
        "[1:a]volume=0.10[bg];[0:a][bg]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        output_master_path
    ]
    subprocess.run(mix_cmd, check=True)

    if os.path.exists(temp_concat):
        os.remove(temp_concat)
    if os.path.exists(concat_list_file):
        os.remove(concat_list_file)
    print(f"--> Master Video Complete: {output_master_path}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open("presentation/slides_data.json", "r", encoding="utf-8") as f:
        slides = json.load(f)

    clip_paths = []
    for slide in slides:
        num = slide["slide_num"]
        out_clip = os.path.join(OUTPUT_DIR, f"master_v2_slide_{num:02d}.mp4")
        render_slide_clip(slide, out_clip)
        clip_paths.append(out_clip)

    concatenate_and_mix(clip_paths, FINAL_OUTPUT)
    print("NEW MASTER COURSE VIDEO GENERATION COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
