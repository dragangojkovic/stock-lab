#!/usr/bin/env python3
"""
scorecard.py — Mission Stock Lab

Računa 5 kriterijuma + kontrolne metrike iz JSON fajla sa finansijskim podacima.
Samo standardna biblioteka — radi svuda.

Upotreba:
    python3 scripts/scorecard.py data/MSFT.json
    python3 scripts/scorecard.py data/MSFT.json --md > analize/MSFT-scorecard.md

Filozofija: skript ne daje "buy/sell". Daje kapije (pass/fail) i signale.
Nedostajući podaci se prikazuju kao N/A i NIKAD se ne procenjuju.
"""

import json
import sys
import statistics
from datetime import date

# ---------------------------------------------------------------- helpers

def g(d, key, default=None):
    """Safe get; prazan string i None se tretiraju kao odsutni."""
    v = d.get(key, default)
    if v == "" or v is None:
        return None
    return v


def div(a, b):
    """Deljenje koje vraća None umesto greške."""
    if a is None or b is None:
        return None
    try:
        if b == 0:
            return None
        return a / b
    except (TypeError, ZeroDivisionError):
        return None


def cagr(first, last, years):
    """CAGR; vraća None ako nije definisan (npr. negativna baza)."""
    if first is None or last is None or years <= 0:
        return None
    if first <= 0:
        return None
    if last <= 0:
        return None
    return (last / first) ** (1.0 / years) - 1.0


def pct(x, nd=1):
    return "N/A" if x is None else f"{x * 100:.{nd}f}%"


def num(x, nd=2, suffix=""):
    return "N/A" if x is None else f"{x:.{nd}f}{suffix}"


def med(vals):
    clean = [v for v in vals if v is not None]
    return statistics.median(clean) if clean else None


def avg(vals):
    clean = [v for v in vals if v is not None]
    return sum(clean) / len(clean) if clean else None


def trend(vals):
    """Grubi trend: uporedi prosek prve i druge polovine niza."""
    clean = [v for v in vals if v is not None]
    if len(clean) < 4:
        return "nedovoljno podataka"
    h = len(clean) // 2
    first, second = avg(clean[:h]), avg(clean[-h:])
    if first is None or second is None or first == 0:
        return "nedovoljno podataka"
    delta = (second - first) / abs(first)
    if delta > 0.10:
        return "RASTE"
    if delta < -0.10:
        return "PADA"
    return "stabilan"


# ---------------------------------------------------------------- core calc

