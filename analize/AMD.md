# Analiza: Advanced Micro Devices, Inc. (AMD)

**Datum:** 2026-09-03 | **Analitičar:** Dragan | **Cena na dan analize:** 459,61 USD (zaključna cena 2026-09-01, IBKR)
**Status:** Hard kapija G1 (ROIC/spread) PALA — dramatično.
**U krugu kompetencije:** DELIMIČNO — poluprovodnici/hardver arhitektura nije
direktno Draganov .NET fokus, ali je blizu IT infrastrukture koju razume
bolje od proseka.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6). Napomena: kapija G1 je
> pala drastično — po CLAUDE.md §3, ovo formalno isključuje akciju osim ako
> Dragan napiše vrlo ubedljivo pisano obrazloženje override-a u §8.

---

## 1. Šta kompanija zapravo radi

AMD je fabless poluprovodnička kompanija (dizajnira čipove, proizvodnju
poverava **TSMC** za sve node-ove ≤7nm i **GLOBALFOUNDRIES** za starije
node-ove — koncentrisan rizik dobavljača, AMD nema kontrolu nad proizvodnim
kapacitetom).

**Segmenti (4 do FY2024, konsolidovano u 3 od FY2025):**

| Segment | FY2021 udeo | FY2025 udeo |
|---|---|---|
| Data Center | 22,5% | **48,0%** |
| Client | 41,9% | 30,7% |
| Gaming | 34,1% | 11,3% |
| Embedded | **1,5%** | 10,0% |

**Drastična promena miksa** — Data Center je postao dominantan segment (AI
bum), Embedded je skočio zahvaljujući Xilinx-u pa oslabio (ciklčan FPGA pad
2023-2024).

**DVA VELIKA DOGAĐAJA KOJA MENJAJU ANALIZU:**

**1) Xilinx akvizicija (zatvorena 14.2.2022, $48,8 mlrd, SVA U AKCIJAMA).**
429 miliona novih AMD akcija izdato Xilinx akcionarima (fair value $48,5
mlrd po ceni $113,18/akcija). Equity je skočio sa $7,497M na $54,750M —
porast gotovo tačno jednak vrednosti izdatih akcija. Goodwill $289M→$24,177M,
nematerijalna imovina $0→$24,118M. **Akcionari su realno razvodnjeni
(~35% dilucije)** čak i bez gotovinskog izdatka. D&A je skočio sa $407M na
$4,174M skoro isključivo zbog amortizacije Xilinx nematerijalne imovine.

**2) Duboki ciklus poluprovodnika.** EBIT: $3.648M (2021, PC/gaming bum) →
$1.264M (2022) → **$401M (2023, dno ciklusa)** → $1.900M (2024) → $3.694M
(2025, AI/data center bum). Standardna 5-godišnja medijana meša potpuno
različite faze ciklusa I različite kapitalne strukture (pre/posle Xilinx).

**Izvozne kontrole ka Kini — materijalan, kvantifikovan rizik:** BIS
ograničenja (okt. 2023) sprečavaju izvoz AI čipova bez licence. April 2025:
novi licencni zahtev pogodio specifično AMD Instinct MI308 — **rezultat
~$800 miliona troška zaliha u Q2 2025**, delimično reversovano (~$360M) u
Q4 2025 kad je dobijena licenca. Avgust 2025: pominjano da bi vlada mogla
tražiti 15% prihoda od licenciranih MI308 prodaja Kini — neformalizovano.

**Konkurencija:** Data Center — Intel, Nvidia, Altera. Client/Gaming —
Intel (CPU/APU), Nvidia (diskretna grafika, lider udela); AMD je lider u
semi-custom konzolama (Xbox/PlayStation). Embedded — Altera, Lattice,
Microsemi.

**Koncentracija:** Customer A rastao 14%→16%→18% prihoda (2021-2023), zatim
ispod praga objavljivanja.

**Dividende/buyback:** Nikad nije plaćao dividende. Buyback varijabilan:
$1.762M→$3.702M→$985M→$862M→$1.316M (2021-2025).

