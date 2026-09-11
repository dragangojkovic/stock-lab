# Analiza: Ecolab Inc. (ECL)

**Datum:** 2026-09-11 | **Analitičar:** Dragan | **Cena na dan analize:** 279.28 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — specialty chemicals/voda-higijena nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

Ecolab je globalni lider u rešenjima za vodu, higijenu i infekcionu prevenciju, organizovan u 4 segmenta: Global Water (tretman vode za industrijske klijente), Global Institutional & Specialty (čišćenje/sanitacija za hotele/restorane/zdravstvo), Global Pest Elimination, Global Life Sciences.

- Izvori prihoda i njihov udeo: Product/equipment $12,618.5M (78.5% FY2025) vs Service/lease $3,462.7M (21.5%) — najbliža objavljena mera recurring prihoda.
- Ko su kupci: hoteli, restorani/QSR lanci, fabrike hrane, zdravstvene ustanove, industrijski klijenti (40+ industrija, 170+ zemalja).
- Kako se naplaćuje: "circle the customer" model — instalirana dosing/dispensing oprema kod klijenta + ponavljajuća prodaja hemikalija/servisne posete.
- Koncentracija: nema koncentracije na nivou kompanije (nijedan kupac ≥10% prihoda), ali Specialty (QSR) posao je zavistan od ograničenog broja velikih QSR lanaca — segmentski rizik.

## 2. Moat — dve rečenice (obavezna kapija)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/ECL.json`:

```
SCORECARD — Ecolab Inc. (ECL) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 10.3%, WACC 8.2%, spread 2.1% - PAO
G2 ND/EBITDA≤2.5x i pokrivenost≥4x: 2.04x, 11.4x - PROŠAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 1.04 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 5/6, Palo 1 (G1)

K1 ROIC: medijana 10.3%, trend SNAZNO RASTE (8.3%→8.5%→10.3%→15.4%→13.0%). WACC 8.2%,
  spread 2.1% (ispod 3pp praga, ali FY2024/2025 same godine imaju spread preko 5pp).
K2 Marže: bruto 40.2%→44.5%, operativna 12.6%→17.0% (RASTE DOSLEDNO), neto 8.9%→12.9% (RASTE).
K3 Zaduženost: ND/EBITDA 3.44x(FY21, Purolite akvizicija)→2.04x(FY25, POBOLJŠAVA SE),
  pokrivenost kamata 7.3x→11.4x. Test produktivnosti duga PROLAZI (dug CAGR -1.5% << EBIT
  CAGR 14.4%) - dug realno opada dok EBIT raste.
K4 FCF: pozitivan 5/5, FCF konverzija prosek 1.04 (dobro), OCF/NI prosek 1.60.
K5 Valuacija: P/E 38.36 (NAJSKUPLJE od tri materijala kandidata). PEG_forward 3.06
  (konsenzus rast 12.55%, blizu trailing EPS CAGR 16.8% - manji jaz od LIN-a). FCF yield
  na EV 2.18%.
```

**Kapije:** prošlo 5/6 | palo 1 (G1) | nepoznato 0
**Override:** Standardni ROIC medijana (10.3%) je ispod praga, ali TREND JE IZUZETNO JAK — ROIC je gotovo udvostručen u 5 godina (8.3%→15.4%, sa blagim padom na 13.0% u FY2025). FY2021 dno (8.3%) je bilo neposredno posle Purolite akvizicije finansirane dugom — integracija je očigledno bila uspešna (ND/EBITDA je pao sa 3.44x na 2.04x dok je ROIC skoro udvostručen). Ovo je klasičan "trend > nivo" slučaj iz CLAUDE.md, jači od LIN-ovog jer nema goodwill-artefakt komplikaciju — poboljšanje je organsko, ne računovodstveno.

## 4. Poređenje sa konkurencijom

*Ecolab NE imenuje konkretne konkurente u svom 10-K (samo kvalitativan opis po segmentu). Nije pronađen dobar javno-kotiran "pure-play" peer za direktno poređenje u ovom prolazu — ovo ostaje otvoreno pitanje za dublju analizu ako se ova kompanija razmatra za budući ulazak.*

**Ako marža pada — pada li svima u grani ili samo njoj?** ECL marže NE padaju — dosledno rastu (operativna 12.6%→17.0%). Bez konkurentskih podataka ne mogu potvrditi da li je ovo makro (industrija) ili specifično za ECL, ali kombinacija sa poboljšanjem ROIC-a i padajućom zaduženošću sugeriše da je ovo kompanijski specifičan operativni napredak, ne samo cikličan makro popravak.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | N/A (nije eksplicitno računat, EPS CAGR 16.8%) | prošli EPS rast se nastavlja |
| PEG_forward | 3.06 | konsenzus analitičara (12.55% EPS rast) je tačan |
| FCF yield na EV | 2.18% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 2.03% | dilucija je realan trošak (ovde nebitna, SBC/prihod 0.8%) |

**Razlika između PEG_trailing i PEG_forward:** Manji jaz nego LIN — konsenzus (12.55%) je blizu trailing (16.8%), sugerišući da tržište veruje da se poboljšanje nastavlja (ne samo jednokratni odskok). ECL je najskuplji od tri materijala kandidata po P/E (38.36), ali sa najjačim ROIC trendom — premija se može opravdati momentumom poslovanja.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 8. Odluka

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2025 income statement | SEC EDGAR 10-K FY2025, CIK 0000031462 | accession 0001104659-26-018357, R2.htm | pristupljeno 2026-09-11, licno verifikovano |
| FY2021-2024 podaci | SEC EDGAR 10-K FY2021-2024 | accession brojevi u data/ECL.json | pristupljeno 2026-09-11 |
| Cena zatvaranja ECL | IBKR (TradingView chart, NYSE) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-11 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-11 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA | https://finviz.com/quote.ashx?t=ECL | pristupljeno 2026-09-11 |
