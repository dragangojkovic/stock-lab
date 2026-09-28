"""
PreToolUse hook (matcher: Edit|Write) — sprovodi CLAUDE.md SS11 / SS7 pravilo:
"Ne amenduj-ujem stare git komite ni prepravljam stare zapise u
data/positions.csv / data/predvidjanja.csv - ispravke idu kao novi datirani zapis."

Za svaki zasticeni fajl definise koje kolone su NEIZMENJIVE (identitet i teza) i
koje su dozvoljeno mutabilne (npr. current_price, ishod). Postojeci redovi mogu
dobiti nove vrednosti u mutabilnim kolonama, ali identitet/teza kolone i
prisustvo reda se ne smeju promeniti niti obrisati. Novi redovi (append) su
uvek dozvoljeni.

Edit tool radi string-replace bez uvida u ceo fajl pa se ne moze bezbedno
proveriti red-po-red - zato je Edit na ovim fajlovima blokiran; koristi Write
sa punim azuriranim sadrzajem, koji ovaj hook onda proverava.
"""
import csv
import io
import json
import os
import sys

PROTECTED = {
    "data/positions.csv": {
        "key": ["ticker", "entry_date"],
        "immutable": [
            "ticker", "naziv", "entry_date", "entry_price",
            "benchmark_entry_price", "weight", "teza_kratko", "izlazno_pravilo",
        ],
    },
    "data/predvidjanja.csv": {
        "key": ["ticker", "datum_unosa", "kvartal_provere", "predvidjanje"],
        "immutable": [
            "ticker", "datum_unosa", "kvartal_provere", "predvidjanje",
            "merljiv_prag", "uverenost",
        ],
    },
}


def norm(path):
    return path.replace("\\", "/")


def rel_path(file_path, cwd):
    if not file_path:
        return ""
    abs_path = file_path if os.path.isabs(file_path) else os.path.join(cwd, file_path)
    abs_path = os.path.abspath(abs_path)
    cwd_abs = os.path.abspath(cwd)
    try:
        return norm(os.path.relpath(abs_path, cwd_abs))
    except ValueError:
        return norm(abs_path)


def parse_csv(text):
    if not text.strip():
        return []
    return list(csv.DictReader(io.StringIO(text)))


def row_key(row, key_fields):
    return tuple((row.get(k) or "").strip() for k in key_fields)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool = payload.get("tool_name")
    tool_input = payload.get("tool_input") or {}
    cwd = payload.get("cwd") or "."
    file_path = tool_input.get("file_path", "")
    rel = rel_path(file_path, cwd)

    cfg = PROTECTED.get(rel)
    if cfg is None:
        sys.exit(0)

    if tool == "Edit":
        sys.stderr.write(
            f"{rel} je zasticen fajl (CLAUDE.md SS11: bez retroaktivnih izmena "
            f"postojecih redova). Edit tool menja tekst bez uvida u ceo fajl, pa se "
            f"ne moze proveriti da li je neko neizmenjivo polje promenjeno. Koristi "
            f"Write sa punim, azuriranim sadrzajem fajla - ovaj hook ce onda "
            f"proveriti integritet po redovima.\n"
        )
        sys.exit(2)

    if tool != "Write":
        sys.exit(0)

    abs_path = file_path if os.path.isabs(file_path) else os.path.join(cwd, file_path)
    if not os.path.exists(abs_path):
        sys.exit(0)  # nov fajl, nema staro stanje za zastitu

    with open(abs_path, encoding="utf-8") as f:
        old_text = f.read()

    new_text = tool_input.get("content", "") or ""

    try:
        old_rows = parse_csv(old_text)
        new_rows = parse_csv(new_text)
    except Exception as e:
        sys.stderr.write(f"{rel}: CSV se ne parsira, blokirano radi sigurnosti ({e}).\n")
        sys.exit(2)

    key_fields = cfg["key"]
    immutable = cfg["immutable"]
    new_by_key = {row_key(r, key_fields): r for r in new_rows}

    problems = []
    for old_row in old_rows:
        k = row_key(old_row, key_fields)
        new_row = new_by_key.get(k)
        if new_row is None:
            problems.append(f"red obrisan ili identitet promenjen: {dict(zip(key_fields, k))}")
            continue
        for field in immutable:
            old_val = (old_row.get(field) or "").strip()
            new_val = (new_row.get(field) or "").strip()
            if old_val != new_val:
                problems.append(
                    f"{dict(zip(key_fields, k))}: neizmenjivo polje '{field}' "
                    f"promenjeno iz '{old_val}' u '{new_val}'"
                )

    if problems:
        sys.stderr.write(
            f"{rel}: blokirano - postojeci redovi bi bili izmenjeni ili obrisani "
            f"(CLAUDE.md SS11, SS7: bez retroaktivnih izmena teze/istorije). "
            f"Ispravke idu kao NOV datirani red, ne izmena starog.\nDetalji:\n- "
            + "\n- ".join(problems) + "\n"
        )
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