*Izvor: Form 10-K FY2025, CIK 0000002488, accession 0000002488-26-000018,
Item 1, Item 1A, Note o akvizicijama.*

---

## 2. Moat — ODLOŽENO (poseban slučaj, vidi §8)

AMD ide direktno na watchlist bez punog moat/predviđanja ciklusa — kombinacija
duboke cikličnosti i mega-akvizicije čini standardnu G5 formulaciju
preuranjenom pre nego što se ROIC ex-goodwill trend stabilizuje kroz još
bar 1-2 kvartala AI ciklusa.

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/AMD.json` (kompletan fajl:
`analize/AMD-scorecard.md`):

```
SCORECARD — Advanced Micro Devices, Inc. (AMD)
Sektor: Poluprovodnici

G1 (ROIC ≥20% poluprovodnici po docs/05, spread ≥3pp nad WACC): PAO DRASTICNO
    — medijana 2,8%, WACC 16,0%, spread **-13,2pp** (ROIC ISPOD cene kapitala)
G2 (Neto dug/EBITDA ≤2.0x, pokriv. kamata ≥4x): PROŠAO — -0,35x / 28,2x
G3 (FCF pozitivan ≥4/5 god.): PROŠAO — 5/5
G4 (FCF konverzija ≥0.7): PROŠAO — 1,49
G5 (Moat u 2 rečenice): čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru): PROŠAO

