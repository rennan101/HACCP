import os
import re
import json
import subprocess

def parse_time(t_str):
    parts = t_str.strip().split(":")
    return float(parts[0]) * 60 + float(parts[1])

def format_srt_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    ms = int(round((sec - int(sec)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def get_audio_duration(path):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", path]
    return float(subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True).stdout.strip())

def main():
    with open("HACCP_Level_2_Voiceover_Script_and_Subtitles.md", "r", encoding="utf-8") as f:
        md_content = f.read()

    slides_raw = re.split(r"### Slide\s+(\d+):", md_content)[1:]
    slide_captions = {}

    for i in range(0, len(slides_raw), 2):
        s_num = int(slides_raw[i])
        s_body = slides_raw[i + 1]
        sub_match = re.search(r"#### [^\n]*Subtitle Captions\s+```(?:text)?(.*?)```", s_body, re.DOTALL)
        if sub_match:
            cues = []
            raw_lines = [l.strip() for l in sub_match.group(1).strip().split("\n") if l.strip()]
            for line in raw_lines:
                m = re.match(r"\[(\d{2}:\d{2})\s*-\s*(\d{2}:\d{2})\]\s*(.*)", line)
                if m:
                    cues.append({
                        "start": parse_time(m.group(1)),
                        "end": parse_time(m.group(2)),
                        "text": m.group(3).strip()
                    })
            slide_captions[s_num] = cues

    with open("presentation/slides_data.json", "r", encoding="utf-8") as f:
        slides_data = json.load(f)

    full_course_srt_entries = []
    entry_idx = 1
    cum_audio_start = 0.0

    for s in slides_data:
        num = s["slide_num"]
        a_path = os.path.join("presentation", s["audio_file"])
        audio_dur = get_audio_duration(a_path)
        cues = slide_captions.get(num, [])

        if cues:
            first_start = cues[0]["start"]
            last_end = cues[-1]["end"]
            raw_span = max(1.0, last_end - first_start)

            scaled_cues = []
            for c in cues:
                rel_s = round((c["start"] - first_start) / raw_span * (audio_dur - 0.3), 2)
                rel_e = round((c["end"] - first_start) / raw_span * (audio_dur - 0.3), 2)
                if rel_e <= rel_s:
                    rel_e = round(rel_s + 2.0, 2)
                txt = c["text"]
                scaled_cues.append({
                    "start": rel_s,
                    "end": rel_e,
                    "text": txt
                })

                full_s = round(cum_audio_start + rel_s, 3)
                full_e = round(cum_audio_start + rel_e, 3)
                full_course_srt_entries.append(
                    f"{entry_idx}\n{format_srt_time(full_s)} --> {format_srt_time(full_e)}\n{txt}\n"
                )
                entry_idx += 1

            s["subtitles"] = scaled_cues

            srt_path = f"video_test/all_slides_subtitles/Slide_{num:02d}.srt"
            with open(srt_path, "w", encoding="utf-8") as sf:
                for s_idx, sc in enumerate(scaled_cues, 1):
                    sf.write(f"{s_idx}\n{format_srt_time(sc['start'])} --> {format_srt_time(sc['end'])}\n{sc['text']}\n\n")

        cum_audio_start += audio_dur

    with open("presentation/slides_data.json", "w", encoding="utf-8") as f:
        json.dump(slides_data, f, indent=2, ensure_ascii=False)

    with open("presentation/slides_data.js", "w", encoding="utf-8") as f:
        f.write("window.HACCP_SLIDES_DATA = " + json.dumps(slides_data, indent=2, ensure_ascii=False) + ";\n")

    with open("video_test/HACCP_Level_2_Full_Course.srt", "w", encoding="utf-8") as f:
        f.write("\n".join(full_course_srt_entries) + "\n")

    print(f"Successfully updated all 26 slides with verbatim spoken captions ({entry_idx - 1} total cues)!")

if __name__ == "__main__":
    main()
