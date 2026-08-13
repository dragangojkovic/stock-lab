# Sektorska kalibracija i kandidati van softvera

Dodatak `CLAUDE.md`. Nastao nakon prve realne analize (MANH), koja je pokazala da
jedinstveni prag za sve sektore ne radi.

---

## 1. Zašto jedinstveni prag ne radi

MANH je prošao G1 sa medijanom ROIC-a od 659% — besmislica, jer je investirani kapital
3,9% prihoda. Obrnut problem postoji kod kompanija sa **negativnim kapitalom** (npr.
posle spinoffa finansiranog dugom, ili posle godina agresivnog buyback-a): tamo D/E i
ROIC eksplodiraju u drugom smeru.

Zaključak: **kriterijumi K1, K3 i K5 su sektorski osetljivi. K2 i K4 su univerzalni.**

---

## 2. Kalibracija pragova po sektoru

| Sektor | ROIC prag (K1) | Neto dug/EBITDA (K3) | Napomena za K5 |
|---|---|---|---|
| Softver / SaaS | 25%+ | < 2,0x | PEG često slomljen (SBC, GAAP EPS pada) |
| Poluprovodnici | 20%+ | < 2,0x | Dubok ciklus — normalizuj E kroz ciklus |
| Industrija / mašine | 15%+ | < 3,0x | PEG radi solidno |
| Industrijska distribucija | 15%+ | < 2,5x | Nizak ROIC ali stabilan; gledaj obrt zaliha |
| Medicinski aparati / dijagnostika | 20%+ | < 2,5x | Razor/blade — proveri udeo potrošnog materijala |
| Potrošačka roba sa brendom | 15%+ | < 3,0x | Uporedi sa organskim rastom, ne ukupnim |
| Maloprodaja | 15%+ | < 2,5x | Uključi obaveze po lizingu prodavnica u dug! |
| Platni sistemi (MA, V) | 30%+ | < 2,0x | Vidi §3 — NISU banke |
| Rejting / podaci | 25%+ | < 3,0x | Regulatorna barijera, stabilne marže |
| Komunalije / telekom / REIT | ne koristi | 3,0–5,0x normalno | K1 i K5 ne primenjuj |
| Banke / osiguranje | **ISKLJUČENO** | — | Vidi §3 |

**Kapije koje ostaju nepromenjene za sve sektore:**
- K2: marže se uvek porede sa 3–5 konkurenata i sopstvenom 5-god istorijom
- K4: FCF pozitivan u ≥4 od 5 god, FCF konverzija ≥ 0,7
- K5-ALT: FCF yield na EV se uvek računa (ne zavisi od projekcija)
- Moat u dve rečenice

---

## 3. Važno razjašnjenje: platni sistemi nisu banke

Isključenje finansijskog sektora iz `CLAUDE.md` §4 postoji jer kod banaka investirani
kapital uključuje depozite — kapital koji drže ali ne poseduju, pa ROIC daje
neuporedive brojeve.

**Mastercard i Visa ne rade tako.** One ne nose kreditni rizik i ne primaju depozite —
zarađuju od obima transakcija. To su asset-light mrežni poslovi sa operativnim maržama
iznad 50%. Ostaju u igri, sa prilagođenim (višim) pragom.

Isto važi i za berze (CME, ICE) i rejting agencije (MCO, SPGI) — infrastruktura, ne
bilansni rizik.

**Isključeno ostaje:** komercijalne banke, investicione banke, osiguravači,
reosiguravači, brokerski dileri, BDC-ovi, hipotekarni REIT-ovi.

---

## 4. Kandidati po sektoru

Status kod svih: **HIPOTEZA — nije verifikovano po standardu scorecard-a.**
Kolona "šta će slomiti sistem" je namerna: kandidati koji stresiraju metodologiju
uče te više od onih koji glatko prolaze.

### Industrija — switching costs na instaliranoj bazi

**OTIS (Otis Worldwide)** — liftovi i eskalatori
Servisni ugovori na instaliranoj bazi nose većinu profita; zamena lifta je regulatorno
i finansijski skupa, a delovi su vlasnički. Snažan moat.
*Šta će slomiti sistem:* kapital je verovatno negativan zbog spinoffa iz UTC-a
finansiranog dugom (2020). D/E će biti besmislen ili negativan — **obrnut problem od
MANH.** Koristi samo Neto dug/EBITDA. Rizik: Kina, novogradnja.
**Ovo je najbolji drugi test slučaj — lomi metodologiju u suprotnom smeru.**

