---
name: kvartalni-pregled
description: Kvartalni pregled fundamenata i ocena prethodnih predviđanja (CLAUDE.md §6-7). Koristi kad stigne novi 10-Q/10-K alert (data/quarterly_alerts.md) ili kad Dragan traži kvartalni pregled.
---

# Kvartalni pregled

Ovo je srce validacionog mehanizma projekta (CLAUDE.md §6) — meri se tačnost
predviđanja fundamenata, ne prinos portfolija.

## Kada se pokreće

- Kad `scripts/quarterly_monitor.py` (lokalni Task Scheduler job) upiše novi unos u
  `data/quarterly_alerts.md` za neki tiker iz `data/positions.csv`.
- Ili kad Dragan eksplicitno traži kvartalni pregled za poziciju.

## Koraci

1. Pronađi 5 otvorenih predviđanja za taj tiker u `data/predvidjanja.csv` (kolone
   `ishod`/`realizovana_vrednost` prazne, `kvartal_provere` odgovara novom izveštaju).
2. Iz novog 10-Q/10-K (SEC EDGAR, primarni izvor — nikad agregator) izvuci realizovane
   vrednosti za svaki merljiv prag: ROIC, operativna marža, Neto dug/EBITDA, FCF
   konverzija, broj akcija, rast prihoda — šta god je konkretno traženo u koloni
   `predvidjanje`/`merljiv_prag`.
3. Za svako predviđanje upiši u `data/predvidjanja.csv`:
   - `ishod` = ISTINITO / NETAČNO (uporedi realizovanu vrednost sa merljivim pragom)
   - `realizovana_vrednost` = stvarni broj sa izvorom
   - Ovo je izmena POSTOJEĆEG reda (ishod/realizovana_vrednost su predviđene za to),
     **ne** novi red — koristi Write sa punim sadržajem fajla. `csv_integrity.py` hook
     dozvoljava promenu ishod/realizovana_vrednost/napomena, ali blokira svaku izmenu
     ticker/datum_unosa/kvartal_provere/predvidjanje/merljiv_prag/uverenost (teza se
     ne prepravlja retroaktivno).
4. Proveri hard kapije za tu poziciju ponovo (ROIC, ND/EBITDA, FCF) — ako je neka
   pala dva kvartala zaredom, flaguj izlazno pravilo iz `analize/{TICKER}.md` §8, ali
   ne zatvaraj poziciju sam.
5. Ako se skupilo dovoljno kvartala (4+) za neku poziciju, izračunaj % tačnih
   predviđanja i prijavi Draganu (CLAUDE.md §6: 70%+ = sistem ima sadržaj, ~50% = ne
   razlikuje ništa).
6. Komituj `data/predvidjanja.csv` promenu, opisna poruka na srpskom, isti dan.
