# HANDOFF.md — prelazak na Claude Code

**Datum predaje:** 2026-08-11
**Putanja projekta:** `C:\Users\dragan.gojkovic\Documents\Dragan\stock-lab`
**Prethodni kontekst:** chat sesija u kojoj je sistem izgrađen i odrađena prva analiza (MANH)

> Claude Code automatski čita `CLAUDE.md` — tamo je specifikacija sistema.
> Ovaj fajl je **stanje stvari**, ne specifikacija. Ne dupliraj CLAUDE.md.
> Pročitaj u ovom redu: `CLAUDE.md` → `docs/04-sta-ovo-moze-da-dokaze.md` →
> `docs/05-sektorska-kalibracija.md` → ovaj fajl.

---

## 1. Šta je projekat

Satelit za stock-picking uz **Mission 1M** (pasivni DCA u UCITS ETF-ove: VUAA, CSNDX,
EIMI, VWRA, VWCE; cilj $1M do 2036). Mission 1M se **ne dira**.

Pet kriterijuma vlasnika (ROIC, marže, zaduženost, FCF, PEG) + šesti dodat u chat-u
(moat u dve rečenice). Faza: **paper trading, $1.000 po poziciji**, bez realnog kapitala.

**Cilj eksperimenta je preformulisan** i to je bitno: nije "dokazati da okvir donosi
veći prinos od indeksa" (matematički nedostižno — treba 16–28 godina za statističku
značajnost), nego **meriti tačnost predviđanja fundamenata** kroz 12 meseci.
Obrazloženje u `docs/04`. Ne vraćaj cilj na prinos.

---

## 2. Stanje: MANH (prva analiza) — ZAVRŠENA, verdikt WATCHLIST

### Podaci — kompletni i verifikovani

`data/MANH.json` sadrži FY2021–FY2025, sve iz zvaničnih 8-K Exhibit 99.1:

| Godine | Izvor |
|---|---|
| FY2025 + FY2024 | press release 27.01.2026 |
| FY2023 + FY2022 | press release 30.01.2024 |
| FY2022 + FY2021 | press release 02.02.2023 |

Unakrsne provere prošle: FY2022 se poklapa do cifre u dva nezavisna dokumenta;
gotovina na kraju FY2023 (270.741) = gotovina na početku FY2024. **Ne prikupljaj ove
podatke ponovo.**

### Rezultat kapija: 5 prošlo, 1 N/P, 0 palo

- G1 (ROIC): **N/P** — investirani kapital 42.198 = 3,9% prihoda. ROIC divergira
  (medijana ispada 659%, besmislica). Zamenjeno FCF maržom.
- G2 (zaduženost): prošao — **nema finansijskog duga**, neto gotovina svih 5 godina
- G3 (FCF pozitivan): prošao 5/5
- G4 (FCF konverzija): prošao, prosek 1,47
- G5 (moat): **nije popunjen — vlasnikov zadatak**
- G6 (sektor): prošao

### Ključni nalazi

**Rast se raspao, marža je to maskirala:**

| FY | Prihod | rast | Cloud rast | Usluge rast | RPO | rast | SBC/prihod | Op. marža |
|---|---|---|---|---|---|---|---|---|
| 2021 | 663.643 | — | — | — | 699.244 | — | 6,5% | 20,2% |
| 2022 | 767.084 | +15,6% | +44,4% | +17,7% | 1.051.544 | +50,4% | 7,7% | 19,9% |
| 2023 | 928.725 | +21,1% | +44,3% | +23,8% | 1.427.854 | +35,8% | 7,7% | 22,6% |
| 2024 | 1.042.352 | +12,2% | +32,4% | +7,7% | 1.780.400 | +24,7% | 8,9% | 25,1% |
| 2025 | 1.081.392 | **+3,7%** | +21,0% | **−4,3%** | 2.232.234 | +25,4% | **10,3%** | 25,9% |

Operativna marža je rasla dok se rast prihoda rušio sa 21,1% na 3,7%. Kriterij K2
gledan izolovano bi rekao "sve odlično" — nije. SBC se ubrzao sa 6,5% na 10,3%
prihoda dok je rast kolabirao.

