# CLAUDE.md — Mission Stock Lab

Operativna specifikacija za analizu pojedinačnih akcija. Ovaj fajl čitaš pre svake
analize i pratiš ga bez improvizacije.

@docs/05-sektorska-kalibracija.md

> `docs/05` je operativan i potreban pri svakoj analizi van softvera — importovan je
> gore da se ne zaboravi. `docs/04-sta-ovo-moze-da-dokaze.md` je filozofski/statistički
> i treba ga pročitati jednom, ne pri svakoj analizi — ostaje referenca u tekstu, nije
> import.

---

## 0. Kontekst i granice

**Vlasnik:** Dragan (Niš, Srbija). Full-time .NET/MSSQL developer, ne profesionalni
investitor. Postojeći portfolio = **Mission 1M** (pasivni DCA u UCITS ETF-ove: VUAA,
CSNDX, EIMI, VWRA, VWCE; cilj $1M do 2036).

**Šta je ovaj projekat:** *satelit* — mala, unapred ograničena alokacija za stock-picking,
u početku kao **paper trading** radi provere procesa.

**Šta ovaj projekat NIJE:**
- Nije diverzifikacija Mission 1M. Dodaje koncentrisani rizik, ne smanjuje ga.
- Nije zamena za core strategiju. Core DCA se ne dira, ne pauzira, ne smanjuje.
- Nije dokaz da okvir "radi" (vidi `docs/04-sta-ovo-moze-da-dokaze.md`).

**Pravila koja Claude ne sme da prekrši:**
1. Nikad ne preporučuj pomeranje kapitala iz Mission 1M u satelit.
2. Nikad ne izmišljaj finansijske brojeve. Ako podatak nije verifikovan iz izveštaja
   ili pouzdanog izvora — napiši `N/A — treba proveriti`, ne procenu.
3. Svaki broj u analizi ima izvor i datum. Bez izvora = ne ulazi u scorecard.
4. Ne daj "buy/sell" preporuku. Daj popunjen scorecard, otvorena pitanja i rizike.
   Odluku donosi Dragan.
5. Ako kompanija pada u isključeni sektor (§4), reci to i stani — ne prilagođavaj
   metriku da bi analiza "prošla".
6. Odgovori na srpskom.

---

## 1. Pet kriterijuma — finalna specifikacija

### K1 — ROIC (Return on Invested Capital)

```
NOPAT            = EBIT × (1 − efektivna poreska stopa)
Investirani kap. = Ukupan dug + Kapital − Gotovina i ekvivalenti
ROIC             = NOPAT / Investirani kapital (kraj godine; skript koristi ovu verziju)
```

**Prag:** ROIC ≥ 12% kao medijana zadnjih 5 godina, **I** ROIC − WACC ≥ 3pp.
15%+ u kontinuitetu = jak signal.

**Ispravka tvoje pretpostavke:** prag od 15% sam po sebi nije dovoljan. ROIC od 15%
uz WACC od 14% ne kreira vrednost. ROIC od 12% uz WACC od 6% je odlična mašina.
**Spread nad cenom kapitala je ono što stvara vrednost, ne apsolutni nivo.**

**Trend > nivo.** ROIC koji pada 30% → 22% → 18% je gori signal od stabilnog 16%
kroz 5 godina. Pad ROIC-a znači da moat erodira.

**Zamke:**
- Serijski akvizitori: goodwill naduvava investirani kapital → ROIC izgleda nizak.
  Izračunaj i ROIC ex-goodwill, ali **ne koristi samo tu verziju** — akvizicije su
  realno potrošen kapital akcionara.
- Agresivni buyback smanjuje kapital → ROIC veštački raste. Uporedi sa ROIC na
  investirani kapital pre buyback-a.
- Asset-light (softver): R&D se rashoduje, ne kapitalizuje → ROIC naduvan. Za ove
  slučajeve dodaj napomenu i pogledaj R&D/Prihod.
- Operativni lizingi su od IFRS 16 na bilansu — proveri da nisu izostavljeni.

