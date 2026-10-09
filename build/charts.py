"""All figures for the Rosy Blue Securities Black Book.

Spec: matplotlib, PNG @200 dpi, serif, white ground, no top/right spines,
light grey horizontal gridlines, no in-image titles, palette limited to
#1F3A73 / #4F81BD / #A9BCDC.
"""
import os
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrow

NAVY, MID, LIGHT = "#1F3A73", "#4F81BD", "#A9BCDC"
GREY = "#BFBFBF"
OUT = os.path.join(os.path.dirname(__file__), "figs")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["STIXGeneral", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 9,
    "axes.edgecolor": "#444444",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})

SIZE = (5.7, 2.72)


def _ax(figsize=SIZE, grid=True):
    fig, ax = plt.subplots(figsize=figsize, dpi=200)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if grid:
        ax.yaxis.grid(True, color="#D9D9D9", linewidth=0.7)
        ax.set_axisbelow(True)
    return fig, ax


def _save(fig, name):
    fig.tight_layout(pad=0.6)
    path = os.path.join(OUT, name + ".png")
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


def _canvas(figsize=(5.7, 3.1)):
    fig, ax = plt.subplots(figsize=figsize, dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, text, fc=LIGHT, fs=7.6, tc="black", ec=NAVY):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.6,rounding_size=1.5",
                                linewidth=0.8, edgecolor=ec, facecolor=fc))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, color=tc, wrap=True)


def arrow(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=1.1,
                                shrinkA=1, shrinkB=1))


# ======================================================== CHAPTER 2
def fig_2_1():
    fig, ax = _canvas((5.7, 3.2))
    box(ax, 33, 84, 34, 13, "Board of Directors", NAVY, 8, "white")
    arrow(ax, 50, 84, 50, 76)
    box(ax, 33, 63, 34, 13, "Managing Director /\nWhole-time Director", MID, 7.6, "white")
    arrow(ax, 50, 63, 50, 56)
    ys = 40
    cols = [("Dealing Desk\n(equity cash, F&O)", 1), ("Risk Management\n(RMS)", 21),
            ("Back Office &\nSettlement", 41), ("Compliance &\nKYC", 61),
            ("Information\nTechnology", 81)]
    for label, x in cols:
        box(ax, x, ys, 18, 16, label, LIGHT, 7.0)
        arrow(ax, 50, 56, x + 9, ys + 16)
    box(ax, 1, 14, 18, 15, "Equity Dealer\n(the intern's role)", NAVY, 7.0, "white")
    arrow(ax, 10, 40, 10, 29)
    ax.text(50, 6, "Reporting lines shown are indicative of a typical broking firm;\n"
                   "the exact chart is to be confirmed by the firm.",
            ha="center", fontsize=6.6, style="italic", color="#555555")
    return _save(fig, "fig_2_1")


# ======================================================== CHAPTER 3
def fig_3_1():
    fig, ax = _canvas((5.7, 3.0))
    box(ax, 30, 84, 40, 13, "Indian Financial System", NAVY, 8.4, "white")
    for lbl, x in [("Financial\nMarkets", 4), ("Financial\nInstitutions", 28),
                   ("Financial\nInstruments", 52), ("Financial\nServices", 76)]:
        box(ax, x, 60, 20, 15, lbl, MID, 7.4, "white")
        arrow(ax, 50, 84, x + 10, 75)
    for lbl, x in [("Money Market\n(up to 1 year)", 2), ("Capital Market\n(over 1 year)", 26)]:
        box(ax, x, 36, 22, 14, lbl, LIGHT, 7.0)
    arrow(ax, 14, 60, 13, 50)
    arrow(ax, 14, 60, 37, 50)
    for lbl, x in [("Primary Market\n(new issues)", 2), ("Secondary Market\n(trading)", 26)]:
        box(ax, x, 12, 22, 14, lbl, LIGHT, 7.0)
    arrow(ax, 37, 36, 13, 26)
    arrow(ax, 37, 36, 37, 26)
    ax.text(76, 26, "The dealing desk of a\nstock broker operates in\nthe secondary segment\nof the capital market.",
            ha="center", va="center", fontsize=7.2, color=NAVY)
    return _save(fig, "fig_3_1")


