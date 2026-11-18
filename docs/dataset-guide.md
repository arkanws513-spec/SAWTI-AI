# Dataset preparation guide

## Recommended first recording set
- Record in a quiet room with the phone 15–20 cm away.
- Use the same microphone and room for a session where possible.
- Speak naturally; do not whisper, shout, or add background music.
- Save original recordings. Never overwrite them during preprocessing.
- Keep each clip focused on one sentence or short paragraph.
- For the first experiment, collect 20–30 minutes of clean, varied Arabic speech. This is a data-collection target, not a promise of model quality.

## Folder layout
```text
datasets/
  my_voice/
    raw/
      session_01/
        clip_001.wav
        clip_002.wav
    consent.json
    transcripts.csv
```

`consent.json` should be based on `consent-template.json`. Keep it private and outside Git.
Use `transcripts.csv` with columns `file,text,language` if you are preparing aligned speech text.
Do not put personal details or recordings in public issues or commits.

## Validation
```bash
sawti validate-dataset datasets/my_voice/raw \\
  --manifest datasets/my_voice/manifest.jsonl \\
  --report datasets/my_voice/report.json
```

The validator does not change audio. It records sample rate, channels, duration, peak, RMS, SHA-256, and warnings.
A warning is a review prompt, not an automatic rejection. A silent clip will be flagged for review.

## Important
The v0.2 dataset tool does not perform denoising, source separation, forced alignment, voice conversion, or model training.
