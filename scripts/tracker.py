#!/usr/bin/env python3
"""
tracker.py — Mission Stock Lab

Prati paper portfolio protiv benchmarka (VUAA) i ocenjuje tačnost predviđanja
fundamenata. Samo standardna biblioteka.

Upotreba:
    python3 scripts/tracker.py                       # pun izveštaj
    python3 scripts/tracker.py --predvidjanja        # samo tabla predviđanja

Ključno: svaka pozicija se poredi sa VUAA za IDENTIČAN period držanja
(benchmark cena na dan ulaza vs benchmark cena danas). Bez toga prinos nema značenje.
"""

import csv
import os
import sys
from datetime import date

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POS = os.path.join(BASE, "data", "positions.csv")
PRED = os.path.join(BASE, "data", "predvidjanja.csv")


def load(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f)
                if r.get("ticker") and not r["ticker"].startswith("#")]
    return rows


def f(v):
    try:
        return float(str(v).replace(",", "."))
    except (TypeError, ValueError):
        return None


def pct(x, nd=2):
    return "N/A" if x is None else f"{x * 100:+.{nd}f}%"


def report_positions():
    rows = load(POS)
    L = []
    L.append(f"PAPER PORTFOLIO — {date.today().isoformat()}")
    L.append("=" * 78)
    if not rows:
        L.append("Nema pozicija u data/positions.csv.")
        return "\n".join(L), None

    open_rows = [r for r in rows if (r.get("status", "open").strip().lower() == "open")]
    L.append("")
    L.append(f"{'Tiker':<8}{'Ulaz':<12}{'Cena ul.':>10}{'Cena sad':>10}"
             f"{'Prinos':>10}{'VUAA':>10}{'Alfa':>10}")
    L.append("-" * 78)

    tot_w, tot_p, tot_b, valid = 0.0, 0.0, 0.0, 0
    for r in rows:
        ep, cp = f(r.get("entry_price")), f(r.get("current_price"))
        bep, bcp = f(r.get("benchmark_entry_price")), f(r.get("benchmark_current_price"))
        w = f(r.get("weight")) or 1.0
        ret = (cp / ep - 1) if (ep and cp) else None
        bret = (bcp / bep - 1) if (bep and bcp) else None
        alfa = (ret - bret) if (ret is not None and bret is not None) else None
        st = "" if r.get("status", "open").strip().lower() == "open" else " [zatvoreno]"
        L.append(f"{r['ticker']:<8}{r.get('entry_date', ''):<12}"
                 f"{('N/A' if ep is None else f'{ep:.2f}'):>10}"
                 f"{('N/A' if cp is None else f'{cp:.2f}'):>10}"
                 f"{pct(ret, 1):>10}{pct(bret, 1):>10}{pct(alfa, 1):>10}{st}")
        if ret is not None and bret is not None:
            tot_w += w
            tot_p += ret * w
            tot_b += bret * w
            valid += 1

    L.append("-" * 78)
    if tot_w > 0:
        pr, br = tot_p / tot_w, tot_b / tot_w
        L.append(f"{'UKUPNO':<8}{'':<12}{'':>10}{'':>10}{pct(pr, 1):>10}{pct(br, 1):>10}"
                 f"{pct(pr - br, 1):>10}")
        L.append("")
        L.append(f"Pozicija sa validnim podacima: {valid} | Otvorenih: {len(open_rows)}")
        L.append("")
        L.append("INTERPRETACIJA — obavezno pročitati:")
        L.append(f"  Alfa od {pct(pr - br, 1)} na {valid} pozicija kroz ovaj period je")
        L.append("  STATISTIČKI BEZ ZNAČENJA. Tracking error portfolija od ~10 akcija je")
        L.append("  8-12% godišnje; sve unutar +/-20% je normalan šum. Ovo je KONTEKST,")
        L.append("  ne rezultat. Rezultat se meri u data/predvidjanja.csv.")
        L.append("  Detalji: docs/04-sta-ovo-moze-da-dokaze.md")
        return "\n".join(L), (pr - br)
    L.append("Nema dovoljno podataka za izračun (popuni current_price i benchmark cene).")
    return "\n".join(L), None


def report_predictions():
    rows = load(PRED)
    L = []
    L.append("")
    L.append("TAČNOST PREDVIĐANJA FUNDAMENATA — glavni test sistema")
    L.append("=" * 78)
    if not rows:
        L.append("Nema zapisa u data/predvidjanja.csv.")
        L.append("Pri svakom ulazu upiši 5 merljivih predviđanja za 4 kvartala unaprijed.")
        return "\n".join(L)

    scored = [r for r in rows if (r.get("ishod", "").strip().lower()
                                 in ("tacno", "netacno", "tačno", "netačno"))]
    def is_true(r):
        return r["ishod"].strip().lower() in ("tacno", "tačno")

    by_ticker, by_conf = {}, {}
    for r in scored:
        by_ticker.setdefault(r["ticker"], []).append(is_true(r))
        c = r.get("uverenost", "?").strip()
        by_conf.setdefault(c, []).append(is_true(r))

    L.append(f"Ocenjeno: {len(scored)} od {len(rows)} predviđanja")
    if not scored:
        L.append("Još nijedno predviđanje nije ocenjeno — sačekaj kvartalne izveštaje.")
        return "\n".join(L)

    hit = sum(1 for r in scored if is_true(r)) / len(scored)
    L.append(f"Ukupna tačnost: {hit * 100:.0f}%")
    L.append("")
    L.append("  Referenca: ~50% = tvoj okvir ne razlikuje ništa (isto kao slučajno).")
    L.append("            70%+ na 40+ ocenjenih predviđanja = signal sa sadržajem.")
    if len(scored) < 30:
        L.append(f"  ⚠ Uzorak od {len(scored)} je previše mali za zaključak. Treba 40+.")
    L.append("")

    L.append("Po poziciji:")
    for t, v in sorted(by_ticker.items()):
        L.append(f"  {t:<8} {sum(v)}/{len(v)}  ({sum(v) / len(v) * 100:.0f}%)")
    L.append("")
    L.append("Kalibracija po nivou uverenosti (da li 90% teze pogađaju ~90%?):")
    for c, v in sorted(by_conf.items()):
        L.append(f"  uverenost {c:<6} → realizovano {sum(v) / len(v) * 100:.0f}% "
                 f"({sum(v)}/{len(v)})")
    L.append("")
    L.append("  Ako je realizovano znatno ispod deklarisane uverenosti, sistematski si")
    L.append("  prekomerno samouveren. To je merljivo i ispravljivo.")
    return "\n".join(L)


def main():
    only_pred = "--predvidjanja" in sys.argv
    if not only_pred:
        txt, _ = report_positions()
        print(txt)
    print(report_predictions())


if __name__ == "__main__":
    main()
