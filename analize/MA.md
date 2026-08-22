# Analiza: Mastercard Incorporated (MA)

**Datum:** 2026-08-22 | **Analitičar:** Dragan | **Cena na dan analize:** 573,85 USD (zaključna cena 2026-08-20, IBKR)
**U krugu kompetencije:** DELIMIČNO — platni sistemi imaju tehnološku/softversku
komponentu (Draganov krug), ali regulatorna/finansijska infrastruktura globalnih
plaćanja nije direktno u njegovom IT/.NET fokusu.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Mastercard je **"four-party" mrežna kompanija** (account holder — issuer banka —
merchant — acquirer banka). Direktan citat iz 10-K: MA "ne izdaje kartice, ne
odobrava kredit, ne određuje i ne prima prihod od kamatnih stopa ili drugih naknada
koje issueri naplaćuju account holder-ima, niti određuje stope koje acquireri
naplaćuju merchant-ima." Zarada dolazi od obima transakcija (switching/
authorization/clearing/settlement) — **NIJE banka, ne nosi kreditni rizik prema
krajnjim korisnicima** (potvrđuje `docs/05` §3 tezu).

**Obim FY2025:** GDV (Gross Dollar Volume) $10,6 triliona (rast na lokalnoj valuti),
switched transactions 175,5 milijardi (+10% god/god), cross-border volume +9%.

**Geografija:** ~29% prihoda iz SAD (71% international) — nijedna druga pojedinačna
zemlja >10%. ~39.800 zaposlenih, ~70% van SAD, preko 90 zemalja.

**Konkurencija — imenovana eksplicitno (Item 1, "Competition"), bogata i
segmentirana:**
- General Purpose Payments Networks: **Visa, American Express, JCB, China
  UnionPay, Discover**
- Real-time Account-based Payment Systems (ACH/RTP): PIX (Brazil), FedNow (SAD),
  UPI (Indija)
- Digital Wallets/Fintech, Digital Currencies (stablecoin/kripto — GENIUS Act 2025)
- Digital Public Infrastructure/Government-Backed Solutions

**Regulatorni rizici — materijalni i aktivni (Item 1A):**
- **DOJ antitrust istraga** (Civil Investigative Demand, 2023) — fokus na US debit
  program, Sherman Act §1/§2, ishod nepoznat
- **US MDL interchange litigacija:** akumulirana obaveza $637M (31.12.2025, raslo
  sa $559M godinu ranije)
- **UK/EU/Australija interchange litigacija:** više aktivnih grupa tužbi (UK
  collective action >£1mlrd, Portugal ~€0,4mlrd, Holandija — MA i Visa zajedno,
  jul 2025, >€0,3mlrd)
- Ovo je **materijalan, ponavljajući trošak** (litigation provision je stalna linija
  u operativnim troškovima, $504M-$680M/god kroz 5 godina) — ne jednokratna stavka.

**Dividende/buyback — redak slučaj u ovom projektu:** MA plaća **i dividende i
radi buyback** (za razliku od CPRT/IDXX/MEDP/ORLY/OTIS koji su isključivo
buyback-only). Dividende rastu (1.741→2.756 FY2021-2025), buyback agresivan i
rastuć (5.904→11.727) — ali equity **ostaje pozitivan** (nije destruktivan kao kod
OTIS/ORLY) jer je profitabilnost dovoljno visoka da nadmaši otkup.

*Izvor: Form 10-K FY2025 (godina završena 31.12.2025), CIK 0001141391, accession
0001141391-26-000013, Item 1, Item 1A, Note (Revenue).*

---

## 2. Moat — dve rečenice (obavezna kapija)

*(popunjava Dragan)*

- Kategorija: *(popuni)*
- **Šta bi ubilo ovaj moat u 5 godina:** *(popuni)*
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** *(popuni)*

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/MA.json` (kompletan fajl:
`analize/MA-scorecard.md`):

```
SCORECARD — Mastercard Incorporated (MA)
Sektor: Infrastruktura tržišta - platni sistemi | Valuta: USD (miliони) | Podaci: 5 god.

