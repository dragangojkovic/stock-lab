# Analiza: AMETEK, Inc. (AME)

**Datum:** 2026-09-02 | **Analitičar:** Dragan | **Cena na dan analize:** 231,32 USD (zaključna cena 2026-09-01, IBKR)
**U krugu kompetencije:** NE — diversifikovani industrijski instrumenti/
elektromehanika nisu u Draganovom IT/.NET fokusu.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

AMETEK je diversifikovan industrijski konglomerat kroz **dva segmenta**:
- **Electronic Instruments Group (EIG)** — ~66-70% prihoda, instrumenti za
  process/power/industrial/aerospace tržišta. Marža stabilnija (25,5-30,7%
  kroz 5 godina).
- **Electromechanical Group (EMG)** — precizna motion control rešenja,
  medicinske komponente/uređaji, thermal management, specialty metals.
  Marža fluktuira više (20,0-26,2%) — MD&A eksplicitno navodi da su Paragon
  Medical (integracija 2023-2024) i FARO (integracija 2025) troškovi
  pritiskali EMG maržu u godini integracije.

**Konkurencija:** AMETEK **ne imenuje konkretne konkurente** u Item 1 —
diversifikovan konglomerat sa desetinama niša, generički opis konkurencije po
tržišnom segmentu. K2 poređenje bi zahtevalo konkurente po segmentu/niši
(npr. proces instrumenti vs Emerson/Honeywell, motion control vs Regal
Rexnord), ne na nivou cele kompanije.

**KLJUČNI NALAZ — AMETEK je serijski akvizitor, tačan test slučaj `docs/05`
kandidatske liste za K1 goodwill zamku.** Kompanija navodi doslovno u 10-K:
*"Since the beginning of 2021 through December 31, 2025, AMETEK has completed
15 acquisitions with annualized sales totaling approximately $1.8 billion."*
Goodwill je porastao **37% kumulativno** ($5,24 mlrd → $7,17 mlrd,
FY2021-2025).

**Istorija akvizicija (5 godina, 15 ukupno):**
| Godina | Broj akvizicija | Cash potrošen | Najveća |
|---|---|---|---|
| 2021 | 6 | $1.959,2M | Alphasense, Abaco Systems, NSI-MI |
| 2022 | 2 | $429,7M | Navitar, RTDS |
| 2023 | 4 | $2.237,9M | **Paragon Medical ($1.892,2M)** — najveća u istoriji AMETEK-a |
| 2024 | 1 | $117,5M | Virtek Vision |
| 2025 | 2 | $933,2M | FARO Technologies ($829,1M) — jedina javna kompanija u periodu |

**Dividende/buyback:** AMETEK plaća i dividende i radi buyback, ali buyback
je veoma varijabilan — prioritet ide ka akvizicijama u godinama velikih
deal-ova (npr. 2023: $2,238 mlrd na akvizicije, samo $7,8M buyback).

*Izvor: Form 10-K FY2025, CIK 0001037868, accession 0001037868-26-000016,
Item 1, Napomena 6 (Acquisitions).*

---

## 2. Moat — dve rečenice (obavezna kapija)

*(popunjava Dragan)*

- Kategorija: *(popuni)*
- **Šta bi ubilo ovaj moat u 5 godina:** *(popuni)*
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** *(popuni)*

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/AME.json` (kompletan fajl:
`analize/AME-scorecard.md`):

```
SCORECARD — AMETEK, Inc. (AME)
Sektor: Industrija - diversifikovani instrumenti/elektromehanika

G1 (ROIC ≥15% industrija po docs/05, spread ≥3pp nad WACC): PADA PO SEKTORSKOM PRAGU
    — medijana 12,6% je ISPOD 15% praga (iako PROLAZI opšti 12% minimum sa
    spreadom 3,6pp nad WACC-om 9,0%)
G2 (Neto dug/EBITDA ≤2.5x, pokriv. kamata ≥4x): PROŠAO — 0,78x / 23,5x
G3 (FCF pozitivan ≥4/5 god.): PROŠAO — 5/5
G4 (FCF konverzija ≥0.7): PROŠAO — 1,10
G5 (Moat u 2 rečenice): čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru): PROŠAO

