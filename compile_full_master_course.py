import os
import sys
import math
import subprocess
from PIL import Image
import slide_render_modules as srm
import filled_vector_assets as fva
import layout_utils
from slides_metadata import SLIDES_DATA

from render_part1 import RENDERERS_PART1
from render_part2 import RENDERERS_PART2
from render_part3 import RENDERERS_PART3
from render_part4 import RENDERERS_PART4

# Combine all 26 slide renderers
ALL_RENDERERS = {}
ALL_RENDERERS.update(RENDERERS_PART1)
ALL_RENDERERS.update(RENDERERS_PART2)
ALL_RENDERERS.update(RENDERERS_PART3)
ALL_RENDERERS.update(RENDERERS_PART4)

WIDTH, HEIGHT = 1920, 1080
FPS = 25
OUTPUT_DIR = "video_test/master_clips"
FINAL_OUTPUT = "video_test/HACCP_Level_2_Full_Master_Course.mp4"
BG_MUSIC = "video_test/ambient_bg_music_long.wav"
CONSOLIDATED_SRT = "video_test/HACCP_Level_2_Full_Course.srt"

def get_audio_duration(audio_path):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", audio_path]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

def format_timestamp_srt(seconds):
    millis = int(round(seconds * 1000))
    hours = millis // 3600000
    millis %= 3600000
    minutes = millis // 60000
    millis %= 60000
    secs = millis // 1000
    millis %= 1000
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def render_slide_clip(slide_data, clip_out_path):
    num = slide_data["number"]
    audio_path = slide_data["audio"]
    dur = get_audio_duration(audio_path)
    total_frames = int(math.ceil(dur * FPS)) + int(FPS * 0.5)  # add 0.5s buffer
    clip_dur = total_frames / FPS
    
    renderer = ALL_RENDERERS.get(num)
    if not renderer:
        raise ValueError(f"No renderer found for slide {num}")
        
    print(f"--> Rendering Slide {num:02d}: {slide_data['title']} ({total_frames} frames, {clip_dur:.2f}s)")
    
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",  # pipe input
        "-i", audio_path,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "veryfast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        clip_out_path
    ]
    
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    try:
        for frame_idx in range(total_frames):
            t = frame_idx / FPS
            img = renderer(t, clip_dur)
            proc.stdin.write(img.tobytes())
    except (BrokenPipeError, IOError):
        pass
    finally:
        try:
            proc.stdin.close()
        except Exception:
            pass
        proc.wait()
        
    actual_dur = get_audio_duration(clip_out_path)
    return actual_dur

def build_master_srt(slides_data, durations, srt_out_path):
    print(f"--> Generating Consolidated Master Subtitles at {srt_out_path}")
    srt_counter = 1
    current_time_offset = 0.0
    
    with open(srt_out_path, "w", encoding="utf-8") as f:
        for idx, slide in enumerate(slides_data):
            num = slide["number"]
            # Read slide individual srt if exists or generate from cards
            slide_srt_file = f"video_test/all_slides_subtitles/Slide_{num:02d}.srt"
            if os.path.exists(slide_srt_file):
                with open(slide_srt_file, "r", encoding="utf-8") as sf:
                    lines = sf.read().strip().split("\n")
                    i = 0
                    while i < len(lines):
                        if lines[i].isdigit():
                            i += 1
                            if i < len(lines) and "-->" in lines[i]:
                                t_parts = lines[i].split(" --> ")
                                # Parse start & end
                                def parse_t(s):
                                    pts = s.replace(",", ".").split(":")
                                    return float(pts[0])*3600 + float(pts[1])*60 + float(pts[2])
                                st = parse_t(t_parts[0]) + current_time_offset
                                et = parse_t(t_parts[1]) + current_time_offset
                                i += 1
                                txt_lines = []
                                while i < len(lines) and lines[i].strip() != "":
                                    txt_lines.append(lines[i])
                                    i += 1
                                f.write(f"{srt_counter}\n")
                                f.write(f"{format_timestamp_srt(st)} --> {format_timestamp_srt(et)}\n")
                                f.write("\n".join(txt_lines) + "\n\n")
                                srt_counter += 1
                        i += 1
            current_time_offset += durations[idx]

def concatenate_and_mix_bg_music(clip_paths, output_master_path):
    print(f"--> Concatenating {len(clip_paths)} clips into Master Course Video...")
    concat_list_file = "video_test/concat_master_list.txt"
    with open(concat_list_file, "w") as f:
        for p in clip_paths:
            f.write(f"file '{os.path.abspath(p)}'\n")
            
    temp_concat_video = "video_test/temp_master_concat.mp4"
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        temp_concat_video
    ]
    subprocess.run(concat_cmd, check=True)
    
    print("--> Mixing Continuous Background Music seamlessly across entire course...")
    mix_cmd = [
        "ffmpeg", "-y",
        "-i", temp_concat_video,
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
    
    if os.path.exists(temp_concat_video):
        os.remove(temp_concat_video)
    if os.path.exists(concat_list_file):
        os.remove(concat_list_file)
    print(f"--> Master Video Complete: {output_master_path}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clip_paths = []
    durations = []
    
    for slide in SLIDES_DATA:
        num = slide["number"]
        clip_path = os.path.join(OUTPUT_DIR, f"master_slide_{num:02d}.mp4")
        if os.path.exists(clip_path) and os.path.getsize(clip_path) > 200000 and num != 18:
            print(f"--> Using cached clip for Slide {num:02d}")
            clip_dur = get_audio_duration(clip_path)
        else:
            clip_dur = render_slide_clip(slide, clip_path)
        clip_paths.append(clip_path)
        durations.append(clip_dur)
        
    build_master_srt(SLIDES_DATA, durations, CONSOLIDATED_SRT)
    concatenate_and_mix_bg_music(clip_paths, FINAL_OUTPUT)
    print("ALL DONE SUCCESSFULLY!")

if __name__ == "__main__":
    main()
