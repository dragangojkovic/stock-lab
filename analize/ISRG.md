# Analiza: Intuitive Surgical, Inc. (ISRG)

**Datum:** 2026-09-02 | **Analitičar:** Dragan | **Cena na dan analize:** 369,25 USD (zaključna cena 2026-09-01, IBKR)
**U krugu kompetencije:** NE — hirurška robotika/medicinski aparati nisu u
Draganovom IT/.NET fokusu.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Intuitive Surgical razvija, proizvodi i prodaje **da Vinci hirurške sisteme**
i **Ion endoluminalni sistem** (fleksibilna, robotski-asistirana
kateter-bazirana platforma za minimalno invazivne biopsije pluća). Poslovni
model je klasičan **razor/blade**: sistemi se prodaju ili lizinguju
(jednokratno), a instrumenti/pribor i usluge (5-godišnji servisni ugovori)
generišu ponavljajući prihod.

**Razor/blade dokazi (5-godišnji trend):**

| Metrika | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| da Vinci installed base | 6.730 | 7.544 (+12%) | 8.606 (+14%) | 9.902 (+15%) | 11.106 (+12%) |
| Ion installed base | 129 | 321 | 534 | 805 | 995 |
| da Vinci procedure/god | ~1,59M | ~1,88M (+18%) | ~2,29M (+22%) | ~2,68M (+17%) | ~3,15M (+18%) |
| **Recurring revenue / ukupan prihod** | **75%** | **79%** | **83%** | **84%** | **84%** |

**Recurring udeo raste kontinuirano svih 5 godina** — instalirana baza
generiše sve veći deo prihoda kroz potrošni materijal/usluge, ne kroz
jednokratnu prodaju sistema. FY2025: da Vinci 5 (nova generacija) installed
base 1.231 jedinica (870 novih plasmana u 2025 vs 362 u 2024 — ubrzanje
lansiranja), da Vinci SP installed base 377 jedinica.

**Konkurencija (Item 1, eksplicitno imenovano):** Beijing Surgerii Robotics,
CMR Surgical, Distalmotion, Harbin Sizhe Rui, **Johnson & Johnson**, Karl
Storz, Medicaroid, **Medtronic plc**, meerecompany, Noah Medical, Shandong
Weigao, Shanghai Microport Medbot, Shenzhen Edge Medical, SS Innovations.
**Napomena:** konkretni konkurentski proizvodi (Medtronic "Hugo", J&J
"Ottava"/Verb Surgical) se ne pominju imenom — samo matične kompanije.
**Stryker/Mako se uopšte ne pominje** u celom dokumentu.

**Pravni rizik relevantan za moat tezu:** SIS antitrust tužba (Surgical
Instrument Service Co., 2021) — tvrdnje o antikonkurentskom ponašanju vezano
za servis/održavanje EndoWrist instrumenata. Sud je presudio **u korist
Intuitive-a** po svim antitrust tačkama (28.1.2025), SIS se žalio (jul
2025), usmena rasprava očekivana april/maj 2026 — **ishod još neizvestan.**
Ovo je direktno relevantno za moat: da li kontrola servisa instrumenata jeste
legitiman deo poslovnog modela ili antikonkurentska praksa je otvoreno
pravno pitanje.

**Goodwill:** Mali i stabilan ($343,6M→$370,3M) — nema značajnih akvizicija,
K1 "serijski akvizitori" zamka se ne primenjuje.

**Dividende/buyback:** Nikad nije plaćala dividende. Buyback veoma
varijabilan/oportunistički: $0(2021)/$2.607,4M(2022)/$416,3M(2023)/
$0(2024)/$2.295,3M(2025).

*Izvor: Form 10-K FY2025, CIK 0001035267, accession 0001035267-26-000010,
Item 1, Note 8 (Commitments and Contingencies).*

---

## 2. Moat — dve rečenice (obavezna kapija)

*(popunjava Dragan)*

- Kategorija: *(popuni)*
- **Šta bi ubilo ovaj moat u 5 godina:** *(popuni)*
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** *(popuni)*

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/ISRG.json` (kompletan fajl:
`analize/ISRG-scorecard.md`):

```
SCORECARD — Intuitive Surgical, Inc. (ISRG)
Sektor: Zdravstvo - medicinski aparati/hirurska robotika

G1 (ROIC ≥20% medicinski aparati po docs/05, spread ≥3pp nad WACC): PADA PO SEKTORSKOM PRAGU
    — medijana 15,5% je ISPOD 20% praga (iako PROLAZI opšti 12% minimum sa
    spreadom 4,2pp nad WACC-om 11,4%)
