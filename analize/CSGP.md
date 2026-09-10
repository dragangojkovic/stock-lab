# Analiza: CoStar Group, Inc. (CSGP)

**Datum:** 2026-09-10 | **Analitičar:** Dragan | **Cena na dan analize:** 30.91 (IBKR zaključna, 04.09.2026)
**U krugu kompetencije:** NE — real estate podaci/analitika nije direktno u Draganovom IT/.NET fokusu, iako je B2B SaaS-adjacent.

---

## 1. Šta kompanija zapravo radi

CoStar je online real estate marketplaces, informacije, analitika i 3D digital-twin tehnologija — CoStar Suite, LoopNet, Apartments.com, STR, Ten-X, Homes.com, plus post-2025 Matterport/Domain/Visual Lease. Najveći istraživački odsek u komercijalnim nekretninama (CRE), proprietarna baza podataka izgrađena preko 35 godina.

- Izvori prihoda i njihov udeo: nije detaljno raščlanjeno u dostupnim izvorima za ovaj prolaz — N/A, treba proveriti. FY2025 uveden novi segmentni okvir (proizvod-portfolio umesto geografski).
- Ko su kupci: komercijalne nekretnine profesionalci (brokeri, investitori, upravnici), plus rezidencijalno tržište preko Apartments.com/Homes.com.
- Kako se naplaćuje: pretežno subscription/recurring model za CRE podatke, marketplace naknade za Apartments.com/Homes.com/LoopNet.
- Koncentracija: nema obelodanjivanja koncentracije kupaca u dostupnim izvorima — N/A.

## 2. Moat — dve rečenice (obavezna kapija)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/CSGP.json`:

```
SCORECARD — CoStar Group, Inc. (CSGP) | Podaci: 5 god.

HARD KAPIJE
G1 ROIC ≥12% i spread≥3pp: medijana 6.7%, WACC 7.7%, spread -0.9% - PAO
G2 ND/EBITDA≤2.0x i pokrivenost≥4x: -3.35x, -2.6x - PAO (pokrivenost NEGATIVNA)
G3 FCF pozitivan ≥4/5g: 4/5 - PROŠAO (FY2024 negativan, -186.4M)
G4 FCF konverzija≥0.7: 3.92 - PROŠAO (VARLJIVO, vidi napomenu)
G5 Moat artikulisan: DA - PROŠAO
G6 Nije iskljucen sektor: u redu - PROŠAO
Prošlo 4/6, Palo 2 (G1, G2)

K1 ROIC: medijana 6.7%, trend PADA DRASTICNO (10.9%→12.0%→6.7%→0.1%→-0.2%). WACC 7.7%,
  spread -0.9% (standardni ROIC ISPOD cene kapitala, negativan trend, NE oporavlja se).
K2 Marže: bruto stabilna ~79-82%, operativna 22.2%→-2.2% (KOLABIRALA, NEGATIVNA u FY2025),
  neto 15.0%→0.2% (kolabirala). Uzrok NIJE impairment - S&M skocio $989.9M(FY23)->
  $1,364.3M(FY24)->$1,560.0M(FY25), Homes.com marketinski rat protiv Zillow-a, plus
  akvizicioni troskovi (Matterport, Domain, Visual Lease).
K3 Zaduženost: pokrivenost kamata NEGATIVNA u FY2025 (-2.6x, EBIT negativan). ND/EBITDA
  formalno "dobar" (-3.35x, neto gotovina) ali G2 formalno PADA jer kamate ne mogu
  biti pokrivene negativnim EBIT-om. Test produktivnosti duga PADA.
K4 FCF: FCF konverzija PRIKAZANA kao 3.92 (izgleda odlicno) ALI JE VARLJIVA - FY2025
  FCF/NI=17.57 je ARTEFAKT skoro-nultog NI imenioca ($7.0M neto dobit), ne stvarna snaga.
  FY2024 FCF bio NEGATIVAN (-$186.4M, CapEx skok na $579.0M za Homes.com).
K5 Valuacija: P/E 1545.50 i PEG_forward 42.95 - OBA BESMISLENA (skoro-nula zarada, klasican
  CLAUDE.md K5 slucaj "gde PEG ne radi"). FCF yield na EV svega 1.0%, NAKON SBC NEGATIVAN
  (-0.6%) - najslabiji od svih kandidata u ovom krugu screeninga.
```

