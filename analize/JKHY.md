# Analiza: Jack Henry & Associates, Inc. (JKHY)

**Datum:** 2026-09-04 | **Analitičar:** Dragan | **Cena na dan analize:** 168.37 (IBKR zaključna, 03.09.2026)
**U krugu kompetencije:** DA — core bankarski/fintech softver je direktno u Draganovom IT/.NET fokusu; verovatno najjači "krug kompetencije" fit od svih kandidata analiziranih u ovom projektu do sada.

> Pravilo: nijedno polje ne ostaje prazno. Ako podatak nije dostupan, upiši
> `N/A — treba proveriti` i navedi šta konkretno treba naći. Prazno polje = nepotpuna
> analiza, a nepotpuna analiza ne ide u portfolio.

---

## 1. Šta kompanija zapravo radi

Jack Henry je core processing softverska firma za banke i credit unions u SAD-u — prodaje i hostuje tri odvojena core bankarska sistema (SilverLake System za banke sa $1-55mlrd aktive, ~13% tržišnog udela u tom segmentu preko 500+ banaka; CIF 20/20 za 200+ banaka; Core Director za manje banke) plus jedan core sistem za credit unions. Servisira preko 7.200 banaka/credit unions/korporativnih entiteta.

- Izvori prihoda i njihov udeo: Services & Support 57% (FY2026, pretežno recurring cloud/hosting/support ugovori), Processing 43% (transakcijski, ali visoko ponavljajući po prirodi obima postojećih klijenata). Manje od 1% prihoda van SAD/Kanade — praktično čisto domaće tržište.
- Ko su kupci: male i srednje američke banke i credit unions — core processing softver je operativno srce banke (obračun računa, transakcije, regulatorno izveštavanje).
- Kako se naplaćuje: dugoročni ugovori — cloud/electronic payment 6-god, on-premise support 1-god (auto-renew), outsourced core processing 6-god sa "per account" fee + minimum guaranteed payments.
- Koncentracija: nema materijalne koncentracije kod jednog klijenta (hiljade malih/srednjih banaka i credit unions). Postoji zavisnost od trećih strana za hardver/tehnologiju (npr. IBM remarketing agreement) — terminacija te veze je pomenuta kao rizik u 10-K.

## 2. Moat — dve rečenice (obavezna kapija)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/JKHY.json`:

```
SCORECARD — Jack Henry & Associates, Inc. (JKHY)
Sektor: Softver - core bankarski/fintech sistemi | Valuta: USD (miliони) | Podaci: 5 god. | Generisano: 2026-09-04

HARD KAPIJE

| # | Kapija | Vrednost | Ishod |
|---|---|---|---|
| G1 | ROIC ≥ 12% (5g medijana) i spread nad WACC ≥ 3pp | medijana 21.8%, WACC 7.3%, spread 14.5% | PROŠAO |
| G2 | Neto dug/EBITDA ≤ 2.0x i pokrivenost kamata ≥ 4x | ND/EBITDA 0.03x, kamate 117.9x | PROŠAO |
| G3 | FCF pozitivan u ≥ 4 od 5 godina | 5 od 5 poznatih | PROŠAO |
| G4 | FCF konverzija (FCF/NI, 5g prosek) ≥ 0.7 | 0.84 | PROŠAO |
| G5 | Moat artikulisan u 2 rečenice | DA | PROŠAO |
| G6 | Nije u isključenom sektoru | u redu | PROŠAO |

Prošlo: 6 | Palo: 0 | Nepoznato: 0 | Nije primenljivo: 0

K1 — ROIC: medijana (5g) 21.8%, trend stabilan (25.2%→19.8%→19.2%→21.8%→23.5%). WACC 7.3%, spread 14.5%.
K2 — Marže: bruto 41.9%→43.7%, operativna 24.4%→22.1%→25.0% (stabilan, blago U-oblik), neto 18.7%→19.8%.
K3 — Zaduženost: Neto dug/EBITDA praktično nula (0.10x→-0.13x→0.03x), pokrivenost kamata 30-200x, D/E 0.00-0.17.
  Test produktivnosti duga: dug CAGR -23.2% (dug OPADA) vs EBIT CAGR 7.6% vs FCF CAGR 12.2% → dug je bio produktivan.
K4 — FCF: pozitivan svih 5 god, FCF konverzija prosek 0.84, OCF/NI prosek 1.37. SBC/prihod 1.3% (nisko, nije dilucioni problem).
  Potraživanja CAGR 0.1% RASTU SPORIJE od prihoda (7.0%) — pozitivan signal kvaliteta zarade.
K5 — Valuacija: P/E 24.12. PEG_trailing 2.67, PEG_forward 2.87 (konsenzus rast 8.4%, blizu trailing 9.0% —
  MALA razlika, za razliku od ZTS/VEEV slučajeva). FCF yield na EV 4.2% (nakon SBC 3.9%).
```

