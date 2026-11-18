from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import soundfile as sf

SUPPORTED = {".wav"}


def inspect_audio(path: Path) -> dict[str, Any]:
    info = sf.info(str(path))
    audio, sample_rate = sf.read(str(path), dtype="float32", always_2d=True)
    duration = len(audio) / sample_rate if sample_rate else 0.0
    peak = float(np.max(np.abs(audio))) if audio.size else 0.0
    warnings: list[str] = []

    if duration < 1.0:
        warnings.append("shorter_than_1_second")
    if duration > 20.0:
        warnings.append("longer_than_20_seconds")
    if peak >= 0.999:
        warnings.append("possible_clipping")
    if info.channels != 1:
        warnings.append("not_mono")
    if sample_rate != 24000:
        warnings.append("sample_rate_not_24000")

    return {
        "file": path.name,
        "sample_rate": sample_rate,
        "channels": info.channels,
        "duration_seconds": round(duration, 3),
        "peak": round(peak, 6),
        "subtype": info.subtype,
        "warnings": warnings,
    }


def inspect_dataset(folder: Path) -> list[dict[str, Any]]:
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Dataset folder does not exist: {folder}")
    paths = sorted(p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED)
    return [inspect_audio(path) for path in paths]


def write_manifest(records: list[dict[str, Any]], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
