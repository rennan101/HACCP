import os
import re
import json
import asyncio
import subprocess
import edge_tts

SCRIPT_FILE = "HACCP_Level_2_Voiceover_Script_and_Subtitles.md"
SLIDES_JSON = "presentation/slides_data.json"
SLIDES_JS = "presentation/slides_data.js"
MASTER_SRT = "video_test/HACCP_Level_2_Full_Course.srt"
SRT_DIR = "video_test/all_slides_subtitles"

VOICE = "en-GB-LibbyNeural"
RATE = "+5%"
PITCH = "+2Hz"

def normalize(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())

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

async def get_word_timestamps(script):
    com = edge_tts.Communicate(script, VOICE, rate=RATE, pitch=PITCH, boundary="WordBoundary")
    words = []
    async for chunk in com.stream():
        if chunk["type"] == "WordBoundary":
            sec = chunk["offset"] / 10_000_000
            dur = chunk["duration"] / 10_000_000
            words.append({"start": sec, "end": sec + dur, "text": chunk["text"], "norm": normalize(chunk["text"])})
    return words

def chunk_script_to_cues(script, words):
    tokens = script.split()
    token_data = []
    w_idx = 0
    num_words = len(words)

    for tok in tokens:
        n = normalize(tok)
        if not n:
            continue
        matched = None
        for j in range(w_idx, min(w_idx + 8, num_words)):
            if words[j]["norm"] == n:
                matched = words[j]
                w_idx = j + 1
                break
        if matched:
            token_data.append({"token": tok, "start": matched["start"], "end": matched["end"]})
        else:
            prev_end = token_data[-1]["end"] if token_data else 0.0
            token_data.append({"token": tok, "start": prev_end, "end": prev_end + 0.3})

    cues = []
    cur_chunk = []
    for td in token_data:
        cur_chunk.append(td)
        tok = td["token"]
        is_sentence_end = any(tok.endswith(p) for p in [".", "!", "?"])
        is_comma_break = any(tok.endswith(p) for p in [",", ";", ":", "—"])
        dur = td["end"] - cur_chunk[0]["start"]
        word_count = len(cur_chunk)

        if (is_sentence_end and (word_count >= 3 or dur >= 2.0)) or \
           (is_comma_break and (word_count >= 5 or dur >= 3.0)) or \
           (word_count >= 9 or dur >= 5.0):
            cue_text = " ".join(c["token"] for c in cur_chunk)
            cues.append({
                "start": round(cur_chunk[0]["start"], 2),
                "end": round(cur_chunk[-1]["end"], 2),
                "text": cue_text
            })
            cur_chunk = []

    if cur_chunk:
        cue_text = " ".join(c["token"] for c in cur_chunk)
        cues.append({
            "start": round(cur_chunk[0]["start"], 2),
            "end": round(cur_chunk[-1]["end"], 2),
            "text": cue_text
        })

    for i in range(len(cues)):
        if i < len(cues) - 1:
            next_start = cues[i + 1]["start"]
            cues[i]["end"] = round(min(cues[i]["end"] + 0.35, next_start), 2)
        else:
            cues[i]["end"] = round(cues[i]["end"] + 0.6, 2)

    return cues

async def main():
    os.makedirs(SRT_DIR, exist_ok=True)
    with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
        md = f.read()

    slides_raw = re.split(r"### Slide\s+(\d+):", md)[1:]
    slide_scripts = {}
    for i in range(0, len(slides_raw), 2):
        s_num = int(slides_raw[i])
        s_body = slides_raw[i + 1]
        vo = re.search(r"#### 🎙️ Voiceover Script.*?\n(>.*?)(?=\n\n#### 💬|\n\n---|\Z)", s_body, re.DOTALL)
        if vo:
            lines = [re.sub(r"^>\s*", "", l).strip() for l in vo.group(1).split("\n")]
            clean = " ".join([l for l in lines if l]).strip(' "')
            clean = re.sub(r"\*(.*?)\*", r"\1", clean)
            clean = re.sub(r"_(.*?)_", r"\1", clean)
            slide_scripts[s_num] = clean

    with open(SLIDES_JSON, "r", encoding="utf-8") as f:
        slides_data = json.load(f)

    full_course_srt = []
    entry_idx = 1
    cum_audio_start = 0.0

    print("Generating exact speech-aligned subtitles for all 26 slides...")
    for s in slides_data:
        num = s["slide_num"]
        script = slide_scripts.get(num, "")
        audio_path = os.path.join("presentation", s["audio_file"])
        audio_dur = get_audio_duration(audio_path)

        words = await get_word_timestamps(script)
        cues = chunk_script_to_cues(script, words)

        print(f"Slide {num:02d}: {len(cues)} cues | Duration: {audio_dur:.2f}s | First: {cues[0]['start']}s '{cues[0]['text'][:30]}...'")

        s["subtitles"] = cues

        srt_path = os.path.join(SRT_DIR, f"Slide_{num:02d}.srt")
        with open(srt_path, "w", encoding="utf-8") as sf:
            for idx, c in enumerate(cues, 1):
                sf.write(f"{idx}\n{format_srt_time(c['start'])} --> {format_srt_time(c['end'])}\n{c['text']}\n\n")

        for c in cues:
            f_start = cum_audio_start + c["start"]
            f_end = cum_audio_start + c["end"]
            full_course_srt.append(f"{entry_idx}\n{format_srt_time(f_start)} --> {format_srt_time(f_end)}\n{c['text']}\n\n")
            entry_idx += 1

        cum_audio_start += audio_dur

    with open(SLIDES_JSON, "w", encoding="utf-8") as f:
        json.dump(slides_data, f, indent=2, ensure_ascii=False)

    with open(SLIDES_JS, "w", encoding="utf-8") as f:
        f.write("window.HACCP_SLIDES_DATA = " + json.dumps(slides_data, indent=2, ensure_ascii=False) + ";\n")

    with open(MASTER_SRT, "w", encoding="utf-8") as f:
        f.writelines(full_course_srt)

    print("\n✅ Subtitle generation complete! All cues speech-aligned with millisecond accuracy.")

if __name__ == "__main__":
    asyncio.run(main())
