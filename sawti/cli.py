from __future__ import annotations

import argparse
import json
from pathlib import Path

from sawti.dataset import inspect_dataset, summarize_dataset, write_manifest


def main() -> None:
    parser = argparse.ArgumentParser(prog="sawti", description="SAWTI-AI dataset utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-dataset", help="Inspect WAV files and write a JSONL manifest")
    validate.add_argument("folder", type=Path)
    validate.add_argument("--manifest", type=Path, default=None)
    validate.add_argument("--report", type=Path, default=None)

    args = parser.parse_args()
    if args.command == "validate-dataset":
        records = inspect_dataset(args.folder)
        manifest = args.manifest or (args.folder / "manifest.jsonl")
        write_manifest(records, manifest)
        summary = summarize_dataset(records)
        summary["manifest"] = str(manifest)
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(
                json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            summary["report"] = str(args.report)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        if summary["errors"]:
            raise SystemExit(2)


if __name__ == "__main__":
    main()
