# Analiza: Moody's Corporation (MCO)

**Datum:** 2026-08-31 | **Analitičar:** Dragan | **Cena na dan analize:** 514,95 USD (zaključna cena 2026-08-28, IBKR)
**U krugu kompetencije:** NE — kreditni rejting/finansijska analitika nije u
Draganovom IT/.NET fokusu, iako Moody's Analytics segment ima softversku
komponentu.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Moody's posluje kroz **dva operativna segmenta**: **MIS** (Moody's Investors
Service — kreditni rejting, pet linija biznisa: CFG, FIG, PPIF, SFG, MIS Other)
i **MA** (Moody's Analytics — Decision Solutions, Research & Insights, Data &
Information). MIS je bio **~53-54% ukupnog prihoda** FY2024-2025 ($4.119M od
$7.718M FY2025).

MIS zarađuje naknade koje izdavaoci duga plaćaju za kreditni rejting — prihod
je **ciklčan**, zavisi od volumena i broja emisija duga na globalnim
tržištima, delimično ublažen godišnjim ugovorima sa čestim izdavaocima.
Registrovan kao **NRSRO** kod SEC-a (Section 15E Exchange Act), takođe
regulisan u EU/UK (ESMA/FCA), i podložan DORA (EU operativna otpornost).

**Konkurencija:** 10-K NE imenuje direktno Fitch/DBRS/Kroll u Item 1 tekstu —
govori generičkim terminima "other CRAs" (credit rating agencies) za MIS, i
"providers of software/analytic solutions" za MA segment.

**Goodwill/akvizicije:** Goodwill stabilan (~$6,0-6,4 mlrd), **bez
mega-akvizicije** u periodu — manja akvizicija ICR Chile (Moody's Local,
Latinska Amerika) nije materijalna. K1 "serijski akvizitori" zamka **NIJE
relevantna** za MCO — za razliku od direktnog konkurenta S&P Global (SPGI),
koji je istovremeno analiziran u ovom projektu i **odbijen zbog G1 pada**
uzrokovanog goodwill-om iz IHS Markit akvizicije (vidi `analize/SPGI.md`).

**Dividende/buyback:** MCO plaća i dividende i radi buyback. Dividende
(rastuće): $463M→$701M (FY2021-2025). Buyback ("Treasury shares"):
$750M→$1.607M — agresivan, posebno rastuć poslednje 2 godine.

*Izvor: Form 10-K FY2025, CIK 0001059556, accession 0001628280-26-009136,
Item 1, Item 1A.*

---

## 2. Moat — dve rečenice (obavezna kapija)

Regulatorna barijera (NRSRO status, reputacija izgrađena kroz vek postojanja)
+ duopol sa S&P Global (Fitch kao manji treći igrač). MCO je jedva prošao
ROIC kapiju na granici sektorskog praga (25,5% vs 25%) dok je direktan
duopol par (SPGI) **pao** na istoj kapiji zbog goodwill-a od IHS Markit
akvizicije — pokazuje da reputacija/moat sama po sebi ne garantuje kapitalnu
efikasnost kad se kapital pogrešno alocira kroz M&A.

- Kategorija: regulatorna/licencna barijera (NRSRO) + duopol/oligopol
- **Šta bi ubilo ovaj moat u 5 godina:** AI-vođeni alati za procenu kreditnog
  rizika postanu "dovoljno dobri" da izdavaoci duga ili investitori zaobiđu
  tradicionalni NRSRO rejting, ili regulatorna reforma ukine oslanjanje na
  NRSRO rejtinge za institucionalne investicione mandate.
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:**
  reputacija/track record izgrađen kroz vek postojanja + NRSRO registracija
  ugrađena u institucionalne/regulatorne mandate — čak ni dobro finansirani
  fintech izazivači nisu razbili duopol decenijama.

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/MCO.json` (kompletan fajl:
`analize/MCO-scorecard.md`):

```
SCORECARD — Moody's Corporation (MCO)
Sektor: Rejting/podaci - infrastruktura tržišta

G1 (ROIC ≥25% rejting/podaci sektor, spread ≥3pp nad WACC): PROŠAO (na granici)
    — medijana 25,5%, WACC 10,1%, spread 15,4pp
