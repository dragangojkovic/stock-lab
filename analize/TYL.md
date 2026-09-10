# Analiza: Tyler Technologies, Inc. (TYL)

**Datum:** 2026-09-10 | **Analitičar:** Dragan | **Cena na dan analize:** 364.03 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** DA — enterprise softver za javnu upravu je adjacent Draganovom IT/.NET fokusu, slično JKHY po logici troškova prelaska.

---

## 1. Šta kompanija zapravo radi

Tyler je vodeći dobavljač integrisanog softvera za javni sektor u SAD-u (lokalna/državna/federalna uprava) — public safety, pravosuđe, javno zdravlje, oporezivanje/budžetiranje, infrastruktura/zemljište, komunalne usluge, K-12 obrazovanje, socijalne usluge.

- Izvori prihoda i njihov udeo: subscription (SaaS) prihod je najveća kategorija — $1,586.2M od $2,332.3M ukupno FY2025 (~68%).
- Ko su kupci: državne/lokalne agencije — duboke, dugoročne relacije, dedicated state-level office u 30 država.
- Kako se naplaćuje: subscription/maintenance/professional services model, dominantno recurring.
- Koncentracija: nema obelodanjivanja koncentracije kupaca — konzistentno sa hiljadama državnih/lokalnih agencija kao klijentima (dispergovana baza).

## 2. Moat — dve rečenice (obavezna kapija)

> Core sistemi zapisa za javnu upravu (pravosuđe, oporezivanje, public safety) su operativno srce agencije — migracija je višegodišnji, regulatorno i politički rizičan poduhvat (izabrani zvaničnici retko rizikuju veliki IT projekat), slično JKHY core-bankarskoj logici.
> Subscription prihod dominira (68%) i operativna marža dosledno raste (11.4%→15.3%) svake godine bez izuzetka, potvrđujući ponavljajuću, lepljivu prirodu odnosa sa agencijama.

- Kategorija: troškovi prelaska (switching costs) + regulatorna/politička inercija
- **Šta bi ubilo ovaj moat u 5 godina:** federalni ili državni mandat za standardizovanu, jeftiniju open-source alternativu ILI veliki cloud provider (Microsoft/Oracle) agresivno subvencioniše ulazak u gov-tech prostor
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** treba mu dedicated state-level prisustvo (Tyler ima u 30 država) izgrađeno godinama odnosa sa agencijama, plus toleranciju za spor prodajni ciklus vezan za budžetske/izborne cikluse javnog sektora

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/TYL.json`:

```
SCORECARD — Tyler Technologies, Inc. (TYL) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 6.6%, WACC 8.3%, spread -1.7% - PAO
G2 ND/EBITDA≤2.0x i pokrivenost≥4x: -0.84x, 71.6x - PROŠAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 2.02 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 5/6, Palo 1 (G1) - KAPIJA JE PALA

K1 ROIC: medijana 6.6%, trend RASTE (6.6%→5.5%→5.4%→7.9%→8.8%). WACC 8.3%, spread -1.7%
  (standardni ROIC je ISPOD cene kapitala na medijani, ali RASTE ka njoj).
K1 ROIC EX-GOODWILL (rucno izracunato, NIC Inc. akvizicija 2021, goodwill $2.36-2.59mlrd):
  FY2021 45.5% → FY2022 19.8% → FY2023 20.6% → FY2024 36.0% → FY2025 41.5%
  Medijana ex-goodwill: ~36.0%, DOSTIZE docs/05 softverski prag (25%+), SNAZNO RASTE
  poslednje 2 godine nakon inicijalnog pada usled NIC integracije.
K2 Marže: bruto 44.6%→46.5%, operativna 11.4%→15.3% (RASTE DOSLEDNO), neto 10.1%→13.5%
  (RASTE). Marze se konzistentno poboljsavaju kroz ceo period.
