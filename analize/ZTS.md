# Analiza: Zoetis Inc. (ZTS)

**Datum:** 2026-09-04 | **Analitičar:** Dragan | **Cena na dan analize:** 76.29 (IBKR zaključna, 03.09.2026)
**U krugu kompetencije:** NE — veterinarska farmacija nije u Draganovom IT/.NET fokusu.

> Pravilo: nijedno polje ne ostaje prazno. Ako podatak nije dostupan, upiši
> `N/A — treba proveriti` i navedi šta konkretno treba naći. Prazno polje = nepotpuna
> analiza, a nepotpuna analiza ne ide u portfolio.

---

## 1. Šta kompanija zapravo radi

Zoetis je najveća svetska kompanija posvećena isključivo animalnom zdravlju — razvija, proizvodi i prodaje lekove, vakcine i dijagnostiku za kućne ljubimce (companion animal) i stoku (livestock). Portfolio pokriva parasiticide (npr. Simparica/Simparica Trio), vakcine, dermatologiju (Apoquel, Cytopoint), anti-infektive i lekove za bol/sedaciju — preko 300 proizvodnih linija.

- Izvori prihoda i njihov udeo: Companion animal ~70% prihoda (FY2025), livestock ostatak; geografski US 54%, International 45%, ostalo (contract manufacturing + human health) ~1%.
- Ko su kupci: veterinari, veterinarske klinike/bolnice i distributeri koji dalje snabdevaju klinike; krajnji potrošač je vlasnik životinje, ali kupovinu odlučuje veterinar.
- Kako se naplaćuje: prodaja proizvoda (jednokratna po transakciji, ali visoko ponavljajuća zbog hroničnih terapija — npr. Apoquel se uzima kontinuirano).
- Koncentracija: najveći kupac (jedan američki veterinarski distributer) = ~16% ukupnog prihoda FY2025. Franšizna koncentracija: Simparica/Simparica Trio ~12% prihoda (FY2022 podatak — N/A za tačan noviji %, treba proveriti u FY2025 10-K segmentnom raščlanjenju).

## 2. Moat — dve rečenice (obavezna kapija)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/ZTS.json`:

```
SCORECARD — Zoetis Inc. (ZTS)
Sektor: Zdravstvo - animalno zdravstvo (farmaceutici/vakcine) | Valuta: USD (miliони) | Podaci: 5 god. | Generisano: 2026-09-04

HARD KAPIJE

| # | Kapija | Vrednost | Ishod |
|---|---|---|---|
| G1 | ROIC ≥ 12% (5g medijana) i spread nad WACC ≥ 3pp | medijana 28.0%, WACC 6.8%, spread 21.2% | PROŠAO |
| G2 | Neto dug/EBITDA ≤ 2.5x i pokrivenost kamata ≥ 4x | ND/EBITDA 1.67x, kamate 16.0x | PROŠAO |
| G3 | FCF pozitivan u ≥ 4 od 5 godina | 5 od 5 poznatih | PROŠAO |
| G4 | FCF konverzija (FCF/NI, 5g prosek) ≥ 0.7 | 0.79 | PROŠAO |
| G5 | Moat artikulisan u 2 rečenice | DA | PROŠAO |
| G6 | Nije u isključenom sektoru | u redu | PROŠAO |

Prošlo: 6 | Palo: 0 | Nepoznato: 0 | Nije primenljivo: 0

K1 — ROIC: medijana (5g) 28.0%, trend stabilan (29.5%→26.6%→25.2%→28.4%→28.0%). WACC 6.8%, spread 21.2%.
K2 — Marže: bruto 70.4%→71.8%, operativna 35.5%→37.5% (stabilan/blago rastući), neto 26.2%→28.2%.
K3 — Zaduženost: Neto dug/EBITDA 0.97x→1.67x (RASTUĆI), pokrivenost kamata 12.3x→16.0x, D/E 1.45→2.71.
  Test produktivnosti duga: dug CAGR 8.2% vs EBIT CAGR 6.5% vs FCF CAGR 7.1% → dug NIJE bio produktivan.
K4 — FCF: pozitivan svih 5 god, FCF konverzija prosek 0.79, OCF/NI prosek 1.05. SBC/prihod 0.9% (nisko).
  Potraživanja CAGR 8.8% i zalihe CAGR 6.0% oba RASTU BRŽE od prihoda (5.0%) — blaga crvena zastavica za proveru.
K5 — Valuacija: P/E 12.67 (istorijski anomalno nisko vs 25-35x raspon). PEG_trailing 1.41, PEG_forward 4.18
  (konsenzus rast samo 3.03% — mnogo niži od trailing 9.0%). FCF yield na EV 5.6% (nakon SBC 5.4%).
```

**Kapije:** prošlo 6/6 | palo 0 | nepoznato 0
**Override (ako je kapija pala):** nema — sve kapije prošle formalno čisto.

> Napomena van formalnih kapija: iako G3 (dug) formalno prolazi, **test produktivnosti duga PADA** (dug je rastao brže od EBIT-a/FCF-a poslednjih 5 godina) — ovo je soft signal upozorenja koji zaslužuje pažnju u §6, ne kapija koja obara analizu.

## 4. Poređenje sa konkurencijom