Prošlo: 5/6 | PALO: 1 (G1, DRASTIČNO)
```

**Ovo je najgori G1 rezultat u celom projektu do sada.** ROIC po godini:
59,5% (2021, pre-Xilinx, mali kapital) → **2,7%** (2022) → **1,2%** (2023,
dno) → 2,8% (2024) → 6,2% (2025). Standardni ROIC je i dalje ispod cene
kapitala čak i u godini oporavka (2025, AI bum).

**Kontrolna provera (CLAUDE.md K1 nalog — ROIC ex-goodwill/ex-intangibles):**
- FY2023 (dno ciklusa): NOPAT $674M / (invest. kapital $54.427M − goodwill
  $24.262M − nematerijalna $21.363M = $8.802M) = **7,7%** — I DALJE SLAB,
  ispod sektorskog praga.
- FY2025: NOPAT $3.784M / (invest. kapital $60.682M − goodwill $25.126M −
  nematerijalna $16.705M = $18.851M) = **20,1%** — tek dostiže sektorski
  prag, u godini AI buma.

**KLJUČNA RAZLIKA od AME/SYK slučajeva:** kod AME i SYK, ROIC ex-goodwill je
bio konzistentno visok (20-30%) kroz CEO period, potvrđujući da je goodwill
dilucija čist računovodstveni efekat, ne signal slabog posla. **Kod AMD-a,
ROIC ex-goodwill je i dalje bio slab u dnu ciklusa (7,7% u FY2023)** — ovo
znači da AMD-ov problem NIJE samo akvizicijska distorzija, već i **stvarna
ciklična slabost osnovnog poslovanja**. Kombinacija dva efekta (mega-akvizicija
+ dubok ciklus) čini standardni override argument mnogo slabijim nego kod
AME.

**Dodatna napomena — poreska stopa:** Efektivna poreska stopa je ekstremno
volatilna (uklj. -68% u FY2023, -2,4% u FY2025 — poreski benefiti, ne
rashodi) — NOPAT računi su manje pouzdani nego kod stabilnijih kompanija,
dodatan razlog za oprez pri tumačenju ROIC brojeva.

---

## 4. Poređenje sa konkurencijom

**NIJE SPROVEDENO u ovoj analizi.** Intel i Nvidia su očigledni kandidati za
poređenje (oba javno listirana, direktni konkurenti u glavnim segmentima).
**Otvoreno pitanje — K2 poređenje sa 3-5 konkurenata (CLAUDE.md obavezno
pravilo) nije zadovoljeno.**

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | N/A (scorecard prazno, EPS CAGR samo 0,8% zbog ciklične distorzije) | ne primenjivo — CLAUDE.md K5 eksplicitno navodi "ciklične kompanije na vrhu/dnu ciklusa" kao slučaj gde PEG ne radi |
| P/E (trailing GAAP) | **173,44** — ekstremno visok, distorzovan i ciklusom i akvizicijom | — |
| FCF yield na EV | **0,74%** (nakon SBC: 0,52%) — najniži FCF yield u celom projektu | ništa — samo tekući cash flow |
| FCF marža | 15,9% | — |

**PEG i P/E su ovde potpuno neupotrebljivi** — GAAP EPS je toliko distorzovan
ciklusom, Xilinx amortizacijom i ekstremno volatilnom poreskom stopom da ne
nosi informativnu vrednost. **FCF yield (0,74%) je najniži zabeležen u ovom
projektu** — tržište plaća ogromnu premiju za AI/data center rast koji tek
treba da se materijalizuje u FCF-u.

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 20,5% |
| EPS (GAAP, distorzovan) | 0,8% |
| FCF po akciji | 6,5% |

**Veliki jaz između prihoda (20,5%) i EPS/FCF-po-akciji rasta (0,8%/6,5%)** —
ali uzrok NIJE buyback-inženjering (broj akcija je RASTAO, CAGR +7,4%, zbog
Xilinx/ZT Systems akvizicija u akcijama) — uzrok je ciklična kompresija
marže + amortizacija akvizicione nematerijalne imovine + dilucija od
akvizicija. Prihod raste brzo, ali profitabilnost po akciji ne prati taj
rast proporcionalno.

---

## 6-7. Opovrgavajuće tačke / predviđanja — ODLOŽENO (vidi §8)

---

## 8. Odluka

- [ ] Ulazi u paper portfolio
- [x] **Watchlist** — poseban slučaj (dubok ciklus + Xilinx mega-akvizicija
      istovremeno), praćenje dok se ROIC ex-goodwill trend ne stabilizuje
- [ ] Odbijeno

**Razlog:** G1 pada drastično (spread -13,2pp, ROIC ispod cene kapitala) i,
za razliku od AME/SYK, čak ni ROIC ex-goodwill ne daje čist override
argument — bio je slab i u dnu ciklusa (7,7% FY2023), znači problem nije
samo goodwill distorzija već i stvarna ciklična slabost osnovnog posla.
Istovremeno, FY2025 ex-goodwill ROIC (20,1%) i AI/data center momentum
zaslužuju praćenje pre konačne odluke (odbijanje ili override). Nema
formalnog override obrazloženja u ovom prolazu — vraćamo se kad ciklus i
integracija ZT Systems/Xilinx daju čistiji signal.

**Trigger za ponovni pogled:** standardni (ne ex-goodwill) ROIC pređe 12%
kroz 2 uzastopna kvartala, ILI ROIC ex-goodwill ostane ≥20% kroz pun
sledeći ciklus (ne samo jednu AI-bum godinu).

- Nema upisa u `positions.csv` ni `predvidjanja.csv` (watchlist bez punog
  moat/predviđanja seta — vidi napomenu u §2).

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| AMD FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R8.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/2488/000000248826000018/ | podnet 04.02.2026 |
| AMD FY2021 finansijski podaci | 10-K FY2021 (accession 0000002488-22-000016), R5.htm lično verifikovano | sec.gov/Archives/edgar/data/2488/000000248822000016/ | podnet 03.02.2022 |
| AMD Xilinx akvizicija detalji | 10-K FY2022 (accession 0000002488-23-000047), Business Combinations napomena | sec.gov/Archives/edgar/data/2488/ | podnet 27.02.2023 |
| AMD poslovni opis, segmenti, konkurencija, izvozne kontrole | Form 10-K FY2025, Item 1, Item 1A | sec.gov/Archives/edgar/data/2488/000000248826000018/ | podnet 04.02.2026 |
| AMD cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-09-01, close 459.61 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-09-01, close 147.92 |
| AMD WACC (15,95%, bottom-up) | rf: treasury.gov (4,79%, 10Y UST, 02.09.2026); beta: stockanalysis.com (2,49, treća strana — najviša u projektu) | treasury.gov, stockanalysis.com/stocks/amd/statistics | 02-03.09.2026 |
