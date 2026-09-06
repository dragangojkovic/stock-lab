# Analiza: Illinois Tool Works Inc. (ITW)

**Datum:** 2026-09-06 | **Analitičar:** Dragan | **Cena na dan analize:** 270.12 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — diversifikovana industrijska proizvodnja nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

ITW je diversifikovani industrijski proizvođač organizovan u 7 nepovezanih segmenata: Automotive OEM (plastični/metalni delovi, fasteneri), Food Equipment (warewashing, kuvanje, hlađenje + servis), Test & Measurement/Electronics, Welding (oprema i potrošni materijal za zavarivanje), Polymers & Fluids (lepkovi, zaptivači, maziva), Construction Products (inženjerski fastening sistemi) i Specialty Products (pakovanje pića, oprema za kodiranje, delovi za bele tehnike).

- Izvori prihoda i njihov udeo: prihod je diversifikovan kroz 7 segmenata bez dominantnog jednog (specifičan % po segmentu nije bio predmet ovog istraživanja — N/A, treba proveriti u 10-K segmentnoj napomeni ako je relevantno za odluku).
- Ko su kupci: OEM proizvođači, distributeri, krajnji korisnici u proizvodnji/transportu/gradnji/prehrambenoj industriji — zavisno od segmenta.
- Kako se naplaćuje: prodaja proizvoda i opreme, delom sa ponavljajućim prihodom od potrošnog materijala (npr. welding potrošni materijal, food equipment servis).
- Koncentracija: nema obelodanjivanja koncentracije kupaca u 10-K (provereno Item 1 i Item 1A) — N/A, nije obelodanjeno.

## 2. Moat — dve rečenice (obavezna kapija)

> "80/20 Front-to-Back" operativni model — decentralizovane poslovne jedinice fokusiraju resurse na najprofitabilniji ~20% proizvoda/kupaca i sistematski eliminišu kompleksnost dugog repa manje profitabilnih SKU-ova, generišući strukturno višu operativnu maržu (26.3%) od diversifikovanih konkurenata (Honeywell 21.7%, Dover/Lincoln Electric 17.0%).
> Diversifikacija kroz 7 nepovezanih segmenata (welding do food equipment) smanjuje ciklični rizik pojedinačnog tržišta bez žrtvovanja ROIC-a (29.5% medijana kroz 5 godina).

- Kategorija: ekonomija obima / troškovna prednost (operativni proces, ne proizvod)
- **Šta bi ubilo ovaj moat u 5 godina:** novi menadžment napusti 80/20 disciplinu radi rasta prihoda (kompromitujući maržu) ILI konkurenti kopiraju model
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** 80/20 zahteva decenijsku decentralizovanu korporativnu kulturu, ne samo strategiju — teško se transplantira preko noći

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/ITW.json`:

```
SCORECARD — Illinois Tool Works Inc. (ITW)
Sektor: Industrija - diversifikovani proizvodjac (7 segmenata) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 29.5%, WACC 8.6%, spread 20.9% - PROŠAO
G2 ND/EBITDA≤3.0x i pokrivenost≥4x: 1.76x, 14.4x - PROŠAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 0.84 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 6/6, Palo 0

K1 ROIC: medijana 29.5%, trend stabilan (28.8%→29.5%→30.9%→32.9%→28.7%). WACC 8.6%, spread 20.9%.
K2 Marže: bruto 41.3%→44.1%, operativna 24.1%→26.3% (RASTE), neto 18.6%→19.1% (stabilan).
K3 Zaduženost: ND/EBITDA 1.58x→1.76x, pokrivenost kamata 17.2x→14.4x, D/E 2.12→2.78 (visok zbog
  niskog equity-ja od decenija buyback-a, NE spinoff-a - equity NIJE negativan).
  Test produktivnosti duga: dug CAGR 3.9% vs EBIT CAGR 4.9% vs FCF CAGR 4.6% → dug PRODUKTIVAN.
K4 FCF: pozitivan 5/5, FCF konverzija prosek 0.84, OCF/NI prosek 0.98. SBC/prihod 0.4% (nisko).
  Potraživanja CAGR 3.2% blago iznad prihoda (2.6%); zalihe CAGR -0.5% ispod prihoda - u redu.
K5 Valuacija: P/E 25.75. PEG_trailing 4.80 (istorijski EPS CAGR samo 5.4% - skupo na trailing bazi),
  PEG_forward 3.43 (konsenzus rast 7.5%, blago povoljniji ali i dalje >2.0). FCF yield na EV 3.1%.
