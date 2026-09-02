# Analiza: Veeva Systems Inc. (VEEV)

**Datum:** 2026-09-02 | **Analitičar:** Dragan | **Cena na dan analize:** 279,23 USD (zaključna cena 2026-09-01, IBKR)
**Status:** Hard kapija G1 (ROIC/spread) PALA.
**U krugu kompetencije:** DA — enterprise SaaS/cloud platforma je direktno u
Draganovom IT/.NET fokusu, iako je vertikala (farma/life sciences) specifična
domenska ekspertiza koju nema.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6). Napomena: kapija G1 je
> pala — po CLAUDE.md §3, ovo formalno isključuje akciju osim ako Dragan napiše
> pisano obrazloženje override-a u §8.

---

## 1. Šta kompanija zapravo radi

Veeva Systems prodaje cloud softver specijalizovan za farmaceutsku/life
sciences industriju, izgrađen na sopstvenoj **Veeva Vault** content/data
platformi. Kompanija **NIJE organizovana u odvojene izveštajne segmente**
(eksplicitno u 10-K: "operates as a single operating and reportable segment")
— "Commercial Solutions" i "R&D and Quality Solutions" su samo **kategorije
prihoda**, ne ASC 280 segmenti:

- **Commercial Solutions** (~45,3% prihoda FY2026, $1.446,9M) — CRM i
  komercijalne aplikacije za farma prodajne timove.
- **R&D and Quality Solutions** (~54,7% prihoda, $1.748,4M, **raste brže**) —
  klinička ispitivanja, regulatorni, kvalitet.

**FY2026 novo:** "Veeva AI" — agentska AI nadogradnja na Vault platformu.

**Konkurencija (Item 1, eksplicitno imenovano):**
- CRM: **Salesforce** (glavni konkurent; IQVIA je licencirala svoj CRM
  Salesforce-u, više nije direktan CRM konkurent)
- Data Cloud/Crossix: IQVIA Holdings, Ipsos Group, Definitive Healthcare
- Development/Quality Cloud: IQVIA, Dassault Systèmes, OpenText, Oracle,
  Honeywell International
- Legacy client-server zamena: Oracle, Microsoft

**Koncentracija kupaca:** Nijedan kupac nije prešao 10% ukupnog prihoda ni u
jednoj godini — niska koncentracija.

**Goodwill:** Statičan $439,9M svih 5 godina — nema novih akvizicija u
periodu (istorijski najveća: Crossix Solutions, FY2020, van posmatranog
perioda). K1 "serijski akvizitori" zamka se ne primenjuje na ovih 5 godina.

**Zaduženost:** Nema finansijskog duga nijedne godine — samo operativni
lizing (nije finansijska poluga). `no_financial_debt=true`.

**Dividende/buyback:** Nikad nije plaćala dividende. Prvi značajniji buyback
tek u FY2026 ($169,9M) — pre toga $0 svih godina.

*Izvor: Form 10-K FY2026 (godina završena 31.01.2026), CIK 0001393052,
accession 0001393052-26-000014, Item 1, Note o segmentima.*

---

## 2. Moat — dve rečenice (obavezna kapija)

*(popunjava Dragan)*

- Kategorija: *(popuni)*
- **Šta bi ubilo ovaj moat u 5 godina:** *(popuni)*
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** *(popuni)*

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/VEEV.json` (kompletan fajl:
`analize/VEEV-scorecard.md`):

```
SCORECARD — Veeva Systems Inc. (VEEV)
Sektor: Softver - life sciences/farma cloud platforma

G1 (ROIC ≥25% softver po docs/05, spread ≥3pp nad WACC): PAO
    — medijana 12,0%, WACC 9,2%, spread SAMO 2,9pp
    (PADA I PO OPŠTEM 12% pragu zbog nedovoljnog spreada, A KAMOLI po
    sektorskom pragu od 25%+ za softver — medijana je manje od polovine
    zahtevanog)
G2 (Neto dug/EBITDA ≤2.0x, pokriv. kamata N/A): PROŠAO — -1,49x (neto gotovina, bez duga)
G3 (FCF pozitivan ≥4/5 god.): PROŠAO — 5/5
G4 (FCF konverzija ≥0.7): PROŠAO — 1,61
G5 (Moat u 2 rečenice): čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru): PROŠAO

