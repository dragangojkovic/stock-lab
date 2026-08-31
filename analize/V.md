# Analiza: Visa Inc. (V)

**Datum:** 2026-08-31 | **Analitičar:** Dragan | **Cena na dan analize:** 381,60 USD (zaključna cena 2026-08-28, IBKR)
**U krugu kompetencije:** DELIMIČNO — identično MA. Tehnološka komponenta
(VisaNet) je blizu Draganovog IT fokusa, regulatorna/finansijska infrastruktura
nije.

> Sekcije 1, 3, 4, 5 i 9 popunio Claude — činjenično, sa izvorima. Sekcije 2, 6, 7, 8
> ostaju za Dragana (vidi podelu rada, `HANDOFF.md` §6).

---

## 1. Šta kompanija zapravo radi

Visa je, kao i Mastercard, **"four-party" mrežna kompanija** (issuer banka —
account holder — merchant — acquirer banka) preko VisaNet infrastrukture, u
preko 200 zemalja/teritorija. Jedan izveštajni segment: "Payment Services".
Zarada dolazi od obima transakcija, ne od kreditnog rizika ili kamata —
**nije banka** (potvrđuje `docs/05` §3 tezu).

**Obim FY2025:** 329 milijardi ukupnih transakcija u ekosistemu (Visa brend), od
čega 258 milijardi obradio direktno sam Visa; prosek ~901 milion transakcija
dnevno.

**Prema Nilson Report #1288 (jun 2025, citirano u Visa 10-K, baza CY2024):**
Visa je **veći partner u duopolu** po svim merenim dimenzijama:

| | Visa | Mastercard |
|---|---|---|
| Payments Volume | $13.433 mlrd | $8.014 mlrd |
| Total Volume | $15.927 mlrd | $9.757 mlrd |
| Total Transactions | 311 mlrd | 204 mlrd |
| Broj kartica | 4.805 mln | 3.146 mln |

**Geografija:** SAD ~39% ukupnog neto prihoda FY2025 (opadajući udeo — 41%
FY2024, 43% FY2023 — rast dolazi iz međunarodnog poslovanja). ~34.100
zaposlenih (FY2025, +8% god/god), prisutni u 86 zemalja, >60% van SAD.

**Koncentracija klijenata:** Jedan neimenovani klijent = **11% ukupnog neto
prihoda** konzistentno FY2023/2024/2025 — 10-K ne otkriva identitet.

**Regulatorni rizici — MATERIJALNO NAPREDNIJI OD MA:**
- **DOJ TUŽBA (ne samo istraga):** 24.9.2024. Antitrust Division je **podneo
  tužbu** protiv Visa (U.S. District Court, SDNY) za navodni monopol/pokušaj
  monopolizacije "general purpose debit network services" i "card-not-present
  debit network services". Visa je **23.6.2025. izgubila zahtev za odbacivanje
  tužbe** (motion to dismiss denied) — tužba je aktivna i u naprednijoj fazi
  nego MA-in CID (koji je i dalje samo istraga, bez podnete tužbe).
- Posledica: shareholder securities class action (20.11.2024) + tri derivative
  actions (jan-mart 2025).
- Isti MDL 1720 interchange litigacija kao MA (upravljana kroz "U.S.
  Retrospective Responsibility Plan" — litigation escrow $2,99 mlrd + Class B
  konverzioni mehanizam).
- Litigation provision skočio na $2,562 mlrd FY2025 (vs $462M FY2024, $927M
  FY2023) — objašnjava pad operativne marže u FY2025 (60,0% vs ~64-66%
  prethodnih godina).

**Dividende/buyback:** Visa plaća i dividende i radi **agresivniji buyback od
MA** u apsolutnom iznosu. Dividende: $2.798M→$4.634M (FY2021-2025). Buyback:
$8.676M→$18.316M — veći nego kod MA ($11.727M FY2025), i equity ostaje
pozitivan/stabilan (~$35,6-39,1 mlrd).

**Goodwill/akvizicije:** Visa ima goodwill $19,879 mlrd i nematerijalnu imovinu
$27,646 mlrd (FY2025) — VEĆI nego kod MA, i rastuć (akvizicije $887M FY2025,
$915M FY2024). K1 "serijski akvizitori" zamka je relevantnija za Visa nego za
MA, iako ne u meri koja bi ugrozila kapiju (vidi §3).

*Izvor: Form 10-K FY2025 (godina završena 30.09.2025), CIK 0001403161,
accession 0001403161-25-000089, Item 1, Item 1A, Note 20.*

---

## 2. Moat — dve rečenice (obavezna kapija)

Isti mehanizam kao MA — dvostrani mrežni efekat (banke izdavaoci ↔
merchant/acquirer mreža) + regulatorna barijera po jurisdikciji. Visa je
veći partner u duopolu po svim merenim dimenzijama (Payments Volume $13,4T
vs MA $8,0T, CY2024) i ima bolju zaduženost/pokrivenost kamata/FCF konverziju
od MA, iako niži ROIC (40,2% vs 80,8%) — verovatno delom zbog većeg
goodwill-a/nematerijalne imovine u imeniocu.

