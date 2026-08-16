# Analiza: Otis Worldwide Corporation (OTIS)

**Datum:** 2026-08-15 | **Analitičar:** Dragan | **Cena na dan analize:** 73,03 USD (zaključna cena 2026-08-13, IBKR)
**U krugu kompetencije:** NE — liftovi/eskalatori i građevinska industrija nisu Draganov krug kompetencije
(softver/.NET/Microsoft ekosistem). Svesno prihvaćeno jer je OTIS **metodološki test slučaj**
(`docs/05` §4/§5) — lomi K1/K3 u suprotnom smeru od MANH (negativan equity umesto kapitalno-lakog
poslovnog modela), ne pick po krugu kompetencije.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

OTIS proizvodi, instalira i servisira liftove i eskalatore. Posao ima dva segmenta:
**New Equipment** (prodaja/instalacija novih liftova, jednokratan prihod) i **Service**
(održavanje, popravke, modernizacija postojeće instalirane baze — recurring prihod).

**Izvori prihoda i udeo (FY2025, izvor: Segment note, 10-K FY2025):**

| Kategorija | FY2025 ($ mil.) | % prihoda |
|---|---|---|
| New Equipment | 4.989 | 34,6% |
| Maintenance and Repair | 7.584 | 52,6% |
| Modernization | 1.858 | 12,9% |
| **Service ukupno (Maint.+Repair+Moderniz.)** | **9.442** | **65,4%** |
| **Ukupno** | **14.431** | 100% |

**Geografska raspodela (izvor: Geographic External Sales note, 10-K FY2025)** — OTIS
ne objavljuje pun Americas/EMEA/APAC split, samo SAD, Kina, i "ostatak sveta":

| | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| SAD | 4.192 (29,0%) | 4.239 | 4.030 |
| **Kina** | **1.650 (11,4%)** | 1.919 | **2.444** |
| Ostatak sveta | 8.589 (59,5%) | 8.103 | 7.735 |

**Kina je pala sa $2.444M (2023) na $1.650M (2025) — pad od 32,5% u 2 godine.** Ovo
potvrđuje rizik oko kineskog tržišta novogradnje liftova pomenut u `docs/05`. 10-K
eksplicitno navodi da nijedna druga zemlja pojedinačno ne prelazi 10% prihoda.

**Ko su kupci:**
- New Equipment: developeri, generalni izvođači, državne agencije (infrastruktura).
  Direktan citat (10-K): *"we are not dependent on any single customer and do not
  have any contracts material to Otis as a whole with any single customer."*
- Service: vlasnici zgrada, facility manageri, stambena udruženja, državne agencije.

**Koncentracija kupaca** — potvrđeno nulta, direktan citat (10-K): *"There were no
customers that individually accounted for 10% or more of the Company's consolidated
Net sales for 2025, 2024 and 2023."*

