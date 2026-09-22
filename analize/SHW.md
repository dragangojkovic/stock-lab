# Analiza: The Sherwin-Williams Company (SHW)

**Datum:** 2026-09-11 | **Analitičar:** Dragan | **Cena na dan analize:** 333.71 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — boje/premazi/maloprodaja nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

Sherwin-Williams proizvodi i distribuira boje i premaze kroz 3 segmenta: Paint Stores Group (preko 5,000 sopstvenih specijalizovanih prodavnica US/Kanada/Karibi, direktna prodaja profesionalnim majstorima/kontraktorima i DIY kupcima), Consumer Brands Group (brendirani/private-label boje kroz treće-strane retailere), Performance Coatings Group (industrijski/OEM/protective&marine premazi kroz distributere).

- Izvori prihoda i njihov udeo: nije detaljno raščlanjeno po segmentima u dostupnim izvorima — N/A, treba proveriti tačan %.
- Ko su kupci: profesionalni majstori/kontraktori (Paint Stores Group), DIY potrošači, treće-strane retaileri, industrijski/OEM klijenti.
- Kako se naplaćuje: prodaja proizvoda u sopstvenim/partnerskim prodavnicama, jednokratno po transakciji ali visoko ponavljajuće (bojenje je periodičan posao).
- Koncentracija: "No individual customer accounted for sales totaling more than ten percent" (FY2025) — nema materijalne koncentracije.

## 2. Moat — dve rečenice (obavezna kapija)

