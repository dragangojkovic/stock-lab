# Analiza: Ulta Beauty, Inc. (ULTA)

**Datum:** 2026-09-08 | **Analitičar:** Dragan | **Cena na dan analize:** 564.12 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — specijalizovana maloprodaja kozmetike nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

Ulta je internacionalni specialty beauty retailer — prodaje ~30,000 SKU-ova od ~600 brendova kroz mass, prestige i profesionalni-salon cenovni nivo pod jednim krovom (kozmetika, nega kože/kose, mirisi, wellness), plus in-store full-service saloni. Preko 1,500 US prodavnica, plus Space NK (84 UK + 2 Ireland, akvizicija 2025), manji footprint u Meksiku/Kuvajtu/UAE.

- Izvori prihoda i njihov udeo: nije detaljno segmentno raščlanjeno u dostupnim izvorima (prodaja proizvoda dominira, salon usluge manji deo) — N/A, treba proveriti tačan %.
- Ko su kupci: potrošači kozmetike/lepote svih cenovnih segmenata (mass do prestige) pod jednim krovom.
- Kako se naplaćuje: prodaja u prodavnicama/online, jednokratno po transakciji, ali visoko ponavljajuće (potrošni proizvodi lepote).
- Koncentracija: nema koncentracije KUPACA. VAŽNO — koncentracija DOBAVLJAČA: top 10 brend partnera = ~51% ukupne neto prodaje FY2025 (rizik na strani ponude).

## 2. Moat — dve rečenice (obavezna kapija)

> Ultamate Rewards loyalty program ima merljiv switching-cost efekat — preko 46 miliona članova generiše ~95% ukupne prodaje, a omnichannel članovi troše preko 3x više od kupaca koji kupuju samo u prodavnici.
> Kombinacija mass+prestige+salon ponude pod jednim krovom je teško replicirati (Sephora je uglavnom prestige-only, drogerije uglavnom mass-only), što potvrđuje ULTA-ina operativna marža (12.4%) koja drastično nadmašuje jedinog pravog peer-a, Sally Beauty (8.9%).

- Kategorija: troškovi prelaska (loyalty program) + brend/asortiman prednost
- **Šta bi ubilo ovaj moat u 5 godina:** Amazon ili TikTok Shop preuzmu značajan udeo prodaje kozmetike direktno od proizvođača, zaobilazeći potrebu za fizičkim/loyalty maloprodajnim kanalom
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** 46 miliona loyalty članova i podaci o njihovom ponašanju su izgrađeni godinama; kombinacija mass+prestige asortimana zahteva odnose sa stotinama brend partnera koji se ne uspostavljaju preko noći

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/ULTA.json`:

```
SCORECARD — Ulta Beauty, Inc. (ULTA) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 33.5%, WACC 7.9%, spread 25.5% - PROŠAO
G2 ND/EBITDA≤2.5x i pokrivenost≥4x: 0.96x, 857.9x - PROŠAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 0.88 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 6/6, Palo 0 - SVE KAPIJE PROLAZE CISTO

K1 ROIC: medijana 33.5% (NAJVISI od svih maloprodajnih kandidata u projektu), trend PADA
  (33.5%→39.6%→37.3%→32.1%→25.4% - vrhunac FY2022, pa dosledan pad). WACC 7.9% (sa poznatom
  distorzijom, vidi napomenu ispod), spread 25.5% - i na dnu trenda (25.4% FY2025) i dalje
  drasticno iznad WACC-a.
K2 Marže: bruto stabilna ~39%, operativna 15.0%→12.4% (PADA DOSLEDNO od FY2022 vrhunca 16.1%),
  neto 11.4%→9.3% (PADA). Marze se smanjuju ali OSTAJU visoke naspram peer grupe.