| Metrika | ZTS | IDXX (dijagnostika) | Elanco (ELAN) | Merck Animal Health | Medijana grane |
|---|---|---|---|---|---|
| ROIC (5g med.) | 28.0% | 44.2% | N/A — treba proveriti (EBIT nije XBRL-tag-ovan, treba ručno iz 10-K income statement-a) | N/A — deo MRK, nije izdvojivo iz konsolidovanog bilansa | N/A |
| Bruto marža | 71.8% (FY2025) | N/A — treba proveriti | 54.9% (FY2024) | N/A | N/A |
| Operativna marža | 37.5% (FY2025) | 28.9% (FY2024) | N/A — treba proveriti (EBIT tag nedostaje) | N/A | N/A |
| Neto marža | 28.2% (FY2025) | 22.8% (FY2024) | 7.6% (FY2024, FY2023 bio gubitak -27.9%) | N/A | N/A |
| Neto dug/EBITDA | 1.67x (FY2025) | N/A — treba proveriti | N/A — treba proveriti (EBITDA nedostupna bez EBIT-a) | N/A | N/A |
| FCF konverzija | 0.79 | N/A — treba proveriti | N/A — treba proveriti | N/A | N/A |
| P/E | 12.67 | 42.12 | N/A — treba proveriti | N/A | N/A |
| PEG (trailing) | 1.41 | N/A — treba proveriti | N/A | N/A | N/A |
| FCF yield na EV | 5.6% | 2.3% | N/A — treba proveriti | N/A | N/A |

*Izvor IDXX brojeva: prethodno kompletirana analiza u ovom projektu (`data/watchlist.csv`, IDXX red — sve kapije prošle, kompletna analiza 2026-08-18). Izvor Elanco: SEC EDGAR 10-K FY2024 (accession 0001739104-25-000014) — EBIT nije eksplicitno XBRL-tag-ovan (Elanco ima drugačiju strukturu izveštavanja), pa ROIC/operativna marža/ND-EBITDA ostaju N/A dok se ne izvuku ručno iz izveštaja o prihodima. Boehringer Ingelheim Animal Health je privatna (nemačka GmbH) — nema SEC podatke, N/A trajno.*

**Ako marža pada — pada li svima u grani ili samo njoj?** ZTS marže NE padaju — operativna marža raste (35.5%→37.5% kroz 5 godina) i neto marža raste (26.2%→28.2%). ZTS je jasno profitabilniji od IDXX na operativnom nivou (37.5% vs 28.9%) i od Elanco (koji je tek FY2024 izašao iz gubitka). Ovo je pozitivan signal specifičan za ZTS, ne makro efekat — Elanco-ov slabiji profil verovatno odražava manji obim i veći dug iz spinoff-a od Eli Lilly (2019), ne opšte opadanje sektora.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 1.41 | prošli EPS rast (9.0% CAGR) se nastavlja |
| PEG_forward | 4.18 | konsenzus analitičara (3.03% EPS rast) je tačan |
| FCF yield na EV | 5.6% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 5.4% | dilucija je realan trošak (ovde gotovo nebitna, SBC/prihod svega 0.9%) |

**Razlika između PEG_trailing i PEG_forward:** OGROMNA — 1.41 vs 4.18. Konsenzus analitičara (finviz "EPS next 5Y" = 3.03%) implicira da će rast EPS-a usporiti na TREĆINU istorijskog tempa (9.0% → 3.03%). Ovo NIJE slučaj "tržište očekuje ubrzanje koje treba opravdati" (kao kod VEEV) — ovde je obrnuto: tržište/analitičari očekuju DRASTIČNO USPORAVANJE, i baš to usporeno očekivanje objašnjava zašto je P/E tako nisko (12.67x) uprkos i dalje solidnom ROIC-u i maržama. Nisko P/E ovde nije očigledna prilika — moglo bi biti tačna cena za realno usporen rast. Otvoreno pitanje za §6: da li je 3.03% konsenzus realan (npr. zbog Librela bezbednosnih pitanja i usporavanja US companion animal tržišta pomenutih u industrijskim izveštajima) ili je to artefakt jednog izvora (finviz) koji nisam mogao unakrsno proveriti (Zacks blokiran bot-zaštitom, WSJ nedostupan).

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 8. Odluka

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2023-2025 income statement, balance sheet, cash flow | SEC EDGAR 10-K FY2025, CIK 0001555280 | accession 0001555280-26-000011, R3/R6/R9.htm | pristupljeno 2026-09-03 |
| FY2021-2022 balance sheet/cash flow | SEC EDGAR 10-K FY2022, CIK 0001555280 | accession 0001555280-23-000074 | pristupljeno 2026-09-03 |
| Cena zatvaranja ZTS | IBKR (TradingView chart, SMART routing) | screenshot, 03.09.2026 zaključna sveća | 2026-09-03 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 03.09.2026 zaključna sveća | 2026-09-03 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-03 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 03.09.2026, 4.77% | pristupljeno 2026-09-04 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, nepotvrđeno drugim izvorom (Zacks blokiran, WSJ nedostupan) | https://finviz.com/quote.ashx?t=ZTS | pristupljeno 2026-09-04 |
| IDXX komparativni podaci | Prethodna kompletna analiza u ovom projektu | `data/watchlist.csv` (IDXX red), `analize/IDXX.md` | 2026-08-18 |
| Elanco (ELAN) delimični podaci | SEC EDGAR 10-K FY2024, CIK 0001739104 | accession 0001739104-25-000014 | pristupljeno 2026-09-04 |
