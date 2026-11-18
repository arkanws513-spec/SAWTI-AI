# SAWTI-AI
**Personal AI Voice & Singing Engine** — an open-source, Arabic-first research project for a consent-based voice workflow.

> Status: **v0.2.0 — dataset quality and provenance**. This release prepares and audits recordings. It does not yet train, clone, convert, or synthesize a voice.

## Current capabilities
- Inspect WAV recordings without modifying source files.
- Detect unreadable files, unusual duration, non-mono audio, sample-rate mismatch, possible clipping, and very quiet/silent recordings.
- Create a JSONL manifest with relative paths and SHA-256 fingerprints.
- Create a compact JSON dataset summary.
- Provide a private consent/provenance template and recording guide.

## Quick start
Python 3.10+.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
sawti validate-dataset datasets/my_voice/raw \\
  --manifest datasets/my_voice/manifest.jsonl \\
  --report datasets/my_voice/report.json
```

## Privacy and consent
Use only your own recordings or recordings with explicit permission for the intended use. Keep consent records, raw audio, transcripts, and model weights private and outside Git. Never use the project to impersonate someone, mislead listeners, or bypass identity checks.

## Roadmap
See [the roadmap](docs/roadmap.md), [dataset guide](docs/dataset-guide.md), and [model policy](docs/model-policy.md).

## Scope and licensing
MIT applies to original project code only. Dependencies, datasets, pretrained checkpoints, and model weights have their own terms and must be reviewed separately. No paid API is required by the current toolkit.
