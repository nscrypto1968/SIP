#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chapters 6 to 8 and Annexures A, B and C."""
import compute as C
from compute import inr, pct
from part2 import SRC_COMP, TBV, TODAY, AS_ON


def chapter6(R):
    R.chapter("CHAPTER 6", "CONCLUSION AND SUGGESTIONS")

    R.section("6.1 Conclusion")
    R.sub("6.1.1 The equity market and the dealing function")
    for lead, txt in [
        ("The dealing role is predominantly procedural",
         "of the nine tasks identified in Table 5.1, seven are preparation, control or "
         "verification and only two involve execution, which indicates that competence is "
         "demonstrated by the absence of error rather than by the presence of skill in "
         "trading."),
        ("Discretion is narrow and bounded",
         "a dealer's judgement operates only between acceptance and execution, because "
         "validation precedes the first and irrevocability follows the second."),
        ("Credit control has displaced credit judgement",
         "the upfront margin framework computes the limit from pledged collateral, so a dealer "
         "can no longer accommodate a reliable client informally, as described in Section 3.9."),
    ]:
        R.bullet(lead, txt)

    R.sub("6.1.2 Futures, options and risk")
    for lead, txt in [
        ("Daily settlement redistributes rather than alters the result",
         "the five daily flows in Table 5.9 sum to Rs. " + inr(C.MTM_TOTAL, 0) + ", exactly "
         "equal to the total price change multiplied by the lot size, but the client must fund "
         "the adverse days in cash along the way."),
        ("Collateral falls faster than the margin requirement",
         "a price fall of " + pct((C.MTM_ENTRY - C.M_LOSS_PRICE) / C.MTM_ENTRY * 100) +
         " per cent converted a surplus of Rs. " + inr(C.M_COLLATERAL - C.M_TOTAL, 0) +
         " into a shortfall of Rs. " + inr(C.M_SHORTFALL, 0) + " in the illustration at "
         "Table 5.15."),
        ("Time decay is non-linear and dominates the final week",
         "the illustrative call lost about " +
         pct((1 - C.DECAY_PRICES[-3] / C.DECAY_PRICES[0]) * 100, 0) + " per cent of its value in "
         "the final five days with the underlying unchanged."),
    ]:
        R.bullet(lead, txt)

    R.sub("6.1.3 Trading terminals and technology")
    for lead, txt in [
        ("The terminal is organised around the decision, not the data",
         "verification, depth assessment, limit confirmation, entry and confirmation each occupy "
         "a separate window, and competence is largely a motor skill acquired by practice."),
        ("The CTCL layer is a credit control before it is a convenience",
         "six of the eight pre-trade checks in Table 5.6 test the client's standing rather than "
         "the order's parameters."),
        ("Diagnosing the source of a rejection is a distinct skill",
         "an internal rejection is negotiable through risk management while an exchange "
         "rejection is not, and the remedy differs accordingly."),
    ]:
        R.bullet(lead, txt)

    R.sub("6.1.4 Findings on Pine Labs Limited")
    for lead, txt in [
        ("The turnaround is real and cash-backed",
         "revenue of Rs. " + inr(C.PL_REV[-1]) + " crore in FY2025-26 with a profit of Rs. " +
         inr(C.PL_PAT[-1]) + " crore, a swing of Rs. " + inr(C.PL_PAT_SWING) + " crore, and "
         "operating cash flow at " + f"{C.PL_OCF_PAT:.2f}" + " times profit."),
        ("The improvement came from operating leverage, not unit economics",
         "adjusted EBITDA grew " + pct(C.PL_AEB_GROWTH) + " per cent on revenue growth of " +
         pct(C.PL_GROWTH[-1]) + " per cent while contribution margin edged down."),
        ("The margin direction is the open question",
         "contribution margin fell again in Q1 FY2026-27 to " + pct(C.Q_CONTRIB_M27) +
         " per cent and adjusted EBITDA margin to " + pct(C.Q_AEB_M27) + " per cent."),
    ]:
        R.bullet(lead, txt)

    R.body(
        "Overall, the internship shows that the competence expected of an equity dealer is not "
        "the ability to form a view on a security but the ability to execute an instruction "
        "correctly within a dense framework of limits, timings and statutory obligations, and "
        "to recognise immediately when that framework has been breached. Chapter 5 shows the "
        "complementary point: the attributes that determine how a security should be traded "
        "\u2014 depth, volatility, band, segment eligibility \u2014 are almost entirely "
        "disjoint from those that determine whether it is a sound business. The principal value "
        "of a dealing-desk internship to a student of finance is that it supplies the frame the "
        "classroom does not.")

    R.section("6.2 Suggestions")
    for lead, txt in [
        ("Formalise a written pre-market checklist for the desk",
         "the most frequent escalations observed arose from an omission in the pre-market block "
         "rather than from an error during trading; a signed checklist covering corporate "
         "actions, the ban list, surveillance changes and limit confirmation would address the "
         "largest single source of avoidable problems."),
        ("Introduce a structured terminal-simulation period for new dealers",
         "because the learning curve is a motor skill rather than a conceptual one, supervised "
         "practice on a simulated order book before live access would shorten the period during "
         "which a new entrant is a net risk."),
        ("Provide clients with a pre-trade cost illustration",
         "Table 5.16 shows that a delivery round trip requires a move of Rs. " +
         inr(C.DEL_BREAKEVEN) + " per share merely to break even; a standard one-page "
         "illustration would reduce the disputes that arise when a client sees the contract note "
         "for the first time."),
        ("Issue a plain-language note on margin asymmetry to derivative clients",
         "the finding that collateral falls faster than the requirement is counter-intuitive and "
         "is the root of most shortfall disputes; the scenario in Table 5.15 could be reproduced "
         "as a client-facing example."),
    ]:
        R.bullet(lead, txt)

    R.section("6.3 Learning outcomes")
    R.body(
        "The internship produced four durable outcomes. First, an operational understanding of "
        "the Indian secondary market that extends from a client instruction to a settled demat "
        "credit, including the points at which the process can fail. Second, the ability to "
        "compute, rather than describe, the quantities that govern a dealing decision: a "
        "futures fair value, a mark-to-market obligation, an option premium and its "
        "sensitivities, a margin requirement and the ladder of statutory charges. Third, "
        "familiarity with the two trading technologies in use on an Indian dealing desk. "
        "Fourth, the discipline of sourcing: every regulatory statement carries the authority "
        "relied upon and the date checked, and every figure is labelled as reported, computed "
        "or illustrative.")


