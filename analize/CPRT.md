# Analiza: Copart, Inc. (CPRT)

**Datum:** 2026-08-16 | **Analitičar:** Dragan | **Cena na dan analize:** 31,61 USD (zaključna cena 2026-08-14, IBKR)
**U krugu kompetencije:** NE — aukcije/logistika havarisanih vozila nisu Draganov krug kompetencije
(softver/.NET/Microsoft ekosistem). Biran namerno kao **kontrolni test slučaj** (`docs/05` §5) —
očekuje se da sistem "prođe čisto" bez lomljenja metodologije, za razliku od MANH i OTIS.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Copart organizuje online aukcije havarisanih/totaled vozila, uglavnom u ime osiguravajućih
kuća, na svojoj platformi VB3 (Virtual Bidding 3rd Generation, patentirano u SAD 2008).
Ima **281 operativnu lokaciju globalno** (FY2025 10-K, Item 2).

**Poslovni model — agency vs principal:**
- U **SAD, Kanadi, Brazilu, R. Irskoj, Finskoj, U.A.E., Omanu i Bahreinu** — Copart prodaje
  **kao agent** (naknada za aukciju/transakciju, ne uzima vlasništvo nad vozilom).
- U **UK, Nemačkoj i Španiji** — radi i kao agent i **kao principal** (kupuje salvage
  vozila i preprodaje za svoj račun; u UK i preko Green Parts Specialist — prodaja
  rastavljenih delova).
- **Tačan % prihoda po metodi (agency vs principal) NIJE objavljen kao broj u 10-K** —
  N/A, otvoreno pitanje.

**Ko su prodavci vozila (snabdevanje):** pretežno osiguravajuće kuće — **81% ukupnog
broja obrađenih vozila u FY2025** dolazi od osiguravača (10-K, Item 1).

**Koncentracija — potvrđena nulta**, direktan citat (10-K): *"No single customer
accounted for more than 10% of our consolidated revenues for fiscal 2025, 2024, or
2023 and our business does not depend on any particular customer to remain
profitable."*

**Ko su kupci na aukcijama:** licencirani vehicle dismantlers (najveća grupa po
volumenu), rebuilders, repair licensees, used vehicle dealers, exporteri, šira javnost.
Indirektan pokazatelj širine kupovne mreže: u FY2025, **69,8% prodatih vozila u SAD**
(po jedinicama) otišlo je kupcima van države gde se vozilo nalazi (31,0% out-of-state
unutar SAD, 38,8% internacionalnim kupcima).

**Mrežni efekat — kvalitativno opisan, ne kvantifikovan.** 10-K tvrdi da veća virtuelna
aukcijska platforma povećava broj potencijalnih kupaca po prodaji, što diže cenu — ali
**broj registrovanih VB3 članova nije objavljen kao apsolutan broj.** Otvoreno pitanje,
relevantno za §2 moat tezu.

**Geografija (FY2025, Note 14):** 83,0% prihoda SAD segment, 17,0% International.

*Izvor: Form 10-K FY2025 (godina završena 31.07.2025), podnet SEC-u 26.09.2025,
CIK 0000900075, accession 0001628280-25-042946, Item 1, Item 2, Item 7 Note 14.*

---

## 2. Moat — dve rečenice (obavezna kapija)

> CPRT ima dvostrani mrežni efekat (osiguravači ↔ kupci vozila preko VB3 platforme)
> plus 281 lokacije na zemljištu koje je regulatorno teško dobiti (zoning, dozvole za
> skladištenje vozila). RB Global sam u svom 10-K priznaje da su CPRT i IAA praktično
> duopol na tržištu SAD — 69,8% prodatih vozila ide kupcima van matične
> države/zemlje, što potvrđuje širinu mreže.

