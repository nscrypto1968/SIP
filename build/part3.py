#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chapter 5 — Analysis and Interpretation."""
import compute as C
from compute import inr, pct
import charts as G
from part2 import (SRC_NSE, SRC_SEBI, SRC_AUTH, SRC_COMP, SRC_PL_FY26, SRC_PL_Q1,
                   SRC_PL_RHP, TBV, TODAY, AS_ON)


def chapter5(R):
    R.chapter("CHAPTER 5", "ANALYSIS AND INTERPRETATION")

    # ---------------------------------------------------------------- 5.1
    R.section("5.1 Introduction")
    R.body(
        "This chapter converts the description in Chapter 3 into computed evidence. It begins "
        "with the shape of the dealing day and a snapshot of the market, follows an order "
        "through the exchange terminal and the member's Computer-to-Computer Link facility, "
        "works through four quantitative demonstrations \u2014 futures pricing and settlement, "
        "option valuation and payoff, margin and shortfall, and transaction charges \u2014 and "
        "applies fundamental analysis to Pine Labs Limited. All trading examples are "
        "illustrative and constructed by the author; no figure is taken from the firm's "
        "records.")

    # ---------------------------------------------------------------- 5.2
    R.section("5.2 A day on the equity dealing desk")
    R.body("The flow of a dealer's working day is shown in Figure 5.1 and set out task by task "
           "in Table 5.1.")
    R.caption("Figure 5.1: Flow of a dealer's day from pre-open to post-close")
    R.image(G.fig_5_1())
    R.source(SRC_COMP)
    R.caption("Table 5.1: Timeline of a dealing-desk day, task by task")
    R.table(
        ["Phase", "Task performed", "Control applied", "Output"],
        [["Pre-market", "Review of news, corporate actions and the derivatives ban list",
          "Cross-check against the exchange circular of the morning", "List of restricted scrips"],
         ["Pre-market", "Verification of client-wise limits released by the risk system",
          "Limit must be read before, not after, an instruction is accepted",
          "Tradable limit per client"],
         ["Continuous", "Order entry against verified client instruction",
          "Client code, quantity, price and segment confirmed before release", "Order number"],
         ["Continuous", "Response to margin-shortfall alerts",
          "Escalation to risk management; no limit granted at the desk", "Top-up or square-off"],
         ["Pre-close", "Intraday square-off of positions that cannot be carried",
          "Executed before the cut-off time set by the firm", "Flat intraday book"],
         ["Post-close", "Verification of executions against the trade book",
          "Every fill matched to an instruction", "Confirmed trade list"],
         ["Post-close", "Reconciliation with the back office and contract-note check",
          "Discrepancy reported the same evening", "Reconciled client position"]],
        widths=[1300, 3000, 3000, 1700], size=9.5,
        align=["left", "left", "left", "left"])
    R.source("Source: Author's observation during the internship; no client or firm data is "
             "included.")
    R.interpretation(
        "Nine distinct tasks appear in the day, of which only two \u2014 order entry and "
        "modification \u2014 involve execution; the remaining seven are preparation, control or "
        "verification. The dealing function is therefore better understood as a controlled "
        "process with an execution step embedded in it than as an execution function with "
        "controls attached. This explains why the most common cause of an escalated problem "
        "observed during the internship was an omission in the pre-market block rather than an "
        "error during trading.")

    # ---------------------------------------------------------------- 5.3
    R.section("5.3 Indian equity market snapshot")
    R.body("The market in which the internship took place is described in Table 5.2 and the "
           "participation data in Table 5.3 and Figure 5.2.")
    R.caption("Table 5.2: Benchmark index levels, as on 30 September 2026")
    R.table(
        ["Index", "Closing level", "Change during September 2026 (%)", "Comment"],
        [["Nifty 50", inr(C.NIFTY_CLOSE), pct(C.NIFTY_SEP_CHG),
          "Second consecutive monthly decline"],
         ["S&P BSE Sensex", inr(C.SENSEX_CLOSE), pct(C.SENSEX_SEP_CHG),
          "Broadly parallel movement to the Nifty 50"]],
        widths=[2100, 2100, 2900, 1900], size=9.5,
        align=["left", "center", "center", "left"])
    R.source("Source: Exchange index data for the month ended 30 September 2026; checked "
             "9 October 2026.")
    R.caption("Table 5.3: Investor participation and demat accounts")
    R.table(
        ["Measure", "Figure", "As on", "Source basis"],
        [["Demat accounts \u2014 CDSL", f"{C.DEMAT_CDSL_AUG26:.2f} crore", "31 August 2026",
          "Depository published count"],
         ["Demat accounts \u2014 NSDL", f"{C.DEMAT_NSDL_AUG26:.2f} crore", "31 August 2026",
          "Depository published count"],
         ["Demat accounts \u2014 total", f"{C.DEMAT_TOTAL:.2f} crore", "31 August 2026",
          "Author's computation, sum of the above"],
         ["CDSL accounts", f"{C.CDSL_MAR26:.2f} crore", "31 March 2026", "Depository disclosure"],
         ["CDSL accounts added in FY26", f"{C.CDSL_FY26_ADD:.2f} crore", "FY2025-26",
          "Author's computation"],
         ["NSE unique registered investors", f"{C.NSE_UNIQUE_INVESTORS:.1f} crore", "July 2026",
          "Unique permanent account numbers"],
         ["Cash-market turnover", "[ADD: verify from NSE and BSE statistics]", "FY2025-26",
          TBV],
         ["Equity-derivatives turnover", "[ADD: verify from NSE and BSE statistics]", "FY2025-26",
          TBV]],
        widths=[2600, 2300, 1900, 2200], size=9.5,
        align=["left", "center", "center", "left"])
    R.source("Source: CDSL and NSDL published statistics and NSE investor data; checked "
             "9 October 2026. Turnover figures could not be verified against a primary exchange "
             "document in the time available and are marked " + TBV + ".")
    R.caption("Figure 5.2: Growth in demat accounts")
    R.image(G.fig_5_5())
    R.source("Source: CDSL and NSDL published statistics; checked 9 October 2026.")
    R.interpretation(
        "Demat accounts at the Central Depository Services (India) Limited rose from " +
        f"{C.CDSL_MAR25:.2f}" + " crore at the end of FY2024-25 to " + f"{C.CDSL_MAR26:.2f}" +
        " crore at the end of FY2025-26, an addition of " + f"{C.CDSL_FY26_ADD:.2f}" + " crore "
        "accounts or " + pct(C.CDSL_FY26_GROWTH) + " per cent in a single year. The gap between "
        "the " + f"{C.DEMAT_TOTAL:.2f}" + " crore total accounts and the " +
        f"{C.NSE_UNIQUE_INVESTORS:.1f}" + " crore unique registered investors indicates that the "
        "average investor holds more than one account. For the dealing desk this growth is "
        "visible as a rise in the number of small, frequent instructions rather than in average "
        "order size, which places the burden on the speed of order entry rather than on depth "
        "assessment.")

    # ---------------------------------------------------------------- 5.4
    R.section("5.4 Life of an order on the exchange terminal")
    R.body("The states through which an order passes are shown in Figure 5.3 and listed in "
           "Table 5.4; the order types a dealer selects between are set out in Table 5.5.")
    R.caption("Figure 5.3: Life of an order from instruction to settlement")
    R.image(G.fig_5_2())
    R.source(SRC_COMP)
    R.caption("Table 5.4: Order states from entry to trade confirmation")
    R.table(
        ["State", "What has happened", "What the dealer can still do"],
        [["Instruction received", "Client instruction captured and recorded",
          "Clarify quantity, price and validity before entry"],
         ["Risk-checked", "Member's pre-trade controls applied at the server",
          "Escalate to risk management if rejected"],
         ["Accepted", "Exchange has acknowledged and allotted an order number",
          "Modify or cancel"],
         ["Open", "Resting in the order book awaiting a counterparty",
          "Modify price or quantity, or cancel"],
         ["Executed", "Full quantity traded; appears in the trade book",
          "Nothing; the trade is irrevocable"],
         ["Cancelled", "Withdrawn before execution", "Re-enter if the client so instructs"],
         ["Rejected", "Failed a validation at the member or exchange level",
          "Correct the parameter or obtain limit"]],
        widths=[1900, 3600, 3500], size=9.5, align=["left", "left", "left"])
    R.source(SRC_COMP)
    R.caption("Table 5.5: Order types used during the internship and the situation calling for each")
    R.table(
        ["Order type", "Validity", "Situation in which it was used"],
        [["Limit", "Day", "The standard instruction where the client specifies a price"],
         ["Market", "Immediate", "Only in liquid scrips where execution certainty was required"],
         ["Stop-loss limit", "Day", "To cap the loss on a carried position at a defined level"],
         ["Stop-loss market", "Day", "Where exit was required irrespective of the price obtained"],
         ["Immediate or cancel", "Immediate", "To avoid leaving a resting order in a fast market"],
         ["Disclosed quantity", "Day", "On larger orders, to limit visible size and market impact"]],
        widths=[2100, 1700, 5200], size=10.5, align=["left", "center", "left"])
    R.source("Source: Author's observation during the internship. [ADD: confirm the order types "
             "actually used and delete any that were not.]")
    R.interpretation(
        "The sequence shows that a dealer's discretion is confined to a narrow window between "
        "acceptance and execution. Before acceptance the order is governed by validation rules "
        "and after execution it is irrevocable, so the whole of a dealer's judgement lies in "
        "deciding what to enter and whether to modify a resting order. This is why the "
        "order-type decision in Table 5.5 is treated on the desk as a risk decision rather than "
        "a convenience.")

    # ---------------------------------------------------------------- 5.5
    R.section("5.5 The Computer-to-Computer Link facility in practice")
    R.body("The routing of an order through the member's own infrastructure is shown in Figure "
           "5.4, the pre-trade checks applied in Table 5.6 and the operational comparison with "
           "the exchange terminal in Table 5.7.")
    R.caption("Figure 5.4: CTCL order routing and pre-trade risk checks")
    R.image(G.fig_5_3())
    R.source(SRC_COMP)
    R.caption("Table 5.6: Pre-trade risk checks applied to an order at the member's server")
    R.table(
        ["Check", "What is tested", "Consequence of failure"],
        [["Client code validity", "Code is registered, active and permitted in the segment",
          "Order rejected; compliance consulted"],
         ["Available margin", "Collateral and free balance cover the margin requirement",
          "Order rejected; client asked to fund or pledge"],
         ["Order value limit", "Single-order value within the client's ceiling",
          "Order rejected; may be split only with authority"],
         ["Price reasonability", "Price within a band around the last traded price",
          "Order rejected; protects against a keying error"],
         ["Scrip permission", "Scrip not restricted, suspended or in a ban period",
          "Order rejected or permitted only to reduce a position"],
         ["Segment permission", "Client authorised for the cash or derivatives segment",
          "Order rejected"],
         ["Terminal and user validity", "Order originates from a registered terminal and user",
          "Order rejected and the attempt logged"]],
        widths=[2200, 3600, 3200], size=9.5, align=["left", "left", "left"])
    R.source("Source: Exchange CTCL requirements and the intern's observation; checked "
             "9 October 2026.")
    R.caption("Table 5.7: Exchange terminal and CTCL compared on the desk")
    R.table(
        ["Operational aspect", "Exchange terminal", "Member CTCL terminal"],
        [["Where the order is first validated", "At the exchange",
          "At the member's server, before the exchange"],
         ["Who sets the limits", "Exchange-level parameters", "The member's risk-management team"],
         ["Source of a rejection message", "Exchange", "Member's server, in most cases"],
         ["Remedy for a rejection", "Correct the order parameter",
          "Usually a limit discussion with risk management"],
         ["Number of workstations", "One per allotted user", "Many behind a single server"],
         ["Customisation of the screen", "Minimal", "Extensive, vendor dependent"]],
        widths=[2600, 3100, 3300], size=9.5, align=["left", "left", "left"])
    R.source("Source: Author's observation and exchange CTCL circulars; checked 9 October 2026. "
             "[ADD: name of the CTCL software used by the firm and any firm-specific difference "
             "in the routing described above.]")
    R.interpretation(
        "Eight checks are applied before an order reaches the exchange, of which only two "
        "relate to the order itself and six to the client's standing, permission or capacity. "
        "The weighting indicates that the primary purpose of the pre-trade layer is credit "
        "control rather than error prevention, which follows from the settlement obligation in "
        "Section 3.8: the member must settle whether or not the client pays. The practical "
        "skill the intern acquired was diagnostic \u2014 identifying from the rejection message "
        "whether the obstacle was internal and negotiable, or external and not.")

    # ---------------------------------------------------------------- 5.6
    R.section("5.6 Futures: pricing and daily settlement")
    R.body(
        "The contract used for the worked example is specified in Table 3.10. Applying the "
        "cost-of-carry relationship to an illustrative spot price of Rs. " + inr(C.F_SPOT) +
        " at a financing rate of " + pct(C.F_RATE * 100, 0) + " per cent for " + str(C.F_DAYS) +
        " days gives the fair value computed in Table 5.8.")
    R.caption("Table 5.8: Cost-of-carry fair value of a futures contract (illustrative)")
    R.table(
        ["Input or output", "Symbol", "Value", "Basis"],
        [["Spot price", "S", "Rs. " + inr(C.F_SPOT), "illustrative"],
         ["Risk-free rate, continuously compounded", "r", pct(C.F_RATE * 100, 2) + " per cent",
          "illustrative"],
         ["Days to expiry", "t", str(C.F_DAYS) + " days", "illustrative"],
         ["Time in years", "t", f"{C.F_DAYS/365:.4f}", "Author's computation"],
         ["Theoretical futures price", "F", "Rs. " + inr(C.FUT_FAIR), "Author's computation"],
         ["Basis", "F \u2212 S", "Rs. " + inr(C.FUT_BASIS), "Author's computation"],
         ["Basis as a percentage of spot", "", pct(C.FUT_BASIS_PCT, 3) + " per cent",
          "Author's computation"]],
        widths=[3400, 1300, 2300, 2000], size=10.5,
        align=["left", "center", "center", "center"],
        total_rows=(4,))
    R.source("Source: Author's computation using F = S \u00d7 e^(r \u00d7 t); illustrative figures.")
    R.body(
        "A long position of one lot is assumed to be opened at Rs. " + inr(C.MTM_ENTRY) +
        ". Table 5.9 traces the daily settlement over the following five trading days.")
    rows = []
    prev = C.MTM_ENTRY
    for i, (p, f, cum) in enumerate(zip(C.MTM_PRICES, C.MTM_FLOWS, C.MTM_CUM), start=1):
        rows.append([f"Day {i}", "Rs. " + inr(prev), "Rs. " + inr(p),
                     "Rs. " + inr(p - prev), "Rs. " + inr(f, 0), "Rs. " + inr(cum, 0)])
        prev = p
    rows.append(["Total", "", "", "Rs. " + inr(C.MTM_PRICES[-1] - C.MTM_ENTRY),
                 "Rs. " + inr(C.MTM_TOTAL, 0), "Rs. " + inr(C.MTM_TOTAL, 0)])
    R.caption("Table 5.9: Five-day mark-to-market settlement on one long lot (illustrative)")
    R.table(
        ["Day", "Previous settlement price", "Settlement price", "Price change",
         "Daily MTM (1,000 units)", "Cumulative MTM"],
        rows,
        widths=[900, 1900, 1600, 1400, 1800, 1400], size=9.5,
        align=["center", "center", "center", "center", "center", "center"],
        total_rows=(5,))
    R.source(SRC_AUTH)
    R.caption("Figure 5.5: Daily mark-to-market cash flow on the illustrative position")
    R.image(G.fig_5_7(C.MTM_FLOWS))
    R.source(SRC_AUTH)
    R.interpretation(
        "The theoretical futures price of Rs. " + inr(C.FUT_FAIR) + " exceeds spot by Rs. " +
        inr(C.FUT_BASIS) + ", or " + pct(C.FUT_BASIS_PCT, 3) + " per cent over thirty days, "
        "which is simply the cost of financing the underlying for that period. The five daily "
        "flows sum to Rs. " + inr(C.MTM_TOTAL, 0) + ", exactly equal to the price change of "
        "Rs. " + inr(C.MTM_PRICES[-1] - C.MTM_ENTRY) + " multiplied by the lot size of 1,000 "
        "units, so daily settlement redistributes the result across days without altering it. "
        "The practical significance is that the client must fund two adverse days of Rs. " +
        inr(abs(C.MTM_FLOWS[1]), 0) + " and Rs. " + inr(abs(C.MTM_FLOWS[2]), 0) + " in cash "
        "even though the position ends profitably \u2014 the mechanism behind the shortfall "
        "scenario in Section 5.8.")

    # ---------------------------------------------------------------- 5.7
    R.section("5.7 Options: valuation, sensitivities and payoff")
    R.body(
        "An illustrative thirty-day call option on the same underlying, struck at Rs. " +
        inr(C.O_K, 0) + " with the spot at Rs. " + inr(C.O_S, 0) + ", is valued in Table 5.10 "
        "using the Black-Scholes-Merton model. Volatility is assumed at " +
        pct(C.O_SIG * 100, 0) + " per cent per annum and the risk-free rate at " +
        pct(C.O_R * 100, 0) + " per cent; both are illustrative assumptions and not market "
        "observations.")
    R.caption("Table 5.10: Black-Scholes inputs, computed price and Greeks (illustrative)")
    R.table(
        ["Item", "Symbol", "Value", "Label"],
        [["Spot price", "S", "Rs. " + inr(C.O_S), "illustrative"],
         ["Strike price", "K", "Rs. " + inr(C.O_K), "illustrative"],
         ["Time to expiry", "t", f"{C.O_T:.4f} years (30 days)", "illustrative"],
         ["Risk-free rate", "r", pct(C.O_R * 100, 2) + " per cent", "illustrative"],
         ["Volatility", "\u03c3", pct(C.O_SIG * 100, 2) + " per cent", "illustrative"],
         ["d\u2081", "d\u2081", f"{C.BS['d1']:.4f}", "Author's computation"],
         ["d\u2082", "d\u2082", f"{C.BS['d2']:.4f}", "Author's computation"],
         ["Call price", "C", "Rs. " + inr(C.CALL_PRICE), "Author's computation"],
         ["Put price at the same strike", "P", "Rs. " + inr(C.PUT_PRICE), "Author's computation"],
         ["Delta of the call", "\u0394", f"{C.BS['delta_c']:.4f}", "Author's computation"],
         ["Gamma", "\u0393", f"{C.BS['gamma']:.6f}", "Author's computation"],
         ["Theta of the call, per day", "\u0398", "Rs. " + f"{C.BS['theta_c']:.4f}",
          "Author's computation"],
         ["Vega, per one point of volatility", "\u03bd", "Rs. " + f"{C.BS['vega']:.4f}",
          "Author's computation"],
         ["Premium outlay on one lot of 1,000", "", "Rs. " + inr(C.CALL_COST, 0), "illustrative"],
         ["Break-even at expiry", "K + C", "Rs. " + inr(C.CALL_BE), "Author's computation"]],
        widths=[3300, 1300, 2500, 1900], size=10.5,
        align=["left", "center", "center", "center"], total_rows=(7, 15))
    R.source("Source: Author's computation using the Black-Scholes-Merton model with no dividend; "
             "illustrative inputs.")
    R.body("The payoff of the position at expiry across a range of underlying prices is set out "
           "in Table 5.11 and plotted in Figure 5.6.")
    R.caption("Table 5.11: Payoff of the long call at expiry (illustrative, one lot of 1,000)")
    R.table(
        ["Underlying at expiry (Rs.)", "Intrinsic value per unit (Rs.)",
         "Premium paid per unit (Rs.)", "Net profit or loss on one lot (Rs.)"],
        [[inr(s, 0), inr(i), inr(C.CALL_PRICE), inr(n, 0)] for s, i, n in C.CALL_PAYOFF],
        widths=[2300, 2400, 2200, 2100], size=9.5,
        align=["center", "center", "center", "center"])
    R.source(SRC_AUTH)
    R.caption("Figure 5.6: Payoff of the long call with break-even marked")
    R.image(G.fig_5_8(C.O_K, C.CALL_PRICE, C.O_LOT))
    R.source(SRC_AUTH)
    R.body(
        "Premium decomposition is shown next. If the same option were quoted in the market at "
        "Rs. " + inr(C.MKT_PREM) + " while the spot stood at Rs. " + inr(C.O_S) + ", the entire "
        "premium would be time value, because the option is out of the money and its intrinsic "
        "value is nil.")
    R.caption("Table 5.12: Premium decomposition of the illustrative call")
    R.table(
        ["Component", "Formula", "Value (Rs. per unit)"],
        [["Market premium", "Observed quote", inr(C.MKT_PREM)],
         ["Intrinsic value", "max(S \u2212 K, 0) = max(1,250 \u2212 1,260, 0)", inr(C.INTRINSIC)],
         ["Time value", "Premium \u2212 intrinsic value", inr(C.TIMEVAL)]],
        widths=[2600, 4200, 2200], size=10.5, align=["left", "left", "center"],
        total_rows=(2,))
    R.source(SRC_AUTH)
    R.caption("Figure 5.7: Decay of the call premium as expiry approaches, spot held constant")
    R.image(G.fig_5_10(C.DECAY_PRICES, C.DECAY_DAYS))
    R.source("Source: Author's computation using the Black-Scholes model with the spot price and "
             "volatility held constant; illustrative.")
    R.body(
        "Finally, a **long straddle** is constructed at the money by buying both a call and a put "
        "struck at Rs. " + inr(C.O_S, 0) + ". The combined premium is Rs. " + inr(C.STR_TOT) +
        " per unit, producing two break-even points.")
    R.caption("Table 5.13: Payoff of a long at-the-money straddle (illustrative, one lot)")
    R.table(
        ["Underlying at expiry (Rs.)", "Net profit or loss on one lot (Rs.)"],
        [[inr(s), inr(n, 0)] for s, n in C.STRADDLE_PAYOFF],
        widths=[4500, 4500], size=10.5, align=["center", "center"])
    R.source(SRC_AUTH)
    R.interpretation(
        "The computed call price of Rs. " + inr(C.CALL_PRICE) + " carries a delta of " +
        f"{C.BS['delta_c']:.4f}" + ", so the option behaves like roughly half a unit of the "
        "underlying, and a theta of Rs. " + f"{abs(C.BS['theta_c']):.4f}" + " per day, the "
        "amount lost for each day that passes without movement. The decay path in Figure 5.7 "
        "shows the consequence: the premium falls from Rs. " + inr(C.DECAY_PRICES[0]) +
        " with thirty days remaining to Rs. " + inr(C.DECAY_PRICES[-3]) + " with five days "
        "remaining, so about " + pct((1 - C.DECAY_PRICES[-3] / C.DECAY_PRICES[0]) * 100, 0) +
        " per cent of the value is lost in the last five days alone. The straddle requires a "
        "move of " + pct(C.STR_TOT / C.O_S * 100) + " per cent in either direction merely to "
        "break even, which makes strategies of this kind considerably less forgiving than "
        "clients commonly assume.")

    # ---------------------------------------------------------------- 5.8
    R.section("5.8 Margin and the mechanics of a shortfall")
    R.body(
        "The margin requirement on the futures position opened in Section 5.6 is built up in "
        "Table 5.14 using illustrative percentages; the actual scenario parameters used by the "
        "clearing corporation are proprietary and vary daily.")
    R.caption("Table 5.14: Margin build-up on one long futures lot (illustrative)")
    R.table(
        ["Component", "Basis", "Rate", "Amount (Rs.)"],
        [["Contract value", "Entry price 1,257.00 \u00d7 lot 1,000", "",
          inr(C.M_CONTRACT_VALUE, 0)],
         ["SPAN / initial margin", "Contract value \u00d7 rate", pct(C.M_SPAN_PCT) + "%",
          inr(C.M_SPAN, 0)],
         ["Exposure margin", "Contract value \u00d7 rate", pct(C.M_EXP_PCT) + "%",
          inr(C.M_EXP, 0)],
         ["Total margin required", "SPAN + exposure", pct(C.M_SPAN_PCT + C.M_EXP_PCT) + "%",
          inr(C.M_TOTAL, 0)],
         ["Margin as a percentage of contract value", "Total margin / contract value", "",
          pct(C.M_TOTAL_PCT) + "%"]],
        widths=[3300, 2700, 1300, 1700], size=10.5,
        align=["left", "left", "center", "center"], total_rows=(3,))
    R.source(SRC_AUTH)
    R.body(
        "The client is assumed to have placed collateral of Rs. " + inr(C.M_COLLATERAL, 0) +
        ", comfortably above the requirement at entry. Table 5.15 shows what happens when the "
        "underlying falls to Rs. " + inr(C.M_LOSS_PRICE) + ".")
    R.caption("Table 5.15: Margin shortfall and square-off scenario (illustrative)")
    R.table(
        ["Step", "Computation", "Amount (Rs.)"],
        [["Collateral placed by the client", "Given", inr(C.M_COLLATERAL, 0)],
         ["Margin required at entry", "From Table 5.14", inr(C.M_TOTAL, 0)],
         ["Surplus at entry", "1,75,000 \u2212 1,63,410",
          inr(C.M_COLLATERAL - C.M_TOTAL, 0)],
         ["Mark-to-market loss on the fall to 1,232.00",
          "(1,232.00 \u2212 1,257.00) \u00d7 1,000", inr(C.M_LOSS, 0)],
         ["Collateral after the loss is debited", "1,75,000 \u2212 25,000", inr(C.M_AFTER, 0)],
         ["Margin required at the lower price", "1,232.00 \u00d7 1,000 \u00d7 13.00%",
          inr(C.M_REQ_AFTER, 0)],
         ["Shortfall", "1,60,160 \u2212 1,50,000", inr(C.M_SHORTFALL, 0)]],
        widths=[3600, 3200, 2200], size=10.5, align=["left", "left", "center"],
        total_rows=(6,))
    R.source(SRC_AUTH)
    R.interpretation(
        "At entry the client held a surplus of Rs. " + inr(C.M_COLLATERAL - C.M_TOTAL, 0) +
        " over the requirement of Rs. " + inr(C.M_TOTAL, 0) + ", an apparently comfortable "
        "position. A fall of " + pct((C.MTM_ENTRY - C.M_LOSS_PRICE) / C.MTM_ENTRY * 100) +
        " per cent converts that surplus into a shortfall of Rs. " + inr(C.M_SHORTFALL, 0) +
        ". The mark-to-market loss of Rs. " + inr(abs(C.M_LOSS), 0) + " is debited from "
        "collateral while the requirement falls only slightly, from Rs. " + inr(C.M_TOTAL, 0) +
        " to Rs. " + inr(C.M_REQ_AFTER, 0) + ", because it is computed on a contract value that "
        "has itself fallen. Collateral therefore declines faster than the requirement. This "
        "asymmetry is the single most important thing a new dealer must understand, and it is "
        "why the margin-alert response in Table 5.1 is treated as time-critical.")

    # ---------------------------------------------------------------- 5.9
    R.section("5.9 Contract note and transaction charges")
    R.body(
        "The rates set out in Table 3.17 are applied here to two illustrative transactions. The "
        "first is a delivery-based round trip of 100 shares bought and sold at Rs. 1,000, at a "
        "brokerage of " + pct(C.DEL_BROK, 2) + " per cent on each side.")
    R.caption("Table 5.16: Charge computation on an illustrative delivery round trip")
    R.table(
        ["Charge", "Rate applied", "Base", "Amount (Rs.)"],
        [["Buy value", "100 shares \u00d7 Rs. 1,000", "", inr(C.DEL_BUY, 0)],
         ["Sell value", "100 shares \u00d7 Rs. 1,000", "", inr(C.DEL_SELL, 0)],
         ["Brokerage", pct(C.DEL_BROK) + "% each side", "Buy + sell value",
          inr(C.DEL["brokerage"])],
         ["Securities Transaction Tax", "0.10% each side", "Buy + sell value", inr(C.DEL["stt"])],
         ["NSE transaction charges", "0.00297%", "Buy + sell value", inr(C.DEL["exchange"])],
         ["SEBI turnover fee", "0.0001%", "Buy + sell value", inr(C.DEL["sebi"])],
         ["Stamp duty", "0.015%", "Buy value only", inr(C.DEL["stamp"])],
         ["Goods and services tax", "18%", "Brokerage + exchange + SEBI", inr(C.DEL["gst"])],
         ["Total charges", "", "", inr(C.DEL["total"])],
         ["Break-even move required per share", "Total charges / 100 shares", "",
          inr(C.DEL_BREAKEVEN)]],
        widths=[2800, 2100, 2300, 1800], size=10.5,
        align=["left", "center", "left", "center"], total_rows=(8, 9))
    R.source("Source: Author's computation applying the rates in Table 3.17; illustrative figures.")
    R.caption("Figure 5.8: Composition of total charges on the delivery round trip")
    R.image(G.fig_5_11(
        ["Securities\nTransaction Tax", "Brokerage", "Goods and\nservices tax",
         "Stamp duty", "Exchange\ncharges", "SEBI fee"],
        [C.DEL["stt"], C.DEL["brokerage"], C.DEL["gst"], C.DEL["stamp"],
         C.DEL["exchange"], C.DEL["sebi"]]))
    R.source(SRC_AUTH)
    R.body(
        "The second transaction is an intraday trade of Rs. " + inr(C.INT_BUY, 0) + " bought and "
        "Rs. " + inr(C.INT_SELL, 0) + " sold on the same day at a flat brokerage of Rs. 20 per "
        "executed order.")
    R.caption("Table 5.17: Charge computation on an illustrative intraday trade")
    R.table(
        ["Charge", "Rate applied", "Base", "Amount (Rs.)"],
        [["Brokerage", "Rs. 20 per order, two orders", "", inr(C.INT["brokerage"])],
         ["Securities Transaction Tax", "0.025%", "Sell value only", inr(C.INT["stt"])],
         ["NSE transaction charges", "0.00297%", "Buy + sell value", inr(C.INT["exchange"])],
         ["SEBI turnover fee", "0.0001%", "Buy + sell value", inr(C.INT["sebi"])],
         ["Stamp duty", "0.003%", "Buy value only", inr(C.INT["stamp"])],
         ["Goods and services tax", "18%", "Brokerage + exchange + SEBI", inr(C.INT["gst"])],
         ["Total charges", "", "", inr(C.INT["total"])],
         ["Gross profit on the trade", "5,02,500 \u2212 5,00,000", "", inr(C.INT_GROSS, 0)],
         ["Net profit after charges", "2,500.00 \u2212 total charges", "", inr(C.INT_NET)],
         ["Charges as a percentage of gross profit", "", "", pct(C.INT_DRAG) + "%"]],
        widths=[2800, 2300, 2100, 1800], size=10.5,
        align=["left", "center", "left", "center"], total_rows=(6, 8, 9))
    R.source("Source: Author's computation applying the rates in Table 3.17; illustrative figures.")
    R.interpretation(
        "On the delivery round trip the total cost of Rs. " + inr(C.DEL["total"]) + " requires "
        "the share to move Rs. " + inr(C.DEL_BREAKEVEN) + ", or about " +
        pct(C.DEL_BREAKEVEN / 1000 * 100, 2) + " per cent, before the client is even. The "
        "Securities Transaction Tax contributes Rs. " + inr(C.DEL["stt"]) + " of that total "
        "against brokerage of only Rs. " + inr(C.DEL["brokerage"]) + ", so the statutory "
        "component is the larger constraint. On the intraday trade the charges of Rs. " +
        inr(C.INT["total"]) + " absorb " + pct(C.INT_DRAG) + " per cent of a gross profit of "
        "Rs. " + inr(C.INT_GROSS, 0) + ", leaving Rs. " + inr(C.INT_NET) + ". Frequency of "
        "trading, rather than size, is therefore the dominant determinant of total cost.")

    # ================================================================ 5.10
    R.section("5.10 Company analysis: Pine Labs Limited")

    R.sub("5.10.1 Company overview")
    R.body(
        "**Pine Labs Limited**, formerly Pine Labs Private Limited, is a merchant-commerce and "
        "payments technology company. It provides digital checkout infrastructure to merchants, "
        "affordability and value-added services at the point of sale, online payment "
        "acceptance, and issuing and processing services covering prepaid instruments, gift "
        "cards and card-related infrastructure for banks and consumer brands. The company "
        "states that it operates in more than twenty-two countries. Its identification details "
        "are set out in Table 5.18.")
    R.caption("Table 5.18: Pine Labs Limited \u2014 company identification")
    R.table(
        ["Particular", "Detail"],
        [["Name", "Pine Labs Limited (formerly Pine Labs Private Limited)"],
         ["NSE symbol", "PINELABS"],
         ["BSE scrip code", "544606"],
         ["ISIN", "INE15B701018"],
         ["Date of listing", "14 November 2025, on both the NSE and the BSE"],
         ["Initial public offer size", "Rs. 3,899.91 crore"],
         ["Price band and issue price", "Rs. 210 to Rs. 221; issued at Rs. 221"],
         ["Listing-day opening price", "Rs. 242 on both exchanges"],
         ["Overall subscription and face value", "About 2.46 times; Rs. 1 per equity share"],
         ["Shares outstanding after the issue", inr(C.PL_SHARES_POST, 0) + " equity shares"],
         ["Managing Director and CEO", "Amrish Rau"],
         ["Group Chief Financial Officer", "Sameer Kamath"],
         ["Book-running lead manager and registrar",
          "Axis Capital Limited; KFin Technologies Limited"]],

        widths=[3300, 5700], size=10.5, align=["left", "left"])
    R.source("Source: Pine Labs Limited offer documents and exchange listing records; checked "
             "9 October 2026.")

    R.sub("5.10.2 Industry background")
    R.body(
        "The company operates in the Indian digital payments and merchant-commerce industry, "
        "which has expanded rapidly on the back of the unified payments interface and the "
        "migration of small retailers from cash to electronic acceptance. Three characteristics "
        "bear on the analysis that follows. First, the economics are **volume-driven and "
        "take-rate-thin**: providers process very large transaction value and retain a small "
        "fraction of it, so profitability depends on operating leverage rather than margin per "
        "transaction. Second, the highest-volume rail carries no merchant discount rate on most "
        "person-to-merchant transactions, forcing providers to monetise through subscriptions, "
        "devices, credit distribution and value-added services. Third, the industry is "
        "**closely regulated** by the Reserve Bank of India in respect of payment aggregation, "
        "prepaid instruments and card data, so a regulatory change can alter a revenue line "
        "directly. "
        "[ADD: insert verified industry-size and transaction-volume data from RBI payment-system "
        "statistics or NPCI monthly data, with the month and the date checked.]")

    R.sub("5.10.3 Business model and revenue streams")
    R.caption("Table 5.19: Pine Labs Limited \u2014 reported segments and revenue streams")
    R.table(
        ["Segment", "What it comprises", "How it is monetised",
         "FY26 revenue (Rs. crore)", "Share of segment revenue (%)"],
        [["Digital Infrastructure and Transaction Platform",
          "Checkout infrastructure, affordability and value-added services, transaction "
          "processing, online payments",
          "Device subscriptions, transaction fees, platform fees from merchants, brands and "
          "lenders", inr(C.PL_DITP[-1]), pct(C.PL_DITP_SHARE26)],
         ["Issuing and Acquiring Platform",
          "Issuing and processing services, prepaid cards, gift cards, interest on float, "
          "breakage income",
          "Processing fees, distribution margin, float income and unredeemed balances",
          inr(C.PL_IAP[-1]), pct(C.PL_IAP_SHARE26)],
         ["Total", "", "", inr(C.PL_REV[-1]), "100.00"]],
        widths=[2000, 2500, 2300, 1200, 1000], size=9.5,
        align=["left", "left", "left", "center", "center"], total_rows=(2,))
    R.source(SRC_PL_FY26)
    R.caption("Figure 5.9: Segment revenue mix")
    R.image(G.fig_5_14(C.PL_YEARS, C.PL_DITP, C.PL_IAP))
    R.source(SRC_PL_FY26 + " FY23 to FY25 from the Red Herring Prospectus.")
    R.interpretation(
        "The Digital Infrastructure and Transaction Platform segment contributed Rs. " +
        inr(C.PL_DITP[-1]) + " crore, or " + pct(C.PL_DITP_SHARE26) + " per cent of segment "
        "revenue in FY2025-26, and remains the core of the business. The Issuing and Acquiring "
        "Platform grew faster, at " + pct(C.PL_IAP_G26) + " per cent against " +
        pct(C.PL_DITP_G26) + " per cent, and its share has risen steadily across the four years "
        "in Figure 5.9. The mix shift matters because the issuing business includes float "
        "income and breakage on unredeemed prepaid balances, which are high-margin but more "
        "exposed to regulatory change than a subscription fee, as discussed in Section "
        "5.10.10.")

    R.sub("5.10.4 Financial performance, FY2022-23 to FY2025-26")
    rows = []
    for i, y in enumerate(C.PL_YEARS):
        g = "\u2014" if i == 0 else pct(C.PL_GROWTH[i - 1])
        rows.append([y, inr(C.PL_REV[i]), g, inr(C.PL_PAT[i]),
                     pct(C.PL_PAT[i] / C.PL_REV[i] * 100)])
    R.caption("Table 5.20: Pine Labs Limited \u2014 consolidated financial performance")
    R.table(
        ["Financial year", "Revenue from operations (Rs. crore)", "Revenue growth (%)",
         "Profit / (loss) after tax (Rs. crore)", "Net profit margin (%)"],
        rows, widths=[1600, 2300, 1700, 2100, 1300], size=9.5,
        align=["center", "center", "center", "center", "center"], total_rows=(3,))
    R.source("Source: FY23 to FY25 from the Red Herring Prospectus, restated consolidated "
             "financial information; FY26 from the audited consolidated results for the year "
             "ended 31 March 2026. Growth and margin are the author's computation. Checked "
             "9 October 2026.")
    R.caption("Figure 5.10: Revenue and profit after tax, FY2022-23 to FY2025-26")
    R.image(G.fig_5_12(C.PL_YEARS, C.PL_REV, C.PL_PAT))
    R.source(SRC_PL_FY26 + " Earlier years from the Red Herring Prospectus.")
    R.caption("Table 5.21: Other consolidated financial indicators")
    R.table(
        ["Indicator", "FY2024-25", "FY2025-26", "Change"],
        [["Total income (Rs. crore)", inr(C.PL_TOTINC[-2]), inr(C.PL_TOTINC[-1]),
          "+" + pct((C.PL_TOTINC[-1] / C.PL_TOTINC[-2] - 1) * 100) + "%"],
         ["Adjusted EBITDA (Rs. crore)", inr(C.PL_AEBITDA_FY25), inr(C.PL_AEBITDA_FY26),
          "+" + pct(C.PL_AEB_GROWTH) + "%"],
         ["Adjusted EBITDA margin (%)", pct(C.PL_AEB_MARGIN25), pct(C.PL_AEB_MARGIN26),
          "+" + pct(C.PL_AEB_MARGIN26 - C.PL_AEB_MARGIN25) + " pp"],
         ["Contribution margin (%)", pct(C.PL_CONTRIB_FY25), pct(C.PL_CONTRIB_FY26),
          pct(C.PL_CONTRIB_FY26 - C.PL_CONTRIB_FY25) + " pp"],
         ["Operating cash flow (Rs. crore)", inr(C.PL_OCF[-2]), inr(C.PL_OCF[-1]),
          "\u00d7" + f"{C.PL_OCF[-1]/C.PL_OCF[-2]:.1f}"],
         ["Total equity (Rs. crore)", "[ADD: verify]", inr(C.PL_EQUITY_FY26), "\u2014"],
         ["Cash and cash equivalents (Rs. crore)", inr(C.PL_CASH_FY25), inr(C.PL_CASH_FY26),
          "\u00d7" + f"{C.PL_CASH_FY26/C.PL_CASH_FY25:.1f}"]],
        widths=[3000, 2000, 2000, 2000], size=10.5,
        align=["left", "center", "center", "center"])
    R.source(SRC_PL_FY26 + " Percentage changes are the author's computation. Adjusted EBITDA is "
             "a measure defined by the company and is not a measure prescribed by accounting "
             "standards.")
    R.interpretation(
        "Revenue rose from Rs. " + inr(C.PL_REV[0]) + " crore in FY2022-23 to Rs. " +
        inr(C.PL_REV[-1]) + " crore in FY2025-26, a compound annual growth rate of " +
        pct(C.PL_CAGR) + " per cent, while the result moved from a loss of Rs. " +
        inr(abs(C.PL_PAT[0])) + " crore to a profit of Rs. " + inr(C.PL_PAT[-1]) + " crore. The "
        "decisive year was FY2025-26: revenue grew " + pct(C.PL_GROWTH[-1]) + " per cent but "
        "adjusted EBITDA grew " + pct(C.PL_AEB_GROWTH) + " per cent. Profit growing far faster "
        "than revenue while contribution margin edged **down** from " + pct(C.PL_CONTRIB_FY25) +
        " to " + pct(C.PL_CONTRIB_FY26) + " per cent indicates that the improvement came from "
        "operating leverage on fixed costs rather than from better unit economics. The cash "
        "evidence supports the reported profit: operating cash flow of Rs. " + inr(C.PL_OCF[-1]) +
        " crore is " + f"{C.PL_OCF_PAT:.2f}" + " times profit after tax, the opposite of the "
        "divergence that would warrant concern.")

    R.body("The most recent reported period is the quarter ended 30 June 2026, set out in "
           "Table 5.22.")
    R.caption("Table 5.22: Pine Labs Limited \u2014 Q1 FY2026-27 against Q1 FY2025-26")
    R.table(
        ["Particular (Rs. crore unless stated)", "Q1 FY2026-27", "Q1 FY2025-26", "Change (%)"],
        [["Revenue from operations", inr(C.Q_REV27), inr(C.Q_REV26), pct(C.Q_REV_G)],
         ["Total income", inr(C.Q_TOT27), inr(C.Q_TOT26),
          pct((C.Q_TOT27 / C.Q_TOT26 - 1) * 100)],
         ["Profit / (loss) before tax", inr(C.Q_PBT27), inr(C.Q_PBT26), "not meaningful"],
         ["Profit after tax", inr(C.Q_PAT27), inr(C.Q_PAT26), pct(C.Q_PAT_G)],
         ["Contribution margin (%)", pct(C.Q_CONTRIB_M27), pct(C.Q_CONTRIB_M26),
          pct(C.Q_CM_DROP) + " pp"],
         ["Adjusted EBITDA", inr(C.Q_AEB27), inr(C.Q_AEB26),
          pct((C.Q_AEB27 / C.Q_AEB26 - 1) * 100)],
         ["Adjusted EBITDA margin (%)", pct(C.Q_AEB_M27), pct(C.Q_AEB_M26),
          pct(C.Q_AEB_M27 - C.Q_AEB_M26) + " pp"],
         ["Segment \u2014 digital infrastructure", inr(C.Q_DITP27), inr(C.Q_DITP26),
          pct(C.Q_DITP_G)],
         ["Segment \u2014 issuing and acquiring", inr(C.Q_IAP27), inr(C.Q_IAP26),
          pct(C.Q_IAP_G)],
         ["Basic earnings per share (Rs.)", f"{C.Q_EPS27:.2f}", f"{C.Q_EPS26:.2f}", "\u2014"]],
        widths=[3400, 1900, 1900, 1800], size=10.5,
        align=["left", "center", "center", "center"], total_rows=(4,))
    R.source(SRC_PL_Q1 + " Percentage changes are the author's computation.")
    R.interpretation(
        "Revenue grew " + pct(C.Q_REV_G) + " per cent to Rs. " + inr(C.Q_REV27) + " crore and "
        "profit after tax rose " + pct(C.Q_PAT_G) + " per cent to Rs. " + inr(C.Q_PAT27) +
        " crore, with profit before tax turning positive. The figure that deserves attention, "
        "however, is the contribution margin, which fell " + pct(abs(C.Q_CM_DROP)) +
        " percentage points to " + pct(C.Q_CONTRIB_M27) + " per cent, and the adjusted EBITDA "
        "margin, which fell from " + pct(C.Q_AEB_M26) + " to " + pct(C.Q_AEB_M27) + " per cent "
        "despite the revenue growth. Management attributes this to deliberate investment in "
        "salesforce, cloud and network capacity. The quarter therefore shows continued top-line "
        "momentum with a pause in margin expansion, and the full-year outcome will test whether "
        "the pause is seasonal or structural.")

    R.sub("5.10.5 Ratio analysis")
    R.caption("Table 5.23: Pine Labs Limited \u2014 ratio analysis, FY2025-26")
    R.table(
        ["Ratio", "Formula applied", "Computation", "Value"],
        [["Net profit margin", "PAT / revenue \u00d7 100", "112.50 / 2,710.60 \u00d7 100",
          pct(C.PL_NPM_FY26) + "%"],
         ["Net profit margin, FY2024-25", "PAT / revenue \u00d7 100",
          "\u2212145.49 / 2,274.27 \u00d7 100", pct(C.PL_NPM_FY25) + "%"],
         ["Adjusted EBITDA margin", "Adjusted EBITDA / revenue \u00d7 100",
          "559 / 2,710.60 \u00d7 100", pct(C.PL_AEB_MARGIN26) + "%"],
         ["Return on equity", "PAT / total equity \u00d7 100", "112.50 / 5,895 \u00d7 100",
          pct(C.PL_ROE_FY26) + "%"],
         ["Return on assets", "PAT / total assets \u00d7 100", "112.50 / 13,297 \u00d7 100",
          pct(C.PL_ROA_FY26) + "%"],
         ["Asset turnover", "Revenue / average total assets",
          "2,710.60 / 12,006.50", f"{C.PL_ASSET_TURN:.3f}"],
         ["Cash conversion", "Operating cash flow / PAT", "395.40 / 112.50",
          f"{C.PL_OCF_PAT:.2f}\u00d7"],
         ["Revenue CAGR, FY23 to FY26", "((2,710.60/1,597.66)^(1/3) \u2212 1) \u00d7 100",
          "three-year compounding", pct(C.PL_CAGR) + "%"],
         ["Earnings per share, FY2025-26", "PAT / shares outstanding",
          "112.50 crore / 114.83 crore shares", "Rs. " + f"{C.PL_EPS_FY26:.2f}"]],
        widths=[2200, 2600, 2400, 1800], size=9.5,
        align=["left", "left", "left", "center"])
    R.source("Source: Author's computation from the audited consolidated results for FY2025-26 "
             "and the Red Herring Prospectus; checked 9 October 2026.")
    R.interpretation(
        "The ratios describe a company at the very beginning of profitability rather than a "
        "mature one. A net profit margin of " + pct(C.PL_NPM_FY26) + " per cent and a return on "
        "equity of " + pct(C.PL_ROE_FY26) + " per cent are low in absolute terms, but they "
        "follow a margin of " + pct(C.PL_NPM_FY25) + " per cent in the preceding year, so the "
        "direction is more informative than the level. Asset turnover of " +
        f"{C.PL_ASSET_TURN:.3f}" + " is strikingly low for a technology business and reflects "
        "the float and settlement balances a payments processor carries; it should not be read "
        "as inefficiency. Cash conversion of " + f"{C.PL_OCF_PAT:.2f}" + " times profit "
        "indicates that reported earnings are supported by cash. The weakest number is the "
        "return on equity, and its improvement depends on whether the operating leverage of "
        "FY2025-26 continues, which the Q1 margin compression leaves open.")

    R.sub("5.10.6 Shareholding pattern")
    R.caption("Table 5.24: Pine Labs Limited \u2014 shareholding pattern, quarter ended June 2026")
    R.table(
        ["Category", "Holding (%)"],
        [[n, pct(v)] for n, v in C.PL_SH] + [["Total", pct(C.PL_SH_TOTAL)]],
        widths=[5500, 3500], size=10.5, align=["left", "center"], total_rows=(4,))
    R.source("Source: Shareholding-pattern filing for the quarter ended 30 June 2026; checked "
             "9 October 2026.")
    R.caption("Figure 5.11: Shareholding pattern")
    R.image(G.fig_5_15([n for n, _ in C.PL_SH], [v for _, v in C.PL_SH]))
    R.source("Source: Shareholding-pattern filing for the quarter ended 30 June 2026.")
    R.interpretation(
        "The most significant feature of the pattern is that promoter holding is nil, which is "
        "characteristic of a venture-funded technology company that has listed after several "
        "private rounds and in which no single shareholder exercises control. Domestic "
        "institutions hold " + pct(C.PL_SH[1][1]) + " per cent and foreign portfolio investors " +
        pct(C.PL_SH[2][1]) + " per cent, with " + pct(C.PL_SH[3][1]) + " per cent in public and "
        "other hands, a category that here includes directors and individual pre-listing "
        "shareholders. The absence of a promoter removes the pledge and related-party concerns "
        "that dominate governance analysis of family-controlled Indian companies, but replaces "
        "them with another: there is no controlling shareholder with a long-term capital "
        "commitment, so the free float is more exposed to institutional repositioning.")

    R.sub("5.10.7 Market data and valuation")
    R.caption("Table 5.25: Pine Labs Limited \u2014 market data and valuation, as on 25 September 2026")
    R.table(
        ["Measure", "Value", "Basis"],
        [["Closing price", "Rs. " + inr(C.PL_PRICE), "Exchange close"],
         ["Market capitalisation", "Rs. " + inr(C.PL_MCAP, 0) + " crore", "Exchange data"],
         ["52-week high", "Rs. " + inr(C.PL_52H), "Exchange data"],
         ["52-week low", "Rs. " + inr(C.PL_52L), "Exchange data"],
         ["Issue price", "Rs. " + inr(C.PL_ISSUE), "Offer document"],
         ["Listing-day premium over issue price", pct(C.PL_LIST_POP) + "%",
          "Author's computation"],
         ["Current price against issue price", pct(C.PL_VS_ISSUE) + "%", "Author's computation"],
         ["Current price against the 52-week high", pct(C.PL_VS_HIGH) + "%",
          "Author's computation"],
         ["Earnings per share, FY2025-26", "Rs. " + f"{C.PL_EPS_FY26:.2f}",
          "Author's computation"],
         ["Price to earnings, on FY2025-26 earnings", f"{C.PL_PE_FY26:.1f}\u00d7",
          "Author's computation"],
         ["Price to book", f"{C.PL_PB:.2f}\u00d7", "Author's computation"],
         ["Price to sales, on FY2025-26 revenue", f"{C.PL_PS:.2f}\u00d7", "Author's computation"],
         ["Dividend", "Nil declared since listing", "Company disclosure"]],
        widths=[3700, 2500, 2800], size=10.5, align=["left", "center", "left"])
    R.source("Source: Exchange market data as on 25 September 2026 and the company's audited "
             "FY2025-26 results; ratios are the author's computation. Checked 9 October 2026.")
    R.interpretation(
        "The valuation picture is dominated by the shortness of the listed history and by the "
        "fact that the company only just became profitable. At Rs. " + inr(C.PL_PRICE) +
        " the share trades " + pct(abs(C.PL_VS_ISSUE)) + " per cent below its issue price and " +
        pct(abs(C.PL_VS_HIGH)) + " per cent below its 52-week high, while standing " +
        pct(C.PL_VS_LOW) + " per cent above its low; a range of " + pct(C.PL_52_RANGE) +
        " per cent of the low in under a year indicates considerable volatility. The "
        "price-to-earnings multiple of about " + f"{C.PL_PE_FY26:.0f}" + " times is "
        "arithmetically correct but of limited analytical use, because it divides by a "
        "first-year profit of Rs. " + inr(C.PL_EPS_FY26, 2) + " per share; the price-to-sales "
        "multiple of " + f"{C.PL_PS:.2f}" + " times and the price-to-book of " +
        f"{C.PL_PB:.2f}" + " times are more stable reference points at this stage. No "
        "multi-year price chart is presented, because the company has been listed for under "
        "eleven months.")

    R.sub("5.10.8 Peer comparison")
    R.body(
        "Four listed comparators have been selected: One97 Communications Limited (Paytm), the "
        "closest listed analogue in merchant payments and distribution; Infibeam Avenues "
        "Limited, which operates a payment gateway and is comparable in online acceptance; One "
        "MobiKwik Systems Limited, comparable in consumer and merchant payments at a smaller "
        "scale; and Zaggle Prepaid Ocean Services Limited, comparable to the issuing and "
        "prepaid side. Razorpay, PhonePe and BharatPe are excluded because they were not listed "
        "entities with comparable public disclosure at the time of writing.")
    R.caption("Table 5.26: Pine Labs Limited and listed peers")
    R.table(
        ["Company", "Principal business", "Latest full-year revenue (Rs. crore)",
         "Latest full-year PAT (Rs. crore)", "Comment"],
        [["Pine Labs Limited", "Merchant commerce, payments and issuing",
          inr(C.PL_REV[-1]), inr(C.PL_PAT[-1]), "First full year of profit in FY2025-26"],
         ["One97 Communications (Paytm)", "Merchant payments, distribution of credit",
          "[ADD: verify]", "[ADD: verify]", "Largest listed comparator by scale"],
         ["Infibeam Avenues", "Online payment gateway and platforms",
          "[ADD: verify]", "[ADD: verify]", "Comparable in online acceptance"],
         ["One MobiKwik Systems", "Consumer and merchant digital payments",
          "[ADD: verify]", "[ADD: verify]", "Smaller scale, consumer-weighted"],
         ["Zaggle Prepaid Ocean Services", "Prepaid instruments and spend management",
          "[ADD: verify]", "[ADD: verify]", "Comparable to the issuing segment"]],
        widths=[1900, 2300, 1700, 1600, 1500], size=9.5,
        align=["left", "left", "center", "center", "left"])
    R.source("Source: Pine Labs figures from the audited FY2025-26 consolidated results. Peer "
             "figures could not be verified against the respective companies' own filings in the "
             "time available and are marked for completion; they must be taken from each "
             "company's annual report or results filing before submission.")

    R.sub("5.10.9 SWOT analysis")
    R.caption("Table 5.27: Pine Labs Limited \u2014 SWOT analysis")
    R.table(
        ["Strengths", "Weaknesses"],
        [["\u2022 Large installed base of digital checkout points and a long-standing merchant "
          "relationship base.\n\u2022 Two distinct revenue engines, with the issuing platform "
          "growing at " + pct(C.PL_IAP_G26) + " per cent against " + pct(C.PL_DITP_G26) +
          " per cent for the core.\n\u2022 Demonstrated operating leverage: adjusted EBITDA grew "
          + pct(C.PL_AEB_GROWTH) + " per cent on revenue growth of " + pct(C.PL_GROWTH[-1]) +
          " per cent in FY2025-26.\n\u2022 Strong cash generation, with operating cash flow at " +
          f"{C.PL_OCF_PAT:.2f}" + " times profit after tax, and a substantial net cash position.",
          "\u2022 Profitability is very thin: a net margin of " + pct(C.PL_NPM_FY26) +
          " per cent and a return on equity of " + pct(C.PL_ROE_FY26) + " per cent.\n"
          "\u2022 Contribution margin declined in FY2025-26 and again in Q1 FY2026-27, to " +
          pct(C.Q_CONTRIB_M27) + " per cent.\n\u2022 Dependence on a company-defined adjusted "
          "EBITDA measure to present profitability.\n\u2022 Short listed history limits the "
          "reliability of market-based valuation."]],
        widths=[4500, 4500], size=9.5, align=["left", "left"])
    R.table(
        ["Opportunities", "Threats"],
        [["\u2022 International business growing from a small base across more than twenty-two "
          "markets.\n\u2022 Continued migration of small and mid-market merchants from cash to "
          "electronic acceptance.\n\u2022 Cross-sell of credit, affordability and value-added "
          "services over an installed device base.\n\u2022 Operating leverage has further room "
          "if indirect costs continue to grow more slowly than revenue.",
          "\u2022 Regulatory change affecting prepaid instruments, float income or unredeemed "
          "balances, which are high-margin revenue lines.\n\u2022 Intense competition from both "
          "listed and large unlisted payment providers, several of which are better "
          "capitalised.\n\u2022 Zero or near-zero merchant discount on the fastest-growing "
          "payment rail.\n\u2022 Valuation risk: a high multiple of a very small first-year "
          "profit leaves limited tolerance for disappointment."]],
        widths=[4500, 4500], size=9.5, align=["left", "left"])
    R.source("Source: Author's analysis based on the company's FY2025-26 and Q1 FY2026-27 "
             "filings; checked 9 October 2026.")

    R.sub("5.10.10 Risks and outlook")
    for lead, txt in [
        ("Regulatory risk",
         "the issuing and prepaid business derives part of its margin from float income and from "
         "balances that are never redeemed; a change in the treatment of either would affect a "
         "disproportionately profitable revenue line."),
        ("Margin risk",
         "contribution margin fell in FY2025-26 and again in the first quarter of FY2026-27, to " +
         pct(C.Q_CONTRIB_M27) + " per cent, and the company attributes this to investment rather "
         "than pricing; if the explanation proves incomplete, the operating leverage thesis "
         "weakens."),
        ("Competitive risk",
         "merchant payments in India is contested by very large unlisted competitors whose "
         "pricing is not constrained by the need to report quarterly profit."),
        ("Concentration and mix risk",
         pct(C.PL_DITP_SHARE26) + " per cent of segment revenue still comes from the digital "
         "infrastructure platform, and that segment grew at only " + pct(C.PL_DITP_G26) +
         " per cent in FY2025-26."),
        ("Valuation risk",
         "at about " + f"{C.PL_PE_FY26:.0f}" + " times FY2025-26 earnings the share price "
         "embeds a sustained improvement in profitability; the stock already trades " +
         pct(abs(C.PL_VS_ISSUE)) + " per cent below its issue price, which indicates that the "
         "market has been repricing that expectation."),
    ]:
        R.bullet(lead, txt)

    R.sub("5.10.11 Overall view")
    R.body(
        "Taken together, the evidence describes a company that has completed the transition "
        "from funded growth to self-funded operation but has not yet shown that the transition "
        "is durable. The positive findings are substantial: revenue compounding at " +
        pct(C.PL_CAGR) + " per cent over three years, a first full-year profit of Rs. " +
        inr(C.PL_PAT[-1]) + " crore after a loss of Rs. " + inr(abs(C.PL_PAT[-2])) + " crore, "
        "and operating cash flow of Rs. " + inr(C.PL_OCF[-1]) + " crore that comfortably "
        "exceeds reported profit. The reservations are equally identifiable: profitability "
        "remains thin in absolute terms, contribution margin is moving in the wrong direction, "
        "part of the most profitable revenue is exposed to regulatory treatment, and the market "
        "multiple rests on a first-year profit small enough to make it unstable. The decisive "
        "question is not whether the company can grow, which it has shown, but whether the "
        "operating leverage of FY2025-26 survives the investment phase of the first quarter of "
        "FY2026-27. **This analysis has been prepared for academic purposes as part of an MMS "
        "project and is not investment advice; no recommendation to buy, hold or sell any "
        "security is made or intended.**")

    # ---------------------------------------------------------------- 5.11
    R.section("5.11 The dealing-desk view of the scrip")
    R.body(
        "The preceding analysis is the view an analyst takes. A dealer looks at the same security "
        "through an entirely different set of attributes, which are set out in Table 5.28.")
    R.caption("Table 5.28: How a dealer would assess the PINELABS scrip")
    R.table(
        ["Attribute", "Position", "Consequence for the desk"],
        [["Exchange and symbol", "NSE: PINELABS; BSE: 544606",
          "Orders routable on either exchange"],
         ["Market capitalisation", "Rs. " + inr(C.PL_MCAP, 0) + " crore, small-capitalisation",
          "Depth thinner than in large-capitalisation names"],
         ["Volatility", "52-week range of " + pct(C.PL_52_RANGE) + " per cent of the low",
          "Market orders avoided; limit orders preferred"],
         ["Price band", "[ADD: verify the applicable band for PINELABS]",
          "Determines the maximum intraday move"],
         ["Surveillance status", "[ADD: verify whether under GSM, ASM or short-term ASM]",
          "Would raise the margin and may restrict intraday trading"],
         ["F&O eligibility", "[ADD: verify whether in the derivatives segment]",
          "If not eligible, no hedging or leverage through futures or options"],
         ["Settlement", "Rolling T+1", "Pay-in obligation on the next business day"],
         ["Typical client interest", "Retail and small high net-worth, post-listing",
          "Frequent small orders rather than block interest"]],
        widths=[2200, 3400, 3400], size=9.5, align=["left", "left", "left"])
    R.source("Source: Exchange data as on 25 September 2026 and the author's assessment; items "
             "marked for completion are " + TBV + " on the date of submission.")
    R.interpretation(
        "The comparison is instructive because the two perspectives disagree about what "
        "matters. The analyst's conclusion in Section 5.10.11 turns on operating leverage and "
        "margin direction, neither of which affects how an order should be entered. The "
        "dealer's conclusion turns on depth, volatility and band, and would be identical "
        "whether the company were profitable or not. A volatility range of " +
        pct(C.PL_52_RANGE) + " per cent of the low in under a year is the single most relevant "
        "fact on the desk. A competent finance professional must be able to hold both views at "
        "once, which is the central learning of this internship.")

    # ---------------------------------------------------------------- 5.12
    R.section("5.12 Skills and learning outcomes mapped to tasks")
    R.caption("Table 5.29: Tasks performed, skills acquired and evidence in this report")
    R.table(
        ["Task performed", "Skill or knowledge gained", "Evidence in this report"],
        [["Pre-market review of news, corporate actions and the ban list",
          "Identification of scrips requiring restricted handling", "Table 5.1; Section 3.19"],
         ["Reading client-wise limits released by the risk system",
          "Understanding of how collateral converts into tradable limit",
          "Section 3.9; Table 5.14"],
         ["Order entry on the exchange terminal under supervision",
          "Accurate use of client code, quantity, price, type and validity",
          "Table 5.4; Table 5.5"],
         ["Observing order routing through the member's CTCL server",
          "Understanding of where pre-trade risk control is applied", "Figure 5.4; Table 5.6"],
         ["Responding to margin-shortfall alerts",
          "Recognition that collateral falls faster than the requirement",
          "Table 5.15"],
         ["Explaining charges to clients",
          "Ability to decompose a contract note into its six components",
          "Table 5.16; Table 5.17"],
         ["Observing futures and option positions on client accounts",
          "Cost-of-carry pricing, mark-to-market settlement, premium decomposition",
          "Tables 5.8, 5.9, 5.10, 5.12"],
         ["Reading company filings for the project",
          "Extraction of segment, margin and cash data from primary filings",
          "Tables 5.20 to 5.25"]],
        widths=[2900, 3000, 3100], size=9.5, align=["left", "left", "left"])
    R.source("Source: Author's record of the internship.")

    # ---------------------------------------------------------------- 5.13
    R.section("5.13 Summary of findings")
    R.caption("Table 5.30: Summary of findings")
    R.table(
        ["Area", "Finding"],
        [["Shape of the dealing function",
          "Of nine tasks in the dealing day, only two involve execution; the function is a "
          "controlled process with an execution step embedded in it."],
         ["Market participation",
          "Demat accounts reached about " + f"{C.DEMAT_TOTAL:.2f}" + " crore by 31 August 2026 "
          "against about " + f"{C.NSE_UNIQUE_INVESTORS:.1f}" + " crore unique investors, "
          "indicating multiple accounts per investor and a rise in order count rather than order "
          "size."],
         ["Pre-trade risk control",
          "Six of the eight checks applied at the member's server relate to client standing "
          "rather than to the order, confirming that the layer exists for credit control."],
         ["Futures pricing and settlement",
          "Fair value of Rs. " + inr(C.FUT_FAIR) + " against spot of Rs. " + inr(C.F_SPOT) +
          "; five daily settlements summing to Rs. " + inr(C.MTM_TOTAL, 0) + " exactly reproduce "
          "the total price change."],
         ["Option behaviour",
          "The illustrative call priced at Rs. " + inr(C.CALL_PRICE) + " loses about " +
          pct((1 - C.DECAY_PRICES[-3] / C.DECAY_PRICES[0]) * 100, 0) + " per cent of its value "
          "in the final five days if the underlying does not move."],
         ["Margin dynamics",
          "A fall of " + pct((C.MTM_ENTRY - C.M_LOSS_PRICE) / C.MTM_ENTRY * 100) + " per cent "
          "converts a surplus of Rs. " + inr(C.M_COLLATERAL - C.M_TOTAL, 0) + " into a shortfall "
          "of Rs. " + inr(C.M_SHORTFALL, 0) + ", because collateral falls faster than the "
          "requirement."],
         ["Transaction costs",
          "A delivery round trip costs Rs. " + inr(C.DEL["total"]) + " on Rs. 1,00,000 each way, "
          "of which Securities Transaction Tax is Rs. " + inr(C.DEL["stt"]) + "; an intraday "
          "trade loses " + pct(C.INT_DRAG) + " per cent of gross profit to charges."],
         ["Pine Labs \u2014 growth",
          "Revenue compounded at " + pct(C.PL_CAGR) + " per cent over three years to Rs. " +
          inr(C.PL_REV[-1]) + " crore in FY2025-26."],
         ["Pine Labs \u2014 profitability",
          "First full-year profit of Rs. " + inr(C.PL_PAT[-1]) + " crore, a swing of Rs. " +
          inr(C.PL_PAT_SWING) + " crore, driven by operating leverage rather than unit "
          "economics."],
         ["Pine Labs \u2014 market position",
          "The share trades " + pct(abs(C.PL_VS_ISSUE)) + " per cent below its issue price at "
          "about " + f"{C.PL_PE_FY26:.0f}" + " times a thin first-year profit."]],
        widths=[2400, 6600], size=9.5, align=["left", "left"])
    R.source("Source: Compiled by the author from Sections 5.2 to 5.11.")
