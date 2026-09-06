# Analiza: Roper Technologies, Inc. (ROP)

**Datum:** 2026-09-06 | **Analitičar:** Dragan | **Cena na dan analize:** 405.89 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** DELIMIČNO — softverski deo (Application/Network Software, većina prihoda) je adjacent Draganovom IT fokusu, ali portfolio je previše fragmentisan (desetine različitih vertikalnih tržišta) da bi bio dubinski procenjiv.

---

## 1. Šta kompanija zapravo radi

Roper je diversifikovana tehnološka kompanija čija je strategija kapitalna alokacija u niše, odbranjive vertikale — ne organska industrijska proizvodnja. Kupuje (i retko prodaje) tržišno-vodeće softverske/tehnološke firme u fragmentisanim vertikalama (pravo, zdravstvo/ABA terapija, K-12 administracija, osiguranje, građevinarstvo, logistika, verske organizacije, komunalije, vodomeri, medicinski uređaji), pa ih drži kao decentralizovane operativne jedinice.

- Izvori prihoda i njihov udeo (FY2025): Application Software (Aderant, CentralReach, Clinisys, Deltek, Frontline, Procare, Vertafore) 56.7% prihoda; Network Software (ConstructConnect, DAT, iPipeline, Subsplash) i Technology Enabled Products (CIVCO Medical, Neptune, Verathon) čine ostatak.
- Ko su kupci: zavisi od vertikale — advokatske kancelarije (Aderant), ABA terapeuti (CentralReach), K-12 škole (Frontline), osiguravajuće kompanije (Vertafore/iPipeline), komunalna preduzeća (Neptune vodomeri), medicinski uređaji (Verathon/CIVCO).
- Kako se naplaćuje: pretežno softver kao usluga/licenca (recurring), zavisno od segmenta.
- Koncentracija: "During 2025, no customer accounted for 10% or more of any segment or total Company net revenues." Nema dalje raspodele obelodanjeno.

## 2. Moat — dve rečenice (obavezna kapija)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/ROP.json`:

```
SCORECARD — Roper Technologies, Inc. (ROP)
Sektor: Industrija/Softver - diversifikovana tehnologija | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 5.8%, WACC 7.3%, spread -1.4% - PAO
G2 ND/EBITDA≤3.0x i pokrivenost≥4x: 2.87x, 6.9x - PROŠAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 1.40 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 5/6, Palo 1 - KAPIJA JE PALA, zahteva override obrazloženje

K1 ROIC (standardni): medijana 5.8%, trend RASTE (5.1%→5.4%→5.8%→6.0%→6.1%). WACC 7.3%, spread -1.4%.
K1 ROIC EX-GOODWILL (rucno izracunato, goodwill je 57-62% ukupne imovine):
  FY2021 17.1% → FY2022 19.7% → FY2023 21.3% → FY2024 22.5% → FY2025 23.5%
  Medijana ex-goodwill: 21.3%, DOSLEDNO RASTE. Spread nad WACC (7.3%): ~14pp.
K2 Marže: bruto 70.5%→69.2% (blag pad), operativna 25.7%→28.4%→28.3% (stabilan), neto 16.7%→19.4% (RASTE).
K3 Zaduženost: ND/EBITDA 4.08x(FY21)→2.45x(FY23)→2.87x(FY25), pokrivenost kamata 5.3x-10.6x.
  Test produktivnosti duga: dug CAGR 4.1% vs EBIT CAGR 15.8% vs FCF CAGR 11.1% → dug PRODUKTIVAN.
K4 FCF: pozitivan 5/5 (FY2022 depresovan na 536M zbog jednokratnog poreza na Indicor dobitak),
  FCF konverzija prosek 1.40, OCF/NI prosek 1.47. SBC/prihod 2.1%.
  Potraživanja CAGR 9.8% i zalihe CAGR 19.6% OBA rastu sporije/slicno od prihoda (13.1%) - u redu
  osim zaliha koje rastu brze, ali baza je mala (69M->142M), nije materijalno.
K5 Valuacija: P/E 28.58. PEG_trailing 1.67 (istorijski EPS CAGR 17.1%), PEG_forward 2.87
  (konsenzus rast 10.0% - MNOGO nizi od trailing, tipican "postoji vs organski" jaz kod
  serijskih akvizitora gde M&A doprinosi istorijskom rastu ali se ne moze ekstrapolirati bez
  daljih akvizicija iste velicine). FCF yield na EV 4.6%.
```

**Kapije:** prošlo 5/6 | palo 1 (G1) | nepoznato 0
**Override:** Standardni G1 pada isključivo zbog goodwill dilucije (goodwill 57-62% ukupne imovine, klasičan serijski akvizitor — CentralReach $1,850M, Subsplash $800M, Procare $1,860M, Transact Campus $1,607M, Syntellis $1,381M, Frontline Education ~$3,750M, Vertafore ~$5,400M). ROIC ex-goodwill, ručno izračunat po CLAUDE.md K1 metodologiji, je **21.3% medijana i dosledno RASTE svake godine** (17.1%→23.5%) — jači i konzistentniji trend od AME (koji je bio ravan na 28-30%). Spread ex-goodwill nad WACC-om je ~14pp. Ovo je legitiman override kandidat: akvizicije su realan potrošen kapital akcionara (CLAUDE.md napomena), ali standardni ROIC ovde sistematski potcenjuje kvalitet osnovnog poslovanja koje generiše sve viši povrat na (goodwill-isključeni) kapital iz godine u godinu.

