from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
import soundfile as sf

SUPPORTED = {".wav"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect_audio(path: Path, root: Path | None = None) -> dict[str, Any]:
    """Inspect a WAV file without modifying it."""
    info = sf.info(str(path))
    audio, sample_rate = sf.read(str(path), dtype="float32", always_2d=True)
    duration = len(audio) / sample_rate if sample_rate else 0.0
    peak = float(np.max(np.abs(audio))) if audio.size else 0.0
    rms = float(np.sqrt(np.mean(np.square(audio)))) if audio.size else 0.0
    warnings: list[str] = []

    if duration < 1.0:
        warnings.append("shorter_than_1_second")
    if duration > 20.0:
        warnings.append("longer_than_20_seconds")
    if peak >= 0.999:
        warnings.append("possible_clipping")
    if rms < 0.001:
        warnings.append("very_quiet_or_silent")
    if info.channels != 1:
        warnings.append("not_mono")
    if sample_rate != 24000:
        warnings.append("sample_rate_not_24000")

    try:
        display_path = path.relative_to(root).as_posix() if root else path.name
    except ValueError:
        display_path = path.name

    return {
        "file": display_path,
        "sha256": sha256_file(path),
        "sample_rate": sample_rate,
        "channels": info.channels,
        "duration_seconds": round(duration, 3),
        "peak": round(peak, 6),
        "rms": round(rms, 6),
        "subtype": info.subtype,
        "status": "warning" if warnings else "ok",
        "warnings": warnings,
    }


def inspect_dataset(folder: Path) -> list[dict[str, Any]]:
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Dataset folder does not exist: {folder}")
    paths = sorted(
        p for p in folder.rglob("*")
        if p.is_file() and p.suffix.lower() in SUPPORTED
        and p.name.lower() != "manifest.jsonl"
    )
    records: list[dict[str, Any]] = []
    for path in paths:
        try:
            records.append(inspect_audio(path, root=folder))
        except (RuntimeError, OSError, ValueError) as exc:
            records.append({
                "file": path.relative_to(folder).as_posix(),
                "status": "error",
                "warnings": ["unreadable_audio"],
                "error": str(exc),
            })
    return records


def write_manifest(records: list[dict[str, Any]], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def summarize_dataset(records: list[dict[str, Any]]) -> dict[str, Any]:
    total_seconds = sum(float(r.get("duration_seconds", 0)) for r in records)
    return {
        "files": len(records),
        "ok": sum(r.get("status") == "ok" for r in records),
        "warnings": sum(r.get("status") == "warning" for r in records),
        "errors": sum(r.get("status") == "error" for r in records),
        "total_duration_seconds": round(total_seconds, 2),
        "total_duration_minutes": round(total_seconds / 60, 2),
    }