def chapter7(R):
    R.chapter("CHAPTER 7", "LIMITATIONS OF THE STUDY")
    R.body("The findings of this report should be read subject to the following limitations.")
    for lead, txt in [
        ("Short duration of the internship",
         "the period of attachment covered only a small number of trading cycles and did not "
         "include a full expiry cycle in every contract month, a quarterly results season or a "
         "period of market-wide circuit-breaker activity, so observations about behaviour under "
         "stress are necessarily limited."),
        ("Limited segments handled",
         "the work was confined to the cash and equity-derivatives segments of a retail-facing "
         "desk; the currency, commodity and debt segments, institutional dealing and "
         "algorithmic order flow were not observed and no conclusion is offered about them."),
        ("Confidentiality constraints on firm data",
         "no client record, internal limit, brokerage tariff or financial figure of Rosy Blue "
         "Securities Pvt. Ltd. could be recorded or reproduced, which means that the "
         "quantitative work in Chapter 5 rests on constructed examples rather than on the firm's "
         "actual order flow."),
        ("Illustrative nature of the worked examples",
         "the prices, lot size, volatility, interest rate and margin percentages used in "
         "Sections 5.6 to 5.9 are assumptions chosen to demonstrate a mechanism and must not be "
         "read as market observations or as parameters applied by any clearing corporation."),
        ("Regulatory change after the date of writing",
         "expiry conventions, margin rules, lot sizes, price bands, surveillance categories and "
         "charge rates are revised frequently; every such statement in this report is dated "
         "9 October 2026 and several are expressly marked " + TBV + ", and all should be "
         "reconfirmed against the exchange and regulator websites before the report is "
         "submitted."),
        ("Reliance on secondary data for the company analysis",
         "the analysis of Pine Labs Limited rests on the company's own published filings and on "
         "exchange market data; no management access, site visit or independent verification of "
         "the underlying records was possible, and the peer figures in Table 5.26 could not be "
         "verified within the time available and are marked for completion."),
        ("No forecasting or recommendation",
         "the study does not project future revenue, earnings or share price, does not apply a "
         "discounted cash-flow or other intrinsic valuation, and makes no recommendation to buy, "
         "hold or sell any security; the analysis is academic in purpose."),
    ]:
        R.bullet(lead, txt)