**RPO / godišnji prihod: 1,05x (2021) → 2,06x (2025).** Backlog je sada dve godine
prihoda. Preko 98% je cloud pretplata sa neotkazivim rokom > 1 god.

**Valuacija — pada u celom rasponu cena:**

| Cena | EV (mln) | P/E adj | FCF yield na EV | nakon SBC |
|---|---|---|---|---|
| 140 | 8.106 | 27,7 | 4,61% | 3,24% |
| 190 | 11.098 | 37,5 | 3,37% | 2,37% |
| 215 | 12.594 | 42,5 | 2,97% | 2,09% |

Konsenzus adjusted EPS 2026 = 5,36 vs FY2025 actual 5,06 = **rast 5,9%**.
Na ceni 190: P/E adj 37,5 / rast 5,9 = **PEG 6,3**. Prag je 2,0.

Za FCF-nakon-SBC yield od 5% cena bi morala biti **92**; za 4% — **114**.

### Verdikt

**Kvalitetan posao po pretkomerno visokoj ceni → WATCHLIST, ne pozicija.**
Trigger za ponovni pogled: cena pod ~130–140 (FCF yield > 4,5%), ILI rast prihoda
nazad iznad 8% god/god dva kvartala zaredom.

### Otvoreno pitanje koje odlučuje tezu

RPO raste 25%, prihod 3,7%. Dve moguće interpretacije:
- (a) odloženo priznavanje koje će se materijalizovati → akcija možda pogrešno cenjena
- (b) cloud ugovori se zaključuju na duže rokove, pa se isti dolar rasteže na više
  godina → RPO rast strukturno precenjuje budući rast prihoda

**Nije rešeno.** Rešava se čitanjem transkripata sa poziva i utvrđivanjem
**prosečnog trajanja ugovora kroz vreme**. Ako se produžilo sa 3 na 5 godina, RPO
rast od 25% je optička iluzija. Ovo je zadatak za Claude Code (istraživanje, ne procena).

---

## 3. Ispravke sistema nastale iz prve analize

Ove su već implementirane u `scripts/scorecard.py`. **Ne vraćaj ih.**

1. **K1-ALT za kapitalno-lake firme.** Ako je investirani kapital ≤ 0 ili < 10%
   prihoda, G1 vraća `N/P` uz obrazloženje i prebacuje se na FCF maržu. Uzrok: MANH
   ima negativan obrtni kapital jer kupci plaćaju avansno (deferred revenue 337.049 >
   ceo kapital 314.765). ROIC prag tada ne nosi informaciju.
2. **`no_financial_debt` flag u meta.** Suzbija "test produktivnosti duga" kada
   kompanija nema finansijski dug. Bez toga je test merio rast zakupa kancelarija i
   davao lažan negativan rezultat.
3. **`docs/05-sektorska-kalibracija.md`** — pragovi ROIC i ND/EBITDA po sektoru.
   Jedinstveni prag ne radi: softveru treba 25%+, industriji 15%+.
4. **Platni sistemi (MA, V), berze i rejting agencije NISU isključeni** kao
   finansijski sektor — ne nose kreditni rizik i ne primaju depozite. Isključene
   ostaju komercijalne/investicione banke, osiguravači, brokeri, BDC, mREIT.

### ZADATAK: CLAUDE.md treba dopuniti

`CLAUDE.md` još ne sadrži ispravke 1–4. Dopuni ga:
- u §1 K1 dodaj pravilo o kapitalno-lakim firmama i K1-ALT
- u §1 K3 dodaj `no_financial_debt` flag
- u §3 kapije: G1 može vratiti `N/P`, i `N/P` se NE računa kao prošla kapija
- u §4 dodaj razjašnjenje o platnim sistemima
- referenciraj `docs/05` za sektorske pragove

---

## 4. Inventar fajlova

