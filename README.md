# SAWTI-AI
**Personal AI Voice & Singing Engine** — an open-source, Arabic-first research project for building a consent-based voice workflow.

> Status: **v0.1.0 — project scaffold**. This repository does not yet train or clone a voice. It establishes the project structure, dataset rules, validation utilities, and a staged roadmap.

## Goals
- Arabic-first speech and singing research.
- Work only with your own voice or recordings for which you have explicit, documented permission.
- Prefer open-source tools and local processing; no paid API is required by this scaffold.
- Keep dataset preparation, model training, conversion, singing, and the studio as separate modules.

## Current capabilities
- Validate a folder of WAV recordings for basic format, duration, and clipping indicators.
- Create a JSONL dataset manifest.
- Provide configuration templates and documentation.

## Quick start
Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python -m sawti.cli validate-dataset ./datasets/my_voice --manifest ./datasets/my_voice/manifest.jsonl
```

Expected input: mono or stereo WAV files. The validator reports technical properties; it does not determine speaker identity or whether consent exists.

## Dataset consent and privacy
1. Record only your own voice, or obtain explicit permission from the speaker.
2. Keep a written record of consent and permitted uses.
3. Do not upload private recordings or identifiable speech without permission.
4. Never use the system to impersonate someone, mislead listeners, or bypass identity checks.
5. Keep raw recordings private; do not commit datasets, model weights, or personal audio to Git.

## Roadmap
See [`docs/roadmap.md`](docs/roadmap.md) and [`docs/architecture.md`](docs/architecture.md).

## License
MIT for the original project code. Third-party model weights, datasets, and dependencies retain their own licenses; review them separately before use.
