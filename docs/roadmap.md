# Roadmap
## v0.1 — Foundation
- [x] Repository structure, WAV inspection, JSONL manifest, basic tests
## v0.2 — Dataset quality and provenance
- [x] Integrity checks, duration/channels/sample-rate/peak/RMS checks
- [x] SHA-256 fingerprints, summary report, consent template and recording guide
## v0.3 — Transcript and Arabic text preparation
- [x] CSV transcript validation against WAV files
- [x] Duplicate, missing, empty transcript and unsafe path checks
- [x] Conservative Arabic text normalization
- [x] CI test matrix for Python 3.10–3.12
- [ ] Curated Arabic pronunciation evaluation corpus
## v0.4 — Arabic speech baseline
- [ ] Reproduce one candidate from its official repository
- [ ] Compare Egyptian and Modern Standard Arabic on identical test sentences
- [ ] Record latency, RAM/VRAM, intelligibility and naturalness
- [ ] Add inference adapter only after license and hardware validation
## v0.5 — Personal voice research
- [ ] Consent-verified adaptation, evaluation and local inference profile
## v0.6 — Singing research
- [ ] Singing dataset schema, pitch metadata and melody-conditioned experiments
## v1.0 — Studio
- [ ] Recording/import interface, text and melody controls, export and projects

Every milestone requires tests, documented hardware requirements, and separate license review. No milestone assumes paid cloud compute.