```
stock-lab/
├── CLAUDE.md                        specifikacija (TREBA DOPUNITI, vidi §3)
├── README.md                        workflow, quickstart
├── HANDOFF.md                       ovaj fajl
├── docs/
│   ├── 04-sta-ovo-moze-da-dokaze.md statistička ograničenja — NE IGNORISATI
│   └── 05-sektorska-kalibracija.md  pragovi po sektoru + lista kandidata
├── templates/analiza.md             šablon analize
├── scripts/
│   ├── scorecard.py                 5 kriterijuma iz JSON-a (ima K1-ALT ispravku)
│   ├── fill_price.py                popunjava market blok iz jedne cene
│   └── tracker.py                   portfolio vs VUAA + ocena predviđanja
├── data/
│   ├── MANH.json                    KOMPLETNO osim market bloka
│   ├── PRIMER.json                  primer formata, IZMIŠLJENI brojevi
│   ├── watchlist.csv                prazan
│   ├── positions.csv                prazan (obriši PRIMER red ako je ostao)
│   ├── predvidjanja.csv             prazan (obriši PRIMER redove ako su ostali)
│   └── fundamentals_log.csv         prazan
└── analize/                         prazan — MANH.md još nije napisan
```

Sve skripte koriste **samo standardnu Python biblioteku**. Na Windows-u komanda je
`python`, ne `python3`. Ako konzola prikazuje naopake karaktere: `chcp 65001`.

---

## 5. Zadaci — po prioritetu

### Z1. Git init (ako nije urađen) — PRVO
```
git init
git add .
git commit -m "Mission Stock Lab: sistem + MANH analiza"
```
Nije higijena, nego **metodološka zaštita**: sprečava retroaktivno prepravljanje teza
posle nego što se vidi kretanje cene (hindsight bias). Commituj svaku analizu i svaki
unos u `predvidjanja.csv` istog dana. **Nikad `--amend` na stari commit.**
`.gitignore`: samo `__pycache__/`.

### Z2. Očisti PRIMER redove
Iz `data/positions.csv` i `data/predvidjanja.csv`. `data/PRIMER.json` ostaje.

### Z3. Dopuni CLAUDE.md (vidi §3)

### Z4. MANH cena — čeka vlasnika
Vlasnik uzima cenu zatvaranja iz IBKR-a. Zatim:
```
python scripts\fill_price.py data\MANH.json <CENA> --growth 0.059 --dry
python scripts\fill_price.py data\MANH.json <CENA> --growth 0.059
python scripts\scorecard.py data\MANH.json --md > analize\MANH-scorecard.md
```
**Napomena:** web izvori su davali kontradiktorne cene (189,11 / 191,20 / 215,44) i
market cap koji se ne slaže sa brojem akcija. Zato cena ide iz IBKR-a, ne sa weba.
`--growth 0.059` je konsenzus adjusted EPS rast (5,36 vs 5,06).

### Z5. MANH.md analiza
Kopiraj `templates/analiza.md` → `analize/MANH.md`. Popuni sekcije sa podacima
(§1, §3, §4, §5) iz ovog handoff-a i scorecard-a. **Sekcije §2, §6, §7, §8 ostavi
vlasniku** — vidi §6 ispod.

Za §4 (poređenje sa konkurencijom) treba istražiti marže: Descartes Systems (DSGX),
Kinaxis (KXS), SPS Commerce (SPSC), e2open. Blue Yonder je privatna (Panasonic),
SAP EWM i Oracle WMS su segmenti unutar većih firmi — za njih nema izdvojenih marži,
navedi to kao ograničenje umesto da procenjuješ.

### Z6. OTIS — druga analiza
Prikupi FY2021–FY2025 iz 10-K/8-K. **Svrha je metodološka:** OTIS lomi K1/K3 u
**suprotnom smeru od MANH** — verovatno negativan kapital zbog spinoffa iz UTC-a
(2020) finansiranog dugom. Kod MANH je kapital bio mali zbog avansa kupaca, kod OTIS
je negativan zbog poluge. Kad prođeš kroz oba, poznati su oba načina na koja
kriterijumi zavaravaju.

Za OTIS koristi Neto dug/EBITDA i pokrivenost kamata; D/E ignoriši (biće negativan
i besmislen). Prag ND/EBITDA za industriju: 3,0x (`docs/05`).

