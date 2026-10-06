# CPRT — provera kapija posle FY2026 10-K (datirani zapis, 2026-10-06)

**Ovo je novi datirani zapis, ne zamena.** Originalni `data/CPRT.json` i `analize/CPRT-scorecard.md` ostaju netaknuti (stanje pri ulazu, 2026-08-14).

- **Izvor:** SEC EDGAR 10-K za FY završen 31.07.2026, podneto 2026-09-29, CIK 0000900075, accession `0001193125-26-405731` (R2 bilans, R4 račun dobiti, R7 tokovi gotovine). Lično verifikovano, pristupljeno 2026-10-06.
- **Metod:** 5-godišnji prozor pomeren na FY2022–FY2026 (FY2021 izbačen, FY2026 dodat); FY2022–FY2025 iz postojećeg `data/CPRT.json`. WACC i market blok preuzeti iz zapisa pri ulazu (nisu osveženi, ne utiču na kapije).
- **FY2026 unosi:** COGS = facility operations 1.965.888 + cost of vehicle sales 616.463 (isto kao ranije; prihod − COGS − G&A = EBIT tačno); neto dobit = attributable to Copart 1.484.270; kamata = "Interest paid" 1.866; efektivna stopa 19,32% (354.580 / 1.834.977); gotovina bez HTM hartija (1.907.901; HTM 2.581.901 nije u gotovini — konzervativno, kao i ranije).
- **Zaključak:** svih 6 kapija prolazi. Za praćenje: prihod +0,4% god/god (naspram ~+10% prethodne godine), ROIC trend pada (18,5% FY2026), operativna marža pada 4. godinu (35,4%), prvi buyback 1,63 mlrd (akcije 967M → 926M), CapEx pao 569M → 337M. Predviđanja za Q1 FY2027 (do 31.10.2026) nisu ocenjena.

---

# SCORECARD — Copart, Inc. (CPRT)
Sektor: Potrošnja/distribucija - aukcije havarisanih vozila | Valuta: USD (hiljade) | Podaci: 5 god. | Generisano: 2026-10-06

## HARD KAPIJE

| # | Kapija | Vrednost | Ishod |
|---|---|---|---|
| G1 | ROIC ≥ 12% (5g medijana) i spread nad WACC ≥ 3pp | medijana 21.6%, WACC 9.2%, spread 12.4% | **PROŠAO** |
| G2 | Neto dug/EBITDA ≤ 3.0x i pokrivenost kamata ≥ 4x | ND/EBITDA -1.01x, kamate 885.6x | **PROŠAO** |
| G3 | FCF pozitivan u ≥ 4 od 5 godina | 5 od 5 poznatih | **PROŠAO** |
| G4 | FCF konverzija (FCF/NI, 5g prosek) ≥ 0.7 | 0.76 | **PROŠAO** |
| G5 | Moat artikulisan u 2 rečenice | DA | **PROŠAO** |
| G6 | Nije u isključenom sektoru | u redu | **PROŠAO** |

Prošlo: 6 | Palo: 0 | Nepoznato: 0 | Nije primenljivo: 0

## K1 — ROIC
- Medijana (5g): **21.6%** | Trend: **PADA**
- WACC: 9.2% | Spread: **12.4%**

| Godina | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| ROIC | 34.5% | 23.5% | 20.8% | 21.6% | 18.5% |

## K2 — Marže (razlaganje)
| Marža | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Trend |
|---|---|---|---|---|---|---|
| Bruto | 45.9% | 44.9% | 45.0% | 45.2% | 44.7% | — |
| **Operativna** | 39.3% | 38.4% | 37.1% | 36.5% | 35.4% | **stabilan** |
| Neto | 31.1% | 32.0% | 32.2% | 33.4% | 31.8% | stabilan |

> Operativna marža je glavni pokazatelj efikasnosti poslovanja. Gap bruto→operativna = SG&A + R&D (investicija, ne nužno neefikasnost).
> **Obavezno: uporedi ove marže sa 3–5 konkurenata pre zaključka.**

## K3 — Zaduženost
| Metrika | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Neto dug/EBITDA | -0.91x | -0.57x | -0.86x | -1.45x | -1.01x |
| Pokrivenost kamata | 82.4x | 568.7x | 502.7x | 840.4x | 885.6x |
| D/E | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

**Test produktivnosti duga** (dug ne sme rasti brže od EBIT/FCF):
- Dug CAGR: N/A | EBIT CAGR: 4.7% | FCF CAGR: 10.8% | Prihod CAGR: 7.4%
- Verdikt: **N/A**

## K4 — Free Cash Flow
| Metrika | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| OCF | 1176683 | 1364210 | 1472564 | 1799750 | 1604492 |
| CapEx | 337448 | 516636 | 510990 | 568990 | 337363 |
| **FCF** | 839235 | 847574 | 961574 | 1230760 | 1267129 |
| FCF nakon SBC | 800270 | 807901 | 926340 | 1192756 | 1228311 |
| FCF/NI | 0.77 | 0.68 | 0.71 | 0.79 | 0.85 |
| OCF/NI | 1.08 | 1.10 | 1.08 | 1.16 | 1.08 |

- FCF konverzija (prosek): **0.76** (cilj ≥ 0.70)
- OCF/NI (prosek): 1.10 — ako je uporno < 1.0, zarada je 'na papiru'
- SBC/Prihod (zadnja god.): 0.8%
- Rast broja akcija (CAGR): -0.2%

**Kvalitet obrtnog kapitala** (potraživanja/zalihe ne smeju rasti brže od prihoda):
- Potraživanja CAGR: 8.8% vs Prihod CAGR: 7.4%
- Zalihe CAGR: -3.3% vs Prihod CAGR: 7.4%

## K5 — Valuacija
- P/E: 19.88
- EPS CAGR (istorijski 4g): 8.2% → **PEG_trailing = 2.42**
- Konsenzus EPS rast (3g): N/A → **PEG_forward = N/A**
- FCF yield na EV: **4.5%** (nakon SBC: 4.4%) ← ne zavisi od projekcija

**Kontrola: da li je rast EPS-a stvaran ili buyback?**
- Prihod CAGR: 7.4% | EPS CAGR: 8.2% | FCF/akcija CAGR: 11.1%

---
*Ovaj scorecard nije preporuka. Kapije i signali su ulaz u analizu, ne zamena za nju. Popuni `templates/analiza.md` pre bilo kakve odluke.*