def chapter8(R):
    R.chapter("CHAPTER 8", "BIBLIOGRAPHY")

    R.section("8.1 Books and study material")
    for t in [
        "Hull, J. C., *Options, Futures and Other Derivatives*, Pearson.",
        "Bhole, L. M. and Mahakud, J., *Financial Institutions and Markets*, McGraw Hill "
        "Education.",
        "Pathak, B. V., *The Indian Financial System: Markets, Institutions and Services*, "
        "Pearson.",
        "NSE Academy certification workbooks on the capital market and the derivatives market "
        "(current editions).",
        "[ADD: any additional textbook or study material prescribed by the institute.]",
    ]:
        R.bullet(t)

    R.section("8.2 Regulations, circulars and rule books")
    for t in [
        "Securities and Exchange Board of India Act, 1992.",
        "SEBI (Stock Brokers) Regulations, 1992, as amended.",
        "SEBI circular dated 26 May 2025 on the standardisation of expiry days for equity "
        "derivative contracts; accessed 9 October 2026.",
        "NSE and BSE circulars on the shift of equity-derivative expiry to Tuesday and Thursday "
        "respectively with effect from 1 September 2025; accessed 9 October 2026.",
        "Exchange circulars on Computer-to-Computer Link software approval, terminal "
        "registration and user identification; accessed 9 October 2026.",
        "Exchange circulars on transaction charges for the capital market and equity-derivatives "
        "segments; accessed 9 October 2026.",
        "Finance Act provisions prescribing Securities Transaction Tax rates applicable from "
        "1 April 2026; accessed 9 October 2026.",
    ]:
        R.bullet(t)

    R.section("8.3 Websites and filings")
    for t in [
        "National Stock Exchange of India Limited, www.nseindia.com; accessed 9 October 2026.",
        "Securities and Exchange Board of India, www.sebi.gov.in; accessed 9 October 2026.",
        "Central Depository Services (India) Limited, www.cdslindia.com; depository statistics "
        "as on 31 August 2026; accessed 9 October 2026.",
        "National Securities Depository Limited, www.nsdl.co.in; depository statistics as on "
        "31 August 2026; accessed 9 October 2026.",
        "Pine Labs Limited, audited consolidated financial results for the year ended 31 March "
        "2026, approved by the board on 25 May 2026; accessed 9 October 2026.",
        "Pine Labs Limited, unaudited consolidated financial results for the quarter ended "
        "30 June 2026, approved by the board on 28 July 2026; accessed 9 October 2026.",
        "Pine Labs Limited, Red Herring Prospectus, October 2025, restated consolidated "
        "financial information; accessed 9 October 2026.",
        "Rosy Blue Securities Pvt. Ltd., [ADD: website address, if any]; accessed "
        "[ADD: date of access].",
    ]:
        R.bullet(t)


