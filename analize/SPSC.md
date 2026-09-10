# Analiza: SPS Commerce, Inc. (SPSC)

**Datum:** 2026-09-10 | **Analitičar:** Dragan | **Cena na dan analize:** 83.00 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** DA — B2B integracija/EDI cloud platforma je direktno adjacent Draganovom enterprise/.NET IT fokusu.

---

## 1. Šta kompanija zapravo radi

SPSC je cloud-bazirana mreža za upravljanje lancem snabdevanja koja povezuje retailere, brendove/dobavljače, distributere, prehrambene lance i logističke provajdere kroz EDI/integraciju podataka. Kupci se "povežu jednom i odmah transaktuju sa hiljadama trgovinskih partnera" — klasičan mrežni efekat flywheel.

- Izvori prihoda i njihov udeo: recurring prihod 96% (FY2025), 94% (FY2024), 94% (FY2023) — eksplicitno objavljeno.
- Ko su kupci: retaileri, brendovi/dobavljači, distributeri, prehrambeni lanci, logistički provajderi.
- Kako se naplaćuje: subscription/recurring model, visok procenat ponavljajućeg prihoda.
- Koncentracija: najveći kupac <1% ukupnog prihoda — eksplicitno objavljeno, nema materijalne koncentracije.

## 2. Moat — dve rečenice (obavezna kapija)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/SPSC.json`:

```
SCORECARD — SPS Commerce, Inc. (SPSC) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 17.1%, WACC 7.1%, spread 10.0% - PROŠAO
G2 ND/EBITDA≤2.0x i pokrivenost≥4x: -0.86x, 1183.0x - PROŠAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 1.73 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 6/6, Palo 0

K1 ROIC: medijana 17.1%, trend PADA (21.5%→17.1%→18.7%→11.2%→10.8%) - standardni ROIC
  ISPOD docs/05 softverskog praga (25%+), i OPADA usled goodwill rasta (Carbon6 akvizicija
  2025). ROIC ex-goodwill (rucno): 58.6%→31.0%→49.2%→32.1%→31.8%, medijana ~32%, ALI
  VOLATILAN - manje stabilan trend od ROP-a. Investirani kapital je 109% prihoda -
  NIJE K1-ALT kapitalno-lak slucaj uprkos SaaS modelu.
K2 Marže: bruto 65.8%→69.2%, operativna 14.3%-15.8% (stabilna), neto 11.6%-12.4% (stabilna).
K3 Zaduženost: BEZ finansijskog duga svih 5 godina (potvrdjeno na bilansu, nema dug linije).
K4 FCF: pozitivan 5/5, FCF konverzija prosek 1.73 (jako), OCF/NI prosek 2.06.
  SBC/prihod 7.1% (FY2025) - PREKO 5% praga, materijalna dilucija.
K5 Valuacija: P/E 33.74. PEG_trailing 1.74, PEG_forward 2.76 (konsenzus rast 12.2%,
  nizi od trailing 19.4% - ocekivano usporavanje). FCF yield na EV 5.1% (nakon SBC 3.3%).
```

**Kapije:** prošlo 6/6 | palo 0 | nepoznato 0
**Override:** Nije formalno potreban (sve kapije prolaze), ali standardni ROIC medijana (17.1%) ne dostiže docs/05 softverski prag (25%+) i OPADA — vredna napomena za §6 čak i bez formalnog pada kapije.

## 4. Poređenje sa konkurencijom

| Metrika | SPSC | MANH (interni projekat-komparator) | Medijana grane |
|---|---|---|---|
| ROIC standardni (5g med.) | 17.1% | N/P (kapitalno-lak, K1-ALT) | N/A |
| Operativna marža | 15.7% (FY2025) | znatno viša (MANH je asset-light, N/P uporediv direktno) | N/A |
| SBC/Prihod | 7.1% (FY2025) | N/A — treba proveriti tačan broj iz MANH.json | N/A |
| Neto dug/EBITDA | -0.86x (neto gotovina) | neto gotovina (slično) | N/A |
| P/E | 33.74 | N/A | N/A |
| PEG (trailing) | 1.74 | N/A | N/A |
| FCF yield na EV | 5.1% | N/A | N/A |

*Napomena: SPSC nema imenovane konkurente u sopstvenom 10-K (samo generičke kategorije — cloud-service provideri, on-premise softver, managed service provideri; Microsoft/NetSuite/Oracle/SAP/Sage su imenovani kao KANAL/RESELLER PARTNERI, ne konkurenti). Nije pronađen pravi javno-kotiran "pure-play" B2B EDI mrežni konkurent za direktno poređenje — MANH (Manhattan Associates, već u portfoliju, supply chain softver) korišćen je kao interni referentni okvir za sličan poslovni prostor, ali MANH je K1-ALT kapitalno-lak slučaj (ROIC N/P), pa direktno numeričko poređenje ROIC-a nije smisleno — poređenje ostaje kvalitativno (oba su supply-chain-adjacent enterprise softver sa visokim switching costs).*

**Ako marža pada — pada li svima u grani ili samo njoj?** SPSC operativna marža je STABILNA (14-16% raspon), ne pada — nema signala pogoršanja specifičnog za kompaniju niti šireg makro pritiska vidljivog u ovim podacima.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 1.74 | prošli EPS rast (19.4% CAGR) se nastavlja |
| PEG_forward | 2.76 | konsenzus analitičara (12.2% EPS rast) je tačan |
| FCF yield na EV | 5.1% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 3.3% | dilucija je realan trošak (SBC/prihod 7.1% — materijalno) |

**Razlika između PEG_trailing i PEG_forward:** Umerena — 1.74 vs 2.76. Konsenzus (12.2%) je niži od trailing (19.4%), implicira očekivano usporavanje rasta nakon "100 uzastopnih kvartala rasta prihoda" faze. FCF yield nakon SBC (3.3%) je značajno niži od pre-SBC (5.1%) — SBC dilucija ovde nije zanemarljiva i treba je uzeti ozbiljno u obzir pri proceni prave vrednosti za akcionara.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 8. Odluka

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2023-2025 income statement | SEC EDGAR 10-K FY2025, CIK 0001092699 | accession 0001092699-26-000012, R5.htm | pristupljeno 2026-09-09/10, licno verifikovano |
| FY2021-2022 podaci | SEC EDGAR 10-K FY2021/2022 | accession 0001564590-22-005952, 0001092699-23-000006 | pristupljeno 2026-09-09 |
| Cena zatvaranja SPSC | IBKR (TradingView chart, NASDAQ) | screenshot, 04.09.2026 zaključna sveća | 2026-09-10 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-10 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-09 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-10 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA | https://finviz.com/quote.ashx?t=SPSC | pristupljeno 2026-09-10 |
