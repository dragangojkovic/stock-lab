# Analiza: Progress Software Corporation (PRGS)

**Datum:** 2026-08-16 | **Analitičar:** Dragan | **Cena na dan analize:** 43,73 USD (zaključna cena 2026-08-14, IBKR)
**U krugu kompetencije:** DA — enterprise softver, .NET/Microsoft ekosistem. Telerik/Kendo UI
je direktno u Draganovom krugu kompetencije kao .NET developer.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Progress Software je **serijski akvizitor** niche enterprise softverskih proizvoda —
kupuje etablirane softverske firme/proizvode i integriše ih u portfolio, umesto da
gradi organski.

**Proizvodni portfolio (FY2025, izvor: 10-K Item 1):** Progress OpenEdge (app-dev
platforma/baza), Sitefinity (CMS), Developer Tools — **Telerik/Kendo UI** (.NET i JS
UI komponente, direktno u Draganovom krugu kompetencije), Chef (DevOps automatizacija),
MOVEit (managed file transfer), MarkLogic + Semaphore (data/semantic AI platforma),
Kemp LoadMaster + Flowmon + WhatsUp Gold (mreža/monitoring), **ShareFile** (dokument
kolaboracija, akvizicija okt. 2024).

**Akvizicije FY2021–2025 (relevantno za K1/K3):**

| Akvizicija | Datum | Cena | Finansiranje |
|---|---|---|---|
| Kemp Technologies + Flowmon | 01.11.2021 | ~$258M | gotovina |
| MarkLogic + Smartlogic | 07.02.2023 | $355M | gotovina, goodwill $161,8M |
| ShareFile (od Cloud Software Group) | 31.10.2024 | $875M | $730M povučeno sa $900M revolvera + gotovina, goodwill $459,5M |
| Nuclia | jun 2025 | mala (kontingentna naknada $1,08M) | — |

**Koncentracija proizvoda — rizik eksplicitno naveden u 10-K (Item 1A):** OpenEdge +
ShareFile zajedno čine **"nešto više od polovine" ukupnog prihoda FY2025** — visoka
zavisnost od dva proizvoda unutar diversifikovanog portfolija od ~8 proizvodnih linija.

**Koncentracija kupaca — potvrđena nulta**, direktan citat: *"No single customer or
partner has accounted for more than 10% of our total revenue in any of our last
three fiscal years."*

**Geografija (FY2025):** ~36% prihoda van Severne Amerike, EMEA sam čini 29%
ukupnog prihoda.

**Konkurencija — NIJE imenovana u 10-K.** Za razliku od MANH/OTIS/CPRT (koji
eksplicitno navode konkurente), PRGS-ov 10-K opisuje konkurenciju samo generički
("kompanije sa uskim ili širokim softverskim rešenjima, proprietary vs. open-source").
Nijedan konkurent nije naveden imenom ni po proizvodnoj liniji — **N/A, ograničenje
izvora**, ne propust istraživanja.

**R&D intenzitet:** Product development trošak FY2025 = 19,7% prihoda (FY2024: 19,4%,
FY2023: 19,1%) — stabilno visok, tipično za softversku firmu.

**Segment:** Jedan operativni i izveštajni segment (potvrđeno, Segments note).

*Izvor: Form 10-K FY2025 (godina završena 30.11.2025), podnet SEC-u 20.01.2026,
CIK 0000876167, accession 0000876167-26-000008, Item 1, Item 1A.*

---

## 2. Moat — dve rečenice (obavezna kapija)

*(popunjava Dragan)*

- Kategorija: *(popuni)*
- **Šta bi ubilo ovaj moat u 5 godina:** *(popuni)*
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** *(popuni)*

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/PRGS.json` (kompletan fajl:
`analize/PRGS-scorecard.md`):

```
SCORECARD — Progress Software Corporation (PRGS)
Sektor: Softver / Enterprise (serijski akvizitor) | Valuta: USD (hiljade) | Podaci: 5 god.

HARD KAPIJE
G1 (ROIC ≥12% i spread ≥3pp nad WACC):        PAO — medijana 9,2% (ispod praga), WACC 6,6%, spread 2,6pp
G2 (Neto dug/EBITDA ≤2.0x softver, pokriv. kamata ≥4x): PAO — ND/EBITDA 4,28x, kamate 2,2x
G3 (FCF pozitivan ≥4/5 god.):                  PROŠAO — 5/5
G4 (FCF konverzija 5g prosek ≥0.7):            PROŠAO — 2,54 (veštački visoko, vidi §5)
G5 (Moat u 2 rečenice):                        PROŠAO (formalno, čeka Draganovu formulaciju — vidi §2)
G6 (Nije u isključenom sektoru):                PROŠAO

