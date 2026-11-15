# BA (The Boeing Company) — skrining kapija (nije puna analiza)

**Datum:** 2026-11-15 | **Cena:** 171,50 USD (IBKR zaključna, petak 2026-11-13; prefiks 'C' tumačen kao 'close', potvrditi); VUAA 145,70
**U krugu kompetencije:** NE — avioindustrija/odbrana.
**Izvor:** SEC XBRL companyfacts, Form 10-K (CIK 0000012927), preuzeto 2026-11-15. Samo stavke potrebne za kapije; JSON `data/BA.json` i pun scorecard NISU građeni jer G1 i G3 jasno padaju (dole). Neizračunato = N/A.

| Stavka ($M) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Prihod | 62.286 | 66.608 | 77.794 | 66.517 | 89.463 |
| Operativni profit | −2.870 | −3.519 | −773 | −10.707 | 4.281 |
| Neto dobit | −4.202 | −4.935 | −2.222 | −11.817 | 2.235 |
| OCF | −3.416 | 3.512 | 5.960 | −12.080 | 1.065 |
| CapEx (PP&E) | 980 | 1.222 | 1.527 | 2.230 | 2.942 |
| **FCF (OCF − CapEx)** | **−4.396** | **2.290** | **4.433** | **−14.310** | **−1.877** |
| Kapital (akcionarski) | −14.999 | −15.883 | −17.233 | −3.908 | 5.454 |
| Dug (tekući + dugoročni) | 59.217 | 61.984 | 57.259 | 54.903 | 62.309 |
| Gotovina | 8.052 | 14.614 | 12.691 | 13.801 | 10.921 |

## Kapije
- **G3 PAO:** FCF pozitivan u 2 od 5 godina (cilj ≥ 4).
- **G1 PAO:** operativni profit negativan 4 od 5 godina (FY2021–FY2024) → ROIC negativan; medijana ne može preći 12%. Kapital je negativan do FY2024 (K1-ALT2 slučaj), ali ni to ne pomaže: operativna zarada nije pozitivna.
- **G4 PAO / nije primenljivo:** FCF/neto dobit besmislen jer je neto dobit negativna u 4 od 5 godina.
- **G2 PAO (procena):** neto dug FY2025 = 62.309 − 10.921 = $51.388M. Da bi Neto dug/EBITDA bio ≤ 3,0x, EBITDA bi morao biti ≥ $17.129M, dok je operativni profit $4.281M (D&A: N/A — nije izvučeno; bi morao biti ≥ $12.848M da prođe). Pokrivenost kamata: N/A — kamate nisu izvučene.
- G5, G6: nisu ocenjivane (moat je vlasnikova kapija; sektor aerospace nije isključen).
- FY2025 je prva godina pozitivnog operativnog profita u skoro 5 godina (marža 4,8%), uz FCF i dalje negativan (−$1.877M).

**Zaključak:** pada na ≥ 3 hard kapije (G1, G3, G4) — akcija ispada. Override zahteva pisano obrazloženje (CLAUDE.md §3); nisam ga pisao niti ga predlažem. Trigger za ponovni pogled (predlog, ne odluka): FCF pozitivan 4 od 5 godina i operativna marža > 8% dve godine zaredom.
Ništa nije upisano u `positions.csv` ni `watchlist.csv`.