**K1-ALT za kapitalno-lake firme.** Ako je investirani kapital ≤ 0 ili < 10% prihoda,
standardni ROIC ne nosi informaciju (medijana može ispasti u stotinama procenata —
besmislica, ne signal). Uzrok je tipično negativan obrtni kapital jer kupci plaćaju
avansno (deferred revenue > kapital) — vidi MANH (`data/MANH.json`,
`analize/MANH.md`). U tom slučaju: G1 vraća **`N/P`** (nije primenjivo) uz obrazloženje,
i scorecard se prebacuje na **FCF maržu** kao zamenu. `N/P` se ne računa kao prošla
kapija (vidi §3). Ovo je već implementirano u `scripts/scorecard.py`.

---

### K2 — Marže (ispravljena verzija)

```
Bruto marža       = (Prihod − COGS) / Prihod
Operativna marža  = EBIT / Prihod          ← GLAVNI POKAZATELJ
Neto marža        = Neto dobit / Prihod
```

**Ispravka tvoje pretpostavke:** rekao si da velika razlika bruto vs neto marže znači
"neefikasnost u administrativnom delu". Delimično tačno, ali gap između bruto i neto
sadrži SG&A **+ R&D + D&A + kamate + poreze + jednokratne stavke**. Farmaceutska
kompanija ili softverska firma sa 20% prihoda u R&D nije neefikasna — ona investira.

**Zato je operativna marža glavni radni pokazatelj, a ne neto.** Neto marža je
kontaminirana poreskom stopom (jurisdikcija, jednokratni poreski efekti), strukturom
kapitala (kamate) i jednokratnim stavkama. Operativna marža meri efikasnost samog
poslovanja.

Razlaganje koje uvek prikaži:
```
Bruto marža → (−SG&A) → (−R&D) → Operativna marža → (−kamate/porezi) → Neto marža
```

**Prag:** nema apsolutnog. Tvoja procena je bila tačna. Obavezno dva poređenja:
1. vs. sopstvena istorija (5 godina) — trend
2. vs. 3–5 direktnih konkurenata u istoj grani, isti period

Tvoje pravilo "ako pada svima u grani → makro/ciklično; ako pada samo njoj → problem
specifičan za kompaniju" je **tačno i ostaje u sistemu.**

---

### K3 — Zaduženost

**Ispravka #1 (terminologija):** napisao si "Debt-to-equity — odnos duga i ukupne
imovine". To nije to. Dug/imovina je *Debt-to-Assets*. D/E je dug prema **kapitalu**
(equity). Tvoja formula je bila ispravna, opis nije.

**Ispravka #2 (brojilac):** "Ukupne obaveze / Ukupni kapital" meša finansijski dug sa
operativnim obavezama (dobavljači, odloženi prihodi, obaveze za zarade). Obaveza prema
dobavljaču nije isto što i bankarski kredit — ne nosi kamatu i nije poluga.

Zato koristimo tri metrike, u ovom redu prioriteta:

```
1. Neto dug / EBITDA   = (Ukupan dug − Gotovina) / EBITDA     ← GLAVNA
2. Pokrivenost kamata  = EBIT / Rashodi kamata                ← SIGURNOSNA
3. D/E                 = Ukupan finansijski dug / Kapital      ← KONTEKST
```

**Pragovi (nefinansijski sektor):**

| Metrika | OK | Prati | Crveno |
|---|---|---|---|
| Neto dug/EBITDA | < 2.0x | 2.0–3.0x | > 3.0x |
| Pokrivenost kamata | > 6x | 4–6x | < 4x |

Sektorske korekcije: komunalije, telekomi, REIT-ovi normalno rade na 3–5x
Neto dug/EBITDA — tamo se prag pomera, ali obavezno uporedi sa konkurencijom. Pragovi
po sektoru za K1, K3 i K5 su detaljno kalibrisani u `docs/05-sektorska-kalibracija.md`
— pročitaj ga pre analize svake kompanije van softvera.

