import math
import struct
import wave
import os
import random

SAMPLE_RATE = 44100
DURATION = 120.0 # 2 minutes
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)

print(f"Generating upbeat corporate background music ({DURATION}s, {SAMPLE_RATE}Hz)...")

# Tempo: 116 BPM
BPM = 116.0
BEAT_DUR = 60.0 / BPM
BAR_DUR = BEAT_DUR * 4.0

# Harmonic Chord Progression in C Major (C - G - Am - F)
chords = [
    [261.63, 329.63, 392.00, 523.25], # C maj
    [196.00, 246.94, 293.66, 392.00], # G maj
    [220.00, 261.63, 329.63, 440.00], # A min
    [174.61, 220.00, 261.63, 349.23], # F maj
]
bass_roots = [130.81, 98.00, 110.00, 87.31] # C3, G2, A2, F2

left_channel = [0.0] * TOTAL_SAMPLES
right_channel = [0.0] * TOTAL_SAMPLES

num_bars = int(DURATION / BAR_DUR)

# 1. Upbeat Pluck Arpeggio
for bar in range(num_bars):
    chord = chords[bar % 4]
    bar_start_t = bar * BAR_DUR
    for step in range(16):
        note_t_start = bar_start_t + step * (BEAT_DUR / 4.0)
        s_start = int(note_t_start * SAMPLE_RATE)
        s_len = int(SAMPLE_RATE * 0.35)
        note_freq = chord[step % len(chord)]
        if step % 2 == 1:
            note_freq *= 2.0
            
        pan = 0.3 if step % 2 == 0 else 0.7
        for i in range(s_len):
            idx = s_start + i
            if idx >= TOTAL_SAMPLES:
                break
            t_rel = i / SAMPLE_RATE
            env = math.exp(-t_rel * 12.0)
            w = 0.6 * math.sin(2 * math.pi * note_freq * t_rel) + 0.3 * math.sin(4 * math.pi * note_freq * t_rel) + 0.1 * math.sin(6 * math.pi * note_freq * t_rel)
            val = w * env * 0.18
            left_channel[idx] += val * (1.0 - pan)
            right_channel[idx] += val * pan

# 2. Warm Bassline
for bar in range(num_bars):
    root = bass_roots[bar % 4]
    bar_start_t = bar * BAR_DUR
    rhythm_steps = [0.0, 0.75, 1.5, 2.0, 2.75, 3.5]
    for r_step in rhythm_steps:
        note_t_start = bar_start_t + r_step * BEAT_DUR
        s_start = int(note_t_start * SAMPLE_RATE)
        s_len = int(SAMPLE_RATE * 0.4)
        for i in range(s_len):
            idx = s_start + i
            if idx >= TOTAL_SAMPLES:
                break
            t_rel = i / SAMPLE_RATE
            env = math.exp(-t_rel * 6.0)
            w = 0.8 * math.sin(2 * math.pi * root * t_rel) + 0.2 * math.sin(4 * math.pi * root * t_rel)
            val = w * env * 0.25 * 0.5
            left_channel[idx] += val
            right_channel[idx] += val

# 3. Upbeat Drums & Shaker
for bar in range(num_bars):
    bar_start_t = bar * BAR_DUR
    for beat in range(4):
        beat_t = bar_start_t + beat * BEAT_DUR
        
        # Soft Kick on 1 and 3
        if beat in [0, 2]:
            s_start = int(beat_t * SAMPLE_RATE)
            s_len = int(SAMPLE_RATE * 0.15)
            for i in range(s_len):
                idx = s_start + i
                if idx >= TOTAL_SAMPLES:
                    break
                t_rel = i / SAMPLE_RATE
                kick_freq = 120.0 * math.exp(-t_rel * 30.0) + 45.0
                kick = math.sin(2 * math.pi * kick_freq * t_rel) * math.exp(-t_rel * 18.0) * 0.22
                left_channel[idx] += kick
                right_channel[idx] += kick
                
        # Snare / Clap on 2 and 4
        if beat in [1, 3]:
            s_start = int(beat_t * SAMPLE_RATE)
            s_len = int(SAMPLE_RATE * 0.12)
            for i in range(s_len):
                idx = s_start + i
                if idx >= TOTAL_SAMPLES:
                    break
                t_rel = i / SAMPLE_RATE
                noise = random.uniform(-1.0, 1.0)
                snare = noise * math.exp(-t_rel * 22.0) * 0.12
                left_channel[idx] += snare
                right_channel[idx] += snare
                
        # 16th Shakers
        for sub in range(4):
            sh_t = beat_t + sub * (BEAT_DUR / 4.0)
            s_start = int(sh_t * SAMPLE_RATE)
            s_len = int(SAMPLE_RATE * 0.04)
            for i in range(s_len):
                idx = s_start + i
                if idx >= TOTAL_SAMPLES:
                    break
                t_rel = i / SAMPLE_RATE
                noise = random.uniform(-1.0, 1.0)
                amp = 0.07 if sub % 2 == 1 else 0.04
                shaker = noise * math.exp(-t_rel * 80.0) * amp
                left_channel[idx] += shaker * 0.6
                right_channel[idx] += shaker * 0.4

# Master Normalization
max_l = max(abs(x) for x in left_channel) or 1.0
max_r = max(abs(x) for x in right_channel) or 1.0
max_val = max(max_l, max_r)
scale = 0.85 / max_val

out_paths = [
    "presentation/assets/audio/upbeat_bg_music.wav",
    "video_test/upbeat_bg_music.wav"
]

for p in out_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with wave.open(p, "w") as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        
        frames = bytearray()
        for i in range(TOTAL_SAMPLES):
            l_val = int(max(-32767, min(32767, left_channel[i] * scale * 32767)))
            r_val = int(max(-32767, min(32767, right_channel[i] * scale * 32767)))
            frames.extend(struct.pack("<hh", l_val, r_val))
            
        wav_file.writeframes(frames)
    print(f"Saved upbeat music track: {p}")

print("Pure Python upbeat background music generated successfully!")
