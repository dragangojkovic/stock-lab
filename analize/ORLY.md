# Analiza: O'Reilly Automotive, Inc. (ORLY)

**Datum:** 2026-08-20 | **Analitičar:** Dragan | **Cena na dan analize:** 90,76 USD (zaključna cena 2026-08-18, IBKR, post-split)
**U krugu kompetencije:** NE — maloprodaja auto delova nije Draganov krug kompetencije
(softver/.NET/Microsoft ekosistem). Biran namerno kao test slučaj (`docs/05` §4/§5) —
kombinuje tri problema odjednom: negativan equity od buyback-a, realan finansijski
dug, i obaveze po lizingu prodavnica.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

ORLY je maloprodaja auto delova sa **"dual market strategy"** — prodaja i DIY
(do-it-yourself) potrošačima i profesionalnim servisnim radnjama. FY2025: DIY 49,3%,
Professional 48,7%, Other 2,0% prihoda. **Professional segment raste udeo brže od
DIY** — strukturni pomak.

**Distribuciona mreža ("Strategic Regional Tiered Distribution Network"):**
- **32 distribucionih centara** — pristup preko 156.000 SKU (same-day/overnight)
- **399 Hub prodavnica** — prosečno 63.000 SKU po hub-u (do ~115.000 na pojedinim
  tržištima)
- >95% prodavnica prima višestruke isporuke istog dana, uklj. vikende
- **6.585 prodavnica ukupno** (6.447 SAD, 112 Meksiko, 26 Kanada), +207 net novih u
  2025, plan +225-235 u 2026

**Koncentracija dobavljača — potvrđena umerena:** preko 655 dobavljača, top 5 = 23%
ukupne kupovine. Najveći pojedinačan dobavljač = ~8%, sledeća četiri po 3-5% svaki.
**Nema materijalnog rizika koncentracije na jednom dobavljaču.**

**Konkurencija — imenovana eksplicitno (Item 1, "Competition"):**
- Nacionalni lanci: **AutoZone, Advance Auto Parts, CARQUEST, NAPA**
- Regionalni lanci, wholesale/jobber prodavnice, dileri automobila
- Mass merchandiseri i online: **Wal-Mart, Amazon.com** (imenovani eksplicitno)

**Dividende/buyback:** Nikad dividende (od IPO 1993). Kapital se vraća isključivo
kroz buyback — ukupno ~$13,08 mlrd FY2021-2025.

**Napomena o formatu podataka — 15-za-1 forward split (10.06.2025):** svi brojevi
akcija/EPS u ovoj analizi su post-split (uporedivi kroz sve godine); FY2021/2022 su
matematički konvertovani iz originalno objavljenih pre-split brojeva (deterministička
konverzija, ne procena — vidi `data/ORLY.json` napomena).

*Izvor: Form 10-K FY2025 (godina završena 31.12.2025), CIK 0000898173, accession
0000898173-26-000009, Item 1.*

---

## 2. Moat — dve rečenice (obavezna kapija)

> Gusta, slojevita distributivna mreža (32 distribucionih centara + 399 hub
> prodavnica, 156.000 SKU) omogućava dostavu profesionalnim mehaničarima istog
> dana — prelazak na konkurenta bez uporedive gustine rizikuje nestašice delova i
> gubitak prihoda servisera. Preko 95% prodavnica prima višestruke isporuke istog
> dana; profesionalni segment (48,7% prihoda) raste brže od DIY, potvrđujući da
> zavisnost profesionalaca od te gustine raste.

- Kategorija: ekonomija obima/gustine (logistika) + switching costs (zavisnost
  profesionalnih kupaca od pouzdane isporuke)
- **Šta bi ubilo ovaj moat u 5 godina:** Amazon/veliki e-commerce postigne
  uporedivu gustinu isporuke delova istog dana kroz svoju širu logističku mrežu,
  ili prelazak na EV smanji potražnju za tradicionalnim rezervnim delovima.
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** izgradnja
  32 distribucionih centara + 399 hub prodavnica sa 60-150K SKU svaki je trajala
  decenijama kapitalnih ulaganja i akvizicije nekretnina — uporediva gustina traži
  godine, ne samo kapital.

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/ORLY.json` (kompletan fajl:
`analize/ORLY-scorecard.md`):

```
SCORECARD — O'Reilly Automotive, Inc. (ORLY)
Sektor: Maloprodaja - auto delovi | Valuta: USD (hiljade) | Podaci: 5 god.

