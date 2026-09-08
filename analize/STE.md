# Analiza: STERIS plc (STE)

**Datum:** 2026-09-08 | **Analitičar:** Dragan | **Cena na dan analize:** 224.59 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — sterilizacija/infekciona kontrola nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

STERIS je dobavljač sterilizacije i infekcione kontrole za bolnice i farmaceutsku/medicinsku industriju, organizovan (posle prodaje Dental segmenta, efektivno maj 2024) u 3 segmenta: Healthcare ($3,878.7M FY2025 prihoda, najveći segment), AST — Applied Sterilization Technologies ($1,038.6M), Life Sciences ($542.3M).

- Izvori prihoda i njihov udeo: Healthcare ~71%, AST ~19%, Life Sciences ~10% (FY2025). Revenue split samo Product vs Service dostupan (Product $2,871.6M / Service $2,587.9M FY2025) — finiji Consumables-vs-Capital-Equipment breakdown nije obelodanjen.
- Ko su kupci: bolnice, farmaceutski i medicinski uređaji proizvođači kojima je potrebna sterilizacija/dekontaminacija.
- Kako se naplaćuje: prodaja opreme (jednokratno) + potrošni materijal/servisni ugovori (ponavljajuće) + AST kontraktne sterilizacione usluge.
- Koncentracija: nema kupca ≥10% prihoda ijednog segmenta (obelodanjeno u 10-K).

**NAPOMENA — samo 4 godine podataka:** FY2021 je isključen iz ove analize jer (a) ne postoji restatovana ex-Dental verzija ni u jednom SEC filing-u i (b) FY2021 ukupan dug nije pouzdano rastavljen na komponente. Standardni 5-godišnji format nije primenjiv — vidi `data/STE.json` za detaljno obrazloženje.

## 2. Moat — dve rečenice (obavezna kapija)

> Bolnice i farmaceutski proizvođači su regulatorno obavezni na sterilizaciju/infekcionu kontrolu (FDA/EPA zahtevi), a STE-ova AST mreža postrojenja i servisni ugovori stvaraju visoke troškove prelaska — promena dobavljača sterilizacionih usluga zahteva regulatornu revalidaciju procesa.
> ROIC ex-goodwill dosledno raste (7.73%→15.10%), pokazujući poboljšanje osnovnog poslovanja nakon Dental problema.

- Kategorija: regulatorna/licencna barijera + troškovi prelaska
- **Šta bi ubilo ovaj moat u 5 godina:** novi tehnologija sterilizacije koja zaobiđe potrebu za AST kontraktnim uslugama ILI bolnice insourcing-uju sterilizaciju
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** regulatorna revalidacija procesa sterilizacije traje godinama; AST mreža postrojenja zahteva kapitalno-intenzivnu izgradnju infrastrukture

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/STE.json`:

```
SCORECARD — STERIS plc (STE) | Podaci: 4 god. (FY2021 iskljucen)

⚠ Samo 4 godine podataka — kapije koje traže 5 godina nisu formalno validne.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 7.1%, WACC 8.3%, spread -1.2% - PAO
G2 ND/EBITDA≤2.5x i pokrivenost≥4x: 1.39x, 10.0x - PROŠAO
G3 FCF pozitivan ≥4/4g: 4/4 - PROŠAO
G4 FCF konverzija≥0.7: 1.11 - PROŠAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 5/6, Palo 1 (G1) - KAPIJA JE PALA

K1 ROIC: medijana 7.1%, trend RASTE (4.1%→7.2%→7.0%→7.8%). WACC 8.3%, spread -1.2%
  (standardni ROIC je ISPOD cene kapitala na medijani).
K1 ROIC EX-GOODWILL (rucno izracunato, goodwill ~45-50% procenjene imovine):
  FY2022 7.73% → FY2023 12.77% → FY2024 12.53% → FY2025 15.10%
  Medijana ex-goodwill: ~12.65%, RASTE, ali NE DOSTIZE docs/05-stil prag za
  medicinske uredjaje (20%+) - slabiji override kandidat od ROP-a.
K2 Marže: bruto 44.6%→44.0% (stabilna), operativna 11.3%→15.9% (RASTE - FY2022 je bila
  losa godina, verovatno tranziciona), neto stabilna ~11%.
