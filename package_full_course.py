import os
import subprocess
import zipfile

CLIPS_DIR = "video_test/master_v2_clips"
BG_MUSIC = "video_test/upbeat_bg_music.wav"
OUTPUT_MP4 = "video_test/HACCP_Level_2_Masterclass_Complete.mp4"
OUTPUT_SRT = "video_test/HACCP_Level_2_Full_Course.srt"
OUTPUT_ZIP = "video_test/HACCP_Level_2_Masterclass_Complete.zip"

def create_master_video():
    clips = [
        os.path.join(CLIPS_DIR, f"master_v2_slide_{i:02d}.mp4")
        for i in range(1, 27)
    ]
    for clip in clips:
        if not os.path.isfile(clip):
            raise FileNotFoundError(f"Missing required clip: {clip}")

    concat_list = "video_test/temp_concat_list.txt"
    with open(concat_list, "w") as f:
        for clip in clips:
            f.write(f"file '{os.path.abspath(clip)}'\n")

    temp_concat = "video_test/temp_concat_video.mp4"
    print(f"--> Concatenating {len(clips)} slide clips...")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list, "-c", "copy", temp_concat],
        check=True
    )

    print("--> Mixing background music (volume 0.10)...")
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
        OUTPUT_MP4
    ]
    subprocess.run(mix_cmd, check=True)

    if os.path.exists(temp_concat):
        os.remove(temp_concat)
    if os.path.exists(concat_list):
        os.remove(concat_list)
    print(f"--> Master MP4 ready: {OUTPUT_MP4}")

def create_zip_package():
    print(f"--> Creating distribution ZIP package: {OUTPUT_ZIP}...")
    if not os.path.isfile(OUTPUT_MP4):
        raise FileNotFoundError(f"Master MP4 not found: {OUTPUT_MP4}")
    if not os.path.isfile(OUTPUT_SRT):
        raise FileNotFoundError(f"Master SRT not found: {OUTPUT_SRT}")

    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(OUTPUT_MP4, arcname="HACCP_Level_2_Masterclass_Complete.mp4")
        zip_file.write(OUTPUT_SRT, arcname="HACCP_Level_2_Full_Course.srt")

    size_mb = os.path.getsize(OUTPUT_ZIP) / (1024 * 1024)
    print(f"--> Successfully packaged ZIP: {OUTPUT_ZIP} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    create_master_video()
    create_zip_package()