def fig_3_2():
    fig, ax = _canvas((5.7, 3.0))
    box(ax, 36, 42, 28, 16, "Stock Exchange\n(NSE / BSE)", NAVY, 8.2, "white")
    ring = [("Investors\n(retail, HNI)", 4, 78), ("Stock Brokers\nand Dealers", 38, 82),
            ("FPIs and Mutual\nFunds", 72, 78), ("Clearing\nCorporation", 76, 42),
            ("Depositories\n(NSDL, CDSL)", 72, 6), ("Clearing Banks\nand DPs", 38, 2),
            ("Proprietary\nTraders", 4, 6), ("SEBI\n(regulator)", 1, 42)]
    for lbl, x, y in ring:
        box(ax, x, y, 22, 14, lbl, LIGHT, 7.0)
        arrow(ax, x + 11, y + 7, 50, 50)
    return _save(fig, "fig_3_2")


def fig_3_3():
    fig, ax = _canvas((5.7, 2.9))
    ax.text(25, 95, "BUY side (bids)", ha="center", fontsize=8.5, color=NAVY, weight="bold")
    ax.text(75, 95, "SELL side (asks)", ha="center", fontsize=8.5, color=NAVY, weight="bold")
    bids = [("1,250.50", "400", "09:31:02"), ("1,250.50", "150", "09:31:40"),
            ("1,250.25", "900", "09:30:11"), ("1,250.00", "1,200", "09:29:58")]
    asks = [("1,250.75", "300", "09:31:05"), ("1,251.00", "750", "09:30:22"),
            ("1,251.25", "500", "09:30:48"), ("1,251.50", "2,000", "09:28:19")]
    for i, (p, q, t) in enumerate(bids):
        y = 76 - i * 17
        box(ax, 2, y, 46, 13, f"Rs. {p}      {q} qty      {t}",
            LIGHT if i else MID, 7.2, "white" if i == 0 else "black")
    for i, (p, q, t) in enumerate(asks):
        y = 76 - i * 17
        box(ax, 52, y, 46, 13, f"Rs. {p}      {q} qty      {t}",
            LIGHT if i else MID, 7.2, "white" if i == 0 else "black")
    ax.text(50, 4, "Best bid and best ask shown in the darker shade. Among orders at the same price,\n"
                   "the earlier time stamp has priority \u2014 price first, then time.",
            ha="center", fontsize=6.9, style="italic", color="#555555")
    return _save(fig, "fig_3_3")


def fig_3_4():
    fig, ax = _canvas((5.7, 2.8))
    steps = [("Trade\nexecuted\n(T day)", 1), ("Exchange sends\ntrade file to\nclearing corp.", 21),
             ("Obligations\ncomputed\n(T day)", 41), ("Pay-in of funds\nand securities\n(T+1)", 61),
             ("Pay-out to\nclients\n(T+1)", 81)]
    for lbl, x in steps:
        box(ax, x, 50, 18, 24, lbl, LIGHT, 7.0)
    for i in range(4):
        arrow(ax, steps[i][1] + 18, 62, steps[i + 1][1], 62)
    box(ax, 21, 12, 24, 20, "Depository\n(NSDL / CDSL)\ndebits and credits\ndemat accounts", MID, 7.0, "white")
    box(ax, 55, 12, 24, 20, "Clearing bank\ndebits and credits\nsettlement\naccounts", MID, 7.0, "white")
    arrow(ax, 70, 50, 67, 32)
    arrow(ax, 70, 50, 33, 32)
    ax.text(90, 22, "Shortage \u2192\nauction /\nclose-out", ha="center", va="center",
            fontsize=7.0, color=NAVY)
    return _save(fig, "fig_3_4")


