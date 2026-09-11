# Analiza: GE HealthCare Technologies Inc. (GEHC)

**Datum:** 2026-09-11 | **Analitičar:** Dragan | **Cena na dan analize:** 68.86 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — medicinska imidžing oprema nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

GE HealthCare je proizvođač medicinske imidžing/dijagnostičke opreme, spinovan iz GE (sada GE Aerospace) 3. januara 2023, organizovan u 4 segmenta: Imaging (MRI/CT/X-ray/mamografija, 44.8% prihoda FY2025), AVS-Advanced Visualization Solutions (ultrazvuk, 26%), PCS-Patient Care Solutions (monitori pacijenata, EKG, potrošni materijal, 15%), PDx-Pharmaceutical Diagnostics (kontrastna sredstva/radiofarmaceutici, 14%).

- Izvori prihoda i njihov udeo: Sales of products $13,661M vs Sales of services $6,964M (FY2025) — 34% prihoda su usluge/servis, najbliža kvantifikovana mera recurring prihoda.
- Ko su kupci: bolnice i dijagnostički centri koji kupuju/servisiraju imidžing opremu.
- Kako se naplaćuje: prodaja opreme (installed base) + dugoročni servisni ugovori + potrošni materijal (kontrastna sredstva, senzori/elektrode).
- Koncentracija: **NEMA** koncentracije kupaca — eksplicitno potvrđeno u 10-K ("No single customer accounted for more than 10% of revenues").

**NAPOMENA — samo 4 godine podataka:** GEHC ima samostalnu istoriju od januara 2023, standardni 5-godišnji format nije primenjiv — vidi `data/GEHC.json` za detalje.

## 2. Moat — dve rečenice (obavezna kapija)

> Velika instalirana baza skupe imidžing opreme (MRI/CT) generiše dugoročne servisne ugovore i recurring prihod od potrošnog materijala (PDx kontrastna sredstva, PCS senzori) — bolnice retko menjaju dobavljača imidžing opreme zbog troškova obuke osoblja i integracije sa postojećim IT sistemima.
> Duopol/oligopol sa Siemens Healthineers i Philips u većini segmenata, uz GEHC koji značajno nadmašuje oba SEC-uporediva konkurenta (Medtronic, Philips) po ROIC-u.

- Kategorija: troškovi prelaska (switching costs) + ekonomija obima/servisna mreža
- **Šta bi ubilo ovaj moat u 5 godina:** disruptivna, jeftinija imidžing tehnologija (npr. AI-pojačan portable ultrazvuk zamenjuje deo MRI/CT upotrebe) ILI bolnice počnu insourcing servis umesto proizvođačkih ugovora
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** FDA/regulatorna odobrenja za medicinsku imidžing opremu traju godinama; servisna mreža i obučeno osoblje na terenu se grade decenijama poverenja sa bolnicama

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/GEHC.json`:

```
SCORECARD — GE HealthCare Technologies Inc. (GEHC) | Podaci: 4 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 12.8%, WACC 7.2%, spread 5.7% - PROŠAO
G2 ND/EBITDA≤2.5x i pokrivenost≥4x: 1.65x, 6.3x - PROŠAO
G3 FCF pozitivan ≥4/4g: 4/4 - PROŠAO
G4 FCF konverzija≥0.7: 0.89 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 6/6, Palo 0

K1 ROIC: medijana 12.8%, trend RASTE (12.1%→11.8%→14.4%→13.5%). WACC 7.2% (beta 0.82,
  ali GEHC trguje samostalno tek ~2.7 godine - beta procena nepouzdana), spread 5.7%.
  Standardni ROIC vec komotno prolazi bez potrebe za goodwill iskljucenjem - ROIC
  ex-goodwill bi bio APSURDNO VISOK (89-150%, artefakt malog IC-a ex goodwill), NIJE
  koriscen kao primaran signal.
K2 Marže: bruto ~39-42% (stabilna), operativna ~12.5-13.8% (stabilna), neto ~8-10.4%
  (stabilna, FY2023 najniza zbog neuobicajeno visoke poreske stope 31.5%).