**Tvoj test "da li je dug doveo do produktivnosti" — konkretizovan:**
Za period od nastanka duga (npr. 5 godina) izračunaj CAGR za: Ukupan dug, Prihod,
EBIT i FCF. Ako je dug rastao brže od EBIT-a i FCF-a → kapital nije bio produktivno
uložen. Ovaj test je ugrađen u `scripts/scorecard.py`.

**`no_financial_debt` flag.** Ako kompanija nema finansijski dug (npr. MANH — neto
gotovina svih 5 godina), test produktivnosti duga gore nema smisla — bez duga bi test
merio rast operativnih obaveza (npr. zakup kancelarija) i vraćao lažan negativan
rezultat. Skript postavlja `no_financial_debt` u `meta` i suzbija test produktivnosti
duga u tom slučaju.

---

### K4 — Free Cash Flow

```
OCF = Neto dobit
      + D&A (amortizacija materijalne I nematerijalne imovine)
      + SBC (stock-based compensation)
      + odloženi porezi i ostale nenovčane stavke
      ± promene obrtnog kapitala
FCF = OCF − CapEx
```

**Ispravka:** u tvojoj formuli je samo "Amortizacija". Nedostaju **SBC** i odloženi
porezi. SBC je kritičan — za softverske/tech kompanije često 5–15% prihoda. Dodaje se
OCF-u jer nije novčani izdatak, **ali je realan trošak za akcionara kroz dilaciju.**
Kompanija koja se hvali "record FCF" a izdaje 10% prihoda u akcijama ne stvara toliko
vrednosti koliko izgleda.

Zato uvek prikaži i:
```
SBC / Prihod                    → ako > 5%, obavezna napomena o dilaciji
FCF nakon SBC = FCF − SBC       → konzervativna verzija
Rast broja akcija (5 god)       → prava mera dilacije
```

**Provere kvaliteta zarade (ovo je najvrednija upotreba cash flow-a):**
```
FCF konverzija = FCF / Neto dobit       → 5-god prosek ≥ 0.7
OCF / Neto dobit                        → ako je uporno < 1.0, zarada je "na papiru"
```

Tvoja intuicija da je cash flow manje podložan manipulaciji od bilansa uspeha je
tačna, i tvoj primer sa fakturom od 1M i rokom od 60 dana je korektno objašnjen.
Dodatak: uporno rastuća potraživanja **brže od prihoda** su klasičan signal da se
prihod priznaje agresivno ili da kupci ne plaćaju. Prati:
```
Rast potraživanja vs rast prihoda    → potraživanja rastu brže = crvena zastavica
Rast zaliha vs rast prihoda          → isto
```

**Prag:** FCF pozitivan u ≥ 4 od poslednjih 5 godina. Uporno negativan FCF uz
pozitivnu neto dobit = automatski izlaz iz analize.

**Bonus metrika (forecast-free valuacija):**
```
FCF yield = FCF / Enterprise Value
```
Ovo je vredno jer **ne zavisi od projekcija rasta** — direktna suprotnost PEG-u.
Koristi je kao kontrolu PEG-a.

---

### K5 — PEG Ratio

```
PEG = (P/E) / (stopa rasta EPS-a izražena kao ceo broj)
```

**Tvoja formula je matematički ispravna.** `15 / (0.20 × 100) = 15/20 = 0.75` ✓
Takođe `60 / (0.20 × 100) = 3.00` ✓ i tvoja napomena da bi pri 80% rasta 60/80 = 0.75
bilo prihvatljivo je tačna. Ovde nema šta da se ispravlja.

**Ali PEG je najslabiji od tvojih pet kriterijuma, i to zbog imenioca.**

Problem: "godišnja stopa rasta EPS-a" — koja? Postoje dve, i daju različite odgovore:

| Verzija | Kako | Prednost | Slabost |
|---|---|---|---|
| PEG_trailing | 5-god istorijski EPS CAGR | činjenica, ne procena | prošlost ≠ budućnost |
| PEG_forward | 3-god konsenzus analitičara | gleda naprijed | analitičari su sistematski optimistični |

