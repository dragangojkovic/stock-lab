# Analiza: Edwards Lifesciences Corporation (EW)

**Datum:** 2026-09-08 | **Analitičar:** Dragan | **Cena na dan analize:** 89.90 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — medicinski uređaji/strukturne bolesti srca nije u Draganovom IT/.NET fokusu.

---

## 1. Šta kompanija zapravo radi

Edwards je lider u lečenju strukturnih bolesti srca — TAVR (transkateterska zamena aortne valvule, SAPIEN platforma, 74% prihoda FY2025), TMTT (transkateterska mitralna/trikuspidalna terapija, PASCAL/EVOQUE/SAPIEN M3, 9% prihoda), Surgical Structural Heart (hirurške valvule, RESILIA tkivo, 17% prihoda). Critical Care (monitoring) segment prodat Becton Dickinson-u (zatvoreno septembar 2023), više nije deo poslovanja.

- Izvori prihoda i njihov udeo: vidi gore — TAVR dominira sa 74% prihoda FY2025.
- Ko su kupci: kardiohirurzi i intervencioni kardiolozi u bolnicama koje izvode strukturne srčane procedure.
- Kako se naplaćuje: prodaja implantabilnih uređaja (jednokratno po proceduri, ali visoko ponavljajuće zbog rastućeg broja procedura godišnje).
- Koncentracija: kompanija eksplicitno navodi da nijedan kupac nije ≥10% prihoda u 2025.

## 2. Moat — dve rečenice (obavezna kapija)

> FDA odobrenje implantabilnih srčanih uređaja je dugotrajan i skup proces, a klinička iskustva/obuka hirurga sa specifičnom platformom (SAPIEN) stvaraju inerciju — promena dobavljača zahteva ponovnu obuku tima i novu kliničku validaciju.
> Tržište je koncentrisano (Edwards/Medtronic/Abbott), a EW i dalje nadmašuje oba diversifikovana konkurenta po operativnoj marži (20.8% vs 17.8%/18.2%) uprkos sopstvenom padu marže.

- Kategorija: regulatorna/licencna barijera + troškovi prelaska (klinička validacija)
- **Šta bi ubilo ovaj moat u 5 godina:** Abbott-ov TMTT portfolio dobije značajniju regulatornu odobrenu ekspanziju i preuzme tržišni udeo ILI cenovni pritisak od bolničkih sistema koji konsoliduju nabavku
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** FDA klinička ispitivanja za nove strukturne srčane platforme traju godinama; hirurška obuka i institucionalno poverenje se grade postepeno, ne kupuju

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/EW.json`:

```
SCORECARD — Edwards Lifesciences Corporation (EW) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 19.0%, WACC 8.5%, spread 10.5% - PROŠAO
G2 ND/EBITDA≤2.5x i pokrivenost≥4x: -1.65x, 62.0x - PROŠAO (neto gotovina)
G3 FCF pozitivan ≥4/5g: 5/5 - PROŠAO
G4 FCF konverzija≥0.7: 0.67 - PAO
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 5/6, Palo 1 (G4) - KAPIJA JE PALA

K1 ROIC: medijana 19.0%, trend PADA DOSLEDNO (26.8%→23.2%→19.0%→16.5%→13.1%). WACC 8.5%,
  spread 10.5% (i dalje komotno pozitivan i na dnu trenda).
K2 Marže: bruto 76.1%→83.8%→78.0% (visoke, ali variraju), operativna 32.3%→20.8% (PADA
  DOSLEDNO), neto marza distorzovana FY2024 anomalijom (76.7% te godine).
K3 Zaduženost: neto gotovina svih 5 godina (ND/EBITDA negativan), pokrivenost kamata 62-92x -
  nema materijalne zaduzenosti. Test produktivnosti duga formalno PADA (dug CAGR 0.1% vs
  EBIT CAGR -7.0%) - ali dug je toliko mali (~$596-598M stabilno) da je ovaj test skoro
  besmislen za prakticno bezdugu kompaniju.
