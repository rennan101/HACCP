import asyncio
import os
import edge_tts

OUTPUT_DIR = "audio_output/british_female_samples"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Engaging & dynamic sample text adapted for British Food & Dairy Training
SAMPLE_TEXT = (
    "Welcome to our HACCP Level Two Masterclass! Today, we're taking a dynamic, practical look at how "
    "we protect our dairy processing lines and guarantee world-class food safety for every single customer. "
    "Let's dive straight in!"
)

# Various British female neural profiles with pitch & rate tuning for maximum engagement/energy
PROFILES = [
    {
        "filename": "1_Libby_Energetic_British.mp3",
        "voice": "en-GB-LibbyNeural",
        "rate": "+5%",
        "pitch": "+2Hz",
        "desc": "Libby - Upbeat, youthful, modern British English with energetic pacing"
    },
    {
        "filename": "2_Maisie_Lively_British.mp3",
        "voice": "en-GB-MaisieNeural",
        "rate": "+4%",
        "pitch": "+3Hz",
        "desc": "Maisie - Bright, enthusiastic and fresh British tone"
    },
    {
        "filename": "3_Sonia_Dynamic_Educator_British.mp3",
        "voice": "en-GB-SoniaNeural",
        "rate": "+5%",
        "pitch": "+0Hz",
        "desc": "Sonia - Confident, engaging senior educator with dynamic flow"
    },
    {
        "filename": "4_Libby_Inspiring_British.mp3",
        "voice": "en-GB-LibbyNeural",
        "rate": "+2%",
        "pitch": "+4Hz",
        "desc": "Libby (Higher Energy) - Cheerful, friendly, highly motivating delivery"
    },
    {
        "filename": "5_Emily_Engaging_Commonwealth.mp3",
        "voice": "en-IE-EmilyNeural",
        "rate": "+4%",
        "pitch": "+2Hz",
        "desc": "Emily - Expressive, warm, very engaging accent"
    },
    {
        "filename": "6_Natasha_Positive_Paced.mp3",
        "voice": "en-AU-NatashaNeural",
        "rate": "+5%",
        "pitch": "+2Hz",
        "desc": "Natasha - Polished, vibrant, crisp international English"
    }
]

async def generate():
    for p in PROFILES:
        out_path = os.path.join(OUTPUT_DIR, p["filename"])
        print(f"Generating: {p['desc']}...")
        communicate = edge_tts.Communicate(
            SAMPLE_TEXT,
            p["voice"],
            rate=p["rate"],
            pitch=p["pitch"]
        )
        await communicate.save(out_path)
    print("\nAll exciting British female samples generated successfully!")

if __name__ == "__main__":
    asyncio.run(generate())
