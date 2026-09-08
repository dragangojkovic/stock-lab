# Analiza: Thermo Fisher Scientific Inc. (TMO)

**Datum:** 2026-09-08 | **Analitičar:** Dragan | **Cena na dan analize:** 613.78 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — life sciences alati/instrumenti/dijagnostika nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

TMO je najveći svetski dobavljač life sciences alata — reagensi, instrumenti, potrošni materijal za biološka/medicinska istraživanja, dijagnostiku i farmaceutsku/biotech industriju, organizovan u 4 segmenta: Life Sciences Solutions, Analytical Instruments, Specialty Diagnostics, Laboratory Products and Biopharma Services (uključuje PPD — kontraktna klinička istraživanja/CRO, i Patheon — kontraktna proizvodnja).

- Izvori prihoda i njihov udeo (FY2025): Product $25,965M (58.3%), Service $18,592M (41.7% — uključuje PPD/Patheon kontraktne usluge, NIJE isto što i "recurring potrošni materijal" metrika).
- Ko su kupci: farma/biotech kompanije, bolnice i klinički dijagnostički laboratoriji, univerziteti/istraživačke institucije, državne agencije, industrijski/environmentalni/QC kupci.
- Kako se naplaćuje: prodaja instrumenata (jednokratno) + ponavljajuća prodaja reagensa/potrošnog materijala + kontraktne usluge (PPD/Patheon, višegodišnji ugovori).
- Koncentracija: nema obelodanjivanja koncentracije kupaca u 10-K — N/A, nije obelodanjeno.

## 2. Moat — dve rečenice (obavezna kapija)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/TMO.json`:

```
SCORECARD — Thermo Fisher Scientific Inc. (TMO) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 8.9%, WACC 7.9%, spread 1.0% - PAO
G2 ND/EBITDA≤2.5x i pokrivenost≥4x: 2.81x, 5.5x - PAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 1.02 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 4/6, Palo 2 (G1, G2) - DVE KAPIJE PADAJU

K1 ROIC: medijana 8.9%, trend PADA (12.3%→10.9%→8.9%→8.7%→8.6%). WACC 7.9%, spread svega 1.0%.
K1 ROIC EX-GOODWILL (rucno izracunato, goodwill 42-47% ukupne imovine):
  FY2021 30.0% → FY2022 26.6% → FY2023 22.2% → FY2024 21.5% → FY2025 21.3%
  Medijana ex-goodwill: 22.2%, ALI DOSLEDNO OPADA - suprotan trend od ROP-a.
K2 Marže: bruto 50.1%→40.9% (naglo pao FY2021→FY2022), operativna 25.6%→17.4% (PADA),
  neto 19.7%→15.0% (PADA). FY2021 je verovatno anomalna bazna godina (COVID-testing boom).
K3 Zaduženost: ND/EBITDA 2.41x→2.81x (PROBIJA prag 2.5x poslednje 3 godine), pokrivenost
  kamata pala sa 18.7x na 5.5x. Test produktivnosti duga: dug CAGR 3.1% vs EBIT CAGR -6.3%
  vs FCF CAGR -1.9% → dug NIJE bio produktivan.
K4 FCF: pozitivan 5/5, FCF konverzija prosek 1.02 (dobro), OCF/NI prosek 1.29.
K5 Valuacija: P/E 34.60. PEG_trailing NEGATIVAN (-15.13, EPS CAGR -2.3%) - PEG formula se
  raspada kad je istorijski rast negativan (vidi CLAUDE.md K5 "gde PEG ne radi"). PEG_forward
  3.55 (konsenzus rast 9.8% - implicira preokret trenda). FCF yield na EV 2.4%.
```

**Kapije:** prošlo 4/6 | palo 2 (G1, G2) | nepoznato 0
**Override:** Standardni ROIC ozbiljno potisnut goodwill-om (42-47% imovine, PPD akvizicija $16mlrd 2021 dominira), ali ZA RAZLIKU OD ROP-a, ex-goodwill ROIC OPADA (30.0%→21.3%) umesto da raste, operativna marža PADA (25.6%→17.4%), test produktivnosti duga PADA, i G2 (leverage) je TAKOĐE formalno pao — ne samo G1. Ovo NIJE isti profil kao ROP (gde je jedina slabost bila goodwill-dilucija standardnog ROIC-a uz snažan i poboljšavajući ex-goodwill trend). Ovde postoje DVA nezavisna problema (goodwill dilucija I realno slabljenje marži/leverage-a) — override je znatno teže opravdati.

