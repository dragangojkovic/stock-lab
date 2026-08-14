# SCORECARD — Otis Worldwide Corporation (OTIS)
Sektor: Industrija - liftovi/eskalatori (Elevators & Escalators) | Valuta: USD (miliони) | Podaci: 5 god. | Generisano: 2026-08-14

## HARD KAPIJE

| # | Kapija | Vrednost | Ishod |
|---|---|---|---|
| G1 | ROIC ≥ 12% i spread nad WACC ≥ 3pp | NIJE PRIMENLJIVO (equity -5392 je negativan) | **N/P** |
| G2 | Neto dug/EBITDA ≤ 3.0x i pokrivenost kamata ≥ 4x | ND/EBITDA 2.97x, kamate 9.8x | **PROŠAO** |
| G3 | FCF pozitivan u ≥ 4 od 5 godina | 5 od 5 poznatih | **PROŠAO** |
| G4 | FCF konverzija (FCF/NI, 5g prosek) ≥ 0.7 | 1.08 | **PROŠAO** |
| G5 | Moat artikulisan u 2 rečenice | DA | **PROŠAO** |
| G6 | Nije u isključenom sektoru | u redu | **PROŠAO** |

Prošlo: 5 | Palo: 0 | Nepoznato: 0 | Nije primenljivo: 1
- ⚠ G1: Equity je negativan (tipično: spinoff finansiran dugom + agresivan buyback, vidi OTIS/docs/05 §4) — dug i equity se skoro poništavaju u imeniocu ROIC-a, pa investirani kapital može ispasti mali ali POZITIVAN (promaši capital_light prag) dok je i dalje besmislen kao mera uloženog kapitala. Ne veruj apsolutnoj vrednosti ROIC-a ovde, ma koliko stabilna izgledala. Koristi Neto dug/EBITDA, pokrivenost kamata i FCF konverziju kao primarne signale K1/K3 umesto ROIC-a i D/E.

## K1 — ROIC
- Medijana (5g): **145.1%** | Trend: **stabilan**
- WACC: N/A | Spread: **N/A**

| Godina | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| ROIC | 73.3% | 207.9% | 230.5% | 145.1% | 109.3% |

## K2 — Marže (razlaganje)
| Marža | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Trend |
|---|---|---|---|---|---|---|
| Bruto | 29.3% | 28.6% | 29.5% | 29.9% | 30.3% | — |
| **Operativna** | 14.7% | 14.9% | 15.4% | 14.1% | 14.8% | **stabilan** |
| Neto | 8.7% | 9.2% | 9.9% | 11.5% | 9.6% | RASTE |

> Operativna marža je glavni pokazatelj efikasnosti poslovanja. Gap bruto→operativna = SG&A + R&D (investicija, ne nužno neefikasnost).
> **Obavezno: uporedi ove marže sa 3–5 konkurenata pre zaključka.**

## K3 — Zaduženost
| Metrika | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Neto dug/EBITDA | 2.47x | 2.51x | 2.36x | 2.75x | 2.97x |
| Pokrivenost kamata | 15.5x | 14.5x | 14.1x | 11.0x | 9.8x |
| D/E | -2.01 | -1.39 | -1.40 | -1.72 | -1.48 |

⚠ **D/E je besmislen** — equity je negativan (-5392), imenilac je negativan pa je i sam odnos negativan/beznačajan. Ignoriši D/E, koristi samo Neto dug/EBITDA i pokrivenost kamata (vidi `docs/05` §3).

**Test produktivnosti duga** (dug ne sme rasti brže od EBIT/FCF):
- Dug CAGR: 2.3% | EBIT CAGR: 0.3% | FCF CAGR: -2.4% | Prihod CAGR: 0.2%
- Verdikt: **dug NIJE bio produktivan**

## K4 — Free Cash Flow
| Metrika | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| OCF | 1750 | 1560 | 1627 | 1563 | 1596 |
| CapEx | 156 | 115 | 138 | 126 | 152 |
| **FCF** | 1594 | 1445 | 1489 | 1437 | 1444 |
| FCF nakon SBC | 1529 | 1378 | 1425 | 1364 | 1364 |
| FCF/NI | 1.28 | 1.15 | 1.06 | 0.87 | 1.04 |
| OCF/NI | 1.40 | 1.25 | 1.16 | 0.95 | 1.15 |

- FCF konverzija (prosek): **1.08** (cilj ≥ 0.70)
- OCF/NI (prosek): 1.18 — ako je uporno < 1.0, zarada je 'na papiru'
- SBC/Prihod (zadnja god.): 0.6%
- Rast broja akcija (CAGR): -2.2%

**Kvalitet obrtnog kapitala** (potraživanja/zalihe ne smeju rasti brže od prihoda):
- Potraživanja CAGR: 3.4% vs Prihod CAGR: 0.2%
- Zalihe CAGR: -0.4% vs Prihod CAGR: 0.2%

## K5 — Valuacija
- P/E: N/A
- EPS CAGR (istorijski 4g): 4.9% → **PEG_trailing = N/A**
- Konsenzus EPS rast (3g): N/A → **PEG_forward = N/A**
- FCF yield na EV: **N/A** (nakon SBC: N/A) ← ne zavisi od projekcija

**Kontrola: da li je rast EPS-a stvaran ili buyback?**
- Prihod CAGR: 0.2% | EPS CAGR: 4.9% | FCF/akcija CAGR: -0.3%

---
*Ovaj scorecard nije preporuka. Kapije i signali su ulaz u analizu, ne zamena za nju. Popuni `templates/analiza.md` pre bilo kakve odluke.*
