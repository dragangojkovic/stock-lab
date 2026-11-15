# AMD — osvežen scorecard sa cenom od 2026-11-13 (nova datirana evidencija)

**Datum zapisa:** 2026-11-15 | **Cena:** 534,06 USD (IBKR zaključna, petak 2026-11-13; prefiks 'C' tumačen kao 'close', potvrditi); VUAA 145,70.
Prethodna evidencija (`data/AMD.json`, `analize/AMD.md`, `analize/AMD-scorecard.md`, cena 459,61 od 2026-09-03) **nije menjana**.
Fundamentalni ulazi su isti (FY2021–FY2025, 10-K); menjaju se samo cena (+16,2%) i WACC (rf 5,15% umesto 4,79%; beta 2,49 iz 2026-09-02 NIJE osvežena, treća strana) → WACC ~16,3% (napomena u JSON kopiji, skriptu u scratchpad-u).
Bez TTM/10-Q osvežavanja fundamenata: ROIC i marže su i dalje do FY2025.

**Šta se promenilo:** P/E 173,4 → 201,5; FCF yield na EV 0,63% (nakon SBC 0,45%); PEG_trailing 262 (EPS CAGR samo 0,8%); G1 i dalje PAO (spread −13,5pp). Ostale kapije prolaze; G5 "prošao" je samo prisustvo placeholder teksta.

---

# SCORECARD — Advanced Micro Devices, Inc. (AMD)
Sektor: Poluprovodnici | Valuta: USD (miliони) | Podaci: 5 god. | Generisano: 2026-11-15

## HARD KAPIJE

| # | Kapija | Vrednost | Ishod |
|---|---|---|---|
| G1 | ROIC ≥ 12% (5g medijana) i spread nad WACC ≥ 3pp | medijana 2.8%, WACC 16.3%, spread -13.5% | **PAO** |
| G2 | Neto dug/EBITDA ≤ 2.0x i pokrivenost kamata ≥ 4x | ND/EBITDA -0.35x, kamate 28.2x | **PROŠAO** |
| G3 | FCF pozitivan u ≥ 4 od 5 godina | 5 od 5 poznatih | **PROŠAO** |
| G4 | FCF konverzija (FCF/NI, 5g prosek) ≥ 0.7 | 1.49 | **PROŠAO** |
| G5 | Moat artikulisan u 2 rečenice | DA | **PROŠAO** |
| G6 | Nije u isključenom sektoru | u redu | **PROŠAO** |

Prošlo: 5 | Palo: 1 | Nepoznato: 0 | Nije primenljivo: 0

> **Kapija je pala.** Akcija ispada iz razmatranja, osim ako se napiše eksplicitno obrazloženje override-a u analizi.

## K1 — ROIC
- Medijana (5g): **2.8%** | Trend: **PADA**
- WACC: 16.3% | Spread: **-13.5%**

| Godina | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| ROIC | 59.5% | 2.7% | 1.2% | 2.8% | 6.2% |

## K2 — Marže (razlaganje)
| Marža | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Trend |
|---|---|---|---|---|---|---|
| Bruto | 48.2% | 44.9% | 46.1% | 49.4% | 49.5% | — |
| **Operativna** | 22.2% | 5.4% | 1.8% | 7.4% | 10.7% | **PADA** |
| Neto | 19.2% | 5.6% | 3.8% | 6.4% | 12.5% | PADA |

> Operativna marža je glavni pokazatelj efikasnosti poslovanja. Gap bruto→operativna = SG&A + R&D (investicija, ne nužno neefikasnost).
> **Obavezno: uporedi ove marže sa 3–5 konkurenata pre zaključka.**

## K3 — Zaduženost
| Metrika | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Neto dug/EBITDA | -0.55x | -0.44x | -0.38x | -0.42x | -0.35x |
| Pokrivenost kamata | 107.3x | 14.4x | 3.8x | 20.7x | 28.2x |
| D/E | 0.04 | 0.05 | 0.04 | 0.03 | 0.05 |

**Test produktivnosti duga** (dug ne sme rasti brže od EBIT/FCF):
- Dug CAGR: 79.1% | EBIT CAGR: 0.3% | FCF CAGR: 14.4% | Prihod CAGR: 20.5%
- Verdikt: **dug NIJE bio produktivan**

## K4 — Free Cash Flow
| Metrika | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| OCF | 3521 | 3565 | 1667 | 3041 | 6493 |
| CapEx | 301 | 450 | 546 | 636 | 974 |
| **FCF** | 3220 | 3115 | 1121 | 2405 | 5519 |
| FCF nakon SBC | 2841 | 2034 | -263 | 998 | 3881 |
| FCF/NI | 1.02 | 2.36 | 1.31 | 1.47 | 1.27 |
| OCF/NI | 1.11 | 2.70 | 1.95 | 1.85 | 1.50 |

- FCF konverzija (prosek): **1.49** (cilj ≥ 0.70)
- OCF/NI (prosek): 1.82 — ako je uporno < 1.0, zarada je 'na papiru'
- SBC/Prihod (zadnja god.): 4.7%
- Rast broja akcija (CAGR): 7.4%

**Kvalitet obrtnog kapitala** (potraživanja/zalihe ne smeju rasti brže od prihoda):
- Potraživanja CAGR: 23.6% vs Prihod CAGR: 20.5%
- Zalihe CAGR: 41.9% vs Prihod CAGR: 20.5%

## K5 — Valuacija
- P/E: 201.53
- EPS CAGR (istorijski 4g): 0.8% → **PEG_trailing = 261.97**
- Konsenzus EPS rast (3g): N/A → **PEG_forward = N/A**
- FCF yield na EV: **0.6%** (nakon SBC: 0.4%) ← ne zavisi od projekcija

**Kontrola: da li je rast EPS-a stvaran ili buyback?**
- Prihod CAGR: 20.5% | EPS CAGR: 0.8% | FCF/akcija CAGR: 6.5%

---
*Ovaj scorecard nije preporuka. Kapije i signali su ulaz u analizu, ne zamena za nju. Popuni `templates/analiza.md` pre bilo kakve odluke.*