Prošlo: 4/6 | Palo: 2 — PRVI SLUČAJ U OVOM PROJEKTU GDE HARD KAPIJE STVARNO PADAJU

K2 (marže): Bruto 80,8% | Operativna 15,7% (OPADA, 21,9%→15,7% kroz 5g) | Neto 7,5% (OPADA)
K3 (zaduženost): ND/EBITDA 4,28x | pokrivenost kamata 2,2x | test produktivnosti duga: NIJE BIO PRODUKTIVAN
  (dug CAGR 25,7% >> EBIT/FCF CAGR 7,2%)
K4 (FCF): FCF konverzija prosek 2,54 (INFLIRANO amortizacijom akvizicija, vidi §5) | SBC/prihod 6,6% ⚠
K5 (valuacija @ 43,73): P/E 26,34 | PEG_trailing -18,14 (BESMISLEN, EPS CAGR negativan) | FCF yield na EV 7,1%
```

**Kapije:** prošlo 4/6 | **palo 2** (G1, G2) — po pravilu CLAUDE.md §3, **akcija ispada
iz razmatranja osim ako se napiše eksplicitno obrazloženje override-a.**
**Override (ako je kapija pala):** *(popunjava Dragan, ako se odluči za override)*

---

## 4. Poređenje sa konkurencijom

**Napomena o uzorku:** PRGS-ov 10-K ne imenuje konkurente (razlika u odnosu na
MANH/OTIS/CPRT). Za poređenje je korišćen **OpenText Corporation (OTEX)** — najbliži
javni analog istog profila (enterprise softver, serijski akvizitor, značajan dug).
Drugi predloženi kandidati (Perficient, PTC, Jack Henry) su proverени i **odbačeni
kao neuporedivi poslovni model** — Perficient je IT konsalting, PTC nema PRGS-tip
dug-finansiranog roll-up profila, Jack Henry je core banking softver, potpuno
drugačija industrija. **Preskočeno je bolje nego forsirano poređenje** (CLAUDE.md
pravilo 5).

| Metrika | PRGS | OpenText (OTEX) |
|---|---|---|
| Prihod | $977,8M (FY2025, godina do 30.11) | $5.246,4M (FY2026, godina do 30.6) |
| Bruto marža | 80,8% | 73,7% |
| Operativna marža (GAAP) | **15,7%** | **20,6%** |
| Neto marža | 7,5% | 12,3% |
| Neto dug/EBITDA | **4,28x** | **2,85x** |
| FCF konverzija | 2,54 (inflirano, vidi §5) | 1,26 |
| P/E (trailing) | 26,34 (računato, @43,73) | ~11,6x (agregator, orijentaciono) |

*Izvori: OpenText 10-K FY2026 (godina do 30.06.2026), podnet SEC-u 06.08.2026,
CIK 0001002638, accession 0001002638-26-000068, Consolidated Statements of Income/
Balance Sheets/Cash Flows. P/E OTEX iz agregatora (stockanalysis.com), orijentaciono.*

**Ključni nalaz:** Iako je PRGS manji, OpenText (isti tip poslovnog modela — softverski
roll-up sa akvizicionim dugom) posluje sa **nižim leverage-om** (ND/EBITDA 2,85x vs
PRGS-ovih 4,28x) i **boljom operativnom maržom** (20,6% vs 15,7%). Ovo je važno: G2
pad kod PRGS-a **nije nužno karakteristika cele kategorije "softverski roll-up"** —
OpenText dokazuje da je moguće voditi sličan model na umerenijem leverage-u. PRGS-ov
leverage (posebno posle ShareFile akvizicije, ND/EBITDA skočio sa 2,79x na 6,20x pa
4,28x) izgleda kao specifičan izbor menadžmenta (agresivnija akvizicija u odnosu na
veličinu firme), ne nužnost modela.

**FCF konverzija PRGS (2,54) je veštački napumpana**, ne znak superiorne efikasnosti
— vidi §5 objašnjenje.

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **-18,14 — BESMISLEN** (P/E 26,34 / EPS CAGR -1,5%) | ne primenjivo — CLAUDE.md K5 eksplicitno kaže da PEG ne radi za negativnu zaradu/rast |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **7,1%** | ništa — samo tekući cash flow |
| FCF yield nakon SBC | **5,1%** | SBC je materijalan (6,6% prihoda) |

**Zašto je FCF konverzija (2,54) obmanjujuća, ne dobra vest:** Formula FCF/NI je
visoka jer je **NI (neto dobit) veštački nizak** — pojeden kamatama ($70,85M FY2025,
raslo 3,5x od FY2021) i ogromnom amortizacijom stečenih nematerijalnih ulaganja
($151,7M D&A FY2025, skoro 3x veće nego FY2021). FCF sam po sebi je zdrav i raste
(OCF $235M FY2025), ali odnos FCF/NI > 2,5 nije znak "superiorne konverzije zarade u
gotovinu" — to je artefakt niskog imenioca zbog troškova akvizicije, ne signal
kvaliteta. **Ne tumačiti G4 prolaz kao snagu bez ove napomene.**

**ROIC ex-goodwill — obavezna dodatna provera za serijske akvizitore (CLAUDE.md K1
zamka):**

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| ROIC (standardni, iz scorecard-a) | 11,7% | 14,1% | 9,2% | 4,9% | 7,7% |
| Goodwill | 671.152 | 671.037 | 832.101 | 1.292.177 | 1.309.054 |
| **ROIC ex-goodwill (ručni izračun)** | 65,2% | 120,1% | 43,4% | 16,2% | 28,9% |

*Ex-goodwill medijana ≈ 43,4% — dramatično iznad standardne medijane od 9,2%.*

**Šta ovo znači, i zašto se NE koristi kao zamena za standardni ROIC:** Same kupljene
firme/proizvodi su operativno vrlo efikasne (ex-goodwill ROIC je izuzetno visok). Ali
CLAUDE.md je eksplicitan — **"ne koristi samo tu verziju — akvizicije su realno
potrošen kapital akcionara."** Standardni ROIC (9,2% medijana, PADA) tretira novac
plaćen za akvizicije kao stvarno uložen kapital, i to je ispravan konzervativan
pogled: **PRGS je platio mnogo (posebno za ShareFile, $875M) u odnosu na povraćaj koji
ta kupovina generiše na nivou cele kompanije.** Razlika između dve ROIC verzije *jeste*
teza koju treba testirati — da li će integracija ShareFile-a vremenom podići
standardni ROIC bliže ex-goodwill nivou, ili će ostati trajni jaz.

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 16,5% |
| EPS | **-1,5%** |
| FCF po akciji | 7,5% |

Broj akcija je blago opao (CAGR -0,3%) — nije buyback-inflacija. EPS je **negativan**
uprkos zdravom rastu prihoda (16,5%) — teret kamata i amortizacije akvizicija
direktno jede zaradu po akciji. Ovo je treći, različit obrazac od MANH-a (buyback
inflacija) i OTIS-a (buyback + slab realni FCF/akcija rast) — kod PRGS-a je **realan
posao koji raste, ali platio je (kroz dug za akvizicije) previše da bi se taj rast
video na bottom line-u.**

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

**Napomena — dve kapije su pale (G1, G2).** Po CLAUDE.md §3, ovo znači da akcija
**ispada iz razmatranja osim ako se napiše eksplicitno pisano obrazloženje
override-a.** Bez override-a, jedina dosledna odluka je "Odbijeno" ili — ako se
override piše — "Watchlist"/"Ulazi" uz jasno obrazloženje zašto se palе kapije
zanemaruju.

- [ ] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Override obrazloženje (OBAVEZNO ako se ne bira "Odbijeno"):** {…}

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
| PRGS FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R9.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/876167/000087616726000008/ | podnet 20.01.2026 |
| PRGS FY2021-FY2022 finansijski podaci | 10-K filings + XBRL companyfacts API, krizno provereno preko dva nezavisna research agenta | sec.gov/Archives/edgar/data/876167/ | 2022 / 2023 |
| PRGS poslovni opis, proizvodi, koncentracija, geografija | Form 10-K FY2025, Item 1, Item 1A | sec.gov/Archives/edgar/data/876167/000087616726000008/prgs-20251130.htm | podnet 20.01.2026 |
| Akvizicije (Kemp, MarkLogic, ShareFile, Nuclia) | 10-K Business Combinations note (više godina) | isti CIK | razni datumi 2021-2025 |
| PRGS cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-14, close 43.73 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-14, close 150.40 |
| PRGS WACC (6,62%, bottom-up) | rf: treasury.gov; beta: stockanalysis.com (treća strana); cost of debt: implicitna stopa iz 10-K | treasury.gov, stockanalysis.com/stocks/prgs/statistics | 14-16.08.2026 |
| OpenText (OTEX) FY2026 finansijski podaci | 10-K FY2026 (godina do 30.06.2026), Consolidated Statements | sec.gov/Archives/edgar/data/1002638/000100263826000068/otex-20260630.htm | podnet 06.08.2026 |