**Pravilo sistema: računaj oba i tretiraj razliku kao informaciju.**
Ako je PEG_forward mnogo niži od PEG_trailing, tržište/analitičari očekuju ubrzanje
koje se još nije dogodilo — to je pretpostavka koju moraš eksplicitno da opravdaš, ne
da prihvatiš.

**Druga slabost — EPS se manipuliše buyback-om.** Kompanija koja otkupljuje 5% akcija
godišnje pokazuje rast EPS-a bez rasta poslovanja. Obavezna kontrola:
```
Prihod CAGR (5g)  vs  EPS CAGR (5g)  vs  FCF/akcija CAGR (5g)
```
Ako EPS CAGR znatno nadmašuje Prihod CAGR → rast je finansijski inženjering, ne posao.

**Gde PEG uopšte ne radi (ne koristi ga, koristi FCF yield + reverse DCF):**
- Ciklične kompanije na vrhu ili dnu ciklusa (E je nereprezentativan)
- Negativna ili blizu-nule zarada
- Rast > 40% (PEG previše blago kažnjava)
- Kvalitetni compounder-i sa nizak rastom (PEG od 2.5 za 6%-rastuću firmu sa
  ROIC-om 25% nije nužno "precenjeno")

**Prag:** PEG < 1.0 = zanimljivo. 1.0–2.0 = neutralno, gledaj ostale kriterijume.
> 2.0 = zahteva eksplicitno obrazloženje zašto plaćaš premiju.

---

## 2. Šesti kriterijum koji nedostaje: MOAT

Tvojih pet kriterijuma su **svi kvantitativni i svi retrospektivni.** Oni mere da je
kompanija bila dobra. Nijedan ne odgovara na pitanje: **zašto konkurencija neće
pojesti taj visok ROIC u sledećih 10 godina?**

Bez ovoga, visok ROIC je samo podatak. Sa ovim, on je teza.

**Obavezan test:** izvor konkurentske prednosti moraš da formulišeš u **dve rečenice**.
Ako ne možeš — preskoči akciju. Ovo nije formalnost; nemogućnost artikulacije je
signal da ne razumeš posao.

Kategorije (ako ne pada ni u jednu, verovatno nema moat):
- Troškovi prelaska (switching costs) — ERP, banke, enterprise softver
- Mrežni efekti — platforme, marketplace-ovi
- Ekonomija obima / troškovna prednost — proizvodnja, logistika
- Brend sa cenovnom moći — potrošačka roba
- Regulatorna/licencna barijera — komunalije, farmacija, infrastruktura
- Nematerijalna imovina — patenti, podaci

**Krug kompetencije (Dragan-specifično):** tvoja realna informaciona prednost je u
softveru, IT uslugama, developer tooling-u, enterprise SaaS-u i .NET/Microsoft
ekosistemu. Tamo možeš da proceniš proizvod, tehnički dug, i da li je "AI strategija"
supstanca ili marketing — na način na koji generalista ne može. Van toga si
prosečan investitor koji čita iste izveštaje kao svi. Prioritizuj svoj krug.

---

## 3. Sistem odlučivanja: kapije vs. signali

Ne pravimo jedan složeni "score" — to je lažna preciznost. Umesto toga:

### HARD KAPIJE (pad = akcija ispada; override zahteva pisano obrazloženje)
1. ROIC (5g medijana) ≥ 12% **I** ROIC − WACC ≥ 3pp. Za kapitalno-lake firme (K1-ALT,
   vidi §1 K1) ova kapija vraća **`N/P`** umesto prolaz/pad — `N/P` **se NE računa kao
   prošla kapija**, ali ne obara analizu; scorecard tada gleda FCF maržu kao zamenu.
2. Neto dug/EBITDA ≤ 3.0x (sektorski korigovano — vidi `docs/05`) **I** pokrivenost
   kamata ≥ 4x
