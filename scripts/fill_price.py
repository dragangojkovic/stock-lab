#!/usr/bin/env python3
"""
fill_price.py — Mission Stock Lab

Popunjava market blok u JSON-u na osnovu jedne unete cene.
Izracunava market cap, EV, P/E i FCF yield iz podataka koji su vec u fajlu.

Upotreba:
    python scripts/fill_price.py data/MANH.json 213.11
    python scripts/fill_price.py data/MANH.json 213.11 --shares 59845.291
    python scripts/fill_price.py data/MANH.json 213.11 --growth 0.08

Argumenti:
    --shares  broj akcija u istoj jedinici kao ostali podaci (hiljade).
              Ako se ne navede, koristi diluted_shares iz zadnje godine.
    --growth  konsenzus EPS rast za 3 god, decimalno (0.08 = 8%).
    --dry     samo prikazi, ne upisuj.

Zasto ovako: cena je jedini podatak koji ne mozes izvuci iz izvestaja, i menja
se svakog dana. Sve ostalo se izvodi. Ovim se izbegava rucna greska u EV formuli
(najcesca greska: zaboravi se oduzeti gotovina).
"""

import json
import sys


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)

    path, price = args[0], float(args[1])
    dry = "--dry" in sys.argv

    shares = None
    growth = None
    for i, a in enumerate(sys.argv):
        if a == "--shares" and i + 1 < len(sys.argv):
            shares = float(sys.argv[i + 1])
        if a == "--growth" and i + 1 < len(sys.argv):
            growth = float(sys.argv[i + 1])

    with open(path, encoding="utf-8") as f:
        d = json.load(f)

    last = d["years"][-1]
    if shares is None:
        shares = last.get("diluted_shares")
        if shares is None:
            print("Nema diluted_shares u zadnjoj godini — navedi --shares.")
            sys.exit(1)

    debt = last.get("total_debt") or 0
    cash = last.get("cash_and_equivalents") or 0
    eps = last.get("diluted_eps")
    ocf = last.get("operating_cash_flow")
    capex = last.get("capex")
    sbc = last.get("stock_based_comp") or 0
    rev = last.get("revenue")

    fcf = (ocf - capex) if (ocf is not None and capex is not None) else None
    mcap = price * shares
    ev = mcap + debt - cash
    pe = (price / eps) if eps else None

    m = d.setdefault("market", {})
    m["price"] = price
    m["market_cap"] = round(mcap, 1)
    m["enterprise_value"] = round(ev, 1)
    m["pe_ratio"] = round(pe, 2) if pe else None
    m["_shares_used"] = shares
    if growth is not None:
        m["consensus_eps_growth_3y"] = growth

    print(f"Fajl:            {path}")
    print(f"Cena:            {price:,.2f}")
    print(f"Akcije (hilj.):  {shares:,.1f}  ({last.get('fy')})")
    print(f"Market cap:      {mcap:,.0f}")
    print(f"  + dug          {debt:,.0f}")
    print(f"  - gotovina     {cash:,.0f}")
    print(f"Enterprise val.: {ev:,.0f}")
    print(f"P/E (trailing):  {pe:,.2f}" if pe else "P/E: N/A")
    if fcf and ev:
        print(f"FCF yield na EV: {fcf / ev * 100:,.2f}%")
        print(f"  nakon SBC:     {(fcf - sbc) / ev * 100:,.2f}%")
    if fcf and rev:
        print(f"FCF marza:       {fcf / rev * 100:,.1f}%")
    if growth is not None and pe:
        peg = pe / (growth * 100) if growth else None
        print(f"PEG_forward:     {peg:,.2f}" if peg else "PEG_forward: N/A")

    if dry:
        print("\n--dry: nije upisano.")
        return

    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print("\nUpisano. Sada pokreni: python scripts/scorecard.py " + path)


if __name__ == "__main__":
    main()