### Z7. Red kandidata posle OTIS-a
| # | Ticker | Sektor | Zašto |
|---|---|---|---|
| 3 | CPRT | Aukcije/potrošnja | Kontrolni slučaj — sistem mora umeti reći "prolazi čisto" |
| 4 | PRGS | Softver | G2 verovatno pada (ND/EBITDA ~3,8x); vlasnikov krug kompetencije (Telerik) |
| 5 | MEDP ili IDXX | Zdravstvo | Provera da li K1-ALT generalizuje (MEDP ima isti avansni model kao MANH) |

Pravilo: **max 3 pozicije iz istog sektora.** 10 softverskih firmi nisu 10 opklada
nego jedna; bez sektorske raznovrsnosti `predvidjanja.csv` nema nezavisna opažanja.

---

## 6. Podela rada — OBAVEZNO

Vlasnik je u chat-u pitao da Claude odradi celu analizu. **To se ne sme prihvatiti u
celini**, i razlog nije formalan.

Ceo validacioni mehanizam (`docs/04`) počiva na merenju **vlasnikove** tačnosti
predviđanja i kalibracije samopouzdanja. Ako Claude napiše moat i pet predviđanja,
`predvidjanja.csv` posle 12 meseci meri Claude-ovu kalibraciju, ne vlasnikovu — a to
je bio jedini statistički dostižan cilj projekta.

| Claude radi | Vlasnik radi |
|---|---|
| Prikupljanje podataka iz izveštaja, sa izvorima | Moat u dve rečenice |
| Izračuni, scorecard, analiza osetljivosti | Tri stvari koje bi opovrgle tezu |
| Istraživanje konkurencije, transkripata, trajanja ugovora | Pet merljivih predviđanja + nivo uverenosti (50/70/90%) |
| Popunjavanje sekcija analize koje su činjenične | Odluka: pozicija / watchlist / odbijeno |

Claude može da **ponudi kandidat-formulacije** za moat ili predviđanja, jasno
označene kao predlog, ali vlasnik ih mora prepisati ili odbaciti svojim rečima.

---

## 7. Pravila ponašanja (izvod iz CLAUDE.md, ponovljeno jer je kritično)

1. **Nikad ne izmišljaj finansijske brojeve.** Nema podatka → `N/A — treba proveriti`.
   Nikad procena predstavljena kao činjenica.
2. Svaki broj ima izvor i datum. Bez izvora ne ulazi u scorecard.
3. **Agregatori (stockanalysis, GuruFocus, Yahoo, TipRanks) ne idu u scorecard.**
   Primarni izvor je SEC EDGAR / 8-K Exhibit 99.1 / 10-K. Dokazan primer: za MANH ROIC
   je GuruFocus davao 28,4%, stockanalysis 309,7% — oba "tačna" po svojoj metodologiji.
4. Ne daj buy/sell preporuku. Daj popunjen scorecard, rizike, otvorena pitanja.
5. Nikad ne preporučuj pomeranje kapitala iz Mission 1M u satelit.
6. Ako kompanija pada u isključeni sektor — reci i stani. Ne prilagođavaj metriku da
   analiza "prođe".
7. **Datum i cena ulaza se ne biraju retroaktivno.** Cena ulaza = cena zatvaranja na
   dan unosa. Uz nju obavezno VUAA cena istog dana (benchmark).
8. Odgovori na srpskom. Vlasnik preferira preciznost nad brzinom i tačne loše vesti
   nad netačnim dobrim. Ispravljaj greške u pretpostavkama eksplicitno.

---

## 8. Nerešeno, van softvera

1. **Poresko tretiranje kapitalnog dobitka i dividendi za pojedinačne akcije preko
   IBKR, za srpskog rezidenta.** Nije verifikovano. Materijalno menja neto prinos.
   Poreski savetnik, ne Claude, ne Google. Nije blokada dok je paper trading.
2. Potvrda da satelit ($1.000 × N pozicija) ostaje ≤ 10% ukupnog portfolija.
3. Odluka o prelasku na mali realan iznos. Paper trading uklanja emotivni pritisak —
   varijablu koja najverovatnije uzrokuje gubitke. Preporuka iz chat-a: mali realan
   iznos je bolji test ponašanja od papira.
