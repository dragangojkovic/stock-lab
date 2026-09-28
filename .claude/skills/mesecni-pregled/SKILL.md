---
name: mesecni-pregled
description: Mesečni pregled paper portfolija naspram VUAA benchmarka (CLAUDE.md §7). Koristi kad Dragan traži "mesečni pregled", "pokreni tracker", ili pita za PNL portfolija.
---

# Mesečni pregled portfolija

Iz CLAUDE.md §7: "Mesečni pregled: ažuriraj cene, pokreni scripts/tracker.py."

## Koraci

1. Za svaku aktivnu poziciju u `data/positions.csv` (status `active`), zatraži od
   Dragana IBKR zaključnu cenu (ne intraday, ne agregator) — jednu po jednu ili sve
   odjednom ako ih ima spreman.
2. Zatraži i VUAA zaključnu cenu istog dana (benchmark, obavezan za svaku poziciju).
3. Ažuriraj kolone `current_price` i `benchmark_current_price` u `data/positions.csv`
   koristeći **Write** (pun sadržaj fajla) — ne Edit. Ovo je jedina legitimna izmena
   postojećih redova (CLAUDE.md dozvoljava mutaciju current_price; entry_date/
   entry_price/teza ostaju nepromenjeni). Hook `csv_integrity.py` će odbiti write ako
   slučajno promeniš neizmenjivo polje (ticker, naziv, entry_date, entry_price,
   benchmark_entry_price, weight, teza_kratko, izlazno_pravilo).
4. Pokreni:
   ```
   python scripts/tracker.py
   ```
5. Prijavi Draganu: PNL po poziciji i agregatno, poređeno sa VUAA total return za isti
   period držanja (CLAUDE.md §7 — obavezan benchmark, "zaradio sam 9%" nema značenje
   bez indeksa).
6. Ako neko izlazno pravilo (definisano pri ulazu, u `izlazno_pravilo` koloni) izgleda
   aktivirano na osnovu ovih cena ili poznatih fundamentala — flaguj to eksplicitno,
   ali **ne zatvaraj poziciju sam** — to je vlasnikova odluka.
7. Komituj `data/positions.csv` promenu (samo cene, opisna poruka na srpskom).