def fig_3_5():
    fig, ax = _ax()
    s = np.linspace(80, 120, 300)
    k = 100
    ax.plot(s, s - k, color=NAVY, lw=1.8, label="Long futures")
    ax.plot(s, k - s, color=LIGHT, lw=1.8, label="Short futures")
    ax.axhline(0, color=GREY, lw=0.9)
    ax.axvline(k, color=GREY, lw=0.7, ls=":")
    ax.set_xlabel("Price of the underlying at expiry (Rs.)")
    ax.set_ylabel("Profit / loss per unit (Rs.)")
    ax.legend(frameon=False, loc="upper left", fontsize=8)
    return _save(fig, "fig_3_5")


def fig_3_6():
    fig, ax = _ax()
    s = np.linspace(80, 120, 400)
    k, prem = 100, 4
    call = np.maximum(s - k, 0) - prem
    put = np.maximum(k - s, 0) - prem
    ax.plot(s, call, color=NAVY, lw=1.8, label="Long call (strike 100, premium 4)")
    ax.plot(s, put, color=MID, lw=1.8, ls="--", label="Long put (strike 100, premium 4)")
    ax.axhline(0, color=GREY, lw=0.9)
    ax.fill_between(s, call, 0, where=call > 0, color=LIGHT, alpha=0.45)
    ax.set_xlabel("Price of the underlying at expiry (Rs.)")
    ax.set_ylabel("Profit / loss per unit (Rs.)")
    ax.legend(frameon=False, loc="upper center", fontsize=7.6)
    return _save(fig, "fig_3_6")


def fig_3_7():
    fig, ax = _canvas((5.7, 2.9))
    box(ax, 1, 58, 21, 20, "Dealer / client\nterminal\n(CTCL user ID)", LIGHT, 7.2)
    box(ax, 27, 58, 21, 20, "Member's CTCL\nserver\n(order router)", MID, 7.2, "white")
    box(ax, 27, 20, 21, 20, "Pre-trade risk\nlayer: limits,\nUCC, margin", LIGHT, 7.2)
    box(ax, 53, 58, 21, 20, "Exchange\ntrading system\n(matching engine)", NAVY, 7.2, "white")
    box(ax, 78, 58, 21, 20, "Clearing\ncorporation", MID, 7.2, "white")
    box(ax, 53, 20, 21, 20, "Audit trail:\norder log, user\nand terminal ID", LIGHT, 7.2)
    arrow(ax, 22, 68, 27, 68)
    arrow(ax, 48, 68, 53, 68)
    arrow(ax, 74, 68, 78, 68)
    arrow(ax, 37, 58, 37, 40)
    arrow(ax, 37, 40, 37, 58)
    arrow(ax, 63, 58, 63, 40)
    ax.text(50, 8, "Every order leaving the member's server carries the approved user ID and terminal ID,\n"
                   "and must pass the pre-trade risk layer before it reaches the exchange.",
            ha="center", fontsize=6.9, style="italic", color="#555555")
    return _save(fig, "fig_3_7")


def fig_3_8():
    fig, ax = _ax((5.7, 2.75))
    labels = ["STT", "Brokerage", "Stamp duty", "GST", "Exchange\ncharges", "SEBI fee"]
    vals = [200.00, 100.00, 15.00, 19.07, 5.94, 0.20]
    colors = [NAVY, MID, LIGHT, LIGHT, LIGHT, LIGHT]
    y = np.arange(len(labels))[::-1]
    ax.barh(y, vals, color=colors, height=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8)
    ax.xaxis.grid(True, color="#D9D9D9", lw=0.7)
    ax.yaxis.grid(False)
    ax.set_axisbelow(True)
    ax.set_xlabel("Amount on an illustrative Rs. 1,00,000 buy and Rs. 1,00,000 sell delivery trade (Rs.)")
    for yi, v in zip(y, vals):
        ax.text(v + 4, yi, f"{v:,.2f}", va="center", fontsize=7.4)
    ax.set_xlim(0, 240)
    return _save(fig, "fig_3_8")