K3 Zaduženost: ND/EBITDA 2.16x→1.65x (POBOLJŠAVA SE), pokrivenost kamata 32.8x(FY22,
  pre pune godine spinoff-duga)→4.5x(FY23, prva puna godina sa punim kamatnim
  opterecenjem)→6.3x(FY25, oporavlja se). TEST PRODUKTIVNOSTI DUGA PADA (dug CAGR
  6.6% > EBIT CAGR 3.1%) - SOFT SIGNAL ZA PAZNJU uprkos formalno cistom prolazu G2.
K4 FCF: pozitivan 4/4, FCF konverzija prosek 0.89 (dobro), ALI FCF OPADA (-6.2% CAGR,
  FCF/akcija CAGR -6.5%) uprkos rastu prihoda (4.0% CAGR) - CapEx raste brze od OCF-a
  (310M->482M) - DRUGI SOFT SIGNAL ZA PAZNJU.
K5 Valuacija: P/E 15.13 (NAJJEFTINIJE od svih zdravstvenih kandidata u projektu).
  PEG_trailing 5.95 (istorijski EPS CAGR samo 2.5% - spor), PEG_forward 1.59 (konsenzus
  rast 9.5% - MNOGO visi od trailing, zahteva eksplicitno obrazlozenje ubrzanja).
  FCF yield na EV 4.1% (nakon SBC 3.7%).
