import os
import re
import asyncio
import edge_tts
import requests

SCRIPT_FILE = "HACCP_Level_2_Voiceover_Script_and_Subtitles.md"
OUTPUT_DIR = "audio_output/sunny_voice"

# Selected cheerful/sunny conversational educator voice
# en-US-EmmaMultilingualNeural (Cheerful, clear, upbeat & natural) or en-GB-SoniaNeural / Libby
VOICE_ID = "en-US-EmmaMultilingualNeural"

def parse_markdown_slides(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    slides_raw = re.split(r"### Slide (\d+):", content)
    slides = []
    
    for i in range(1, len(slides_raw), 2):
        slide_num = int(slides_raw[i])
        slide_body = slides_raw[i+1]
        
        title_match = re.search(r"^\s*(.+?)\n", slide_body)
        title = title_match.group(1).strip() if title_match else f"Slide {slide_num}"
        
        vo_match = re.search(r"#### 🎙️ Voiceover Script.*?\n(>.*?)(?=\n\n#### 💬|\n\n---|\Z)", slide_body, re.DOTALL)
        if vo_match:
            raw_script = vo_match.group(1)
            clean_lines = [re.sub(r"^>\s*", "", line).strip() for line in raw_script.split("\n")]
            clean_script = " ".join([l for l in clean_lines if l])
            clean_script = re.sub(r"\*(.*?)\*", r"\1", clean_script)
            clean_script = re.sub(r"_(.*?)_", r"\1", clean_script)
            slides.append({
                "number": slide_num,
                "title": title,
                "script": clean_script
            })
            
    return slides

async def generate_edge_tts(text, output_path, voice=VOICE_ID):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

def generate_elevenlabs_sunny(text, output_path, api_key, voice_id):
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
            "stability": 0.45,
            "similarity_boost": 0.85,
            "style": 0.20,
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

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    slides = parse_markdown_slides(SCRIPT_FILE)
    
    target_slides = slides[:3]
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    sunny_eleven_id = os.environ.get("ELEVENLABS_VOICE_ID", "").strip()
    
    for slide in target_slides:
        out_file = os.path.join(OUTPUT_DIR, f"Slide_{slide['number']:02d}_{slide['title'].replace(' ', '_').replace('&', 'and')[:30]}.mp3")
        print(f"\n--- Generating Sunny Voice for Slide {slide['number']}: {slide['title']} ---")
        
        if api_key and sunny_eleven_id:
            print(f"Generating with ElevenLabs Voice ID: {sunny_eleven_id}...")
            success, msg = generate_elevenlabs_sunny(slide['script'], out_file, api_key, sunny_eleven_id)
            if success:
                print(f"Saved: {out_file}")
                continue
            else:
                print(f"ElevenLabs failed: {msg}")
                
        print(f"Generating with Neural Sunny/Upbeat Voice ({VOICE_ID})...")
        asyncio.run(generate_edge_tts(slide['script'], out_file, voice=VOICE_ID))
        print(f"Saved: {out_file}")

    print("\nGeneration completed successfully!")

if __name__ == "__main__":
    main()
