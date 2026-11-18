from pathlib import Path
import json

import numpy as np
import soundfile as sf

from sawti.dataset import (
    inspect_audio, inspect_dataset, summarize_dataset, write_manifest
)


def test_inspect_audio(tmp_path: Path):
    audio_path = tmp_path / "sample.wav"
    sf.write(audio_path, np.zeros(24000, dtype=np.float32), 24000)
    result = inspect_audio(audio_path)
    assert result["sample_rate"] == 24000
    assert result["channels"] == 1
    assert result["duration_seconds"] == 1.0
    assert "very_quiet_or_silent" in result["warnings"]
    assert len(result["sha256"]) == 64


def test_manifest_and_summary(tmp_path: Path):
    folder = tmp_path / "audio"
    folder.mkdir()
    sf.write(folder / "one.wav", np.ones(24000, dtype=np.float32) * 0.1, 24000)
    records = inspect_dataset(folder)
    target = tmp_path / "manifest.jsonl"
    write_manifest(records, target)
    parsed = [json.loads(line) for line in target.read_text(encoding="utf-8").splitlines()]
    assert parsed[0]["file"] == "one.wav"
    summary = summarize_dataset(records)
    assert summary["files"] == 1
    assert summary["ok"] == 1


def test_missing_folder():
    import pytest
    with pytest.raises(FileNotFoundError):
        inspect_dataset(Path("this-folder-should-not-exist-sawti"))


def test_corrupt_wav_is_reported(tmp_path: Path):
    folder = tmp_path / "audio"
    folder.mkdir()
    (folder / "broken.wav").write_bytes(b"not a wav")
    records = inspect_dataset(folder)
    assert records[0]["status"] == "error"
    assert "unreadable_audio" in records[0]["warnings"]
