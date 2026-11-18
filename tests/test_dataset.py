from pathlib import Path

import numpy as np
import soundfile as sf

from sawti.dataset import inspect_audio, inspect_dataset, write_manifest


def test_inspect_audio(tmp_path: Path):
    audio_path = tmp_path / "sample.wav"
    sf.write(audio_path, np.zeros(24000, dtype=np.float32), 24000)
    result = inspect_audio(audio_path)
    assert result["sample_rate"] == 24000
    assert result["channels"] == 1
    assert result["duration_seconds"] == 1.0
    assert result["warnings"] == []


def test_manifest(tmp_path: Path):
    folder = tmp_path / "audio"
    folder.mkdir()
    sf.write(folder / "one.wav", np.zeros(24000, dtype=np.float32), 24000)
    records = inspect_dataset(folder)
    target = tmp_path / "manifest.jsonl"
    write_manifest(records, target)
    assert target.exists()
    assert '"file": "one.wav"' in target.read_text(encoding="utf-8")
