import asyncio
import os
import edge_tts

VOICES = {
    "Sonia_British": "en-GB-SoniaNeural",
    "Libby_British": "en-GB-LibbyNeural",
    "Maisie_British": "en-GB-MaisieNeural",
    "Ava_Conversational": "en-US-AvaMultilingualNeural",
    "Emma_Cheerful_Sunny": "en-US-EmmaMultilingualNeural",
    "Jenny_Friendly": "en-US-JennyNeural"
}

SAMPLE_TEXT = "Welcome to this HACCP Level Two Training Programme, specifically tailored for food and dairy professionals."

async def run():
    os.makedirs("audio_output/voice_samples", exist_ok=True)
    for name, v_id in VOICES.items():
        out = f"audio_output/voice_samples/{name}.mp3"
        print(f"Generating sample: {name} ({v_id})...")
        communicate = edge_tts.Communicate(SAMPLE_TEXT, v_id)
        await communicate.save(out)
    print("Done generating samples!")

if __name__ == "__main__":
    asyncio.run(run())