K4 FCF: pozitivan 5/5, FCF konverzija prosek 0.67 (PADA ISPOD PRAGA) - DIREKTNO IZAZVANO
  FY2024 anomalnom neto dobiti ($4,174.6M, ukljucuje ~$3.5mlrd jednokratni dobitak verovatno
  vezan za Critical Care divestituru; sastav nije nezavisno verifikovan). Bez te godine
  (0.94, 0.64, N/A-izuzeta, 1.24 prosek preostalih) bi FCF konverzija bila ~0.94, iznad praga.
K5 Valuacija: P/E 49.13 (NAJSKUPLJE od tri zdravstvena kandidata ovog kruga). PEG_trailing
  NEGATIVAN/besmislen (-7.73, EPS CAGR -6.4% - distorzovano istom FY2024 anomalijom).
  PEG_forward 3.50 (konsenzus rast 14.0% - najvisi konsenzus rast od tri kandidata, ali i dalje
  ne cini PEG jeftinim jer je P/E toliko visok). FCF yield na EV 2.7%.
```

**Kapije:** prošlo 5/6 | palo 1 (G4) | nepoznato 0
**Override:** G4 formalno pada isključivo zbog FY2024 računovodstvene anomalije (jednokratni dobitak naduvava imenilac FCF/NI odnosa tu godinu na 0.07, vukući petogodišnji prosek ispod praga). Bez te distorzije, FCF konverzija bi bila ~0.94 — komotno iznad 0.70. Ovo je legitiman override kandidat SLIČAN WST slučaju (jednokratni/ciklični artefakt, ne strukturni problem kvaliteta zarade). MEĐUTIM — nezavisno od ovog override-a, **ROIC i operativna marža opadaju dosledno svake godine bez izuzetka** (26.8%→13.1% i 32.3%→20.8%), što NIJE računovodstveni artefakt već realan trend koji zaslužuje ozbiljnu pažnju čak i ako se G4 override prihvati.

## 4. Poređenje sa konkurencijom

| Metrika | EW | Medtronic (MDT) | Abbott (ABT) | Medijana grane |
|---|---|---|---|---|
| ROIC (5g med. za EW; najnovija FG za konk.) | 19.0% (FY2025: 13.1%) | 6.75% | 10.98% | N/A |
| Bruto marža | 78.0% (FY2025) | 65.0% | 56.4% | N/A |
| Operativna marža | 20.8% (FY2025) | 17.8% | 18.2% | N/A |
| Neto marža | 17.7% (FY2025) | 13.2% | 14.7% | N/A |
| Neto dug/EBITDA | -1.65x (neto gotovina) | 2.76x | 0.39x | N/A |
| P/E | 49.13 | N/A | N/A | N/A |
| PEG (trailing) | -7.73 (raspao se) | N/A | N/A | N/A |
| FCF yield na EV | 2.7% | N/A | N/A | N/A |

*Izvor Medtronic: SEC EDGAR 10-K (fiskalna godina zavrsava krajem aprila), CIK 0001613103, accession 0001628280-26-044354. Izvor Abbott: CIK 0000001800, accession 0001628280-26-010185. VAŽNA NAPOMENA O UPOREDIVOSTI: I Medtronic I Abbott su MNOGO diversifikovaniji od Edwards-a — Medtronic pokriva Cardiovascular, Neuroscience, Medical Surgical, Diabetes (samo deo Cardiovascular segmenta je uporediv sa EW), Abbott pokriva Nutrition, Diagnostics, Established Pharma, Medical Devices (TMTT-uporediv deo je mali udeo ukupnog biznisa). Konsolidovane marže NISU reprezentativne za njihove strukturne-srce podsegmente specifično.*

**Ako marža pada — pada li svima u grani ili samo njoj?** EW-ova operativna marža (20.8%) i dalje NADMAŠUJE oba diversifikovana konkurenta (17.8% Medtronic, 18.2% Abbott) čak i posle pada, ali TREND je zabrinjavajući — EW je počeo sa mnogo višom maržom (32.3%) i konvergira ka nivou diversifikovanih konkurenata. Pošto Medtronic/Abbott nisu čisti strukturno-srčani igrači, nije moguće utvrditi da li i njihovi uporedivi podsegmenti takođe padaju (makro efekat u TAVR/TMTT tržištu) ili je pad specifičan za EW (npr. gubitak tržišnog udela, cenovni pritisak od Abbott-ovog TMTT portfolija). **Ovo je otvoreno pitanje koje zahteva dalje istraživanje pre odluke.**

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | -7.73 (BESMISLENO) | prošli EPS rast se nastavlja — ali GAAP EPS istorija je distorzovana FY2024 anomalijom |
| PEG_forward | 3.50 | konsenzus analitičara (14.0% EPS rast) je tačan |
| FCF yield na EV | 2.7% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 2.3% | dilucija je realan trošak (SBC/prihod 2.6%, umereno) |

**Razlika između PEG_trailing i PEG_forward:** PEG_trailing je neupotrebljiv (negativan/distorzovan istom FY2024 anomalijom koja utiče na G4). PEG_forward od 3.50 pretpostavlja da će EPS rasti 14.0% godišnje sledeće 3-5 godine — ovo je NAJVIŠI konsenzus rast od sva tri zdravstvena kandidata u ovom krugu (TMO 9.8%, STE 9.8%), ali čak i uz taj optimizam PEG ostaje iznad 3.0 zbog ekstremno visokog P/E (49.13). Per CLAUDE.md §K5, PEG > 40% rasta se "prekomerno blago kažnjava" — konsenzus rast od 14% NIJE u toj kategoriji (nije preko 40%), pa PEG signal ovde ostaje validan i pokazuje da je akcija skupa čak i uz optimistična očekivanja rasta.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

1. Operativna marža nastavi da pada ispod 18% — potvrđuje da je pad strukturan (konkurentski pritisak), ne privremen.
2. ROIC padne ispod 10% dva kvartala zaredom — signal da moat erodira brže nego što cena implicira.
3. Tačan sastav FY2024 jednokratnog dobitka se pokaže kao maskiranje operativne slabosti (npr. poreski trik, ne stvarna dobit od prodaje) — narušava override obrazloženje za G4.

**Šta je najjači argument protiv kupovine ove akcije?** ROIC i operativna marža opadaju dosledno svake godine bez ijednog izuzetka od 2021 (26.8%→13.1% i 32.3%→20.8%) — ovo nije jedna loša godina, ovo je petogodišnji trend. Plaćaš P/E od 49.13 (najskuplje od svih zdravstvenih kandidata u projektu) za kompaniju čiji fundamenti se pogoršavaju iz godine u godinu, oslanjajući se na to da će konsenzus rast od 14.0% preokrenuti taj trend — ali ništa u trenutnim podacima ne potvrđuje da je preokret već počeo.

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | ROIC drži nivo | ≥ 12% | 70% |
| 2 | Operativna marža stabilna | ≥ 19% (±1pp) | 70% |
| 3 | FCF konverzija (bez jednokratnih stavki) | ≥ 0.85 | 70% |
| 4 | Prihod raste | ≥ 8% god/god | 70% |
| 5 | Broj akcija nastavlja da opada | buyback nastavlja | 70% |

## 8. Odluka

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam: operativna marža se stabilizuje ≥ 22% dva kvartala zaredom ILI PEG_forward padne ispod 2.5
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
| FY2022-2025 income statement, balance sheet, cash flow (restatovano continuing ops) | SEC EDGAR 10-K FY2025, CIK 0001099800 | accession 0001099800-26-000009 | pristupljeno 2026-09-06 |
| FY2021 podaci (originalno objavljeno, ukljucuje Critical Care) | SEC EDGAR 10-K FY2021, CIK 0001099800 | accession 0001099800-22-000005 | pristupljeno 2026-09-06 |
| Cena zatvaranja EW | IBKR (TradingView chart, NYSE) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-08 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-06 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-08 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, cross-check sa marketbeat.com u sličnom rasponu | https://finviz.com/quote.ashx?t=EW | pristupljeno 2026-09-08 |
| Medtronic, Abbott komparativni podaci | SEC EDGAR 10-K | accession brojevi navedeni u §4 | pristupljeno 2026-09-08 |