# ============================================================ ANNEXURES
GLOSSARY = [
    ("Arbitrage", "Simultaneous purchase and sale of related instruments to profit from a price difference."),
    ("Assignment", "Allocation of an exercise obligation to an option seller."),
    ("Audit trail", "Time-stamped record of every order, modification and cancellation, identifying user and terminal."),
    ("Basis", "Difference between the futures price and the spot price of the underlying."),
    ("Circuit filter", "Price band beyond which a security may not trade during a session."),
    ("Clearing corporation", "Entity that acts as central counterparty and computes settlement obligations."),
    ("Contract note", "Document issued by a broker recording the price, quantity and charges on a trade."),
    ("Cost of carry", "Financing and holding cost reflected in the difference between futures and spot prices."),
    ("CTCL", "Computer-to-Computer Link; a member's own front end and server connected to the exchange."),
    ("Delta", "Change in an option's value for a unit change in the price of the underlying."),
    ("Depository participant", "Agent of a depository through which an investor holds a demat account."),
    ("ELM", "Extreme loss margin; margin covering losses beyond the value-at-risk confidence interval."),
    ("Expiry", "Date on which a derivative contract ceases to exist and is finally settled."),
    ("Exposure margin", "Margin levied as a percentage of notional contract value."),
    ("Gamma", "Rate of change of an option's delta for a unit change in the underlying."),
    ("GSM", "Graded Surveillance Measure; framework restricting trading in specified securities."),
    ("Intrinsic value", "The in-the-money amount of an option, never less than zero."),
    ("Lot size", "Number of units of the underlying in one derivative contract."),
    ("Margin pledge", "Creation of a charge over client securities held in the client's own demat account."),
    ("Moneyness", "Relationship between the price of the underlying and the strike price of an option."),
    ("MTM", "Mark to market; daily revaluation of an open position and settlement of the change."),
    ("NEAT PLUS", "Multi-segment variant of the exchange-supplied trading front end."),
    ("Open interest", "Total number of derivative contracts outstanding and not yet closed or settled."),
    ("Peak margin", "Highest intraday margin requirement measured across random snapshots."),
    ("Premium", "Amount paid by an option buyer to an option seller."),
    ("Price-time priority", "Matching rule under which the best price, and then the earliest order, is matched first."),
    ("Rolling settlement", "Settlement of each day's trades a fixed number of business days later."),
    ("SPAN", "Portfolio-based margining system that revalues positions across prescribed scenarios."),
    ("Square-off", "Closing of an open position by an equal and opposite transaction."),
    ("Strike price", "Price at which an option holder may buy or sell the underlying."),
    ("Theta", "Loss of option value attributable to the passage of one day."),
    ("Time value", "The part of an option premium in excess of its intrinsic value."),
    ("UCC", "Unique client code; the exchange-registered identifier for a client."),
    ("VaR margin", "Value-at-risk margin; statistical estimate of a one-day adverse price move."),
    ("Vega", "Change in an option's value for a one-point change in volatility."),
]

FORMULAE = [
    ("Futures fair value", "F = S x e^(r x t)"),
    ("Basis", "Basis = F - S"),
    ("Daily mark to market", "MTM = (today's settlement price - previous settlement price) x lot size"),
    ("Intrinsic value, call", "max(S - K, 0)"),
    ("Premium decomposition", "Premium = intrinsic value + time value"),
    ("Long call payoff at expiry", "(max(S - K, 0) - premium) x lot size"),
    ("Long call break-even", "Break-even = K + premium"),
    ("Long straddle break-even", "Lower = K - total premium; Upper = K + total premium"),
    ("Black-Scholes call", "C = S x N(d1) - K x e^(-rt) x N(d2)"),
    ("d1 and d2", "d1 = [ln(S/K) + (r + sigma^2/2)t] / (sigma x sqrt(t)); d2 = d1 - sigma x sqrt(t)"),
    ("Delta of a call", "Delta = N(d1)"),
    ("Gamma", "Gamma = n(d1) / (S x sigma x sqrt(t))"),
    ("Theta of a call, per day", "Theta = [-S x n(d1) x sigma / (2 sqrt(t)) - r K e^(-rt) N(d2)] / 365"),
    ("Vega, per one point", "Vega = S x n(d1) x sqrt(t) / 100"),
    ("Total derivatives margin", "Margin = SPAN margin + exposure margin"),
    ("Margin shortfall", "Shortfall = margin required - collateral available after MTM debit"),
    ("Goods and services tax", "GST = 18% x (brokerage + exchange transaction charges + SEBI fee)"),
    ("Total charges", "Total = brokerage + STT + exchange charges + SEBI fee + stamp duty + GST"),
    ("Break-even move per share", "Break-even = total charges / quantity"),
    ("Year-on-year growth", "Growth = (current - previous) / previous x 100"),
    ("Compound annual growth rate", "CAGR = ((ending value / beginning value)^(1/n) - 1) x 100"),
    ("Net profit margin", "NPM = profit after tax / revenue from operations x 100"),
    ("Adjusted EBITDA margin", "Margin = adjusted EBITDA / revenue from operations x 100"),
    ("Contribution margin", "Margin = contribution profit / revenue from operations x 100"),
    ("Return on equity", "ROE = profit after tax / total equity x 100"),
    ("Return on assets", "ROA = profit after tax / total assets x 100"),
    ("Asset turnover", "Asset turnover = revenue / average total assets"),
    ("Cash conversion", "Cash conversion = operating cash flow / profit after tax"),
    ("Earnings per share", "EPS = profit after tax / number of equity shares outstanding"),
    ("Price to earnings", "P/E = market price per share / earnings per share"),
    ("Price to book", "P/B = market price per share / book value per share"),
]