def compute(data):
    """Vraća dict sa svim izvedenim metrikama i verdiktima kapija."""
    years = data.get("years", [])          # lista po godinama, najstarija prva
    mkt = data.get("market", {})
    meta = data.get("meta", {})
    n = len(years)
    out = {"meta": meta, "n_years": n, "warnings": []}

    if n == 0:
        out["warnings"].append("Nema godišnjih podataka.")
        return out
    if n < 5:
        out["warnings"].append(
            f"Samo {n} godina podataka — kapije koje traže 5 godina nisu validne."
        )

    per_year = []
    for i, y in enumerate(years):
        revenue = g(y, "revenue")
        cogs = g(y, "cogs")
        ebit = g(y, "ebit")
        net_income = g(y, "net_income")
        tax_rate = g(y, "effective_tax_rate")
        interest = g(y, "interest_expense")
        da = g(y, "depreciation_amortization")
        sbc = g(y, "stock_based_comp")
        ocf = g(y, "operating_cash_flow")
        capex = g(y, "capex")
        debt = g(y, "total_debt")
        cash = g(y, "cash_and_equivalents")
        equity = g(y, "total_equity")
        shares = g(y, "diluted_shares")
        recv = g(y, "receivables")
        inv = g(y, "inventory")
        eps = g(y, "diluted_eps")

        # NOPAT & invested capital
        nopat = ebit * (1 - tax_rate) if (ebit is not None and tax_rate is not None) else None
        invested = None
        if debt is not None and equity is not None:
            invested = debt + equity - (cash or 0)

        ebitda = (ebit + da) if (ebit is not None and da is not None) else None
        fcf = (ocf - capex) if (ocf is not None and capex is not None) else None
        fcf_after_sbc = (fcf - sbc) if (fcf is not None and sbc is not None) else None

        per_year.append({
            "fy": y.get("fy", f"Y{i+1}"),
            "revenue": revenue,
            "gross_margin": div((revenue - cogs) if (revenue is not None and cogs is not None) else None, revenue),
            "operating_margin": div(ebit, revenue),
            "net_margin": div(net_income, revenue),
            "roic": div(nopat, invested),
            "nopat": nopat,
            "invested_capital": invested,
            "ebit": ebit,
            "ebitda": ebitda,
            "net_debt": (debt - (cash or 0)) if debt is not None else None,
            "nd_ebitda": div((debt - (cash or 0)) if debt is not None else None, ebitda),
            "interest_cover": div(ebit, interest),
            "de": div(debt, equity),
            "ocf": ocf,
            "capex": capex,
            "fcf": fcf,
            "fcf_after_sbc": fcf_after_sbc,
            "fcf_conversion": div(fcf, net_income),
            "ocf_ni": div(ocf, net_income),
            "sbc_rev": div(sbc, revenue),
            "net_income": net_income,
            "shares": shares,
            "eps": eps,
            "receivables": recv,
            "inventory": inv,
            "total_debt": debt,
        })

    out["per_year"] = per_year
    span = n - 1

    # --- agregati
    roics = [p["roic"] for p in per_year]
    out["roic_median"] = med(roics)
    out["roic_trend"] = trend(roics)
    out["wacc"] = g(mkt, "wacc")
    out["roic_spread"] = (
        out["roic_median"] - out["wacc"]
        if (out["roic_median"] is not None and out["wacc"] is not None) else None
    )

    # kapitalno-laka detekcija: investirani kapital <= 10% prihoda ili negativan
    ic_last = per_year[-1]["invested_capital"]
    rev_last = per_year[-1]["revenue"]
    out["invested_capital_last"] = ic_last
    out["ic_to_revenue"] = div(ic_last, rev_last)
    out["capital_light"] = (
        ic_last is not None and rev_last is not None
        and (ic_last <= 0 or ic_last < 0.10 * rev_last)
    )
    out["fcf_margin_last"] = div(per_year[-1]["fcf"], rev_last)
    out["fcf_after_sbc_margin_last"] = div(per_year[-1]["fcf_after_sbc"], rev_last)

    out["gross_margin_last"] = per_year[-1]["gross_margin"]
    out["op_margin_last"] = per_year[-1]["operating_margin"]
    out["net_margin_last"] = per_year[-1]["net_margin"]
    out["op_margin_median"] = med([p["operating_margin"] for p in per_year])
    out["op_margin_trend"] = trend([p["operating_margin"] for p in per_year])
    out["net_margin_trend"] = trend([p["net_margin"] for p in per_year])

    out["nd_ebitda_last"] = per_year[-1]["nd_ebitda"]
    out["interest_cover_last"] = per_year[-1]["interest_cover"]
    out["de_last"] = per_year[-1]["de"]

    fcfs = [p["fcf"] for p in per_year]
    out["fcf_positive_count"] = sum(1 for f in fcfs if f is not None and f > 0)
    out["fcf_known_count"] = sum(1 for f in fcfs if f is not None)
    out["fcf_conversion_avg"] = avg([p["fcf_conversion"] for p in per_year])
    out["ocf_ni_avg"] = avg([p["ocf_ni"] for p in per_year])
    out["sbc_rev_last"] = per_year[-1]["sbc_rev"]

    # --- CAGR-ovi (test produktivnosti duga + buyback zavisnost)
    out["cagr_revenue"] = cagr(per_year[0]["revenue"], per_year[-1]["revenue"], span)
    out["cagr_ebit"] = cagr(per_year[0]["ebit"], per_year[-1]["ebit"], span)
    out["cagr_fcf"] = cagr(per_year[0]["fcf"], per_year[-1]["fcf"], span)
    out["cagr_debt"] = cagr(per_year[0]["total_debt"], per_year[-1]["total_debt"], span)
    out["cagr_eps"] = cagr(per_year[0]["eps"], per_year[-1]["eps"], span)
    out["cagr_receivables"] = cagr(per_year[0]["receivables"], per_year[-1]["receivables"], span)
    out["cagr_inventory"] = cagr(per_year[0]["inventory"], per_year[-1]["inventory"], span)
    out["cagr_shares"] = cagr(per_year[0]["shares"], per_year[-1]["shares"], span)

    fcf_ps_first = div(per_year[0]["fcf"], per_year[0]["shares"])
    fcf_ps_last = div(per_year[-1]["fcf"], per_year[-1]["shares"])
    out["cagr_fcf_per_share"] = cagr(fcf_ps_first, fcf_ps_last, span)

    # dug produktivan? dug ne sme rasti brže od EBIT i FCF
    dp = None
    out["no_financial_debt"] = bool(g(meta, "no_financial_debt", False))
    if out["cagr_debt"] is not None and not out["no_financial_debt"]:
        refs = [x for x in (out["cagr_ebit"], out["cagr_fcf"]) if x is not None]
        if refs:
            dp = out["cagr_debt"] <= max(refs)
    out["debt_productive"] = dp

    # --- PEG
    pe = g(mkt, "pe_ratio")
    fwd_growth = g(mkt, "consensus_eps_growth_3y")   # decimalno, npr 0.14
    out["pe"] = pe
    out["peg_trailing"] = div(pe, out["cagr_eps"] * 100 if out["cagr_eps"] else None)
    out["peg_forward"] = div(pe, fwd_growth * 100 if fwd_growth else None)
    out["fwd_growth"] = fwd_growth

    ev = g(mkt, "enterprise_value")
    out["ev"] = ev
    out["fcf_yield_ev"] = div(per_year[-1]["fcf"], ev)
    out["fcf_yield_ev_after_sbc"] = div(per_year[-1]["fcf_after_sbc"], ev)

    # ---------------------------------------------------------- HARD KAPIJE
    gates = []

    # G1 ROIC
    roic_ok = None
    if out["roic_median"] is not None:
        lvl = out["roic_median"] >= 0.12
        spr = out["roic_spread"] >= 0.03 if out["roic_spread"] is not None else None
        roic_ok = lvl if spr is None else (lvl and spr)
    if out["capital_light"]:
        gates.append({
            "id": "G1", "name": "ROIC ≥ 12% i spread nad WACC ≥ 3pp",
            "value": f"NIJE PRIMENLJIVO (inv. kapital {num(out['invested_capital_last'], 0)} = "
                     f"{pct(out['ic_to_revenue'])} prihoda)",
            "pass": "NP",
            "note": "Investirani kapital je nula/negativan — ROIC divergira i prag od 12% "
                    "ne nosi informaciju. Zameni ga FCF maržom (vidi K1-ALT). Poslovanje "
                    "se finansira iz avansa kupaca (deferred revenue), ne iz kapitala.",
        })
    else:
        gates.append({
            "id": "G1", "name": "ROIC ≥ 12% (5g medijana) i spread nad WACC ≥ 3pp",
            "value": f"medijana {pct(out['roic_median'])}, WACC {pct(out['wacc'])}, spread {pct(out['roic_spread'])}",
            "pass": roic_ok,
            "note": "" if out["wacc"] is not None else "WACC nije unet — spread nije proveren!",
        })

    # G2 zaduženost
    lev_ok = None
    thr = g(meta, "nd_ebitda_threshold", 3.0)
    if out["nd_ebitda_last"] is not None:
        a = out["nd_ebitda_last"] <= thr
        b = out["interest_cover_last"] >= 4.0 if out["interest_cover_last"] is not None else None
        lev_ok = a if b is None else (a and b)
    gates.append({
        "id": "G2", "name": f"Neto dug/EBITDA ≤ {thr}x i pokrivenost kamata ≥ 4x",
        "value": f"ND/EBITDA {num(out['nd_ebitda_last'], 2, 'x')}, kamate {num(out['interest_cover_last'], 1, 'x')}",
        "pass": lev_ok, "note": "",
    })

    # G3 FCF pozitivan
    fcf_ok = None
    if out["fcf_known_count"] >= 4:
        fcf_ok = out["fcf_positive_count"] >= 4
    gates.append({
        "id": "G3", "name": "FCF pozitivan u ≥ 4 od 5 godina",
        "value": f"{out['fcf_positive_count']} od {out['fcf_known_count']} poznatih",
        "pass": fcf_ok, "note": "",
    })

    # G4 FCF konverzija
    conv_ok = out["fcf_conversion_avg"] >= 0.7 if out["fcf_conversion_avg"] is not None else None
    gates.append({
        "id": "G4", "name": "FCF konverzija (FCF/NI, 5g prosek) ≥ 0.7",
        "value": num(out["fcf_conversion_avg"]),
        "pass": conv_ok, "note": "",
    })

    # G5 moat (manualno)
    moat = g(meta, "moat_two_sentences")
    gates.append({
        "id": "G5", "name": "Moat artikulisan u 2 rečenice",
        "value": "DA" if moat else "NIJE UPISAN",
        "pass": bool(moat) if moat is not None else None, "note": "",
    })

    # G6 sektor
    excluded = g(meta, "excluded_sector", False)
    gates.append({
        "id": "G6", "name": "Nije u isključenom sektoru",
        "value": "isključen" if excluded else "u redu",
        "pass": (not excluded), "note": "",
    })

    out["gates"] = gates
    out["gates_passed"] = sum(1 for x in gates if x["pass"] is True)
    out["gates_failed"] = sum(1 for x in gates if x["pass"] is False)
    out["gates_unknown"] = sum(1 for x in gates if x["pass"] is None)
    out["gates_na"] = sum(1 for x in gates if x["pass"] == "NP")
    return out


