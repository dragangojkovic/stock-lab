# Analiza: Parker-Hannifin Corporation (PH)

**Datum:** 2026-09-06 | **Analitičar:** Dragan | **Cena na dan analize:** 962.59 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — motion/control industrijska proizvodnja nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

Parker-Hannifin je lider u pokretnoj i kontrolnoj tehnologiji — hidraulika, pneumatika, filtracija, fluid connectors, motion systems, inženjerski materijali — organizovan u dva segmenta: Diversified Industrial (77% prihoda FY2023) i Aerospace Systems (23% prihoda FY2023, prodaje direktno OEM-ovima i krajnjim korisnicima).

- Izvori prihoda i njihov udeo: Diversified Industrial 77%, Aerospace Systems 23% (FY2023 podatak, noviji % nije bio predmet ovog istraživanja — N/A, treba proveriti u FY2025 10-K).
- Ko su kupci: ~548.000 kupaca u gotovo svakoj proizvodnoj/transportnoj/procesnoj industriji — OEM proizvođači i distributeri (Diversified Industrial), OEM-i i krajnji korisnici direktno (Aerospace).
- Kako se naplaćuje: prodaja proizvoda/komponenti, delom sa ponavljajućim prihodom od aftermarket/replacement delova.
- Koncentracija: potvrđeno u FY2023 10-K — "No single customer accounted for more than four percent of our total net sales." Nema materijalne koncentracije kupaca.

## 2. Moat — dve rečenice (obavezna kapija)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/PH.json`:

```
SCORECARD — Parker-Hannifin Corporation (PH)
Sektor: Industrija - pokretna i kontrolna tehnologija | Podaci: 5 god. (fiskalna, zavrsava 30.6.)

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 12.9%, WACC 9.7%, spread 3.2% - PROŠAO (GRANIČNO)
G2 ND/EBITDA≤3.0x i pokrivenost≥4x: 1.78x, 9.9x - PROŠAO (probijeno FY2022-2023, vidi ispod)
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 1.26 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 6/6, Palo 0 - ali G1 spread je TIK IZNAD praga (3.2% vs minimum 3.0pp)

K1 ROIC: medijana 12.9%, trend RASTE ali sa dubokim V-oblikom (12.9%→11.6%→10.7%→13.6%→15.5%)
  - dno u FY2023 (10.7%) tacno poklapa sa godinom posle Meggitt akvizicije. WACC 9.7% (beta
  nekonzistentna izmedju izvora, koriscen prosek - vidi napomenu u JSON-u), spread 3.2%.
K2 Marže: bruto 33.1%→36.9% (RASTE), operativna 16.4%→20.5% (RASTE, V-oblik tokom Meggitt godina),
  neto 12.2%→8.3%→17.8% (RASTE, najveci pad u FY2022 zbog akvizicionih troskova/kamata).
K3 Zaduženost: ND/EBITDA 1.98x(FY21)→3.24x(FY22, PROBIJA docs/05 prag 3.0x)→3.10x(FY23, i dalje
  iznad praga)→2.14x(FY24)→1.78x(FY25). Pokrivenost kamata NIKAD ispod 4x (najnize 5.4x FY23).
  Test produktivnosti duga: dug CAGR 9.0% vs EBIT CAGR 14.5% vs FCF CAGR 9.0% → dug PRODUKTIVAN
  (iako je privremeno probio ND/EBITDA prag, EBIT je rastao brze od duga kroz ceo period).
K4 FCF: pozitivan 5/5, FCF konverzija prosek 1.26, OCF/NI prosek 1.40. SBC/prihod 0.8% (nisko).
  Potraživanja CAGR 7.4% i zalihe CAGR 7.9% oba blago ispod prihoda (8.5%) - u redu.
K5 Valuacija: P/E 35.49 (NAJSKUPLJE od tri industrijska kandidata). PEG_trailing 1.83 (istorijski
  EPS CAGR 19.4% - delom naduvan FY2022 padom pa oporavkom), PEG_forward 3.57 (konsenzus rast
  samo 9.9% - drasticno nize od trailing, ocekivano usporavanje EPS rasta). FCF yield na EV 2.5%
  (najnizi od tri kandidata). EPS CAGR (19.4%) znacajno nadmasuje Prihod CAGR (8.5%) - proveri
  koliko dolazi od marze/buyback-a vs stvarnog rasta posla (vidi K5 upozorenje u scorecard-u).
```

**Kapije:** prošlo 6/6 | palo 0 | nepoznato 0
**Override:** Nije formalno potreban (sve kapije prolaze), ALI G1 spread (3.2%) je tik iznad minimalnog praga od 3pp — da je WACC procenjen samo 0.3pp više (npr. da je korišćena viša beta 1.26 umesto proseka 1.19), kapija bi PALA. Ovo zaslužuje eksplicitnu napomenu u §6, ne tretirati kao komotno prolaznu kapiju.

