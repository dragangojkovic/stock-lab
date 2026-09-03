# Analiza: Stryker Corporation (SYK)

**Datum:** 2026-09-02 | **Analitičar:** Dragan | **Cena na dan analize:** 317,40 USD (zaključna cena 2026-09-01, IBKR)
**Status:** **ODBIJENO** — hard kapija G1 (ROIC) pala na oba praga, bez override-a.
**U krugu kompetencije:** NE — medicinski uređaji/ortopedija nisu u
Draganovom IT/.NET fokusu.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6). Napomena: kapija G1 je
> pala — po CLAUDE.md §3, ovo formalno isključuje akciju osim ako Dragan napiše
> pisano obrazloženje override-a u §8.

---

## 1. Šta kompanija zapravo radi

Stryker je diversifikovan proizvođač medicinskih uređaja kroz **dva
segmenta**:
- **MedSurg and Neurotechnology** (~58% prihoda FY2023) — hirurška oprema,
  neurotehnologija.
- **Orthopaedics and Spine** (~42%) — zamena zglobova, trauma, kičmeni
  implanti, **Mako robotska platforma**.

**Konkurencija (imenovano u opisu Orthopaedics segmenta, ne u generičkom
"Competition" pasusu):**
- Joint replacement/trauma/robotika: Stryker je jedan od 4 vodeća globalna
  igrača — **Zimmer Biomet, DePuy Synthes (J&J), Smith & Nephew**.
- Spine: jedan od 4 vodeća — **Medtronic Sofamor Danek, Globus Medical
  (uklj. Nuvasive), DePuy Synthes**.

**Mako Robotic-Arm Assisted Surgical System** (Partial Knee/Total Hip/Total
Knee): FY2023 10-K obeležava 10-godišnjicu Mako Surgical Corp akvizicije i
prekretnicu od **1 milion kumulativnih Mako procedura globalno**. Nema
eksplicitnog broja instalirane baze u 10-K tekstu (van SEC scope-a).

**KLJUČNI NALAZ #1 — Stryker je serijski akvizitor.** Goodwill je rastao
**svih 5 godina** ($12,918M → $19,291M, +49%). Najveći skokovi: FY2022
(Vocera akvizicija, $2.563M cash) i **FY2025 (+$3,44 mlrd, akvizicije cash
$4,96 mlrd — identitet velike akvizicije NIJE potvrđen u ovoj analizi, N/A —
treba proveriti Napomenu o akvizicijama u FY2025 10-K)**. FY2025 takođe
uključuje **divestiranje Spinal Implants biznisa** ($165M proceeds) —
portfolio restrukturiranje, ne samo ekspanzija.

**KLJUČNI NALAZ #2 — jednokratna stavka objašnjava pad EPS-a.** Income
statement ima posebnu liniju **"Goodwill and other impairments"**: $36M
(2023) / **$977M (2024)** / $170M (2025). FY2024 impairment od $977M
**objašnjava pad diluted EPS-a** (2023: $8,25 → 2024: $7,76) uprkos rastu
prihoda ($20,5→$22,6 mlrd) — **nije signal slabljenja operativnog
poslovanja**, već jednokratna računovodstvena stavka.

**Kapitalna alokacija — eksplicitno rangirana (FY2023 10-K MD&A):** (1)
Akvizicije, (2) Dividende, (3) Otkup akcija. Buyback je bio **$0 svih 5
godina** (2021-2025) — dosledno sa izjavljenim prioritetom.

**Napomena — nepotvrđeno:** Efektivna poreska stopa je skočila na 28,1% u
FY2025 (vs 13,8-14,3% FY2023-2024) — uzrok nije istražen u ovoj sesiji, N/A.

*Izvor: Form 10-K FY2025, CIK 0000310764, accession 0000310764-26-000010,
Item 1, R3/R5/R8.htm.*

---

## 2. Moat — NE POPUNJAVA SE (akcija odbijena pre ove faze)

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/SYK.json` (kompletan fajl:
`analize/SYK-scorecard.md`):

```
SCORECARD — Stryker Corporation (SYK)
Sektor: Zdravstvo - medicinski uredjaji/ortopedija

G1 (ROIC ≥20% medicinski aparati po docs/05, spread ≥3pp nad WACC): PAO
    — medijana 10,3%, WACC 7,6%, spread SAMO 2,6pp
    (PADA I PO OPŠTEM 12% pragu — medijana je ISPOD 12%, a kamoli sektorskog
    praga od 20%+ za medicinske aparate)
G2 (Neto dug/EBITDA ≤2.5x, pokriv. kamata ≥4x): PROŠAO — 1,95x / 8,1x
G3 (FCF pozitivan ≥4/5 god.): PROŠAO — 5/5
G4 (FCF konverzija ≥0.7): PROŠAO — 1,14
G5 (Moat u 2 rečenice): čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru): PROŠAO

