# Architecture

SAWTI-AI is organized as a staged pipeline. The initial release deliberately contains dataset tooling only; model training and generation are later milestones.

```text
Recording
   |
   v
Dataset validation --> Consent / provenance records
   |
   v
Preprocessing --> Feature extraction
   |
   v
Voice model research and training
   |
   +--> Speech inference
   +--> Voice conversion
   +--> Singing / melodic performance
   |
   v
Audio post-processing --> Export
```

## Modules
- `sawti/dataset.py`: inspect recordings and produce a manifest.
- `sawti/training/`: future training adapters; no trainer is implemented yet.
- `sawti/conversion/`: future voice-conversion pipeline.
- `sawti/singing/`: future singing-oriented research.
- `sawti/studio/`: future user interface and project management.

## Design constraints
- Keep raw data outside Git.
- Store dataset provenance and consent metadata separately from audio.
- Make sample rate, channels, and segmentation configurable.
- Pin and audit third-party model licenses before integrating weights.