- Kategorija: mrežni efekat (dvostran) + regulatorna/licencna barijera
- **Šta bi ubilo ovaj moat u 5 godina:** isto kao MA — državno-podržani
  real-time payment sistemi (FedNow, PIX, UPI) postignu dovoljno usvajanje da
  zaobiđu kartične mreže.
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:**
  identično MA — decenije izgradnje bankarskih odnosa + regulatorno
  odobrenje u svakoj jurisdikciji istovremeno.

---

## 3. Scorecard

Izlaz iz `python scripts/scorecard.py data/V.json` (kompletan fajl:
`analize/V-scorecard.md`):

```
SCORECARD — Visa Inc. (V)
Sektor: Infrastruktura tržišta - platni sistemi

G1 (ROIC ≥30% platni sistemi, spread ≥3pp nad WACC): PROŠAO
    — medijana 40,2%, WACC 8,0%, spread 32,2pp
G2 (Neto dug/EBITDA ≤2.0x, pokriv. kamata ≥4x):      PROŠAO — 0,32x / 40,7x
G3 (FCF pozitivan ≥4/5 god.):                        PROŠAO — 5/5
G4 (FCF konverzija ≥0.7):                            PROŠAO — 1,11
G5 (Moat u 2 rečenice):                              čeka Draganovu formulaciju
G6 (Nije u isključenom sektoru):                     PROŠAO

Prošlo: 6/6 | Palo: 0

K2 (marže): Bruto N/A (mrežni posao, nema COGS) | Operativna 60,0% (FY2025,
   pad sa ~64-66% zbog litigation provision skoka) | Neto 50,1%
K3 (zaduženost): ND/EBITDA 0,32x | pokrivenost kamata 40,7x | dug PRODUKTIVAN
K4 (FCF): FCF konverzija prosek 1,11 | SBC/prihod 2,2%
K5 (valuacija @ 381,60): P/E 37,41 | PEG_trailing 2,34 (IZNAD praga 2,0) |
   FCF yield na EV 2,8%
```

**Kapije:** prošlo 6/6 | palo 0. ROIC (40,2% medijana) je genuinski visok, isti
mehanizam kao MA (`docs/05` §4) — signal saturiran, FCF marža (53,9%) je
korisniji primarni pokazatelj kvaliteta od ROIC-a.

---

## 4. Poređenje sa konkurencijom

**Mastercard (MA) — direktan duopol par, ista analiza kao u `analize/MA.md`
§4, sada iz Visa perspektive.**

| Metrika | Visa (FY2025) | Mastercard (FY2025) |
|---|---|---|
| Prihod | $40.000M | $32.791M |
| Operativna marža | 60,0% (pad zbog litigacije — normalno ~64-66%) | 57,6% |
| Neto marža | 50,1% | 45,6% |
| ROIC medijana (5g) | 40,2% | 80,8% |
| Neto dug/EBITDA | 0,32x | 0,42x |
| Pokrivenost kamata | 40,7x | 26,2x |
| FCF konverzija | 1,11 | 1,03 |
| FCF marža | 53,9% | 50,1% |
| P/E | 37,41 | 34,74 |
| PEG_trailing | 2,34 | 2,02 |

**Ključni nalaz — MA-in ROIC je impresivniji (80,8% vs 40,2%), ali Visa je bolja
po skoro svim ostalim metrikama** (niža zaduženost, viša pokrivenost kamata,
viša FCF konverzija i FCF marža, veći apsolutni obim). Razlika u ROIC-u
verovatno delom odražava razliku u investiranom kapitalu — Visa nosi veći
goodwill/nematerijalnu imovinu ($47,5 mlrd kombinovano) nego MA, što povećava
imenilac ROIC formule bez nužno smanjenja kvaliteta posla. **Ovo je isti
"kontrolni duopol" zaključak kao u MA analizi — oba igrača su izuzetno
disciplinovana, razlike su u nijansama, ne u redovima veličine.**

**Regulatorni rizik je AKTIVNIJI kod Visa** — DOJ je već podneo tužbu (ne samo
CID kao kod MA) i izgubila je motion to dismiss. Ovo je materijalna razlika
koju treba uzeti u obzir pri poređenju rizika, ne samo brojeva.

*Izvor: Mastercard Incorporated 10-K FY2025, CIK 0001141391 (vidi
`analize/MA.md` za pun izvor).*

---

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | **2,34** (P/E 37,41 / EPS CAGR 16,0%) — IZNAD praga 2,0, zahteva obrazloženje | prošli rast se nastavlja |
| PEG_forward | N/A — konsenzus rast nije prikupljen | — |
| FCF yield na EV | **2,8%** (nakon SBC: 2,7%) | ništa — samo tekući cash flow |
| **FCF marža** | **53,9%** — primarni K1-ALT-stil signal (ROIC signal saturiran) | zamenska metrika |

