# Analiza: Medpace Holdings, Inc. (MEDP)

**Datum:** 2026-08-18 | **Analitičar:** Dragan | **Cena na dan analize:** 578,50 USD (zaključna cena 2026-08-14, IBKR)
**U krugu kompetencije:** NE — klinička istraživanja/CRO nisu Draganov krug kompetencije
(softver/.NET/Microsoft ekosistem). Biran namerno kao test slučaj (`docs/05` §4/§5) —
provera da li K1-ALT ispravka generalizuje na CRO avansni model kao kod MANH.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Medpace je full-service CRO (Contract Research Organization) — sprovodi kliničke
studije faza I–IV za biotech/farma klijente, specijalizovan za **male i srednje
biopharma kompanije**.

**Funkcionalne jedinice (izvor: 10-K Item 1):** Medical Department (terapeutski
lideri), Clinical Trial Management (sopstveni sistem ClinTrak), Data-Driven
Feasibility, Study Start-Up, Patient Recruitment, Clinical Monitoring, Regulatory
Affairs, Medical Writing, Biometrics/Biostatistika, Pharmacovigilance, Core
Laboratory (imaging + kardiovaskularni), Central Laboratory (4 lokacije: Cincinnati,
Leuven Belgija, Šangaj, Singapur), Bioanalytical Laboratory, Clinics.

**Terapeutske oblasti FY2025 (prihod):** Oncology $747,6M, Metabolic $745,0M, Other
$408,5M, CNS $254,8M, Cardiology $239,4M, AVAI $134,9M.

**Backlog:** $3.027,2M na 31.12.2025 (+4,3% god/god). Net new business awards:
$2.646,8M (FY2025) vs $2.230,0M (FY2024).

**Konkurencija — imenovana eksplicitno (Item 1, "Competition"), direktan citat:**
*"Our major CRO competitors include IQVIA Holdings Inc., ICON plc, PPD, Inc. (now
part of Thermo Fisher Scientific Inc.), Fortrea, Inc., and numerous specialty and
regional CROs."*

**Koncentracija kupaca — potvrđena umerena** (viša nego kod MANH/OTIS/CPRT/IDXX):
top 10 kupaca = 35,1% prihoda FY2025, nijedan pojedinačan kupac >10%.

**Geografija/mreža:** ~6.200 zaposlenih u **46 zemalja** (31.12.2025). Glavni kampus:
Cincinnati, Ohio (~620.000 kv. stopa, 5 zgrada). Prihod po lokaciji ugovarajućeg
entiteta je ~99% SAD — ovo je **artefakt kontraktne strukture, ne mesta izvršenja
studija** (MEDP posluje globalno kroz podružnice).

**Dividende/buyback:** Nikad dividende. Buyback drastično ubrzan: FY2023 $144,0M →
FY2024 $174,2M → **FY2025 $917,4M** (2.961.924 akcija). Preostala autorizacija na
31.12.2025: $821,7M — očekuj nastavak agresivnog otkupa.

*Izvor: Form 10-K FY2025 (godina završena 31.12.2025), CIK 0001668397, accession
0001668397-26-000006, Item 1, Item 1A, Item 2, Item 5.*

---

## 2. Moat — dve rečenice (obavezna kapija)

*(popunjava Dragan)*

- Kategorija: *(popuni)*
- **Šta bi ubilo ovaj moat u 5 godina:** *(popuni)*
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** *(popuni)*

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/MEDP.json` (kompletan fajl:
`analize/MEDP-scorecard.md`):

```
SCORECARD — Medpace Holdings, Inc. (MEDP)
Sektor: Zdravstvo - CRO | Valuta: USD (hiljade) | Podaci: 5 god.

HARD KAPIJE
G1 (ROIC ≥12% i spread ≥3pp nad WACC):        N/P — inv. kapital -37.978 (-1,5% prihoda), K1-ALT aktiviran (vidi §5 za mehanizam)
G2 (Neto dug/EBITDA ≤2.5x, pokriv. kamata ≥4x): PROŠAO — ND/EBITDA -0,88x (neto gotovina), kamate N/A (nema duga)
G3 (FCF pozitivan ≥4/5 god.):                  PROŠAO — 5/5
G4 (FCF konverzija 5g prosek ≥0.7):            PROŠAO — 1,41
G5 (Moat u 2 rečenice):                        PROŠAO (formalno, čeka Draganovu formulaciju — vidi §2)
G6 (Nije u isključenom sektoru):                PROŠAO

Prošlo: 5/6 | Palo: 0 | Nije primenljivo: 1 (G1 → K1-ALT generalizuje van softvera, prvi put)

