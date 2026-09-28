"""
PostToolUse hook (matcher: Edit|Write) - odmah posle upisa u data/*.json, proveri
da je JSON validan (Faza 3 workflow-a oslanja se na python scripts/scorecard.py
koje puca kasnije i manje citljivo ako je JSON pokvaren). Ne blokira nista (fajl
je vec upisan) - samo odmah signalizira gresku.
"""
import json
import os
import sys


def norm(path):
    return path.replace("\\", "/")


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_input = payload.get("tool_input") or {}
    cwd = payload.get("cwd") or "."
    file_path = tool_input.get("file_path", "") or ""

    if not file_path.lower().endswith(".json"):
        sys.exit(0)

    abs_path = file_path if os.path.isabs(file_path) else os.path.join(cwd, file_path)
    rel = norm(os.path.relpath(abs_path, cwd)) if os.path.isabs(file_path) else norm(file_path)

    if "data/" not in rel and not rel.startswith("data/"):
        sys.exit(0)

    try:
        with open(abs_path, encoding="utf-8") as f:
            json.load(f)
    except Exception as e:
        sys.stderr.write(f"UPOZORENJE: {rel} nije validan JSON posle upisa: {e}\n")
        sys.exit(0)

    sys.exit(0)


if __name__ == "__main__":
    main()