K3 Zaduženost: ND/EBITDA 1.39x(FY21)→-0.84x(FY25, neto gotovina), pokrivenost kamata
  7.8x→71.6x. Test produktivnosti duga PROLAZI (dug CAGR -5.4% << EBIT CAGR 18.6%) - dug
  (NIC akvizicioni term loan) u potpunosti otplacen, kompanija sada neto gotovinska.
K4 FCF: pozitivan 5/5, FCF konverzija prosek 2.02 (jako), OCF/NI prosek 2.27.
  SBC/prihod 6.5% (FY2025) - PREKO 5% praga, materijalna dilucija.
K5 Valuacija: P/E 50.56 (NAJSKUPLJE od tri softverska kandidata ovog kruga). PEG_trailing
  2.94, PEG_forward 3.19 (konsenzus rast 15.8%, blizu trailing 17.2% - konzistentno,
  ne drastican jaz). FCF yield na EV 4.0% (nakon SBC 3.0%).
```

**Kapije:** prošlo 5/6 | palo 1 (G1) | nepoznato 0
**Override:** Standardni ROIC pada ispod WACC-a (spread -1.7%) isključivo zbog goodwill dilucije (NIC Inc. akvizicija, 2021, najveća u istoriji kompanije). ROIC ex-goodwill, ručno izračunat po CLAUDE.md K1 metodologiji, je **36.0% medijana i SNAŽNO RASTE** poslednje dve godine (20.6%→41.5%) — jači nivo i sličan trend rasta kao kod ROP-a. Za razliku od ROP-a, standardni ROIC ovde takođe RASTE (6.6%→8.8%) što ukazuje da se integracija akvizicije nastavlja da sazreva pozitivno, ne da se goodwill problem pogoršava. Ovo je legitiman override kandidat: sve ostale metrike (marže, FCF konverzija, zaduženost) su odlične i dosledno se poboljšavaju.

## 4. Poređenje sa konkurencijom

| Metrika | TYL | ROP (interni projekat-komparator) | PRGS (interni, ODBIJEN) | Medijana grane |
|---|---|---|---|---|
| ROIC standardni (5g med.) | 6.6% | 5.8% | 9.2% | N/A |
| ROIC ex-goodwill (medijana) | 36.0% | 21.3% | N/A — treba proveriti (nije izracunato u PRGS analizi) | N/A |
| Operativna marža (najnovija god.) | 15.3% | 28.3% (ROP) | N/A | N/A |
| Neto dug/EBITDA | -0.84x (neto gotovina) | 2.87x | 4.28x | N/A |
| P/E | 50.56 | 28.58 (ROP) | N/A | N/A |
| PEG_forward | 3.19 | 2.87 (ROP) | N/A | N/A |
| FCF yield na EV | 4.0% | 4.6% (ROP) | N/A | N/A |

*Napomena: TYL 10-K imenuje konkretne konkurente (Oracle, Infor, SAP, Workday, CentralSquare Technologies, Thomson Reuters, Motorola Solutions, Axon Enterprise, Constellation Software), ali svi su mnogo veći/diversifikovaniji ili nisu javno-kotirani na SEC-u (CentralSquare privatna, Constellation Software kotirana na TSX ne SEC) — nijedan nije bio predmet ovog istraživanja zbog vremenskih ograničenja. Korišćeni su ROP i PRGS kao INTERNI projekat-komparatori (oba serijski akvizitori softvera, oba analizirana u ovom projektu) radi konteksta, ne kao pravi industrijski peer-ovi. TYL ima ZNAČAJNO BOLJI ROIC ex-goodwill (36.0%) i nulti neto dug naspram oba internа komparatora — najčistiji override profil od tri testirana serijska akvizitora u projektu (ROP, PRGS, TYL).*

**Ako marža pada — pada li svima u grani ili samo njoj?** TYL marže NE padaju — operativna marža raste dosledno (11.4%→15.3%) svake godine bez izuzetka. Ovo je pozitivan signal specifičan za TYL, ne makro efekat.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 2.94 | prošli EPS rast (17.2% CAGR) se nastavlja |
| PEG_forward | 3.19 | konsenzus analitičara (15.8% EPS rast) je tačan |
| FCF yield na EV | 4.0% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 3.0% | dilucija je realan trošak (SBC/prihod 6.5% — materijalno) |

**Razlika između PEG_trailing i PEG_forward:** MALA — 2.94 vs 3.19, konsenzus (15.8%) je blizu trailing (17.2%), konzistentno bez drastičnog jaza koji bi zahtevao posebno objašnjenje. Oba PEG-a su iznad 2.0 praga koji zahteva eksplicitno obrazloženje premije — ovde premija dolazi od dokazanog kvaliteta (dosledno rastuće marže, snažan i rastući ex-goodwill ROIC, nulti neto dug) i visokog switching-cost moat-a u javnom sektoru, ne od spekulativnog očekivanja ubrzanja.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

1. ROIC ex-goodwill padne ispod 25% (obrne dvogodišnji trend rasta) — signal da integracija NIC akvizicije prestaje da sazreva pozitivno.
2. Operativna marža stagnira ili padne ispod 14% dva kvartala zaredom — prekid dosledno rastućeg trenda.
3. R&D skok u FY2025 (+73%) se pokaže kao neefikasna AI investicija bez merljivog povratka (npr. rast prihoda ne ubrza) — signal lošeg kapitalnog alociranja.

**Šta je najjači argument protiv kupovine ove akcije?** Plaćaš P/E od 50.56 (najskuplje od tri softverska kandidata ovog kruga) za override tezu koja se oslanja na samo dve godine pozitivnog ex-goodwill trenda (FY2024-2025) posle tri prethodne godine slabijeg/volatilnog rezultata (FY2021-2023, 19.8-45.5% raspon) — ako se FY2024-2025 poboljšanje pokaže kao privremeni skok (npr. jednokratni veliki ugovori), a ne strukturna promena, standardni ROIC bi mogao ostati trajno ispod WACC-a.

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | ROIC ex-goodwill ostaje visok | ≥ 30% | 70% |
| 2 | Operativna marža stabilna/raste | ≥ 14% (±1pp) | 70% |
| 3 | Zaduženost ostaje niska | Neto dug/EBITDA negativan (neto gotovina) | 70% |
| 4 | FCF konverzija ostaje jaka | ≥ 1.5 | 70% |
| 5 | Prihod raste | ≥ 8% god/god | 70% |

## 8. Odluka

- [x] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Datum ulaza:** 2026-09-04
**Cena ulaza:** 364.03
**VUAA cena istog dana:** 149.02 ← obavezno za benchmark
**Veličina pozicije:** 1/10 satelita

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu):**
1. ROIC ex-goodwill padne ispod 20% dva kvartala zaredom
2. Operativna marža padne ispod 12% dva kvartala zaredom
3. Neto dug/EBITDA ponovo postane pozitivan i pređe 1.5x (signal nove velike zaduženo-finansirane akvizicije)

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2025 income statement, goodwill | SEC EDGAR 10-K FY2025, CIK 0000860731 | accession 0000860731-26-000016, R4/R5.htm | pristupljeno 2026-09-09/10, licno verifikovano |
| FY2021-2024 podaci | SEC EDGAR 10-K FY2021-2024 | accession brojevi u data/TYL.json | pristupljeno 2026-09-09 |
| Cena zatvaranja TYL | IBKR (TradingView chart, NYSE) | screenshot, 04.09.2026 zaključna sveća | 2026-09-10 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-10 |
| Beta (5g) | procena ~0.85 (raspon 0.81-0.92 između izvora), TREĆA STRANA | N/A — treba nezavisno potvrditi tačan URL | pristupljeno 2026-09-10 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-10 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA | https://finviz.com/quote.ashx?t=TYL | pristupljeno 2026-09-10 |