## 4. Poređenje sa konkurencijom

| Metrika | TMO | Danaher (DHR) | Medijana grane |
|---|---|---|---|
| ROIC standardni (5g med. za TMO; FY2025 za DHR) | 8.9% | 6.0% | ~7% |
| ROIC ex-goodwill (TMO rucno) / Goodwill % imovine | 22.2% / 42-47% | N/A rucno — goodwill 51.7% ukupne imovine (slican profil) | N/A |
| Operativna marža | 17.4% (FY2025) | 19.1% (FY2025) | N/A |
| Neto marža | 15.0% (FY2025) | 14.7% (FY2025) | N/A |
| Neto dug/EBITDA | 2.81x (FY2025) | N/A — treba proveriti (D&A nije XBRL-tagovan u DHR FY2025) | N/A |
| P/E | 34.60 | N/A | N/A |
| PEG (trailing) | -15.13 (raspao se) | N/A | N/A |
| FCF yield na EV | 2.4% | N/A | N/A |

*Izvor Danaher: SEC EDGAR 10-K FY2025, CIK 0000313616, accession 0000313616-26-000062 (isti podaci prikupljeni i korišćeni u analize/ROP.md). Danaher je izabran jer nosi sličan life-sciences/serijski-akvizitorski profil kao TMO — oba su konglomerati u istoj široj life-sciences/dijagnostičkoj industriji. TMO NEMA imenovane konkurente u sopstvenom 10-K.*

**Ako marža pada — pada li svima u grani ili samo njoj?** TMO operativna marža pada strmo (25.6%→17.4%) dok je Danaher-ova marža (19.1%) STABILNIJA i trenutno VIŠA od TMO-ove. Ovo je delimično objašnjivo makro faktorom (FY2021 je bio anomalno visok zbog COVID-testing potražnje kroz ceo life-sciences sektor), ali pad se nastavlja i posle normalizacije (FY2022→FY2025 i dalje pada sa manjim intenzitetom, 18.7%→17.4%), što sugeriše da bar deo pada NIJE čisto ciklični/makro efekat već delom kompanijski specifičan (možda integracija PPD-a, koja nosi niže marže od core instrumenata/reagensa).

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | -15.13 (BESMISLENO) | prošli EPS rast se nastavlja — ali rast je NEGATIVAN (-2.3% CAGR), PEG formula se raspada |
| PEG_forward | 3.55 | konsenzus analitičara (9.8% EPS rast) je tačan |
| FCF yield na EV | 2.4% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 2.3% | dilucija je realan trošak (ovde manje bitna, SBC/prihod 0.7%) |

**Razlika između PEG_trailing i PEG_forward:** Per CLAUDE.md K5, PEG_trailing je BESKORISTAN ovde (negativan istorijski rast — jedan od eksplicitno navedenih slučajeva gde PEG ne radi). PEG_forward od 3.55 pretpostavlja da konsenzus rast od 9.8% predstavlja PREOKRET trenda (EPS CAGR poslednje 4 godine je bio -2.3%). Ovo je snažna pretpostavka koju treba eksplicitno opravdati — trenutno nema jasnog kataliza u podacima (marže i dalje padaju u FY2025) koji bi potkrepio ovako oštar preokret. FCF yield na EV (2.4%, ne zavisi od projekcija) je najniži signal opreza — kompanija generiše relativno mali slobodan novčani tok naspram svoje enterprise vrednosti.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 8. Odluka

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2023-2025 income statement, balance sheet, cash flow | SEC EDGAR 10-K FY2025, CIK 0000097745 | accession 0000097745-26-000018, R5.htm | pristupljeno 2026-09-06, licno verifikovano |
| FY2021-2023 podaci | SEC EDGAR 10-K FY2023, CIK 0000097745 | accession 0000097745-24-000007 | pristupljeno 2026-09-06 |
| Cena zatvaranja TMO | IBKR (TradingView chart, NYSE) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-06 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-08 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, cross-check sa marketbeat.com u sličnom rasponu | https://finviz.com/quote.ashx?t=TMO | pristupljeno 2026-09-08 |
| Danaher (DHR) komparativni podaci | SEC EDGAR 10-K FY2025, CIK 0000313616 | accession 0000313616-26-000062 | pristupljeno 2026-09-06 |