```

**Kapije:** prošlo 6/6 | palo 0 | nepoznato 0
**Override:** Nije formalno potreban (sve kapije prolaze), ali DVA soft signala zaslužuju pažnju u §6: (1) test produktivnosti duga formalno pada (dug raste brže od EBIT-a), i (2) FCF dosledno opada (-6.2% CAGR) uprkos rastu prihoda, zbog CapEx-a koji raste brže od operativnog cash flow-a. Ovo nije dovoljno da obori kapije, ali je vredno praćenja.

## 4. Poređenje sa konkurencijom

| Metrika | GEHC | Medtronic (MDT) | Philips (PHG) | Medijana grane |
|---|---|---|---|---|
| ROIC (5g med. za GEHC; FY najnovija za konk.) | 12.8% (FY2025: 13.5%) | 6.75% | 6.66% | N/A |
| Bruto marža | 40.0% (FY2025) | 65.0% | 45.2% | N/A |
| Operativna marža | 13.4% (FY2025) | 17.8% | 8.0% | N/A |
| Neto marža | 10.1% (FY2025) | 13.2% | 5.0% | N/A |
| Neto dug/EBITDA | 1.65x (FY2025) | 2.76x (ili ~1.99x uz kratkoročne investicije kao kvazi-gotovinu) | 2.08x | N/A |
| P/E | 15.13 | N/A | N/A | N/A |
| PEG (trailing) | 5.95 | N/A | N/A | N/A |
| FCF yield na EV | 4.1% | N/A | N/A | N/A |

*Izvor Medtronic: SEC EDGAR 10-K FY2026, CIK 0001613103, accession 0001628280-26-044354. Izvor Philips: SEC EDGAR 20-F FY2025 (holandska kompanija, ADR filer, IFRS), CIK 0000313216, accession 0001628280-26-009470. Siemens Healthineers (najbliži direktan imidžing konkurent) NIJE SEC filer (nemačka kompanija, izveštava po BaFin/EU pravilima, nema 10-K/20-F/40-F na EDGAR-u) — N/A, nije uključen u tabelu. GEHC ZNAČAJNO NADMAŠUJE oba SEC-uporediva konkurenta po ROIC-u (12.8-13.5% vs 6.75%/6.66%) — moguće objašnjenje: Medtronic i Philips su šire diversifikovani (Medtronic ima velike Cardiovascular/Neuroscience segmente, Philips ima Consumer Health i druge niže-marginalne linije) dok je GEHC fokusiran čisto na imaging/dijagnostiku.*

**Ako marža pada — pada li svima u grani ili samo njoj?** GEHC-ove marže su STABILNE (ne padaju) kroz sve 4 godine dostupnih podataka. GEHC ima nižu bruto maržu od oba konkurenta (40.0% vs 65.0% Medtronic, ali VIŠU od 45.2% Philips) ali VIŠU operativnu maržu od Philips-a (13.4% vs 8.0%) — sugeriše da GEHC posluje efikasnije od Philips-a specifično u imidžing/dijagnostičkom prostoru, iako je manje profitabilan po bruto marži od šire-diversifikovanog Medtronic-a.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 5.95 | prošli EPS rast (2.5% CAGR) se nastavlja — vrlo spor istorijski rast |
| PEG_forward | 1.59 | konsenzus analitičara (9.5% EPS rast) je tačan |
| FCF yield na EV | 4.1% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 3.7% | dilucija je realan trošak (ovde gotovo nebitna, SBC/prihod 0.6%) |

**Razlika između PEG_trailing i PEG_forward:** OGROMNA — 5.95 vs 1.59, skoro 4x razlika. Konsenzus (9.5%) je drastično viši od trailing EPS CAGR-a (2.5%) — ovo JE tačno CLAUDE.md upozorenje: "ako je PEG_forward mnogo niži od PEG_trailing, tržište/analitičari očekuju ubrzanje koje se još nije dogodilo." Trailing period (FY2022-2025) je bio opterećen post-spinoff troškovima (penziona obaveza, jednokratna poreska stopa FY2023, kamate na novi dug) koji verovatno neće se ponoviti — deo očekivanog ubrzanja može biti legitiman (normalizacija posle spinoff tranzicije), ali 9.5% konsenzus i dalje zahteva eksplicitnu proveru šta konkretno ga pokreće (novi proizvodi? AI-imidžing? margin expansion?) pre prihvatanja kao datosti.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

1. Test produktivnosti duga se ne popravi (dug nastavi da raste brže od EBIT-a) — signal da spinoff-dug postaje strukturan teret, ne prolazna faza.
2. FCF nastavi da opada (CapEx raste brže od OCF-a) dva kvartala zaredom — signal da kompanija troši više nego što generiše, bez jasnog povratka na investiciju.
3. PEG_forward premisa (9.5% EPS rast) se ne materijalizuje — ako EPS rast ostane na trailing nivou (2.5%), akcija nije jeftina kao što izgleda.

**Šta je najjači argument protiv kupovine ove akcije?** GEHC ima samo 2.7 godine samostalne trgovinske istorije i istorija je opterećena post-spinoff šumom (penziona obaveza skok, jednokratna poreska stopa, kamate na novi dug) — teško je razlikovati "normalizaciju" od "strukturnog problema" sa tako kratkom čistom istorijom. Test produktivnosti duga formalno pada i FCF opada uprkos rastu prihoda — ako se ovi trendovi nastave, niska P/E (15.13) neće ostati jeftina, postaće opravdano niska.

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | ROIC ostaje visok | ≥ 12% | 70% |
| 2 | Operativna marža stabilna | ≥ 13% (±1pp) | 70% |
| 3 | Zaduženost ostaje umerena | Neto dug/EBITDA < 2.0x | 70% |
| 4 | FCF prestane da opada | ≥ 0% god/god | 70% |
| 5 | Prihod raste | ≥ 4% god/god | 70% |

## 8. Odluka

- [x] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Datum ulaza:** 2026-09-04
**Cena ulaza:** 68.86
**VUAA cena istog dana:** 149.02 ← obavezno za benchmark
**Veličina pozicije:** 1/10 satelita

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu):**
1. Neto dug/EBITDA pređe 2.5x dva kvartala zaredom
2. FCF nastavi da opada 3 uzastopna kvartala
3. Standardni ROIC padne ispod 10% dva kvartala zaredom

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2025 income statement | SEC EDGAR 10-K FY2025, CIK 0001932393 | accession 0001932393-26-000007, R3.htm | pristupljeno 2026-09-11, licno verifikovano |
| FY2022-2024 podaci | SEC EDGAR 10-K FY2023/2024, CIK 0001932393 | accession 0001932393-24-000013, 0001932393-25-000005 | pristupljeno 2026-09-11 |
| Cena zatvaranja GEHC | IBKR (TradingView chart, NASDAQ) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Beta | stockanalysis.com — TREĆA STRANA, NEPOUZDANA (GEHC ima samo ~2.7 godine samostalne trgovinske istorije, "5g" labela je verovatno pogrešna/uključuje pre-spinoff proxy) | N/A — treba proveriti tačan URL | pristupljeno 2026-09-11 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-11 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA | https://finviz.com/quote.ashx?t=GEHC | pristupljeno 2026-09-11 |
| Medtronic, Philips komparativni podaci | SEC EDGAR 10-K/20-F | accession brojevi navedeni u §4 | pristupljeno 2026-09-11 |
