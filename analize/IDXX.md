# Analiza: IDEXX Laboratories, Inc. (IDXX)

**Datum:** 2026-08-18 | **Analitičar:** Dragan | **Cena na dan analize:** 550,96 USD (zaključna cena 2026-08-14, IBKR)
**U krugu kompetencije:** NE — veterinarska dijagnostika nije Draganov krug kompetencije
(softver/.NET/Microsoft ekosistem). Biran namerno kao test slučaj (`docs/05` §4/§5) —
provera da li K1-ALT generalizuje i da li skupa valuacija (K5) "puca" kao kod MANH.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

IDEXX prodaje dijagnostičke analizatore i (dominantno) potrošni materijal za
veterinarske klinike — klasičan **razor/blade model**.

**Instalirana baza IDEXX VetLab premium instrumenata (hiljade jedinica, na kraj
godine, izvor: 10-K MD&A tabela):**

| Instrument | 2025 | 2024 | 2023 |
|---|---|---|---|
| Catalyst | 78 | 74 | 69 |
| Premium Hematology | 56 | 52 | 48 |
| SediVue Dx | 24 | 21 | 18 |
| IDEXX inVue Dx | 6 | — | — |

**Model naplate — precizirano, ne "besplatno postavljanje":** Direktan citat (10-K):
*"Many instruments are placed through our customer commitment arrangements in
exchange for multi-year customer commitments to purchase recurring products and
services."* Instrumenti se prodaju/plasiraju, ali veliki deo plasmana ide kroz
višegodišnje ugovore o obavezujućoj kupovini potrošnog materijala — ekonomski
ekvivalentno razor/blade modelu, ali ugovorno formalizovano (multi-year commitment),
ne samo cenovni podsticaj.

**Recurring vs capital prihod (CAG Diagnostics, izvor: Note Disaggregation of
Revenue):** Recurring (potrošni materijal/rapid assay) ~94% CAG Diagnostics prihoda
FY2025 — potvrđuje da je najveći deo prihoda ponavljajući.

**Segmenti FY2025:** CAG (Companion Animal Group) 91,9% ukupnog prihoda, Water 4,7%,
LPD (Livestock/Poultry/Dairy) 3,1%.

**Konkurencija — bogato imenovana u 10-K (Item 1, "Competitive factors"), za razliku
od PRGS:**
- Companion animal dijagnostika (SAD): **Mars, Incorporated** (brendovi Antech
  Diagnostics i Heska); **Zoetis Inc.** (uklj. Abaxis)
- Internacionalno: Zoetis, Mars brendovi, **Fujifilm**, **Arkray**, **Mindray**,
  **BioNote**
- Water/livestock testing: **Neogen**, Charm Sciences, Thermo Fisher Scientific
- Veterinarski softver: **Covetrus**
- **Rizik vertikalne integracije:** Mars istovremeno kontroliše veliki deo kupovne
  baze (Banfield Pet Hospitals, Blue Pearl, VCA) I konkurentski Antech/Heska — 10-K
  eksplicitno navodi ovo kao rizik.

**Koncentracija kupaca — potvrđena nulta**, direktan citat: *"we have no significant
customers that accounted for greater than 10% of our consolidated revenues during
the year ended December 31, 2025."*

**Geografija FY2025:** SAD 64,0%, internacionalno 36,0% (EMEA 21,8%, APAC 8,3%,
Kanada+Lat.Amerika 6,0%).

*Izvor: Form 10-K FY2025 (godina završena 31.12.2025), CIK 0000874716, accession
0000874716-26-000038, Item 1, Item 1A, Item 7, Note "Concentrations of Risk".*

---

## 2. Moat — dve rečenice (obavezna kapija)

> IDXX plasira instrumente kroz višegodišnje ugovore o obavezujućoj kupovini
> vlasničkog potrošnog materijala (rapid assay), što pravi prelazak skupim — klinika
> mora da zameni instrument i rekvalifikuje radni tok. Instalirana baza raste
> stabilno (Catalyst 69k→78k jedinica u 2 godine), a 94% CAG dijagnostika prihoda je
> recurring — potvrđuje zaključavanje.