K3 Zaduženost: ND/EBITDA 2.66x→1.39x (POBOLJŠAVA SE, verovatno delom Dental proceeds),
  pokrivenost kamata 5.3x-10.0x. Test produktivnosti duga PROLAZI (dug CAGR -12.9% << EBIT
  CAGR 22.0%) - dug realno opada dok EBIT raste.
K4 FCF: pozitivan 4/4, FCF konverzija prosek 1.11 (dobro, iznad praga 0.70).
K5 Valuacija: P/E 37.37. PEG_trailing 1.52 (istorijski EPS CAGR 24.6% - VEROVATNO NADUVAN
  niskom FY2022 baznom godinom, koja je bila tranziciona/losa). PEG_forward 3.81 (konsenzus
  rast 9.8% - realisticniji, MNOGO nizi od trailing). FCF yield na EV 3.2% (najvisi od tri
  zdravstvena kandidata ovog kruga).
```

**Kapije:** prošlo 5/6 | palo 1 (G1) | nepoznato 0
**Override:** Standardni ROIC pada ispod WACC-a (spread -1.2%), delom zbog goodwill-a (~45-50% procenjene imovine, umeren nivo — manji od ROP/TMO/DHR ~50-62%). ROIC ex-goodwill je BOLJI i RASTE (7.73%→15.10%, medijana ~12.65%), što je pozitivan trend SLIČAN ROP-u po SMERU, ali SLABIJI PO NIVOU — medijana ex-goodwill od 12.65% je ispod docs/05-stil praga za medicinske uređaje (20%+) čak i posle isključivanja goodwill-a. Ovo je slabiji override kandidat od ROP-a: kod ROP-a je ex-goodwill ROIC bio jasno iznad sektorskog praga (21.3% medijana), ovde je jasno ispod njega. Dodatna komplikacija: podaci su samo 4 godine, i FY2022 (najniža godina, 7.73% ex-goodwill) je verovatno bila "loša" tranziciona godina (Dental problemi, goodwill impairment u originalnoj prezentaciji) — bez FY2021 kao dodatnog konteksta, teško je proceniti da li je 4.1%-7.8% standardni raspon normalan ili je FY2022 bio anomalno dno.

## 4. Poređenje sa konkurencijom

| Metrika | STE | Boston Scientific (BSX) | Baxter (BAX) | Medijana grane |
|---|---|---|---|---|
| ROIC (medijana za STE; FY2025 za konk.) | 7.1% (ex-goodwill medijana 12.65%) | 9.16% | N/A — FY2025 operativni gubitak, nereprezentativna godina | N/A |
| Bruto marža | 44.0% (FY2025) | 69.0% (FY2025) | 30.1% (FY2025, neuobičajeno nisko) | N/A |
| Operativna marža | 15.9% (FY2025) | 18.0% (FY2025) | -2.7% (FY2025, operativni gubitak) | N/A |
| Neto marža | 10.9% (FY2025) | 14.4% (FY2025) | -8.5% (FY2025, neto gubitak) | N/A |
| Neto dug/EBITDA | 1.39x (FY2025) | 1.90x (FY2025) | 11.2x (FY2025, distresirano izgleda) | N/A |
| P/E | 37.37 | N/A | N/A | N/A |
| PEG (trailing) | 1.52 | N/A | N/A | N/A |
| FCF yield na EV | 3.2% | N/A | N/A | N/A |

*Izvor Boston Scientific: SEC EDGAR 10-K FY2025, CIK 0000885725, accession 0000885725-26-000010 — imenovan konkurent u STE Healthcare segmentu, ali BSX je mnogo šire diversifikovan portfolio (kardiologija, urologija, endoskopija, neuromodulacija) uporediv samo delimično sa STE Healthcare segmentom. Izvor Baxter: CIK 0000010456, accession 0001628280-26-007733 — imenovan konkurent, ali FY2025 pokazuje OPERATIVNI GUBITAK (-2.7% marža) i neto gubitak — jednogodišnji podaci NISU reprezentativni za normalnu godinu, potrebno proveriti FY2023/2024 pre bilo kakvog čvrstog zaključka. Sterigenics International (najbliži pojedinačni AST konkurent) je deo Sotera Health, javno kotirane firme (SHC) — NIJE istražen u ovom prolazu, N/A.*

**Ako marža pada — pada li svima u grani ili samo njoj?** STE marže NE padaju — operativna marža raste (11.3%→15.9%). Nije moguće utvrditi šire sektorske trendove pouzdano jer je Baxter u FY2025 imao anomalno loš rezultat (operativni gubitak, verovatno jednokratni faktori ili restrukturiranje van ovog istraživanja), a Boston Scientific je previše diversifikovan za direktno poređenje sterilization-specifičnog poslovanja.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 1.52 | prošli EPS rast (24.6% CAGR) se nastavlja — VEROVATNO naduvan niskom FY2022 baznom godinom |
| PEG_forward | 3.81 | konsenzus analitičara (9.8% EPS rast) je tačan |
| FCF yield na EV | 3.2% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 3.0% | dilucija je realan trošak (SBC/prihod 1.1%, nisko) |

**Razlika između PEG_trailing i PEG_forward:** VELIKA — 1.52 vs 3.81, više nego duplo. Trailing EPS CAGR od 24.6% je gotovo sigurno artefakt niske FY2022 bazne godine (EPS $3.11 tu godinu, verovatno tranziciona/loša godina pre pune normalizacije posle Dental problema) — CLAUDE.md K5 eksplicitno upozorava na ovaj scenario ("ciklične kompanije na dnu ciklusa"). Konsenzus od 9.8% je verovatno realniji pokazatelj održivog tempa, i PEG_forward od 3.81 (najviši od tri zdravstvena kandidata ovog kruga) pokazuje da akcija NIJE jeftina na održivoj osnovi uprkos naizgled privlačnom PEG_trailing broju.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

1. ROIC ex-goodwill se zaustavi ispod 15% — signal da poboljšanje nije nastavljeno.
2. Neto dug/EBITDA prestane da opada — signal da je poboljšanje bilo jednokratno (Dental proceeds), ne strukturno.
3. FY2026 podaci (kad postanu dostupni sa punijim istorijskim kontekstom) pokažu da je FY2022 (7.73% ex-goodwill) bio tipičan nivo, ne anomalno dno — obarajući "poboljšanje" tezu.

**Šta je najjači argument protiv kupovine ove akcije?** Ceo pozitivan trend (ROIC ex-goodwill raste, ND/EBITDA pada) počiva na samo 4 godine podataka koje počinju odmah posle Dental problema (FY2022 goodwill impairment) — nemamo dovoljno istorijskog konteksta da znamo da li je STE strukturno poboljšao poslovanje ili se jednostavno oporavlja od jednokratnog udarca ka svom normalnom nivou. Plaćaš PEG_forward od 3.81 (najskuplje od tri zdravstvena kandidata) za trend koji možda nije ni pravi trend, samo povratak na srednju vrednost.

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | ROIC ex-goodwill nastavlja da raste | ≥ 15% | 70% |
| 2 | Operativna marža stabilna | ≥ 15% (±1pp) | 70% |
| 3 | Zaduženost ostaje niska | Neto dug/EBITDA < 1.5x | 70% |
| 4 | FCF konverzija ostaje jaka | ≥ 1.0 | 70% |
| 5 | Prihod raste | ≥ 6% god/god | 70% |

## 8. Odluka

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam: ROIC ex-goodwill medijana pređe 18% ILI se dobije FY2021 restatovan podatak za potvrdu pravog 5-godišnjeg trenda
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
| FY2023-2025 income statement | SEC EDGAR 10-K FY2025, CIK 0001757898 | accession 0001757898-25-000005, R5.htm | pristupljeno 2026-09-06, licno verifikovano |
| FY2022 (restatovano) | SEC EDGAR 10-K FY2024, CIK 0001757898 | accession 0001757898-24-000008, R5.htm | pristupljeno 2026-09-06, licno verifikovano |
| Cena zatvaranja STE | IBKR (TradingView chart, NYSE) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-06 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-08 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, cross-check sa marketbeat.com u sličnom rasponu | https://finviz.com/quote.ashx?t=STE | pristupljeno 2026-09-08 |
| Boston Scientific, Baxter komparativni podaci | SEC EDGAR 10-K | accession brojevi navedeni u §4 | pristupljeno 2026-09-08 |
