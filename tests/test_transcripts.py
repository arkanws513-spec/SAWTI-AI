from pathlib import Path
import csv
import numpy as np
import soundfile as sf
from sawti.text import normalize_arabic_text
from sawti.transcripts import validate_transcripts

def test_arabic_normalization():
    assert normalize_arabic_text("  أَهْلًا   ـبِكِ ") == "اَهْلًا بِكِ"

def test_transcript_validation(tmp_path: Path):
    audio = tmp_path / "audio"
    audio.mkdir()
    sf.write(audio / "clip.wav", np.ones(24000, dtype=np.float32) * .1, 24000)
    source = tmp_path / "transcripts.csv"
    with source.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file","text","language"])
        w.writeheader()
        w.writerow({"file":"clip.wav","text":"أهلاً بك","language":"ar-EG"})
    result = validate_transcripts(source, audio)
    assert result["valid_rows"] == 1 and result["invalid_rows"] == 0
    assert result["rows"][0]["normalized_text"] == "اهلاً بك"

def test_path_escape_rejected(tmp_path: Path):
    audio = tmp_path / "audio"
    audio.mkdir()
    source = tmp_path / "transcripts.csv"
    source.write_text("file,text,language\\n../outside.wav,hello,en\\n", encoding="utf-8")
    result = validate_transcripts(source, audio)
    assert "path_outside_audio_root" in result["rows"][0]["errors"]