## 4. Poređenje sa konkurencijom

| Metrika | PH | Eaton (ETN) | Honeywell (HON) | Medijana grane |
|---|---|---|---|---|
| ROIC (5g med. za PH; FY2025 za konk.) | 12.9% | N/A — treba proveriti (EBIT nije XBRL-tagovan u ETN FY2025 filing-u) | 18.2% | N/A |
| Bruto marža | 36.9% (FY2025) | 37.6% (FY2025) | 36.9% (FY2025) | ~37% |
| Operativna marža | 20.5% (FY2025) | N/A — treba proveriti | 21.7% (FY2025) | N/A |
| Neto marža | 17.8% (FY2025) | 14.9% (FY2025) | 12.6% (FY2025) | ~15% |
| Neto dug/EBITDA | 1.78x (FY2025) | N/A — treba proveriti (EBIT/EBITDA nedostupno) | ~2.36x (nepotpuni D&A, gornja granica) | N/A |
| P/E | 35.49 | N/A — treba proveriti | N/A — treba proveriti | N/A |
| PEG (trailing) | 1.83 | N/A | N/A | N/A |
| FCF yield na EV | 2.5% | N/A | N/A | N/A |

*Izvor Eaton: SEC EDGAR 10-K FY2025, CIK 0001551182, accession 0001551182-26-000007 — EBIT/operating income NIJE posebno XBRL-tagovan (samo pretax income $4,932.0M), pa ROIC/operativna marža/leverage ostaju N/A radije nego procena. Eaton NIJE imenovan konkurent u PH-ovom sopstvenom 10-K (Parker ne imenuje nikog), ali je najčešće citiran peer u motion/control/hidraulika prostoru. Izvor Honeywell: CIK 0000773840, accession 0000773840-26-000013 (isti podaci korišćeni i za ITW poređenje).*

**Ako marža pada — pada li svima u grani ili samo njoj?** PH marže NE padaju u trendu — i bruto i operativna i neto marža RASTU kroz 5 godina (uz privremeni pad u FY2022 tokom Meggitt integracije). PH ima BOLJU neto maržu od oba komparatora (17.8% vs 14.9% Eaton, 12.6% Honeywell), ali operativna marža (20.5%) je blago ispod Honeywell-a (21.7%) — razlika nije velika. Meggitt integracija (aerospace fokus) izgleda da doprinosi margin-mix poboljšanju (Aerospace Systems segment tipično nosi više marže od Diversified Industrial), konzistentno sa oporavkom marži nakon FY2022-2023 dna.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 1.83 | prošli EPS rast (19.4% CAGR) se nastavlja |
| PEG_forward | 3.57 | konsenzus analitičara (9.9% EPS rast) je tačan |
| FCF yield na EV | 2.5% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 2.4% | dilucija je realan trošak (ovde manje bitna, SBC/prihod 0.8%) |

**Razlika između PEG_trailing i PEG_forward:** VELIKA — 1.83 vs 3.57, skoro duplo. Konsenzus (9.9%) je upola niži od trailing EPS CAGR-a (19.4%). Trailing broj je delom artefakt V-oblika (FY2022 dno pa oporavak) — 4-godišnji CAGR računat od niske FY2022 baze prirodno preuveličava "rast". Konsenzus od 9.9% je verovatno realniji pokazatelj održivog tempa. PEG_forward od 3.57 (najviši od tri industrijska kandidata) sugeriše da je PH trenutno najskuplji od ITW/ROP/PH po ovom pokazatelju, uprkos time što ima najslabiji standardni ROIC (12.9% medijana, granično iznad opšteg praga).

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 8. Odluka

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2025 income statement | SEC EDGAR 10-K FY2025, CIK 0000076334 | accession 0000076334-25-000035, R3.htm | pristupljeno 2026-09-04, licno verifikovano |
| FY2021-2024 podaci (restatovano za COGS/SG&A reklasifikaciju) | SEC EDGAR 10-K FY2023/FY2024, CIK 0000076334 | accession 0000076334-23-000042, 0000076334-24-000044 | pristupljeno 2026-09-04 |
| Cena zatvaranja PH | IBKR (TradingView chart, NYSE) | screenshot, 04.09.2026 zaključna sveća | 2026-09-04 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-04 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, NEKONZISTENTNA između dva poziva (1.12 vs 1.26), korišćen prosek 1.19, treba nezavisna verifikacija | N/A — treba proveriti tačan URL | pristupljeno 2026-09-04 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-06 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, drugi izvor (Simply Wall St 7.9%) daje nešto niže, flagovano kao raspon | https://finviz.com/quote.ashx?t=PH | pristupljeno 2026-09-06 |
| Eaton, Honeywell komparativni podaci | SEC EDGAR 10-K FY2025 | accession brojevi navedeni u §4 | pristupljeno 2026-09-06 |
