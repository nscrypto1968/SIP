#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chapters 3 to 8 and the annexures."""
import compute as C
from compute import inr, pct
import charts as G
from docxlib import add_runs, set_spacing, el
from docx.shared import Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH

TODAY = "9 October 2026"
AS_ON = "25 September 2026"
SRC_NSE = "Source: NSE India, circulars and market-statistics pages; checked 9 October 2026."
SRC_SEBI = "Source: SEBI circulars and master circulars; checked 9 October 2026."
SRC_AUTH = "Source: Author's computation; illustrative figures."
SRC_COMP = "Source: Compiled by the author."
SRC_PL_FY26 = ("Source: Pine Labs Limited, audited consolidated financial results for the year "
               "ended 31 March 2026 (board meeting of 25 May 2026); checked 9 October 2026.")
SRC_PL_Q1 = ("Source: Pine Labs Limited, unaudited consolidated financial results for the quarter "
             "ended 30 June 2026 (board meeting of 28 July 2026); checked 9 October 2026.")
SRC_PL_RHP = ("Source: Pine Labs Limited, Red Herring Prospectus, October 2025, restated "
              "consolidated financial information; checked 9 October 2026.")
TBV = "to be verified"


# ============================================================ CHAPTER 3
def chapter3(R):
    R.chapter("CHAPTER 3", "THEORETICAL FRAMEWORK")

    R.section("3.1 Introduction")
    R.body(
        "This chapter sets out the conceptual and regulatory framework within which an equity "
        "dealer operates, in the order in which the subject matter becomes relevant to a person "
        "joining a dealing desk: the structure of the market, the rules that govern it, the "
        "mechanics of trading and settlement, risk management, derivatives and their margining, "
        "the two trading technologies used on the desk, and the costs and controls attaching to "
        "every transaction. Each regulatory statement carries a source line identifying the "
        "authority relied upon and the date checked; where verification against a primary "
        "source could not be completed, the statement is marked " + TBV + ".")

    R.section("3.2 The financial system and the capital market in India")
    R.body(
        "The **financial system** is the arrangement of markets, institutions, instruments and "
        "services through which savings are transferred to productive use. The **financial markets** component divides into the **money "
        "market**, which deals in instruments of original maturity up to one year, and the "
        "**capital market**, which deals in longer-dated instruments including equity. The "
        "capital market in turn divides into the **primary market**, in which securities are "
        "issued for the first time, and the **secondary market**, in which existing securities "
        "change hands. A stock broker's dealing desk operates almost entirely in the secondary "
        "segment of the capital market, which is why that is the focus of this report.")
    R.body(
        "The distinction matters operationally. In the primary market the broker is a "
        "distribution channel and the applicant's funds are blocked rather than debited; in the "
        "secondary market the broker is an execution intermediary with settlement obligations "
        "to the clearing corporation that arise within a fixed number of days regardless of "
        "whether the client pays. That asymmetry is the origin of the margin framework "
        "described in Sections 3.9 and 3.13.")

    R.section("3.3 Primary market and secondary market")
    R.caption("Table 3.1: Primary market and secondary market compared")
    R.table(
        ["Basis", "Primary market", "Secondary market"],
        [["Nature of transaction", "Issue of new securities", "Transfer of existing securities"],
         ["Recipient of funds", "The issuing company", "The selling investor"],
         ["Effect on company capital", "Capital is raised", "No change in company capital"],
         ["Price determination", "Book-building or fixed price", "Continuous order matching"],
         ["Frequency", "Occasional, issue by issue", "Continuous on every trading day"],
         ["Role of the broker", "Distribution and application support", "Execution of orders"],
         ["Principal document", "Prospectus or offer document", "Contract note"],
         ["Typical settlement", "On allotment and listing", "Rolling settlement cycle"]],
        widths=[2200, 3400, 3400], size=10.5, align=["left", "left", "left"])
    R.source(SRC_COMP)
    R.interpretation(
        "The comparison indicates why a dealer's risk exposure is concentrated in the secondary "
        "market. In the primary market the intermediary's obligation ends when the application "
        "is forwarded, whereas an executed secondary-market trade creates an irrevocable "
        "obligation to deliver securities or funds on a fixed date. A client who does not pay "
        "does not cancel that obligation; the member must settle and then recover. This "
        "explains why the pre-trade limit check in Section 3.16 is applied before an order is "
        "released rather than after it is executed.")

    R.section("3.4 Stock exchanges, indices and market segments")
    R.body(
        "A **stock exchange** is a recognised body that provides the trading platform, the rules "
        "of trading and the framework of surveillance for securities transactions. India's two "
        "principal exchanges are the **National Stock Exchange of India Limited** and **BSE "
        "Limited**. Both operate fully electronic, order-driven markets with anonymous order "
        "matching. Each exchange supports several segments, of which the **capital market "
        "segment**, dealing in equity shares, and the **equity derivatives segment**, dealing in "
        "futures and options on indices and individual securities, are relevant to this report.")
    R.body(
        "An **index** is a statistical measure of the aggregate price movement of a defined "
        "basket of securities, computed on a free-float market-capitalisation basis for the "
        "principal Indian benchmarks. The **Nifty 50** comprises fifty companies on the "
        "National Stock Exchange and the **S&P BSE Sensex** thirty on the BSE. For a dealer, "
        "indices matter in three ways: they are the underlying for the most liquid derivative "
        "contracts, they are the benchmark against which a client judges performance, and index "
        "levels define the market-wide circuit breakers that halt trading after specified "
        "falls.")

    R.section("3.5 Market participants")
    R.caption("Table 3.2: Market participants and their roles")
    R.table(
        ["Participant", "Role in the market", "Point of contact with the dealing desk"],
        [["Retail investor", "Buys and sells securities for personal account in modest size",
          "Places orders by telephone or through the firm's platform"],
         ["Stock broker", "Executes orders as an intermediary and is a member of the exchange",
          "The employer of the dealer"],
         ["Clearing member", "Assumes responsibility for settlement of trades with the clearing "
                             "corporation",
          "Determines the collateral the broker must place"],
         ["Clearing corporation", "Acts as central counterparty, computes obligations and margins",
          "Sets the margin that constrains every client limit"],
         ["Depository and DP", "Holds securities in electronic form and effects transfers",
          "Delivers pay-out and processes pledge instructions"],
         ["Institutional investor", "Foreign portfolio investors and mutual funds investing "
                                    "under registered categories and stated mandates",
          "Rarely a retail desk's client; drives market direction and volume"]],
        widths=[1750, 3700, 3550], size=9.5, align=["left", "left", "left"])
    R.source(SRC_COMP)
    R.interpretation(
        "The table shows that a dealer deals directly with only two of the categories listed "
        "and indirectly with the rest through the constraints they impose. The clearing "
        "corporation is the most consequential participant the dealer never speaks to, because "
        "its margin computation determines the limit the risk-management system will grant, "
        "which determines what the dealer may execute. This chain is worked through numerically "
        "in Section 5.8, where an illustrative position of Rs. " + inr(C.M_CONTRACT_VALUE, 0) +
        " requires margin of Rs. " + inr(C.M_TOTAL, 0) + ", or " + pct(C.M_TOTAL_PCT) +
        " per cent of contract value.")

    R.section("3.6 The regulatory framework")
    R.caption("Table 3.3: Principal statutes and regulations governing stock broking")
    R.table(
        ["Instrument", "Principal subject matter", "Relevance to the dealing desk"],
        [["Securities Contracts (Regulation) Act, 1956",
          "Recognition of stock exchanges and regulation of contracts in securities",
          "Establishes that trades must occur on a recognised exchange"],
         ["SEBI Act, 1992",
          "Constitution and powers of the Securities and Exchange Board of India",
          "Source of the regulator's authority over brokers"],
         ["Depositories Act, 1996",
          "Dematerialisation and electronic transfer of securities",
          "Underlies demat delivery and pledge of collateral"],
         ["SEBI (Stock Brokers) Regulations, 1992",
          "Registration, conduct, records and obligations of stock brokers",
          "Governs client registration, contract notes and records"],
         ["Exchange byelaws, rules and regulations",
          "Trading parameters, member obligations, discipline",
          "Day-to-day operating rules of the terminal"],
         ["Clearing corporation regulations",
          "Margining, settlement, default and close-out",
          "Determines margin rates and settlement timelines"]],
        widths=[2700, 3200, 3100], size=9.5, align=["left", "left", "left"])
    R.source(SRC_SEBI)
    R.interpretation(
        "The structure is hierarchical: statute confers power on the regulator, the regulator "
        "makes regulations and issues circulars, and the exchanges and clearing corporations "
        "issue operating rules consistent with them. For a dealer the binding instruction on "
        "any given day is usually the most recent circular rather than the parent regulation, "
        "and circulars change frequently. The expiry-day change described in Section 3.11 is an "
        "example: the statutory framework was unaltered, but a single circular changed the "
        "operating routine of every derivatives desk in the country.")

    R.section("3.7 The equity trading mechanism")
    R.body(
        "The Indian cash market is an **order-driven market**. Buyers and sellers submit orders "
        "to a central electronic order book and the exchange's matching engine pairs them "
        "according to **price-time priority**: the order offering the best price is matched "
        "first, and among orders at the same price the one entered earlier is matched first. "
        "There is no obligation on any participant to provide a two-way quote in most securities, "
        "which means liquidity is a function of participation rather than of designated market "
        "making. Figure 3.1 illustrates the principle on an order book.")
    R.caption("Figure 3.1: Price-time priority in an order-driven market")
    R.image(G.fig_3_3())
    R.source(SRC_COMP)
    R.body(
        "The trading day is divided into defined sessions. The **pre-open session** collects "
        "orders without matching them, determines a single **equilibrium price** at which the "
        "maximum quantity can trade, and executes at that price; it exists to reduce the "
        "volatility that follows an overnight accumulation of information. The **continuous "
        "trading session** then operates on price-time priority until the close, followed by a "
        "**closing session** in which the closing price is computed. Indicative timings are set "
        "out in Table 3.4.")
    R.caption("Table 3.4: Equity trading sessions and indicative timings")
    R.table(
        ["Session", "Indicative timing", "What happens"],
        [["Pre-open order collection", "09:00 \u2013 09:08",
          "Orders entered, modified and cancelled; no matching"],
         ["Pre-open price determination", "09:08 \u2013 09:12",
          "Equilibrium price computed and orders matched at that price"],
         ["Continuous trading", "09:15 \u2013 15:30",
          "Order-driven matching on price-time priority"],
         ["Closing price computation", "15:30 \u2013 15:40",
          "Weighted average of the last half hour used as the closing price"],
         ["Post-closing session", "15:40 \u2013 16:00",
          "Limited trading at the closing price, where offered"]],
        widths=[2600, 2400, 4000], size=10.5, align=["left", "center", "left"])
    R.source("Source: NSE and BSE trading-hours pages; checked 9 October 2026. Exact session "
             "boundaries are " + TBV + " against the exchange notice in force on the date of "
             "submission.")
    R.body(
        "**Price bands**, also called circuit filters, limit the movement permitted in a security "
        "during a day. Securities in the derivatives segment generally carry a wider operating "
        "range, while others are placed in fixed bands. In addition, **market-wide circuit "
        "breakers** linked to index movement halt trading across the market for specified "
        "durations. Table 3.5 sets out the order types a dealer uses and Table 3.6 the band "
        "categories.")
    R.caption("Table 3.5: Order types, validity conditions and typical use")
    R.table(
        ["Order type", "Definition", "When a dealer uses it"],
        [["Market order", "Executes at the best available price in the book",
          "When certainty of execution matters more than price"],
         ["Limit order", "Executes only at the stated price or better",
          "The default for client orders with a price instruction"],
         ["Stop-loss limit (SL)", "Becomes a limit order once the trigger price is reached",
          "To cap loss on an open position at a defined level"],
         ["Stop-loss market (SL-M)", "Becomes a market order once the trigger is reached",
          "Where exit is required even at an unfavourable price"],
         ["Immediate or cancel (IOC)", "Executes immediately in whole or part; the rest lapses",
          "To avoid leaving a resting order in a fast market"],
         ["Disclosed quantity", "Reveals only part of the total quantity to the market",
          "To reduce market impact on a large order"]],
        widths=[2100, 3400, 3500], size=10.5, align=["left", "left", "left"])
    R.source(SRC_NSE)
    R.caption("Table 3.6: Price-band and circuit-filter categories")
    R.table(
        ["Category", "Indicative band", "Comment"],
        [["Securities in the derivatives segment", "Dynamic operating range",
          "Wider range with a flexing mechanism rather than a hard daily band"],
         ["Other securities \u2014 band 1", "20 per cent", "Most actively traded non-F&O scrips"],
         ["Other securities \u2014 band 2", "10 per cent", "Lower-liquidity scrips"],
         ["Other securities \u2014 band 3", "5 per cent", "Scrips under closer monitoring"],
         ["Surveillance categories", "2 per cent or lower",
          "Scrips placed under additional surveillance measures"],
         ["Market-wide circuit breaker", "10, 15 and 20 per cent index movement",
          "Trading halted market-wide for a specified duration"]],
        widths=[3200, 2300, 3500], size=10.5, align=["left", "center", "left"])
    R.source("Source: NSE and BSE price-band circulars; checked 9 October 2026. Scrip-wise band "
             "assignment changes periodically and is " + TBV + " on the date of submission.")
    R.interpretation(
        "Order type and price band interact in a way that is not obvious until observed live. A "
        "market order entered in a scrip approaching its upper band may execute at the band "
        "itself rather than near the prevailing price, producing an execution the client "
        "regards as an error. The standing instruction on the desk was therefore to avoid "
        "market orders in scrips with a narrow band or thin depth and to use an aggressively "
        "priced limit order instead \u2014 a practical application of the price-time priority "
        "principle shown in Figure 3.1.")

    R.section("3.8 Clearing, settlement and the depositories")
    R.body(
        "**Clearing** is the computation of what each party owes after a trading day; "
        "**settlement** is the exchange of securities and funds. Both are performed by a "
        "**clearing corporation** acting as **central counterparty**, which interposes itself "
        "between buyer and seller so neither is exposed to the other's default. Obligations are "
        "netted at clearing-member level and settled on a **rolling settlement** basis. The "
        "standard cycle for equities is **T+1**, with an optional same-day **T+0** facility for "
        "a specified list of securities. The sequence is shown in Figure 3.2 and the timeline "
        "in Table 3.7.")
    R.caption("Figure 3.2: Clearing and settlement flow")
    R.image(G.fig_3_4())
    R.source(SRC_COMP)
    R.caption("Table 3.7: Rolling settlement timeline under the T+1 cycle")
    R.table(
        ["Stage", "Day", "Action"],
        [["Trade", "T", "Order matched on the exchange; contract note issued to the client"],
         ["Securities pay-in", "T+1", "Selling member delivers securities to the clearing "
                                      "corporation through the depository"],
         ["Funds pay-in", "T+1", "Buying member transfers funds through the clearing bank"],
         ["Pay-out", "T+1", "Securities and funds released to the entitled members and credited "
                            "to client accounts"],
         ["Shortage handling", "T+1 onward", "Undelivered securities met through auction or "
                                             "close-out at a prescribed rate"]],
        widths=[2100, 1300, 5600], size=10.5, align=["left", "center", "left"])
    R.source("Source: Clearing corporation settlement-cycle documents and SEBI circulars; checked "
             "9 October 2026. The scope of the optional T+0 facility is " + TBV + ".")
    R.interpretation(
        "The compression of the cycle to T+1 has had a direct effect on the dealing desk. Under "
        "a longer cycle a client had time to arrange funds after executing a purchase; under "
        "T+1 the funds must effectively be in place at the time of the trade, which is why "
        "upfront margin collection became unavoidable rather than merely prudent. The "
        "consequence observed on the desk was a shift of effort from post-trade collection to "
        "pre-trade verification, the same shift visible in Table 2.3.")

    R.section("3.9 Risk management in the cash market")
    R.body(
        "Margin in the cash market covers the risk that a client fails to meet an obligation "
        "between trade and settlement; the components appear in Table 3.8. The **value-at-risk "
        "margin** is a statistical estimate of the loss not exceeded on a given proportion of "
        "days, scrip by scrip; the **extreme loss margin** covers losses outside that interval; "
        "and **mark-to-market margin** covers the notional loss on an unsettled position at the "
        "close. Under the upfront margin framework the first two must be collected before the "
        "trade, and compliance is tested against snapshots taken at random during the day, "
        "which is the **peak margin** concept.")
    R.caption("Table 3.8: Margins applicable in the cash market")
    R.table(
        ["Margin", "What it covers", "Timing of collection"],
        [["Value-at-risk (VaR) margin", "Statistical estimate of a one-day adverse price move",
          "Upfront, before the order is released"],
         ["Extreme loss margin (ELM)", "Losses beyond the VaR confidence interval",
          "Upfront, together with VaR margin"],
         ["Mark-to-market (MTM) margin", "Notional loss on an unsettled position at the close",
          "Collected after the close for the next day"],
         ["Delivery margin", "Risk on positions moving into the delivery cycle",
          "Levied in stages approaching settlement"],
         ["Peak margin obligation", "Highest intraday margin requirement across random snapshots",
          "Tested intraday; shortfall attracts penalty"]],
        widths=[2500, 3400, 3100], size=10.5, align=["left", "left", "left"])
    R.source("Source: SEBI margin-framework circulars and clearing corporation documents; checked "
             "9 October 2026. Current rates are scrip-specific and " + TBV + ".")
    R.body(
        "Client collateral may be furnished in cash or in securities. Securities are furnished "
        "through the **margin pledge** mechanism, under which they remain in the client's own "
        "demat account and a pledge is created in favour of the broker, who may **re-pledge** "
        "them to the clearing member and clearing corporation. This replaced the earlier "
        "practice of transferring client securities into a broker-controlled account. For the "
        "dealer the effect is that a client who holds shares but has not pledged them has no "
        "additional limit, however large the holding.")
    R.interpretation(
        "The upfront margin regime converted a credit decision into a systems decision. A "
        "dealer can no longer extend informal accommodation to a reliable client, because the "
        "limit is computed by the risk system from collateral actually pledged and the order is "
        "rejected at entry if it is insufficient. This is the largest practical difference "
        "between the desk described in older study material and the desk observed during this "
        "internship, and it is quantified in Section 5.8, where a price fall of Rs. 25.00 on "
        "one lot converts an adequately margined position into a shortfall of Rs. " +
        inr(C.M_SHORTFALL, 0) + ".")

    R.section("3.10 Derivatives: concept, history and types")
    R.body(
        "A **derivative** is a contract whose value is derived from an underlying asset, rate "
        "or index. Derivatives serve three economic functions: **hedging**, the transfer of an "
        "unwanted price risk; **speculation**, the assumption of price risk in search of "
        "profit; and **arbitrage**, the exploitation of price differences between related "
        "instruments, which keeps prices consistent. Exchange-traded derivatives in India began "
        "with index futures in 2000, followed by index options, stock options and stock futures "
        "over the next two years.")
    R.caption("Table 3.9: Types of derivative contracts")
    R.table(
        ["Type", "Obligation of the buyer", "Obligation of the seller", "Traded in India"],
        [["Forward", "To buy at a fixed price on a future date",
          "To sell at that price", "Over the counter only"],
         ["Future", "To buy at a fixed price on expiry, settled daily",
          "To sell at that price, settled daily", "On exchange, index and stock"],
         ["Call option", "Right, not obligation, to buy at the strike",
          "Obligation to sell if exercised", "On exchange, index and stock"],
         ["Put option", "Right, not obligation, to sell at the strike",
          "Obligation to buy if exercised", "On exchange, index and stock"]],
        widths=[1500, 2700, 2500, 2300], size=9.5, align=["left", "left", "left", "left"])
    R.source(SRC_COMP)
    R.interpretation(
        "The asymmetry between futures and options is the point a new dealer must internalise "
        "first. In a futures contract both parties carry an obligation and both post margin; in "
        "an option only the seller carries an obligation, so only the seller posts margin while "
        "the buyer pays a premium and can lose no more than that premium. Clients frequently "
        "assume an option purchase carries the same margin consequence as a futures position. "
        "Section 5.7 shows a call premium outlay of Rs. " + inr(C.CALL_COST, 0) + " for one "
        "lot, against margin of Rs. " + inr(C.M_TOTAL, 0) + " for a comparable futures "
        "position in Section 5.8.")

    R.section("3.11 Futures: specification, pricing and settlement")
    R.body(
        "A **futures contract** is a standardised agreement to buy or sell a specified quantity "
        "of an underlying at a price agreed today for settlement on a specified future date. "
        "Standardisation extends to the **lot size**, the **expiry date**, the **tick size** "
        "and the settlement method. Lot sizes are revised periodically and the minimum contract "
        "value has been raised in recent years, so any lot size quoted must carry the contract "
        "month and the date checked.")
    R.body(
        "Expiry conventions changed materially with effect from 1 September 2025. Following a "
        "regulatory direction limiting equity-derivative expiries to two days of the week, the "
        "National Stock Exchange moved its weekly and monthly equity-derivative expiries to "
        "**Tuesday** and the BSE to **Thursday**. In addition, each exchange retains only one "
        "weekly benchmark index option contract, and all other equity-derivative contracts carry "
        "a minimum tenor of one month expiring in the last week of the month on the exchange's "
        "chosen day. Any description of a universal Thursday expiry is therefore obsolete.")
    R.body(
        "The theoretical price of a futures contract is given by the **cost-of-carry** "
        "relationship, under which the futures price equals the spot price compounded at the "
        "financing rate over the remaining life of the contract, adjusted for any income "
        "forgone.")
    R.formula("F = S \u00d7 e^(r \u00d7 t)")
    R.body(
        "where F is the futures price, S the spot price, r the continuously compounded "
        "risk-free rate and t the time to expiry in years. The difference between futures and "
        "spot is the **basis**, which converges to zero at expiry; the worked computation "
        "appears in Section 5.6. Futures are settled daily by **mark to market**, so the "
        "accumulated exposure never exceeds one day's movement. Figure 3.3 shows the payoff "
        "profile.")
    R.caption("Figure 3.3: Payoff of long and short futures positions")
    R.image(G.fig_3_5())
    R.source(SRC_AUTH)
    R.caption("Table 3.10: Illustrative equity-futures contract specification")
    R.table(
        ["Parameter", "Illustrative specification"],
        [["Underlying", "An illustrative listed equity security"],
         ["Contract size (lot)", "1,000 units"],
         ["Tick size", "Rs. 0.05"],
         ["Expiry day", "Last Tuesday of the contract month on the NSE; Thursday on the BSE"],
         ["Settlement basis", "Daily mark to market; final settlement in cash on expiry"],
         ["Final settlement price", "Closing price of the underlying on the expiry day"],
         ["Daily price limit", "Operating range with a flexing mechanism"]],
        widths=[3000, 6000], size=10.5, align=["left", "left"])
    R.source("Source: NSE contract specification pages; checked 9 October 2026. Lot size shown is "
             "illustrative; the actual lot size for any contract is " + TBV + ".")

    R.section("3.12 Options: payoff, premium and the Greeks")
    R.body(
        "An **option** confers a right without an obligation. A **call option** gives its "
        "holder the right to buy the underlying at the **strike price**; a **put option** gives "
        "the right to sell. The buyer pays a **premium** to the seller, or writer, and that "
        "premium is the buyer's maximum loss. **Moneyness** describes the relationship between "
        "the underlying price and the strike: a call is **in the money** when the underlying "
        "exceeds the strike, **at the money** when they are equal and **out of the money** "
        "below it, with the reverse applying to puts.")
    R.formula("Premium = Intrinsic value + Time value")
    R.formula("Intrinsic value of a call = max(S \u2212 K, 0);  of a put = max(K \u2212 S, 0)")
    R.caption("Table 3.11: Option moneyness, intrinsic value and time value")
    R.table(
        ["Condition", "Call option", "Put option", "Intrinsic value"],
        [["Underlying above strike", "In the money", "Out of the money", "Positive for the call"],
         ["Underlying equal to strike", "At the money", "At the money", "Nil for both"],
         ["Underlying below strike", "Out of the money", "In the money", "Positive for the put"],
         ["At expiry", "Premium equals intrinsic value", "Premium equals intrinsic value",
          "Time value is nil"]],
        widths=[2300, 2300, 2300, 2100], size=9.5, align=["left", "left", "left", "left"])
    R.source(SRC_COMP)
    R.caption("Figure 3.4: Payoff of a long call and a long put")
    R.image(G.fig_3_6())
    R.source(SRC_AUTH)
    R.body(
        "The theoretical value of a European option is given by the **Black-Scholes-Merton "
        "model**, which expresses the option price as a function of the underlying price, the "
        "strike, the time to expiry, the risk-free rate and the volatility of the underlying.")
    R.formula("C = S \u00d7 N(d\u2081) \u2212 K \u00d7 e^(\u2212rt) \u00d7 N(d\u2082)")
    R.formula("d\u2081 = [ln(S/K) + (r + \u03c3\u00b2/2)t] \u00f7 (\u03c3\u221at);   "
              "d\u2082 = d\u2081 \u2212 \u03c3\u221at")
    R.body(
        "The partial derivatives of the option price with respect to its inputs are called the "
        "**Greeks**. **Delta** measures the change in option value for a unit change in the "
        "underlying; **gamma** measures the rate of change of delta; **theta** measures the loss "
        "of value from the passage of one day; **vega** measures sensitivity to a one-point "
        "change in volatility; and **rho** measures sensitivity to interest rates. A worked "
        "computation for an illustrative contract appears in Section 5.7.")

    R.section("3.13 Margining in the futures and options segment")
    R.body(
        "Margin in the derivatives segment is computed by a portfolio-based system commonly "
        "referred to as **SPAN**, which revalues the client's portfolio under scenarios "
        "combining movements in the underlying price and in volatility and takes the worst "
        "outcome as the requirement. To this is added an **exposure margin** on contract value "
        "and, for option buyers, the **premium margin**. Spread positions across contract "
        "months attract a **calendar spread** concession because the legs offset. Table 3.12 "
        "summarises the components.")
    R.caption("Table 3.12: Components of margin in the derivatives segment")
    R.table(
        ["Component", "Basis of computation", "Who pays it"],
        [["SPAN or initial margin", "Worst-case portfolio loss across prescribed scenarios",
          "Futures buyers and sellers; option sellers"],
         ["Exposure margin", "A percentage of notional contract value",
          "Futures buyers and sellers; option sellers"],
         ["Premium margin", "Premium payable on purchased options until pay-in",
          "Option buyers, until the premium is settled"],
         ["Calendar spread benefit", "Concession for offsetting positions in different months",
          "Reduces the requirement for spread positions"],
         ["Delivery margin", "Levied on stock derivatives approaching physical settlement",
          "Both parties in the expiry week"]],
        widths=[2300, 3700, 3000], size=10.5, align=["left", "left", "left"])
    R.source("Source: Clearing corporation margin documents; checked 9 October 2026. Scenario "
             "parameters and exposure-margin percentages are " + TBV + ".")
    R.interpretation(
        "Two features matter on the desk. First, because SPAN is portfolio-based, adding a "
        "hedging leg can reduce total margin rather than increase it, which is "
        "counter-intuitive to clients who assume more positions require more money. Second, "
        "margin is recomputed continuously, so a position adequately margined at entry can fall "
        "into shortfall purely because the underlying moved. Section 5.8 demonstrates this: the "
        "requirement falls from Rs. " + inr(C.M_TOTAL, 0) + " to Rs. " + inr(C.M_REQ_AFTER, 0) +
        " while available collateral falls faster, from Rs. " + inr(C.M_COLLATERAL, 0) +
        " to Rs. " + inr(C.M_AFTER, 0) + ".")

    R.section("3.14 Trading strategies observed on a dealing desk")
    R.body(
        "A dealing desk does not devise strategies, but it must recognise them, because the "
        "margin consequence and the order sequence differ by strategy. The principal structures "
        "encountered are summarised in Table 3.13.")
    R.caption("Table 3.13: Common strategies and their payoff characteristics")
    R.table(
        ["Strategy", "Construction", "Maximum profit", "Maximum loss", "View"],
        [["Protective put", "Long stock plus long put", "Unlimited", "Limited to put strike",
          "Bullish with protection"],
         ["Covered call", "Long stock plus short call", "Limited to strike plus premium",
          "Substantial if stock falls", "Mildly bullish"],
         ["Long straddle", "Long call and long put at the same strike", "Unlimited",
          "Total premium paid", "Large move, direction unknown"],
         ["Bull call spread", "Long lower-strike call, short higher-strike call",
          "Difference in strikes less net premium", "Net premium paid", "Moderately bullish"],
         ["Bear put spread", "Long higher-strike put, short lower-strike put",
          "Difference in strikes less net premium", "Net premium paid", "Moderately bearish"]],
        widths=[1700, 2500, 1800, 1600, 1400], size=9.5,
        align=["left", "left", "left", "left", "left"])
    R.source(SRC_COMP)

    R.section("3.15 The NEAT PLUS trading terminal")
    R.body(
        "**NEAT**, the National Exchange for Automated Trading system, is the front-end "
        "application supplied by the National Stock Exchange to its trading members for order "
        "entry in the capital-market segment; **NEAT PLUS** is the multi-segment variant "
        "allowing a single terminal to access more than one segment. The terminal is "
        "keyboard-driven, with function keys mapped to the most frequent operations, and is "
        "organised around a small number of windows.")
    R.caption("Table 3.14: Principal screens of the terminal and their use")
    R.table(
        ["Screen", "Content", "Use by the dealer"],
        [["Market watch", "User-selected list of securities with best bid, best ask and last "
                          "traded price",
          "Continuous monitoring of the scrips in which clients are active"],
         ["Market by price", "Aggregated depth at each price level on both sides",
          "Assessment of liquidity before entering a large order"],
         ["Order entry", "Entry of client code, quantity, price, order type and validity",
          "The principal working screen during market hours"],
         ["Outstanding order book", "All orders entered and not yet executed or cancelled",
          "Modification and cancellation of resting orders"],
         ["Trade book", "All executions of the day with price, quantity and time",
          "Confirmation of fills and end-of-day verification"],
         ["Limits and margin", "Available limit and utilisation against collateral",
          "Pre-entry check that the order will not be rejected"]],
        widths=[1900, 3500, 3600], size=9.5, align=["left", "left", "left"])
    R.source("Source: NSE trading-system documentation and the intern's observation; checked "
             "9 October 2026. [ADD: confirm which of these screens were used, and list the "
             "specific function keys and shortcuts used on the desk.]")
    R.interpretation(
        "The organisation of the terminal reflects the sequence of a dealer's decision rather "
        "than the structure of the data. Verification of the security, assessment of depth, "
        "confirmation of limit, entry and confirmation each has its own window, and a competent "
        "dealer moves between them by keystroke. The learning curve observed during the "
        "internship was concentrated almost entirely in this motor skill rather than in "
        "conceptual understanding, consistent with the challenge recorded in Section 1.5.")

    R.section("3.16 The Computer-to-Computer Link facility")
    R.body(
        "**CTCL**, the Computer-to-Computer Link, is an arrangement under which a trading member "
        "connects its own front-end application and server to the exchange trading system, "
        "instead of using only the exchange-supplied terminal. The member's server receives "
        "orders from dealer workstations, applies the member's own pre-trade risk controls and "
        "then transmits the order to the exchange. The architecture is shown in Figure 3.5.")
    R.caption("Figure 3.5: Computer-to-Computer Link architecture")
    R.image(G.fig_3_7())
    R.source(SRC_COMP)
    R.body(
        "The facility is subject to a defined regulatory discipline. The software used must be "
        "of a version approved by the exchange; every terminal must be registered with a unique "
        "**terminal identifier** mapped to a location; every operator must hold a unique "
        "**user identifier** and the prescribed certification; and the member must maintain a "
        "complete **audit trail** of every order, modification and cancellation, identifying "
        "the user and terminal that originated it. Pre-trade risk controls must be applied at "
        "the member's server and cannot be bypassed by the operator. Where orders are generated "
        "by software, the separate framework governing algorithmic trading applies.")
    R.caption("Table 3.15: NEAT PLUS and CTCL compared")
    R.table(
        ["Basis", "Exchange terminal (NEAT PLUS)", "Member CTCL facility"],
        [["Software owner", "The exchange", "The trading member or its vendor"],
         ["Point of risk control", "Exchange-level validations only",
          "Member's own pre-trade risk layer in addition"],
         ["Customisation", "Limited to user settings", "Substantial; screens and controls vary"],
         ["User identification", "Exchange-allotted user ID",
          "Member-allotted user ID mapped to a registered terminal ID"],
         ["Audit trail", "Maintained at the exchange", "Maintained by the member and inspected"],
         ["Approval requirement", "Terminal allotment by the exchange",
          "Software version approval plus terminal registration"]],
        widths=[1900, 3400, 3700], size=9.5, align=["left", "left", "left"])
    R.source("Source: Exchange CTCL circulars and member compliance documents; checked "
             "9 October 2026. [ADD: name of the CTCL software used by the firm.]")
    R.interpretation(
        "The essential difference is the location of the risk control rather than the "
        "appearance of the screen. On an exchange terminal the validations are those the "
        "exchange applies to every member; on a CTCL terminal the member interposes its own, "
        "invariably tighter, limits. An order may therefore be rejected by the firm's own "
        "server without ever reaching the exchange. Recognising which layer has rejected an "
        "order is a practical diagnostic skill, because the remedy differs: an internal "
        "rejection requires a limit discussion with risk management, while an exchange "
        "rejection usually indicates a parameter error such as a price outside the band.")

    R.section("3.17 The back office and the risk-management system")
    R.body(
        "The **back office** maintains the records that convert executions into enforceable "
        "entitlements. Every client is identified by a **unique client code** registered with "
        "the exchange, and an order entered against an incorrect code is a reportable "
        "irregularity rather than a clerical error. At the close the back office receives the "
        "exchange trade file, computes client-wise obligations, generates **contract notes** "
        "within the prescribed time, posts entries to the **client ledger** and reconciles "
        "holdings against depository records. Table 3.16 lists the principal records.")
    R.caption("Table 3.16: Records maintained against each client")
    R.table(
        ["Record", "Content", "Why the dealer needs it"],
        [["Client registration file", "KYC documents, agreements, risk-disclosure acknowledgement",
          "Confirms the client may trade in the segment"],
         ["Unique client code mapping", "Exchange-registered code against the client",
          "Every order must carry a valid code"],
         ["Client ledger", "Running record of funds due to and from the client",
          "Determines free balance available as limit"],
         ["Holding statement", "Securities held, pledged and free",
          "Determines deliverable quantity and collateral"],
         ["Margin statement", "Daily margin required, collected and shortfall",
          "Basis of the shortfall alert and square-off decision"],
         ["Contract note", "Trade-wise price, quantity, brokerage and statutory charges",
          "The client's primary evidence of the transaction"]],
        widths=[2200, 3500, 3300], size=9.5, align=["left", "left", "left"])
    R.source(SRC_COMP)

    R.section("3.18 Transaction costs and statutory charges")
    R.body(
        "Six distinct charges attach to an executed equity transaction, only one of which "
        "accrues to the broker. **Brokerage** is the member's own fee; **exchange transaction "
        "charges** are levied on turnover; the **Securities Transaction Tax** is a central levy "
        "on specified securities transactions; **stamp duty** is a state levy collected on the "
        "buy side; the **SEBI turnover fee** is a small regulatory charge on traded value; and "
        "**goods and services tax** is charged at eighteen per cent on the sum of brokerage, "
        "exchange charges and the regulator's fee, but not on the statutory levies. Depository "
        "charges apply additionally on delivery-based sales. The rates are set out in Table "
        "3.17 and applied in Section 5.9.")
    R.caption("Table 3.17: Statutory charges and transaction costs")
    R.table(
        ["Charge", "Equity delivery", "Equity intraday", "Equity futures", "Equity options"],
        [["Securities Transaction Tax",
          "0.10% buy and sell", "0.025% sell only", "0.05% sell only",
          "0.15% on premium, sell"],
         ["Stamp duty (buy side only)", "0.015%", "0.003%", "0.002%", "0.003%"],
         ["NSE transaction charges", "0.00297%", "0.00297%", "0.00173%", "0.03503% on premium"],
         ["SEBI turnover fee", "0.0001%", "0.0001%", "0.0001%", "0.0001%"],
         ["Goods and services tax", "18% on brokerage, exchange and SEBI charges",
          "18% on the same base", "18% on the same base", "18% on the same base"],
         ["Brokerage", "As per the firm's tariff", "As per the firm's tariff",
          "As per the firm's tariff", "As per the firm's tariff"],
         ["Depository charges", "On delivery-based sale", "Not applicable", "Not applicable",
          "Not applicable"]],
        widths=[2100, 1800, 1700, 1700, 1700], size=9.5,
        align=["left", "center", "center", "center", "center"])
    R.source("Source: Rates compiled from the Securities Transaction Tax schedule as revised with "
             "effect from 1 April 2026, state stamp-duty notifications, NSE transaction-charge "
             "circulars and SEBI fee regulations; checked 9 October 2026. Rates are revised "
             "periodically and must be reconfirmed on the date of submission.")
    R.interpretation(
        "The composition of the charge is as important as its size. Because the Securities "
        "Transaction Tax falls on turnover rather than profit, it is payable on a losing trade "
        "as readily as on a winning one, and because goods and services tax applies to "
        "brokerage but not to the statutory levies, a reduction in brokerage reduces the tax "
        "base as well as the fee. On the delivery round trip in Section 5.9 the tax alone "
        "accounts for Rs. " + inr(C.DEL["stt"]) + " of the Rs. " + inr(C.DEL["total"]) +
        " total, or " + pct(C.DEL["stt"] / C.DEL["total"] * 100) + " per cent, which indicates "
        "that negotiating brokerage addresses only a minority of the cost.")

    R.section("3.19 Investor protection, compliance and surveillance")
    R.body(
        "Client onboarding requires **know your customer** verification, execution of the "
        "prescribed agreements and acknowledgement of the risk-disclosure document, after which "
        "the client is allotted a unique client code. Orders must be placed only against a "
        "verified instruction, which is why telephone instructions are recorded. "
        "**Surveillance** measures are applied by the exchanges to securities exhibiting "
        "unusual price or volume behaviour, as summarised in Table 3.18.")
    R.caption("Table 3.18: Surveillance frameworks and their effect on trading")
    R.table(
        ["Framework", "Purpose", "Effect on the dealing desk"],
        [["Graded Surveillance Measure (GSM)",
          "Applied to securities with weak fundamentals and sharp price rises",
          "Periodic call auction, higher margin, restricted trading"],
         ["Additional Surveillance Measure (ASM)",
          "Applied to securities with unusual volatility or volume",
          "Elevated margin, often 100 per cent of value"],
         ["Ban period in derivatives",
          "Applied when market-wide open interest exceeds a threshold",
          "Only position-reducing orders permitted"],
         ["Trade-for-trade segment", "Compulsory delivery-based settlement",
          "No intraday squaring-off permitted"],
         ["Investor grievance redressal",
          "SCORES and the exchange investor-services cell",
          "Complaints routed away from the desk to compliance"]],
        widths=[2600, 3400, 3000], size=9.5, align=["left", "left", "left"])
    R.source("Source: Exchange surveillance circulars; checked 9 October 2026. The scrip-wise "
             "list under each framework changes daily and is " + TBV + ".")

    R.section("3.20 Digital payments and financial technology in the capital market")
    R.body(
        "This section provides the bridge to the company analysed in Chapter 5. The capital "
        "market now depends on digital payment infrastructure at several points: client funds "
        "move by electronic transfer and increasingly through the unified payments interface; "
        "public-issue applications rely on a blocked-amount mechanism using the same rails; and "
        "the compression of the settlement cycle to T+1 would not have been feasible without "
        "near-real-time funds movement. A dealer experiences this directly, because a transfer "
        "that clears within minutes releases limit within minutes.")
    R.body(
        "The companies that build this infrastructure have themselves become listed securities, "
        "and are therefore both the plumbing of the market and objects traded within it. **Pine "
        "Labs Limited**, a merchant-commerce and payments platform that listed on both "
        "principal exchanges on 14 November 2025, is analysed in Section 5.10 for that reason.")


