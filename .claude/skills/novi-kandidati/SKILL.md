---
name: novi-kandidati
description: Predlaže nove kandidate za analizu u datom sektoru, poštujući sektorske kapice i popunjenost portfolija (docs/05 §6). Koristi kad Dragan traži "novi kandidati" za neki sektor ili opšte "traži dalje".
---

# Traženje novih kandidata

**Argument:** sektor (npr. "Zdravstvo", "Softver") ili prazno za opšte skeniranje.

## Korak 1 — Proveri prostor

1. Pročitaj `data/positions.csv` — koliko pozicija je aktivno (status active/open) i
   iz kojih sektora, prema `docs/05-sektorska-kalibracija.md` §6 (max 3 softver, max 2
   industrija/zdravstvo/potrošnja-distribucija, max 1 infrastruktura tržišta, max
   8-12 ukupno po CLAUDE.md §7).
2. Ako je traženi sektor pun, ili je portfolio pun (10-12 pozicija) — reci to
   eksplicitno Draganu **pre** predlaganja kandidata. Kandidati u tom slučaju idu
   samo u `data/watchlist.csv`, ne mogu ući u poziciju dok se slot ne oslobodi
   (izlazna pravila neke postojeće pozicije se aktiviraju).
3. Proveri `data/watchlist.csv` — da li su kandidati za taj sektor već predloženi
   ranije i odbačeni/watchlistovani? Ne duplira posao bez razloga.

## Korak 2 — Predloži kandidate

- Predloži 2-4 tikera koji spadaju u traženi sektor, sa kratkim obrazloženjem zašto
  su zanimljivi kandidati (šta bi mogli da dokažu ili slome u metodologiji — vidi
  stil `docs/05` §4 "šta će slomiti sistem").
- Prioritizuj Draganov krug kompetencije (IT/.NET/softver/enterprise SaaS, CLAUDE.md
  §2) kad je relevantno, ali ne isključivo — projekat namerno testira metodologiju
  van kruga kompetencije takođe.
- Izbegavaj već isključene sektore (CLAUDE.md §4) i firme sa <5g javne istorije osim
  ako Dragan eksplicitno odobri izuzetak (kao kod IREN).
- Koristi `AskUserQuestion` da Dragan izabere finalne 2-3 od predloženih, umesto da
  sam biraš umesto njega.

## Korak 3 — Predaj izabrane analizi

Za svaki izabrani tiker pokreni skill `analiza-kompanije` (Faza 1 provera
prihvatljivosti prvo — sektor/limit/istorija), ne skači direktno na prikupljanje
podataka.