K3 Zaduženost: prakticno bez finansijskog duga do FY2025 (samo lizinzi), ND/EBITDA 0.60-0.96x.
  Test produktivnosti duga PROLAZI (dug CAGR 4.3% = EBIT CAGR 4.3%, uglavnom lizinzi rastu
  sa brojem prodavnica, ne akvizicijom).
K4 FCF: pozitivan 5/5, FCF konverzija prosek 0.88 (solidno iznad praga 0.70). OCF/NI prosek
  1.17 - zdrav kvalitet zarade.
K5 Valuacija: P/E 22.00 (NAJNIŽE od svih zdravstvenih/industrijskih/potrošackih kandidata
  ovog kruga uprkos najvisem ROIC-u). PEG_trailing 2.37, PEG_forward 1.95 (konsenzus rast
  11.3% - JEDINI kandidat u ovom krugu sa PEG_forward ISPOD 2.0). FCF yield na EV 3.9%.
```

**Kapije:** prošlo 6/6 | palo 0 | nepoznato 0
**Override:** Nije potreban — sve kapije prolaze formalno čisto. Jedina napomena je metodološka: WACC (7.9%) ima poznatu distorziju jer `interest_expense` polje ne uključuje implicitnu kamatu na lease obaveze (koje čine >95% `total_debt` polja) — sa realističnijom pretpostavkom cene lizing-duga, WACC bi bio ~8.3%, što NE menja zaključak G1 (spread ostaje >20pp u oba scenarija).

## 4. Poređenje sa konkurencijom

| Metrika | ULTA | Sally Beauty Holdings (SBH) | Medijana grane |
|---|---|---|---|
| ROIC (5g med. za ULTA; FY2025 za SBH) | 33.5% (FY2025: 25.4%) | 11.05% | N/A |
| Bruto marža | 39.1% (FY2025) | 51.6% (FY2025) | N/A |
| Operativna marža | 12.4% (FY2025) | 8.9% (FY2025) | N/A |
| Neto marža | 9.3% (FY2025) | 5.3% (FY2025) | N/A |
| Neto dug/EBITDA | 0.96x (FY2025) | N/A — treba proveriti EBITDA komponente | N/A |
| P/E | 22.00 | N/A | N/A |
| PEG (trailing) | 2.37 | N/A | N/A |
| FCF yield na EV | 3.9% | N/A | N/A |

*Izvor Sally Beauty: SEC EDGAR 10-K, CIK 0001368458, accession 0001193125-25-280122. VAŽNA NAPOMENA O UPOREDIVOSTI: SBH je jedini pravi "pure-play" specialty beauty retailer sa javnim SEC podacima, ali je manji i pozicioniran mnogo bliže "value/mass" segmentu (51.6% bruto marža vs ULTA-inih 39% odražava drugačiji proizvodni/wholesale mix, ne nužno superiorniju ekonomiju) — NIJE direktno uporediv sa ULTA-inim mass+prestige modelom. ULTA značajno nadmašuje SBH po ROIC-u (33.5% vs 11.05%), operativnoj marži (12.4% vs 8.9%) i neto marži (9.3% vs 5.3%) uprkos nižoj bruto marži — sugeriše da je ULTA operativno mnogo efikasnija, verovatno zahvaljujući skali i loyalty-vođenom modelu koji Sally Beauty nema.*

**Ako marža pada — pada li svima u grani ili samo njoj?** ULTA-ina operativna marža pada (16.1%→12.4%) dok nemam dovoljno podataka da utvrdim trend kod Sally Beauty (samo jedna godina prikupljena). Bez šireg konteksta, ne mogu čvrsto zaključiti da li je pad makro (industrija kozmetike/lepote generalno pod pritiskom, npr. usled promene potrošačkih navika ili konkurencije od Amazon-a/TikTok Shop-a) ili specifičan za ULTA. **Ovo je otvoreno pitanje** — vredno je proveriti pre ulaska da li je pad marže vezan za investicije u loyalty/marketing (dobra investicija) ili cenovni pritisak (loš signal).

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 2.37 | prošli EPS rast (9.3% CAGR) se nastavlja |
| PEG_forward | 1.95 | konsenzus analitičara (11.3% EPS rast) je tačan |
| FCF yield na EV | 3.9% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 3.8% | dilucija je realan trošak (ovde nebitna, SBC/prihod 0.3%) |

**Razlika između PEG_trailing i PEG_forward:** MALA i u OČEKIVANOM SMERU — 2.37 vs 1.95, konsenzus (11.3%) je BLAGO viši od trailing (9.3%), implicira umereno ubrzanje. Ovo je najzdraviji PEG profil od svih kandidata analiziranih u ovom krugu (TMO, EW, STE, TSCO su svi imali PEG_forward >3.5 ili besmislen negativan PEG_trailing) — ULTA je JEDINI kandidat gde i trailing i forward PEG padaju ispod 2.5, sa forward ispod 2.0. Per CLAUDE.md K5, PEG < 1.0 je "zanimljivo", 1.0-2.0 je "neutralno" — ULTA je na samoj granici neutralne zone, atraktivnije od svega drugog analiziranog nedavno.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

1. Operativna marža nastavi da pada ispod 11% — signal da loyalty program gubi snagu cenovne moći, ne samo da apsorbuje marketing investicije.
2. Broj loyalty članova ili % prodaje od loyalty počne da opada — direktan udar na moat tezu.
3. Prihod padne ispod 5% god/god rasta dva kvartala zaredom — signal da konkurencija (Amazon, TikTok Shop, Sephora) preuzima tržišni udeo brže nego što se misli.

**Šta je najjači argument protiv kupovine ove akcije?** Operativna marža opada dosledno već 3 godine (16.1%→12.4%) i ROIC prati isti trend (39.6%→25.4%) — čak i ako je ULTA i dalje najbolji od loše grupe (Sally Beauty), sama činjenica da pad traje 3 uzastopne godine sugeriše da konkurentski pritisak (online prodaja lepote, TikTok Shop influenceri koji preusmeravaju kupovinu) nije prolazan trend nego strukturna promena industrije koju ni najjača loyalty baza ne može potpuno zaustaviti.

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | ROIC drži nivo | ≥ 25% | 70% |
| 2 | Operativna marža stabilna | ≥ 12% (±1pp) | 70% |
| 3 | Zaduženost ostaje niska | Neto dug/EBITDA < 1.5x | 70% |
| 4 | Prihod raste | ≥ 6% god/god | 70% |
| 5 | Broj akcija nastavlja da opada | buyback nastavlja | 70% |

## 8. Odluka

- [x] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Datum ulaza:** 2026-09-04
**Cena ulaza:** 564.12
**VUAA cena istog dana:** 149.02 ← obavezno za benchmark
**Veličina pozicije:** 1/10 satelita

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu):**
1. Operativna marža padne ispod 10% dva kvartala zaredom
2. Neto dug/EBITDA pređe 2.0x dva kvartala zaredom
3. Moat teza opovrgnuta — konkretno, % prodaje od loyalty članova padne ispod 90% ili broj članova stagnira/opada

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2025 income statement | SEC EDGAR 10-K FY2025, CIK 0001403568 | accession 0001104659-26-035243, R4.htm | pristupljeno 2026-09-08, licno verifikovano |
| FY2021-2024 podaci | SEC EDGAR 10-K FY2021-2024 | accession brojevi u data/ULTA.json | pristupljeno 2026-09-08 |
| Cena zatvaranja ULTA | IBKR (TradingView chart, NASDAQ) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-08 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-08 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, interno konzistentan sa next-Y figurom | https://finviz.com/quote.ashx?t=ULTA | pristupljeno 2026-09-08 |
| Sally Beauty Holdings komparativni podaci | SEC EDGAR 10-K, CIK 0001368458 | accession 0001193125-25-280122 | pristupljeno 2026-09-08 |
