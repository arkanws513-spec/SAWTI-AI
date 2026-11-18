# Arabic speech model shortlist (reviewed 2026-11-18)

This is a research shortlist, not an automatic dependency. No model weights are bundled or downloaded by SAWTI-AI. Before use, re-check the exact model-card license, code license, upstream dependencies, and dataset terms.

## Candidate A — SILMA TTS v1

- Model card: https://huggingface.co/silma-ai/silma-tts
- Code: https://github.com/SILMA-AI/silma-tts
- Model card lists 150M parameters, Arabic/English support, Arabic diacritics, and an Apache-2.0 license for weights (MIT for code).
- The model card documents reference-audio inference and a fine-tuning path based on F5-TTS v1.1.7.
- Its real-time performance claim is measured on an RTX 4090; do not interpret that as evidence of phone support.
- **SAWTI assessment:** best first candidate for a controlled local Arabic/Fusha baseline and later personal-voice adaptation experiments, subject to a reproducible installation and evaluation.

## Candidate B — VoiceTut-TTS

- Model card: https://huggingface.co/Aliabdo/VoiceTut-TTS
- Code: https://github.com/MohammedAly22/VoiceTuT-TTS
- Model card describes Egyptian Arabic, Arabic/English code-switching, 19 built-in voices, and zero-shot reference-voice synthesis.
- The model card lists Apache-2.0 and reports 0.6B parameters and 2.93 GB peak VRAM on a single NVIDIA T4 in its stated evaluation setup.
- Those are project-reported figures, not independent benchmarks. Check the license of the OmniVoice base, tokenizer, and all dependencies before redistribution or derivative work.
- **SAWTI assessment:** useful Egyptian-dialect comparison candidate; likely more demanding than SILMA and not assumed to run on a phone.

## Candidate C — Habibi-TTS

- Model card: https://huggingface.co/SWivid/Habibi-TTS
- Code: https://github.com/SWivid/Habibi-TTS
- The model card describes dialect-specific Arabic models. It states that ALG, EGY, IRQ, MAR, and MSA checkpoints are Apache-2.0, while unified, SAU, and UAE checkpoints are CC-BY-NC-SA-4.0.
- **SAWTI assessment:** valuable dialect comparison set. Never treat the entire repository as having one permissive license; inspect the exact checkpoint and its data restrictions.

## Candidate D — Meta MMS Arabic TTS

- Model card: https://huggingface.co/facebook/mms-tts-ara
- License shown on the model card: CC-BY-NC-4.0.
- **SAWTI assessment:** reference baseline for Arabic speech synthesis only. The non-commercial license makes it unsuitable as the default foundation for a broadly reusable project, and it is not a personal-voice training solution.

## Decision for SAWTI-AI

1. Start with SILMA TTS v1 as the first local Arabic/Fusha inference candidate.
2. Compare VoiceTut-TTS for Egyptian dialect quality using the same short, consented test sentences.
3. Use Habibi-TTS only after selecting a dialect checkpoint and confirming that checkpoint's exact license.
4. Keep MMS as a non-commercial reference baseline only.
5. Do not add any checkpoint to the repository. Store weights locally under the ignored `models/` directory.

## What this does not solve

Ordinary text-to-speech is not singing synthesis. A reference-audio voice prompt is also not the same as training a durable personal model. SAWTI must evaluate speech quality first, then design a separate singing dataset and melody/prosody pipeline. No mobile deployment or training performance is promised until tested on the actual device.

## Safety and privacy gate

Only test a voice belonging to the project owner or a speaker who has explicitly agreed to the intended synthesis and training uses. Keep source audio private, do not publish consent records, and label generated audio as synthetic when a listener could mistake it for a real recording.
