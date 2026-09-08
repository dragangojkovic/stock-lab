# Analiza: Tractor Supply Company (TSCO)

**Datum:** 2026-09-08 | **Analitičar:** Dragan | **Cena na dan analize:** 34.99 (IBKR zaključna, 04.09.2026, POST-SPLIT)
**U krugu kompetencije:** NE — ruralna maloprodaja nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

TSCO je najveći ruralni lifestyle retailer u SAD-u, servisira farmere/rančere i stanovnike ruralnih/malih gradova kroz tri brenda: Tractor Supply (2,395 prodavnica, farm/ranch oprema, alati, radna odeća, hrana za kućne ljubimce), Petsense by Tractor Supply (207 malih pet-specialty prodavnica), Allivet (online pet apoteka, akvizicija 30.12.2024).

- Izvori prihoda i njihov udeo: nije segmentno raščlanjeno u dostupnim izvorima — N/A, treba proveriti.
- Ko su kupci: rekreativni farmeri/rančeri i vlasnici zemlje/ljubimaca/stoke u ruralnim/malim gradovima.
- Kako se naplaćuje: prodaja robe u prodavnicama i online, jednokratno po transakciji ali visoko ponavljajuće (potrošna roba — hrana za životinje, potrepštine).
- Koncentracija: nema obelodanjivanja koncentracije kupaca. Nijedan proizvod nije >10% prodaje FY2025.

## 2. Moat — dve rečenice (obavezna kapija)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/TSCO.json`:

```
SCORECARD — Tractor Supply Company (TSCO) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 16.8%, WACC 5.5%, spread 11.4% - PROŠAO
G2 ND/EBITDA≤2.5x i pokrivenost≥4x: 2.93x, 21.2x - PAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 0.57 - PAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 4/6, Palo 2 (G2, G4)

K1 ROIC: medijana 16.8%, trend PADA DOSLEDNO (20.2%→18.2%→16.8%→15.4%→13.8%). WACC 5.5%
  (niska zbog bete 0.47), spread 11.4% i dalje komotan i na dnu trenda.
K2 Marže: bruto 35.2%→36.4% (stabilna/blago raste), operativna ~9.5-10.3% (stabilna),
  neto ~7.1-7.8% (stabilna). Marze NISU problem - problem je zaduzenost i CapEx.
K3 Zaduženost: ND/EBITDA 1.93x→2.93x (PROBIJA prag 2.5x poslednje 2 godine, dug ukljucuje
  lizinge po projektnom pravilu za maloprodaju). Pokrivenost kamata i dalje visoka (21.2x)
  jer je finansijski dug mali deo ukupnog. Test produktivnosti duga PADA (dug CAGR 11.0% >>
  EBIT CAGR 2.9%) - dug (uglavnom lizinzi novih prodavnica) raste mnogo brze od EBIT-a.
K4 FCF: pozitivan 5/5, ALI FCF konverzija prosek SVEGA 0.57 (ISPOD PRAGA 0.70) - visok i
  RASTUCI CapEx (628M->895M) za otvaranje novih prodavnica (~4%/god rast povrsine) trosi
  vecinu FCF-a. OCF/NI je zdrav (prosek 1.28) - problem NIJE kvalitet zarade, vec kapitalni
  intenzitet rasta.
K5 Valuacija: P/E 16.99 (jeftino nominalno). PEG_trailing 3.71, PEG_forward 5.92 (konsenzus
  rast SAMO 2.87% - FLAGOVANO KAO POTENCIJALNO SPLIT-DISTORZOVANO, nije nezavisno potvrdjeno
  drugim izvorom). FCF yield na EV 3.0%.
```

**Kapije:** prošlo 4/6 | palo 2 (G2, G4) | nepoznato 0
**Override:** DVE kapije padaju istovremeno iz ISTOG uzroka — agresivan rast broja prodavnica (~4%/god) troši kapital brže nego što EBIT raste, gurajući i zaduženost (lizinzi novih prodavnica) i FCF konverziju (CapEx) preko granica. Ovo NIJE računovodstveni artefakt (kao WST/EW slučajevi) — ovo je STVARNA kapitalna alokaciona odluka: TSCO bira da reinvestira agresivno u fizičku ekspanziju umesto da maksimizira FCF u kratkom roku. Da li je ovo dobra odluka zavisi od toga da li nove prodavnice generišu ROIC iznad WACC-a (5.5%) — standardni ROIC (13.8% FY2025, iako opada) i dalje je komotno iznad WACC-a, što sugeriše da ekspanzija NIJE destruktivna po vrednost, samo je kapitalno-intenzivna u kratkom roku.