**Kapije:** prošlo 4/6 | palo 2 (G1, G2) | nepoznato 0
**Override:** Nema uverljivog override obrazloženja. Za razliku od ROP/TYL (gde je standardni ROIC pao ISKLJUČIVO zbog goodwill dilucije, uz jak i poboljšavajući ex-goodwill trend), CSGP-ov problem je **realno operativno pogoršanje** — EBIT je doslovno negativan u FY2025, ne samo goodwill-om potisnut. Nema smislenog "ex-goodwill" spasa kad je i sam EBIT negativan.

## 4. Poređenje sa konkurencijom

*Konkurentski podaci NISU prikupljeni u ovom prolazu zbog vremenskih ograničenja i jer je nalaz iz §3 (dve kapije padaju, EBIT negativan) dovoljno jasan signal za razmatranje pravca odluke pre dubljeg ulaganja u poređenje. Ako se ipak nastavi puna analiza, MCO/SPGI (već u projektu, "podaci kao IP" logika iz docs/05) bili bi najbliži analogni okvir za "data moat" tezu, iako su u drugačijem sektoru (rejting/finansijski podaci vs real estate).*

**Ako marža pada — pada li svima u grani ili samo njoj?** Nemam podatke o Zillow-u (glavni pomenuti konkurent u Homes.com prostoru) ili drugim CRE data peer-ovima da odgovorim pouzdano. Kvalitativno, S&M rat je INICIRAN od strane CSGP-a (agresivna ekspanzija Homes.com-a) — ovo sugeriše da je pad marže SAMOIZAZVAN strateškom odlukom, ne eksternim pritiskom, ali ovo nije potvrđeno nezavisnim izvorom.

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | -25.99 (BESMISLENO) | prošli EPS rast se nastavlja — ali je EPS CAGR -59.5% (kolaps) |
| PEG_forward | 42.95 (BESMISLENO) | konsenzus analitičara (36.0% EPS rast) je tačan — ali je ovo bazni efekat (EPS blizu nule), ne organski rast |
| FCF yield na EV | 1.0% | ništa — samo tekući cash flow — NAJNIŽI od svih kandidata screenovanih u ovoj sesiji |
| FCF yield nakon SBC | -0.6% (NEGATIVAN) | dilucija je realan trošak — kad se uzme u obzir, CSGP trenutno NE generiše slobodan novčani tok za akcionara |

**Razlika između PEG_trailing i PEG_forward:** Oba su BESMISLENA i ne treba ih koristiti — per CLAUDE.md K5, ovo je klasičan slučaj "gde PEG uopšte ne radi" (zarada blizu nule/negativna). FCF yield (koji ne zavisi od projekcija) je jedini pouzdan signal ovde, i on je najslabiji od svih nedavno analiziranih kandidata — nakon SBC, negativan.

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 8. Odluka

**PREDLOG (nije odluka vlasnika) — vidi poruku u chatu za finalizaciju.**

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| FY2023-2025 income statement | SEC EDGAR 10-K FY2025, CIK 0001057352 | accession 0001057352-26-000020, R3/R4.htm | pristupljeno 2026-09-10, licno verifikovano |
| FY2021-2022 podaci | SEC EDGAR 10-K FY2021/2022, XBRL companyfacts | accession brojevi u data/CSGP.json | pristupljeno 2026-09-10 |
| Cena zatvaranja CSGP | IBKR (TradingView chart, NASDAQ) | screenshot, 04.09.2026 zaključna sveća | 2026-09-10 |
| Cena zatvaranja VUAA (benchmark) | IBKR (TradingView chart, LSEETF) | screenshot, 04.09.2026 zaključna sveća | 2026-09-10 |
| Beta (5g) | stockanalysis.com — TREĆA STRANA, nije SEC izvor | N/A — treba proveriti tačan URL | pristupljeno 2026-09-10 |
| 10Y UST prinos (za WACC) | treasury.gov, Daily Treasury Par Yield Curve Rates | 04.09.2026, 4.78% | pristupljeno 2026-09-10 |
| Konsenzus EPS rast (3-5g) | finviz.com "EPS next 5Y" — TREĆA STRANA, EKSPLICITNO flagovan kao bazni efekat, ne pouzdan | https://finviz.com/quote.ashx?t=CSGP | pristupljeno 2026-09-10 |