# ======================================================== CHAPTER 5
def fig_5_1():
    fig, ax = _canvas((5.7, 3.0))
    steps = [("08:45\nPre-market\npreparation", 1), ("09:00\nLimits and\nmargin upload", 17),
             ("09:07\nPre-open\nsession", 33), ("09:15\nContinuous\ntrading", 49),
             ("15:30\nPost-close\nchecks", 65), ("17:00\nReconciliation\nand reports", 81)]
    for lbl, x in steps:
        box(ax, x, 56, 18, 24, lbl, LIGHT, 7.0)
    for i in range(5):
        arrow(ax, steps[i][1] + 18, 68, steps[i + 1][1], 68)
    notes = [("News, corporate\nactions, ban list", 1), ("Client-wise\ncollateral", 17),
             ("Equilibrium\nprice discovery", 33), ("Order entry,\nmodification, RMS", 49),
             ("Trade file,\nobligations", 65), ("Contract notes,\nledger match", 81)]
    for lbl, x in notes:
        box(ax, x, 20, 18, 22, lbl, "#FFFFFF", 6.7)
        arrow(ax, x + 9, 56, x + 9, 42)
    return _save(fig, "fig_5_1")


def fig_5_2():
    fig, ax = _canvas((5.7, 3.2))
    chain = [("Client\ninstruction\nreceived", 70), ("Order entered on\nthe terminal", 70),
             ("Pre-trade risk\nand limit check", 70)]
    xs = [2, 36, 70]
    for (lbl, y), x in zip(chain, xs):
        box(ax, x, y, 28, 20, lbl, LIGHT, 7.2)
    arrow(ax, 30, 80, 36, 80)
    arrow(ax, 64, 80, 70, 80)
    box(ax, 70, 40, 28, 20, "Order accepted by\nexchange; unique\norder number", MID, 7.2, "white")
    arrow(ax, 84, 70, 84, 60)
    box(ax, 36, 40, 28, 20, "Resting in the\norder book", LIGHT, 7.2)
    arrow(ax, 70, 50, 64, 50)
    box(ax, 2, 40, 28, 20, "Modified, cancelled\nor allowed to lapse", LIGHT, 7.2)
    arrow(ax, 36, 50, 30, 50)
    box(ax, 36, 8, 28, 20, "Matched \u2014 trade\nconfirmation in the\ntrade book", NAVY, 7.2, "white")
    arrow(ax, 50, 40, 50, 28)
    box(ax, 70, 8, 28, 20, "Obligation, pay-in,\npay-out, contract\nnote", MID, 7.2, "white")
    arrow(ax, 64, 18, 70, 18)
    box(ax, 2, 8, 28, 20, "Unexecuted order\nlapses at close of\nthe trading day", "#FFFFFF", 7.2)
    arrow(ax, 16, 40, 16, 28)
    return _save(fig, "fig_5_2")


def fig_5_3():
    fig, ax = _canvas((5.7, 2.9))
    box(ax, 1, 60, 20, 22, "Dealing-desk\nworkstation\n(CTCL terminal)", LIGHT, 7.2)
    box(ax, 27, 60, 20, 22, "Member CTCL\nserver at the\nbroker's premises", MID, 7.2, "white")
    box(ax, 53, 60, 20, 22, "Leased line /\nexchange\nconnectivity", LIGHT, 7.2)
    box(ax, 79, 60, 20, 22, "Exchange\nmatching\nengine", NAVY, 7.2, "white")
    for x in (21, 47, 73):
        arrow(ax, x, 71, x + 6, 71)
    checks = ["Client code (UCC)\nvalidation", "Available margin\nand limit check",
              "Quantity, value and\nprice-band check", "Scrip-level and\nban-period check"]
    for i, c in enumerate(checks):
        box(ax, 1 + i * 25, 18, 22, 22, c, "#FFFFFF", 6.8)
        arrow(ax, 37, 60, 12 + i * 25, 40)
    ax.text(50, 6, "All four checks are applied inside the member's server before the order is released.",
            ha="center", fontsize=6.9, style="italic", color="#555555")
    return _save(fig, "fig_5_3")