HARD KAPIJE
G1 (ROIC ≥12% i spread ≥3pp nad WACC):        N/P — equity -763.352 (negativan svih 5 god.), K1-ALT2
G2 (Neto dug/EBITDA ≤2.5x maloprodaja, pokriv. kamata ≥4x): PROŠAO — ND/EBITDA 2,09x (SA lizingom), kamate 14,7x
G3 (FCF pozitivan ≥4/5 god.):                  PROŠAO — 5/5
G4 (FCF konverzija 5g prosek ≥0.7):            PROŠAO — 0,96 (ALI oštro OPADA, vidi §5)
G5 (Moat u 2 rečenice):                        PROŠAO (formalno, čeka Draganovu formulaciju — vidi §2)
G6 (Nije u isključenom sektoru):                PROŠAO

Prošlo: 5/6 | Palo: 0 | Nije primenljivo: 1 (G1 → K1-ALT2, treći put u projektu posle OTIS)

K2 (marže): Bruto 51,6% | Operativna 19,5% (stabilna ali blago OPADA 21,9%→19,5%) | Neto 14,3%
K3 (zaduženost, dug UKLJUČUJE lizing prodavnica po docs/05 §2): ND/EBITDA 2,09x | pokrivenost kamata 14,7x
  test produktivnosti duga: NIJE BIO PRODUKTIVAN (dug CAGR 9,7% > EBIT CAGR 4,4%)