- Kategorija: mrežni efekat (dvostran) + ekonomija obima/regulatorna barijera (zemljište)
- **Šta bi ubilo ovaj moat u 5 godina:** novi igrač (npr. ACV Auctions) postigne
  uporedivu gustinu kupaca kroz čisto digitalni/bez-fizičkog-skladišta model, ili
  osiguravači počnu sami da prodaju vozila direktno, zaobilazeći CPRT/IAA.
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** dobijanje
  dozvola za stotine velikih parkinga za vozila u različitim jurisdikcijama traje
  godinama (zoning, otpor lokalne zajednice), a gustina kupaca (dismantleri,
  exporteri) se gradi decenijama poverenja u platformu.

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/CPRT.json` (kompletan fajl:
`analize/CPRT-scorecard.md`):

```
SCORECARD — Copart, Inc. (CPRT)
Sektor: Potrošnja/distribucija - aukcije havarisanih vozila | Valuta: USD (hiljade) | Podaci: 5 god.

HARD KAPIJE
G1 (ROIC ≥12% i spread ≥3pp nad WACC):        PROŠAO — medijana 23,5%, WACC 9,2%, spread 14,3pp
G2 (Neto dug/EBITDA ≤3.0x, pokriv. kamata ≥4x): PROŠAO — ND/EBITDA -1,45x (neto gotovina), kamate 840,4x
G3 (FCF pozitivan ≥4/5 god.):                  PROŠAO — 5/5
G4 (FCF konverzija 5g prosek ≥0.7):            PROŠAO — 0,70 (tačno na pragu)
G5 (Moat u 2 rečenice):                        PROŠAO (formalno, čeka Draganovu formulaciju — vidi §2)
G6 (Nije u isključenom sektoru):                PROŠAO

Prošlo: 6/6 | Palo: 0 | Nije primenljivo: 0 — SVE KAPIJE PROŠLE ČISTO, PRVI PUT U OVOM PROJEKTU