def fig_5_4():
    fig, ax = _ax()
    cats = ["Equity cash\nmarket", "Equity\nderivatives\n(premium\nturnover)"]
    x = np.arange(2)
    ax.bar(x, [1, 1], color="white")
    ax.clear()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.grid(True, color="#D9D9D9", lw=0.7)
    ax.set_axisbelow(True)
    labels = ["FY24", "FY25", "FY26"]
    xx = np.arange(3)
    w = 0.36
    ax.bar(xx - w / 2, [np.nan] * 3, w, color=NAVY, label="Cash market")
    ax.bar(xx + w / 2, [np.nan] * 3, w, color=LIGHT, label="Equity derivatives")
    ax.set_xticks(xx)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Turnover (Rs. lakh crore)")
    ax.set_ylim(0, 1)
    ax.text(1, 0.5, "Figures to be verified from the NSE and BSE\nmarket-statistics pages before submission.",
            ha="center", va="center", fontsize=8.4, color=NAVY, style="italic")
    ax.legend(frameon=False, loc="upper left", fontsize=8)
    return _save(fig, "fig_5_4")


def fig_5_5():
    fig, ax = _ax()
    labels = ["CDSL\n(31 Mar 2025)", "CDSL\n(31 Mar 2026)", "CDSL\n(31 Aug 2026)", "NSDL\n(31 Aug 2026)"]
    vals = [15.30, 18.01, 19.10, 4.67]
    colors = [LIGHT, MID, NAVY, LIGHT]
    ax.bar(labels, vals, color=colors, width=0.56)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.3, f"{v:.2f}", ha="center", fontsize=8)
    ax.set_ylabel("Demat accounts (crore)")
    ax.set_ylim(0, 22)
    ax.tick_params(axis="x", labelsize=7.6)
    return _save(fig, "fig_5_5")


def fig_5_6():
    fig, ax = _ax()
    d = np.arange(30, -1, -1)
    spot = 1250.0
    r = 0.07
    fut = spot * np.exp(r * d / 365.0)
    days = 30 - d
    ax.plot(days, fut, color=NAVY, lw=1.8, label="Futures price (cost-of-carry)")
    ax.plot(days, np.full_like(fut, spot), color=LIGHT, lw=1.8, ls="--", label="Spot price (held constant)")
    ax.set_xlabel("Days elapsed in the contract (expiry at day 30)")
    ax.set_ylabel("Price (Rs.)")
    ax.legend(frameon=False, loc="upper right", fontsize=8)
    return _save(fig, "fig_5_6")


def fig_5_7(mtm):
    fig, ax = _ax()
    days = [f"Day {i+1}" for i in range(len(mtm))]
    colors = [NAVY if v >= 0 else LIGHT for v in mtm]
    ax.bar(days, mtm, color=colors, width=0.55)
    ax.axhline(0, color=GREY, lw=0.9)
    for i, v in enumerate(mtm):
        ax.text(i, v + (900 if v >= 0 else -1700), f"{v:,.0f}", ha="center", fontsize=7.6)
    ax.set_ylabel("Daily mark-to-market settlement (Rs.)")
    return _save(fig, "fig_5_7")