- Kategorija: switching costs (instalirana baza + ugovori) + vlasnička/regulatorna
  barijera (odobreni testovi)
- **Šta bi ubilo ovaj moat u 5 godina:** komoditizacija point-of-care dijagnostike
  (otvoreni analizatori koji prihvataju tuđe reagense), ili Mars/Antech vertikalno
  integriše svoje klinike (Banfield, VCA, BluePearl) i istisne IDXX iz velikog dela
  tržišta koje kontroliše.
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** izgradnja
  uporedive instalirane baze + regulatorno odobren portfolio vlasničkih testova kroz
  više vrsta životinja traži godine R&D-a i kliničkog poverenja; Mars već kontroliše
  i distribuciju i sopstveni dijagnostički brend.

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/IDXX.json` (kompletan fajl:
`analize/IDXX-scorecard.md`):

```
SCORECARD — IDEXX Laboratories, Inc. (IDXX)
Sektor: Zdravstvo - veterinarska dijagnostika (razor/blade) | Valuta: USD (hiljade) | Podaci: 5 god.

HARD KAPIJE
G1 (ROIC ≥12% i spread ≥3pp nad WACC):        PROŠAO — medijana 44,2%, WACC 11,5%, spread 32,7pp (enorman)
G2 (Neto dug/EBITDA ≤2.5x zdravstvo, pokriv. kamata ≥4x): PROŠAO — ND/EBITDA 0,44x, kamate 35,0x
G3 (FCF pozitivan ≥4/5 god.):                  PROŠAO — 5/5
G4 (FCF konverzija 5g prosek ≥0.7):            PROŠAO — 0,85
G5 (Moat u 2 rečenice):                        PROŠAO (formalno, čeka Draganovu formulaciju — vidi §2)
G6 (Nije u isključenom sektoru):                PROŠAO

Prošlo: 6/6 | Palo: 0 — SVE KAPIJE PROŠLE ČISTO, DRUGI PUT POSLE CPRT

K2 (marže): Bruto 61,8% | Operativna 31,6% (stabilna, 26,7%-31,6% kroz 5g) | Neto 24,6%
K3 (zaduženost): ND/EBITDA 0,44x | pokrivenost kamata 35,0x | test produktivnosti duga: DUG JE BIO PRODUKTIVAN
  (redak pozitivan signal — dug CAGR -2,1%, EBIT CAGR 9,9%, FCF CAGR 13,5%)
