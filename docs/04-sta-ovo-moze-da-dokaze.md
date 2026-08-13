# Šta ovaj eksperiment može, a šta ne može da dokaže

Ovo je najvažniji dokument u projektu. Pročitaj ga pre nego što uložiš mesece rada
u nešto što neće dati odgovor koji tražiš.

---

## Problem: rekao si "radićemo demo trgovanje određeni period kako bismo dokazali teoriju"

Ta rečenica sadrži pretpostavku koja ne stoji. **Paper trading kroz 6–24 meseca sa
8–12 pozicija ne može da dokaže ni da okvir radi, ni da ne radi.** Ne zato što je
okvir loš, nego zato što matematika ne dozvoljava.

## Matematika

Da bi razlikovao stvarnu sposobnost (alfa) od sreće, potreban ti je statistički
značajan uzorak. Formula za t-statistiku alfe:

```
t = (alfa / tracking error) × √(broj godina)
```

Za konvencionalni prag značajnosti t ≈ 2, potreban broj godina je:

```
godine = (2 × TE / alfa)²
```

Realni brojevi za koncentrisan portfolio od 10 akcija:

| Prava alfa | Tracking error | Godine potrebne za t=2 |
|---|---|---|
| 2% god. | 8% | **64 godine** |
| 3% god. | 8% | **28 godina** |
| 5% god. | 8% | **10 godina** |
| 3% god. | 6% | **16 godina** |

Čak i da tvoj okvir stvarno donosi 3% godišnje iznad indeksa — što bi bio izvanredan
rezultat — trebalo bi ti oko **16–28 godina** da to statistički dokažeš.

**Šta to znači za 12 meseci:** rezultat od +20% ili −20% u odnosu na VUAA je unutar
normalnog šuma za portfolio od 10 akcija. Nijedan od tih ishoda ti ne govori ništa o
kvalitetu okvira. Dobiće ti signal koji ćeš pogrešno interpretirati — i to je gore od
nedostatka signala, jer ćeš doneti odluku na osnovu šuma.

## Dodatni problemi koje ova vrsta eksperimenta ima

**1. Nedovoljan broj nezavisnih opažanja.** 10 akcija u istom periodu nisu 10
nezavisnih testova. Ako sve budu tech, ti u suštini imaš **jedan** test — test na
tech sektor u tom makro režimu.

**2. Paper trading ne testira ponašanje.** Najverovatniji način na koji ćeš izgubiti
novac u stock-picking-u nije loša analiza — nego panika, prerano izlaženje,
dokupljivanje u padu bez teze, ili držanje pozicije iz ega. Paper trading **uklanja
upravo tu varijablu.** Portfolio bez emotivnog pritiska je test analize, ne test
investitora.

**3. Look-ahead i hindsight bias.** Ako ulaziš u poziciju danas na osnovu podataka iz
zadnjeg kvartala, znaš već kako se cena kretala. Prirodna tendencija je da birate
kompanije koje su "očigledno" bile dobre. Zato je zaključavanje datuma i cene ulaza
(§7 CLAUDE.md) neophodno, ali nije potpuna zaštita.

**4. Selekcija režima.** Jedan tržišni režim (npr. AI-driven megacap koncentracija
2023–2026) nije reprezentativan. Value/quality okviri prolaze kroz duge periode
podbacivanja koji nemaju veze sa njihovom valjanošću. Graham-ov pristup je podbacivao
kroz ceo late-90s dot-com period — pa je bio ispravan.

---

## Šta ovaj eksperiment ZAISTA može da dokaže

I to je vredno, samo drugačije od onoga što si tražio:

### ✅ 1. Izvodljivost procesa
Možeš li realno da prikupiš sve podatke za 5 godina, izračunaš metrike, i održiš
kvartalni ritam — dok radiš full-time? Ovo je pravo pitanje, i odgovor dobijaš u
3 meseca. Ako se sistem raspadne zbog vremena, imaš odgovor.

### ✅ 2. Tačnost predviđanja fundamenata ← NAJVREDNIJE
Ovo je ključna zamena za merenje prinosa. Fundamenti (ROIC, marže, FCF, zaduženost) su
**dramatično manje šumoviti od cena.** Cena akcije ima godišnju volatilnost 25–40%;
operativna marža kvalitetne kompanije se kreće u opsegu od nekoliko procentnih poena.

Pa ako pri ulazu zapišeš 5 merljivih predviđanja po poziciji i pratiš ih 4 kvartala:
- 10 pozicija × 5 predviđanja = **50 opažanja u 12 meseci**
- Očekivanje pod nultom hipotezom (ne znaš ništa) ≈ 50% tačnosti
- Ako dobiješ 70%+, to je signal sa stvarnim sadržajem

**Ovo je test koji 12-mesečni period može da položi ili obori.** Test kroz prinose ne može.

### ✅ 3. Kalibracija sopstvenog samopouzdanja
Za svaku tezu zapiši i nivo uverenosti (50/70/90%). Posle 12 meseci uporedi: da li se
90%-uverene teze ostvaruju u ~90% slučajeva? Većina ljudi je sistematski
prekomerno samouverena, i to je merljivo na malom uzorku.

### ✅ 4. Da li tvoja teza objašnjava kretanje cene
Odvojeno pitanje od "da li je cena porasla". Ako je pozicija porasla 30% zbog M&A
spekulacije, a tvoja teza je bila o ROIC-u — bio si u pravu iz pogrešnog razloga.
To se broji kao neuspeh procesa, iako je rezultat pozitivan. Vođenje ove evidencije te
štiti od učenja pogrešnih lekcija.

### ✅ 5. Da li si u svom krugu kompetencije
Uporedi tačnost predviđanja za softver/IT pozicije vs. sve ostalo. Ako je razlika
jasna, to je akcionabilan nalaz — suzi domen.

---

## Preporuka: preformuliši cilj eksperimenta

**Umesto:** "Dokazaćemo da okvir daje bolji prinos od indeksa."
**U:** "Utvrdićemo da li mogu dosledno da izvršavam okvir i da li se moja predviđanja o
poslovanju kompanija ostvaruju — pre nego što izložim značajan kapital."

Prvi cilj je nedostižan u razumnom roku. Drugi je dostižan za 12 meseci i praktično
koristan.

Prinos protiv VUAA se **i dalje meri i evidentira** — samo se ne tretira kao dokaz.
On je kontekst, ne rezultat.

---

## I jedna neprijatna, ali bitna napomena

Većina aktivnih menadžera sa punim timovima, Bloomberg terminalima i pristupom
menadžmentu kompanija podbacuje protiv S&P 500 na horizontima od 10+ godina. Ti
ulaziš u istu igru sa nekoliko sati nedeljno, posle radnog dana.

To **ne znači da ne treba da probaš.** Ali znači da je verovatnija realna vrednost ovog
projekta u drugim stvarima: razumevanje kako biznisi zaista funkcionišu (što ti pomaže
i u ProfitOptics kontekstu), bolja procena rizika, disciplina, intelektualno
zadovoljstvo. To su legitimne isplate.

Ono što bi bilo skupo je da ovaj projekat postane izgovor za odstupanje od Mission 1M
DCA discipline — jer disciplinovani DCA u diversifikovane ETF-ove kroz 10 godina ima
mnogo veću verovatnoću da te dovede do $1M nego stock-picking sa nekoliko sati
nedeljno. To nije pesimizam, to je baznа stopa.
