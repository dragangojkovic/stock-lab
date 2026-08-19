# Analiza: IREN Ltd (IREN)

**Datum:** 2026-08-19 | **Analitičar:** Dragan | **Cena na dan analize:** 44,90 USD (zaključna cena 2026-08-17, IBKR)
**U krugu kompetencije:** DELIMIČNO — infrastruktura/data centri za AI su blizu Draganovog
IT/softverskog kruga kompetencije, ali bitcoin mining ekonomija (hashrate, difficulty,
halving) i energetski ugovori nisu.

> ⚠ **IZUZETAK OD METODOLOGIJE — eksplicitno tražen od vlasnika (2026-08-18), ne
> podrazumevan.** IREN ima samo **4 fiskalne godine** javne istorije (IPO 2021, prve
> 20-F/10-K FY2022–FY2025), ne 5, i promenila je poslovni model usred perioda
> (bitcoin mining → AI/HPC data centri, promena imena "Iris Energy"→"IREN" nov.
> 2024). Po CLAUDE.md §4 ovo bi trebalo da znači "čekaj". Analiza je urađena na
> izričit zahtev, sa ovim ograničenjem transparentno dokumentovanim, ne sakrivenim.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

IREN (ranije "Iris Energy Ltd") je počela kao čista **bitcoin mining** kompanija, i
tek od FY2024 dodaje **AI Cloud Services** (GPU cloud za HPC/AI treniranje) kao novu
liniju posla. Prihod FY2025: $484,6M bitcoin mining (96,7%) + $16,4M AI Cloud (3,3%)
= $501,0M ukupno. AI Cloud je porastao sa $3,1M (FY2024) na $16,4M (FY2025), ali je
i dalje mali deo poslovanja — **track record novog posla je manji od 2 godine.**

**Infrastruktura (izvor: 10-K FY2025, Item 1/2):** Childress, Teksas — ~650MW
operativno. U razvoju: Sweetwater 1 (1.400MW) i Sweetwater 2 (600MW), ~40 milja od
Abilene, TX — plaćeni depoziti za priključak preko $25M kombinovano.

**Konvertibilne obveznice (ključno za K3, izvor: 10-K FY2025, Napomena 18):**
- **2030 Notes:** $440M nominalno (izdato dec. 2024), kupon 3,25%, konverzija ≈
  $16,81/akciju
- **2029 Notes:** $550M nominalno (izdato jun 2025), kupon 3,50%, konverzija ≈
  $13,64/akciju
- Uz obe serije: **Capped Call** i **Prepaid Forward Contract** ugovori (standardni
  instrumenti da se ograniči dilucija pri konverziji) — objašnjavaju "Financial
  assets/Derivative assets" od $339,5M na bilansu, koji **NISU** investicija u treću
  stranu, već strukturni pratioci ovog duga.

**Koncentracija kupaca:**
- Bitcoin mining: 97% prihoda (FY2025) kroz samo **3 mining pool operatora** —
  visoka koncentracija, ali to je normalno za industriju (mining pools su
  standardni kanal, ne pojedinačni kupci u klasičnom smislu).
- AI Cloud Services: 10-K priznaje "significant customer concentration" kao rizik,
  ali **ne objavljuje konkretan procenat ni imena kupaca.** N/A, otvoreno pitanje.

**Konkurencija — imenovana u 10-K (Item 1, "Competition"):**
- Cloud provideri: AWS, CoreWeave, Crusoe Cloud, Google Cloud, Lambda, Microsoft
  Azure, Nebius, Oracle Cloud
- Colocation provideri: Digital Realty, QTS, CyrusOne, Equinix, Vantage Data
  Centers, Aligned Data Centers

**Dividende/buyback:** Nema. Kompanija **masovno emituje nove akcije** (ATM/
committed equity facility: $731,7M FY2024, $601,8M FY2025) za finansiranje CapEx-a —
suprotno od buyback-a. Broj akcija porastao ~445% u 3 godine (40,9M→223,2M na kraju
FY2025; treća strana navodi već 357,4M akcija sredinom avgusta 2026 — dilucija
se nastavlja i posle FY2025).

*Izvor: Form 10-K FY2025 (godina završena 30.06.2025), CIK 0001878848, accession
0001878848-25-000063, Item 1, Item 1A, Item 2, Napomena 18.*

---

## 2. Moat — dve rečenice (obavezna kapija)

*(popunjava Dragan)*

- Kategorija: *(popuni)*
- **Šta bi ubilo ovaj moat u 5 godina:** *(popuni)*
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** *(popuni)*

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/IREN.json` (kompletan fajl:
`analize/IREN-scorecard.md`):

```
SCORECARD — IREN Ltd (IREN)
Sektor: Bitcoin mining / AI-HPC data centri (hibridni) | Valuta: USD (hiljade) | Podaci: 4 god.
⚠ Samo 4 godine podataka — kapije koje traže 5 godina nisu validne.