G2 (Neto dug/EBITDA ≤2.5x, bez duga): PROŠAO — -0,93x (neto gotovina, bez duga)
G3 (FCF pozitivan ≥4/5 god.): PROŠAO — 5/5
G4 (FCF konverzija ≥0.7): PROŠAO (na granici) — 0,72
G5 (Moat u 2 rečenice): čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru): PROŠAO

Prošlo: 5/6 (po sektorskom pragu) | Formalno (opšti prag): 6/6
```

**Isti obrazac kao AME — dva čitanja:**
1. **Sirovi scorecard (opšti prag):** G1 prolazi (15,5% medijana, spread
   4,2pp).
2. **Sektorski prag (`docs/05`, 20%+ za medicinske aparate):** G1 **pada**.

**G4 je na granici (0,72 vs prag 0,70) iz istog razloga kao WST — CapEx
ciklus.** FCF konverzija po godini: 1,02/0,72/**0,42**/0,56/0,87
(FY2021-2025). FY2023-2024 su bile godine najvećeg CapEx-a ($1.064M/$1.111M
— verovatno izgradnja proizvodnog kapaciteta za da Vinci 5 lansiranje) —
FY2025 CapEx je pao na $540M i FCF konverzija se oporavila na 0,87. **Ovo NIJE
signal slabljenja — OCF/NI je bio iznad 1,0 svake godine (1,01-1,23), zarada
nije "na papiru."**

**Automatski flag skripte:** SBC/Prihod (7,8% zadnje godine) je **materijalna
dilucija** — vredno pažnje u §5.

**Kvalitet obrtnog kapitala — upozorenje:** Zalihe rastu (CAGR 33,1%) znatno
brže od prihoda (CAGR 15,2%) — konzistentno sa izgradnjom proizvodnog
kapaciteta za rastuću instaliranu bazu i da Vinci 5 lansiranje, ali vredi
pratiti da li se ovaj jaz smanjuje u narednim kvartalima (CLAUDE.md K4
pravilo o obrtnom kapitalu).

---

## 4. Poređenje sa konkurencijom

**NIJE SPROVEDENO u ovoj analizi.** Intuitive nema direktnog javno-listiranog
čistog konkurenta u robotskoj hirurgiji uporedive veličine (CMR Surgical je
privatna, kineski konkurenti nisu SEC filer-i). Medtronic i J&J su
diversifikovani konglomerati gde je robotska hirurgija mali deo poslovanja —
segment-nivo poređenje bi zahtevalo podatke koje ove kompanije ne
obelodanjuju odvojeno. **Otvoreno pitanje — K2 poređenje sa 3-5 konkurenata
nije zadovoljeno.**

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | N/A (scorecard nije izračunao — EPS CAGR 14,0% ali PEG polje prazno, verovatno zbog P/E izostavljenog u prikazu; P/E 46,92 / 14,0 ≈ **3,35** ručno) | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **1,9%** (nakon SBC: **1,3%** — velika razlika) | ništa — samo tekući cash flow |
| FCF marža | 24,7% | — |

**FCF yield nakon SBC (1,3%) je drastično niži od pre SBC (1,9%)** — najveći
proporcionalni pad od svih pozicija analiziranih u projektu, odražava
SBC/prihod od 7,8%. **P/E od 46,92 i implicitan PEG ~3,35 čine ovo skupom
akcijom** po klasičnim merilima, uprkos snažnom razor/blade rastu.

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 15,2% |
| EPS | 14,0% |
| FCF po akciji | 9,7% |

**EPS CAGR (14,0%) je blizu prihoda (15,2%), oba veća od FCF/akcije (9,7%)**
— razlika dolazi delom od CapEx ciklusa koji je pritiskao FCF u FY2023-2024
(objašnjeno gore), ne od agresivnog finansijskog inženjeringa. Broj akcija je
praktično stabilan (CAGR -0,2%).

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
| ISRG FY2023-FY2025 finansijski podaci | 10-K FY2025, R4/R6/R8/R9/R10.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/1035267/000103526726000010/ | podnet 03.02.2026 |
| ISRG FY2021-FY2022 finansijski podaci | XBRL companyfacts, unakrsno provereno protiv originalnih 10-K | data.sec.gov/api/xbrl/companyfacts/CIK0001035267.json | pristupljeno 02.09.2026 |
| ISRG poslovni opis, installed base/procedure, konkurencija, pravni sporovi | Form 10-K FY2025, Item 1, Note 8 | sec.gov/Archives/edgar/data/1035267/000103526726000010/ | podnet 03.02.2026 |
| ISRG cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-09-01, close 369.25 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-09-01, close 147.92 |
| ISRG WACC (11,36%, bottom-up) | rf: treasury.gov (4,79%, 10Y UST, 01.09.2026); beta: stockanalysis.com (1,46, treća strana) | treasury.gov, stockanalysis.com/stocks/isrg/statistics | 01-02.09.2026 |