> Mreža od preko 5,000 sopstvenih prodavnica direktno opslužuje profesionalne majstore/kontraktore sa savetodavnom prodajom i lokalnom zalihom, stvarajući lojalnost baziranu na pouzdanosti/dostupnosti koju DIY-fokusirani konkurenti (Home Depot/Lowe's private-label) teško repliciraju za profesionalni segment.
> Brend ima cenovnu moć u premium segmentu, potvrđenu najboljom bruto maržom (48.8%) od sva tri poređena materijala kandidata.

- Kategorija: distribuciona gustina/kontrola kanala + brend
- **Šta bi ubilo ovaj moat u 5 godina:** online B2B distribucija farbe direktno kontraktorima (zaobilazeći fizičke prodavnice) postane dovoljno pouzdana i brza
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** izgradnja mreže od 5,000+ prodavnica sa lokalnom zalihom i odnosima sa lokalnim kontraktorima je decenijski poduhvat, ne kapitalni izdatak koji se brzo duplira

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/SHW.json`:

```
SCORECARD — The Sherwin-Williams Company (SHW) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 16.9%, WACC 8.8%, spread 8.1% - PROŠAO
G2 ND/EBITDA≤3.0x i pokrivenost≥4x: 2.84x, 8.2x - PROŠAO
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 0.91 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 6/6, Palo 0 - SVE KAPIJE PROLAZE CISTO

K1 ROIC: medijana 16.9%, trend RASTE (15.4%→15.3%→18.0%→18.8%→16.9%). WACC 8.8%, spread
  8.1% - najveci od tri materijala kandidata.
K2 Marže: bruto 42.8%→48.8%, operativna 12.8%→16.2% (RASTE), neto 9.3%→10.9% (RASTE).
K3 Zaduženost: ND/EBITDA 3.62x(FY21)→2.84x(FY25, POBOLJŠAVA SE), pokrivenost kamata
  7.6x→8.2x. D/E VEOMA VISOK (2.81-4.72x) zbog tankog equity-ja (posledica buyback-a,
  ne dug problem) - NIJE pokazatelj distresa jer je pokrivenost kamata stabilna.
  Test produktivnosti duga PROLAZI (dug CAGR 3.0% << EBIT CAGR 10.5%).
K4 FCF: pozitivan 5/5, FCF konverzija prosek 0.91 (dobro), OCF/NI prosek 1.23.
K5 Valuacija: P/E 32.53. PEG_forward 3.35 (konsenzus rast 9.72%, blizu trailing EPS
  CAGR 10.1% - mali jaz, konzistentno). FCF yield na EV 2.76% (najvisi od tri kandidata).
```

**Kapije:** prošlo 6/6 | palo 0 | nepoznato 0
**Override:** Nije potreban — sve kapije prolaze formalno čisto. Jedina napomena je metodološka: EBIT je ručno izračunat iz linija izveštaja (SHW nema eksplicitan "operating income" podzbir na licu izveštaja), provereno da se tačno poklapa sa objavljenim "Income before taxes" za svaku godinu.

## 4. Poređenje sa konkurencijom

| Metrika | SHW | PPG Industries (PPG) | RPM International (RPM) | Medijana grane |
|---|---|---|---|---|
| ROIC (5g med. za SHW; FY najnovija za konk.) | 16.9% (FY2025: 16.9%) | 15.86% | 11.95% | N/A |
| Bruto marža | 48.8% (FY2025) | 41.3% (FY2025) | 41.4% (FY2026*) | N/A |
| Operativna marža | 16.2% (FY2025) | 16.8% (FY2025, procenjeno iz linija) | 11.0% (FY2026*) | N/A |
| Neto marža | 10.9% (FY2025) | 9.9% (FY2025) | 8.4% (FY2026*) | N/A |
| Neto dug/EBITDA | 2.84x (FY2025) | ~1.6x (FY2025) | ~2.05x (FY2026*) | N/A |
| P/E | 32.53 | N/A | N/A | N/A |
| FCF yield na EV | 2.76% | N/A | N/A | N/A |

*RPM fiskalna godina završava 31.5, "FY2026" = godina završena 31.5.2026.

*Izvor PPG: SEC EDGAR 10-K FY2025, CIK 0000079879, accession 0000079879-26-000046 — EBIT nije direktno XBRL-tagovan u FY2025 filing-u, izračunat kao Revenue-COGS-SG&A-R&D (metodologija transparentna, ne agregatorska procena). Izvor RPM: CIK 0000110621, accession 0001193125-26-312142. SHW ima BOLJU bruto maržu od oba direktna konkurenta (48.8% vs 41.3%/41.4%) — verovatno zbog kontrole distribucije kroz sopstvene prodavnice (Direct-to-professional model bez marže posrednika). ROIC SHW (16.9%) je uporediv sa PPG-om (15.86%) i bolji od RPM-a (11.95%).*

**Ako marža pada — pada li svima u grani ini samo njoj?** SHW marže NE padaju — dosledno rastu (operativna 12.8%→16.2%). SHW ima najbolju bruto maržu od tri kompanije u tabeli, potvrđujući da model sopstvenih prodavnica (direktna distribucija profesionalcima) generiše strukturnu prednost naspram konkurenata koji prodaju kroz treće-strane distributere/retailere.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | N/A (nije eksplicitno računat, EPS CAGR 10.1%) | prošli EPS rast se nastavlja |
| PEG_forward | 3.35 | konsenzus analitičara (9.72% EPS rast) je tačan |
| FCF yield na EV | 2.76% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 2.63% | dilucija je realan trošak (ovde nebitna, SBC/prihod 0.5%) |

**Razlika između PEG_trailing i PEG_forward:** Mala — konsenzus (9.72%) je blizu trailing EPS CAGR-a (10.1%), konzistentno bez drastičnog jaza. SHW ima najviši FCF yield (2.76%) od tri materijala kandidata — najatraktivnija forecast-free valuacija od LIN/ECL/SHW, uz najčistiji scorecard profil.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

1. Broj prodavnica prestane da raste ili počne da opada — signal gubitka tržišnog udela profesionalnom segmentu.
2. Operativna marža padne ispod 15% dva kvartala zaredom — prekid dosledno rastućeg trenda.
3. D/E nastavi da raste dok equity/imovina odnos ostane ispod 15% — signal da "tanak equity" postaje strukturan rizik, ne samo posledica buyback-a.

**Šta je najjači argument protiv kupovine ove akcije?** D/E od preko 2.8x i equity koji je bio ispod 12% ukupne imovine u FY2021 pokazuju da je kompanija strukturno agresivna sa finansijskim inženjeringom (buyback) — ako se ikad pojavi recesija u građevinskom/renovacionom ciklusu istovremeno sa potrebom refinansiranja duga po višim stopama, tanka equity baza daje mnogo manje prostora za apsorpciju šoka nego kod kompanija sa konzervativnijim bilansom.

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | ROIC ostaje visok | ≥ 15% | 70% |
| 2 | Operativna marža stabilna | ≥ 15% (±1pp) | 70% |
| 3 | Zaduženost ostaje umerena | Neto dug/EBITDA < 3.0x | 70% |
| 4 | FCF konverzija ostaje jaka | ≥ 0.85 | 70% |
| 5 | Broj prodavnica nastavlja da raste | god/god pozitivan | 70% |

## 8. Odluka

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam: bilo koja postojeća pozicija ispadne (izlazno pravilo aktivirano) ILI se odluči povećanje broja pozicija van 8-12 raspona
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
| FY2025 income statement | SEC EDGAR 10-K FY2025, CIK 0000089800 | accession 0000089800-26-000008, R3.htm | pristupljeno 2026-09-11, licno verifikovano |
| FY2021-2024 podaci | SEC EDGAR 10-K FY2021-2024 | accession brojevi u data/SHW.json | pristupljeno 2026-09-11 |
| Cena zatvaranja SHW | IBKR (TradingView chart, NYSE) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-11 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-11 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-11 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA | https://finviz.com/quote.ashx?t=SHW | pristupljeno 2026-09-11 |
| PPG, RPM komparativni podaci | SEC EDGAR 10-K | accession brojevi navedeni u §4 | pristupljeno 2026-09-11 |