```

**Kapije:** prošlo 6/6 | palo 0 | nepoznato 0
**Override (ako je kapija pala):** nema — sve kapije prošle formalno čisto.

## 4. Poređenje sa konkurencijom

| Metrika | ITW | Dover (DOV) | Honeywell (HON) | Lincoln Electric (LECO, Welding niša) | Medijana grane |
|---|---|---|---|---|---|
| ROIC (FY2025) | 28.7% (5g med. 29.5%) | 12.1% | 18.2% | 22.5% | ~20% |
| Bruto marža | 44.1% | 39.8% | 36.9% | 36.2% | ~39% |
| Operativna marža | 26.3% | 17.0% | 21.7% | 17.0% | ~20% |
| Neto marža | 19.1% | 13.5% | 12.6% | 12.3% | ~13% |
| Neto dug/EBITDA | 1.76x | 0.94x | ~2.36x (nepotpuni D&A) | 1.21x | ~1.5x |
| P/E | 25.75 | N/A — treba proveriti | N/A — treba proveriti | N/A — treba proveriti | N/A |
| PEG (trailing) | 4.80 | N/A | N/A | N/A | N/A |
| FCF yield na EV | 3.1% | N/A | N/A | N/A | N/A |

*Izvor DOV/HON/LECO: SEC EDGAR 10-K FY2025 (Dover CIK 0000029905 accn 0000029905-26-000009; Honeywell CIK 0000773840 accn 0000773840-26-000013; Lincoln Electric CIK 0000059527 accn 0000059527-26-000006). ROIC izračunat istom formulom kao za ITW (NOPAT=EBIT×(1-tax), IC=dug+equity-gotovina). Honeywell ND/EBITDA je gornja granica procene — D&A nije potpuno XBRL-tagovano (samo PP&E deo), pa je EBITDA verovatno potcenjena i realan ND/EBITDA je NIŽI. LECO je jedini konkurent imenovan direktno u ITW 10-K (Welding segment) — najbliže poređenje po samom izvoru.*

**Ako marža pada — pada li svima u grani ili samo njoj?** ITW marže NE padaju — operativna marža raste (24.1%→26.3%) i ostaje najviša od sve četiri kompanije u tabeli. ITW ima najbolju operativnu maržu (26.3% vs 21.7% Honeywell, 17.0% Dover/LECO) — konzistentno sa "80/20" tezom da fokus na najprofitabilnije proizvode/kupce generiše strukturno višu maržu od diversifikovanih konkurenata koji ne primenjuju isti model. ROIC je nešto slabija priča relativno — LECO (22.5%) i Honeywell (18.2%) su blizu ITW-a (28.7% FY2025), dok Dover (12.1%) zaostaje značajno — razlika je verovatno u kombinaciji obima kapitala i goodwill-a iz akvizicija (nije istraženo dublje ovde, N/A za tačan uzrok).

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 4.80 | prošli EPS rast (5.4% CAGR) se nastavlja |
| PEG_forward | 3.43 | konsenzus analitičara (7.5% EPS rast) je tačan |
| FCF yield na EV | 3.1% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 3.0% | dilucija je realan trošak (ovde gotovo nebitna, SBC/prihod 0.4%) |

**Razlika između PEG_trailing i PEG_forward:** Umerena — 4.80 vs 3.43. Konsenzus (7.5%) je viši od trailing (5.4%), implicira blago ubrzanje rasta EPS-a naspram istorijskog tempa. Oba PEG-a su iznad CLAUDE.md praga od 2.0 koji zahteva eksplicitno obrazloženje premije — ovde premija dolazi od kvaliteta (najviša operativna marža u peer grupi, dosledan ROIC 28-33%), ne od očekivanog ubrzanja rasta prihoda (prihod CAGR svega 2.6%, sazrelo/sporo rastuće tržište).

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

1. Operativna marža padne ispod 25% dva kvartala zaredom — signal da 80/20 disciplina slabi.
2. Prihod CAGR ostane ispod 3% dok konkurenti rastu brže — signal gubitka tržišnog udela, ne samo zrelog tržišta.
3. Test produktivnosti duga se obrne (dug počne rasti brže od EBIT/FCF) — signal da se buyback finansira agresivnije dugom.

**Šta je najjači argument protiv kupovine ove akcije?** ITW plaća gotovo sav svoj slobodan novčani tok akcionarima (dividende + buyback ~$3.3mlrd/god) umesto da ga reinvestira u rast — prihod CAGR od svega 2.6% pokazuje da je ovo zreo, sporo rastući biznis koji se prodaje po P/E od 25.75x i PEG_forward od 3.43. Plaćaš premiju za kvalitet operativnog modela, ne za rast — ako tržište ikad preceni koliko dugo 80/20 model može održati marže bez rasta prihoda, multiple kompresija bi bila bolna.

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | ROIC ostaje visok | ≥ 27% | 70% |
| 2 | Operativna marža stabilna | ≥ 25% (±1pp) | 70% |
| 3 | Zaduženost ostaje niska | Neto dug/EBITDA < 2.0x | 70% |
| 4 | Buyback nastavlja da smanjuje broj akcija | broj akcija opada | 70% |
| 5 | Prihod ne opada | raste ≥ 2% god/god | 70% |

## 8. Odluka

- [x] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Datum ulaza:** 2026-09-04
**Cena ulaza:** 270.12
**VUAA cena istog dana:** 149.02 ← obavezno za benchmark
**Veličina pozicije:** 1/10 satelita

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu):**
1. Operativna marža padne ispod 24% dva kvartala zaredom
2. Neto dug/EBITDA pređe 2.5x dva kvartala zaredom
3. Standardni ROIC padne ispod 20% dva kvartala zaredom

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2023-2025 income statement, balance sheet, cash flow | SEC EDGAR 10-K FY2025, CIK 0000049826 | accession 0000049826-26-000008, R3/R5/R9.htm | pristupljeno 2026-09-04, licno verifikovano |
| FY2021-2022 podaci | SEC EDGAR 10-K FY2022, CIK 0000049826 | accession 0000049826-23-000008 | pristupljeno 2026-09-04 |
| Cena zatvaranja ITW | IBKR (TradingView chart, NYSE) | screenshot, 04.09.2026 zaključna sveća | 2026-09-04 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-04 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-04 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-06 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, cross-check sa Yahoo/Simply Wall St u sličnom rasponu | https://finviz.com/quote.ashx?t=ITW | pristupljeno 2026-09-06 |
| Dover, Honeywell, Lincoln Electric komparativni podaci | SEC EDGAR 10-K FY2025 | accession brojevi navedeni u §4 | pristupljeno 2026-09-06 |
