# Analiza: DexCom, Inc. (DXCM)

**Datum:** 2026-09-11 | **Analitičar:** Dragan | **Cena na dan analize:** 87.90 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — medicinski uređaji/CGM tehnologija nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

DexCom razvija i komercijalizuje sisteme za kontinuirani monitoring glukoze (CGM) za dijabetičare. Sistem se sastoji od potrošnog senzora (nosi se 10-15.5 dana, zavisno od generacije — G6 vs G7/G7 15 Day platforma), reusable transmittera i opcionog receiver-a/smartphone aplikacije.

- Izvori prihoda i njihov udeo: prodaja po kanalu (FY2025): US distributer $3,195.7M, US direktno $139.2M, internacionalno distributer $763.3M, internacionalno direktno $563.8M — ukupno $4,662M. Nema objavljenog % prihoda specifično od potrošnog senzora vs trajne opreme.
- Ko su kupci: dijabetičari (pacijenti), preko distributera/apotekarskih kanala.
- Kako se naplaćuje: senzor je "razor/blade" recurring komponenta (menja se svakih 10-15 dana), transmitter/receiver su trajni.
- Koncentracija: **EKSTREMNA** — tri neimenovana kupca ("Customer A/B/C") predstavljaju 35-55%, 30-35%, 37-46% prihoda respektivno (FY2023-2025), zajedno preko 100% (verovatno preklapajući distributerski/PBM kanali). Customer A sam čini >50% prihoda u FY2025 — identitet nije utvrđen iz izveštaja.

## 2. Moat — dve rečenice (obavezna kapija)

> Razor/blade model (potrošni senzori se menjaju svakih 10-15 dana) generiše ponavljajuću prodaju, a FDA odobrenje + integracija sa insulin pump/automated-dosing sistemima stvara troškove prelaska za pacijenta i lekara.
> Operativna marža (19.6%) je najviša od DXCM/Abbott/Medtronic uprkos padu bruto marže, sugerišući operativnu disciplinu koja kompenzuje cenovni pritisak.

- Kategorija: troškovi prelaska (switching costs) + regulatorna barijera (FDA)
- **Šta bi ubilo ovaj moat u 5 godina:** Abbott-ov FreeStyle Libre nastavi da preuzima tržišni udeo cenovnom konkurencijom ILI se pojavi neinvazivna alternativa monitoringu glukoze koja eliminiše potrebu za senzorom
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** FDA odobrenje za nove CGM platforme traje godinama kliničkih ispitivanja; integracija sa insulin pump ekosistemima (Tandem, Insulet) zahteva partnerske ugovore izgrađene tokom vremena

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/DXCM.json`:

```
SCORECARD — DexCom, Inc. (DXCM) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 11.6%, WACC 10.8%, spread 0.8% - PAO (GRANICNO)
G2 ND/EBITDA≤2.5x i pokrivenost≥4x: 0.28x, 49.8x - PROŠAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 0.89 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 5/6, Palo 1 (G1, GRANICNO)

K1 ROIC: medijana 11.6% (TIK ISPOD 12% praga), trend SNAZNO RASTE (8.8%→9.9%→11.6%→
  12.4%→22.8% - gotovo utrostruceno kroz 5 godina). WACC 10.8% (visoka zbog bete 1.42),
  spread svega 0.8% na medijani, ALI FY2025 SAMA GODINA (22.8%) ima spread od 12pp.
K2 Marže: bruto OPADA DOSLEDNO (68.6%→60.1%, verovatno cenovni pritisak od Abbott Libre),
  operativna RASTE (10.9%→19.6%) i neto RASTE (8.9%→17.9%) uprkos padu bruto marze -
  operativni leveridž (SG&A/R&D rastu sporije od prihoda) kompenzuje pad bruto marze.
K3 Zaduženost: ND/EBITDA 1.77x→0.28x (POBOLJŠAVA SE), pokrivenost kamata 14.1x→49.8x.
  Test produktivnosti duga PROLAZI (dug CAGR -7.6% << EBIT CAGR 36.1%).
K4 FCF: pozitivan 5/5, FCF konverzija prosek 0.89 (dobro). FY2021 FCF nakon SBC bio
  NEGATIVAN (-60M) - jedina slaba godina, objasnjena visokim CapEx-om (fabrika izgradnja).
K5 Valuacija: P/E 42.06 (skupo nominalno). PEG_trailing 1.03 (odlicno), PEG_forward 1.99
  (na granici neutralne zone <2.0). FCF yield na EV 3.0%.