**Kapije:** prošlo 6/6 | palo 0 | nepoznato 0
**Override (ako je kapija pala):** nema — sve kapije prošle formalno čisto.

> Napomena van formalnih kapija: standardni prag G1 (12%) prolazi lako, ali **docs/05 softverski prag (25%+) NIJE dostignut** (21.8% medijana) — JKHY je najbliži od svih softverskih kandidata analiziranih do sada tom pragu, ali formalno ga ne dostiže. Ovo je soft signal za §6, ne kapija koja obara analizu.

## 4. Poređenje sa konkurencijom

| Metrika | JKHY | FIS | Fiserv | Medijana grane |
|---|---|---|---|---|
| ROIC (5g med. za JKHY; FY2025 za konk.) | 21.8% | ~5.1% (FY2025) | ~8.7% (FY2025) | N/A |
| Bruto marža | 43.7% (FY2026) | 36.9% (FY2025) | 59.4% (FY2025) | N/A |
| Operativna marža | 25.0% (FY2026) | 16.3% (FY2025) | 27.5% (FY2025) | N/A |
| Neto marža | 19.8% (FY2026) | 3.6% (FY2025, opterećeno jednokratnom stavkom) | 16.4% (FY2025) | N/A |
| Neto dug/EBITDA | 0.03x (FY2026) | ~3.4x (FY2025) | ~3.1x (FY2025) | N/A |
| FCF konverzija | 0.84 | N/A — treba proveriti | N/A — treba proveriti | N/A |
| P/E | 24.12 | N/A — treba proveriti (tržišna cena nije uzeta iz IBKR-a za konkurenciju) | N/A — treba proveriti | N/A |
| PEG (trailing) | 2.67 | N/A | N/A | N/A |
| FCF yield na EV | 4.2% | N/A — treba proveriti | N/A — treba proveriti | N/A |

*Izvor FIS: SEC EDGAR 10-K FY2025, CIK 0001136893, accession 0001136893-26-000013. Izvor Fiserv: SEC EDGAR 10-K FY2025, CIK 0000798354, accession 0000798354-26-000009. VAŽNA NAPOMENA O UPOREDIVOSTI: FIS i Fiserv NISU čisti core-processing "pure play" konkurenti kao JKHY — Fiserv nosi ~$16.5mlrd "merchant settlement assets/obligations" na bilansu (Clover/merchant acquiring čini ~20%+ prihoda, JKHY to uopšte ne radi), a FIS ima kapital-tržišnu tehnologiju i istoriju velikih akvizicija/divestitura (Worldpay spinoff, -$6.6mlrd gubitak iz obustavljenog poslovanja u 2023). Niži ROIC i veći dug kod obe kompanije delom odražavaju obim/M&A istoriju/mešoviti biznis-model, ne nužno slabiji core-processing posao sam po sebi. Corelation i Finastra (takođe imenovani konkurenti u 10-K) su privatne firme — N/A, nema SEC podataka.*

