# Analiza: Robinhood Markets, Inc. (HOOD) — IZUZETAK OD §4

**Datum:** 2026-11-15 | **Analitičar:** Dragan (pripremio Claude) | **Cena na dan analize:** 77,86 USD (IBKR zaključna, petak 2026-11-13; prefiks 'C' tumačen kao 'close', potvrditi); VUAA 145,70
**U krugu kompetencije:** DELIMIČNO — fintech/potrošački softver (proizvod i app su razumljivi), ali brokerski bilans i regulatorni rizik nisu.

> **IZUZETAK (odobrio Dragan u chatu, 2026-11-15):** HOOD je brokerski diler — "isključeni sektor" po CLAUDE.md §4
> (brokerski dileri). Pravilo 5 kaže da se staje; vlasnik je izričito odobrio izuzetak. **CLAUDE.md nije menjan.**
> Pet kriterijuma (K1 ROIC, K3 zaduženost, K4 FCF konverzija, K5 PEG/EV) **ne primenjujem i ne pokrećem
> `scorecard.py`** — rezultat bi bio besmislen i bio bi prilagođavanje metrike da analiza "prođe" (§11).
> Umesto toga: činjenice iz SEC izveštaja i metrike koje u brokerskom modelu imaju smisla. Ovo **nije** scorecard i
> **ne ulazi** u kapije; kandidat za paper portfolio je moguć samo uz Draganovu odluku (portfolio je pun, 10/10).

## Zašto standardni okvir ne radi
- **Ukupna aktiva $38,1 mlrd naspram kapitala $9,2 mlrd** (FY2025): većina bilansa su novac i hartije klijenata (obaveze $29,0 mlrd). Dug, EV i "investirani kapital" nisu merljivi na način iz K1/K3.
- **OCF je nepouzdan kao mera zarade**: menja se sa promenama sredstava klijenata i poravnanja — FY2021 −885, FY2022 −852, FY2023 +1.181, FY2024 −157, FY2025 +1.638 ($M) uz neto dobit −3.687 … +1.883. FCF konverzija (G4) bi pala/prošla slučajno.
- **CapEx**: standardni XBRL tag nije dostupan; kapitalizovani softver $39M (FY2025). FCF: **N/A — treba proveriti** (10-K tok gotovine, R-stranica).
- Istorija: IPO jul 2021 → 10-K za FY2021–FY2025 je tačno 5 izveštaja (granica CLAUDE.md §4); FY2021 je iskrivljen IPO-om (SBC $1.572M).

## Podaci (SEC XBRL companyfacts, Form 10-K, CIK 0001783879, preuzeto 2026-11-15)

| $M | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Neto prihod | 1.815 | 1.358 | 1.865 | 2.951 | 4.473 |
| Zarada pre poreza | −3.685 | −1.027 | −533 | 1.064 | 2.108 |
| Porez | 2 | 1 | 8 | −347 | 225 |
| Neto dobit | −3.687 | −1.028 | −541 | 1.411 | 1.883 |
| Diluted EPS ($) | −7,49 | −1,17 | −0,61 | 1,56 | 2,05 |
| Diluted akcije (M, prosek) | 492,4 | 878,6 | 890,9 | 906,2 | 918,8 |
| SBC | 1.572 | 654 | 871 | 304 | 305 |
| Operativni troškovi | 3.456 | 2.369 | 2.401 | 1.897 | 2.379 |
| OCF | −885 | −852 | 1.181 | −157 | 1.638 |
| Kapital | 7.293 | 6.956 | 6.696 | 7.972 | 9.151 |
| Goodwill | 101 | 100 | 175 | 179 | 385 |
| Otkup akcija | 0 | 0 | 608 | 257 | 653 |

Izvedeno (aritmetika iz tabele):
- Prihod +51,6% u FY2025 (2.951→4.473); CAGR FY2021–FY2025 = 25,2%.
- Marža pre poreza FY2025 47,1%; neto marža 42,1% (FY2024 47,8% uz poreski benefit −347).
- ROE FY2025 = 1.883 / prosečan kapital 8.561,5 = 22,0%; FY2024: 1.411 / 7.334 = 19,2%.
- SBC/prihod FY2025 = 6,8%; FY2024 10,3%; broj akcija raste uprkos otkupu (906,2→918,8M, +1,4%).
- Dobit je zarađena samo 2 godine (FY2024–FY2025) — kratak zapis; marže iz FY2025 su na ubrzanju, ne na stabilnom nivou.

## Valuacija (dan 2026-11-13, približno)
- Tržišna kapitalizacija ≈ 77,86 × 918,8M = **$71,5 mlrd** (koristi prosek diluted FY2025; broj akcija na kraju perioda: N/A — treba proveriti).
- P/E (FY2025 EPS 2,05) = **38,0**. P/S = 16,0. Zarada pre poreza ≈ 2,9% prinos na kapitalizaciju (2.108 / 71.500 — samo za red veličine).
- PEG_trailing: nema smisla (EPS CAGR iz negativne baze); PEG_forward: N/A — konsenzus nije dostavljen. FCF yield: N/A (nema pouzdanog FCF-a).

## Šta nedostaje za pravu analizu (N/A — treba proveriti)
Funded customers i ARPU; udeo prihoda od kamata na neto-sredstva vs transakcioni prihod (rizik kamatnih stopa) i payment-for-order-flow (regulatorni rizik); Gold pretplatnici; neto depoziti; kapital i likvidnost regulatora (net capital); dug i troškovi kamata; konkurenti (Schwab, IBKR, Coinbase) i poređenje marži; period-end broj akcija; FCF.
Poređenje sa konkurencijom (§4) **nije urađeno**.

## 2. Moat / 6. Tri opovrgavajuće tačke / 7. Predviđanja / 8. Odluka
*Vlasnikove sekcije — ostavljene prazne. Za predviđanja: kriterijumi iz CLAUDE.md §6 (ROIC, ND/EBITDA…) za HOOD ne važe; ako odlučiš da pratiš poziciju, definišemo metrike posebno (npr. prihod, marža pre poreza, ROE, broj akcija).*

## 9. Izvori

| Podatak | Izvor | Link | Datum |
|---|---|---|---|
| Prihod, zarada pre poreza, porez, neto dobit, EPS, akcije, SBC, OCF, kapital, goodwill, otkup, aktiva, obaveze | SEC XBRL companyfacts (Form 10-K) | data.sec.gov/api/xbrl/companyfacts/CIK0001783879.json | preuzeto 2026-11-15 |
| Cena 77,86 USD | IBKR zaključna (prosledio Dragan) | — | 2026-11-13 |