HARD KAPIJE
G1 (ROIC ≥12% i spread ≥3pp nad WACC):        PAO — medijana -2,2%, WACC 22,1%, spread -24,3pp
G2 (Neto dug/EBITDA ≤3.0x, pokriv. kamata ≥4x): PAO — ND/EBITDA 2,01x, kamate 1,6x
G3 (FCF pozitivan ≥4/5 god.):                  PAO — 0 od 4 poznatih (sve negativne)
G4 (FCF konverzija 5g prosek ≥0.7):            PROŠAO — 0,78 (STATISTIČKI ARTEFAKT, vidi §5)
G5 (Moat u 2 rečenice):                        PROŠAO (formalno, čeka Draganovu formulaciju — vidi §2)
G6 (Nije u isključenom sektoru):                PROŠAO

Prošlo: 3/6 | Palo: 3 — NAJVIŠE PALIH KAPIJA OD SVIH KOMPANIJA U OVOM PROJEKTU

K2 (marže): Operativna marža RASTE (0,5%→3,5% kroz 4g, uz -208%/-14,5% u međugodinama)
K3: Test produktivnosti duga kaže "produktivan" ALI serija je izlomljena (vidi §4/§5 napomene)
K4: FCF negativan sve 4 godine, sve dublje (-272,7M → -1.126,7M)
K5 (valuacija @ 44,90): P/E 115,13 | FCF yield na EV -10,8% (negativan!)
```

**Kapije:** prošlo 3/6 | **palo 3** (G1, G2, G3) — po pravilu CLAUDE.md §3, **akcija
ispada iz razmatranja osim ako se napiše eksplicitno pisano obrazloženje
override-a.**
**Override (ako je kapija pala):** *(popunjava Dragan)*

---

## 4. Poređenje sa konkurencijom

**Ključni nalaz — cela grana pati od istog obrasca, ne samo IREN.** Poređenje sa tri
javno listirana "bitcoin-mining-pivotira-na-AI" peer-a i jednim čistim "AI
neocloud" igračem:

| Metrika | IREN (FY2025) | Core Scientific (CORZ, FY2025) | Cipher Mining (CIFR, FY2025) | CoreWeave (CRWV, FY2025) |
|---|---|---|---|---|
| Prihod | $501,0M | $319,0M | $223,9M | $5.131,0M |
| Operativni rezultat | +$17,3M | **-$245,6M** | **-$421,6M** | -$46,0M |
| Neto rezultat | +$86,9M (jednokratne stavke, vidi §5) | -$288,6M | -$822,2M | -$1.167,0M |
| CapEx | $1.372,6M | $729,0M | $487,9M | $10.309,0M |
| Dugoročni dug (kraj FY) | $964,2M | $1.060,3M | $2.711,6M | $14.665,0M |
| Dug — najnoviji kvartal (2026-Q2) | N/A — nije prikupljeno | **$4.298,0M** (skok!) | **$5.446,9M** (skok!) | $25.149,0M (skok!) |

*Izvori: Core Scientific 10-K FY2025 (CIK 0001839341, accession 0001628280-26-013305,
podneto 02.03.2026) + 10-Q Q2 2026 (podneto 28.07.2026). Cipher Mining 10-K FY2025
(CIK 0001819989, accession 0001819989-26-000009, podneto 24.02.2026) + 10-Q Q2 2026
(podneto 04.08.2026). CoreWeave 10-K FY2025 (CIK 0001769628, accession
0001769628-26-000104, podneto 02.03.2026) + 10-Q Q2 2026 (podneto 12.08.2026).*

**Ovo je makro/ciklična karakteristika cele faze izgradnje AI infrastrukture, ne
problem specifičan za IREN** (K2 pravilo iz CLAUDE.md, primenjeno na CapEx/dug
umesto na marže): sve četiri kompanije — uključujući CoreWeave, "čist" AI neocloud
igrač bez bitcoin mining nasleđa — imaju ogromne operativne gubitke, CapEx koji
višestruko nadmašuje prihod, i dug koji se **duplira iz kvartala u kvartal** (CORZ
$1,06 mlrd → $4,30 mlrd u jednom kvartalu; CIFR $2,71 mlrd → $5,45 mlrd; CRWV
$14,67 mlrd → $25,15 mlrd). **IREN je, relativno, najmanje ekstremna od četiri — jedina
sa pozitivnim operativnim rezultatom (+$17,3M) i najmanjim odnosom duga prema
prihodu.** Ovo ne opravdava automatski ulazak, ali menja okvir: pitanje nije "je li
IREN loša kompanija" nego "da li je cela ova faza sektora investabilna po ovoj
metodologiji uopšte" — a to je pitanje van obima jedne scorecard analize.

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | N/A — EPS CAGR nije definisan (baza je bila negativna) | — |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **-10,8%** (nakon SBC: -11,2%) — **negativan** | ništa — samo tekući cash flow |

**FCF yield je negativan — kupuješ akciju čiji poslovni model trenutno troši
gotovinu brže nego što je generiše, na nivou cene koja već pretpostavlja da će
buildout uspeti.** Napomena o preciznosti: EV je računat sa FY2025-kraj-godine
brojem akcija (223,2M), a treća strana (stockanalysis.com, avgust 2026) navodi
aktuelni broj od 357,4M akcija — IREN nastavlja da emituje akcije i posle FY2025,
pa je **stvaran trenutni EV vrlo verovatno veći** od ovde prikazanog, što bi FCF
yield učinilo blago manje negativnim u procentu (ne promenilo bi zaključak — i
dalje negativan).

**G4 (FCF konverzija = 0,78, formalno PROŠLA) je statistički artefakt, ne
signal kvaliteta.** Pojedinačni godišnji odnosi FCF/NI menjaju predznak (0,65 /
0,64 / 14,79 / **-12,96**) jer i FCF i neto dobit prelaze kroz nulu u različitim
godinama — prosek ovakvih odnosa je matematički besmislen. **Ne tumačiti prolaz G4
kao snagu.**

**FY2025 neto dobit (+$86,9M) je dominantno jednokratna** — vidi `_napomena_neto_
dobit_fy2025` u `data/IREN.json`: $77,5M nerealizovan dobitak na finansijskim
instrumentima (Capped Call/Prepaid Forward fer vrednost) + $9,1M dobitak na
delimičnom razduženju. Operativni rezultat sam po sebi (+$17,3M na $501M prihoda =
3,5% marža) je tanko profitabilan bez tih stavki — realna slika je znatno slabija
od "prve profitabilne godine" naslova.

**Kontrola rasta EPS-a:** nije izvodljiva — EPS je negativan u 3 od 4 godine, CAGR
nije definisan. Ono što jeste merljivo: broj akcija je porastao 76% CAGR (masivna
dilucija, ne buyback) — svaki dolar rasta prihoda se deli na sve veći broj akcija.

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. *(popuni)*
2. *(popuni)*
3. *(popuni)*

**Šta je najjači argument protiv kupovine ove akcije?** *(popuni)*

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | | | 50/70/90% |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## 8. Odluka (popunjava Dragan)

**Napomena — tri kapije su pale (G1, G2, G3), uz dodatni metodološki izuzetak
(< 5 godina istorije).** Po CLAUDE.md §3, bez pisanog override obrazloženja jedina
dosledna odluka je "Odbijeno".

- [ ] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Override obrazloženje (OBAVEZNO ako se ne bira "Odbijeno"):** {…}

**Datum ulaza:** {datum unosa, NE retroaktivan, ako override}
**Cena ulaza:** {cena zatvaranja tog dana}
**VUAA cena istog dana:** {…}
**Veličina pozicije:** {1/N satelita}

**Izlazna pravila:** {…}

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| IREN FY2023-FY2025 finansijski podaci | 10-K FY2025 (US GAAP), R3/R5/R7.htm | sec.gov/Archives/edgar/data/1878848/000187884825000063/ | podnet 28.08.2025 |
| IREN FY2022 finansijski podaci (IFRS original) | 20-F FY2024, R2/R5.htm | sec.gov/Archives/edgar/data/1878848/000162828024038677/ | podnet 28.08.2024 |
| IREN restatement (cash flow reklasifikacija) | 6-K + 20-F/A, 20.03.2025 | sec.gov/Archives/edgar/data/1878848/000187884825000020/ i 000187884825000027/ | 20.03.2025 |
| IREN poslovni opis, konvertibilne obveznice, konkurencija | Form 10-K FY2025, Item 1, Item 1A, Item 2, Napomena 18 | sec.gov/Archives/edgar/data/1878848/000187884825000063/iren-20250630.htm | podnet 28.08.2025 |
| IREN cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-17, close 44.90 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-17, close 150.30 |
| IREN WACC (22,1%, bottom-up) | rf: treasury.gov; beta: stockanalysis.com (treća strana, 4,30 — ekstremna) | treasury.gov, stockanalysis.com/stocks/iren/statistics | 14-18.08.2026 |
| Core Scientific (CORZ) finansijski podaci | 10-K FY2025 + 10-Q Q2 2026 | sec.gov, CIK 0001839341 | 02.03.2026 / 28.07.2026 |
| Cipher Mining (CIFR) finansijski podaci | 10-K FY2025 + 10-Q Q2 2026 | sec.gov, CIK 0001819989 | 24.02.2026 / 04.08.2026 |
| CoreWeave (CRWV) finansijski podaci | 10-K FY2025 + 10-Q Q2 2026 | sec.gov, CIK 0001769628 | 02.03.2026 / 12.08.2026 |