ABBREVIATIONS = [
    ("ASM", "Additional Surveillance Measure"),
    ("BSE", "BSE Limited, formerly the Bombay Stock Exchange"),
    ("CAGR", "Compound annual growth rate"),
    ("CDSL", "Central Depository Services (India) Limited"),
    ("CTCL", "Computer-to-Computer Link"),
    ("DII", "Domestic institutional investor"),
    ("DITP", "Digital Infrastructure and Transaction Platform"),
    ("DP", "Depository participant"),
    ("EBITDA", "Earnings before interest, tax, depreciation and amortisation"),
    ("ELM", "Extreme loss margin"),
    ("EPS", "Earnings per share"),
    ("F&O", "Futures and options"),
    ("FPI", "Foreign portfolio investor"),
    ("FY", "Financial year"),
    ("GSM", "Graded Surveillance Measure"),
    ("GST", "Goods and services tax"),
    ("GTV", "Gross transaction value"),
    ("IAP", "Issuing and Acquiring Platform"),
    ("IPO", "Initial public offering"),
    ("ISIN", "International Securities Identification Number"),
    ("KYC", "Know your customer"),
    ("LODR", "Listing Obligations and Disclosure Requirements"),
    ("MTM", "Mark to market"),
    ("NEAT", "National Exchange for Automated Trading"),
    ("NPCI", "National Payments Corporation of India"),
    ("NSDL", "National Securities Depository Limited"),
    ("NSE", "National Stock Exchange of India Limited"),
    ("OFS", "Offer for sale"),
    ("P/B", "Price to book"),
    ("P/E", "Price to earnings"),
    ("PAT", "Profit after tax"),
    ("RBI", "Reserve Bank of India"),
    ("RHP", "Red Herring Prospectus"),
    ("RMS", "Risk management system"),
    ("ROA", "Return on assets"),
    ("ROE", "Return on equity"),
    ("SCORES", "SEBI Complaints Redress System"),
    ("SEBI", "Securities and Exchange Board of India"),
    ("SPAN", "Standard Portfolio Analysis of Risk"),
    ("STT", "Securities Transaction Tax"),
    ("SWOT", "Strengths, weaknesses, opportunities and threats"),
    ("UCC", "Unique client code"),
    ("UPI", "Unified Payments Interface"),
    ("VaR", "Value at risk"),
]


def annexures(R):
    R.chapter("ANNEXURE A", "GLOSSARY OF TERMS")
    R.caption("Table A.1: Glossary of terms used in this report")
    R.table(["Term", "Meaning"], [[a, b] for a, b in sorted(GLOSSARY)],
            widths=[2400, 6600], size=10, align=["left", "left"])
    R.source(SRC_COMP)

    R.chapter("ANNEXURE B", "FORMULA SHEET")
    R.caption("Table B.1: Formulae applied in this report")
    R.table(["Quantity", "Formula as applied"], [[a, b] for a, b in FORMULAE],
            widths=[2900, 6100], size=10, align=["left", "left"])
    R.source(SRC_COMP)

    R.chapter("ANNEXURE C", "LIST OF ABBREVIATIONS")
    R.caption("Table C.1: Abbreviations used in this report")
    R.table(["Abbreviation", "Expansion"], [[a, b] for a, b in sorted(ABBREVIATIONS)],
            widths=[2200, 6800], size=10, align=["left", "left"])
    R.source(SRC_COMP)
