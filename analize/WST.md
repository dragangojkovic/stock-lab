# Analiza: West Pharmaceutical Services, Inc. (WST)

**Datum:** 2026-08-31 | **Analitičar:** Dragan | **Cena na dan analize:** 337,47 USD (zaključna cena 2026-08-28, IBKR)
**Status:** Hard kapija G4 (FCF konverzija) PALA — 0,69 naspram praga 0,70.
**U krugu kompetencije:** NE — farmaceutska pakovanja/medicinski uređaji nisu u
Draganovom IT/.NET fokusu.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6). Napomena: kapija G4 je
> pala — po CLAUDE.md §3, ovo formalno isključuje akciju osim ako Dragan napiše
> pisano obrazloženje override-a u §8.

---

## 1. Šta kompanija zapravo radi

West Pharmaceutical Services proizvodi komponente za pakovanje i isporuku
lekova. **Dva segmenta:**
- **Proprietary Products** (~81% prihoda FY2025, $2.492 mlrd) — stoppers,
  seals, containment rešenja, drug delivery/self-injection sistemi. Nosi
  **skoro sav operativni profit** (marža ~26%).
- **Contract-Manufactured Products** (~19% prihoda, $582M) — dizajn/proizvodnja
  kompleksnih uređaja za farma/dijagnostiku klijente (marža ~11%, znatno niža).

**Konkurencija (Item 1, eksplicitno imenovano):** Datwyler i Aptar. Stevanato
Group i Gerresheimer NISU imenovani u ovom 10-K tekstu (samo generički "number
of competitors") — puno K2 poređenje sa svim glavnim konkurentima nije
sprovedeno u ovoj analizi (otvoreno pitanje, §4).

**GLP-1 tema — eksplicitan rizik u 10-K:** Kompanija zavisi delom od kupaca
čiji lekovi se isporučuju injekcijom (npr. GLP-1 lekovi za dijabetes/gojaznost).
Rizik je **dvosmeran** — trenutno tailwind (self-injection uređaji), ali rizik
ako kupci pređu na oralne GLP-1 formulacije ili ređe doziranje.

**Koncentracija kupaca — RASTUĆA i materijalna:** Deset najvećih kupaca = 47,6%
prihoda (FY2025). Jedan pojedinačni kupac: **10,9% (FY2023) → 12,3% (FY2024)
→ 15,8% ($485,9M, FY2025)** — kupac nije imenovan, verovatno vezan za GLP-1
self-injection program. Ovo je promena vredna pažnje — rastuća zavisnost od
jednog kupca povećava koncentracioni rizik.

**Goodwill:** Mali i statičan (~$108-110M, promene samo FX) — nema novih
akvizicija, K1 "serijski akvizitori" zamka se ne primenjuje.

*Izvor: Form 10-K FY2025, CIK 0000105770, accession 0000105770-26-000010,
Item 1, Item 1A, Note 19 (Segment Information).*

---

## 2. Moat — dve rečenice (obavezna kapija)

*(popunjava Dragan)*

- Kategorija: *(popuni)*
- **Šta bi ubilo ovaj moat u 5 godina:** *(popuni)*
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** *(popuni)*

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/WST.json` (kompletan fajl:
`analize/WST-scorecard.md`):

```
SCORECARD — West Pharmaceutical Services, Inc. (WST)
Sektor: Zdravstvo - farmaceutska pakovanja/drug delivery komponente

G1 (ROIC ≥20% medicinski aparati/dijagnostika, spread ≥3pp nad WACC): PROŠAO
    — medijana 25,0%, WACC 9,8%, spread 15,2pp
G2 (Neto dug/EBITDA ≤2.5x, pokriv. kamata ≥4x): PROŠAO — -0,78x (neto gotovina) / 1169,8x
G3 (FCF pozitivan ≥4/5 god.): PROŠAO — 5/5
G4 (FCF konverzija ≥0.7): PAO — 0,69 (TAČNO ispod praga)
G5 (Moat u 2 rečenice): čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru): PROŠAO