**Ako marža pada — pada li svima u grani ili samo njoj?** JKHY marže NE padaju u trendu — operativna marža je blago U-oblika (24.4%→22.1%→25.0%) ali završava više nego što je počela. JKHY ima BOLJU operativnu maržu od FIS-a (25.0% vs 16.3%) ali NIŽU od Fiserv-a (25.0% vs 27.5%) — Fiserv-ova viša marža je delom artefakt njegovog merchant-acquiring segmenta koji ima drugačiju ekonomiju obima, ne direktan dokaz boljeg core-processing poslovanja. JKHY drastično nadmašuje obe kompanije po ROIC-u (21.8% vs 5.1%/8.7%) i zaduženosti (ND/EBITDA ~0x vs 3.1-3.4x) — najverovatnije objašnjenje je da JKHY nikad nije radio veliku dugom-finansiranu akviziciju kao FIS (Worldpay) ili nosio strukturni dug kao Fiserv, plus JKHY je fokusiran isključivo na core banking bez kapitalno-intenzivnijih segmenata.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | 2.67 | prošli EPS rast (9.0% CAGR) se nastavlja |
| PEG_forward | 2.87 | konsenzus analitičara (8.4% EPS rast) je tačan |
| FCF yield na EV | 4.2% | ništa — samo tekući cash flow |
| FCF yield nakon SBC | 3.9% | dilucija je realan trošak (ovde manje bitna, SBC/prihod svega 1.3%) |

**Razlika između PEG_trailing i PEG_forward:** MALA — 2.67 vs 2.87, konsenzus (8.4%) je zapravo blago NIŽI od trailing (9.0%), suprotno tipičnom analitičarskom optimizmu. Ovo je neuobičajeno konzervativan/realan konsenzus (za razliku od ZTS-a gde je konsenzus drastično niži od trailing, ili VEEV-a gde je forward optimističniji od trailing) — nema eksplicitnog "ubrzanja koje treba opravdati" ovde, konsenzus praktično potvrđuje nastavak istorijskog tempa. PEG oko 2.7-2.9 spada u CLAUDE.md kategoriju "1.0-2.0 neutralno, >2.0 zahteva eksplicitno obrazloženje zašto se plaća premija" — ovde premija dolazi od kvaliteta (skoro nulti dug, stabilan ROIC 2x veći od WACC-a), ne od očekivanog ubrzanja rasta.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 8. Odluka

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2024-2026 income statement, balance sheet, equity, cash flow | SEC EDGAR 10-K FY2026, CIK 0000779152 | accession 0000779152-26-000067, R2/R3/R4/R5.htm | pristupljeno 2026-09-03 |
| FY2021-2023 podaci | Research agent, unakrsno proveren metodologijom potvrđenom za noviji period | 10-K/XBRL companyconcept, CIK 0000779152 | pristupljeno 2026-09-03 |
| Cena zatvaranja JKHY | IBKR (TradingView chart, NASDAQ) | screenshot, 03.09.2026 zaključna sveća | 2026-09-03 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 03.09.2026 zaključna sveća | 2026-09-03 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-03 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 03.09.2026, 4.77% | pristupljeno 2026-09-04 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, grubo potvrđeno drugim modelskim izvorima (Simply Wall St 6.9%, KoalaGains 7-8%) | https://finviz.com/quote.ashx?t=JKHY | pristupljeno 2026-09-04 |
| FIS FY2025 podaci | SEC EDGAR 10-K, CIK 0001136893 | accession 0001136893-26-000013, R3/R5/R9.htm | pristupljeno 2026-09-04 |
| Fiserv FY2025 podaci | SEC EDGAR 10-K, CIK 0000798354 | accession 0000798354-26-000009, R3/R6/R10.htm | pristupljeno 2026-09-04 |