```

**Kapije:** prošlo 5/6 | palo 1 (G1, granično) | nepoznato 0
**Override:** Standardni ROIC pada TIK ispod praga (11.6% vs 12%, spread 0.8pp) — ovo je granični, ne dramatičan pad. Trend je izuzetno snažan (ROIC gotovo utrostručen 8.8%→22.8%), a FY2025 sama godina (22.8%) ima spread od 12pp iznad WACC-a. Ovo je klasičan "trend > nivo" slučaj iz CLAUDE.md — override bi bio opravdan da nije EKSTREMNE koncentracije distributera (Customer A >50% prihoda), koja predstavlja materijalan, nekvantifikovan rizik nezavisan od finansijskih metrika.

## 4. Poređenje sa konkurencijom

| Metrika | DXCM | Abbott (ABT) | Medtronic (MDT) | Medijana grane |
|---|---|---|---|---|
| ROIC (5g med. za DXCM; FY najnovija za konk.) | 11.6% (FY2025: 22.8%) | 10.86% | 6.75% | N/A |
| Bruto marža | 60.1% (FY2025) | 56.4% | 65.0% | N/A |
| Operativna marža | 19.6% (FY2025) | 18.2% | 17.8% | N/A |
| Neto marža | 17.9% (FY2025) | 14.7% | 13.2% | N/A |
| Neto dug/EBITDA | 0.28x (FY2025) | 0.39x | 2.76x (ili ~1.99x uz kratkorocne investicije kao kvazi-gotovinu) | N/A |
| P/E | 42.06 | N/A | N/A | N/A |
| PEG (trailing) | 1.03 | N/A | N/A | N/A |
| FCF yield na EV | 3.0% | N/A | N/A | N/A |

*Izvor Abbott: SEC EDGAR 10-K FY2025, CIK 0000001800, accession 0001628280-26-010185. Izvor Medtronic: 10-K FY2026 (fiskalna godina zavrsava krajem aprila), CIK 0001613103, accession 0001628280-26-044354. VAŽNA NAPOMENA O UPOREDIVOSTI: oba su MNOGO diversifikovanija od DXCM-a — Abbott pokriva Nutrition/Diagnostics/Established Pharma/Medical Devices (samo Diabetes Care/Libre je uporediv deo), Medtronic pokriva Cardiovascular/Neuroscience/Medical Surgical/Diabetes (samo Diabetes segment je uporediv). Konsolidovane marže NISU reprezentativne za njihove CGM podsegmente specificno — ABT-ov FreeStyle Libre je DIREKTAN konkurent DXCM-u u istoj niši.*

**Ako marža pada — pada li svima u grani ili samo njoj?** DXCM-ova bruto marža pada (68.6%→60.1%) dok Abbott (56.4%) i Medtronic (65.0%) nemaju uporedive CGM-specifične brojeve za proveru da li i njima pada. DXCM-ova operativna marža (19.6%) je NAJVIŠA od sve tri kompanije uprkos padu bruto marže — ovo sugeriše da je pad bruto marže delom cenovni pritisak (verovatno od Abbott Libre-a, koji je jeftiniji proizvod), ali da DXCM kompenzuje operativnom disciplinom (SG&A/R&D rastu sporije od prihoda).

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 1.03 | prošli EPS rast (40.9% CAGR) se nastavlja |
| PEG_forward | 1.99 | konsenzus analitičara (21.2% EPS rast) je tačan |
| FCF yield na EV | 3.0% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 2.6% | dilucija je realan trošak (SBC/prihod 3.4%, umereno, opadajuće) |

**Razlika između PEG_trailing i PEG_forward:** ZNAČAJNA — 1.03 vs 1.99. Konsenzus (21.2%) je upola niži od trailing EPS CAGR-a (40.9%) — implicira usporavanje rasta nakon perioda vrlo brzog uvećanja profitabilnosti (FY2025 EBIT skočio 52% god/god). Ovo je razumno očekivanje (teško je održati 40%+ EPS rast neograničeno), ali PEG_forward od 1.99 je i dalje na granici "zanimljivo/neutralno" praga (2.0) — nije skupo čak i uz konzervativniju pretpostavku.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

1. Bruto marža nastavi da pada ispod 58% — potvrđuje da je cenovni pritisak od Abbott Libre strukturan, ne privremen.
2. ROIC padne ispod 15% dva kvartala zaredom nakon FY2025 skoka na 22.8% — signal da je taj skok bio jednokratan, ne novi nivo.
3. Identitet i priroda "Customer A" (>50% prihoda) se otkrije kao rizičniji nego pretpostavljeno (npr. gubitak tog kanala bi bio katastrofalan) — materijalizacija koncentracionog rizika.

**Šta je najjači argument protiv kupovine ove akcije?** Preko 50% prihoda DXCM-a zavisi od jednog neimenovanog distributerskog/PBM kanala ("Customer A") čiji identitet nije utvrđen iz izveštaja — ovo je materijalan, nekvantifikovan rizik koji nijedan drugi kandidat u ovom krugu healthcare screeninga nema (GEHC eksplicitno nema koncentraciju kupaca). Ako taj kanal promeni uslove, izgubi ugovor, ili bude zamenjen konkurentskim rešenjem, uticaj na prihod bi bio nesrazmerno veliki.

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | ROIC ostaje visok | ≥ 15% | 70% |
| 2 | Operativna marža stabilna | ≥ 18% (±1pp) | 70% |
| 3 | Bruto marža ne pada dalje | ≥ 58% | 70% |
| 4 | Prihod raste | ≥ 15% god/god | 70% |
| 5 | Zaduženost ostaje niska | Neto dug/EBITDA < 1.0x | 70% |

## 8. Odluka

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam: identitet/priroda Customer A se razjasni kao manje rizičan ILI standardni ROIC pređe 15% dva kvartala zaredom
- [ ] Odbijeno — razlog: {…}

**Datum ulaza:** N/A — nije ulazak, watchlist
**Cena ulaza:** N/A
**VUAA cena istog dana:** N/A
**Veličina pozicije:** N/A

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu):**
1. N/A — watchlist, nema pozicije za izlaz

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2023-2025 income statement | SEC EDGAR 10-K FY2025, CIK 0001093557 | accession 0001093557-26-000027, R5.htm | pristupljeno 2026-09-11, licno verifikovano |
| FY2021-2022 podaci (restatovano ASU 2020-06) | SEC EDGAR 10-K FY2021/2022, CIK 0001093557 | accession 0001093557-22-000014, 0001093557-23-000024 | pristupljeno 2026-09-11 |
| Cena zatvaranja DXCM | IBKR (TradingView chart, NASDAQ) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-11 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-11 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA | https://finviz.com/quote.ashx?t=DXCM | pristupljeno 2026-09-11 |
| Abbott, Medtronic komparativni podaci | SEC EDGAR 10-K | accession brojevi navedeni u §4 | pristupljeno 2026-09-11 |
