# SAWTI-AI
**Personal AI Voice & Singing Engine** — an open-source, Arabic-first research project for a consent-based voice workflow.

> Status: **v0.3.0-dev — dataset and transcript preparation**. This release prepares and audits data. It does not yet train, clone, convert, or synthesize a voice.

## Current capabilities
- Inspect WAV recordings without modifying source files.
- Detect unreadable files, unusual duration, non-mono audio, sample-rate mismatch, possible clipping, and very quiet/silent recordings.
- Create JSONL manifests with relative paths and SHA-256 fingerprints, plus dataset summaries.
- Validate transcript CSV files against WAV files, including duplicate, missing, empty, and unsafe path checks.
- Normalize Arabic text conservatively for comparison while preserving original transcripts.
- Use an original Egyptian/Modern Standard Arabic evaluation prompt set.
- Run automated tests on Python 3.10, 3.11, and 3.12 using GitHub Actions.

## Quick start
Python 3.10+.
```bash
python -m venv .venv
pip install -r requirements.txt
pip install -e .
sawti validate-dataset datasets/my_voice/raw --manifest datasets/my_voice/manifest.jsonl --report datasets/my_voice/report.json
sawti validate-transcripts datasets/my_voice/transcripts.csv --audio-root datasets/my_voice/raw --report datasets/my_voice/transcript-report.json
```
Transcript CSV columns: file,text,language; paths are relative to --audio-root.

## Evaluation prompts
See [original Arabic evaluation prompts](data/prompts/arabic-evaluation.csv) and [how to use them](docs/evaluation-prompts.md). Keep this set held out from training when using it for fair comparisons.

## Privacy and consent
Use only your own recordings or recordings with explicit permission for the intended use. Keep consent records, raw audio, transcripts, and model weights private and outside Git. Never use the project to impersonate someone, mislead listeners, or bypass identity checks.

## Research
See [roadmap](docs/roadmap.md), [dataset guide](docs/dataset-guide.md), [model policy](docs/model-policy.md), and [Arabic model shortlist](docs/model-selection.md).

MIT applies to original project code only. Third-party dependencies, datasets, checkpoints, and weights retain their own licenses. No paid API is required by the current toolkit.