G2 (Neto dug/EBITDA ≤3.0x, pokriv. kamata ≥4x):             PROŠAO — 1,20x / 15,7x
G3 (FCF pozitivan ≥4/5 god.):                                PROŠAO — 5/5
G4 (FCF konverzija ≥0.7):                                    PROŠAO — 1,03
G5 (Moat u 2 rečenice):                                      čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru):                              PROŠAO

Prošlo: 6/6 | Palo: 0
```

**Kapija G1 prolazi, ali NA GRANICI sektorskog praga** (25,5% naspram 25%
praga za rejting agencije iz `docs/05`) — za razliku od MA/Visa (ROIC 40-80%,
signal saturiran) i za razliku od SPGI (koji pada ispod čak i opšteg 12%
minimuma). MCO je **jedini od četiri infrastrukturne kompanije u ovoj seriji
(MA, V, MCO, SPGI) gde je ROIC prag zaista granica, ne formalnost.**

ROIC trend RASTE (27,4% FY2021 → 18,1% FY2022 pad → 30,4% FY2025) — pad u
FY2022 se poklapa sa opštim padom operativne marže te godine (34,4% vs 45,7%
FY2021), verovatno vezano za pad obima izdavanja obveznica u ciklusu rasta
kamatnih stopa 2022. Ovo je **ciklična osetljivost karakteristična za MIS
segment**, ne strukturni problem.

---

## 4. Poređenje sa konkurencijom

**S&P Global (SPGI) — direktan duopol/oligopol par, ODBIJEN u ovoj istoj
analitičkoj seriji zbog pada G1 (vidi `analize/SPGI.md`).**

| Metrika | Moody's (FY2025) | S&P Global (FY2025) |
|---|---|---|
| Prihod | $7.718M | $15.336M (skoro 2x veći, posle IHS Markit) |
| Ratings/MIS segment % prihoda | ~53% | ~30% (razblaženo IHS Markit akvizicijom) |
| Operativna marža | 43,4% | 42,2% |
| Neto marža | 31,9% | 29,2% |
| ROIC medijana (5g) | **25,5% (PROŠAO)** | **8,0% (PAO — goodwill efekat)** |
| Neto dug/EBITDA | 1,20x | 1,48x |
| Pokrivenost kamata | 15,7x | 22,6x |
| FCF konverzija | 1,03 | 1,20 |
| Goodwill (FY2025) | $6.368M | $36.475M |

**Ključni nalaz — MCO je "čistiji" test slučaj metodologije.** SPGI je skoro 2x
veći po prihodu (nakon IHS Markit akvizicije 2022) i ima blago bolju FCF
konverziju/pokrivenost kamata, ali njegov ROIC je uništen naduvanim
investiranim kapitalom iz akvizicije — MCO je zadržao organski profil rasta i
prošao kapiju bez potrebe za bilo kakvom ALT/ex-goodwill korekcijom. **Ovo je
direktna ilustracija CLAUDE.md K1 upozorenja: "akvizicije su realno potrošen
kapital akcionara"** — SPGI-jeva veličina posle akvizicije ne prevodi se
automatski u bolji ROIC.

*Izvor: S&P Global Inc. 10-K FY2025, CIK 0000064040 (vidi `analize/SPGI.md`
za pun izvor).*

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **9,94** (P/E 37,67 / EPS CAGR 3,8%) — DRASTIČNO iznad praga 2,0 | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **2,6%** (nakon SBC: 2,4%) | ništa — samo tekući cash flow |
| FCF marža | 33,4% | — |

**PEG_trailing od 9,94 je alarmantno visok** — po CLAUDE.md K5 pravilu ovo
zahteva eksplicitno obrazloženje. Uzrok: istorijski EPS CAGR (5g, 3,8%) je
nizak zbog FY2022 pada zarade (litigation/ciklus obveznica), pa 4-godišnji
trailing prozor potcenjuje trenutni momentum (FY2024→FY2025 EPS je skočio sa
$11,26 na $13,67, +21% god/god). **PEG_trailing je ovde verovatno loš
pokazatelj upravo iz razloga koje CLAUDE.md K5 navodi eksplicitno** — "ciklične
kompanije na vrhu ili dnu ciklusa (E je nereprezentativan)". Preporuka: gledaj
FCF yield i PEG_forward (kada bude dostupan) umesto trailing PEG-a za MCO.

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 5,6% |
| EPS | 3,8% |
| FCF po akciji | 9,6% |

**Zdrav obrazac.** FCF po akciji raste brže (9,6%) i od prihoda (5,6%) i od
EPS-a (3,8%) — rast nije buyback-inženjering, EPS CAGR je zapravo NIŽI od
prihoda zbog FY2022 ciklusnog pada, ne zbog dilucije ili slabljenja
operativnog posla.

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. Globalni obim izdavanja obveznica padne >15% god/god dva kvartala zaredom
   (ciklični kolaps prihoda, pogađa MIS segment).
2. Operativna marža padne ispod 38% dva kvartala zaredom (litigacija/troškovi
   rastu brže od prihoda).
3. Neto dug/EBITDA pređe 2,0x dva kvartala zaredom (poluga se približava
   sektorskom plafonu od 3,0x).

**Šta je najjači argument protiv kupovine ove akcije?** MCO-ov prolazak ROIC
kapije (25,5%) je TAČNO na sektorskom pragu — jedna slabija ciklična godina
bi mogla gurnuti 5-godišnju medijanu ispod 25%, za razliku od MA/V gde je
margina sigurnosti ogromna. Uz PEG_trailing od 9,94 (čak i ako je delom
artefakt cikličnog dna) i sektorski cap već popunjen sa MA, ovo je najslabiji
prolazak kapije od sve četiri infrastrukturne kompanije analizirane u ovoj
seriji — razumno je sačekati pun kreditni ciklus da se proceni "pravi" ROIC
nivo.

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | Operativna marža ostaje visoka | ≥ 40% | 70% |
| 2 | ROIC (godišnji) ostaje iznad sektorskog praga | ≥ 25% | 70% |
| 3 | Zaduženost ostaje umerena | Neto dug/EBITDA ≤ 1,5x | 70% |
| 4 | FCF konverzija ostaje solidna | ≥ 0,9 | 70% |
| 5 | MIS segment prihod ne padne naglo | pad ≤ 10% god/god | 70% |

---

## 8. Odluka (popunjava Dragan)

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam da ROIC održi ≥28% kroz pun ciklus ILI se sektorski
      cap oslobodi (MA teza pukne) ILI PEG_forward postane dostupan i pokaže
      razumnu vrednost
- [ ] Odbijeno — razlog: {…}

**Razlog:** Granični prolazak kapije (ROIC 25,5% baš na sektorskom pragu od
25%, najslabija margina sigurnosti od sve četiri infrastrukturne kompanije u
seriji) + PEG_trailing alarmantno visok (9,94, delom ciklični artefakt) +
sektorski cap već popunjen sa MA (`docs/05` §6 grupiše MA/V/MCO pod istim
limitom od 1 pozicije). Watchlist do punog kreditnog ciklusa ili oslobađanja
sektorskog capa.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| MCO FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R7.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/1059556/000162828026009136/ | podnet 18.02.2026 |
| MCO FY2021-FY2022 finansijski podaci | 10-K FY2023 (accession 0001059556-24-000017), R3.htm lično verifikovano | sec.gov/Archives/edgar/data/1059556/000105955624000017/ | podnet 14.02.2024 |
| MCO CIK korekcija | sec.gov/cgi-bin/browse-edgar (istraživački agent je pogrešno naveo CIK GAP Inc. — ispravan CIK 0001059556 lično potvrđen) | sec.gov | 31.08.2026 |
| MCO cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-28, close 514.95 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-28, close 150.12 |
| MCO WACC (10,13%, bottom-up) | rf: treasury.gov (4,73%, 10Y UST, 28.08.2026); beta: stockanalysis.com (1,33, treća strana) | treasury.gov, stockanalysis.com/stocks/mco/statistics | 28-31.08.2026 |
| S&P Global (SPGI) FY2025 podaci za poređenje | vidi `analize/SPGI.md` §9 | — | — |