K4 (FCF): FCF konverzija prosek 0,96 (ali FY2025 samostalno = 0,63, oštar pad) | rast akcija CAGR -4,8%
K5 (valuacija @ 90,76): P/E 30,56 | PEG_trailing 3,25 (iznad praga 2,0!) | FCF yield na EV 1,9% (nisko)
```

**Kapije:** prošlo 5/6 | palo 0 | nije primenljivo 1 (G1 → K1-ALT2, ne računa se kao
prošla kapija po pravilu §3).
**Override (ako je kapija pala):** nema pale kapije.

---

## 4. Poređenje sa konkurencijom

**Konkurencija ovde funkcioniše kao "kontrolna grupa" različitog kvaliteta** — retko
vidljivo tako čisto u ovom projektu.

| Metrika | ORLY | AutoZone (AZO, FY2025) | Advance Auto Parts (AAP, FY2025) | Genuine Parts (GPC, FY2025) |
|---|---|---|---|---|
| Prihod | $17.782M | $18.939M | $8.601M | $24.300M (samo 63,4% automotive, ostalo Industrial) |
| Bruto marža | 51,6% | 52,6% | 43,4% | 36,8% (diversifikovano, ne čist automotive) |
| Operativna marža | 19,5% | 19,1% | **-0,5% (GUBITAK)** | N/A GAAP (izobličeno, vidi napomena) |
| Neto marža | 14,3% | 13,2% | 0,5% (samo zbog poreske koristi, vidi napomena) | 0,3% GAAP (izobličeno) |
| Equity (kraj FY) | **-$763M** | **-$3.414M (još ekstremnije negativan)** | **+$2.198M (POZITIVAN)** | +$4.423M (pozitivan) |
| Neto dug/EBITDA | 2,09x | 2,83x (uklj. lizing) | 1,26x (nepouzdana EBITDA baza) | 1,68x |
| Pokrivenost kamata | 14,7x | 7,59x | **-0,31x (PADA K3!)** | 12,26x |
| FCF konverzija | 0,96 (prosek), 0,63 (FY2025) | 0,72 (FY2025, tačno na pragu) | **negativan FCF (-$298M)** | 6,38x (besmislen, vidi napomena) |

*Izvori: AutoZone 10-K FY2025 (godina do 30.08.2025), CIK 0000866787, accession
0001104659-25-102611. Advance Auto Parts 10-K FY2025 (53 nedelje do 03.01.2026),
CIK 0001158449, accession 0001193125-26-051305. Genuine Parts Company 10-K FY2025
(godina do 31.12.2025), CIK 0000040987, accession 0000040987-26-000003.*

**Ključni nalaz #1 — AutoZone potvrđuje da negativan equity NIJE anomalija ORLY-ja,
već industrijska norma za disciplinovane igrače.** AZO ima **još ekstremniji**
negativan equity (-$3,4 mlrd vs ORLY-jevih -$763M) uz slično zdrav operativni profil
(marže, pokrivenost kamata) — K1-ALT2 mehanizam se ponavlja identično. Ovo je
vredna potvrda: negativan equity kroz agresivan buyback je *strateški izbor
sektora* kad je posao stabilan i predvidiv (retail auto delova), ne signal
propadanja.

**Ključni nalaz #2 — Advance Auto Parts je upozoravajući primer šta se desi kad
ovaj model pođe po zlu.** AAP ima **pozitivan equity** (nije primenio K1-ALT2 igru
agresivno), ali **operativni gubitak, negativan FCF, i pokrivenost kamata −0,31x**
— po CLAUDE.md pravilima, K3 kapija bi kod AAP-a formalno PALA. Neto dobit od $44M
je **gotovo isključivo od poreske koristi ($159M)**, ne od poslovanja — klasičan
"zarada na papiru" signal. **Ovo je dokaz da retail auto delova nije automatski
dobar posao — izvršenje je presudno, ne sam sektor.**

**Ključni nalaz #3 — GPC-ova GAAP neto dobit je izobličena jednokratnim troškom, ne
pravi signal.** Pad neto dobiti −92,7% (2024→2025) je dominantno **$742M jednokratni
trošak poravnanja penzionog plana** + $151M rezervacija za bankrot dobavljača
(First Brands). Company-reported "Adjusted EPS" pad je samo −10,0% ($8,16→$7,37).
GPC je i diversifikovan (36,6% prihoda Industrial segment, ne automotive) — nije
čist peer za direktno poređenje marži.

**Zaključak za K2 pravilo ("pada li svima u grani ili samo njoj"):** Operativna
marža ORLY-ja (19,5%) blago opada, ali **ne zbog makro faktora cele grane** — AZO
je stabilan (19,1%), i samo AAP genuinski pati (izvršenje, ne sektor). ORLY-jev pad
marže (21,9%→19,5%) je specifičan njemu, vredan dalje provere u §6.

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **3,25** (P/E 30,56 / EPS CAGR 9,4%) — **iznad praga 2,0** | prošli rast se nastavlja; CLAUDE.md K5: zahteva eksplicitno obrazloženje premije |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **1,9%** — nisko, treće najniže od svih analiziranih kompanija | ništa — samo tekući cash flow |
| FCF yield nakon SBC | **1,8%** | SBC zanemarljiv (0,2% prihoda) |

**Kontrola — da li je rast EPS-a stvaran ili buyback (K5 obavezna provera):**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 7,5% |
| EPS | 9,4% |
| **FCF po akciji** | **-8,4%** |

**Ovo je najgori obrazac otkriven u ovom projektu do sada — gori od OTIS/PRGS.**
EPS raste (9,4% CAGR) isključivo kroz smanjenje broja akcija (CAGR -4,8%), dok
**FCF po akciji stvarno OPADA** (-8,4% CAGR). Za razliku od CPRT/IDXX/MEDP (gde FCF
po akciji raste brže od EPS-a — zdrav obrazac) i za razliku čak od OTIS/PRGS (gde je
FCF/akcija bar bio blizu nule ili blago negativan), ORLY-jev FCF po akciji **aktivno
opada dok se EPS prikazuje kao rastući.** Buyback maskira realno pogoršanje
gotovinske generacije po akciji — CapEx intenzitet (distribucioni centri, hub
prodavnice) raste brže nego OCF poslednje 2 godine (§K4 napomena).

**PEG iznad praga (3,25) + FCF yield nisko (1,9%) + FCF/akcija opada (-8,4%) — tri
nezavisna signala se slažu da je ovo trenutno preplaćena akcija za tempo realnog
rasta gotovine**, uprkos tome što su hard kapije formalno prošle (leverage i FCF
konverzija su i dalje u zdravom rasponu, ali trend je negativan).

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. Operativna marža nastavi da pada ispod 18% dva kvartala zaredom.
2. FCF konverzija padne ispod 0,7 dva kvartala zaredom (približavanje AAP
   obrascu).
3. Neto dug/EBITDA (sa lizingom) pređe 2,5x dva kvartala zaredom, ili pokrivenost
   kamata padne ispod 10x.

**Šta je najjači argument protiv kupovine ove akcije?**

Ovo je najgori "EPS vs FCF/akcija" obrazac u celom portfoliju — FCF po akciji
opada (−8,4% CAGR) dok EPS raste (9,4%) isključivo kroz buyback. Plaćaš PEG 3,25
za posao čija stvarna gotovinska generacija po akciji opada, uz već vidljivu
kompresiju marže (21,9%→19,5%). AAP je upozorenje šta se desi kad ovaj model
klizne u izvršenju.

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | Operativna marža ostaje u opsegu | ≥19%, trenutno 19,5% | 70% |
| 2 | FCF konverzija ostaje | ≥0,85, trenutno prosek 0,96 (FY2025 samo 0,63) | 70% |
| 3 | Neto dug/EBITDA (sa lizingom) ostaje | ≤2,2x, trenutno 2,09x | 70% |
| 4 | Pokrivenost kamata ostaje | ≥12x, trenutno 14,7x | 70% |
| 5 | FCF po akciji prestaje da opada | CAGR postaje pozitivan (trailing 2g) | 70% |

---

## 8. Odluka (popunjava Dragan)

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam konkretan trigger (vidi ispod)
- [ ] Odbijeno — razlog: {…}

**Trigger za ponovni pogled:** FCF po akciji prestane da opada I operativna marža
se stabilizuje ≥19,5% dva kvartala zaredom. Razlog za watchlist, ne odmah pozicija:
kapije formalno prolaze, ali akumulacija negativnih signala (najgori EPS/FCF
divergencija u portfoliju, opadajuća marža, skup PEG 3,25, nizak FCF yield 1,9%)
traži pauzu.

**Datum ulaza:** N/A — nije ušlo u portfolio, samo watchlist
**Cena ulaza:** N/A
**VUAA cena istog dana:** N/A
**Veličina pozicije:** N/A

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu) — primenjuju se AKO
watchlist trigger aktivira ulazak:**
1. Operativna marža nastavi da pada ispod 18% dva kvartala zaredom.
2. FCF konverzija padne ispod 0,7 dva kvartala zaredom.
3. Neto dug/EBITDA (sa lizingom) pređe 2,5x dva kvartala zaredom.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| ORLY FY2023-FY2025 finansijski podaci | 10-K FY2025, R2/R4/R7.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/898173/000089817326000009/ | podnet 27.02.2026 |
| ORLY FY2021-FY2022 finansijski podaci | 10-K FY2023 (accession 0000898173-24-000009) i 10-K FY2021 (accession 0000898173-22-000012) | sec.gov/Archives/edgar/data/898173/ | 2022 / 2024 |
| ORLY poslovni opis, distribucija, dobavljači, konkurencija | Form 10-K FY2025, Item 1 | sec.gov/Archives/edgar/data/898173/000089817326000009/orly-20251231x10k.htm | podnet 27.02.2026 |
| ORLY cena zatvaranja | IBKR TWS, sveća 1D (post-split) | — | 2026-08-18, close 90.76 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-18, close 148.78 |
| ORLY WACC (6,77%, bottom-up) | rf: treasury.gov; beta: stockanalysis.com (treća strana) | treasury.gov, stockanalysis.com/stocks/orly/statistics | 18-19.08.2026 |
| AutoZone (AZO) FY2025 finansijski podaci | 10-K FY2025 (godina do 30.08.2025) | sec.gov/Archives/edgar/data/866787/000110465925102611/azo-20250830x10k.htm | podnet 27.10.2025 |
| Advance Auto Parts (AAP) FY2025 finansijski podaci | 10-K FY2025 (53 nedelje do 03.01.2026) | sec.gov/Archives/edgar/data/1158449/000119312526051305/aap-20260103.htm | podnet 13.02.2026 |
| Genuine Parts Company (GPC) FY2025 finansijski podaci | 10-K FY2025 (godina do 31.12.2025), Segment/EBITDA reconciliation note | sec.gov/Archives/edgar/data/40987/000004098726000003/gpc-20251231.htm | podnet 20.02.2026 |
