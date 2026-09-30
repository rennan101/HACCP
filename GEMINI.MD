# GEMINI Guidelines & Workspace Rules

This repository maintains automated scripts, voiceover narration, subtitles, and video rendering pipelines for the **HACCP Level 2 Training** project (specifically adapted for the Food & Dairy Processing sector).

All AI assistants, subagents, and automated workflows operating in this workspace must strictly adhere to the mandatory skills and standards below.

---

## 1. Mandatory Skills & Directives

### A. Token Optimization (`Skills/optimize-tokens/SKILL.md`)
- **The 300-Line Rule**: No single source code or documentation file should exceed 300 lines unless strictly necessary. Split monolithic files into modular components.
- **Laser Focus**: Keep tasks and file contexts small, modular, and purpose-driven. Avoid dumping multi-topic documentation into single root files.
- **Separation of Concerns**: Separate data models, generation scripts, visual templates, and asset pipelines.

### B. Direct, Human & Anti-Slop Writing (`Skills/no-ai-slop.md`)
- **No AI Buzzwords**: Banned words include *delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game changer, multifaceted, intricate, paramount, transformative, elevate, embark, harness, ever-evolving*.
- **No Throat-Clearing**: Cut openers like *"Here's the thing"*, *"It's worth noting"*, *"At its core"*, *"In today's world"*. Lead directly with the point.
- **Concrete & Direct**: Use active voice, clear facts, real numbers, and precise operational parameters.
- **No Empty Metadiscourse & Formatting Slop**: Avoid excessive bolding mid-sentence, emojis in technical headings, binary contrasts (*"It's not X, it's Y"*), or fake-profound kickers.

---

## 2. Project Architecture & Standards

- **Core Script Source**: [`HACCP_Level_2_Voiceover_Script_and_Subtitles.md`](./HACCP_Level_2_Voiceover_Script_and_Subtitles.md) (Dairy industry adaptation, British English).
- **Audio Output**: [`audio_output/libby_energetic_british/`](./audio_output/libby_energetic_british/) (26 generated slide voiceover MP3s using `en-GB-LibbyNeural`).
- **Video & Style Assets**: [`video_test/`](./video_test/) (1080p slide generation, background audio mixing, separate `.srt` subtitles).
- **Python Environment**: Managed via local virtual environment [`.venv/`](./.venv).
