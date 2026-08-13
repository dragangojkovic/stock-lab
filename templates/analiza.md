# Analiza: {NAZIV} ({TIKER})

**Datum:** {YYYY-MM-DD} | **Analitičar:** Dragan | **Cena na dan analize:** {cena}
**U krugu kompetencije:** DA / NE — obrazloži: {…}

> Pravilo: nijedno polje ne ostaje prazno. Ako podatak nije dostupan, upiši
> `N/A — treba proveriti` i navedi šta konkretno treba naći. Prazno polje = nepotpuna
> analiza, a nepotpuna analiza ne ide u portfolio.

---

## 1. Šta kompanija zapravo radi

U 3–4 rečenice, bez marketinškog jezika. Ako ne možeš da objasniš odakle dolazi novac
i kome se šta prodaje, preskoči akciju.

- Izvori prihoda i njihov udeo: {…}
- Ko su kupci: {…}
- Kako se naplaćuje (jednokratno / pretplata / transakciono): {…}
- Koncentracija: top kupac / top 10 kupaca kao % prihoda: {…}

## 2. Moat — dve rečenice (obavezna kapija)

> {Rečenica 1: izvor prednosti.}
> {Rečenica 2: dokaz da prednost postoji, izmerljiv.}

- Kategorija: switching costs / mrežni efekat / obim / brend / regulativa / IP
- **Šta bi ubilo ovaj moat u 5 godina:** {…}
- **Zašto konkurent sa dovoljno kapitala to ne može odmah da replicira:** {…}

## 3. Scorecard

Priloži izlaz iz `python3 scripts/scorecard.py data/{TIKER}.json`

```
{ovde nalepiti izlaz}
```

**Kapije:** prošlo {x}/6 | palo {y} | nepoznato {z}
**Override (ako je kapija pala):** {obrazloženje ili "nema"}

## 4. Poređenje sa konkurencijom

| Metrika | {TIKER} | Konk. 1 | Konk. 2 | Konk. 3 | Medijana grane |
|---|---|---|---|---|---|
| ROIC (5g med.) | | | | | |
| Bruto marža | | | | | |
| Operativna marža | | | | | |
| Neto marža | | | | | |
| Neto dug/EBITDA | | | | | |
| FCF konverzija | | | | | |
| P/E | | | | | |
| PEG (trailing) | | | | | |
| FCF yield na EV | | | | | |

**Ako marža pada — pada li svima u grani ili samo njoj?** {…}
(Ako svima → makro/ciklično. Ako samo njoj → problem specifičan za kompaniju.)

## 5. Valuacija — dve nezavisne provere

| Metod | Rezultat | Šta pretpostavlja |
|---|---|---|
| PEG_trailing | | prošli rast se nastavlja |
| PEG_forward | | konsenzus analitičara je tačan |
| FCF yield na EV | | ništa — samo tekući cash flow |
| FCF yield nakon SBC | | dilacija je realan trošak |

**Razlika između PEG_trailing i PEG_forward:** {…}
Ako je forward mnogo niži — koje konkretno ubrzanje konsenzus pretpostavlja i zašto
bi se ostvarilo? {…}

## 6. Tri stvari koje bi opovrgle tezu (obavezno)

Ne "rizici" u opštem smislu — konkretne, merljive stvari koje bi te naterale da
promeniš mišljenje.

1. {…}
2. {…}
3. {…}

**Šta je najjači argument protiv kupovine ove akcije?** (napiši ga kao da ga piše
neko ko shortuje) {…}

## 7. Merljiva predviđanja za 4 kvartala — SRCE SISTEMA

Ova predviđanja se upisuju u `data/predvidjanja.csv` i ocenjuju kvartalno.
Moraju biti merljiva, sa numeričkim pragom i deklarisanim nivoom uverenosti.

| # | Predviđanje | Merljiv prag | Uverenost |
|---|---|---|---|
| 1 | | | 50/70/90% |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## 8. Odluka

- [ ] Ulazi u paper portfolio
- [ ] Watchlist — čekam {konkretan trigger, ne "bolju cenu"}
- [ ] Odbijeno — razlog: {…}

**Datum ulaza:** {datum unosa, NE retroaktivan}
**Cena ulaza:** {cena zatvaranja tog dana}
**VUAA cena istog dana:** {…} ← obavezno za benchmark
**Veličina pozicije:** {1/N satelita}

**Izlazna pravila (definisana SADA, vezana za tezu ne za cenu):**
1. {…}
2. {…}
3. {…}

## 9. Izvori

| Podatak | Izvor | Strana/link | Datum |
|---|---|---|---|
| | | | |
