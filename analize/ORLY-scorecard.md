# SCORECARD — O'Reilly Automotive, Inc. (ORLY)
Sektor: Maloprodaja - auto delovi | Valuta: USD (hiljade) | Podaci: 5 god. | Generisano: 2026-08-19

## HARD KAPIJE

| # | Kapija | Vrednost | Ishod |
|---|---|---|---|
| G1 | ROIC ≥ 12% i spread nad WACC ≥ 3pp | NIJE PRIMENLJIVO (equity -763352 je negativan) | **N/P** |
| G2 | Neto dug/EBITDA ≤ 2.5x i pokrivenost kamata ≥ 4x | ND/EBITDA 2.09x, kamate 14.7x | **PROŠAO** |
| G3 | FCF pozitivan u ≥ 4 od 5 godina | 5 od 5 poznatih | **PROŠAO** |
| G4 | FCF konverzija (FCF/NI, 5g prosek) ≥ 0.7 | 0.96 | **PROŠAO** |
| G5 | Moat artikulisan u 2 rečenice | DA | **PROŠAO** |
| G6 | Nije u isključenom sektoru | u redu | **PROŠAO** |

Prošlo: 5 | Palo: 0 | Nepoznato: 0 | Nije primenljivo: 1
- ⚠ G1: Equity je negativan (tipično: spinoff finansiran dugom + agresivan buyback, vidi OTIS/docs/05 §4) — dug i equity se skoro poništavaju u imeniocu ROIC-a, pa investirani kapital može ispasti mali ali POZITIVAN (promaši capital_light prag) dok je i dalje besmislen kao mera uloženog kapitala. Ne veruj apsolutnoj vrednosti ROIC-a ovde, ma koliko stabilna izgledala. Koristi Neto dug/EBITDA, pokrivenost kamata i FCF konverziju kao primarne signale K1/K3 umesto ROIC-a i D/E.

## K1 — ROIC
- Medijana (5g): **41.7%** | Trend: **PADA**
- WACC: N/A | Spread: **N/A**

| Godina | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| ROIC | 41.7% | 42.7% | 42.7% | 39.7% | 36.0% |

## K1-ALT2 — negativan equity, ROIC i D/E nisu upotrebljivi
- Equity (zadnja god.): **-763352**
- Investirani kapital (zadnja god.): **7534354** (42.4% prihoda) — mali ali pozitivan, promašuje K1-ALT prag
- **Neto dug/EBITDA: 2.09x** ← primarna metrika K3
- **Pokrivenost kamata: 14.7x** ← sigurnosna metrika

> Dug i negativan equity se skoro poništavaju u imeniocu ROIC-a — investirani kapital je artefakt strukture kapitala (spinoff/buyback), ne mera stvarno uloženog kapitala. Ne veruj ROIC medijani iznad ma koliko izgledala stabilna. Teret dokazivanja prelazi na Neto dug/EBITDA, pokrivenost kamata i FCF konverziju.

## K2 — Marže (razlaganje)
| Marža | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Trend |
|---|---|---|---|---|---|---|
| Bruto | 52.7% | 51.2% | 51.3% | 51.2% | 51.6% | — |
| **Operativna** | 21.9% | 20.5% | 20.2% | 19.5% | 19.5% | **stabilan** |
| Neto | 16.2% | 15.1% | 14.8% | 14.3% | 14.3% | stabilan |

> Operativna marža je glavni pokazatelj efikasnosti poslovanja. Gap bruto→operativna = SG&A + R&D (investicija, ne nužno neefikasnost).
> **Obavezno: uporedi ove marže sa 3–5 konkurenata pre zaključka.**

## K3 — Zaduženost
| Metrika | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Neto dug/EBITDA | 1.70x | 1.94x | 2.10x | 2.10x | 2.09x |
| Pokrivenost kamata | 20.2x | 18.7x | 15.8x | 14.6x | 14.7x |
| D/E | -88.32 | -6.17 | -4.51 | -5.78 | -11.12 |

⚠ **D/E je besmislen** — equity je negativan (-763352), imenilac je negativan pa je i sam odnos negativan/beznačajan. Ignoriši D/E, koristi samo Neto dug/EBITDA i pokrivenost kamata (vidi `docs/05` §3).

**Test produktivnosti duga** (dug ne sme rasti brže od EBIT/FCF):
- Dug CAGR: 9.7% | EBIT CAGR: 4.4% | FCF CAGR: -12.9% | Prihod CAGR: 7.5%
- Verdikt: **dug NIJE bio produktivan**

## K4 — Free Cash Flow
| Metrika | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| OCF | 3207310 | 3148250 | 3034084 | 3049576 | 2761993 |
| CapEx | 442853 | 563342 | 1006264 | 1023387 | 1168815 |
| **FCF** | 2764457 | 2584908 | 2027820 | 2026189 | 1593178 |
| FCF nakon SBC | 2739801 | 2558450 | 2000309 | 1997258 | 1558063 |
| FCF/NI | 1.28 | 1.19 | 0.86 | 0.85 | 0.63 |
| OCF/NI | 1.48 | 1.45 | 1.29 | 1.28 | 1.09 |

- FCF konverzija (prosek): **0.96** (cilj ≥ 0.70)
- OCF/NI (prosek): 1.32 — ako je uporno < 1.0, zarada je 'na papiru'
- SBC/Prihod (zadnja god.): 0.2%
- Rast broja akcija (CAGR): -4.8%

**Kvalitet obrtnog kapitala** (potraživanja/zalihe ne smeju rasti brže od prihoda):
- Potraživanja CAGR: 9.4% vs Prihod CAGR: 7.5%
- Zalihe CAGR: 11.7% vs Prihod CAGR: 7.5%

## K5 — Valuacija
- P/E: N/A
- EPS CAGR (istorijski 4g): 9.4% → **PEG_trailing = N/A**
- Konsenzus EPS rast (3g): N/A → **PEG_forward = N/A**
- FCF yield na EV: **N/A** (nakon SBC: N/A) ← ne zavisi od projekcija

**Kontrola: da li je rast EPS-a stvaran ili buyback?**
- Prihod CAGR: 7.5% | EPS CAGR: 9.4% | FCF/akcija CAGR: -8.4%

---
*Ovaj scorecard nije preporuka. Kapije i signali su ulaz u analizu, ne zamena za nju. Popuni `templates/analiza.md` pre bilo kakve odluke.*
