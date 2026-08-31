# Analiza: S&P Global Inc. (SPGI)

**Datum:** 2026-08-31 | **Analitičar:** Dragan
**Status:** **ODBIJENO** — hard kapija G1 (ROIC) pala, bez override-a.

> Sekcije 1, 3, 9 popunio Claude — činjenično, sa izvorima. Sekcije 2/6/7 (moat,
> opovrgavajuće tačke, predviđanja) se ne popunjavaju — akcija ne ulazi dalje u
> proces jer je hard kapija pala (vidi `HANDOFF.md` §6, CLAUDE.md §3).

---

## 1. Šta kompanija zapravo radi

S&P Global posluje kroz **pet izveštajnih segmenata**: Ratings (S&P Global Ratings —
NRSRO rejting agencija), Market Intelligence, Energy (bivši Commodity Insights),
Mobility, i Indices (S&P Dow Jones Indices — joint venture sa CME Group). Ratings
segment je FY2025 činio **~30% ukupnog prihoda** ($4.549 mlrd od $15.336 mlrd) —
znatno manji udeo nego kod Moody's-a (~53%), jer je akvizicija IHS Markit (zatvorena
28.2.2022, "merger of equals") uglavnom uvećala Market Intelligence, Mobility i
Energy segmente.

**Regulatorni status:** S&P Global Ratings je registrovan kao NRSRO kod SEC-a.
10-K pominje rizik od državno-podržanih lokalnih rejting agencija kao konkurencije,
bez direktnog imenovanja Moody's/Fitch u izvučenom delu teksta.

*Izvor: Form 10-K FY2025, CIK 0000064040, accession 0000064040-26-000013, Item 1.*

---

## 2. Moat — NE POPUNJAVA SE (akcija odbijena pre ove faze)

---

## 3. Scorecard — HARD KAPIJA G1 PALA

```
SCORECARD — S&P Global Inc. (SPGI)
Sektor: Rejting/podaci - infrastruktura tržišta

G1 (ROIC ≥25% sektorski prag za rejting agencije, opšti minimum 12%): PAO
    — medijana 8,0%, WACC nije unet ali spread je irelevantan jer medijana
    vec pada ispod OPŠTEG minimuma od 12%
G2 (Neto dug/EBITDA ≤3.0x, pokrivenost kamata ≥4x): PROŠAO — 1,48x / 22,6x
G3 (FCF pozitivan ≥4/5 god.): PROŠAO — 5/5
G4 (FCF konverzija ≥0.7): PROŠAO — 1,20
G5 (Moat u 2 rečenice): NIJE POPUNJENO (nepotrebno — G1 već pao)
G6 (Nije u isključenom sektoru): PROŠAO

Prošlo: 4/6 (G5 nepopunjeno) | PALO: 1 (G1)
```

**Detalji ROIC po godini:** FY2021 **-942,4%** | FY2022 8,0% | FY2023 7,1% |
FY2024 10,2% | FY2025 11,8%. Medijana 5g = **8,0%**.

**Uzrok — dva odvojena efekta koja se preklapaju:**

1. **FY2021 je numerički artefakt, ne signal.** Pre IHS Markit akvizicije,
   investirani kapital (dug + equity − gotovina) je bio blago **negativan**
   ($4.114M duga + $2.032M equity − $6.497M gotovine = **-$351M**) jer je SPGI
   držao neuobičajeno mnogo gotovine u odnosu na skroman kapitalni bilans.
   Deljenje pozitivnog NOPAT-a negativnim brojem daje besmislen rezultat
   (-942%) — isti mehanizam kao K1-ALT2 (OTIS/ORLY), samo što je ovde uzrok
   visak gotovine, ne negativan equity.

