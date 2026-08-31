# Analiza: Fastenal Company (FAST)

**Datum:** 2026-08-31 | **Analitičar:** Dragan | **Cena na dan analize:** 49,78 USD (zaključna cena 2026-08-28, IBKR)
**U krugu kompetencije:** NE — fizička distribucija/logistika spojnog
materijala nije u Draganovom IT/.NET fokusu, iako FASTVend/FMI ima manju
softversku komponentu.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Fastenal je industrijski distributer spojnog materijala (fasteners) i MRO
(maintenance/repair/operations) proizvoda. Poslovni model se oslanja na
**Fastenal Managed Inventory (FMI)** — FASTStock/FASTBin/**FASTVend**
(industrijski vending, ~124.000 uređaja u polju krajem 2025) i **Onsite
lokacije** (sopstveno osoblje fizički kod velikog kupca, integrisano u
njegov workflow), plus integrated supply usluge.

**Obim (kraj 2025):** 1.595 branch lokacija u 25 zemalja, 19 distributivnih
centara (12 SAD, 2 Kanada, 1 Meksiko, 2 Azija, 2 Evropa, ~5,3 miliona kv.
stopa kapaciteta), ~24.489 zaposlenih.

**Konkurencija:** 10-K (Item 1) opisuje konkurenciju generički — "veliki
nacionalni distributeri" i "manji regionalni/lokalni distributeri" — bez
imenovanja tickera. Sekundarno identifikovani direktni konkurenti: **W.W.
Grainger (GWW)**, **MSC Industrial Direct (MSM)**, Applied Industrial
Technologies (AIT).

**Stock split:** Fastenal je 21.5.2025. sproveo **2-za-1 split akcija**.
Istorijski brojevi akcija/EPS u ovoj analizi su onako kako su originalno
prijavljeni u svakoj godini (pre-split FY2021-2024, post-split FY2025) —
CAGR računi na sirovim brojevima su **distorzovani ovim splitom** (vidi §5,
korekcija).

**Dug/kapital:** Fastenal je **pretežno dividend-only** kompanija (redak
slučaj u ovom projektu — većina ostalih pozicija je buyback-only ili oba).
Buyback je oportunistički i mali: $0 (FY2021), ~$237,8M (FY2022), $0
(FY2023-2025). Kompanija je krajem 2024/2025 prešla u **neto gotovinsku
poziciju** (neto dug: $154M→$325M→$39M→**-$56M**→**-$152M** FY2021-2025).
**Nema goodwill liniju na bilansu** — organski rast, K1 "serijski akvizitori"
zamka se ne primenjuje.

*Izvor: Form 10-K FY2025, CIK 0000815556, accession 0000815556-26-000009,
Item 1.*

---

## 2. Moat — dve rečenice (obavezna kapija)

*(popunjava Dragan)*

- Kategorija: *(popuni)*
- **Šta bi ubilo ovaj moat u 5 godina:** *(popuni)*
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** *(popuni)*

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/FAST.json` (kompletan fajl:
`analize/FAST-scorecard.md`):

```
SCORECARD — Fastenal Company (FAST)
Sektor: Industrijska distribucija

G1 (ROIC ≥15% industrijska distribucija, spread ≥3pp nad WACC): PROŠAO
    — medijana 32,4%, WACC 7,9%, spread 24,4pp
G2 (Neto dug/EBITDA ≤2.5x, pokriv. kamata ≥4x): PROŠAO — -0,08x (neto gotovina) / 267,0x
G3 (FCF pozitivan ≥4/5 god.): PROŠAO — 5/5
G4 (FCF konverzija ≥0.7): PROŠAO — 0,82
G5 (Moat u 2 rečenice): čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru): PROŠAO

Prošlo: 6/6 | Palo: 0
```

**Kapije prošle čisto, ROIC (32,4% medijana) čvrsto iznad sektorskog praga od
15%** — najviši spread nad WACC-om (24,4pp) od svih infrastrukturnih/kvalitetnih
pozicija u ovom projektu do sada zbog niskog WACC-a (skoro bez duga).

**Upozorenje na artefakt:** scorecard-ov automatski PEG_trailing (-4,99) i
rast broja akcija (CAGR 18,8%) su **artefakt 2-za-1 splita akcija** — vidi
korekciju u §5.

---

## 4. Poređenje sa konkurencijom

**W.W. Grainger (GWW)** i **MSC Industrial Direct (MSM)** — najbliži direktni
konkurenti u MRO/industrijskoj distribuciji (FY2025 podaci, SEC EDGAR):

| Metrika | Fastenal (FAST) | Grainger (GWW) | MSC Industrial (MSM) |
|---|---|---|---|
| Prihod (FY2025) | $8.201M | $17.942M | $3.770M (FYE avg. 2025) |
| Operativna marža FY2025 | **20,2%** | 13,9% | 8,0% |
| Operativna marža FY2024 | 20,0% | 15,4% | 10,2% |
| Neto marža FY2025 | **15,3%** | 9,5% | 5,3% |
| ROIC FY2025 | 33,2% | 32,9% | 12,5% |
| Neto dug/EBITDA | **-0,08x (neto gotovina)** | 0,69x | 1,09x |
| Pokrivenost kamata | **267,0x** | 30,8x | 12,5x |

**Ključni nalaz — Fastenal ima NAJVIŠE marže od sve tri, uprkos tome što je
manji od Grainger-a po prihodu.** Operativna marža FAST-a (20,2%) je skoro
1,5x veća od Grainger-ove (13,9%) i preko 2,5x veća od MSC-ove (8,0%).
Fastenal-ov ROIC (33,2%) je uporediv sa Grainger-ovim (32,9%) — impresivno za
manju kompaniju — i drastično bolji od MSC-a (12,5%, tek iznad opšteg 12%
praga, ne sektorskog).

**Divergentan trend — CLAUDE.md K2 signal.** I Grainger i MSC su zabeležili
**pad** operativne marže FY2024→FY2025 (GWW: 15,4%→13,9%; MSM: 10,2%→8,0%) —
ovo izgleda kao makro/ciklični pritisak u industrijskoj distribuciji. **Fastenal
je jedini od tri koji je maržu ZADRŽAO STABILNOM** (20,0%→20,2%, blagi rast).
Po CLAUDE.md pravilu ("ako pada svima → makro; ako pada samo njoj →
specifično za kompaniju") — obrnuta varijanta ovog testa je **da FAST
nadmašuje sopstvenu granu baš u periodu kad grana slabi**, što je jak
pozitivan signal specifičan za kompaniju (izvršenje, cenovna moć, ili
gustina distribucije koja amortizuje ciklus), ne samo pasivno jahanje na
istom vetru.

**Zaduženost — Fastenal je jedini praktično bez finansijskog rizika** (neto
gotovina, pokrivenost kamata 267x) naspram GWW (30,8x) i MSM (12,5x) koji
oba nose realan dug.

*Izvor: W.W. Grainger 10-K FY2025 (CIK 0000277135, accession
0000277135-26-000011) — lično verifikovano R3.htm; MSC Industrial 10-K FY2025
(CIK 0001003078, accession 0001003078-25-000123) — istraživački agent, SEC
XBRL companyfacts.*

---

## 5. Valuacija — dve nezavisne provere

**KOREKCIJA ZBOG SPLITA (obavezna pre čitanja PEG-a):** Scorecard-ov sirovi
izračun (PEG_trailing -4,99, rast akcija +18,8%) je besmislen jer meša
pre-split brojeve akcija (FY2021-2024) sa post-split brojem (FY2025, posle
2-za-1 splita 21.5.2025). Korigovano na uporedivoj (post-split-ekvivalentnoj)
osnovi:

| Metrika | Sirovo (scorecard) | Korigovano (split-ekvivalentno) |
|---|---|---|
| EPS CAGR (4g) | -9,1% (besmisleno) | **~+8,0%** |
| Rast broja akcija (CAGR) | +18,8% (besmisleno) | **~0% (stabilno)** |
| PEG_trailing | -4,99 (besmisleno) | **~5,71** (P/E 45,67 / 8,0) |
| FCF po akciji CAGR | -3,7% (besmisleno) | **~+14,5%** |

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing (korigovan) | **~5,71** — DRASTIČNO iznad praga 2,0, zahteva obrazloženje | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **1,8%** (nakon SBC: 1,8%) — najniži od svih pozicija u projektu | ništa — samo tekući cash flow |
| FCF marža | 12,8% | — |

**Fastenal je SKUP po klasičnim merilima** (P/E 45,67, PEG korigovan ~5,71,
FCF yield samo 1,8% — najniži FCF yield od svih kompanija analiziranih u ovom
projektu do sada). Ovo drastično kontrastira sa niskim FCF prinosom uprkos
odličnom kvalitetu posla (visoke marže, minimalna zaduženost, ROIC uporediv sa
mnogo većim konkurentom).

**Kontrola — da li je rast EPS-a stvaran (split-korigovana osnova):**

| Metrika | CAGR (5g, split-korigovano) |
|---|---|
| Prihod | 8,1% |
| EPS (korigovan) | ~8,0% |
| FCF po akciji (korigovan) | **~14,5%** |

**Zdrav obrazac.** FCF po akciji raste znatno brže (14,5%) i od prihoda (8,1%)
i od EPS-a (8,0%) — rast je stvaran, ne buyback-inženjering (buyback je bio
minimalan i samo u FY2022). Cash generacija po akciji raste brže od
računovodstvene zarade — pozitivan kvalitetni signal, ali ga tržište već
naplaćuje visokim multiplom.

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
| FAST FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R7/R8.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/815556/000081555626000009/ | podnet 05.02.2026 |
| FAST FY2021-FY2022 finansijski podaci | 10-K FY2022 (accession 0000815556-23-000009), R3/R5/R8.htm lično verifikovano | sec.gov/Archives/edgar/data/815556/000081555623000009/ | podnet 07.02.2023 |
| FAST poslovni opis, konkurencija | Form 10-K FY2025, Item 1 | sec.gov/Archives/edgar/data/815556/000081555626000009/fast-20251231.htm | podnet 05.02.2026 |
| FAST cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-28, close 49.78 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-28, close 150.12 |
| FAST WACC (7,91%, bottom-up) | rf: treasury.gov (4,73%, 10Y UST, 28.08.2026); beta: stockanalysis.com (0,71, treća strana) | treasury.gov, stockanalysis.com/stocks/fast/statistics | 28-31.08.2026 |
| Grainger (GWW) FY2025 finansijski podaci | 10-K FY2025, R3.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/277135/000027713526000011/ | podnet 19.02.2026 |
| MSC Industrial (MSM) FY2025 finansijski podaci | SEC XBRL companyfacts API, CIK 0001003078, 10-K accession 0001003078-25-000123 | data.sec.gov/api/xbrl/companyfacts/CIK0001003078.json | podnet 23.10.2025 |