K2 (marže): Bruto 30,1% | Operativna 21,1% (RASTE, 17,4%→21,1% kroz 5g) | Neto 17,8% (RASTE)
K3 (zaduženost): ND/EBITDA -0,88x | pokrivenost kamata N/A (nema duga u FY2024-25)
K4 (FCF): FCF konverzija prosek 1,41 | SBC/prihod 1,4% (zanemarljivo) | rast akcija CAGR -5,9%
K5 (valuacija @ 578,50): P/E 37,86 | PEG_trailing 1,13 (privlačno, ispod praga 2,0!) | FCF yield na EV 4,1%
```

**Kapije:** prošlo 5/6 | palo 0 | nije primenljivo 1 (G1 → K1-ALT, ne računa se kao
prošla kapija po pravilu §3).
**Override (ako je kapija pala):** nema pale kapije.

---

## 4. Poređenje sa konkurencijom

**Velika vest otkrivena tokom istraživanja: ICON plc (jedan od imenovanih
konkurenata) ima aktivnu računovodstvenu istragu.** U oktobru 2025. Odbor za
reviziju ICON-a pokrenuo je istragu o priznavanju prihoda od ugovora za klinička
ispitivanja (nakon interne prijave), utvrdio greške u periodu Q3 2023–Q4 2024, i
**restatovao finansijske izveštaje**: FY2024 prihod −1,1% ($8.281,7M→$8.189,0M),
FY2024 neto dobit −6,6%. Menadžment je zaključio da interna kontrola nad finansijskim
izveštavanjem **nije bila efektivna** na 31.12.2025 (material weakness). Kompanija
se samoprijavila SEC-u. **Ovo mora biti eksplicitno navedeno kao ograničenje
pouzdanosti — ICON-ovi brojevi ispod nose rizik dodatnih revizija.**

| Metrika | MEDP | ICON plc (ICLR)* | IQVIA — R&D Solutions segment (CRO deo) |
|---|---|---|---|
| Prihod | $2.530,2M (FY2025) | $8.251,3M (FY2025) | $8.896M (FY2025, segment) |
| Bruto marža | **30,1%** | 26,4% | N/A (segment ne prikazuje bruto odvojeno) |
| Operativna marža (GAAP) | **21,1%** | 5,4% GAAP (13,8% "prilagođeno", non-GAAP) | 21,0% (segment margin) |
| Neto marža | **17,8%** | 2,8% GAAP | N/A (segment ne prikazuje net income) |
| Neto dug/EBITDA | **-0,88x (neto gotovina)** | 3,34x GAAP / ~1,97x prilagođeno | N/A (segment) — IQVIA konsolidovano: 4,13x |
| Pokrivenost kamata | N/A (nema duga) | 2,24x GAAP / ~5,13x prilagođeno | N/A (segment) — IQVIA konsolidovano: 2,99x |
| Backlog | $3,0 mlrd | N/A — nije nađen jedinstven broj u 20-F | $32,7 mlrd (R&D Solutions, ali ~3x veći prihod od MEDP) |

*ICON brojevi iz 20-F FY2025 (CIK preko accession 0001628280-26-038487), **pod
napomenom o restatement rizika iznad**. IQVIA R&D Solutions iz 10-K FY2025
(CIK 0001478242, accession 0001628280-26-008322), Item 7 segment breakdown.
**PPD (Thermo Fisher)** — potvrđeno integrisan kao poslovna linija "Clinical
research" unutar "Laboratory Products and Biopharma Services" segmenta (Thermo
Fisher 10-K, CIK 0000097745), prihod $7.915M FY2025 ali **nema odvojene marže/duga/
FCF-a** — ostaje kvalitativni konkurent bez sopstvenog scorecard-a.

**Ključni nalaz — MEDP ima najbolju operativnu maržu i najčistiji bilans u grupi.**
MEDP-ova operativna marža (21,1%) je uporediva sa IQVIA-inim čistim CRO segmentom
(21,0%) — validno poređenje jer je oboje na nivou "samo CRO posao". MEDP nadmašuje
ICON-ovu GAAP operativnu maržu (5,4%, iako je ta godina opterećena restatement-om i
jednokratnim stavkama — "prilagođena" 13,8% je ipak niža od MEDP-ove). **MEDP je
jedina od tri kompanije bez ikakvog neto duga** — ICON nosi 3,34x (GAAP) i IQVIA
(cela kompanija) 4,13x. Ovo je snažan signal da MEDP-ov visok kvalitet nije
industrijska norma — ICON i IQVIA su preuzimanjima (PRA Health Sciences za ICON,
2021) nagomilali dug da bi rasli, MEDP nije.

**Fortrea Inc.** je pomenut u 10-K kao konkurent van originalne liste — spinoff
Labcorp-ovog CRO segmenta (2023), samostalno javno preduzeće. **Nije dalje
istražen u ovoj sesiji** — otvoreno za dodatno istraživanje ako je potrebno.

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **1,13** (P/E 37,86 / EPS CAGR 33,5%) — **ispod praga 2,0, privlačno** | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **4,1%** | ništa — samo tekući cash flow |
| FCF yield nakon SBC | **3,9%** | SBC zanemarljiv (1,4% prihoda) |

**MEDP je jedina kompanija do sada gde je P/E visok (37,86) ALI PEG_trailing ispod
praga (1,13)** — jer EPS raste izuzetno brzo (33,5% CAGR). Ovo je suprotno IDXX
slučaju (visok P/E, visok PEG) — MEDP-ov visok P/E je bar delimično opravdan tempom
rasta, ne čisto skup.

**K1-ALT mehanizam — detaljnije objašnjenje (za razliku od čistog MANH slučaja):**
Investirani kapital ide od $491.624K (43,0% prihoda, FY2021) do **negativnog**
(-$37.978K, FY2025), ali mehanizam NIJE identičan MANH-u:
- Working capital (obrtni kapital) je negativan već od FY2022 zbog rasta **Advanced
  billings** (avansi klijenata) — ovo *potvrđuje* CRO avansnu hipotezu iz `docs/05`.
- ALI standardni investirani kapital ostaje **pozitivan do FY2023** jer ga "nosi"
  goodwill od $662M (konstantan, iz LBO strukture pre IPO-a) i operativna imovina —
  te stavke nisu u obrtnom kapitalu.
- Investirani kapital postaje negativan tek **FY2024–2025**, najviše zbog
  **agresivnog buyback-a** ($917,4M samo u FY2025, equity pao sa $952,9M na $459,1M
  kroz 5 godina) koji je istovremeno trošio i equity i gotovinu.
- **Zaključak: K1-ALT ispravka generalizuje (G1 je ispravno N/P), ali uzrok je
  hibridan — delom avansi klijenata (MANH obrazac), delom equity uništen buyback-om
  (OTIS obrazac).** Ovo je vredan nalaz za metodologiju — nije čist test slučaj kao
  što je docs/05 pretpostavio.

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 22,0% |
| EPS | 33,5% |
| **FCF po akciji** | **38,7%** |

EPS raste 11,5pp brže od prihoda (skripta upozorava) — ALI FCF po akciji raste **još
brže** (38,7%) — isti zdrav obrazac kao CPRT/IDXX: buyback je finansiran realnom
gotovinom, ne dugom (MEDP praktično nema dug), i FCF/akcija dokazuje da rast nije
finansijski inženjering.

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
| MEDP FY2025 finansijski podaci | 10-K FY2025, R3/R5.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/1668397/000166839726000006/ | podnet 10.02.2026 |
| MEDP FY2021-FY2024 finansijski podaci | 10-K FY2023 (accession 0001668397-24-000013) i 10-K FY2021 (accession 0000950170-22-001280), interna konzistentnost provereno | sec.gov/Archives/edgar/data/1668397/ | 2022 / 2024 |
| MEDP poslovni opis, backlog, koncentracija, konkurencija | Form 10-K FY2025, Item 1, Item 1A, Item 2, Item 5 | sec.gov/Archives/edgar/data/1668397/000166839726000006/medp-20251231.htm | podnet 10.02.2026 |
| MEDP cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-14, close 578.50 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-14, close 150.40 |
| MEDP WACC (9,86%, bottom-up) | rf: treasury.gov; beta: stockanalysis.com (treća strana) | treasury.gov, stockanalysis.com/stocks/medp/statistics | 14-18.08.2026 |
| ICON plc (ICLR) FY2025 finansijski podaci + restatement/istraga | 20-F FY2025, Item 5, Note 1A (Restatement), Item 15 | sec.gov/Archives/edgar/data/(ICLR CIK)/000162828026038487/iclr-20251231.htm | podnet 27.05.2026 |
| IQVIA (IQV) FY2025 finansijski podaci + R&D Solutions segment | 10-K FY2025, Item 7 (MD&A, segment breakdown) | sec.gov/Archives/edgar/data/1478242/000162828026008322/iqv-20251231.htm | podnet 17.02.2026 |
| PPD/Thermo Fisher integracija status | 10-K FY2025 (Thermo Fisher Scientific), Note 11 (Segments) | sec.gov/Archives/edgar/data/97745/000009774526000018/tmo-20251231.htm | podnet 26.02.2026 |