3. FCF pozitivan u ≥ 4 od 5 godina
4. FCF konverzija (5g prosek) ≥ 0.7
5. Moat artikulisan u 2 rečenice
6. Kompanija nije u isključenom sektoru (§4)

### SOFT SIGNALI (ne isključuju, ali ulaze u rang i u tezu)
- ROIC trend: raste / stabilan / pada
- Operativna marža vs. konkurenti i vs. sopstvena 5-god istorija
- PEG_trailing i PEG_forward + razlika između njih
- FCF yield na EV
- Gap Prihod CAGR vs EPS CAGR (zavisnost od buyback-a)
- SBC / Prihod i rast broja akcija
- Test produktivnosti duga (dug CAGR vs EBIT/FCF CAGR)
- Potraživanja i zalihe vs rast prihoda

---

## 4. Isključeni sektori (v1)

Ovih **ne diramo**, jer pet kriterijuma tamo daju besmislene rezultate:

| Sektor | Zašto | Šta bi trebalo umesto |
|---|---|---|
| Banke, osiguranje | Dug je sirovina, ne poluga. ROIC/EV nemaju smisla | ROTCE, CET1, P/TBV, kombinovani racio |
| REIT-ovi | Amortizacija dominira; neto dobit nije relevantna | FFO/AFFO, NAV, LTV, cap rate |
| Pre-profit / biotech | Nema E, nema FCF, nema PEG | Runway, faze ispitivanja — spekulacija |
| Duboko ciklične na ekstremu | E i marže neupotrebljivi | Normalizovana zarada kroz ciklus |
| Kompanije sa < 5 god javne istorije | Nema kontinuiteta za proveru | čekaj |

**Razjašnjenje — platni sistemi nisu banke.** Isključenje finansijskog sektora
postoji jer kod banaka investirani kapital uključuje depozite (kapital koji drže ali
ne poseduju), pa ROIC daje neuporedive brojeve. **Mastercard i Visa ne rade tako** —
ne nose kreditni rizik, ne primaju depozite, zarađuju od obima transakcija
(asset-light mrežni posao, operativne marže preko 50%). Isto važi za berze (CME, ICE)
i rejting agencije (MCO, SPGI) — infrastruktura, ne bilansni rizik. Platni sistemi,
berze i rejting agencije **NISU isključeni** i analiziraju se sa prilagođenim (višim)
pragovima iz `docs/05-sektorska-kalibracija.md` §2–3.

**Isključeno ostaje:** komercijalne banke, investicione banke, osiguravači,
reosiguravači, brokerski dileri, BDC-ovi, hipotekarni REIT-ovi.

---

## 5. Workflow za jednu analizu

Kada Dragan traži analizu kompanije:

**Faza 1 — Provera prihvatljivosti**
- Sektor nije isključen? Ima ≥ 5 godina javnih izveštaja? Ako ne → stani, objasni.

**Faza 2 — Prikupljanje podataka**
- Pozicije za 5 fiskalnih godina + poslednja 4 kvartala (TTM):
  Prihod, COGS, SG&A, R&D, EBIT, Rashodi kamata, Neto dobit, Efektivna poreska stopa,
  D&A, SBC, Promene obrtnog kapitala, OCF, CapEx, Ukupan dug (kratkoročni+dugoročni),
  Gotovina, Ukupan kapital, Broj akcija (diluted), Potraživanja, Zalihe
- Tržišni: cena, market cap, EV, P/E, konsenzus EPS rast (3g)
- WACC: ako nije dostupan, koristi konzervativnu procenu i **eksplicitno je označi
  kao procenu sa navedenim pretpostavkama**
- Svaki broj → izvor + datum. Nema izvora → `N/A`.

**Faza 3 — Izračun**
- Popuni JSON po šablonu `data/primer_kompanija.json`
- Pokreni `python3 scripts/scorecard.py data/<ticker>.json`