**Kontrola — da li je rast EPS-a stvaran ili buyback:**

| Metrika | CAGR (5g) |
|---|---|
| Prihod | 13,5% |
| EPS | 16,0% |
| FCF po akciji | 13,4% |

**Blago upozorenje, ne alarm.** EPS CAGR (16,0%) je nešto iznad i prihoda
(13,5%) i FCF/akcije (13,4%) — buyback doprinosi delu EPS rasta iznad onoga što
cash generacija sama pokazuje, ali razlika je mala (2-3pp) i sve tri metrike
rastu zdravo. Ovo NIJE ORLY-stil obrazac (gde je FCF/akcija opadao dok je EPS
rastao) — ovde sve tri metrike rastu, samo neravnomerno.

**PEG 2,34 je iznad praga i nešto skuplji od MA (2,02) uprkos nižem ROIC-u** —
tržište plaća premiju za veći obim/tržišnu poziciju i nižu zaduženost, ali ovo
zahteva eksplicitno obrazloženje po CLAUDE.md K5 pravilu ("PEG > 2,0 zahteva
eksplicitno obrazloženje zašto plaćaš premiju") — kandidat obrazloženje: niža
zaduženost i viša FCF konverzija/marža delimično kompenzuju niži trailing PEG
kvalitet, ali ovo je otvoreno pitanje za Faza 6 (moat/odluka).

---

## 6. Tri stvari koje bi opovrgle tezu (obavezno — popunjava Dragan)

1. DOJ tužba rezultira strukturnom merom (npr. prisilne promene pristupa
   debit mreži) koja merljivo smanji US debit prihod.
2. Operativna marža padne ispod 55% dva kvartala zaredom (dalja eskalacija
   litigation provision-a iznad FY2025 nivoa).
3. Rast switched/processed transakcija padne ispod 5% god/god dva kvartala
   zaredom.

**Šta je najjači argument protiv kupovine ove akcije?** DOJ tužba je već
preživela zahtev za odbacivanje (jun 2025) — aktivnija i rizičnija faza od
MA-inog CID-a. Uz to, MA je već u portfoliu iz istog sektora ("Infrastruktura
tržišta", `docs/05` §6 preporučuje max 1 poziciju) — Visa i Mastercard su
gotovo savršeno korelisana opklada (isti duopol, ista makro/regulatorna
izloženost), pa dodavanje V ne diverzifikuje nego udvostručuje istu opkladu,
uz PEG (2,34) iznad praga.

---

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA (popunjava Dragan)

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | Operativna marža ostaje visoka | ≥ 58% | 70% |
| 2 | FCF konverzija ostaje solidna | ≥ 1,0 | 70% |
| 3 | Zaduženost ostaje niska | Neto dug/EBITDA ≤ 1,0x | 70% |
| 4 | Rast switched transakcija se nastavlja | ≥ 6% god/god | 70% |
| 5 | DOJ tužba ne rezultira presudom/nagodbom koja materijalno menja poslovni model | u narednih 12 meseci | 70% |

---

## 8. Odluka (popunjava Dragan)

- [ ] Ulazi u paper portfolio
- [x] Watchlist — čekam da MA teza pukne (izlazak iz portfolia) ILI da se
      DOJ tužba razreši povoljno/razjasni rizik ILI da PEG padne ispod 2,0
- [ ] Odbijeno — razlog: {…}

**Razlog:** Kvalitet je vrhunski, čak bolji od MA po zaduženosti/pokrivenosti
kamata/FCF konverziji, ali sektorski cap (`docs/05` §6, max 1 pozicija
"Infrastruktura tržišta") je već popunjen sa MA, i V/MA su gotovo savršeno
korelisana opklada (isti duopol). Regulatorni rizik je u naprednijoj fazi
(aktivna DOJ tužba, izgubljen motion to dismiss) nego kod MA (samo CID).
Watchlist umesto dodatne pozicije u istom sektoru.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| V FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R9.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/1403161/000140316125000089/ | podnet 06.11.2025 |
| V FY2021-FY2022 finansijski podaci | 10-K FY2022 (accession 0001403161-22-000081), R5.htm lično verifikovano | sec.gov/Archives/edgar/data/1403161/000140316122000081/ | podnet 16.11.2022 |
| V poslovni opis, konkurencija, regulatorni rizici, DOJ tužba | Form 10-K FY2025, Item 1, Item 1A, Note 20 | sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm | podnet 06.11.2025 |
| V cena zatvaranja | IBKR TWS, sveća 1D | — | 2026-08-28, close 381.60 |
| VUAA cena istog dana | IBKR TWS, sveća 1D | — | 2026-08-28, close 150.12 |
| V WACC (7,95%, bottom-up) | rf: treasury.gov (4,73%, 10Y UST, 28.08.2026); beta: stockanalysis.com (0,76, treća strana) | treasury.gov, stockanalysis.com/stocks/v/statistics | 28-31.08.2026 |
| Mastercard (MA) FY2025 podaci za poređenje | vidi `analize/MA.md` §9 | — | — |
