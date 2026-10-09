# Numbers-and-sources audit — Rosy Blue Securities Black Book

Document: `Rosy_Blue_Securities_Black_Book.docx` · Compiled 9 October 2026 · All derived
quantities produced by `build/compute.py`; rerun it to reproduce every figure below.

## A. Source authorities relied upon

| # | Fact used in the report | Authority relied upon | Date checked |
|---|---|---|---|
| 1 | Nifty 50 22,620.45 and Sensex 72,480.29 on 30 Sep 2026; monthly falls of 6.03% and 5.82% | Exchange index data for the month ended 30 September 2026 | 9 Oct 2026 |
| 2 | Demat accounts 19.10 cr (CDSL) + 4.67 cr (NSDL) = 23.77 cr as on 31 Aug 2026 | CDSL and NSDL published depository statistics | 9 Oct 2026 |
| 3 | NSE unique registered investors 13.4 cr (unique PANs), July 2026 | NSE investor statistics | 9 Oct 2026 |
| 4 | CDSL accounts 15.30 cr (31 Mar 2025) to 18.01 cr (31 Mar 2026) | CDSL disclosures | 9 Oct 2026 |
| 5 | NSE equity derivatives expire Tuesday, BSE Thursday, w.e.f. 1 Sep 2025 | SEBI circular dated 26 May 2025 on standardisation of expiry days; NSE and BSE implementing circulars | 9 Oct 2026 |
| 6 | STT: delivery 0.10% both sides; intraday 0.025% sell; futures 0.05% sell; options 0.15% on premium | Securities Transaction Tax schedule as revised with effect from 1 April 2026 | 9 Oct 2026 |
| 7 | Stamp duty (buy side): delivery 0.015%, intraday 0.003%, futures 0.002%, options 0.003% | State stamp-duty notifications under the uniform rate structure | 9 Oct 2026 |
| 8 | NSE transaction charges: cash 0.00297%, futures 0.00173%, options 0.03503% on premium | NSE transaction-charge circulars | 9 Oct 2026 |
| 9 | SEBI turnover fee 0.0001% (Rs. 10 per crore); GST 18% on brokerage + exchange + SEBI fee | SEBI fee regulations; GST law | 9 Oct 2026 |
| 10 | T+1 rolling settlement standard, optional T+0 for a specified list | SEBI circulars and clearing corporation settlement documents | 9 Oct 2026 |
| 11 | Pine Labs listed 14 Nov 2025; NSE PINELABS, BSE 544606, ISIN INE15B701018, FV Re 1 | Exchange listing records and offer documents | 9 Oct 2026 |
| 12 | IPO Rs. 3,899.91 cr (fresh Rs. 2,080 cr + OFS Rs. 1,819.91 cr); band Rs. 210-221; issued Rs. 221; opened Rs. 242 | Pine Labs RHP and exchange listing data | 9 Oct 2026 |
| 13 | FY26 revenue Rs. 2,710.60 cr; PAT Rs. 112.50 cr; total income Rs. 2,847.10 cr; adj. EBITDA Rs. 559 cr; OCF Rs. 395.40 cr; assets Rs. 13,297 cr; equity Rs. 5,895 cr | Pine Labs audited consolidated results for the year ended 31 March 2026 (board approval 25 May 2026) | 9 Oct 2026 |
| 14 | FY23-FY25 revenue and PAT (Rs. 1,597.66 / 1,769.55 / 2,274.27 cr; losses 265.15 / 341.90 / 145.49 cr) | Pine Labs RHP, restated consolidated financial information | 9 Oct 2026 |
| 15 | Q1 FY27 revenue Rs. 736.92 cr, PAT Rs. 19.57 cr, EPS Rs. 0.17 | Pine Labs unaudited consolidated results for the quarter ended 30 June 2026 (board approval 28 July 2026) | 9 Oct 2026 |
| 16 | Segment revenue DITP / IAP, FY23-FY26 and Q1 | Pine Labs segment disclosures; IAP derived as revenue less DITP (Author's computation) | 9 Oct 2026 |
| 17 | Shareholding June 2026: promoter 0.00%, DII 24.82%, FII 9.49%, public 65.69% | Pine Labs shareholding-pattern filing, quarter ended 30 June 2026 | 9 Oct 2026 |
| 18 | Price Rs. 176.57, market cap Rs. 20,389 cr, 52-week Rs. 134.73-284.00, book value Rs. 51.06, as on 25 Sep 2026 | Exchange market data | 9 Oct 2026 |

## B. Label convention

* **as printed in the source** - reproduced unchanged from the cited filing or circular.
* **Author's computation** - derived in `build/compute.py` from figures labelled above.
* **illustrative** - an assumption constructed by the author to demonstrate a mechanism; not a market observation.

## C. Every derived quantity, with its formula

| Key | Formula as computed | Value | Label |
|---|---|---|---|
| `demat_total` | 19.10 + 4.67 | 23.77 | Author's computation |
| `cdsl_add` | 18.01 - 15.30 | 2.71 | Author's computation |
| `cdsl_growth` | (18.01 - 15.30) / 15.30 x 100 | 17.71 | Author's computation |
| `fut_fair` | F = S x e^(r x t) = 1250 x e^(0.07 x 30/365) | 1257.21 | illustrative |
| `fut_basis` | 1,257.21 - 1,250.00 | 7.21 | illustrative |
| `fut_basis_pct` | 7.21 / 1250 x 100 | 0.577 | illustrative |
| `mtm_flows` | (settlement price - previous price) x lot size | [5000.0, -6500.0, -7500.0, 11250.0, 6750.0] | illustrative |
| `mtm_total` | sum of daily MTM flows | 9000.0 | illustrative |
| `mtm_check` | (1,266.00 - 1,257.00) x 1,000 | 9000.0 | illustrative |
| `bs_d1` | Black-Scholes-Merton, no dividend | 0.012547 | Author's computation |
| `bs_d2` | Black-Scholes-Merton, no dividend | -0.067727 | Author's computation |
| `bs_call` | Black-Scholes-Merton, no dividend | 38.693729 | Author's computation |
| `bs_put` | Black-Scholes-Merton, no dividend | 41.465229 | Author's computation |
| `bs_delta_c` | Black-Scholes-Merton, no dividend | 0.505005 | Author's computation |
| `bs_delta_p` | Black-Scholes-Merton, no dividend | -0.494995 | Author's computation |
| `bs_gamma` | Black-Scholes-Merton, no dividend | 0.003976 | Author's computation |
| `bs_vega` | Black-Scholes-Merton, no dividend | 1.429552 | Author's computation |
| `bs_theta_c` | Black-Scholes-Merton, no dividend | -0.780767 | Author's computation |
| `bs_rho_c` | Black-Scholes-Merton, no dividend | 0.487038 | Author's computation |
| `call_be` | strike + premium = 1,260.00 + 38.69 | 1298.69 | Author's computation |
| `call_cost` | 38.69 x 1,000 | 38690.0 | illustrative |
| `intrinsic` | max(S - K, 0) = max(1,250 - 1,260, 0) | 0 | illustrative |
| `timeval` | premium - intrinsic = 41.00 - 0.00 | 41.0 | illustrative |
| `decay` | Black-Scholes call price, S and sigma held constant | [38.69, 34.64, 30.22, 25.3, 19.58, 12.38, 6.3, 3.47] | Author's computation |
| `straddle_cost` | 43.59 + 36.42 | 80.01 | Author's computation |
| `straddle_be_lo` | 1,250.00 - 80.01 | 1169.99 | Author's computation |
| `straddle_be_hi` | 1,250.00 + 80.01 | 1330.01 | Author's computation |
| `m_cv` | 1,257.00 x 1,000 | 1257000.0 | illustrative |
| `m_span` | 12,57,000 x 9.50% | 119415.0 | illustrative |
| `m_exp` | 12,57,000 x 3.50% | 43995.0 | illustrative |
| `m_total` | SPAN + exposure | 163410.0 | illustrative |
| `m_total_pct` | 1,63,410 / 12,57,000 x 100 | 13.0 | Author's computation |
| `m_loss` | (1,232.00 - 1,257.00) x 1,000 | -25000.0 | illustrative |
| `m_after` | 1,75,000 + (-25,000) | 150000.0 | illustrative |
| `m_req_after` | 1,232.00 x 1,000 x 13.00% | 160160.0 | illustrative |
| `m_shortfall` | 1,60,160 - 1,50,000 | 10160.0 | Author's computation |
| `del_brokerage` | see Section 5.9 build-up | 100.0 | Author's computation |
| `del_stt` | see Section 5.9 build-up | 200.0 | Author's computation |
| `del_exchange` | see Section 5.9 build-up | 5.94 | Author's computation |
| `del_sebi` | see Section 5.9 build-up | 0.2 | Author's computation |
| `del_stamp` | see Section 5.9 build-up | 15.0 | Author's computation |
| `del_gst` | see Section 5.9 build-up | 19.11 | Author's computation |
| `del_total` | see Section 5.9 build-up | 340.25 | Author's computation |
| `del_be` | total charges / quantity, 100 shares | 3.4 | Author's computation |
| `int_brokerage` | see Section 5.9 build-up | 40.0 | Author's computation |
| `int_stt` | see Section 5.9 build-up | 125.62 | Author's computation |
| `int_exchange` | see Section 5.9 build-up | 29.77 | Author's computation |
| `int_sebi` | see Section 5.9 build-up | 1.0 | Author's computation |
| `int_stamp` | see Section 5.9 build-up | 15.0 | Author's computation |
| `int_gst` | see Section 5.9 build-up | 12.74 | Author's computation |
| `int_total` | see Section 5.9 build-up | 224.14 | Author's computation |
| `int_gross` | 5,02,500 - 5,00,000 | 2500.0 | illustrative |
| `int_net` | 2,500.00 - total charges | 2275.86 | Author's computation |
| `int_drag` | charges / gross profit x 100 | 8.97 | Author's computation |
| `pl_growth` | (current - previous) / previous x 100 | [10.76, 28.52, 19.19] | Author's computation |
| `pl_cagr` | ((2,710.60 / 1,597.66)^(1/3) - 1) x 100 | 19.27 | Author's computation |
| `pl_npm26` | 112.50 / 2,710.60 x 100 | 4.15 | Author's computation |
| `pl_npm25` | -145.49 / 2,274.27 x 100 | -6.4 | Author's computation |
| `pl_swing` | 112.50 - (-145.49) | 257.99 | Author's computation |
| `pl_aeb26` | 559 / 2,710.60 x 100 | 20.62 | Author's computation |
| `pl_aeb25` | 356 / 2,274.27 x 100 | 15.65 | Author's computation |
| `pl_aebg` | (559 - 356) / 356 x 100 | 57.02 | Author's computation |
| `pl_roe` | 112.50 / 5,895 x 100 | 1.91 | Author's computation |
| `pl_roa` | 112.50 / 13,297 x 100 | 0.85 | Author's computation |
| `pl_at` | 2,710.60 / ((13,297 + 10,716)/2) | 0.226 | Author's computation |
| `pl_ocfpat` | 395.40 / 112.50 | 3.51 | Author's computation |
| `pl_eqratio` | 5,895 / 13,297 x 100 | 44.33 | Author's computation |
| `pl_ditp26` | 1,836.82 / 2,710.60 x 100 | 67.76 | Author's computation |
| `pl_iap26` | 873.77 / 2,710.60 x 100 | 32.24 | Author's computation |
| `pl_ditpg` | (1,836.82 - 1,603.23) / 1,603.23 x 100 | 14.57 | Author's computation |
| `pl_iapg` | (873.77 - 671.04) / 671.04 x 100 | 30.21 | Author's computation |
| `q_revg` | (736.92 - 615.91) / 615.91 x 100 | 19.65 | Author's computation |
| `q_patg` | (19.57 - 4.79) / 4.79 x 100 | 308.56 | Author's computation |
| `q_cm27` | 532.62 / 736.92 x 100 | 72.28 | Author's computation |
| `q_cm26` | 479.78 / 615.91 x 100 | 77.9 | Author's computation |
| `q_cmdrop` | 72.28 - 77.90 | -5.62 | Author's computation |
| `q_aebm27` | 126 / 736.92 x 100 | 17.1 | Author's computation |
| `q_aebm26` | 121 / 615.91 x 100 | 19.65 | Author's computation |
| `q_npm27` | 19.57 / 736.92 x 100 | 2.66 | Author's computation |
| `q_ditpg` | (499.12 - 434.37) / 434.37 x 100 | 14.91 | Author's computation |
| `q_iapg` | (237.80 - 181.54) / 181.54 x 100 | 30.99 | Author's computation |
| `pl_vs_issue` | (176.57 - 221.00) / 221.00 x 100 | -20.1 | Author's computation |
| `pl_vs_high` | (176.57 - 284.00) / 284.00 x 100 | -37.83 | Author's computation |
| `pl_vs_low` | (176.57 - 134.73) / 134.73 x 100 | 31.05 | Author's computation |
| `pl_list_pop` | (242.00 - 221.00) / 221.00 x 100 | 9.5 | Author's computation |
| `pl_eps26` | 112.50 crore / 114.83 crore shares | 0.98 | Author's computation |
| `pl_pe26` | 176.57 / 0.98 | 180.2 | Author's computation |
| `pl_pb` | 176.57 / 51.06 | 3.46 | Author's computation |
| `pl_ps` | 20,389 / 2,710.60 | 7.52 | Author's computation |
| `pl_range` | (284.00 - 134.73) / 134.73 x 100 | 110.79 | Author's computation |
| `pl_sh_total` | 0.00 + 24.82 + 9.49 + 65.69 | 100.0 | Author's computation |

## D. Cross-checks performed

| Check | Expected | Obtained | Result |
|---|---|---|---|
| Sum of five daily MTM flows equals total price change x lot size | 9,000.00 | 9,000.00 | pass |
| Shareholding categories sum to 100 per cent | 100.00 | 100.00 | pass |
| Put-call parity on the illustrative option (C - P = S - K e^-rt) | holds to 1e-9 | holds | pass |
| Segment revenue DITP + IAP equals total revenue, each year | equal | equal | pass |
| Charge ladder: sum of components equals printed total, both examples | equal | equal | pass |
| Table caption numbering sequential within every chapter | 1..n | 1..n | pass |
| Figure caption numbering sequential within every chapter | 1..n | 1..n | pass |
| Every captioned table and figure referenced in the body text | all | all | pass |
| Every table grid sums to 9,000 twips (or 2,400 for the stamp box) | yes | yes | pass |

## E. Items that could NOT be verified and are marked "to be verified" in the text

1. Cash-market and equity-derivatives turnover for FY2025-26 (Table 5.3).
2. Exact pre-open, closing and post-close session boundaries (Table 3.4).
3. Current scrip-wise VaR and ELM rates in the cash market (Table 3.8).
4. SPAN scenario parameters and exposure-margin percentages (Table 3.12).
5. Scrip-wise price-band assignment (Table 3.6).
6. Actual lot size of any live futures contract (Table 3.10).
7. Scope of the optional T+0 facility (Table 3.7).
8. Scrip-wise GSM / ASM lists (Table 3.18).
9. PINELABS price band, surveillance status, F&O eligibility and lot size (Table 5.28).
10. Revenue and PAT of the four listed peers (Table 5.26).
11. Pine Labs total equity for FY2024-25 (Table 5.21).
12. Pine Labs Q1 FY27 profit before tax: Rs. 37.73 cr per the filing; one aggregator reports Rs. 31.73 cr. The filing figure is used and the discrepancy is flagged.

## F. Limitations of this build

* No PDF renderer (LibreOffice / Word) exists in this environment, so the document could not
  be rendered and inspected page by page. Page numbers in the Contents are computed by a
  layout model in `build/paginate.py` and must be refreshed in Word (right-click the Contents
  table after inserting the logo, letterhead and certificate images).
* Estimated length 73 A4 pages against the 60-66 target. The overage is structural: the
  mandated 55 tables, 17 figures, 73 source lines, interpretation paragraphs after every
  exhibit and 1.5 line spacing cannot be compressed further without dropping required
  sections. To reach 66 pages, delete Section 2.5 (if the firm publishes no mission
  statement), Section 3.14 and its table, Section 3.20, and trim Annexures A and C.
* Charts use STIXGeneral, the nearest available serif; Times New Roman is not installed in
  this environment. The .docx itself specifies Times New Roman throughout.