Prošlo: 5/6 | PALO: 1 (G1)
```

**G1 je pala jasno i nedvosmisleno — za razliku od WST-a (gde je promašaj bio
0,01 na drugoj kapiji), ovde je promašaj strukturan i dvostruk:**
1. Spread nad WACC-om (2,9pp) je ispod opšteg minimuma od 3pp.
2. Medijana ROIC-a (12,0%) je **manje od polovine** sektorskog praga za
   softver (25%+ po `docs/05`).

**ROIC trend je takođe zabrinjavajući:** 23,8% (FY2022) → 15,5% → **9,7%
(FY2024, dno)** → 11,4% → 12,0% (FY2026) — opadao je 3 godine zaredom, sada se
blago oporavlja ali je i dalje daleko ispod nivoa sa početka perioda.
**Uzrok pada ROIC-a nije pad profitabilnosti** (operativna marža je zapravo
RASLA od FY2024 dna: 18,2%→25,2%→28,7%) — uzrok je da je **investirani
kapital rastao brže od NOPAT-a** (equity je porastao sa $2,9 mlrd na $7,2
mlrd, uglavnom akumulacijom gotovine/investicija koje kompanija ne vraća
akcionarima, pošto ne plaća dividende i tek je nedavno počela sa buyback-om).

**Ovo je važan metodološki nalaz:** Veeva-in ROIC pad NIJE signal slabljenja
posla — poslovanje se ubrzava (marža raste, prihod CAGR 14,6%). Pad ROIC-a je
**mehanički efekat gomilanja neupotrebljene gotovine/investicija na bilansu**
(kompanija generiše više cash-a nego što investira ili vraća akcionarima).
Ovo je suprotno od tipičnog "ROIC pada jer moat erodira" upozorenja iz
CLAUDE.md K1 — ovde formula kažnjava kompaniju za konzervativnu alokaciju
kapitala, ne za lošije poslovanje. **Ipak, formalno, kapija je pala i
zahteva override obrazloženje da bi se nastavilo dalje.**

**Dodatno upozorenje (automatski flag skripte):** SBC/Prihod (14,8% zadnje
godine) je **materijalna dilucija** — tipično za softversku firmu, ali vredno
pažnje u §5 valuaciji.

---

## 4. Poređenje sa konkurencijom

**NIJE SPROVEDENO u ovoj analizi.** Salesforce (CRM) je javno listirana i
mogla bi se porediti u budućem prolazu, ali IQVIA (glavni konkurent u
Development/Quality Cloud i Data Cloud) ima drugačiji poslovni model (CRO +
podaci, ne čist softver) što otežava direktno K2 poređenje. **Otvoreno
pitanje — K2 poređenje sa 3-5 konkurenata (CLAUDE.md obavezno pravilo) nije
zadovoljeno u ovoj verziji analize.**

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **2,58** (P/E 51,33 / EPS CAGR 19,9%) — iznad praga 2,0 | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **3,1%** (nakon SBC: **2,0%** — razlika je materijalna) | ništa — samo tekući cash flow |
| FCF marža | 43,4% | — |

**FCF yield nakon SBC (2,0%) je bitno niži od FCF yield-a pre SBC (3,1%)** —
razlika od 1,1pp direktno odražava SBC/prihod od 14,8%. CLAUDE.md K4 pravilo:
"kompanija koja se hvali 'record FCF' a izdaje 10%+ prihoda u akcijama ne
stvara toliko vrednosti koliko izgleda" — primenjivo ovde. **Koristi FCF
yield nakon SBC (2,0%) kao konzervativniju, realniju meru.**

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 14,6% |
| EPS | 19,9% |
| FCF po akciji | 15,8% |

**EPS raste brže (19,9%) i od prihoda (14,6%) i od FCF/akcije (15,8%)** — ali
razlog NIJE buyback (broj akcija je gotovo stabilan, CAGR +0,7% — kompanija je
neto EMITOVALA akcije kroz većinu perioda, buyback je tek počeo FY2026).
Razlika dolazi od **operativne poluge** (marža raste sa skalom) i **opadajuće
efektivne poreske stope** u ranijim godinama (16,6%→4,2%→10,6%→22,3%→23,9% —
FY2023 je imala neuobičajeno nisku stopu od 4,2%, verovatno jednokratna
poreska korist, što je delimično naduvalo taj deo EPS rasta). **Ovo je
zdraviji obrazac od buyback-inženjeringa, ali FY2023 poreska anomalija
zaslužuje napomenu — deo istorijskog EPS CAGR-a nije ponovljiv.**

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

- [ ] Ulazi u paper portfolio (zahteva PISANO OBRAZLOŽENJE OVERRIDE-a za G1 — vidi CLAUDE.md §3)
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
| VEEV FY2024-FY2026 finansijski podaci | 10-K FY2026, R3/R5/R8.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/1393052/000139305226000014/ | podnet 20.03.2026 |
| VEEV FY2022-FY2023 finansijski podaci | 10-K FY2024 (accession 0001393052-24-000013), R5.htm lično verifikovano | sec.gov/Archives/edgar/data/1393052/000139305224000013/ | podnet 25.03.2024 |
| VEEV poslovni opis, segmenti/kategorije prihoda, konkurencija | Form 10-K FY2026, Item 1, Note o segmentima | sec.gov/Archives/edgar/data/1393052/000139305226000014/ | podnet 20.03.2026 |
| VEEV cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-09-01, close 279.23 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-09-01, close 147.92 (napomena: 31.08.2026 UK Bank Holiday - LSE zatvorena, datum unosa pomeren na 1.09 da se uskladi sa VEEV cenom) |
| VEEV WACC (9,16%, bottom-up) | rf: treasury.gov (4,79%, 10Y UST, 01.09.2026); beta: stockanalysis.com (0,97, treća strana) | treasury.gov, stockanalysis.com/stocks/veev/statistics | 01-02.09.2026 |
