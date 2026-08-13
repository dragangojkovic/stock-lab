# Mission Stock Lab

Sistem za analizu pojedinačnih akcija po 5 kriterijuma + paper trading evidencija.
Satelit uz **Mission 1M** (koji ostaje netaknut).

---

## Pre nego što bilo šta uradiš

Pročitaj **`docs/04-sta-ovo-moze-da-dokaze.md`**.

Kratko: cilj "dokazaćemo teoriju kroz prinos paper portfolija" je matematički
nedostižan u razumnom roku (potrebno 16–28 godina za statističku značajnost).
Cilj je zato preformulisan na nešto što je dostižno za 12 meseci: **tačnost
predviđanja fundamenata**. Prinos protiv VUAA se meri i evidentira, ali se ne
tretira kao dokaz.

---

## Struktura

```
mission-stock-lab/
├── CLAUDE.md                        ← specifikacija sistema; Claude ovo čita pre analize
├── README.md                        ← ovaj fajl
├── docs/
│   └── 04-sta-ovo-moze-da-dokaze.md ← statistička ograničenja (OBAVEZNO)
├── templates/
│   └── analiza.md                   ← šablon za analizu jedne kompanije
├── scripts/
│   ├── scorecard.py                 ← računa 5 kriterijuma iz JSON-a
│   └── tracker.py                   ← portfolio vs VUAA + ocena predviđanja
├── data/
│   ├── PRIMER.json                  ← primer ulaznog fajla (IZMIŠLJENI brojevi)
│   ├── watchlist.csv                ← kandidati u obradi
│   ├── positions.csv                ← paper pozicije + benchmark cene
│   ├── predvidjanja.csv             ← merljiva predviđanja + ishodi ← GLAVNI TEST
│   └── fundamentals_log.csv         ← kvartalni fundamenti po poziciji
└── analize/                         ← popunjene analize (jedan .md po kompaniji)
```

---

## Quickstart

```bash
# 1. Test da sve radi
python3 scripts/scorecard.py data/PRIMER.json
python3 scripts/tracker.py

# 2. Obriši primer redove iz positions.csv i predvidjanja.csv

# 3. Za novu kompaniju: kopiraj PRIMER.json, popuni pravim podacima
cp data/PRIMER.json data/XYZ.json
# ... popuni ...
python3 scripts/scorecard.py data/XYZ.json --md > analize/XYZ-scorecard.md

# 4. Popuni templates/analiza.md → analize/XYZ.md
```

Skriptovi koriste samo standardnu Python biblioteku — rade i lokalno i u Claude
okruženju bez instalacije.

---

## Ritam rada

| Frekvencija | Šta | Vreme |
|---|---|---|
| Po kandidatu | Prikupljanje podataka + scorecard + analiza | 3–5h (realno, prvi put i više) |
| Mesečno | Ažuriraj cene u `positions.csv`, pokreni `tracker.py` | 15 min |
| Kvartalno | Fundamenti u `fundamentals_log.csv`, oceni predviđanja, proveri kapije | 2–3h |
| Godišnje | Pregled: tačnost predviđanja, kalibracija, da li nastavljam | 2h |

**Iskrena provera realnosti:** ako 10 pozicija zahteva 3–5h analize svaka plus
2–3h kvartalno, to je ~50h inicijalno i ~10h kvartalno. Uz full-time .NET posao.
Ako to nije održivo, bolje je 4–5 pozicija dobro odrađenih nego 12 površno.

---

## Kako se koristi sa Claude-om

Reci: *"Otvori mission-stock-lab, pročitaj CLAUDE.md, i uradimo analizu {kompanija}."*

Claude tada:
1. Proveri da sektor nije isključen i da ima 5 god. javne istorije
2. Prikuplja podatke sa navođenjem izvora (i eksplicitno označava šta nije našao)
3. Popunjava JSON, pokreće scorecard
4. Popunjava `templates/analiza.md` — uključujući tri stvari koje bi opovrgle tezu
5. **Ne daje buy/sell preporuku** — daje popunjen scorecard, rizike i otvorena pitanja

---

## Nerešeno — reši pre realnog kapitala

1. **Poresko tretiranje kapitalnog dobitka i dividendi za pojedinačne akcije preko
   IBKR, za srpskog rezidenta.** Stopa, obaveza samostalne prijave, withholding tax
   na dividende (i da li W-8BEN utiče), eventualni period držanja koji menja obavezu.
   **Ovo nije verifikovano u projektu i materijalno menja neto prinos.** Poreski
   savetnik, ne Google, ne Claude.
2. Konkretan iznos satelita. Potvrdi da je ≤ 10% ukupnog portfolija i da je to suma
   koju možeš izgubiti u celosti bez uticaja na cilj od $1M do 2036.
3. Paper only, ili paper + mali realan iznos? Paper ne testira ponašanje — emotivni
   pritisak realnog novca je ono što razbija disciplinu, i ta varijabla je uklonjena
   iz paper testa.
4. Ako želiš mid-cap tezu iz Grahamovog poglavlja 7 bez idiosinkratičnog rizika
   pojedinačne firme — to je mid-cap ETF tilt, ne stock-picking. Dve različite odluke,
   ne mešati ih.