HARD KAPIJE
G1 (ROIC ≥30% za platne sisteme prema docs/05, spread ≥3pp nad WACC): PROŠAO — medijana 80,8%, WACC 7,8%, spread 73,0pp
G2 (Neto dug/EBITDA ≤2.0x platni sistemi, pokriv. kamata ≥4x): PROŠAO — ND/EBITDA 0,42x, kamate 26,2x
G3 (FCF pozitivan ≥4/5 god.):                  PROŠAO — 5/5
G4 (FCF konverzija 5g prosek ≥0.7):            PROŠAO — 1,03
G5 (Moat u 2 rečenice):                        PROŠAO (formalno, čeka Draganovu formulaciju — vidi §2)
G6 (Nije u isključenom sektoru):                PROŠAO — platni sistemi NISU banka (docs/05 §3)

Prošlo: 6/6 | Palo: 0 — TREĆA KOMPANIJA (posle CPRT, IDXX) KOJA PROLAZI ČISTO, SA NAJEKSTREMNIJIM BROJEVIMA

K2 (marže): Bruto N/A (nema COGS liniju, mrežni posao) | Operativna 57,6% (stabilna, RASTE ka kraju) | Neto 45,6%
K3 (zaduženost): ND/EBITDA 0,42x | pokrivenost kamata 26,2x | test produktivnosti duga: DUG JE BIO PRODUKTIVAN (redak signal)
K4 (FCF): FCF konverzija prosek 1,03 | SBC/prihod 1,8% (zanemarljivo)
K5 (valuacija @ 573,85): P/E 34,74 | PEG_trailing 2,02 (na granici praga) | FCF yield na EV 3,1%
```

**Kapije:** prošlo 6/6 | palo 0. **G1 nije K1-ALT/ALT2 artefakt** — equity je pozitivan
(~$7-8 mlrd) i investirani kapital nije blizu nule; ROIC je genuinski ekstremno
visok jer je posao stvarno toliko profitabilan na skromnom kapitalu. Ovo je
tačno `docs/05` §4 predviđanje: **"ROIC je toliko visok da prag ne razlikuje
ništa. Prelazi na FCF maržu."**
**Override (ako je kapija pala):** nema pale kapije.

---

## 4. Poređenje sa konkurencijom

**Visa Inc. (V) — direktan duopol par, najbolje moguće poređenje u ovom
projektu.** Za razliku od skoro svih prethodnih kompanija (gde je čist konkurent
bio integrisan/privatizovan/nedostupan), Visa je **savršeno uporediva** — isti
poslovni model, slična veličina, oba javno listirana.

| Metrika | MA (FY2025) | Visa (V, FY2025 — fiskalna do 30.09.2025) |
|---|---|---|
| Prihod | $32.791M | $40.000M |
| Operativna marža (GAAP) | 57,6% | **~60,0%** (blago viša) |
| Neto marža | 45,6% | 50,1% |
| Neto dug/EBITDA | 0,42x | **~0,32x** (još niži leverage) |
| Pokrivenost kamata | 26,2x | **~40,7x** |
| FCF konverzija (FCF/NI) | 1,03 | ~1,08 |
| Dividende + buyback (FY2025) | $2.756M + $11.727M = $14.483M | $4.634M + $18.316M = **$22.950M** (veći apsolutno, Visa je i veća kompanija) |

*Izvor: Visa Inc. 10-K FY2025 (godina završena 30.09.2025), CIK 0001403161,
accession 0001403161-25-000089, Consolidated Statements of Operations/Balance
Sheets/Cash Flows.*

**Ključni nalaz — Visa je marginalno bolja po skoro svakoj metrici, ali razlika je
mala.** Ovo je duopol gde su oba igrača izuzetno disciplinovana — nijedan ne
"pobeđuje" drastično, razlike su u desetinkama procentnih poena, ne u redovima
veličine kao kod ORLY vs AAP ili IDXX vs Zoetis. **Ovo je najčistiji "kontrolni
duopol" test slučaj u projektu** — potvrđuje da mrežni efekat + regulatorna
barijera (potreba za dozvolama u svakoj jurisdikciji) stvara prostor za DVA
igrača koji oba profitiraju izuzetno, ne nužno "pobednika koji uzima sve".

**Napomena o GDV poređenju — otvoreno pitanje.** Visa 10-K (citirajući Nilson
Report, kalendarska 2024) navodi Payments Volume $13.433 mlrd (Visa) vs $8.014
mlrd (MA) — ovo se **ne poklapa direktno** sa MA-inim sopstvenim GDV brojem od
$10,6 triliona (FY2025) korišćenim u §1. Razlika je verovatno u periodu (CY2024
Nilson vs FY2025 MA sopstveni izveštaj) i/ili definiciji (Payments Volume vs GDV,
Total Transactions vs Switched Transactions). **N/A — treba uskladiti identične
baze pre preciznog broja tržišnog učešća**, ali oba izvora se slažu da je Visa
veća po volumenu.

**MA ima aktivniju antitrust/regulatornu izloženost trenutno** (DOJ CID 2023 fokus
na US debit program) — vredno praćenja, ali nije jedinstveno za MA (Visa deli
sličnu regulatornu izloženost u UK/EU/Holandiji, uklj. zajedničku tužbu sa MA u
Holandiji jul 2025).

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **2,02** (P/E 34,74 / EPS CAGR 17,2%) — na granici praga 2,0 | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **3,1%** (nakon SBC: 3,0%) | ništa — samo tekući cash flow |
| **FCF marža** | **50,1%** ← primarni K1-ALT-stil signal za ovaj sektor | zamenska metrika kad ROIC ne razlikuje ništa |

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 14,8% |
| EPS | 17,2% |
| **FCF po akciji** | **20,1%** |

**Zdrav obrazac — isti kao CPRT/IDXX/MEDP.** FCF po akciji raste brže i od EPS-a i
od prihoda; broj akcija opada blago (CAGR -2,2%, umeren buyback iz realno
generisane gotovine). **Rast nije finansijski inženjering — poslovanje genuinski
raste brže od otkupa.**

**PEG na granici praga (2,02) uz FCF maržu od 50,1% i FCF yield 3,1%** — ovo nije
"jeftino" u apsolutnom smislu, ali je **znatno umerenije nego IDXX** (PEG 3,81, FCF
yield 2,3%) uz sličan nivo fundamentalnog kvaliteta. Tržište plaća premiju za MA,
ali manju nego za IDXX.

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
| MA FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R8.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/1141391/000114139126000013/ | podnet 11.02.2026 |
| MA FY2021-FY2022 finansijski podaci + capex detalji FY2021-2023 | 10-K FY2023 (accession 0001141391-24-000022), R8.htm lično verifikovano; ostalo preko XBRL companyfacts API | sec.gov/Archives/edgar/data/1141391/ | 2022 / 13.02.2024 |
| MA poslovni opis, konkurencija, regulatorni rizici, geografija | Form 10-K FY2025, Item 1, Item 1A, Note (Revenue) | sec.gov/Archives/edgar/data/1141391/000114139126000013/ma-20251231.htm | podnet 11.02.2026 |
| MA cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-20, close 573.85 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-20, close 148.54 |
| MA WACC (7,81%, bottom-up) | rf: treasury.gov; beta: stockanalysis.com (treća strana) | treasury.gov, stockanalysis.com/stocks/ma/statistics | 20-21.08.2026 |
| Visa (V) FY2025 finansijski podaci | 10-K FY2025 (godina do 30.09.2025), Item 7/8 | sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm | podnet 06.11.2025 |
| Visa GDV/volumen poređenje (Nilson Report CY2024, citirano u Visa 10-K) | Visa 10-K FY2025, Item 1 Competition tabela | isti dokument | Nilson Report issue 1288, jun 2025 |