K4 (FCF): FCF konverzija prosek 0,85 | SBC/prihod 1,4% (zanemarljivo)
K5 (valuacija @ 550,96): P/E 42,12 | PEG_trailing 3,81 (iznad praga 2,0 — zahteva obrazloženje) | FCF yield na EV 2,3% (nisko)
```

**Kapije:** prošlo 6/6 | palo 0 — **kompanija je fundamentalno izuzetnog kvaliteta.**
Jedini signal opreza je **K5 (soft signal, ne hard kapija)** — PEG_trailing 3,81 i
FCF yield na EV samo 2,3% ukazuju na skupu valuaciju, tačno kako je `docs/05`
predvideo za ovaj test slučaj.
**Override (ako je kapija pala):** nema pale kapije.

---

## 4. Poređenje sa konkurencijom

**Ključno ograničenje — treći put u ovom projektu (posle IAA/RB Global i TK
Elevator) da čist konkurentski par ne postoji javno.**

- **Zoetis Inc. (ZTS)** — najveći imenovani konkurent, ali je **primarno farmaceutska
  kompanija za životinje** (vakcine, parazitici), ne čist dijagnostika peer.
  "Animal health diagnostics" je objavljena kao *kategorija proizvoda* (ne finansijski
  segment): **$434M FY2025 = samo 4,6% ukupnog Zoetis prihoda** ($9.467M). Zoetis
  **ne objavljuje** operativnu maržu/ROIC za samu dijagnostiku — nemoguće izračunati
  čist diagnostics-only profit iz javnih podataka. **N/A, potvrđeno ograničenje.**
- **Heska Corporation** — bio je čist mali javni veterinarski dijagnostika
  konkurent. **Preuzet od Antech Diagnostics (Mars, Incorporated)**, transakcija
  zatvorena **13.06.2023.**, $120,00/akciju u kešu (izvor: 8-K, accession
  0001140361-23-029433). Delistovana i deregistrovana kod SEC-a (Form 15-12G,
  23.06.2023). **Nema javnih finansijskih podataka posle juna 2023.**

| Metrika | IDXX | Zoetis (CELA kompanija, kontaminirano — diagnostika je samo 4,6%) |
|---|---|---|
| Prihod | $4.304M (FY2025) | $9.467M (FY2025) — dijagnostika deo: $434M |
| Operativna marža | **31,6%** | ~37,5% (izračunato iz komponenti, cela kompanija) |
| Neto marža | **24,6%** | 28,2% |
| Neto dug/EBITDA | **0,44x** | 1,67x |
| Pokrivenost kamata | 35,0x | 16,0x |
| Koncentracija kupca | Nema >10% | **16% jednog distributera** (veća koncentracija nego IDXX) |

*Izvori: Zoetis 10-K FY2025 (godina do 31.12.2025), podnet SEC-u 12.02.2026, CIK
0001555280, accession 0001555280-26-000011, Consolidated Statement of Income,
Balance Sheet, Note 4 (Revenue by major product category), Note 4B (koncentracija
kupca). Heska 8-K, CIK 0001038133, accession 0001140361-23-029433 (13.06.2023) i
Form 15-12G, accession 0001140361-23-031048 (23.06.2023).*

**Zašto se ova tabela ne može koristiti za direktan zaključak "IDXX je bolji/gori":**
Zoetis-ovi brojevi su za celu kompaniju gde je dijagnostika sporedna linija (4,6%
prihoda) — poređenje operativne marže cele Zoetis-ove farmaceutske/vakcinske
kompanije sa IDXX-ovim čistim dijagnostičkim biznisom nije jabuka-jabuka poređenje.
**Jedini legitiman zaključak iz ove tabele:** IDXX ima niži leverage i manju
koncentraciju kupaca od Zoetis-a na nivou cele kompanije — ali ovo ne govori ništa
direktno o relativnom kvalitetu dijagnostika segmenta samog po sebi, jer taj segment
nije finansijski izdvojen kod konkurenta.

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **3,81** (P/E 42,12 / EPS CAGR 11,1%) — **iznad praga 2,0** | prošli rast se nastavlja; CLAUDE.md K5 pravilo: >2,0 "zahteva eksplicitno obrazloženje zašto plaćaš premiju" |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **2,3%** — nisko | ništa — samo tekući cash flow |
| FCF yield nakon SBC | **2,2%** | SBC zanemarljiv (1,4% prihoda), razlika minimalna |

**Ovo je tačno test slučaj koji `docs/05` predviđa — fundamenti su izuzetni (sve
kapije prolaze, ROIC 44%, dug produktivan), ali cena je vrlo visoka.** FCF yield od
2,3% je niži i od MANH-ovog (3,3%) i od OTIS-ovog (4,0%) — tržište plaća najveću
premiju baš za ovu kompaniju od svih pet analiziranih do sada.

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 7,6% |
| EPS | 11,1% |
| **FCF po akciji** | **15,4%** |

**Zdrav obrazac, sličan CPRT-u.** FCF po akciji raste brže i od EPS-a i od prihoda —
rast nije veštački napumpan (broj akcija blago opada, CAGR -1,6%, umeren buyback iz
realno generisane gotovine, ne iz duga kao kod OTIS-a/PRGS-a). **Problem nije
kvalitet rasta — problem je cena koju treba platiti za taj kvalitet.**

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. Rast instalirane baze (Catalyst) padne ispod 5% god/god dva uzastopna godišnja
   izveštaja.
2. Recurring % CAG dijagnostika padne ispod 90% dva kvartala zaredom (signal
   komoditizacije ili promene kanala).
3. Mars/Antech-kontrolisane klinike (Banfield/VCA/BluePearl) materijalno smanje
   kupovinu od IDXX-a.

**Šta je najjači argument protiv kupovine ove akcije?**

Plaćaš 42x zarade za samo 2,3% FCF yield-a na EV — najskuplje od svih pet
analiziranih kompanija. Čak i blago usporavanje rasta (trenutno 7,6% CAGR) bi moglo
da izazove ozbiljnu kompresiju multiple-a. Dodatni rizik: Mars istovremeno kontroliše
i konkurentski dijagnostički brend (Antech/Heska) I veliki deo kupovne baze
(Banfield/VCA/BluePearl) — koncentrisan rizik van IDXX-ove kontrole.

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | Operativna marža ostaje u opsegu | ≥30%, trenutno 31,6% | 70% |
| 2 | ROIC medijana ostaje | ≥35%, trenutno 44,2% | 70% |
| 3 | FCF konverzija ostaje | ≥0,85, trenutno tačno 0,85 | 70% |
| 4 | Prihod raste | ≥7% god/god, trenutno CAGR 7,6% | 70% |
| 5 | Instalirana baza (Catalyst) raste | ≥5% god/god | 70% |

---

## 8. Odluka (popunjava Dragan)

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam konkretan trigger (vidi ispod)
- [ ] Odbijeno — razlog: {…}

**Trigger za ponovni pogled:** FCF yield na EV pređe 3,5% (korekcija cene) ILI rast
prihoda ubrza iznad 10% god/god dva kvartala zaredom (opravdava premiju). Razlog za
watchlist, ne odmah pozicija: sve kapije prolaze čisto i fundamenti su izuzetni, ali
je cena (P/E 42,12, FCF yield 2,3%) najveća premija od svih pet analiziranih
kompanija — isti obrazac kao MANH, samo izraženiji.

**Datum ulaza:** N/A — nije ušlo u portfolio, samo watchlist
**Cena ulaza:** N/A
**VUAA cena istog dana:** N/A
**Veličina pozicije:** N/A

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu) — primenjuju se AKO
watchlist trigger aktivira ulazak:**
1. Rast instalirane baze (Catalyst) padne ispod 5% god/god dva uzastopna godišnja
   izveštaja.
2. Recurring % CAG dijagnostika padne ispod 90% dva kvartala zaredom.
3. Mars/Antech-kontrolisane klinike materijalno smanje kupovinu od IDXX-a.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| IDXX FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R10.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/874716/000087471626000038/ | podnet 20.02.2026 |
| IDXX FY2021-FY2022 finansijski podaci | 10-K FY2022 (accession 0000874716-23-000006), interna konzistentnost provereno | sec.gov/Archives/edgar/data/874716/ | podnet 16.02.2023 |
| IDXX poslovni opis, instalirana baza, konkurencija, koncentracija, geografija | Form 10-K FY2025, Item 1, Item 1A, Item 7, Note Concentrations of Risk | sec.gov/Archives/edgar/data/874716/000087471626000038/idxx-20251231.htm | podnet 20.02.2026 |
| IDXX cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-14, close 550.96 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-14, close 150.40 |
| IDXX WACC (11,46%, bottom-up) | rf: treasury.gov; beta: stockanalysis.com (treća strana); cost of debt: implicitna stopa iz 10-K | treasury.gov, stockanalysis.com/stocks/idxx/statistics | 14-17.08.2026 |
| Zoetis (ZTS) FY2025 finansijski podaci | 10-K FY2025, Consolidated Statements, Note 4, Note 4B | sec.gov/Archives/edgar/data/1555280/000155528026000011/zts-20251231.htm | podnet 12.02.2026 |
| Heska status (preuzeta, delistovana) | 8-K + Form 15-12G, CIK 0001038133 | sec.gov/Archives/edgar/data/1038133/ | zatvoreno 13.06.2023, deregistracija 23.06.2023 |