Prošlo: 5/6 (po sektorskom pragu) | Formalno (opšti prag): 6/6
```

**Ovo je granični metodološki slučaj — treba jasno razlikovati dva čitanja:**
1. **Sirovi scorecard (opšti 12% prag):** G1 PROLAZI (12,6% medijana, spread
   3,6pp — tačno iznad 3pp minimuma).
2. **Sektorski prag iz `docs/05` (15%+ za industriju):** G1 **PADA** —
   medijana je ispod praga.

**Uzrok — potvrđena K1 "serijski akvizitori" zamka.** Ručno izračunat **ROIC
ex-goodwill** (investirani kapital minus goodwill):
- FY2021: NOPAT $1.060M / (invest. kapital $9.069M − goodwill $5.239M =
  $3.831M) = **27,7%**
- FY2025: NOPAT $1.572M / (invest. kapital $12.454M − goodwill $7.171M =
  $5.283M) = **29,8%**

**Ex-goodwill ROIC je konzistentno 28-30% kroz ceo period — daleko iznad
sektorskog praga.** Ovo potvrđuje CLAUDE.md K1 upozorenje doslovno: standardni
ROIC (12,6%) je **razblažen goodwill-om** iz 15 akvizicija ($5,68 mlrd
ukupno potrošeno na akvizicije 2021-2025), ne odražava slabost osnovnog
poslovanja. **Ali CLAUDE.md je isto tako eksplicitan: "ne koristi samo
ex-goodwill verziju — akvizicije su realno potrošen kapital akcionara."**
Akcionari su realno platili $5,68 mlrd za taj rast — pitanje za Draganovu
moat/odluku sekciju je da li je taj kapital bio dobro potrošen (M&A
disciplina) ili je to prosto "kupljeni rast" po ceni koja razvodnjava
povrat na kapital.

---

## 4. Poređenje sa konkurencijom

**NIJE SPROVEDENO u ovoj analizi.** AMETEK nema jasan peer set na nivou cele
kompanije (diversifikovan portfolio niša) — poređenje bi zahtevalo
segment-po-segment analizu (npr. Emerson/Honeywell za proces instrumente,
Regal Rexnord za motion control), što je van obima ovog prolaza. **Otvoreno
pitanje — K2 poređenje sa 3-5 konkurenata (CLAUDE.md obavezno pravilo) nije
zadovoljeno u ovoj verziji analize.**

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **3,35** (P/E 36,14 / EPS CAGR 10,8%) — iznad praga 2,0 | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **3,0%** (nakon SBC: 2,9%) | ništa — samo tekući cash flow |
| FCF marža | 22,6% | — |

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 7,5% |
| EPS | 10,8% |
| FCF po akciji | 12,5% |

**Zdrav obrazac.** FCF po akciji raste brže (12,5%) i od EPS-a (10,8%) i od
prihoda (7,5%) — broj akcija je praktično stabilan (CAGR -0,2%), pa rast EPS-a
iznad prihoda dolazi od operativne poluge/akvizicija koje dodaju zaradu, ne
od finansijskog inženjeringa. **Napomena:** deo prihodnog rasta (7,5% CAGR)
je neorganski (dolazi iz 15 akvizicija) — organski rast bi bio niži, ali
10-K ne daje jasnu dekompoziciju organski vs. akvizicijom-vođen rast za ceo
period u delu koji sam pregledao.

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. *(popuni)*
2. *(popuni)*
3. *(popuni)*

**Šta je najjači argument protiv kupovine ove akcije?** *(popuni)*

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | | | 50/70/90% |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## 8. Odluka (popunjava Dragan)

- [ ] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Datum ulaza:** {datum unosa, NE retroaktivan}
**Cena ulaza:** {cena zatvaranja tog dana}
**VUAA cena istog dana:** {…} ← obavezno za benchmark
**Veličina pozicije:** {1/N satelita}

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu):**
1. {…}
2. {…}
3. {…}

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| AME FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R6/R8/R10.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/1037868/000103786826000016/ | podnet 17.02.2026 |
| AME FY2021-FY2022 finansijski podaci | XBRL companyfacts, unakrsno provereno protiv originalnih 10-K | data.sec.gov/api/xbrl/companyfacts/CIK0001037868.json | pristupljeno 02.09.2026 |
| AME poslovni opis, segmenti, akvizicije | Form 10-K FY2025, Item 1, Napomena 6 | sec.gov/Archives/edgar/data/1037868/000103786826000016/ | podnet 17.02.2026 |
| AME cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-09-01, close 231.32 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-09-01, close 147.92 |
| AME WACC (9,03%, bottom-up) | rf: treasury.gov (4,79%, 10Y UST, 01.09.2026); beta: stockanalysis.com (1,00, treća strana) | treasury.gov, stockanalysis.com/stocks/ame/statistics | 01-02.09.2026 |
