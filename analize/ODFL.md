# Analiza: Old Dominion Freight Line, Inc. (ODFL)

**Datum:** 2026-08-31 | **Analitičar:** Dragan | **Cena na dan analize:** 198,63 USD (zaključna cena 2026-08-28, IBKR)
**U krugu kompetencije:** NE — teretni transport/logistika nije u Draganovom
IT/.NET fokusu.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Old Dominion je jedan od najvećih severnoameričkih **LTL (less-than-truckload)**
prevoznika, sa jedinstvenom integrisanom mrežom i **nesindikalizovanom radnom
snagom**. Preko 98% prihoda dolazi od LTL usluga.

**Mreža (kraj 2025):** 260 servisnih centara (240 u vlasništvu, 20 pod
zakupom), 48 centara za održavanje flote. **Flota:** 10.184 traktora (prosečna
starost 3,9 god), 30.824 linehaul prikolice, 14.313 P&D prikolice. ~20.591
zaposlenih (kraj 2025).

**Konkurencija:** 10-K (Item 1) **ne imenuje konkretne konkurente** (nema XPO,
Saia, TForce/TFI, Estes po imenu) — opisuje generički "regional,
inter-regional and national LTL carriers". Navodi (citirajući Transport
Topics, treća strana) da najveći 5/10 LTL prevoznika drže ~56%/81% domaćeg LTL
tržišta (CY2024 baza).

**Koncentracija kupaca — NISKA, zdrav signal:** najveći kupac ~4% prihoda, top
5/10/20 kupaca ~11%/16%/23% (2025).

**Zaduženost — praktično bez finansijskog rizika.** Ukupan dug je JEDNA
amortizujuća nezaštićena nota koja se smanjuje $20M/god (od $99,9M FY2021 na
$40,0M FY2025) — **NEMA finance/capital lease duga** (ODFL poseduje svoju
flotu u potpunosti, za razliku od tipičnih trucking kompanija koje flotu
finansiraju lizingom). Postoji odvojena operating lease obaveza (ASC 842,
~$100-120M/god za servisne centre) koja nije uključena u finansijski dug.

**Operating Ratio (OR — standardna trucking metrika, niže = bolje):**
73,5% (2021) → 70,6% (2022) → 72,0% (2023) → 73,4% (2024) → **75,2% (2025)** —
**pogoršava se poslednje 3 godine**, poklapa se sa opštim usporavanjem u
teretnom sektoru ("freight recession"). CapEx na revenue equipment specifično
je drastično pao 2025 ($173,8M naspram $322,6M u 2024) — konzistentno sa
cikličnim usporavanjem, ne strukturnim problemom.

*Izvor: Form 10-K FY2025, CIK 0000878927, accession 0001193125-26-067161,
Item 1, MD&A.*

---

## 2. Moat — dve rečenice (obavezna kapija)

Gustina servisne mreže (260 centara) + decenijska reputacija za
pouzdanost/doslednost isporuke u LTL industriji — klijentima je skupo da
rizikuju pouzdanost menjajući prevoznika, pogotovo kad alternativa nema
uporediv track record. Bilans bez finansijskog rizika (praktično neto
gotovina) i stabilne marže kroz cikluse potvrđuju disciplinu, ali Operating
Ratio se pogoršava poslednje 3 godine (70,6%→75,2%) — moat ublažava ciklus,
ne štiti od njega potpuno.

- Kategorija: gustina distribucione/servisne mreže + reputacija za pouzdanost
- **Šta bi ubilo ovaj moat u 5 godina:** produžena "freight recession" koja
  natera ODFL na cenovnu konkurenciju da zadrži obim, ili strukturna promena
  u e-commerce/last-mile logistici (npr. Amazon-ova sopstvena freight mreža)
  koja zaobiđe tradicionalne LTL prevoznike.
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:**
  izgradnja 260 servisnih centara + reputacija za pouzdanost izgrađena
  decenijama ne kupuje se kapitalom — LTL je posao gustine mreže gde novi
  igrač godinama posluje ispod ciljne iskorišćenosti dok gradi tu gustinu.

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/ODFL.json` (kompletan fajl:
`analize/ODFL-scorecard.md`):

```
SCORECARD — Old Dominion Freight Line, Inc. (ODFL)
Sektor: Industrija - LTL teretni transport

G1 (ROIC ≥15% industrija, spread ≥3pp nad WACC): PROŠAO
    — medijana 31,3%, WACC 10,0%, spread 21,2pp
G2 (Neto dug/EBITDA ≤2.5x, pokriv. kamata ≥4x): PROŠAO — -0,05x (neto gotovina) / 4598,1x
G3 (FCF pozitivan ≥4/5 god.): PROŠAO — 5/5
G4 (FCF konverzija ≥0.7): PROŠAO — 0,73 (blizu praga, ne komforno iznad)
G5 (Moat u 2 rečenice): čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru): PROŠAO

