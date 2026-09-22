# Analiza: Linde plc (LIN)

**Datum:** 2026-09-11 | **Analitičar:** Dragan | **Cena na dan analize:** 477.57 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — industrijski gasovi/hemijska proizvodnja nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

Linde je najveći svetski proizvođač industrijskih gasova (kiseonik, azot, vodonik) kroz tri distribuciona kanala: on-site/tonnage (najveći kupci preko kriogenih/procesnih postrojenja izgrađenih direktno kod klijenta), merchant/bulk (distribuiran tečni gas cisternama), i packaged/cylinder (mali kupci preko cilindara).

- Izvori prihoda i njihov udeo: nije detaljno segmentno raščlanjeno u dostupnim izvorima — N/A, treba proveriti tačan % po kanalu.
- Ko su kupci: industrijski proizvođači (hemijska, metalurška, prehrambena, elektronska industrija), zdravstvo (medicinski gasovi).
- Kako se naplaćuje: on-site ugovori tipično 10-20 godina sa minimalnim obavezama kupovine (de facto take-or-pay), merchant 3-7 godina, packaged 1-3 godine.
- Koncentracija: "Linde is not dependent upon a single customer or a few customers" — eksplicitno navedeno, bez numeričkog podatka.

## 2. Moat — dve rečenice (obavezna kapija)

> On-site/pipeline infrastruktura izgrađena direktno kod klijenta (kriogena postrojenja, cevovodi za kiseonik/azot/vodonik) integrisana je u proizvodni proces klijenta — premeštanje na drugog dobavljača zahteva novu kapitalnu investiciju i godine izgradnje, stvarajući ekstremno visoke troškove prelaska.
> Take-or-pay ugovori od 10-20 godina obezbeđuju predvidljiv, ugovorno zaštićen prihod.

- Kategorija: troškovi prelaska (switching costs) + regulatorna/infrastrukturna barijera
- **Šta bi ubilo ovaj moat u 5 godina:** industrijski vodonik CapEx ekspanzija se pokaže neisplativom (Air Products stil impairment) i troši kapital bez povrata
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** treba mu godine izgradnje sopstvene on-site infrastrukture kod svakog klijenta pojedinačno; postojeća pipeline mreža Linde-a je decenijska prednost koju nije moguće brzo duplirati

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/LIN.json`:

```
SCORECARD — Linde plc (LIN) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 11.4%, WACC 7.4%, spread 4.0% - PAO (spread prolazi,
  ali apsolutni nivo 11.4% ne dostize 12% prag - kapija zahteva OBA uslova)
G2 ND/EBITDA≤3.0x i pokrivenost≥4x: 1.73x, 15.5x - PROŠAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 1.10 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 5/6, Palo 1 (G1)

K1 ROIC: medijana 11.4%, trend RASTE (6.8%→7.6%→11.4%→12.1%→11.5%). WACC 7.4%, spread 4.0%.
K1 ROIC EX-GOODWILL (rucno izracunato, goodwill $25.8-27.9mlrd od 2018 Linde/Praxair merdzera):
  FY2021 13.2% → FY2022 14.9% → FY2023 22.4% → FY2024 22.9% → FY2025 21.5%
  Medijana ex-goodwill ~21.5%, SNAZNO RASTE - jak override argument.
K2 Marže: bruto 43.0%→48.8%, operativna 16.2%→26.3% (RASTE DOSLEDNO), neto 12.4%→20.3% (RASTE).
K3 Zaduženost: ND/EBITDA 1.18x→1.73x (blago RASTE), pokrivenost kamata 22.0x→15.5x (i dalje
  komotno iznad praga). TEST PRODUKTIVNOSTI DUGA PADA (dug CAGR 17.4% > EBIT CAGR 15.7%) -
  dug raste da finansira buyback+CapEx brze nego EBIT - SOFT SIGNAL ZA PAZNJU.
K4 FCF: pozitivan 5/5, FCF konverzija prosek 1.10 (dobro), ALI FCF OPADA 2021-2024
  (6,639M->4,926M) usled rastuceg CapEx-a (clean energy/vodonik projekti), pa blago raste
  2025 (5,089M).
K5 Valuacija: P/E 32.69. PEG_trailing N/A (nije racunat u ovom prolazu), PEG_forward 3.46
  (konsenzus rast 9.44%, mnogo nizi od trailing EPS CAGR 18.8% - ocekivano usporavanje).
  FCF yield na EV 2.06%.
