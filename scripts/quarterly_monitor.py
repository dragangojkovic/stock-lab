"""
Kvartalni monitor: proverava SEC EDGAR za nove 10-Q/10-K podneske za pozicije
iz data/positions.csv (status active/open) i belezi ih u data/quarterly_alerts.md.

Koristi samo standardnu biblioteku (isti konvencija kao ostale skripte u projektu).
Pokrece se lokalno preko Windows Task Scheduler-a (ne cloud rutina - ta je bila
blokirana organizacionom mrežnom politikom).
"""
import csv
import json
import os
import ssl
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSITIONS = os.path.join(ROOT, "data", "positions.csv")
STATE = os.path.join(ROOT, "data", "quarterly_watch_state.json")
ALERTS = os.path.join(ROOT, "data", "quarterly_alerts.md")
UA = "stock-lab-monitor (personal project; dragan.gojkovic@profitoptics.com)"


def _ssl_context():
    # Neki Windows sertifikati u sistemskom store-u imaju los ASN.1 encoding
    # koji Python-ov ssl modul ne moze da parsira (load_default_certs puca).
    # Koristimo certifi CA bundle ako je dostupan, umesto Windows store-a.
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


_SSL_CTX = _ssl_context()


def http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30, context=_SSL_CTX) as r:
        return json.loads(r.read().decode("utf-8"))


def load_tickers():
    tickers = []
    with open(POSITIONS, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status", "").strip().lower() in ("active", "open"):
                tickers.append((row["ticker"].strip(), row.get("naziv", "").strip()))
    return tickers


def resolve_ciks(tickers):
    data = http_json("https://www.sec.gov/files/company_tickers.json")
    by_ticker = {v["ticker"].upper(): str(v["cik_str"]).zfill(10) for v in data.values()}
    out = {}
    for t, name in tickers:
        cik = by_ticker.get(t.upper())
        if cik:
            out[t] = {"cik": cik, "naziv": name}
        else:
            print(f"UPOZORENJE: CIK nije nadjen za {t}", file=sys.stderr)
    return out


def latest_filing(cik):
    data = http_json(f"https://data.sec.gov/submissions/CIK{cik}.json")
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accns = recent.get("accessionNumber", [])
    for i, form in enumerate(forms):
        if form in ("10-Q", "10-K"):
            return {"form": form, "date": dates[i], "accession": accns[i]}
    return None


def load_state():
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")


def append_alert(entries):
    today = date.today().isoformat()
    header = "# Kvartalni alerti\n\n"
    existing = ""
    if os.path.exists(ALERTS):
        with open(ALERTS, encoding="utf-8") as f:
            existing = f.read()
        if existing.startswith(header):
            existing = existing[len(header):]
    else:
        existing = ""

    block = f"## {today}\n\n"
    for e in entries:
        cik = e["cik"]
        link = (f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&"
                f"CIK={cik}&type=10-Q&dateb=&owner=include&count=10")
        block += (f"- **{e['ticker']}** ({e['naziv']}) — {e['form']}, "
                  f"podneto {e['date']}, accession `{e['accession']}` — [SEC EDGAR]({link})\n")
    block += "\n"

    with open(ALERTS, "w", encoding="utf-8") as f:
        f.write(header + block + existing)


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)


def main():
    tickers = load_tickers()
    if not tickers:
        print("Nema aktivnih pozicija u positions.csv.")
        return

    resolved = resolve_ciks(tickers)
    state = load_state()
    new_entries = []
    baseline_only = []

    for ticker, info in resolved.items():
        cik = info["cik"]
        try:
            filing = latest_filing(cik)
        except urllib.error.URLError as e:
            print(f"GRESKA pri proveri {ticker}: {e}", file=sys.stderr)
            continue
        if filing is None:
            continue

        prior = state.get(ticker)
        if prior is None:
            baseline_only.append(ticker)
        elif prior.get("accession") != filing["accession"]:
            new_entries.append({
                "ticker": ticker, "naziv": info["naziv"], "cik": cik,
                "form": filing["form"], "date": filing["date"],
                "accession": filing["accession"],
            })

        state[ticker] = {**filing, "checked": date.today().isoformat()}

    save_state(state)

    if new_entries:
        append_alert(new_entries)

    files_to_track = [f for f in ("data/quarterly_watch_state.json", "data/quarterly_alerts.md")
                       if os.path.exists(os.path.join(ROOT, f))]

    changed = git("status", "--porcelain", *files_to_track).stdout.strip()
    if not changed:
        print("Nema promena od poslednje provere.")
        return

    add_result = git("add", *files_to_track)
    if add_result.returncode != 0:
        print(f"Git add nije uspeo: {add_result.stderr}", file=sys.stderr)
        return

    if new_entries:
        tickers_str = ", ".join(e["ticker"] for e in new_entries)
        msg = f"Kvartalni monitor: novi izvestaj za {tickers_str}"
    elif baseline_only:
        msg = "Kvartalni monitor: baseline stanje azurirano"
    else:
        msg = "Kvartalni monitor: azuriranje stanja"

    result = git("commit", "-m", msg)
    if result.returncode != 0:
        print(f"Commit nije uspeo: {result.stderr}", file=sys.stderr)
        return

    push = git("push")
    if push.returncode != 0:
        print(f"Push nije uspeo: {push.stderr}", file=sys.stderr)
    else:
        print(f"Komitovano i pushovano: {msg}")


if __name__ == "__main__":
    main()