**FAST (Fastenal)** — industrijski spojni materijal, on-site vending
Gustina distribucije + oprema kod klijenta. Niska zaduženost, visok ROIC za industriju.
*Slomiće:* zalihe su ovde ključne (K4 obrtni kapital), a ciklične su.

### Zdravstvo — razor/blade i regulatorna barijera

**IDXX (IDEXX Laboratories)** — veterinarska dijagnostika
Instalirana baza analizatora + potrošni materijal sa visokom maržom. Vlasnički testovi.
*Slomiće:* skupo je; K5 će verovatno pući. Proveri koji % prihoda je recurring
potrošni materijal vs prodaja aparata.

**MEDP (Medpace)** — klinička istraživanja (CRO)
Asset-light, neto gotovina, klijenti plaćaju avansno.
*Slomiće:* **istu zamku kao MANH** — negativan obrtni kapital iz avansa kupaca, pa će
K1 opet biti N/P. Dobra provera da li K1-ALT ispravka generalizuje.

### Potrošnja i distribucija — obim

**CPRT (Copart)** — aukcije havarisanih vozila
Dvostrani mrežni efekat (osiguravači ↔ kupci) + posedovanje zemljišta koje je
regulatorno teško dobiti. Neto gotovina, visok ROIC.
*Slomiće:* malo šta — ovo je najčistiji test slučaj gde kriterijumi rade kako su
zamišljeni. Dobar za kontrolu da sistem uopšte ume da kaže "prolazi".

**ORLY (O'Reilly Automotive)** — auto delovi
Gustina zaliha i dostava u roku od sata profesionalnim mehaničarima.
*Slomiće:* negativan kapital od godina buyback-a **plus** realan dug **plus** obaveze
po lizingu prodavnica. Tri problema odjednom u K1 i K3.

### Infrastruktura tržišta — asset-light mreže

**MA / V (Mastercard, Visa)** — platni sistemi
Mrežni efekat, operativne marže preko 50%, bez kreditnog rizika.
*Slomiće:* ROIC je toliko visok da prag ne razlikuje ništa. Prelazi na FCF maržu i
uporedi MA vs V direktno — savršen par za K2 poređenje konkurenata.

**MCO / SPGI (Moody's, S&P Global)** — rejting i podaci
Regulatorno zaštićen duopol.
*Slomiće:* ciklična izloženost izdavanju obveznica — E nije stabilan kroz ciklus.

---

## 5. Predlog redosleda za sledeće analize

| # | Ticker | Sektor | Zašto ovaj |
|---|---|---|---|
| 1 | MANH | Softver | ✅ urađeno — otkrilo K1 problem kod kapitalno-lakih |
| 2 | **OTIS** | Industrija | Lomi K1/K3 u suprotnom smeru (negativan kapital od duga) |
| 3 | **CPRT** | Potrošnja/aukcije | Kontrolni slučaj — sistem mora umeti da kaže "prolazi čisto" |
| 4 | PRGS | Softver | Kapija G2 pada (ND/EBITDA ~3,8x) + tvoj krug kompetencije |
| 5 | MEDP ili IDXX | Zdravstvo | Provera da li K1-ALT generalizuje |

Nakon ova četiri-pet, imaćeš metodologiju testiranu na svim glavnim načinima na koje
može da pukne. **To je vredniji rezultat od bilo kog prinosa u tom periodu.**

---

## 6. Sektorska korelacija — ograničenje na alokaciju

Sa $1.000 po poziciji i 10 pozicija, **maksimalno 3 pozicije iz istog sektora.**
Deset softverskih firmi nisu deset opklada nego jedna. Ovo pravilo postoji da bi
`predvidjanja.csv` imao stvarno nezavisna opažanja, a ne deset varijacija istog
makro režima.

Preporučena raspodela za 10 pozicija:
- Softver / tehnologija: max 3
- Industrija: 2
- Zdravstvo: 2
- Potrošnja / distribucija: 2
- Infrastruktura tržišta (MA/V/MCO): 1