**Faza 4 — Analiza (šablon `templates/analiza.md`)**
- Scorecard rezultat
- Moat u 2 rečenice
- Poređenje sa 3–5 konkurenata (marže, ROIC, zaduženost)
- **Tri stvari koje bi opovrgle tezu** (obavezno — ako ih nema, analiza je nepotpuna)
- **Merljiva predviđanja za 4 kvartala unaprijed** (vidi §6 — ovo je srce sistema)
- Otvorena pitanja i N/A polja

**Faza 5 — Odluka i evidencija**
- Ako ulazi u paper portfolio: upiši u `data/positions.csv` sa timestamp-om
- Datum ulaza je **datum unosa, ne retroaktivan**. Cena ulaza = cena zatvaranja tog
  dana. Nikad ne birati bolju cenu iz prošlosti.

---

## 6. Kako se ovo zapravo validira

**Ne kroz prinos paper portfolija.** Detaljno obrazloženje u
`docs/04-sta-ovo-moze-da-dokaze.md`, ali kratko: 10 pozicija kroz 12 meseci nema
statističku moć da razdvoji sposobnost od sreće. Šum dominira.

**Validiramo kroz tačnost predviđanja fundamenata.** Za svaku poziciju, pri ulazu
zapisuješ konkretna, merljiva očekivanja za 4 kvartala:

```
Primer:
- ROIC ostaje ≥ 15%                          → ISTINITO / NETAČNO
- Operativna marža ≥ 22% (±1pp)              → ISTINITO / NETAČNO
- FCF raste ≥ 8% god/god                     → ISTINITO / NETAČNO
- Neto dug/EBITDA ostaje < 1.5x              → ISTINITO / NETAČNO
- Broj akcija ne raste više od 1%            → ISTINITO / NETAČNO
```

Nakon svakog kvartala: upiši realizovane vrednosti u `data/fundamentals_log.csv` i
oceni predviđanja. **Fundamenti su mnogo manje šumoviti od cena**, pa ovaj test daje
upotrebljiv signal za 12–18 meseci — dok bi test kroz prinose zahtevao decenije.

Ako ti se predviđanja fundamenata ostvaruju u 70%+ slučajeva, tvoja analiza ima
sadržaj. Ako je oko 50%, tvoj okvir ne razlikuje ništa i cena ti neće pomoći.

---

## 7. Pravila paper trading-a

- **Benchmark je obavezan.** Svaka pozicija se meri protiv **VUAA total return za
  identičan period držanja.** "Zaradio sam 9%" nema značenje ako je indeks dao 13%.
- Maks 8–12 pozicija. Manje = previše šuma; više = de facto indeks uz mnogo rada.
- Jednake početne veličine pozicija (npr. 1/10 satelita svaka). Bez "sizing by
  conviction" u v1 — to dodaje varijablu koju ne možeš da izoluješ.
- **Bez retroaktivnih izmena.** Teze se ne prepravljaju posle činjenice. Ispravke se
  dodaju kao novi datirani zapis, staro ostaje.
- Izlazna pravila se definišu **pri ulazu**, i vezana su za tezu, ne za cenu:
  - Hard kapija pada (npr. Neto dug/EBITDA > 3.5x dva kvartala zaredom)
  - Moat teza opovrgnuta (konkretno, ne "osećaj")
  - ROIC pada ispod 12% dva kvartala zaredom
  - Ne prodajemo zato što je cena pala. Ne držimo zato što je cena pala.
- Mesečni pregled: ažuriraj cene, pokreni `scripts/tracker.py`.
- Kvartalni pregled: fundamenti, ocena predviđanja, provera kapija.

---

## 8. Otvorene stavke koje Dragan treba da razreši

1. **Poresko tretiranje kapitalnog dobitka u Srbiji za pojedinačne akcije preko IBKR**
   — stopa, obaveza samostalne prijave, mogući period držanja koji utiče na obavezu,
   tretman dividendi i withholding tax. **Ovo nije verifikovano u ovom projektu i
   materijalno menja neto prinos.** Proveri sa poreskim savetnikom pre realnog kapitala.
