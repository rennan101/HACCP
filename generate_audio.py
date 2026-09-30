import os
import re
import sys
import requests
import asyncio
import edge_tts

SCRIPT_FILE = "HACCP_Level_2_Voiceover_Script_and_Subtitles.md"
OUTPUT_DIR = "audio_output"

# ElevenLabs voice ID for "Alice" (British, confident, educator)
# Default Alice Voice ID in ElevenLabs library: Xb7hH8MSUJpSbSDYk0k2
ALICE_VOICE_ID = "Xb7hH8MSUJpSbSDYk0k2"

def parse_markdown_slides(filepath):
    """Parses markdown file and extracts slide titles and voiceover scripts."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by slide header
    slides_raw = re.split(r"### Slide (\d+):", content)
    slides = []
    
    # slides_raw has structure: [preamble, "1", slide_1_content, "2", slide_2_content, ...]
    for i in range(1, len(slides_raw), 2):
        slide_num = int(slides_raw[i])
        slide_body = slides_raw[i+1]
        
        # Extract title
        title_match = re.search(r"^\s*(.+?)\n", slide_body)
        title = title_match.group(1).strip() if title_match else f"Slide {slide_num}"
        
        # Extract Voiceover Script (between > quotes)
        vo_match = re.search(r"#### 🎙️ Voiceover Script.*?\n(>.*?)(?=\n\n#### 💬|\n\n---|\Z)", slide_body, re.DOTALL)
        if vo_match:
            raw_script = vo_match.group(1)
            # Clean blockquote > markers and excess newlines
            clean_lines = [re.sub(r"^>\s*", "", line).strip() for line in raw_script.split("\n")]
            clean_script = " ".join([l for l in clean_lines if l])
            # Clean markdown formatting like *Listeria* -> Listeria
            clean_script = re.sub(r"\*(.*?)\*", r"\1", clean_script)
            clean_script = re.sub(r"_(.*?)_", r"\1", clean_script)
            slides.append({
                "number": slide_num,
                "title": title,
                "script": clean_script
            })
            
    return slides

def generate_elevenlabs(text, output_path, api_key, voice_id=ALICE_VOICE_ID):
    """Generates MP3 using ElevenLabs TTS API."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.50,
            "similarity_boost": 0.80,
            "style": 0.15,
            "use_speaker_boost": True
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        return True, "Success"
    else:
        return False, f"ElevenLabs API Error {response.status_code}: {response.text}"

async def generate_edge_tts(text, output_path, voice="en-GB-SoniaNeural"):
    """Fallback generator using High-Quality British English Neural TTS."""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    slides = parse_markdown_slides(SCRIPT_FILE)
    
    print(f"Loaded {len(slides)} slides from {SCRIPT_FILE}")
    
    # Process first 3 slides
    target_slides = slides[:3]
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    
    for slide in target_slides:
        out_file = os.path.join(OUTPUT_DIR, f"Slide_{slide['number']:02d}_{slide['title'].replace(' ', '_').replace('&', 'and')[:30]}.mp3")
        print(f"\n--- Generating Audio for Slide {slide['number']}: {slide['title']} ---")
        print(f"Text length: {len(slide['script'])} characters")
        print(f"Sample: {slide['script'][:120]}...")
        
        if api_key:
            print("Using ElevenLabs API (Alice - British Educator)...")
            success, msg = generate_elevenlabs(slide['script'], out_file, api_key, ALICE_VOICE_ID)
            if success:
                print(f"Saved: {out_file}")
                continue
            else:
                print(f"ElevenLabs failed: {msg}")
                print("Falling back to Edge-TTS Sonia (British Neural)...")
        else:
            print("No ELEVENLABS_API_KEY detected in environment.")
            print("Generating with British Neural Voice (en-GB-SoniaNeural - Clear Educator)...")
            
        asyncio.run(generate_edge_tts(slide['script'], out_file, voice="en-GB-SoniaNeural"))
        print(f"Saved: {out_file}")

    print("\nGeneration completed successfully!")
    print(f"Audio files saved in: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    main()
