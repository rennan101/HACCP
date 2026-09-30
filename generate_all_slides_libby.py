import os
import re
import asyncio
import edge_tts

SCRIPT_FILE = "HACCP_Level_2_Voiceover_Script_and_Subtitles.md"
OUTPUT_DIR = "audio_output/libby_energetic_british"

# Chosen voice: 1_Libby_Energetic_British
VOICE = "en-GB-LibbyNeural"
RATE = "+5%"
PITCH = "+2Hz"

def parse_markdown_slides(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    slides_raw = re.split(r"### Slide (\d+):", content)
    slides = []
    
    for i in range(1, len(slides_raw), 2):
        slide_num = int(slides_raw[i])
        slide_body = slides_raw[i+1]
        
        title_match = re.search(r"^\s*(.+?)\n", slide_body)
        title = title_match.group(1).strip() if title_match else f"Slide_{slide_num}"
        
        vo_match = re.search(r"#### 🎙️ Voiceover Script.*?\n(>.*?)(?=\n\n#### 💬|\n\n---|\Z)", slide_body, re.DOTALL)
        if vo_match:
            raw_script = vo_match.group(1)
            clean_lines = [re.sub(r"^>\s*", "", line).strip() for line in raw_script.split("\n")]
            clean_script = " ".join([l for l in clean_lines if l])
            # Clean markdown formatting like *Listeria* -> Listeria
            clean_script = re.sub(r"\*(.*?)\*", r"\1", clean_script)
            clean_script = re.sub(r"_(.*?)_", r"\1", clean_script)
            # Remove any trailing / leading quotation marks if present
            clean_script = clean_script.strip(' "')
            slides.append({
                "number": slide_num,
                "title": title,
                "script": clean_script
            })
            
    return slides

def clean_filename(title):
    # Remove unwanted characters for clean filenames
    cleaned = re.sub(r'[^\w\s-]', '', title).strip()
    return re.sub(r'[-\s]+', '_', cleaned)[:40]

async def generate_slide_audio(slide, out_path):
    print(f"[{slide['number']:02d}/26] Generating: Slide {slide['number']} - {slide['title']}...")
    communicate = edge_tts.Communicate(slide['script'], VOICE, rate=RATE, pitch=PITCH)
    await communicate.save(out_path)

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    slides = parse_markdown_slides(SCRIPT_FILE)
    print(f"Loaded {len(slides)} slides from {SCRIPT_FILE}")
    print(f"Voice Profile: {VOICE} | Rate: {RATE} | Pitch: {PITCH}")
    print(f"Output Directory: {os.path.abspath(OUTPUT_DIR)}\n")
    
    tasks = []
    for slide in slides:
        fname = f"Slide_{slide['number']:02d}_{clean_filename(slide['title'])}.mp3"
        out_path = os.path.join(OUTPUT_DIR, fname)
        tasks.append(generate_slide_audio(slide, out_path))
        
    await asyncio.gather(*tasks)
    print(f"\n✅ All {len(slides)} slide audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
