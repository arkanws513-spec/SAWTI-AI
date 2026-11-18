from __future__ import annotations
import csv
from pathlib import Path
from typing import Any
from sawti.text import normalize_arabic_text

REQUIRED_COLUMNS = {"file", "text", "language"}

def validate_transcripts(csv_path: Path, audio_root: Path) -> dict[str, Any]:
    """Validate transcript CSV references without modifying audio or source text."""
    if not csv_path.is_file():
        raise FileNotFoundError(f"Transcript CSV not found: {csv_path}")
    if not audio_root.is_dir():
        raise FileNotFoundError(f"Audio folder not found: {audio_root}")
    available = {p.relative_to(audio_root).as_posix() for p in audio_root.rglob("*") if p.is_file() and p.suffix.lower() == ".wav"}
    rows, errors, seen = [], [], set()
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
        if missing:
            raise ValueError("Missing CSV columns: " + ", ".join(missing))
        for line, row in enumerate(reader, start=2):
            name = (row.get("file") or "").strip().replace("\\", "/")
            transcript, language = (row.get("text") or "").strip(), (row.get("language") or "").strip()
            issues = []
            if not name: issues.append("missing_file")
            elif name in seen: issues.append("duplicate_file")
            else: seen.add(name)
            candidate = (audio_root / name).resolve() if name else None
            if candidate is not None:
                try: candidate.relative_to(audio_root.resolve())
                except ValueError: issues.append("path_outside_audio_root")
            if name and name not in available: issues.append("audio_file_not_found")
            if not transcript: issues.append("empty_transcript")
            if not language: issues.append("missing_language")
            item = {"line": line, "file": name, "normalized_text": normalize_arabic_text(transcript),
                    "language": language, "status": "error" if issues else "ok", "errors": issues}
            rows.append(item)
            if issues: errors.append({"line": line, "file": name, "errors": issues})
    return {"csv": csv_path.name, "audio_files": len(available), "transcript_rows": len(rows),
            "valid_rows": sum(r["status"] == "ok" for r in rows),
            "invalid_rows": sum(r["status"] == "error" for r in rows),
            "unreferenced_audio_files": sorted(available - seen), "rows": rows, "errors": errors}