# ---------------------------------------------------------------- rendering

def flag(v):
    return {True: "PROŠAO", False: "PAO", None: "N/A", "NP": "N/P"}.get(v, "N/A")


def render(r, markdown=False):
    L = []
    m = r.get("meta", {})
    name = m.get("name", "?")
    tk = m.get("ticker", "?")
    h = "## " if markdown else ""

    L.append(f"{'# ' if markdown else ''}SCORECARD — {name} ({tk})")
    L.append(f"Sektor: {m.get('sector', 'N/A')} | Valuta: {m.get('currency', 'N/A')} "
             f"| Podaci: {r.get('n_years')} god. | Generisano: {date.today().isoformat()}")
    L.append("")

    if r.get("warnings"):
        L.append(f"{h}⚠ Upozorenja")
        for w in r["warnings"]:
            L.append(f"- {w}")
        L.append("")

    if not r.get("per_year"):
        return "\n".join(L)

    # kapije
    L.append(f"{h}HARD KAPIJE")
    L.append("")
    L.append("| # | Kapija | Vrednost | Ishod |")
    L.append("|---|---|---|---|")
    for gt in r["gates"]:
        L.append(f"| {gt['id']} | {gt['name']} | {gt['value']} | **{flag(gt['pass'])}** |")
    L.append("")
    L.append(f"Prošlo: {r['gates_passed']} | Palo: {r['gates_failed']} | "
             f"Nepoznato: {r['gates_unknown']} | Nije primenljivo: {r.get('gates_na', 0)}")
    for gt in r["gates"]:
        if gt.get("note"):
            L.append(f"- ⚠ {gt['id']}: {gt['note']}")
    if r["gates_failed"] > 0:
        L.append("")
        L.append("> **Kapija je pala.** Akcija ispada iz razmatranja, osim ako se napiše "
                 "eksplicitno obrazloženje override-a u analizi.")
    if r["gates_unknown"] > 0:
        L.append("")
        L.append("> **Nedostaju podaci.** Nepopunjena kapija nije prošla kapija. "
                 "Popuni podatke pre odluke.")
    L.append("")

    # K1
    L.append(f"{h}K1 — ROIC")
    L.append(f"- Medijana (5g): **{pct(r['roic_median'])}** | Trend: **{r['roic_trend']}**")
    L.append(f"- WACC: {pct(r['wacc'])} | Spread: **{pct(r['roic_spread'])}**")
    L.append("")
    L.append("| Godina | " + " | ".join(p["fy"] for p in r["per_year"]) + " |")
    L.append("|---|" + "---|" * len(r["per_year"]))
    L.append("| ROIC | " + " | ".join(pct(p["roic"]) for p in r["per_year"]) + " |")
    L.append("")

    if r.get("capital_light"):
        L.append(f"{h}K1-ALT — kapitalno-laka firma, ROIC nije upotrebljiv")
        L.append(f"- Investirani kapital (zadnja god.): **{num(r['invested_capital_last'], 0)}** "
                 f"({pct(r['ic_to_revenue'])} prihoda)")
        L.append(f"- **FCF marža: {pct(r['fcf_margin_last'])}** ← zamenska metrika kvaliteta")
        L.append(f"- **FCF marža nakon SBC: {pct(r['fcf_after_sbc_margin_last'])}** ← konzervativno")
        L.append("")
        L.append("> Kompanija ne troši kapital da bi rasla. To je ekonomski jak signal, ali "
                 "znači da ROIC prag ne razlikuje ništa. Teret dokazivanja prelazi na FCF maržu, "
                 "operativnu maržu i trajnost moat-a.")
        L.append("")

    # K2
    L.append(f"{h}K2 — Marže (razlaganje)")
    L.append("| Marža | " + " | ".join(p["fy"] for p in r["per_year"]) + " | Trend |")
    L.append("|---|" + "---|" * (len(r["per_year"]) + 1))
    L.append("| Bruto | " + " | ".join(pct(p["gross_margin"]) for p in r["per_year"]) + " | — |")
    L.append("| **Operativna** | " + " | ".join(pct(p["operating_margin"]) for p in r["per_year"])
             + f" | **{r['op_margin_trend']}** |")
    L.append("| Neto | " + " | ".join(pct(p["net_margin"]) for p in r["per_year"])
             + f" | {r['net_margin_trend']} |")
    L.append("")
    L.append("> Operativna marža je glavni pokazatelj efikasnosti poslovanja. "
             "Gap bruto→operativna = SG&A + R&D (investicija, ne nužno neefikasnost).")
    L.append("> **Obavezno: uporedi ove marže sa 3–5 konkurenata pre zaključka.**")
    L.append("")

    # K3
    L.append(f"{h}K3 — Zaduženost")
    L.append("| Metrika | " + " | ".join(p["fy"] for p in r["per_year"]) + " |")
    L.append("|---|" + "---|" * len(r["per_year"]))
    L.append("| Neto dug/EBITDA | " + " | ".join(num(p["nd_ebitda"], 2, "x") for p in r["per_year"]) + " |")
    L.append("| Pokrivenost kamata | " + " | ".join(num(p["interest_cover"], 1, "x") for p in r["per_year"]) + " |")
    L.append("| D/E | " + " | ".join(num(p["de"]) for p in r["per_year"]) + " |")
    L.append("")
    L.append("**Test produktivnosti duga** (dug ne sme rasti brže od EBIT/FCF):")
    L.append(f"- Dug CAGR: {pct(r['cagr_debt'])} | EBIT CAGR: {pct(r['cagr_ebit'])} "
             f"| FCF CAGR: {pct(r['cagr_fcf'])} | Prihod CAGR: {pct(r['cagr_revenue'])}")
    dp = r["debt_productive"]
    if r.get("no_financial_debt"):
        L.append("- Verdikt: **TEST PRESKOČEN** — kompanija nema finansijski dug. "
                 "Brojevi iznad su obaveze po operativnom lizingu, ne poluga.")
    else:
        L.append(f"- Verdikt: **{'dug je bio produktivan' if dp else ('dug NIJE bio produktivan' if dp is False else 'N/A')}**")
    L.append("")

    # K4
    L.append(f"{h}K4 — Free Cash Flow")
    L.append("| Metrika | " + " | ".join(p["fy"] for p in r["per_year"]) + " |")
    L.append("|---|" + "---|" * len(r["per_year"]))
    L.append("| OCF | " + " | ".join(num(p["ocf"], 0) for p in r["per_year"]) + " |")
    L.append("| CapEx | " + " | ".join(num(p["capex"], 0) for p in r["per_year"]) + " |")
    L.append("| **FCF** | " + " | ".join(num(p["fcf"], 0) for p in r["per_year"]) + " |")
    L.append("| FCF nakon SBC | " + " | ".join(num(p["fcf_after_sbc"], 0) for p in r["per_year"]) + " |")
    L.append("| FCF/NI | " + " | ".join(num(p["fcf_conversion"]) for p in r["per_year"]) + " |")
    L.append("| OCF/NI | " + " | ".join(num(p["ocf_ni"]) for p in r["per_year"]) + " |")
    L.append("")
    L.append(f"- FCF konverzija (prosek): **{num(r['fcf_conversion_avg'])}** (cilj ≥ 0.70)")
    L.append(f"- OCF/NI (prosek): {num(r['ocf_ni_avg'])} — ako je uporno < 1.0, zarada je 'na papiru'")
    L.append(f"- SBC/Prihod (zadnja god.): {pct(r['sbc_rev_last'])}"
             + ("  ⚠ **> 5% — dilacija je materijalna**"
                if (r["sbc_rev_last"] or 0) > 0.05 else ""))
    L.append(f"- Rast broja akcija (CAGR): {pct(r['cagr_shares'])}")
    L.append("")
    L.append("**Kvalitet obrtnog kapitala** (potraživanja/zalihe ne smeju rasti brže od prihoda):")
    L.append(f"- Potraživanja CAGR: {pct(r['cagr_receivables'])} vs Prihod CAGR: {pct(r['cagr_revenue'])}")
    L.append(f"- Zalihe CAGR: {pct(r['cagr_inventory'])} vs Prihod CAGR: {pct(r['cagr_revenue'])}")
    L.append("")

    # K5
    L.append(f"{h}K5 — Valuacija")
    L.append(f"- P/E: {num(r['pe'])}")
    L.append(f"- EPS CAGR (istorijski {r['n_years'] - 1}g): {pct(r['cagr_eps'])} → "
             f"**PEG_trailing = {num(r['peg_trailing'])}**")
    L.append(f"- Konsenzus EPS rast (3g): {pct(r['fwd_growth'])} → "
             f"**PEG_forward = {num(r['peg_forward'])}**")
    L.append(f"- FCF yield na EV: **{pct(r['fcf_yield_ev'])}** "
             f"(nakon SBC: {pct(r['fcf_yield_ev_after_sbc'])}) ← ne zavisi od projekcija")
    L.append("")
    L.append("**Kontrola: da li je rast EPS-a stvaran ili buyback?**")
    L.append(f"- Prihod CAGR: {pct(r['cagr_revenue'])} | EPS CAGR: {pct(r['cagr_eps'])} "
             f"| FCF/akcija CAGR: {pct(r['cagr_fcf_per_share'])}")
    if r["cagr_eps"] is not None and r["cagr_revenue"] is not None:
        gap = r["cagr_eps"] - r["cagr_revenue"]
        if gap > 0.05:
            L.append(f"- ⚠ EPS raste **{pct(gap)}** brže od prihoda — proveri koliko toga "
                     "dolazi od buyback-a/marži, a koliko od stvarnog rasta posla.")
    if r["peg_trailing"] and r["peg_forward"]:
        if r["peg_forward"] < r["peg_trailing"] * 0.7:
            L.append("- ⚠ PEG_forward je znatno niži od PEG_trailing → konsenzus očekuje "
                     "ubrzanje koje se još nije dogodilo. **Opravdaj tu pretpostavku eksplicitno.**")
    L.append("")

    L.append("---")
    L.append("*Ovaj scorecard nije preporuka. Kapije i signali su ulaz u analizu, "
             "ne zamena za nju. Popuni `templates/analiza.md` pre bilo kakve odluke.*")
    return "\n".join(L)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(1)
    with open(args[0], encoding="utf-8") as f:
        data = json.load(f)
    print(render(compute(data), markdown="--md" in sys.argv))


if __name__ == "__main__":
    main()