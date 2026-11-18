from __future__ import annotations

import argparse
import json
from pathlib import Path

from sawti.dataset import inspect_dataset, write_manifest


def main() -> None:
    parser = argparse.ArgumentParser(prog="sawti", description="SAWTI-AI dataset utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-dataset", help="Inspect WAV files and write a JSONL manifest")
    validate.add_argument("folder", type=Path)
    validate.add_argument("--manifest", type=Path, default=None)

    args = parser.parse_args()
    if args.command == "validate-dataset":
        records = inspect_dataset(args.folder)
        manifest = args.manifest or (args.folder / "manifest.jsonl")
        write_manifest(records, manifest)
        print(json.dumps({
            "files": len(records),
            "manifest": str(manifest),
            "warnings": sum(bool(r["warnings"]) for r in records),
        }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
