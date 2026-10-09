"""Every derived number in the report is computed here, never by hand.

Running this module prints the audit trail that feeds the
'Numbers and Sources Audit' deliverable.
"""
import math
from collections import OrderedDict

AUDIT = OrderedDict()


def rec(key, formula, value, label):
    AUDIT[key] = dict(formula=formula, value=value, label=label)
    return value


def inr(x, dp=2):
    """Indian digit grouping."""
    neg = x < 0
    x = abs(x)
    s = f"{x:,.{dp}f}" if dp else f"{x:,.0f}"
    ip, _, fp = s.partition(".")
    ip = ip.replace(",", "")
    if len(ip) > 3:
        head, tail = ip[:-3], ip[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        ip = ",".join(parts + [tail])
    out = ip + ("." + fp if fp else "")
    return ("-" if neg else "") + out


def pct(x, dp=2):
    return f"{x:.{dp}f}"


# ===================================================== 1. market snapshot
NIFTY_CLOSE = 22620.45          # 30 Sep 2026
SENSEX_CLOSE = 72480.29         # 30 Sep 2026
NIFTY_SEP_CHG = -6.03
SENSEX_SEP_CHG = -5.82
DEMAT_CDSL_AUG26 = 19.10        # crore, 31 Aug 2026
DEMAT_NSDL_AUG26 = 4.67         # crore, 31 Aug 2026
DEMAT_TOTAL = rec("demat_total", "19.10 + 4.67",
                  round(DEMAT_CDSL_AUG26 + DEMAT_NSDL_AUG26, 2),
                  "Author's computation")
NSE_UNIQUE_INVESTORS = 13.4     # crore unique PANs, Jul 2026
CDSL_MAR25, CDSL_MAR26 = 15.30, 18.01
CDSL_FY26_ADD = rec("cdsl_add", "18.01 - 15.30", round(CDSL_MAR26 - CDSL_MAR25, 2),
                    "Author's computation")
CDSL_FY26_GROWTH = rec("cdsl_growth", "(18.01 - 15.30) / 15.30 x 100",
                       round((CDSL_MAR26 - CDSL_MAR25) / CDSL_MAR25 * 100, 2),
                       "Author's computation")

# ===================================================== 2. futures worked example
F_SPOT = 1250.00
F_RATE = 0.07
F_DAYS = 30
F_LOT = 1000
FUT_FAIR = rec("fut_fair", "F = S x e^(r x t) = 1250 x e^(0.07 x 30/365)",
               round(F_SPOT * math.exp(F_RATE * F_DAYS / 365), 2), "illustrative")
FUT_BASIS = rec("fut_basis", "1,257.21 - 1,250.00", round(FUT_FAIR - F_SPOT, 2), "illustrative")
FUT_BASIS_PCT = rec("fut_basis_pct", "7.21 / 1250 x 100",
                    round(FUT_BASIS / F_SPOT * 100, 3), "illustrative")

# five-day MTM on a long futures position of one lot
MTM_ENTRY = 1257.00
MTM_PRICES = [1262.00, 1255.50, 1248.00, 1259.25, 1266.00]
MTM_FLOWS, MTM_CUM = [], []
_prev = MTM_ENTRY
_c = 0.0
for p in MTM_PRICES:
    f = (p - _prev) * F_LOT
    _c += f
    MTM_FLOWS.append(round(f, 2))
    MTM_CUM.append(round(_c, 2))
    _prev = p
rec("mtm_flows", "(settlement price - previous price) x lot size", MTM_FLOWS, "illustrative")
MTM_TOTAL = rec("mtm_total", "sum of daily MTM flows", round(sum(MTM_FLOWS), 2), "illustrative")
MTM_CHECK = rec("mtm_check", "(1,266.00 - 1,257.00) x 1,000",
                round((MTM_PRICES[-1] - MTM_ENTRY) * F_LOT, 2), "illustrative")

# ===================================================== 3. option worked example
O_S, O_K, O_T, O_R, O_SIG, O_LOT = 1250.00, 1260.00, 30 / 365, 0.07, 0.28, 1000


def _N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _n(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def bs(S, K, T, r, sig):
    d1 = (math.log(S / K) + (r + sig * sig / 2) * T) / (sig * math.sqrt(T))
    d2 = d1 - sig * math.sqrt(T)
    call = S * _N(d1) - K * math.exp(-r * T) * _N(d2)
    put = K * math.exp(-r * T) * _N(-d2) - S * _N(-d1)
    delta_c = _N(d1)
    delta_p = _N(d1) - 1
    gamma = _n(d1) / (S * sig * math.sqrt(T))
    vega = S * _n(d1) * math.sqrt(T) / 100
    theta_c = (-S * _n(d1) * sig / (2 * math.sqrt(T))
               - r * K * math.exp(-r * T) * _N(d2)) / 365
    rho_c = K * T * math.exp(-r * T) * _N(d2) / 100
    return dict(d1=d1, d2=d2, call=call, put=put, delta_c=delta_c, delta_p=delta_p,
                gamma=gamma, vega=vega, theta_c=theta_c, rho_c=rho_c)


BS = bs(O_S, O_K, O_T, O_R, O_SIG)
for k, v in BS.items():
    rec("bs_" + k, "Black-Scholes-Merton, no dividend", round(v, 6), "Author's computation")
CALL_PRICE = round(BS["call"], 2)
PUT_PRICE = round(BS["put"], 2)
CALL_BE = rec("call_be", "strike + premium = 1,260.00 + " + str(CALL_PRICE),
              round(O_K + CALL_PRICE, 2), "Author's computation")
CALL_COST = rec("call_cost", f"{CALL_PRICE} x 1,000", round(CALL_PRICE * O_LOT, 2), "illustrative")

# premium decomposition at a market premium of Rs. 41.00
MKT_PREM = 41.00
INTRINSIC = rec("intrinsic", "max(S - K, 0) = max(1,250 - 1,260, 0)", max(O_S - O_K, 0), "illustrative")
TIMEVAL = rec("timeval", "premium - intrinsic = 41.00 - 0.00", round(MKT_PREM - INTRINSIC, 2), "illustrative")

# time decay path, constant spot and volatility
DECAY_DAYS = [30, 25, 20, 15, 10, 5, 2, 1]
DECAY_PRICES = [round(bs(O_S, O_K, d / 365, O_R, O_SIG)["call"], 2) for d in DECAY_DAYS]
rec("decay", "Black-Scholes call price, S and sigma held constant", DECAY_PRICES, "Author's computation")

# straddle
STR_CALL = round(bs(O_S, O_S, O_T, O_R, O_SIG)["call"], 2)
STR_PUT = round(bs(O_S, O_S, O_T, O_R, O_SIG)["put"], 2)
STR_TOT = rec("straddle_cost", f"{STR_CALL} + {STR_PUT}", round(STR_CALL + STR_PUT, 2), "Author's computation")
STR_BE_LO = rec("straddle_be_lo", f"1,250.00 - {STR_TOT}", round(O_S - STR_TOT, 2), "Author's computation")
STR_BE_HI = rec("straddle_be_hi", f"1,250.00 + {STR_TOT}", round(O_S + STR_TOT, 2), "Author's computation")

# payoff table for the long call
CALL_PAYOFF = []
for s in [1150, 1200, 1250, 1260, 1280, 1301, 1320, 1360, 1400]:
    intr = max(s - O_K, 0)
    net = (intr - CALL_PRICE) * O_LOT
    CALL_PAYOFF.append((s, round(intr, 2), round(net, 2)))

STRADDLE_PAYOFF = []
for s in [1100, 1150, STR_BE_LO, 1250, STR_BE_HI, 1350, 1400]:
    net = (max(s - O_S, 0) + max(O_S - s, 0) - STR_TOT) * O_LOT
    STRADDLE_PAYOFF.append((round(s, 2), round(net, 2)))

# ===================================================== 4. margin worked example
M_CONTRACT_VALUE = rec("m_cv", "1,257.00 x 1,000", round(MTM_ENTRY * F_LOT, 2), "illustrative")
M_SPAN_PCT, M_EXP_PCT = 9.50, 3.50
M_SPAN = rec("m_span", "12,57,000 x 9.50%", round(M_CONTRACT_VALUE * M_SPAN_PCT / 100, 2), "illustrative")
M_EXP = rec("m_exp", "12,57,000 x 3.50%", round(M_CONTRACT_VALUE * M_EXP_PCT / 100, 2), "illustrative")
M_TOTAL = rec("m_total", "SPAN + exposure", round(M_SPAN + M_EXP, 2), "illustrative")
M_TOTAL_PCT = rec("m_total_pct", "1,63,410 / 12,57,000 x 100",
                  round(M_TOTAL / M_CONTRACT_VALUE * 100, 2), "Author's computation")
M_COLLATERAL = 1_75_000.00
M_LOSS_PRICE = 1_232.00
M_LOSS = rec("m_loss", "(1,232.00 - 1,257.00) x 1,000",
             round((M_LOSS_PRICE - MTM_ENTRY) * F_LOT, 2), "illustrative")
M_AFTER = rec("m_after", "1,75,000 + (-25,000)", round(M_COLLATERAL + M_LOSS, 2), "illustrative")
M_REQ_AFTER = rec("m_req_after", "1,232.00 x 1,000 x 13.00%",
                  round(M_LOSS_PRICE * F_LOT * (M_SPAN_PCT + M_EXP_PCT) / 100, 2), "illustrative")
M_SHORTFALL = rec("m_shortfall", "1,60,160 - 1,50,000",
                  round(M_REQ_AFTER - M_AFTER, 2), "Author's computation")

# ===================================================== 5. charges worked examples
RATE = dict(
    stt_del=0.1, stt_intra_sell=0.025, stt_fut_sell=0.05, stt_opt_sell=0.15,
    stamp_del=0.015, stamp_intra=0.003, stamp_fut=0.002, stamp_opt=0.003,
    nse_eq=0.00297, nse_fut=0.00173, nse_opt=0.03503,
    sebi=0.0001, gst=18.0,
)


def delivery_trade(buy_val, sell_val, brokerage_pct):
    b_brok = buy_val * brokerage_pct / 100
    s_brok = sell_val * brokerage_pct / 100
    brok = b_brok + s_brok
    stt = (buy_val + sell_val) * RATE["stt_del"] / 100
    exch = (buy_val + sell_val) * RATE["nse_eq"] / 100
    sebi = (buy_val + sell_val) * RATE["sebi"] / 100
    stamp = buy_val * RATE["stamp_del"] / 100
    gst = (brok + exch + sebi) * RATE["gst"] / 100
    total = brok + stt + exch + sebi + stamp + gst
    return OrderedDict(brokerage=brok, stt=stt, exchange=exch, sebi=sebi,
                       stamp=stamp, gst=gst, total=total)


DEL_BUY, DEL_SELL, DEL_BROK = 1_00_000.0, 1_00_000.0, 0.05
DEL = delivery_trade(DEL_BUY, DEL_SELL, DEL_BROK)
for k, v in DEL.items():
    rec("del_" + k, "see Section 5.9 build-up", round(v, 2), "Author's computation")
DEL_BREAKEVEN = rec("del_be", "total charges / quantity, 100 shares",
                    round(DEL["total"] / 100, 2), "Author's computation")


def intraday_trade(buy_val, sell_val, brok_flat):
    brok = min(brok_flat, buy_val * 0.05 / 100) + min(brok_flat, sell_val * 0.05 / 100)
    stt = sell_val * RATE["stt_intra_sell"] / 100
    exch = (buy_val + sell_val) * RATE["nse_eq"] / 100
    sebi = (buy_val + sell_val) * RATE["sebi"] / 100
    stamp = buy_val * RATE["stamp_intra"] / 100
    gst = (brok + exch + sebi) * RATE["gst"] / 100
    total = brok + stt + exch + sebi + stamp + gst
    return OrderedDict(brokerage=brok, stt=stt, exchange=exch, sebi=sebi,
                       stamp=stamp, gst=gst, total=total)


INT_BUY, INT_SELL = 5_00_000.0, 5_02_500.0
INT = intraday_trade(INT_BUY, INT_SELL, 20.0)
for k, v in INT.items():
    rec("int_" + k, "see Section 5.9 build-up", round(v, 2), "Author's computation")
INT_GROSS = rec("int_gross", "5,02,500 - 5,00,000", round(INT_SELL - INT_BUY, 2), "illustrative")
INT_NET = rec("int_net", "2,500.00 - total charges", round(INT_GROSS - INT["total"], 2),
              "Author's computation")
INT_DRAG = rec("int_drag", "charges / gross profit x 100",
               round(INT["total"] / INT_GROSS * 100, 2), "Author's computation")

# ===================================================== 6. Pine Labs
PL_YEARS = ["FY23", "FY24", "FY25", "FY26"]
PL_REV = [1597.66, 1769.55, 2274.27, 2710.60]      # restated / audited consolidated
PL_PAT = [-265.15, -341.90, -145.49, 112.50]
PL_DITP = [1152.40, 1276.43, 1603.23, 1836.82]
PL_IAP = [445.26, 493.12, 671.04, 873.77]
PL_TOTINC = [None, None, 2327.10, 2847.20]
PL_AEBITDA_FY26, PL_AEBITDA_FY25 = 559.0, 356.0
PL_CONTRIB_FY26, PL_CONTRIB_FY25 = 75.0, 76.0
PL_OCF = [None, None, 49.70, 395.40]
PL_ASSETS_FY26, PL_ASSETS_FY25 = 13297.0, 10716.0
PL_EQUITY_FY26 = 5895.0
PL_CASH_FY26, PL_CASH_FY25 = 1273.90, 245.20

PL_GROWTH = []
for i in range(1, len(PL_REV)):
    g = (PL_REV[i] - PL_REV[i - 1]) / PL_REV[i - 1] * 100
    PL_GROWTH.append(round(g, 2))
rec("pl_growth", "(current - previous) / previous x 100", PL_GROWTH, "Author's computation")
PL_CAGR = rec("pl_cagr", "((2,710.60 / 1,597.66)^(1/3) - 1) x 100",
              round(((PL_REV[-1] / PL_REV[0]) ** (1 / 3) - 1) * 100, 2), "Author's computation")
PL_NPM_FY26 = rec("pl_npm26", "112.50 / 2,710.60 x 100",
                  round(PL_PAT[-1] / PL_REV[-1] * 100, 2), "Author's computation")
PL_NPM_FY25 = rec("pl_npm25", "-145.49 / 2,274.27 x 100",
                  round(PL_PAT[-2] / PL_REV[-2] * 100, 2), "Author's computation")
PL_PAT_SWING = rec("pl_swing", "112.50 - (-145.49)", round(PL_PAT[-1] - PL_PAT[-2], 2),
                   "Author's computation")
PL_AEB_MARGIN26 = rec("pl_aeb26", "559 / 2,710.60 x 100",
                      round(PL_AEBITDA_FY26 / PL_REV[-1] * 100, 2), "Author's computation")
PL_AEB_MARGIN25 = rec("pl_aeb25", "356 / 2,274.27 x 100",
                      round(PL_AEBITDA_FY25 / PL_REV[-2] * 100, 2), "Author's computation")
PL_AEB_GROWTH = rec("pl_aebg", "(559 - 356) / 356 x 100",
                    round((PL_AEBITDA_FY26 - PL_AEBITDA_FY25) / PL_AEBITDA_FY25 * 100, 2),
                    "Author's computation")
PL_ROE_FY26 = rec("pl_roe", "112.50 / 5,895 x 100",
                  round(PL_PAT[-1] / PL_EQUITY_FY26 * 100, 2), "Author's computation")
PL_ROA_FY26 = rec("pl_roa", "112.50 / 13,297 x 100",
                  round(PL_PAT[-1] / PL_ASSETS_FY26 * 100, 2), "Author's computation")
PL_ASSET_TURN = rec("pl_at", "2,710.60 / ((13,297 + 10,716)/2)",
                    round(PL_REV[-1] / ((PL_ASSETS_FY26 + PL_ASSETS_FY25) / 2), 3),
                    "Author's computation")
PL_OCF_PAT = rec("pl_ocfpat", "395.40 / 112.50",
                 round(PL_OCF[-1] / PL_PAT[-1], 2), "Author's computation")
PL_EQ_RATIO = rec("pl_eqratio", "5,895 / 13,297 x 100",
                  round(PL_EQUITY_FY26 / PL_ASSETS_FY26 * 100, 2), "Author's computation")
PL_DITP_SHARE26 = rec("pl_ditp26", "1,836.82 / 2,710.60 x 100",
                      round(PL_DITP[-1] / PL_REV[-1] * 100, 2), "Author's computation")
PL_IAP_SHARE26 = rec("pl_iap26", "873.77 / 2,710.60 x 100",
                     round(PL_IAP[-1] / PL_REV[-1] * 100, 2), "Author's computation")
PL_DITP_G26 = rec("pl_ditpg", "(1,836.82 - 1,603.23) / 1,603.23 x 100",
                  round((PL_DITP[-1] - PL_DITP[-2]) / PL_DITP[-2] * 100, 2), "Author's computation")
PL_IAP_G26 = rec("pl_iapg", "(873.77 - 671.04) / 671.04 x 100",
                 round((PL_IAP[-1] - PL_IAP[-2]) / PL_IAP[-2] * 100, 2), "Author's computation")

# Q1 FY27
Q_REV27, Q_REV26 = 736.92, 615.91
Q_TOT27, Q_TOT26 = 765.87, 653.08
Q_EXP27, Q_EXP26 = 728.14, 657.86
Q_PBT27, Q_PBT26 = 37.73, -4.84
Q_PAT27, Q_PAT26 = 19.57, 4.79
Q_CONTRIB27, Q_CONTRIB26 = 532.62, 479.78
Q_AEB27, Q_AEB26 = 126.0, 121.0
Q_DITP27, Q_DITP26 = 499.12, 434.37
Q_IAP27, Q_IAP26 = 237.80, 181.54
Q_EPS27, Q_EPS26 = 0.17, 0.05
Q_REV_G = rec("q_revg", "(736.92 - 615.91) / 615.91 x 100",
              round((Q_REV27 - Q_REV26) / Q_REV26 * 100, 2), "Author's computation")
Q_PAT_G = rec("q_patg", "(19.57 - 4.79) / 4.79 x 100",
              round((Q_PAT27 - Q_PAT26) / Q_PAT26 * 100, 2), "Author's computation")
Q_CONTRIB_M27 = rec("q_cm27", "532.62 / 736.92 x 100",
                    round(Q_CONTRIB27 / Q_REV27 * 100, 2), "Author's computation")
Q_CONTRIB_M26 = rec("q_cm26", "479.78 / 615.91 x 100",
                    round(Q_CONTRIB26 / Q_REV26 * 100, 2), "Author's computation")
Q_CM_DROP = rec("q_cmdrop", "72.28 - 77.90",
                round(Q_CONTRIB_M27 - Q_CONTRIB_M26, 2), "Author's computation")
Q_AEB_M27 = rec("q_aebm27", "126 / 736.92 x 100", round(Q_AEB27 / Q_REV27 * 100, 2),
                "Author's computation")
Q_AEB_M26 = rec("q_aebm26", "121 / 615.91 x 100", round(Q_AEB26 / Q_REV26 * 100, 2),
                "Author's computation")
Q_NPM27 = rec("q_npm27", "19.57 / 736.92 x 100", round(Q_PAT27 / Q_REV27 * 100, 2),
              "Author's computation")
Q_DITP_G = rec("q_ditpg", "(499.12 - 434.37) / 434.37 x 100",
               round((Q_DITP27 - Q_DITP26) / Q_DITP26 * 100, 2), "Author's computation")
Q_IAP_G = rec("q_iapg", "(237.80 - 181.54) / 181.54 x 100",
              round((Q_IAP27 - Q_IAP26) / Q_IAP26 * 100, 2), "Author's computation")

# market data as on 25 September 2026
PL_PRICE = 176.57
PL_MCAP = 20389.0
PL_52H, PL_52L = 284.00, 134.73
PL_ISSUE = 221.00
PL_LIST_OPEN = 242.00
PL_BV = 51.06
PL_FV = 1.00
PL_SHARES_POST = 114_82_76_377
PL_VS_ISSUE = rec("pl_vs_issue", "(176.57 - 221.00) / 221.00 x 100",
                  round((PL_PRICE - PL_ISSUE) / PL_ISSUE * 100, 2), "Author's computation")
PL_VS_HIGH = rec("pl_vs_high", "(176.57 - 284.00) / 284.00 x 100",
                 round((PL_PRICE - PL_52H) / PL_52H * 100, 2), "Author's computation")
PL_VS_LOW = rec("pl_vs_low", "(176.57 - 134.73) / 134.73 x 100",
                round((PL_PRICE - PL_52L) / PL_52L * 100, 2), "Author's computation")
PL_LIST_POP = rec("pl_list_pop", "(242.00 - 221.00) / 221.00 x 100",
                  round((PL_LIST_OPEN - PL_ISSUE) / PL_ISSUE * 100, 2), "Author's computation")
PL_EPS_FY26 = rec("pl_eps26", "112.50 crore / 114.83 crore shares",
                  round(PL_PAT[-1] / (PL_SHARES_POST / 1e7), 2), "Author's computation")
PL_PE_FY26 = rec("pl_pe26", "176.57 / 0.98",
                 round(PL_PRICE / (PL_PAT[-1] / (PL_SHARES_POST / 1e7)), 1), "Author's computation")
PL_PB = rec("pl_pb", "176.57 / 51.06", round(PL_PRICE / PL_BV, 2), "Author's computation")
PL_PS = rec("pl_ps", "20,389 / 2,710.60", round(PL_MCAP / PL_REV[-1], 2), "Author's computation")
PL_52_RANGE = rec("pl_range", "(284.00 - 134.73) / 134.73 x 100",
                  round((PL_52H - PL_52L) / PL_52L * 100, 2), "Author's computation")

# shareholding, quarter ended June 2026
PL_SH = [("Promoter and promoter group", 0.00),
         ("Domestic institutional investors", 24.82),
         ("Foreign portfolio investors", 9.49),
         ("Public and others", 65.69)]
PL_SH_TOTAL = rec("pl_sh_total", "0.00 + 24.82 + 9.49 + 65.69",
                  round(sum(v for _, v in PL_SH), 2), "Author's computation")

if __name__ == "__main__":
    for k, v in AUDIT.items():
        print(f"{k:22s} {str(v['value'])[:46]:48s} {v['label']:20s} {v['formula']}")
    print("\ntotal audited quantities:", len(AUDIT))
