from __future__ import annotations
import argparse, json
from pathlib import Path
from sawti.dataset import inspect_dataset, summarize_dataset, write_manifest
from sawti.transcripts import validate_transcripts

def emit(data: dict, destination: Path | None) -> None:
    rendered = json.dumps(data, ensure_ascii=False, indent=2)
    if destination:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)

def main() -> None:
    parser = argparse.ArgumentParser(prog="sawti", description="SAWTI-AI dataset utilities")
    sub = parser.add_subparsers(dest="command", required=True)
    ds = sub.add_parser("validate-dataset", help="Inspect WAV files and write a JSONL manifest")
    ds.add_argument("folder", type=Path)
    ds.add_argument("--manifest", type=Path)
    ds.add_argument("--report", type=Path)
    tx = sub.add_parser("validate-transcripts", help="Check transcript CSV rows against WAV files")
    tx.add_argument("csv_file", type=Path)
    tx.add_argument("--audio-root", type=Path, required=True)
    tx.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.command == "validate-dataset":
        records = inspect_dataset(args.folder)
        manifest = args.manifest or args.folder / "manifest.jsonl"
        write_manifest(records, manifest)
        summary = summarize_dataset(records)
        summary["manifest"] = str(manifest)
        emit(summary, args.report)
        if summary["errors"]:
            raise SystemExit(2)
    elif args.command == "validate-transcripts":
        report = validate_transcripts(args.csv_file, args.audio_root)
        emit(report, args.report)
        if report["invalid_rows"]:
            raise SystemExit(2)

if __name__ == "__main__":
    main()