Prošlo: 5/6 | PALO: 1 (G4)
```

**G4 je pala za samo 0,01 (0,69 vs 0,70 prag) — ovo je granični slučaj, ne
katastrofalan pad**, ali pravilo je pravilo: bez override obrazloženja, akcija
formalno ispada. Vredi razumeti UZROK: FCF konverzija po godini je 0,50 / 0,75
/ 0,70 / 0,56 / 0,95 (FY2021-2025) — **volatilna, ne uporno niska**. Loše
godine (2021, 2024) se poklapaju sa vrhovima CapEx ciklusa (FY2024 CapEx
$377M, najviši u periodu) — ovo je verovatno **kapitalni ciklus, ne strukturni
problem kvaliteta zarade** (OCF/NI prosek je 1,26, čvrsto iznad 1,0 — zarada
NIJE "na papiru").

**Ozbiljniji signal — trend, ne prag.** ROIC opada svih 5 godina (35,3% →
30,5% → 25,0% → 19,4% → **18,0%**) i operativna marža takođe opada (26,6% →
19,0%). Medijana (25,0%) i dalje prolazi sektorski prag (20%+ za medicinske
aparate/dijagnostiku po `docs/05`), ali **trend pada je konzistentan i
kontinuiran 5 godina — ovo je klasičan CLAUDE.md K1 upozorenje: "trend > nivo.
ROIC koji pada je gori signal od stabilnog nižeg nivoa."**

---

## 4. Poređenje sa konkurencijom

**NIJE SPROVEDENO u ovoj analizi.** 10-K imenuje Datwyler i Aptar kao direktne
konkurente, ali njihovi finansijski podaci nisu prikupljeni sa SEC-a (Datwyler
je švajcarska kompanija, verovatno ne podnosi SEC 10-K — treba proveriti da li
uopšte postoji uporediva SEC dokumentacija; Aptar — AptarGroup, ticker ATR —
JESTE SEC filer i mogao bi se porediti u budućem prolazu). **Otvoreno pitanje
— K2 poređenje sa 3-5 konkurenata (CLAUDE.md obavezno pravilo) nije
zadovoljeno u ovoj verziji analize.**

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **-8,38** (besmisleno — EPS CAGR je NEGATIVAN, -5,9%) | ne primenjivo |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **2,0%** (nakon SBC: 1,9%) | ništa — samo tekući cash flow |
| FCF marža | 15,3% | — |

**PEG ovde ne radi uopšte** (CLAUDE.md K5 eksplicitno navodi "negativna ili
blizu-nule zarada" kao slučaj gde PEG ne funkcioniše — ovde je istorijski EPS
CAGR negativan zbog opadajuće marže, ne zbog nekog jednokratnog gubitka).
**Koristiti FCF yield (2,0%, ispodprosečan) kao jedini upotrebljiv valuacioni
signal** — P/E od 49,70 je skup za posao čija marža i ROIC opadaju.

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 2,1% |
| EPS | -5,9% |
| FCF po akciji | 10,5% |

**Neobičan i vredan pažnje obrazac.** FCF po akciji RASTE (10,5% CAGR) dok EPS
OPADA (-5,9%) — ovo je suprotno od tipičnog "buyback maskira slabost"
obrasca. Uzrok: veliki CapEx ciklus 2023-2024 (D&A rastao, pritiskao
računovodstvenu zaradu) je sada iza vrhunca (CapEx pao sa $377M na $286M u
2025), pa se cash generacija oporavlja brže od GAAP zarade. **Ovo je
POTENCIJALNO pozitivan signal** (capex ciklus se završava, FCF se oporavlja)
**ILI signal da su marže strukturno niže na novom, većem kapitalnom
osnovu** — razlikovanje ova dva zahteva Draganovu procenu moat-a i budućih
kvartala, ne samo brojeve.

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

- [ ] Ulazi u paper portfolio (zahteva PISANO OBRAZLOŽENJE OVERRIDE-a za G4 — vidi CLAUDE.md §3)
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Override obrazloženje (OBAVEZNO ako se bira "Ulazi u portfolio" ili čak
Watchlist sa namerom kasnijeg ulaska):** {…}

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
| WST FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R6/R8/R10.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/105770/000010577026000010/ | podnet 17.02.2026 |
| WST FY2021-FY2022 finansijski podaci | 10-K FY2022 (accession 0000105770-23-000012), R3.htm lično verifikovano | sec.gov/Archives/edgar/data/105770/000010577023000012/ | podnet 21.02.2023 |
| WST poslovni opis, segmenti, konkurencija, GLP-1 rizik, koncentracija | Form 10-K FY2025, Item 1, Item 1A, Note 19 | sec.gov/Archives/edgar/data/105770/000010577026000010/wst-20251231.htm | podnet 17.02.2026 |
| WST cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-28, close 337.47 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-28, close 150.12 |
| WST WACC (9,78%, bottom-up) | rf: treasury.gov (4,73%, 10Y UST, 28.08.2026); beta: stockanalysis.com (1,14, treća strana) | treasury.gov, stockanalysis.com/stocks/wst/statistics | 28-31.08.2026 |
