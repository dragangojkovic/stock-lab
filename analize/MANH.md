# Analiza: Manhattan Associates, Inc. (MANH)

**Datum:** 2026-08-13 | **Analitičar:** Dragan | **Cena na dan analize:** 192.63 USD (zaključna cena 2026-08-12, IBKR)
**U krugu kompetencije:** DELIMIČNO — enterprise softver DA (proizvod, arhitektura, cloud migracija su procenjivi), ali supply chain/WMS domen NE (ne mogu proceniti da li je Manhattan Active bolji od Blue Yonder ili SAP EWM bez domenskog znanja u logistici).

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcija 2 (moat)
> je Draganova finalna formulacija. Sekcije 6, 7, 8 ostaju za Dragana (vidi podelu
> rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Manhattan Associates prodaje softver za upravljanje lancima snabdevanja, zalihama i
omnichannel operacijama — prevashodno **WMS (warehouse management)** i platformu
"Manhattan Active" — kupcima koji su **maloprodavci, veletrgovci, proizvođači i
logistički provajderi** (10-K FY2025, Item 1). Kompanija je u tranziciji od
jednokratne licence ka cloud pretplati (SaaS, "versionless" arhitektura).

**Izvori prihoda i udeo (FY2025, iz 8-K Exhibit 99.1, press release 27.01.2026):**

| Kategorija | FY2025 ($ hilj.) | % prihoda | FY2024 ($ hilj.) | god/god |
|---|---|---|---|---|
| Cloud subscriptions | 408.138 | 37,7% | 337.203 | +21,0% |
| Software license | 14.819 | 1,4% | 15.085 | −1,8% |
| Maintenance | 129.972 | 12,0% | 138.304 | −6,0% |
| Services | 503.044 | 46,5% | 525.517 | −4,3% |
| Hardware | 25.419 | 2,4% | 26.243 | −3,1% |
| **Ukupno** | **1.081.392** | 100% | 1.042.352 | +3,7% |

Napomena: **usluge (services) su najveća kategorija prihoda (46,5%)**, ne cloud
subskripcija — ovo je relevantno za §4 (bruto marža) niže, jer usluge po pravilu
nose nižu maržu od softvera/SaaS-a.

**Ko su kupci:** retail, wholesale, manufacturing, logistika — 10-K ne izdvaja
precizniju raspodelu prihoda po industriji.

**Naplata:** hibridni model — cloud pretplata (rastuća kategorija), preostala
licenca (opada), maintenance (opada), usluge implementacije (najveća, ali opada
god/god poslednje godine — vidi HANDOFF §2, otvoreno pitanje o RPO).

**Koncentracija kupaca** — 10-K, Notes to Financial Statements (Significant
Customers), direktan citat: *"Our top five customers... in the aggregate accounted
for 10%, 12%, and 11% of total revenue for the years ended December 31, 2025, 2024,
and 2023, respectively. No single customer accounted for more than 10% of our total
revenue"* — **niska koncentracija, nema key-customer rizika.**

**Geografija:** internacionalni prihod $373,5M = 35% ukupnog (2025), vs 33% (2024).

*Izvor: Form 10-K FY2025 (godina završena 31.12.2025), podnet SEC-u 04.02.2026,
accession 0001193125-26-037138, Item 1 i Item 7; i 8-K Exhibit 99.1 press release
27.01.2026, accession 0001193125-26-024382.*

---

## 2. Moat — dve rečenice (obavezna kapija)

> MANH je multi-tenant platforma gde svaki novi klijent pojačava ekonomiju obima,
> dok istovremeno pravi izlazak klijenta skupim. Cloud prihod raste dok
> license-model opada — platforma pobeđuje.

- Kategorija: ekonomija obima + switching costs
- **Šta bi ubilo ovaj moat u 5 godina:** veliki klijenti razviju svoja in-house
  rešenja umesto da koriste MANH.
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** godine
  operativnih procesa kod hiljada postojećih klijenata zadovoljnih uslugom se ne
  mogu tek tako izgubiti/preuzeti kapitalom.

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/MANH.json` (kompletan fajl:
`analize/MANH-scorecard.md`):

```
SCORECARD — Manhattan Associates, Inc. (MANH)
Sektor: Supply Chain / Omnichannel Commerce Software | Valuta: USD (hiljade) | Podaci: 5 god.

HARD KAPIJE
G1 (ROIC ≥12% i spread ≥3pp nad WACC):        N/P — inv. kapital 42.198 = 3,9% prihoda, ROIC divergira (medijana 687,4%)
G2 (Neto dug/EBITDA ≤3.0x, pokriv. kamata ≥4x): PROŠAO — ND/EBITDA -0,95x (neto gotovina), kamate N/A (nema finansijskog duga)
G3 (FCF pozitivan ≥4/5 god.):                  PROŠAO — 5/5
G4 (FCF konverzija 5g prosek ≥0.7):            PROŠAO — 1,47
G5 (Moat u 2 rečenice):                        PROŠAO (formalno, čeka Draganovu formulaciju — vidi §2)
G6 (Nije u isključenom sektoru):                PROŠAO

Prošlo: 5 | Palo: 0 | Nije primenljivo: 1

K1-ALT (kapitalno-laka firma): FCF marža 34,6% | FCF marža nakon SBC 24,3%
K2 (marže): Bruto 56,3% | Operativna 25,9% (RASTE, 20,2%→25,9% kroz 5g) | Neto 20,3%
K3 (zaduženost): ND/EBITDA -0,95x | D/E 0,18 | nema finansijskog duga (samo operativni lease)
K4 (FCF): FCF $374,0M (2025) | FCF konverzija prosek 1,47 | SBC/prihod 10,3% ⚠ | rast akcija CAGR -1,3%
K5 (valuacija @ 192,63): P/E 53,51 (GAAP) | PEG_trailing 2,64 | PEG_forward 107,02 (GAAP, vidi napomenu §5) | FCF yield na EV 3,3% (2,3% nakon SBC)
```

**Kapije:** prošlo 5/6 | palo 0 | nije primenljivo 1 (G1 → zamenjeno FCF maržom, ne
računa se kao prošla kapija po pravilu K1-ALT)
**Override (ako je kapija pala):** nema pale kapije.

---

## 4. Poređenje sa konkurencijom

**Napomena o uzorku:** e2open je preuzet od strane WiseTech Global (transakcija
zatvorena 03.08.2025, $3,30/akciju keš) i delistovan sa NYSE — ne objavljuje više
samostalne javne finansijske izveštaje, pa je **isključen iz tabele** (nije
primenjivo za poređenje). Blue Yonder (privatna, Panasonic), SAP EWM i Oracle WMS
**nemaju izdvojene javne finansijske izveštaje** (privatna kompanija / segmenti
unutar većih firmi) — ograničenje strukture izveštavanja, ne propust istraživanja.

| Metrika | MANH | DSGX (Descartes) | KXS (Kinaxis) | SPSC (SPS Commerce) | Medijana grane |
|---|---|---|---|---|---|
| ROIC (5g med.) | 687,4% (N/P — kapitalno-laka firma, vidi K1-ALT) | N/A — treba proveriti (van obima ovog istraživanja) | N/A — treba proveriti | N/A — treba proveriti | — |
| Bruto marža | **56,3%** | 77,1% | 64,7% | 69,2% | 69,2% |
| Operativna marža | **25,9%** | 28,8% (GAAP) | 14,5% (IFRS) | 15,7% (GAAP) | 15,7% |
| Neto marža | **20,3%** | 22,5% | 12,9% | 12,4% | 12,9% |
| Neto dug/EBITDA | -0,95x (neto gotovina) | neto gotovina ($356,5M) | neto gotovina (~$324,7M) | neto gotovina ($151,4M) | — (sve neto gotovina) |
| FCF konverzija | **1,47** | 1,59 | 1,59 | 1,63 | 1,59 |
| P/E (trailing, poslednji FY EPS) | 53,51 (@192,63) | ≈41,0x (@$76,62) | ≈50,8x (@~$124,4 USD, FX orijentacioni) | ≈45,5x (@$112,00) | 45,5x |
| PEG (trailing) | **2,64** | N/A — treba proveriti | N/A — treba proveriti | N/A — treba proveriti | — |
| FCF yield na EV | **3,3%** | N/A — treba proveriti (EV nije prikupljen) | N/A — treba proveriti | N/A — treba proveriti | — |

*Fiskalne godine: MANH FY2025 (do 31.12.2025); DSGX FY26 (do 31.1.2026, izvor: 8-K
Exhibit 99.1, 11.03.2026); KXS FY2025 (do 31.12.2025, izvor: press release
04.03.2026, IFRS, izveštava u USD); SPSC FY2025 (do 31.12.2025, izvor: press
release 12.02.2026). Cene akcija konkurenata i implicirani P/E su tržišni kvot na
13.08.2026 (orijentacioni, ne iz izveštaja) — obeleženo gde je relevantno. KXS cena
je konvertovana iz CAD orijentacionim kursom — nije precizna.*

**Ključni nalaz — bruto marža:** MANH ima **strukturno nižu bruto maržu** (56,3%)
od sve tri poređene firme (64,7%–77,1%). Razlog je verovatno mix prihoda: usluge
(services) čine 46,5% prihoda MANH-a (§1) i po pravilu nose nižu maržu od
pretplate/softvera koji dominira kod DSGX/KXS/SPSC. **Ovo nije pad marže god/god
(marža MANH-a raste), nego strukturna razlika u poslovnom modelu — nije nužno
crvena zastavica, ali objašnjava zašto MANH "izgleda" manje profitabilno na bruto
nivou uz uporedivu ili bolju operativnu maržu.**

**Provera hipoteze (istraživanje 2026-08-14):** udeo usluga/implementacije u
prihodu kod konkurencije — DSGX 7% (Professional services, izvor: 8-K Ex-99.1
11.03.2026), SPSC 4,5% (One-time revenues, izvor: 10-K FY2025, Note C — Revenue),
KXS ~28–34% (Professional services + license + maintenance zbirno, izvor: press
release 04.03.2026, FY split po stavkama nije objavljen). Redosled udela usluga
(DSGX 7% < SPSC 4,5%... KXS ~30% < MANH 46,5%) generalno prati inverzni redosled
bruto marže (DSGX 77% > SPSC 69% > KXS 65% > MANH 56%), sa izuzetkom što SPSC ima
manji udeo usluga od DSGX ali i nižu maržu — **mix objašnjava deo gap-a, ne sav.**
Nijedna od četiri firme ne objavljuje bruto maržu po kategoriji prihoda (samo
blendovanu), pa se ne može razdvojiti "MANH ima više usluga" od "MANH ima nižu
maržu i unutar cloud/softver dela samog po sebi" — **N/A, otvoreno pitanje.**

**Operativna marža:** MANH (25,9%) je iznad KXS (14,5%) i SPSC (15,7%), ispod DSGX
(28,8%). Nije generalni pad u grani — svaka firma ima svoju trajektoriju
(KXS operativna marža je skočila sa 2,6%→14,5% god/god, jednokratni skok koji treba
istražiti pre poređenja).

**FCF konverzija:** MANH (1,47) je najniža u grupi (1,59–1,63), ali sve četiri su
znatno iznad praga 0,70 — nije diferencijator u ovom uzorku.

---

## 5. Valuacija — dve nezavisne provere

**Ispravka (2026-08-13):** raniji broj `consensus_eps_growth_3y = 5,9%` je uklonjen
— nije imao naveden izvor u `data/MANH.json` (kršenje pravila "bez izvora ne ulazi
u scorecard"). Istraživanjem je potvrđeno da nije postojao imenovan primarni ni
agregatorski izvor za taj konkretan broj. Zamenjen je verifikovanim, sourced brojem
— vidi napomena ispod.

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **2,64** (P/E 53,51 GAAP / EPS CAGR 20,3% GAAP) | prošli rast (buyback + operativni leverage) se nastavlja |
| PEG_forward (GAAP, iz scorecard-a) | **107,02** (P/E 53,51 GAAP / FY2026 GAAP EPS guidance rast 0,5%) | GAAP EPS guidance za FY2026 je realan — a on je gotovo ravan |
| PEG_forward (Adjusted, ručni kontrolni izračun — NIJE iz scorecard.py) | **4,48** (Adjusted P/E 38,07 / FY2026 Adjusted EPS guidance rast 8,5%) | Adjusted (non-GAAP) EPS je relevantnija baza za rast |
| FCF yield na EV | **3,3%** | ništa — samo tekući cash flow |
| FCF yield nakon SBC | **2,3%** | dilacija (SBC) je realan trošak akcionara |

**Šta se stvarno desilo (potvrđeno iz 8-K Exhibit 99.1, 27.01.2026 i 28.07.2026):**
MANH ima veliki, konzistentan gap između GAAP i Adjusted (non-GAAP) EPS-a, gonjen
uglavnom stock-based compensation-om (~$1,71/akciju razlike):

| | GAAP diluted EPS | Adjusted (non-GAAP) diluted EPS |
|---|---|---|
| FY2025 actual | $3,60 | **$5,06** |
| FY2024 actual | $3,51 | $4,72 |
| FY2026 guidance (posle Q2, 28.07.2026) | $3,59–$3,65 (+0–1%) | **$5,44–$5,50 (+8–9%)** |

GAAP EPS je guidovan da **gotovo stagnira** u FY2026 (SBC i restructuring troškovi
jedu rast), dok Adjusted EPS raste solidno (+8–9%). Naš P/E (53,51) je računat na
GAAP EPS-u, pa je interno konzistentno da PEG_forward na GAAP osnovi ispadne
ekstremno visok (107,02) — to je **istinit nalaz**, ne greška: govori da akcija na
GAAP osnovi praktično nema merljiv forward rast na koji PEG može da se osloni.

Adjusted-osnova (P/E 38,07 / rast 8,5% = PEG 4,48) daje umerenije, ali i dalje
iznad praga od 2,0, sliku. **Koja osnova je relevantnija zavisi od toga koliko SBC
tretiraš kao realan trošak akcionara** — CLAUDE.md K4 stav je da SBC JESTE realan
trošak kroz dilaciju, što ide u prilog GAAP tumačenju (i time bliže PEG 107, ne 4,48).
FCF yield na EV (3,3%, ne zavisi od projekcija) ostaje najpouzdanija kontrola i slaže
se sa "PEG je ovde slomljen" zaključkom — cena implicira mnogo veći rast nego što ga
FCF trenutno pokazuje.

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. Ako cloud rast padne ispod 15% dva kvartala zaredom.
2. Ako se u earnings call transkriptu ili 10-K otkrije da je prosečno trajanje
   novih ugovora produženo (npr. sa 3 na 5 godina) — RPO rast od 25% bi bio
   optička iluzija, ne stvaran signal budućeg prihoda.
3. Ako usluge (Services) nastave da opadaju brže od −5% god/god dva kvartala
   zaredom BEZ odgovarajuće akceleracije cloud rasta iznad 20% — znak da MANH
   gubi ukupan posao, ne da se transformiše ka cloud-u.

**Šta je najjači argument protiv kupovine ove akcije?**

Rast prihoda je kolabirao sa 21% (2023) na 3,7% (2025), a najveća linija prihoda
(Services, 46,5%) opada 4,3% god/god — kompanija maskira usporavanje rastućom
operativnom maržom koja delom dolazi od smanjenja troškova, ne od jačanja
poslovanja. Cena implicira rast koji brojevi ne podržavaju: FCF yield na EV je
samo 3,3% (2,3% nakon SBC), a na GAAP osnovi EPS praktično stagnira u 2026
guidance-u — plaćaš 53x zarade za posao koji raste ispod 1% na osnovi koja
stvarno stiže akcionaru. RPO rast od 25% je jedini "dokaz" budućeg rasta, ali
niko nije potvrdio da to nije samo produženje trajanja ugovora — ako se pokaže
da jeste, cela teza o zaključavanju klijenata gubi merljivu podlogu i ostaje
samo skupa akcija sa usporenim rastom.

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | Cloud subscriptions rast ostaje ≥15% god/god | ≥15%, trenutno 21% | 70% |
| 2 | Operativna marža ostaje u opsegu | ≥24% (±1pp), trenutno 25,9% | 70% |
| 3 | FCF marža nakon SBC ostaje | ≥20%, trenutno 24,3% | 70% |
| 4 | SBC/Prihod ne prelazi prag | ≤12%, trenutno 10,3% | 70% |
| 5 | Ukupan prihod raste | ≥5% god/god, trenutno 3,7% | 70% |

---

## 8. Odluka (popunjava Dragan)

- [x] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Datum ulaza:** 2026-08-13
**Cena ulaza:** 200,92 USD (zaključna cena, IBKR, 2026-08-13)
**VUAA cena istog dana:** 150,40 USD (zaključna cena, IBKR, 2026-08-13)
**Veličina pozicije:** 1/10 satelita

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu):**
1. Cloud rast padne ispod 15% dva kvartala zaredom (kill-switch iz §6).
2. Potvrđeno (iz earnings call transkripta ili 10-K) da je RPO rast objašnjen
   produženjem trajanja ugovora, ne stvarnim nakupljanjem budućeg posla.
3. Services prihod opada brže od −5% god/god dva kvartala zaredom BEZ
   akceleracije cloud rasta iznad 20%.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| MANH FY2021–FY2025 finansijski podaci | 8-K Exhibit 99.1 press release-i (Q4 2022, Q4 2023, Q4 2025) | vidi `data/MANH.json` `_izvori` | 02.02.2023 / 30.01.2024 / 27.01.2026 |
| MANH revenue mix po kategoriji (cloud/license/maint./services/hw) | 8-K Exhibit 99.1, "Manhattan Associates Reports Fourth Quarter Results" | sec.gov, accession 0001193125-26-024382 | 27.01.2026 |
| MANH poslovni opis, kupci, koncentracija | Form 10-K FY2025, Item 1 i Item 7 (MD&A), Notes (Significant Customers) | sec.gov/Archives/edgar/data/1056696/000119312526037138/manh-20251231.htm | podnet 04.02.2026 |
| MANH cena za valuaciju (§5, K5 scorecard) | IBKR TWS, sveća 1D | — | 2026-08-12, close 192.63 |
| VUAA cena istog dana (za valuaciju) | IBKR TWS, sveća 1D | — | 2026-08-12, close 149.56 |
| MANH cena ulaza u paper portfolio (§8, positions.csv) | IBKR TWS, sveća 1D | — | 2026-08-13, close 200.92 |
| VUAA cena istog dana (benchmark ulaza, positions.csv) | IBKR TWS, sveća 1D | — | 2026-08-13, close 150.40 |
| MANH WACC procena (10,68%) | GuruFocus, treća strana, NIJE Claude-ov izračun | — | mart 2026 (procena) |
| MANH guidance FY2026 GAAP EPS | `data/MANH.json` napomena `_guidance_fy2026` (izvor: jan. 2026 guidance, nije dalje verifikovan u ovoj sesiji) | — | jan. 2026 |
| DSGX FY26 finansijski podaci | 8-K Exhibit 99.1, "Descartes Announces Fiscal 2026 Fourth Quarter and Annual Financial Results" | sec.gov/Archives/edgar/data/1050140/000092963826000965/exhibit99-1.htm | 11.03.2026 |
| KXS FY2025 finansijski podaci | Press release "Kinaxis Inc. Reports Record Fourth Quarter 2025 Results" | kinaxis.com/en/news/press-releases/2026/ | 04.03.2026 |
| SPSC FY2025 finansijski podaci | Press release "SPS Commerce Reports Fourth Quarter and Fiscal Year 2025 Financial Results" | globenewswire.com/news-release/2026/02/12/3237661/ | 12.02.2026 |
| e2open status (preuzeta, delistovana) | WiseTech Global / e2open press release-i + SEC 8-K | sec.gov/Archives/edgar/data/1800347/000119312525126316/d924933dex991.htm | dogovor 25.05.2025, zatvoreno 03.08.2025 |
| Konkurentske cene akcija (DSGX/KXS/SPSC) — orijentacione, ne primarni izvor | tržišni kvot (web) | — | 13.08.2026 |