2. Konkretan iznos satelita i potvrda da je to ≤ 10% ukupnog portfolija.
3. Odluka: samo paper, ili paper + mali realan iznos? (Paper ne testira ponašanje —
   emotivni pritisak realnog novca je ono što razbija disciplinu.)

---

## 9. Komande

Sve skripte koriste samo standardnu Python biblioteku. Windows: `python`, ne
`python3`. Ako Unicode karakteri (≥, →) pucaju sa `UnicodeEncodeError` na Windows
konzoli, postavi `PYTHONIOENCODING=utf-8` pre pozivanja skripte.

```
# 1. Popuni market blok (cena, EV, P/E, PEG...) iz jedne cene zatvaranja
python scripts/fill_price.py data/<ticker>.json <CENA> --growth <konsenzus_EPS_rast> --dry
python scripts/fill_price.py data/<ticker>.json <CENA> --growth <konsenzus_EPS_rast>

# 2. Generiši scorecard (5 kriterijuma + kapije) iz popunjenog JSON-a
python scripts/scorecard.py data/<ticker>.json --md > analize/<ticker>-scorecard.md

# 3. Mesečni pregled portfolija vs VUAA benchmark
python scripts/tracker.py
```

Cena za `fill_price.py` ide isključivo iz IBKR-a (zaključna cena, ne intraday, ne
agregatori sa weba — vidi §0 pravilo 3 i `docs/05`). Uz nju se uvek uzima i VUAA
zaključna cena istog dana.

---

## 10. Definicija završene analize

Analiza jedne kompanije **nije završena** dok nije provereno sve sledeće:

1. Svaki broj u `data/<ticker>.json` ima izvor (dokument + datum) — bez izvora broj
   ne ulazi u scorecard, ide kao `N/A — treba proveriti`.
2. `scripts/scorecard.py` je pokrenut i izlaz je sačuvan u `analize/<ticker>-scorecard.md`.
3. Sekcije koje popunjava Claude (podaci, izračuni, poređenje sa konkurencijom,
   otvorena pitanja) su u `analize/<ticker>.md` — vidi podelu rada §6 u `HANDOFF.md`.
4. Sekcije koje popunjava vlasnik (moat, tri stvari koje bi opovrgle tezu, pet
   predviđanja sa nivoom uverenosti, odluka) su **ostavljene prazne ili kao predlog
   jasno obeležen kao predlog** — Claude ih ne popunjava u ime vlasnika.
5. Ako pozicija ulazi u paper portfolio: upis u `data/positions.csv` je sa
   neretroaktivnim datumom i cenom zatvaranja tog dana, plus VUAA cena istog dana.
6. Sve gorenavedeno je komitovano istog dana (vidi Z1 u `HANDOFF.md` — metodološka
   zaštita od hindsight bias-a, ne higijena).

Ako nešto od 1–6 ne može da se verifikuje (npr. izvor nedostupan), to se kaže
eksplicitno — ne tretira se kao završeno.

---

## 11. Šta da ne radim

- Ne izmišljam brojeve ni kada je "očigledno" koliki bi trebalo da budu — `N/A`.
- Ne uzimam cenu ili finansijske brojeve sa agregatora (stockanalysis, GuruFocus,
  Yahoo, TipRanks) — samo SEC EDGAR / 8-K / 10-K / IBKR za cenu.
- Ne biram "bolju" cenu ili datum iz prošlosti kad je dostupna novija informacija —
  datum i cena ulaza se zaključavaju pre nego što se ishod zna.
- Ne pišem moat, tri opovrgavajuće tačke, predviđanja ili odluku u ime vlasnika —
  mogu da ponudim predlog, jasno obeležen kao predlog.
- Ne prilagođavam metriku ili prag da bi analiza "prošla" kad kompanija pada u
  isključeni sektor ili kapiju.
- Ne preporučujem buy/sell, ni pomeranje kapitala iz Mission 1M u satelit.
- Ne amenduj-ujem stare git komite ni prepravljam stare zapise u `positions.csv` /
  `predvidjanja.csv` — ispravke idu kao novi datirani zapis.