## 4. Poređenje sa konkurencijom

| Metrika | ROP | Danaher (DHR) | Medijana grane |
|---|---|---|---|
| ROIC standardni (5g med. za ROP; FY2025 za DHR) | 5.8% | 6.0% | ~6% |
| ROIC ex-goodwill (ROP rucno) / Goodwill % imovine | 21.3% / 57-62% | N/A rucno — ali goodwill 51.7% ukupne imovine (potvrdjeno slican profil) | N/A |
| Bruto marža | 69.2% (FY2025) | 59.1% (FY2025) | N/A |
| Operativna marža | 28.3% (FY2025) | 19.1% (FY2025) | N/A |
| Neto marža | 19.4% (FY2025) | 14.7% (FY2025) | N/A |
| Neto dug/EBITDA | 2.87x (FY2025) | N/A — treba proveriti (D&A nije XBRL-tagovan u FY2025 filing-u) | N/A |
| P/E | 28.58 | N/A — treba proveriti | N/A |
| PEG (trailing) | 1.67 | N/A | N/A |
| FCF yield na EV | 4.6% | N/A | N/A |

*Izvor Danaher: SEC EDGAR 10-K FY2025, CIK 0000313616, accession 0000313616-26-000062. Danaher je izabran kao komparator jer nosi VEOMA SLICAN profil serijskog akvizitora sa goodwill-om na 51.7% ukupne imovine (vs ROP-ovih 57-62%) — oba imaju standardni ROIC potisnut na jednocifren nivo (Danaher 6.0%, ROP 5.8%) iz istog strukturnog razloga. Roper NEMA imenovane konkurente u sopstvenom 10-K (doslovan citat: "no single company competes with us over a significant number of product lines") - Danaher nije formalno imenovan konkurent, vec analitičarski najbliži uporediv profil kapitalne alokacije.*

**Ako marža pada — pada li svima u grani ili samo njoj?** ROP marže NE padaju u trendu — operativna marža stabilna (25.7%→28.3%) i neto marža raste (16.7%→19.4%). ROP ima bolju operativnu i neto maržu od Danaher-a (28.3% vs 19.1%; 19.4% vs 14.7%) uprkos sličnom akvizicijskom profilu — razlika je verovatno u tome što je ROP fokusiraniji na softver (56.7% prihoda) dok je Danaher i dalje pretežno hardversko/dijagnostička kompanija sa nižim strukturnim maržama.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 1.67 | prošli EPS rast (17.1% CAGR) se nastavlja |
| PEG_forward | 2.87 | konsenzus analitičara (10.0% EPS rast) je tačan |
| FCF yield na EV | 4.6% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 4.3% | dilucija je realan trošak (SBC/prihod 2.1%, umereno) |

**Razlika između PEG_trailing i PEG_forward:** ZNAČAJNA — 1.67 vs 2.87. Konsenzus (10.0%) je gotovo upola niži od trailing EPS CAGR-a (17.1%). Ovo je OČEKIVANO i OBJAŠNJIVO za serijskog akvizitora: istorijski EPS rast je delom vođen velikim akvizicijama (Frontline $3.75mlrd, Vertafore $5.4mlrd) koje se ne mogu ekstrapolirati u istom tempu bez pretpostavke da će ROP nastaviti da nalazi i finansira akvizicije slične veličine — konsenzus analitičara implicitno pretpostavlja usporavanje M&A tempa ili organskiji rast. Ovo NIJE crvena zastavica sama po sebi (ROP je nedavno pokazao pojačan tempo akvizicija — $8.96mlrd 2023-2025), ali PEG_trailing od 1.67 je varljivo nizak ako se koristi kao jedini pokazatelj.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 8. Odluka

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2023-2025 income statement, balance sheet, cash flow | SEC EDGAR 10-K FY2025, CIK 0000882835 | accession 0000882835-26-000009 | pristupljeno 2026-09-04, licno verifikovano (R5.htm) |
| FY2021-2022 podaci (restatovano za continuing operations) | SEC EDGAR 10-K FY2022, CIK 0000882835 | accession 0000882835-23-000016, unakrsno provereno u accn 0000882835-24-000008 | pristupljeno 2026-09-04 |
| Cena zatvaranja ROP | IBKR (TradingView chart, NASDAQ) | screenshot, 04.09.2026 zaključna sveća | 2026-09-04 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-04 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-04 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-06 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, cross-check sa S&P Global konsenzusom u sličnom rasponu | https://finviz.com/quote.ashx?t=ROP | pristupljeno 2026-09-06 |
| Danaher (DHR) komparativni podaci | SEC EDGAR 10-K FY2025, CIK 0000313616 | accession 0000313616-26-000062 | pristupljeno 2026-09-06 |