Prošlo: 6/6 | Palo: 0
```

**Kapije formalno prošle čisto, ALI dva signala upozorenja vredna pažnje:**

1. **ROIC opada 4 od 5 godina** (31,3% → 38,6% vrh → 31,6% → 28,0% →
   **24,2%**). I dalje čvrsto iznad sektorskog praga (15%), ali trend je
   negativan i poklapa se sa opštim pogoršanjem Operating Ratio-a. Isto
   CLAUDE.md K1 upozorenje kao kod WST — "trend > nivo".
2. **FCF konverzija (0,73) je blizu praga (0,70), ne komforno iznad** — za
   razliku od MA/V/CPRT (1,0+), ODFL nosi mnogo kapitalno-intenzivniji
   biznis (flota, terminali) pa je gep OCF-CapEx-a strukturno manji.

---

## 4. Poređenje sa konkurencijom

**NIJE SPROVEDENO u ovoj analizi.** 10-K namerno ne imenuje konkretne LTL
konkurente (Saia, TFI/TForce, XPO, Estes su najbliži javno-listirani
kandidati), a njihovi finansijski podaci nisu prikupljeni sa SEC-a u ovom
prolazu. **Otvoreno pitanje — K2 poređenje sa 3-5 konkurenata (CLAUDE.md
obavezno pravilo) nije zadovoljeno u ovoj verziji analize.** ODFL je istorijski
poznat u industriji po najnižem Operating Ratio-u u LTL sektoru — ali ovo NIJE
proverено u ovoj analizi direktnim SEC poređenjem, samo je opšte poznata
reputacija, ne treba je tretirati kao potvrđenu činjenicu.

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **19,08** (P/E 41,04 / EPS CAGR 2,2%) — EKSTREMNO iznad praga 2,0 | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **2,3%** (nakon SBC: 2,2%) | ništa — samo tekući cash flow |
| FCF marža | 17,4% | — |

**PEG_trailing od 19,08 je alarmantan.** Za razliku od MCO (gde je visok PEG
verovatno artefakt jednog cikličnog pada), ovde je uzrok **strukturan: prihod
praktično stagnira (CAGR 1,1% za 5 godina)** dok se P/E drži na 41,04 — tržište
plaća premijski multipl za kompaniju čiji prihod skoro ne raste.

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 1,1% |
| EPS | 2,2% |
| FCF po akciji | **12,2%** |

**Klasičan "buyback maskira stagnaciju" obrazac — vredan pažnje.** EPS raste
(2,2%) brže od prihoda (1,1%) skoro isključivo zbog agresivnog otkupa akcija
(broj akcija pao sa ~233M na ~212M, split-korigovano, za 5 godina). FCF po
akciji raste mnogo brže (12,2%) jer CapEx je pao (2025 je bila godina niske
investicije), ne zato što je operativni posao ubrzao. **Prihod koji stagnira
uz P/E od 41 i PEG od 19 je kombinacija koja zahteva jako opravdanje u §6/§8**
— ovo je verovatno najskuplja/najslabije rastuća pozicija analizirana u ovom
projektu do sada po fundamentalnom rastu, uprkos tehnički čistom prolasku svih
kapija.

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. Operating Ratio pređe 76% dva kvartala zaredom (nastavak pogoršanja iznad
   trenutnog nivoa).
2. Prihod padne (ne samo stagnira) dva kvartala zaredom bez oporavka obima.
3. ROIC (godišnji) padne ispod 20% dva kvartala zaredom (približavanje
   pragu, ne samo trend).

**Šta je najjači argument protiv kupovine ove akcije?** Ovo je verovatno
najskuplja/najslabije rastuća pozicija analizirana u projektu do sada uprkos
čistom prolasku kapija — PEG 19, prihod CAGR svega 1,1%, ROIC opada 4 od 5
godina. Buyback maskira stagnaciju: EPS raste samo zato što broj akcija
opada, ne zato što posao raste. Ako se tempo otkupa uspori (npr. CapEx
ponovo poraste), EPS rast nestaje u potpunosti. Plaćanje premijskog multipla
za ciklčan posao baš u trenutku kad sopstveni trend metrike slabe je
klasičan value trap rizik.

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | Operating Ratio ostaje pod kontrolom | ≤ 76% | 70% |
| 2 | ROIC (godišnji) ostaje solidan | ≥ 22% | 70% |
| 3 | Zaduženost ostaje minimalna | Neto dug/EBITDA ≤ 0,3x | 70% |
| 4 | FCF konverzija ostaje iznad praga | ≥ 0,70 | 70% |
| 5 | Prihod ne padne naglo | pad ≤ 3% god/god | 70% |

---

## 8. Odluka (popunjava Dragan)

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam da PEG padne na razumniji nivo kroz korekciju cene
      ILI Operating Ratio se vrati ka ~72% pokazujući da se ciklus okreće
- [ ] Odbijeno — razlog: {…}

**Razlog:** Kvalitet bilansa je izuzetan (praktično bez duga, pokrivenost
kamata u hiljadama x, kapije formalno prošle), ali valuacija (PEG 19,08) ne
kompenzuje slabljenje trenda — ROIC opada 4 od 5 godina, Operating Ratio se
pogoršava, prihod praktično stagnira (CAGR 1,1%), a EPS rast dolazi skoro
isključivo od buyback-a. Watchlist do korekcije cene ili preokreta ciklusa.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| ODFL FY2023-FY2025 finansijski podaci | 10-K FY2025, R2/R4/R7.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/878927/000119312526067161/ | podnet 24.02.2026 |
| ODFL FY2021-FY2022 finansijski podaci | 10-K FY2022 (accession 0000950170-23-003783), R4.htm lično verifikovano | sec.gov/Archives/edgar/data/878927/000095017023003783/ | podnet 22.02.2023 |
| ODFL poslovni opis, mreža, flota, konkurencija | Form 10-K FY2025, Item 1, MD&A | sec.gov/Archives/edgar/data/878927/000119312526067161/ | podnet 24.02.2026 |
| ODFL cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-28, close 198.63 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-28, close 150.12 |
| ODFL WACC (10,03%, bottom-up) | rf: treasury.gov (4,73%, 10Y UST, 28.08.2026); beta: stockanalysis.com (1,18, treća strana) | treasury.gov, stockanalysis.com/stocks/odfl/statistics | 28-31.08.2026 |
