# Roadmap

## v0.1 — Foundation
- [x] Repository structure and project metadata
- [x] WAV dataset inspection
- [x] JSONL manifest generation
- [x] Basic tests

## v0.2 — Dataset quality and provenance
- [x] WAV integrity checks and unreadable-file reporting
- [x] Duration, channels, sample-rate, peak and RMS checks
- [x] SHA-256 fingerprints and relative paths
- [x] Dataset summary JSON report
- [x] Consent metadata template and recording guide
- [ ] Optional transcript validation and alignment checks

## v0.3 — Arabic speech baseline
- [x] Research Arabic-capable open-weight model candidates and their license caveats
- [ ] Select a baseline after reproducible installation and local hardware test
- [ ] Arabic text normalization and pronunciation evaluation
- [ ] Inference wrapper with model-card and hardware notes

## v0.4 — Personal voice research
- [ ] Consent-verified personal adaptation workflow
- [ ] Speaker-independent evaluation and intelligibility tests
- [ ] Local inference profile for modest hardware

## v0.5 — Singing research
- [ ] Singing dataset schema and pitch metadata
- [ ] Melody-conditioned experiments
- [ ] Arabic singing/nasheed prosody evaluation

## v1.0 — Studio
- [ ] Recording/import interface
- [ ] Text, melody, and performance controls
- [ ] Export and project management

Every milestone requires tests, documented hardware requirements, and separate license review for code, datasets, and weights. No milestone assumes paid cloud compute.