**Struktura Service ugovora — OTVORENO PITANJE.** 10-K **ne objavljuje** prosečno
trajanje ugovora ni brojčani retention/renewal rate — samo kvalitativan opis
("customers owning large portfolios tend to execute long-term maintenance
agreements"). **N/A — nije objavljeno u primarnom izvoru.** Ovo je direktno relevantno
za moat tezu (§2) o switching costs — nemamo merljiv dokaz "zaključavanja" analogan
MANH-ovom RPO broju.

**Instalirana baza (izvor: 10-K FY2025):** ~2,5 miliona jedinica pod održavanjem
globalno (Otis + oprema drugih proizvođača), 37.000 servisnih mehaničara, 1.400+
ogranaka, ~1,1 milion jedinica digitalno povezano. Konkurenti eksplicitno navedeni u
10-K: **KONE Oyj, Schindler Group, TK Elevator**; nezavisni servisni provajderi drže
~50% servisnih jedinica po broju, ali manji % po vrednosti (veći/noviji ugovori
ostaju kod OEM-a).

*Izvor: Form 10-K FY2025 (godina završena 31.12.2025), podnet SEC-u 05.02.2026,
CIK 0001781335, accession 0001781335-26-000011.*

---

## 2. Moat — dve rečenice (obavezna kapija)

> OTIS ima prednost kroz servisnu mrežu na instaliranoj bazi (2,5 miliona liftova,
> 37.000 mehaničara, 1.400+ ogranaka) — teško je brzo izgraditi tu gustinu mreže
> samo novcem, treba decenije.

- Kategorija: switching costs (instalirana baza) + ekonomija obima (gustina servisne mreže)
- **Šta bi ubilo ovaj moat u 5 godina:** nezavisni serviseri (već drže ~50% jedinica
  po broju) nastave da preuzimaju i skuplje ugovore, ili se pad tržišta iz Kine
  proširi na ostatak sveta.
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** kapital
  kupuje opremu i ogranke, ali ne kupuje obučene tehničare i pola veka instaliranih
  jedinica po geografiji — to zahteva decenije, ne novac.

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/OTIS.json` (kompletan fajl:
`analize/OTIS-scorecard.md`):

```
SCORECARD — Otis Worldwide Corporation (OTIS)
Sektor: Industrija - liftovi/eskalatori | Valuta: USD (miliони) | Podaci: 5 god.

HARD KAPIJE
G1 (ROIC ≥12% i spread ≥3pp nad WACC):        N/P — equity -5.392 negativan, ROIC divergira (medijana 145,1%, artefakt strukture kapitala)
G2 (Neto dug/EBITDA ≤3.0x, pokriv. kamata ≥4x): PROŠAO — ND/EBITDA 2,97x, kamate 9,8x
G3 (FCF pozitivan ≥4/5 god.):                  PROŠAO — 5/5
G4 (FCF konverzija 5g prosek ≥0.7):            PROŠAO — 1,08
G5 (Moat u 2 rečenice):                        PROŠAO (formalno, čeka Draganovu formulaciju — vidi §2)
G6 (Nije u isključenom sektoru):                PROŠAO

Prošlo: 5 | Palo: 0 | Nije primenljivo: 1

K1-ALT2 (negativan equity): investirani kapital 1.468 (10,2% prihoda) — mali ali pozitivan,
  promašuje K1-ALT prag od 10%, i dalje besmislen kao mera kapitala. D/E takođe besmislen (-1,48).
K2 (marže): Bruto 30,3% | Operativna 14,8% (stabilna, 14,1%-15,4% kroz 5g) | Neto 9,6%
K3 (zaduženost): ND/EBITDA 2,97x | pokrivenost kamata 9,8x | test produktivnosti duga: DUG NIJE BIO PRODUKTIVAN
  (dug CAGR 2,3% > EBIT CAGR 0,3% i FCF CAGR -2,4%)
K4 (FCF): FCF $1.444M (2025) | FCF konverzija prosek 1,08 | SBC/prihod 0,6% (zanemarljivo) | rast akcija CAGR -2,2%
K5 (valuacija @ 73,03): P/E 20,87 | PEG_trailing 4,26 | FCF yield na EV 4,0% (3,8% nakon SBC)
```

**Kapije:** prošlo 5/6 | palo 0 | nije primenljivo 1 (G1 → equity negativan, K1-ALT2,
ne računa se kao prošla kapija)
**Override (ako je kapija pala):** nema pale kapije.

---

## 4. Poređenje sa konkurencijom

**Napomena o uzorku:** **TK Elevator (TKE)** je i dalje privatna kompanija (vlasništvo
konzorcijuma Advent/Cinven od spinoff-a iz thyssenkrupp-a 2020) — nema redovne javne
finansijske izveštaje. **Bitna vest otkrivena tokom istraživanja:** 29.04.2026. KONE
i konzorcijum koji vodi Advent/Cinven potpisali su Share Purchase Agreement za
spajanje KONE+TKE (EV €29,4 mlrd, cash+share transakcija, očekivano zatvaranje
najranije Q2 2027). Do zatvaranja TKE ostaje privatna — **isključena iz brojčane
tabele**, ali M&A obelodanjivanje je dalo jednokratan uvid u njene brojeve (ispod
tabele). Ovo materijalno menja budući konkurentski pejzaž — vidi napomenu posle tabele.

**Napomena o valuti:** OTIS izveštava u USD, KONE u EUR, Schindler u CHF — apsolutni
iznosi prihoda NISU direktno uporedivi bez FX konverzije (nije rađena). Marže i
racija (%, x) su valutno-neutralni i uporedivi direktno.

| Metrika | OTIS | KONE | Schindler |
|---|---|---|---|
| Prihod (izvorna valuta) | $14.431M | €11.245,2M | CHF 10.947M |
| Bruto marža | **30,3%** | N/A — nije objavljeno u bulletinu | N/A — nije objavljeno |
| Operativna marža (reported) | **14,8%** | 11,9% | 12,6% |
| Operativna marža (adjusted) | — (nema adjusted metriku) | 12,2% | 13,3% |
| Neto marža | **9,6%** | 8,8% | 9,8% |
| Neto dug/gotovina | Neto **dug** 2,97x EBITDA | Neto **gotovina** €699,8M | N/A na 31.12.2025 (istorijski neto gotovina) |
| FCF konverzija | **1,08** | N/A — treba proveriti | N/A — treba proveriti |
| P/E (trailing) | **20,87** (računato, @73,03) | ~26–28x (agregator, orijentaciono) | ~30,0x (agregator, orijentaciono) |
| Service+Modernization % prihoda | **65,4%** | 63,6% (rekonstruisano) | N/A — Schindler ne objavljuje split (jedan segment) |

*Izvori: OTIS 10-K FY2025 (05.02.2026); KONE Financial Statement Bulletin Jan-Dec 2025
(06.02.2026); Schindler Annual Results 2025 press release + Consolidated Financial
Statements (11.02.2026, Note 5 Segment reporting). P/E konkurenata: agregatori,
pristupljeno u ovoj sesiji — orijentaciono, NE primarni izvor.*

**Ključni nalaz — OTIS ima najbolju operativnu maržu u grupi (14,8%), ali najslabiji
bilans.** Suprotno očekivanju da bi "test slučaj koji lomi metodologiju" morao biti
operativno slabiji, OTIS zapravo **vodi po operativnoj marži** ispred i KONE (11,9–12,2%)
i Schindlera (12,6–13,3%). Segment mix (Service 65,4% vs KONE-ovih rekonstruisanih
63,6%) je vrlo blizu — nije objašnjenje razlike u marži.

**Ono što OTIS izdvaja u lošem smislu je bilans stanja, ne poslovanje:** KONE posluje
sa **neto gotovinom** (€699,8M), OTIS nosi **neto dug 2,97x EBITDA**. Ovo NIJE
industrijska norma (KONE dokazuje da posao može da se vodi bez leverage-a) — to je
**specifično za OTIS**, posledica spinoff-a i agresivnog buyback programa, ne
karakteristika sektora. Po K2 pravilu ("ako pada svima u grani → makro, ako samo
njoj → specifično"), primenjeno na bilans: KONE-ov neto-gotovina profil pokazuje da
OTIS-ova zaduženost je OTIS-ov izbor (buyback-om finansiran), ne nužnost sektora.

**Schindler ne objavljuje New Installation/Service/Modernization split u CHF** —
potvrđeno iz primarnog izvora (Note 5, IFRS 8 segment reporting: "Elevators &
Escalators segment is managed as one global unit") — ovo je limitacija njihove
strukture izveštavanja, ne propust istraživanja.

**TK Elevator (M&A obelodanjivanje, FY do 30.09.2025, izvor: KONE Cision saopštenje
29.04.2026) — za kontekst, ne za scorecard poređenje:** prihod €9.230M, adjusted EBIT
marža 14,8%, adjusted EBITDA marža 17,5%, neto dug €9.192M. TKE-ova adjusted EBIT
marža (14,8%) je iznenađujuće blizu OTIS-ovoj GAAP operativnoj marži (14,8%) — ali
brojevi nisu direktno uporedivi (adjusted vs GAAP, različiti izvori kvaliteta
verifikacije — M&A materijal, ne redovan godišnji izveštaj).

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **4,26** (P/E 20,87 / EPS CAGR 4,9%) | prošli rast (buyback-om vođen) se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen u ovoj sesiji | — |
| FCF yield na EV | **4,0%** | ništa — samo tekući cash flow |
| FCF yield nakon SBC | **3,8%** | SBC je zanemarljiv (0,6% prihoda) kod OTIS-a, razlika je mala |

**Kontrola — da li je rast EPS-a stvaran ili buyback (K5 obavezna provera):**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 0,2% |
| EPS | 4,9% |
| **FCF po akciji** | **−0,3%** |

**Ovo je oštriji signal nego kod MANH-a.** Prihod praktično stagnira (0,2% CAGR),
EPS raste 4,9% — ali **FCF po akciji zapravo OPADA** (−0,3% CAGR). Kod MANH-a je
FCF/akcija rastao brže od prihoda (rast je bio realan, samo skupo plaćen); kod
OTIS-a **EPS rast dolazi gotovo isključivo od smanjenja broja akcija (buyback CAGR
−2,2%/god), dok se realna gotovina po akciji ne poboljšava.** Buyback je delom
finansiran dugom (dug CAGR 2,3% > EBIT/FCF CAGR, vidi K3 test produktivnosti duga) —
ovo je finansijski inženjering koji ne stvara vrednost, ne organski rast praćen
gotovinom.

PEG_trailing od 4,26 pri ovakvom nalazu je **manje ohrabrujući nego što brojka sama
sugeriše** — rast koji ga generiše nije poslovni rast.

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. Neto dug/EBITDA pređe 3,0x dva kvartala zaredom.
2. Test produktivnosti duga ostane negativan I dug nastavi da raste brže od
   EBIT-a/FCF-a.
3. Prihod iz Kine nastavi da opada preko 15% god/god dva kvartala zaredom BEZ
   kompenzacije rastom drugde.

**Šta je najjači argument protiv kupovine ove akcije?**

Najbolja operativna marža u grupi, ali "rast" EPS-a dolazi od otkupa akcija
finansiranog dugom, ne od realnog poslovnog rasta — FCF po akciji zapravo opada.
KONE dokazuje (posluje bez duga) da to nije nužno za ovaj posao — OTIS je to sam
izabrao.

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | Neto dug/EBITDA ostaje u pragu | ≤3,0x, trenutno 2,97x | 70% |
| 2 | Operativna marža ostaje u opsegu | ≥14%, trenutno 14,8% | 70% |
| 3 | FCF konverzija ostaje | ≥1,0, trenutno 1,08 | 70% |
| 4 | Kina prihod ne opada više od praga | ≤−10% god/god | 70% |
| 5 | Broj akcija ne opada više od praga | ≤−3% god/god, trenutno CAGR −2,2% | 70% |

---

## 8. Odluka (popunjava Dragan)

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam konkretan trigger (vidi ispod)
- [ ] Odbijeno — razlog: {…}

**Trigger za ponovni pogled:** Neto dug/EBITDA padne ispod 2,0x, ILI FCF po akciji
počne realno da raste dva kvartala zaredom. Razlog za watchlist, ne odmah pozicija:
cena je jeftinija od konkurencije (P/E 20,87 vs 26–30x kod KONE/Schindler), ali to
"jeftino" je zasenjeno finansijskim inženjeringom (dug-finansiran buyback, vidi §5).

**Datum ulaza:** N/A — nije ušlo u portfolio, samo watchlist
**Cena ulaza:** N/A
**VUAA cena istog dana:** N/A
**Veličina pozicije:** N/A

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu) — primenjuju se AKO
watchlist trigger aktivira ulazak:**
1. Neto dug/EBITDA pređe 3,0x dva kvartala zaredom.
2. Test produktivnosti duga ostane negativan I dug nastavi da raste brže od
   EBIT-a/FCF-a.
3. Kina prihod nastavi da opada preko 15% god/god dva kvartala zaredom bez
   kompenzacije rastom drugde.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| OTIS FY2021-FY2025 finansijski podaci (FY2023-2025) | 10-K FY2025, R3/R5/R9/R17.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/1781335/000178133526000011/ | podnet 05.02.2026 |
| OTIS FY2021-FY2022 finansijski podaci | 10-K FY2022 (acc. 0001781335-23-000009) i 10-K FY2023 (acc. 0001781335-24-000013), krizno provereno | sec.gov/Archives/edgar/data/1781335/ | 03.02.2023 / 02.02.2024 |
| OTIS poslovni opis, segment split, geografija, koncentracija kupaca | Form 10-K FY2025, Item 1/7, Segment note, Geographic External Sales note | sec.gov/Archives/edgar/data/1781335/000178133526000011/otis-20251231.htm | podnet 05.02.2026 |
| OTIS cena zatvaranja (entry/valuation price) | IBKR TWS, sveća 1D | — | 2026-08-13, close 73.03 |
| OTIS WACC (7,19%, bottom-up CAPM) | rf: treasury.gov (zvaničan); beta: stockanalysis.com (treća strana); cost of debt: 10-K R17 | treasury.gov, stockanalysis.com/stocks/otis/statistics | 13-14.08.2026 |
| KONE FY2025 finansijski podaci | KONE Financial Statement Bulletin January-December 2025 | KONE_Financial Statement Bulletin_2025 (kone.com investor relations) | objavljeno 06.02.2026 |
| Schindler FY2025 finansijski podaci | Schindler Annual Results 2025 press release + Consolidated Financial Statements | schindler.com investor relations | objavljeno 11.02.2026 |
| TK Elevator status i M&A finansijski profil | KONE Corporation "Inside information" saopštenje o spajanju sa TKE | news.cision.com/kone-oyj/ | 29.04.2026 |
| KONE/Schindler P/E (orijentaciono) | Agregatori (companiesmarketcap, tradingeconomics, morningstar i sl.) — NE primarni izvor | — | pristupljeno u ovoj sesiji, 2026-08 |