def fig_5_8(k, prem, lot):
    fig, ax = _ax()
    s = np.linspace(k - 400, k + 400, 500)
    pnl = (np.maximum(s - k, 0) - prem) * lot
    ax.plot(s, pnl, color=NAVY, lw=1.8)
    ax.axhline(0, color=GREY, lw=0.9)
    ax.fill_between(s, pnl, 0, where=pnl > 0, color=LIGHT, alpha=0.45)
    be = k + prem
    ax.plot([be], [0], "o", color=NAVY, ms=5)
    ax.annotate(f"Break-even {be:,.0f}", xy=(be, 0), xytext=(be + 40, -prem * lot * 0.55),
                fontsize=7.8, color=NAVY)
    ax.set_xlabel("Price of the underlying at expiry (Rs.)")
    ax.set_ylabel("Profit / loss on one lot (Rs.)")
    return _save(fig, "fig_5_8")


def fig_5_9(k, cp, pp, lot):
    fig, ax = _ax()
    s = np.linspace(k - 800, k + 800, 700)
    tot = cp + pp
    pnl = (np.maximum(s - k, 0) + np.maximum(k - s, 0) - tot) * lot
    ax.plot(s, pnl, color=NAVY, lw=1.8)
    ax.axhline(0, color=GREY, lw=0.9)
    ax.fill_between(s, pnl, 0, where=pnl > 0, color=LIGHT, alpha=0.45)
    for be in (k - tot, k + tot):
        ax.plot([be], [0], "o", color=NAVY, ms=5)
    ax.annotate(f"Lower\nbreak-even\n{k-tot:,.0f}", xy=(k - tot, 0), xytext=(k - 780, tot * lot * 0.35),
                fontsize=7.4, color=NAVY)
    ax.annotate(f"Upper\nbreak-even\n{k+tot:,.0f}", xy=(k + tot, 0), xytext=(k + 380, tot * lot * 0.35),
                fontsize=7.4, color=NAVY)
    ax.set_xlabel("Price of the underlying at expiry (Rs.)")
    ax.set_ylabel("Profit / loss on one lot (Rs.)")
    return _save(fig, "fig_5_9")


def fig_5_10(prices, days):
    fig, ax = _ax()
    ax.plot(days, prices, color=NAVY, lw=1.8, marker="o", ms=3.4)
    ax.set_xlabel("Calendar days remaining to expiry")
    ax.set_ylabel("Option premium (Rs. per unit)")
    ax.invert_xaxis()
    return _save(fig, "fig_5_10")


def fig_5_11(labels, vals):
    fig, ax = _ax((5.7, 2.8))
    y = np.arange(len(labels))[::-1]
    colors = [NAVY if i == 0 else (MID if i == 1 else LIGHT) for i in range(len(labels))]
    ax.barh(y, vals, color=colors, height=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8)
    ax.xaxis.grid(True, color="#D9D9D9", lw=0.7)
    ax.yaxis.grid(False)
    ax.set_axisbelow(True)
    for yi, v in zip(y, vals):
        ax.text(v + max(vals) * 0.015, yi, f"{v:,.2f}", va="center", fontsize=7.4)
    ax.set_xlim(0, max(vals) * 1.22)
    ax.set_xlabel("Amount (Rs.)")
    return _save(fig, "fig_5_11")