K2 (marže): Bruto 45,2% | Operativna 36,5% (stabilna, ali OPADA 42,2%→36,5% kroz 5g) | Neto 33,4%
K3 (zaduženost): ND/EBITDA -1,45x (neto gotovina) | pokrivenost kamata 840,4x | dug CAGR N/A (nema duga na kraju)
K4 (FCF): FCF $1.230,8M (2025) | FCF konverzija prosek 0,70 (granično) | SBC/prihod 0,8% (zanemarljivo)
K5 (valuacija @ 31,61): P/E 19,88 | PEG_trailing 1,51 | FCF yield na EV 4,4% (4,2% nakon SBC)
```

**Kapije:** prošlo 6/6 | palo 0 | nije primenljivo 0 — **prva kompanija u ovom projektu
koja prolazi bez ijedne N/P ili palе kapije.**
**Override (ako je kapija pala):** nema pale kapije.

---

## 4. Poređenje sa konkurencijom

**Ključno ograničenje — Copart nema čist javni konkurentski par sa odvojenim
finansijskim brojevima.** Ovo je *drugačiji* način na koji CPRT "testira sistem" od
onoga što je `docs/05` predvideo (predviđalo je da CPRT prolazi čisto — što jeste
tačno za scorecard, §3) — ali **poređenje konkurencije (K2 pravilo, obavezno 3–5
konkurenata) je ono što se pokazalo neizvodljivim**, ne sama analiza CPRT-a.

**Šta se desilo sa konkurencijom:**
- **IAA, Inc.** (bivši javno listiran, NYSE: IAA) — jedini pravi ravnopravan konkurent.
  Preuzet od strane **RB Global (Ritchie Bros. Auctioneers)** 20.03.2023 (izvor: 8-K,
  RB Global). RB Global 10-K FY2025 eksplicitno navodi: *"In the automotive sector...
  We primarily compete with Copart, Inc."* — potvrđuje **duopol** na tržištu SAD. Ali
  RB Global izveštava kao **jedan jedini operativni segment** (Note, FY2025 10-K,
  direktan citat: *"The Company has one operating and reportable segment"*) — **IAA
  finansijski brojevi (prihod, marža) NE postoje odvojeno od 2023.** N/A, potvrđeno
  ograničenje strukture izveštavanja, ne propust istraživanja.
- **OPENLANE, Inc.** (bivši KAR Auction Services, ticker menja se sa KAR na OPLN od
  26.12.2025) — **NIJE direktan konkurent.** Nakon spinoff-a IAA (2019) i prodaje
  ADESA US fizičkih lokacija Carvani (2022), OPENLANE se fokusira isključivo na
  **wholesale rabljena vozila** (dealer-to-dealer, ne salvage/havarisana). Reč
  "salvage" se ne pominje u opisu njihovog poslovanja. **Isključen iz poređenja.**
- **Manheim (Cox Automotive)** — privatna kompanija, nema javne finansijske izveštaje.
  **N/A, isključen.**

| Metrika | CPRT | RB Global (CELA kompanija, kontaminirano) |
|---|---|---|
| Prihod | $4.647M | $4.590,7M (FY2025) |
| Operativna marža | **36,5%** | ~15,5% (**NIJE uporedivo** — uključuje CC&T industrijsku aukciju i non-salvage automotive, ne samo IAA) |
| Neto marža | **33,4%** | ~9,3% |
| Neto dug/EBITDA | -1,45x (neto gotovina) | Adjusted neto dug/EBITDA 1,4x (ima realan dug $2.471,5M) |

*Izvori: RB Global 10-K FY2025 (godina do 31.12.2025, podneto 25.02.2026, accession
0001628280-26-011682), Item 7 MD&A, Note o segmentima. OPENLANE 10-K FY2025 (podneto
18.02.2026, accession 0001395942-26-000006), Item 1.*

**Zašto ova tabela NE dozvoljava zaključak "CPRT je bolji od konkurencije":** RB
Global-ova marža meša IAA/salvage automotive segment sa CC&T (komercijalna/industrijska
oprema) i non-salvage automotive GTV — to je fundamentalno drugačiji miks poslova, ne
čisto poređenje istog posla. **Jedini legitiman zaključak:** CPRT i IAA (unutar RB
Global) su **duopol** u SAD salvage aukcijama po izjavi samog RB Global-a, ali
kvantitativno poređenje marži na segmentnom nivou trenutno nije izvodljivo iz javnih
izvora. Ovo je granica K2 pravila za ovu specifičnu kompaniju — treba eksplicitno
navesti kao ograničenje, ne zaobići prilagođavanjem metrike.

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **1,51** (P/E 19,88 / EPS CAGR 13,2%) | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen u ovoj sesiji | — |
| FCF yield na EV | **4,4%** | ništa — samo tekući cash flow |
| FCF yield nakon SBC | **4,2%** | SBC zanemarljiv (0,8% prihoda), razlika minimalna |

**Kontrola — da li je rast EPS-a stvaran ili buyback (K5 obavezna provera):**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 14,6% |
| EPS | 13,2% |
| FCF po akciji | **23,0%** |

**Ovo je čist, zdrav nalaz.** EPS CAGR (13,2%) je *ispod* Prihod CAGR (14,6%) —
suprotno crvenoj zastavici koju smo videli kod MANH i OTIS (gde je EPS rastao brže
od prihoda usled buyback-a). Broj akcija je gotovo ravan (CAGR +0,4%, blago RASTE, ne
opada) — rast nije veštački napumpan otkupom. **FCF po akciji raste čak brže od
prihoda (23,0%)** — realan, sve jači generator gotovine, ne finansijski inženjering.

Jedina napomena opreza: **FCF konverzija je tačno na pragu od 0,70** (§3), ne udobno
iznad njega — CapEx (uglavnom kupovina zemljišta za nove "yard" lokacije) raste brzo
i troši veći deo OCF-a nego kod MANH/OTIS. Ovo nije crvena zastavica, ali je
granični slučaj vredan praćenja u predviđanjima (§7).

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. Operativna marža nastavi da pada ispod 30% dva kvartala zaredom (trenutno 36,5%,
   već opada 5 godina).
2. FCF konverzija padne ispod 0,70 (već je tačno na pragu) dva kvartala zaredom.
3. Veliki osiguravač (ili grupa) počne da zaobilazi CPRT/IAA kroz sopstveni digitalni
   kanal prodaje havarisanih vozila.

**Šta je najjači argument protiv kupovine ove akcije?**

Iako scorecard prolazi čisto, operativna marža je na petogodišnjem silaznom trendu
(42,2%→36,5%), a FCF konverzija je tačno na minimalno prihvatljivom pragu — teški
kontinuirani CapEx (kupovina zemljišta) mogao bi da signalizira opadajući prinos na
dodatni kapital. Plaćaš premiju (P/E ~20x) za "čist" duopol čiju maržu ne možemo
potvrditi da li opada zbog konkurencije ili je samo zrelost tržišta — jer IAA brojevi
ne postoje odvojeno da bi se uporedilo.

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | Operativna marža ostaje u opsegu | ≥35%, trenutno 36,5% | 70% |
| 2 | FCF konverzija ostaje | ≥0,70, trenutno tačno 0,70 | 70% |
| 3 | ROIC medijana ostaje | ≥20%, trenutno 23,5% | 70% |
| 4 | Prihod raste | ≥10% god/god, trenutno CAGR 14,6% | 70% |
| 5 | Broj akcija ne raste više od praga | ≤1% god/god, trenutno CAGR +0,4% | 70% |

---

## 8. Odluka (popunjava Dragan)

- [x] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Datum ulaza:** 2026-08-14
**Cena ulaza:** 31,61 USD (zaključna cena, IBKR, 2026-08-14)
**VUAA cena istog dana:** 150,40 USD (zaključna cena, IBKR, 2026-08-14)
**Veličina pozicije:** 1/10 satelita

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu):**
1. Operativna marža nastavi da pada ispod 30% dva kvartala zaredom.
2. FCF konverzija padne ispod 0,70 dva kvartala zaredom.
3. Veliki osiguravač počne da zaobilazi CPRT/IAA kroz sopstveni digitalni kanal.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| CPRT FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R8.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/900075/000162828025042946/ | podnet 26.09.2025 |
| CPRT FY2021-FY2022 finansijski podaci | 10-K FY2022 (acc. 0000900075-22-000050) i 10-K FY2023 (acc. 0000900075-23-000034), krizno provereno preko XBRL companyfacts API | sec.gov/Archives/edgar/data/900075/ | 2022 / 2023 |
| CPRT poslovni opis, agency/principal, koncentracija, konkurencija, lokacije | Form 10-K FY2025, Item 1, Item 2, Item 7 Note 14 | sec.gov/Archives/edgar/data/900075/000162828025042946/cprt-20250731.htm | podnet 26.09.2025 |
| CPRT cena zatvaranja (valuacija) | IBKR TWS, sveća 1D | — | 2026-08-14, close 31.61 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-14, close 150.40 |
| CPRT WACC (9,23%, bottom-up CAPM) | rf: treasury.gov (zvaničan); beta: stockanalysis.com (treća strana); Copart nema duga | treasury.gov, stockanalysis.com/stocks/cprt/statistics | 14-16.08.2026 |
| IAA/RB Global akvizicija status | 8-K RB Global, "Ritchie Bros. Completes Acquisition of IAA" | sec.gov (RB Global CIK 1046102), PR Newswire | zatvoreno 20.03.2023 |
| RB Global FY2025 finansijski podaci (kontaminirano, ne čist IAA) | 10-K FY2025, Item 7 MD&A, Note segmenti | sec.gov/Archives/edgar/data/1046102/000162828026011682/rba-20251231.htm | podnet 25.02.2026 |
| OPENLANE FY2025 status i finansijski podaci (isključen iz poređenja) | 10-K FY2025, Item 1 | sec.gov/Archives/edgar/data/(OPENLANE CIK)/000139594226000006/opln-20251231.htm | podnet 18.02.2026 |