2. **FY2022-FY2025 (7,1%-11,8%) NIJE artefakt — ovo je stvaran signal.**
   IHS Markit akvizicija (zatvorena feb. 2022, "merger of equals") je preko
   noći podigla goodwill sa $3,5 mlrd na $34,5 mlrd i equity sa $2,0 mlrd na
   $36,4 mlrd. Investirani kapital je posle akvizicije mnogo veći, a
   operativna zarada nije rasla proporcionalno — **standardni ROIC posle
   akvizicije (7-12%) je ispod čak i opšteg 12% minimuma, kamoli sektorskog
   praga od 25%+ za rejting agencije.**

**Kontrolna provera (CLAUDE.md K1 nalog — "izračunaj i ROIC ex-goodwill, ali ne
koristi samo tu verziju"):** ROIC ex-goodwill za FY2025 (investirani kapital
minus goodwill od $36,475 mlrd) izlazi na **~83,6%** — ekstremno visok. Ovo
potvrđuje da je **osnovni operativni posao odličan**, ali da je akvizicija IHS
Markit-a **realno potrošila akcionarski kapital** po ceni koja trenutna zarada
ne opravdava po standardnom ROIC testu. Tačno upozorenje iz CLAUDE.md K1:
"akvizicije su realno potrošen kapital akcionara" — ne treba koristiti
ex-goodwill verziju kao izgovor da se kapija zaobiđe.

**Napomena o equity strukturi:** SPGI ima značajan "Redeemable noncontrolling
interest" (S&P Dow Jones Indices JV sa CME Group, $4,9 mlrd FY2025) koji je
KLASIFIKOVAN VAN equity sekcije bilansa (mezzanine stavka) — ovo blago
**podcenjuje** investirani kapital u odnosu na 100%-konsolidovan EBIT, što znači
da je standardni ROIC (7-12%) ako nešto **blago naduvan** u odnosu na stvarnu
ekonomsku sliku, ne obrnuto. Ovo dodatno učvršćuje zaključak da kapija zasluženo
pada.

---

## 4. Poređenje sa konkurencijom — NIJE RAĐENO (nepotrebno, akcija već odbijena)

Za kontekst: Moody's (MCO), direktan analog u istom sektoru, je u istoj analitičkoj
seriji prošao G1 čisto (medijana ROIC 25,5%, bez akvizicione distorzije uporedive
veličine) — vidi `analize/MCO.md`.

---

## 5. Valuacija — NIJE RAĐENO (nepotrebno, akcija već odbijena)

---

## 6-7. Opovrgavajuće tačke / predviđanja — NE POPUNJAVA SE

---

## 8. Odluka

- [x] **Odbijeno**
- **Razlog:** Hard kapija G1 (ROIC) pada — medijana 8,0% je ispod i opšteg
  praga (12%) i sektorskog praga za rejting agencije (25%+). Uzrok je
  identifikovan i razumljiv (IHS Markit akvizicija 2022. je goodwill-om
  naduvala investirani kapital iznad onoga što trenutna zarada opravdava), ali
  po CLAUDE.md §3 pravilu pad hard kapije zahteva **pisano obrazloženje
  override-a** da bi se nastavilo dalje, a takvo obrazloženje nije napisano
  (dosledno sa PRGS i IREN ranije u projektu — bez override-a do sada).
- Nema upisa u `positions.csv`, `watchlist.csv` ni `predvidjanja.csv`.

---

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| SPGI FY2023-FY2025 finansijski podaci | 10-K FY2025, R3/R5/R7.htm — lično verifikovano na SEC EDGAR | sec.gov/Archives/edgar/data/64040/000006404026000013/ | podnet 11.02.2026 |
| SPGI FY2021-FY2022 finansijski podaci (uklj. IHS Markit skok) | 10-K FY2022 (accession 0000064040-23-000058), R3/R5/R7.htm — lično verifikovano | sec.gov/Archives/edgar/data/64040/000006404023000058/ | podnet 10.02.2023 |
| SPGI FY2023 bilans (potvrda duga/equity) | 10-K FY2024 (accession 0000064040-25-000052), R5.htm | sec.gov/Archives/edgar/data/64040/000006404025000052/ | podnet 11.02.2025 |
