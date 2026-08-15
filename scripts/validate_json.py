#!/usr/bin/env python3
"""
validate_json.py — Mission Stock Lab

Proverava da je JSON fajl validan (parsira se bez greske). Standardna biblioteka.

Upotreba:
    python scripts/validate_json.py data/OTIS.json
"""

import json
import sys


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        json.load(f)
    print(f"OK valid JSON: {path}")


if __name__ == "__main__":
    main()
