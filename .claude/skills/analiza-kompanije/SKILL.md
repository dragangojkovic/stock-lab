---
name: analiza-kompanije
description: Kompletna analiza jedne kompanije po Mission Stock Lab metodologiji (CLAUDE.md §5, Faza 1-5). Koristi kad Dragan traži analizu konkretnog tikera (npr. "analiziraj OTIS", "uradi CPRT").
---

# Analiza kompanije — Faza 1-5

Ovo je operativna procedura iz `CLAUDE.md` §5, sa podelom rada iz `HANDOFF.md` §6.
Pre svega pročitaj `CLAUDE.md` i `docs/05-sektorska-kalibracija.md` ako nisu već u
kontekstu — ne improvizuj van njih.

**Argument:** tiker kompanije (npr. `OTIS`). Ako fali, pitaj.

## Faza 1 — Provera prihvatljivosti

1. Da li sektor pada u isključene (CLAUDE.md §4: banke, osiguranje, REIT, pre-profit/
   biotech, duboko ciklične na ekstremu, <5g javne istorije)? Platni sistemi/berze/
   rejting agencije **nisu** isključeni (§4 razjašnjenje).
2. Ima li ≥5 godina javnih finansijskih izveštaja?
3. Proveri `docs/05-sektorska-kalibracija.md` §2 za sektorske pragove (K1/K3/K5) i §4
   da li je već hipoteza/kandidat.
4. Proveri `data/watchlist.csv` i `data/positions.csv` — da li je već analizirana? Ne
   ponavljaj prikupljene podatke bez razloga.
5. Proveri sektorski limit iz `docs/05` §6 (max 3 softver, max 2 industrija/zdravstvo/
   potrošnja, max 1 infrastruktura tržišta) i broj slobodnih slotova u portfoliju
   (max 8-12 pozicija, §7). Ako je portfolio pun ili sektor pun — kandidat ide najviše
   do Watchlist-a, ne u poziciju.

Ako ne prolazi — stani, objasni zašto, ne nastavljaj na Fazu 2.

## Faza 2 — Prikupljanje podataka

Prikupi za 5 fiskalnih godina + TTM: Prihod, COGS, SG&A, R&D, EBIT, Rashodi kamata,
Neto dobit, Efektivna poreska stopa, D&A, SBC, Promene obrtnog kapitala, OCF, CapEx,
Ukupan dug, Gotovina, Ukupan kapital, Broj akcija (diluted), Potraživanja, Zalihe.

**Izvori — striktno:**
- Finansijski brojevi → **samo** SEC EDGAR 10-K / 8-K Exhibit 99.1. Nikad agregatori
  (stockanalysis, GuruFocus, Yahoo, TipRanks) za brojeve koji ulaze u scorecard.
- Cena akcije i VUAA → **samo** IBKR zaključna cena (screenshot od Dragana), nikad
  intraday ni sa weba.
- Beta (5g) → stockanalysis.com dozvoljeno, ali eksplicitno označi kao treću stranu.
- 10Y UST prinos (za WACC) → treasury.gov, isti datum kao cena.
- Konsenzus EPS rast → finviz ili slično, eksplicitno označi kao treću stranu.
- Svaki broj → izvor + datum. Bez izvora → `N/A — treba proveriti`, ne ulazi u scorecard.

Za veći obim istraživanja (npr. 5 godina 10-K iskopavanja, poređenje sa 3-5
konkurenata) koristi Agent tool (subagent) da ne puni glavni kontekst — ali **uvek
lično verifikuj** ključne brojeve pre upisa u JSON (agent može halucinirati ili
pobrkati restated/originalne verzije, kao što se desilo kod DXCM ASU 2020-06).

Proveri poznate zamke pre upisa:
- Serijski akvizitori → izračunaj i ROIC ex-goodwill (CLAUDE.md K1).
- Kapitalno-lake firme (investirani kapital ≤0 ili <10% prihoda) → K1-ALT, G1 vraća `N/P`.
- Negativan equity → K1-ALT2, D/E besmislen, osloni se na Neto dug/EBITDA + pokrivenost.
- Non-calendar fiskalna godina, divestiture/spinoff restatement, split-adjustment.

## Faza 3 — Izračun

1. Kopiraj `data/PRIMER.json` → `data/{TICKER}.json`, popuni sa izvorima (dodaj
   `_napomena_*` polja za svaku netrivijalnu odluku — restatement, ex-goodwill,
   sektorski override).
2. `python scripts/validate_json.py data/{TICKER}.json`
3. Sačekaj cenu od Dragana (IBKR zaključna, uz VUAA istog dana), zatim:
   ```
   python scripts/fill_price.py data/{TICKER}.json <CENA> --growth <konsenzus_rast> --dry
   python scripts/fill_price.py data/{TICKER}.json <CENA> --growth <konsenzus_rast>
   ```
4. Izračunaj WACC bottom-up: CoE = rf(10Y UST) + beta×4.5% ERP; CoD = interest_expense/
   prosečan ukupan dug, poreski efektovan (efektivna stopa, ili normalizovanih 21% ako
   je efektivna anomalna). Upiši u JSON sa napomenom o pretpostavkama.
5. `python scripts/scorecard.py data/{TICKER}.json --md > analize/{TICKER}-scorecard.md`

## Faza 4 — Analiza (šablon `templates/analiza.md`)

Kopiraj šablon u `analize/{TICKER}.md`. **Popuni SAMO sekcije koje su Claude-ov posao**
(HANDOFF.md §6):
- §1 Šta kompanija radi
- §3 Scorecard (nalepi izlaz) + override obrazloženje ako je kapija pala
- §4 Poređenje sa 3-5 konkurenata (marže, ROIC, zaduženost — istraženo, ne procenjeno)
- §5 Valuacija (PEG_trailing/forward, FCF yield na EV)
- §9 Izvori

**NE popunjavaj** §2 (moat), §6 (tri opovrgavajuće tačke), §7 (predviđanja), §8
(odluka) — to je vlasnikov posao. Možeš ponuditi **predlog**, jasno obeležen kao
predlog, u odvojenoj poruci Draganu — ne upisuj ga direktno u fajl kao gotovo.

Kad prezentuješ rezultat, daj Draganu "predlog paket": predloženi moat, tri
opovrgavajuće tačke, bear case, pet merljivih predviđanja sa nivoom uverenosti,
predlog odluke — sve jasno označeno kao predlog za njegovo odobrenje/prepravku.

## Faza 5 — Odluka i evidencija (tek posle Draganovog "važi")

1. Ako ulazi u portfolio: dodaj red u `data/positions.csv` (append, datum unosa =
   danas, cena = zaključna tog dana, nikad retroaktivno) i 5 redova u
   `data/predvidjanja.csv` (append).
2. Ako watchlist: dodaj red u `data/watchlist.csv` sa konkretnim trigger uslovom.
3. Ako odbijeno: samo `analize/{TICKER}.md` sa razlogom, nema CSV upisa.
4. Commituj sve odjednom, isti dan, opisnom porukom na srpskom. Nikad `--amend`.

## Definicija završenog (CLAUDE.md §10)

Ne javljaj analizu kao završenu dok nije: svaki broj sa izvorom, scorecard pokrenut i
sačuvan, Claude-ove sekcije u `analize/{TICKER}.md` popunjene, vlasnikove sekcije
prazne ili jasno obeležene kao predlog, CSV upisi (ako ih ima) neretroaktivni, sve
komitovano isti dan.