## 4. Poređenje sa konkurencijom

| Metrika | TSCO | Home Depot (HD) | Lowe's (LOW) | Medijana grane |
|---|---|---|---|---|
| ROIC (5g med. za TSCO; FY2025 za konk.) | 16.8% | 20.71% | 22.87% | N/A |
| Bruto marža | 36.4% (FY2025) | 33.3% | 33.5% | N/A |
| Operativna marža | 9.5% (FY2025) | 12.7% | 11.8% | N/A |
| Neto marža | 7.1% (FY2025) | 8.6% | 7.7% | N/A |
| Neto dug/EBITDA | 2.93x (FY2025) | N/A — treba proveriti EBITDA komponente | N/A — negativan equity čini D/E besmislenim, koristi ND/EBITDA | N/A |
| P/E | 16.99 | N/A | N/A | N/A |
| PEG (trailing) | 3.71 | N/A | N/A | N/A |
| FCF yield na EV | 3.0% | N/A | N/A | N/A |

*Izvor Home Depot: SEC EDGAR 10-K, CIK 0000354950, accession 0001628280-26-019436. Izvor Lowe's: CIK 0000060667, accession 0000060667-26-000029. VAŽNA NAPOMENA O UPOREDIVOSTI: HD i Lowe's su 22-44x veći od TSCO po prihodu, opšti home-improvement (pro+DIY) retaileri, NE rural/farm-niša — koriste se samo kao skala/marža benčmark, ne kao moat-ekvivalentni peer-ovi. Lowe's ima NEGATIVAN equity (-$9,917M, veliki buyback) — D/E tamo nije smislen, ND/EBITDA je relevantnija metrika (konzistentno sa CLAUDE.md K1-ALT2 pristupom).*

**Ako marža pada — pada li svima u grani ili samo njoj?** TSCO operativna marža je STABILNA (9.5-10.3%), ne pada. TSCO ima NIŽU operativnu maržu od oba diversifikovana konkurenta (9.5% vs 12.7% HD, 11.8% LOW) — verovatno zbog manjeg obima kupovne moći i niše sa manje predvidljivom potražnjom (poljoprivredni ciklusi) nego opšta home-improvement potražnja. Ovo je strukturna razlika u poslovnom modelu, ne signal pogoršanja.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 3.71 | prošli EPS rast (4.6% CAGR) se nastavlja |
| PEG_forward | 5.92 | konsenzus analitičara (2.87% EPS rast) je tačan |
| FCF yield na EV | 3.0% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 2.8% | dilucija je realan trošak (ovde nebitna, SBC/prihod 0.4%) |

**Razlika između PEG_trailing i PEG_forward:** PEG_forward (5.92) je MNOGO gori od PEG_trailing (3.71) jer je konsenzus rast (2.87%) drastično niži od istorijskog (4.6%). MEĐUTIM, ovaj 2.87% broj je EKSPLICITNO FLAGOVAN kao potencijalno split-distorzovan od strane istraživačkog agenta — finviz "EPS next Y" pokazuje -6.11% za tekuću godinu (moguć jednokratni pad), a cross-check izvor (marketbeat) je pokazao cenu koja ne odgovara post-split rasponu, sugerišući stale/pre-split podatke na tom izvoru. **Ovaj broj treba nezavisno potvrditi pre bilo kakve odluke** — P/E od 16.99 je nominalno jeftino, ali PEG_forward interpretacija zavisi kritično od pouzdanosti ovog konsenzus broja.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 8. Odluka

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2025 income statement | SEC EDGAR 10-K FY2025, CIK 0000916365 | accession 0000916365-26-000014, R3.htm | pristupljeno 2026-09-08, licno verifikovano |
| FY2021-2024 podaci (FY2021-2023 rucno prilagodjeni za 5-za-1 split) | SEC EDGAR 10-K FY2021-2024 | accession brojevi u data/TSCO.json | pristupljeno 2026-09-08 |
| Cena zatvaranja TSCO | IBKR (TradingView chart, NASDAQ) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-08 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-08 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, FLAGOVAN kao potencijalno split-distorzovan, nije nezavisno potvrđen | https://finviz.com/quote.ashx?t=TSCO | pristupljeno 2026-09-08 |
| Home Depot, Lowe's komparativni podaci | SEC EDGAR 10-K | accession brojevi navedeni u §4 | pristupljeno 2026-09-08 |