def fig_5_12(years, rev, pat):
    fig, ax = _ax((5.7, 2.9))
    x = np.arange(len(years))
    w = 0.42
    ax.bar(x - w / 2, rev, w, color=NAVY, label="Revenue from operations")
    ax.bar(x + w / 2, pat, w, color=LIGHT, label="Profit / (loss) after tax")
    ax.axhline(0, color=GREY, lw=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylabel("Rs. crore")
    for xi, v in zip(x - w / 2, rev):
        ax.text(xi, v + 60, f"{v:,.0f}", ha="center", fontsize=7.2)
    for xi, v in zip(x + w / 2, pat):
        ax.text(xi, v + (60 if v >= 0 else -170), f"{v:,.0f}", ha="center", fontsize=7.2)
    ax.legend(frameon=False, loc="upper left", fontsize=7.8)
    ax.set_ylim(min(pat) * 1.9, max(rev) * 1.25)
    return _save(fig, "fig_5_12")


def fig_5_13(years, contrib, aebitda):
    fig, ax = _ax((5.7, 2.85))
    x = np.arange(len(years))
    ax.plot(x, contrib, color=NAVY, lw=1.8, marker="o", ms=4, label="Contribution margin")
    ax.plot(x, aebitda, color=MID, lw=1.8, ls="--", marker="s", ms=4, label="Adjusted EBITDA margin")
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylabel("Per cent of revenue from operations")
    ax.set_ylim(0, 90)
    ax.legend(frameon=False, loc="center right", fontsize=7.8)
    for xi, v in zip(x, contrib):
        ax.text(xi, v + 3.5, f"{v:.0f}", ha="center", fontsize=7.2)
    for xi, v in zip(x, aebitda):
        ax.text(xi, v + 3.5, f"{v:.0f}", ha="center", fontsize=7.2)
    return _save(fig, "fig_5_13")


def fig_5_14(years, ditp, iap):
    fig, ax = _ax((5.7, 2.85))
    x = np.arange(len(years))
    tot = [d + i for d, i in zip(ditp, iap)]
    dp = [100 * d / t for d, t in zip(ditp, tot)]
    ip = [100 * i / t for i, t in zip(iap, tot)]
    ax.bar(x, dp, 0.5, color=NAVY, label="Digital Infrastructure and Transaction Platform")
    ax.bar(x, ip, 0.5, bottom=dp, color=LIGHT, label="Issuing and Acquiring Platform")
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylabel("Share of segment revenue (per cent)")
    ax.set_ylim(0, 128)
    for xi, (a, b) in enumerate(zip(dp, ip)):
        ax.text(xi, a / 2, f"{a:.1f}", ha="center", fontsize=7.4, color="white")
        ax.text(xi, a + b / 2, f"{b:.1f}", ha="center", fontsize=7.4)
    ax.legend(frameon=False, loc="upper center", fontsize=7.0, ncol=1)
    return _save(fig, "fig_5_14")


def fig_5_15(labels, vals):
    fig, ax = _ax((5.7, 2.7))
    y = np.arange(len(labels))[::-1]
    colors = [NAVY, MID, LIGHT, LIGHT]
    ax.barh(y, vals, color=colors[:len(vals)], height=0.58)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8)
    ax.xaxis.grid(True, color="#D9D9D9", lw=0.7)
    ax.yaxis.grid(False)
    ax.set_axisbelow(True)
    for yi, v in zip(y, vals):
        ax.text(v + 1.2, yi, f"{v:.2f}", va="center", fontsize=7.6)
    ax.set_xlim(0, 80)
    ax.set_xlabel("Holding (per cent of total equity capital)")
    return _save(fig, "fig_5_15")


def fig_5_16(names, growth, margin):
    fig, ax = _ax((5.7, 2.9))
    x = np.arange(len(names))
    w = 0.4
    ax.bar(x - w / 2, growth, w, color=NAVY, label="Revenue growth, latest full year (%)")
    ax.bar(x + w / 2, margin, w, color=LIGHT, label="Net profit margin, latest full year (%)")
    ax.axhline(0, color=GREY, lw=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=7.4)
    ax.set_ylabel("Per cent")
    ax.legend(frameon=False, loc="upper right", fontsize=7.2)
    return _save(fig, "fig_5_16")


if __name__ == "__main__":
    for f in (fig_2_1, fig_3_1, fig_3_2, fig_3_3, fig_3_4, fig_3_5, fig_3_6,
              fig_3_7, fig_3_8, fig_5_1, fig_5_2, fig_5_3, fig_5_4, fig_5_5, fig_5_6):
        print(f())