```

**Kapije:** prošlo 5/6 | palo 1 (G1) | nepoznato 0
**Override:** Standardni ROIC (medijana 11.4%) je TIK ispod praga (12%) - spread (4.0pp) formalno prolazi, ali apsolutni nivo ne. Ovo je delom goodwill dilucija (2018 merdžer), a ROIC ex-goodwill (21.5% medijana, snažno rastući) bi bio jak override argument. MEĐUTIM, test produktivnosti duga PADA (dug raste brže od EBIT-a) i FCF opada 4 od 5 godina — ovo NIJE čist "goodwill artefakt" slučaj kao ROP, već kombinacija goodwill dilucije I rastuće CapEx/dug intenzivnosti (verovatno vodonik/dekarbonizacija investicije). Override bi zahtevao potvrdu da će ti CapEx projekti generisati adekvatan povrat.

## 4. Poređenje sa konkurencijom

| Metrika | LIN | Air Products (APD) | Medijana grane |
|---|---|---|---|
| ROIC (5g med. za LIN; FY2025 za APD) | 11.4% (ex-goodwill: 21.5%) | N/A — FY2025 operativni/neto gubitak (impairment/restrukturiranje) | N/A |
| Bruto marža | 48.8% (FY2025) | 31.4% (FY2025) | N/A |
| Operativna marža | 26.3% (FY2025) | -7.3% (FY2025, anomalna godina) | N/A |
| Neto marža | 20.3% (FY2025) | -3.3% (FY2025) | N/A |
| Neto dug/EBITDA | 1.73x (FY2025) | N/A — EBITDA depresovana jednokratnim troškovima, netačno bi bilo računati | N/A |
| P/E | 32.69 | N/A | N/A |
| FCF yield na EV | 2.06% | N/A | N/A |

*Izvor Air Products: SEC EDGAR 10-K, CIK 0000002969, accession 0000002969-25-000055 (fiskalna godina završava 30.9). L'Air Liquide S.A. (drugi glavni konkurent) NIJE SEC filer (francuska kompanija, nema 10-K/20-F na EDGAR-u) — N/A, nije uključen. VAŽNA NAPOMENA: Air Products je imao operativni i neto GUBITAK u FY2025 usled velikih impairment/restrukturiranje troškova — ovo NIJE reprezentativna godina za poređenje kvaliteta poslovanja, samo za kontekst da je industrija trenutno pod pritiskom (verovatno vezano za velike vodonik projekte koji nisu isplativi kao planirano — relevantno jer LIN ima sličnu CapEx ekspanziju u vodonik).*

**Ako marža pada — pada li svima u grani ili samo njoj?** LIN marže NE padaju — dosledno rastu (operativna 16.2%→26.3%). Air Products-ov gubitak u FY2025 je verovatno signal da industrijski gas sektor ima izazove sa velikim vodonik/clean energy CapEx projektima koji ne generišu očekivan povrat — LIN takođe ima rastući CapEx u istom prostoru, što je relevantno upozorenje za praćenje (da li će i LIN imati slične probleme sa svojim vodonik investicijama).

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | N/A (nije eksplicitno računat, EPS CAGR 18.8%) | prošli EPS rast se nastavlja |
| PEG_forward | 3.46 | konsenzus analitičara (9.44% EPS rast) je tačan |
| FCF yield na EV | 2.06% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 1.99% | dilucija je realan trošak (ovde nebitna, SBC/prihod 0.5%) |

**Razlika između PEG_trailing i PEG_forward:** Konsenzus (9.44%) je upola niži od trailing EPS CAGR-a (18.8%) — implicira usporavanje. FCF yield od 2.06% je nisko naspram ostalih materijala kandidata (ECL 2.18%, SHW 2.76%) — LIN je najskuplji od tri po ovoj forecast-free metrici, verovatno zbog kvaliteta/moat-a koji tržište plaća premijom.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

1. Test produktivnosti duga se ne popravi (dug nastavi da raste brže od EBIT-a) — signal da CapEx ekspanzija (vodonik/dekarbonizacija) ne generiše adekvatan povrat.
2. Air Products stil operativni gubitak (impairment na vodonik projekte) se ponovi kod LIN-a — direktna potvrda da je industrijski vodonik CapEx trenutno loše investiran kapital.
3. ROIC ex-goodwill padne ispod 18% (obrne rastući trend) — signal da čak i osnovni posao slabi, ne samo goodwill dilucija.

**Šta je najjači argument protiv kupovine ove akcije?** LIN je usred velike CapEx ekspanzije u vodonik/clean energy prostoru gde je najbliži konkurent (Air Products) upravo prijavio operativni gubitak zbog istog tipa investicije — postoji realan rizik da LIN prati isti put, samo sa vremenskim pomakom, i da ćemo za 1-2 godine gledati sličan impairment.

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | ROIC ex-goodwill ostaje visok | ≥ 18% | 70% |
| 2 | Operativna marža stabilna | ≥ 25% (±1pp) | 70% |
| 3 | FCF prestane da opada | ≥ 0% god/god | 70% |
| 4 | Zaduženost ostaje umerena | Neto dug/EBITDA < 2.0x | 70% |
| 5 | CapEx tempo se stabilizuje | ne pređe $5.5mlrd | 70% |

## 8. Odluka

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam: FCF trend se obrne naviše 2 kvartala zaredom ILI standardni ROIC pređe 12%
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
| FY2025 income statement | SEC EDGAR 10-K FY2025, CIK 0001707925 | accession 0001628280-26-011430, R3.htm | pristupljeno 2026-09-11, licno verifikovano |
| FY2021-2024 podaci | SEC EDGAR 10-K FY2021-2024 | accession brojevi u data/LIN.json | pristupljeno 2026-09-11 |
| Cena zatvaranja LIN | IBKR (TradingView chart, NASDAQ) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-11 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-11 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA | https://finviz.com/quote.ashx?t=LIN | pristupljeno 2026-09-11 |
| Air Products komparativni podaci | SEC EDGAR 10-K, CIK 0000002969 | accession 0000002969-25-000055 | pristupljeno 2026-09-11 |