Prošlo: 5/6 | PALO: 1 (G1)
```

**G1 pada nedvosmisleno na OBA praga — opšti (12%) i sektorski (20%+).**
Medijana ROIC-a (10,3%) je najniža od svih pozicija analiziranih u ovom
projektu do sada koje su formalno "prošle" bilo koji prag.

**Kontrolna provera (CLAUDE.md K1 nalog — ROIC ex-goodwill):**
- FY2021: NOPAT $2.259M / (invest. kapital $24.412M − goodwill $12.918M =
  $11.494M) = **19,7%**
- FY2025: NOPAT $3.516M / (invest. kapital $34.268M − goodwill $19.291M =
  $14.977M) = **23,5%**

**Ex-goodwill ROIC (20-23%) je solidan i blizu/iznad sektorskog praga** — bolji
nego AME-ov standardni ROIC, ali NIŽI od AME-ovog ex-goodwill nivoa
(28-30%). **Razlika između standardnog i ex-goodwill ROIC-a kod SYK (10,3%
vs ~20-23%) je VEĆA proporcionalno nego kod AME** — goodwill čini veći deo
investiranog kapitala kod SYK ($19,3 mlrd goodwill od $34,3 mlrd ukupnog
investiranog kapitala = 56%, naspram AME-ovih $7,17 mlrd od $12,45 mlrd =
58% — slično proporcionalno, ali SYK-ov osnovni posao je manje profitabilan
na tom kapitalu (23,5% vs AME-ovih 29,8%).

**ROIC ex-goodwill i dalje ispod docs/05 20%+ praga u FY2021 (19,7%)**, iako
FY2025 (23,5%) prelazi prag — trend RASTE, za razliku od AME gde je
ex-goodwill ROIC bio stabilan kroz ceo period.

---

## 4. Poređenje sa konkurencijom

**NIJE SPROVEDENO u ovoj analizi.** Zimmer Biomet (ZBH), Smith & Nephew
(SNN) i Globus Medical (GMED) su javno listirani i mogli bi se porediti u
budućem prolazu. **Otvoreno pitanje — K2 poređenje sa 3-5 konkurenata
(CLAUDE.md obavezno pravilo) nije zadovoljeno u ovoj verziji analize.**

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | N/A (scorecard field prazno) — ručno: P/E 37,79 / EPS CAGR N/A (distorzovan impairment-om) | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **3,2%** (nakon SBC: 3,0%) | ništa — samo tekući cash flow |
| FCF marža | 17,1% | — |

**PEG_trailing nije pouzdano izračunljiv** jer je FY2024 EPS distorzovan
$977M impairment-om — istorijski EPS CAGR ne odražava stvarni operativni
trend. **Preporuka: koristi EBIT ili NOPAT CAGR (ex-impairment) za precizniju
sliku rasta**, ne GAAP EPS CAGR, dok se PEG za SYK ne izračuna ponovo na
očišćenoj osnovi.

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 10,1% |
| EPS (GAAP, distorzovan impairment-om) | 12,7% |
| FCF po akciji | 11,5% |

**Broj akcija praktično stabilan** (CAGR +0,3%, buyback $0 svih godina) —
EPS rast NIJE buyback-inženjering, ali je delimično distorzovan
impairment-om u suprotnom smeru (FY2024 EPS je BIO NIŽI nego što bi bio bez
impairment-a, pa GAAP EPS CAGR podcenjuje pravi operativni rast, ne
precenjuje ga).

---

## 6-7. Opovrgavajuće tačke / predviđanja — NE POPUNJAVA SE

---

## 8. Odluka

- [ ] Ulazi u paper portfolio
- [ ] Watchlist
- [x] **Odbijeno**

**Razlog:** Hard kapija G1 (ROIC) pada na oba praga — medijana 10,3% je
ispod i opšteg minimuma (12%) i sektorskog praga za medicinske aparate
(20%+). ROIC ex-goodwill (20-23%) pokazuje da je osnovni posao solidan, ali
za razliku od AME (gde je override odobren jer je ex-goodwill ROIC
konzistentno visok 28-30% kroz ceo period), Stryker-ov ex-goodwill ROIC
je bio ispod sektorskog praga i u FY2021 (19,7%) — slabija margina
sigurnosti za override argument. Bez pisanog obrazloženja override-a, po
CLAUDE.md §3 pravilu akcija je odbijena.
- Nema upisa u `positions.csv`, `watchlist.csv` ni `predvidjanja.csv`.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| SYK FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R8.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/310764/000031076426000010/ | podnet 11.02.2026 |
| SYK FY2021 finansijski podaci | 10-K FY2021 (accession 0000310764-22-000028), R3.htm lično verifikovano | sec.gov/Archives/edgar/data/310764/000031076422000028/ | podnet 11.02.2022 |
| SYK FY2022 finansijski podaci (equity/buyback potvrda) | 10-K FY2022 (accession 0000310764-23-000017), R8.htm lično verifikovano | sec.gov/Archives/edgar/data/310764/000031076423000017/ | podnet 10.02.2023 |
| SYK poslovni opis, segmenti, konkurencija, Mako | Form 10-K FY2023, Item 1 | sec.gov/Archives/edgar/data/310764/000031076424000024/ | podnet 14.02.2024 |
| SYK cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-09-01, close 317.40 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-09-01, close 147.92 |
| SYK WACC (7,65%, bottom-up) | rf: treasury.gov (4,79%, 10Y UST, 01.09.2026); beta: stockanalysis.com (0,77, treća strana) | treasury.gov, stockanalysis.com/stocks/syk/statistics | 01-02.09.2026 |