# ============================================================ CHAPTER 4
def chapter4(R):
    R.chapter("CHAPTER 4", "RESEARCH METHODOLOGY")

    R.section("4.1 Research design")
    R.body(
        "The study adopts a **descriptive research design** combined with **work-based "
        "learning**, or participant observation. A descriptive design is appropriate because "
        "the objective is to document and explain an existing process rather than to test a "
        "causal hypothesis. The work-based element arises because the author was placed within "
        "the function studied and the observations were generated by performing the work rather "
        "than by interviewing those who perform it. The design has a recognised strength and "
        "weakness: it produces detail an external observer could not obtain, and a single-site "
        "account that cannot be generalised without further evidence.")

    R.section("4.2 Data collection")
    R.body(
        "**Primary data** consists of the author's own structured observation of the dealing desk "
        "during the internship, including the sequence of the working day, the screens and "
        "functions used, the categories of client instruction received, the nature of the risk "
        "alerts generated and the reconciliation procedure followed at the close. No client "
        "record, internal limit or firm financial figure was copied, and no screenshot is "
        "reproduced unless it has been anonymised. [ADD: state whether masked terminal "
        "screenshots are attached; if yes, insert them in Sections 5.4 and 5.5 with the "
        "prescribed caption and source line.]")
    R.body(
        "**Secondary data** consists of publicly available documents: circulars of the "
        "Securities and Exchange Board of India; circulars, contract specifications and "
        "statistics of the National Stock Exchange and BSE Limited; settlement and margin "
        "documentation of the clearing corporations; depository statistics; and, for the "
        "company analysis, the financial results, offer document, shareholding-pattern filings "
        "and investor material of Pine Labs Limited together with exchange price data. "
        "Aggregator websites were used only to locate primary documents and are not relied "
        "upon as the source of any figure.")

    R.section("4.3 Period of the study")
    R.body(
        "The internship was undertaken from [ADD: internship start date] to [ADD: internship end "
        "date]. Market and regulatory facts are stated as they stood on " + TODAY + ", which is "
        "the date of writing. Market price data for Pine Labs Limited is stated as on " + AS_ON +
        ". The financial period covered in the company analysis is the four financial years "
        "FY2022-23 to FY2025-26 together with the quarter ended 30 June 2026.")

    R.section("4.4 Tools and techniques")
    for lead, txt in [
        ("Trend analysis",
         "year-on-year growth and compound annual growth rate applied to the revenue and profit "
         "series of the company analysed, to separate the level of performance from its "
         "direction."),
        ("Ratio analysis",
         "profitability, return, efficiency and capital-structure ratios, each shown with the "
         "formula applied and the computed value, so that the derivation is auditable."),
        ("Option pricing",
         "the Black-Scholes-Merton model used to value an illustrative contract and to compute "
         "its delta, gamma, theta, vega and rho."),
        ("Cost-of-carry and mark-to-market computation",
         "derivation of a theoretical futures price and simulation of a five-day daily "
         "settlement sequence, with a cross-check that daily flows sum to the total price "
         "change."),
        ("Charge computation",
         "line-by-line application of the current statutory rate card to illustrative delivery "
         "and intraday transactions."),
    ]:
        R.bullet(lead, txt)
    R.body(
        "All arithmetic in this report was performed in code rather than by hand, and the "
        "computations were cross-checked where an independent check exists. The mark-to-market "
        "sequence in Section 5.6, for example, was verified by confirming that the sum of the "
        "five daily flows, Rs. " + inr(C.MTM_TOTAL, 0) + ", equals the product of the total price "
        "change and the lot size, Rs. " + inr(C.MTM_CHECK, 0) + ".")

    R.section("4.5 Mapping of objectives to methods")
    R.caption("Table 4.1: Mapping of objectives to methods and report sections")
    R.table(
        ["Objective", "Method used", "Section"],
        [["To study the Indian equity market",
          "Review of statute, circulars and exchange documents; observation of the trading day",
          "3.2 \u2013 3.9, 5.2, 5.3"],
         ["To study the futures and options market",
          "Cost-of-carry computation, mark-to-market simulation, Black-Scholes valuation, payoff "
          "analysis", "3.10 \u2013 3.14, 5.6, 5.7"],
         ["To examine the NEAT PLUS terminal",
          "Direct use under supervision; documentation of screens and order states",
          "3.15, 5.4"],
         ["To examine the CTCL facility",
          "Observation of routing and risk checks; review of exchange requirements",
          "3.16, 5.5"],
         ["To study risk management",
          "SPAN and exposure illustration; shortfall and square-off scenario",
          "3.9, 3.13, 5.8"],
         ["To analyse Pine Labs Limited",
          "Trend analysis, ratio analysis, shareholding and peer comparison from filings",
          "5.10, 5.11"]],
        widths=[2500, 4500, 2000], size=9.5, align=["left", "left", "center"])
    R.source(SRC_COMP)

    R.section("4.6 Data coverage and ethical safeguards")
    R.body(
        "Four safeguards were adopted. First, **no client-identifying information** appears in "
        "this report; where an example requires a client, the designation Client A or Client B "
        "is used. Second, **no internal figure of the firm** is disclosed; all monetary "
        "examples are constructed by the author and labelled illustrative. Third, **no fact "
        "about the firm has been invented**: where a particular was not available from the "
        "firm's own documents, a marked placeholder has been left rather than an assumed value. "
        "Fourth, **every regulatory statement carries a source and a date of checking**, and "
        "where verification could not be completed the statement is marked " + TBV +
        " rather than presented as established.")
