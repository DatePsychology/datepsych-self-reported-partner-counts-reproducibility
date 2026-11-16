# Methods, assumptions, and known limits

This document applies to **[Can We Trust Self-Reported Sexual Partner Counts?](https://datepsych.substack.com/p/can-we-trust-self-reported-sexual)**, not the other Substack article on fake lie detectors.

## Input provenance

All numerical inputs are either quoted from a named study's table/results section or retained from the broader critique's existing published figure reconstruction. The CSV files have human-readable labels, source locations, and limitations. No microdata were supplied or fabricated; no raw survey data are downloaded automatically. The script uses only deterministic transformations.

### Ratios of totals versus ratios of means (Morris, 1993)

For the under-20 selected subgroup, the sum of reported opposite-sex partnerships is 5,852 for 1,363 men and 4,921 for 1,792 women. Thus:

- **Reported total-partnership ratio:** 5,852 / 4,921 ≈ 1.189.
- **Selected male mean:** 5,852 / 1,363 ≈ 4.29.
- **Selected female mean:** 4,921 / 1,792 ≈ 2.75.
- **Ratio of selected means:** (5,852/1,363) / (4,921/1,792) ≈ 1.56.

These distinct denominators explain why the 1.19 ratio cannot be interpreted as a respondent-by-respondent match. Conditioning both sexes' participation on their own count breaks any claim that this selected sample is a closed network.

### Retained fraction versus individual accuracy

The retained fraction is 1,363/1,691 for men, 1,792/1,845 for women, and (1,363+1,792)/(1,691+1,845) combined. None of these computations determines whether retained persons reported the correct partner count. The `illustrative_aggregate_consistency.csv` file constructs one deliberately **hypothetical** case with equal male and female totals but inaccurate answers to demonstrate the logic. It is not a dataset about real individuals.

### Numerical heaping (Wiederman, 1997)

194/226 men and 53/64 women in the specified high-count GSS subgroups reported multiples of five. These figures indicate **digit preference/rounding**, not the direction or size of discrepancies from unknown true histories. No upward- versus downward-rounding proportions are computed.

### Small cells in estimation strategies (Brown & Sinclair, 1999)

The reviewed article reports 29.4% of 85 men and 4.4% of 90 women in the high-count subgroup using rough approximation. Multiplying reported percentages by n yields ~25 and ~4, respectively. These are approximate reconstructions from rounded fractions and are **not** source-reported individual records or exact subgroup stratifications.

### Turchik & Garske (2009)

The five ordinal response codes vary by item. Figure 4 intentionally **does not fabricate an outcome-by-lifetime-partners joint distribution** from marginal item frequencies. Its Item 8 category-4 raw-frequency boundary is displayed as 'Not printed' because no such numeric threshold was supplied in the cited appendix. The diagram is a comparison of label meanings, not a test or estimated association. Its cited Item 1 frequencies relate to a six-month question about behavior short of oral/vaginal/anal sex.

### Bogus-pipeline studies (2003, 2013)

The CSVs preserve cell means reported or reconstructed in the article and report the relevant tests separately.

- For the **2003 study**, only `F < 1` is recorded for the partner-count interaction. No particular F value or p is invented to fill the gap; the means alone are insufficient to reconstruct the trial's correct model-based p.
- For **2013**, `F(1, 284)=4.57` describes the sex-by-condition **interaction** (p≈.033). `F(1,284)=6.94` describes a **within-condition sex comparison** (p≈.009) and is never presented as the interaction. The sample-level difference-in-differences of the rounded means is ≈1.54 partners; the code does not infer its model-standard error from those means.
- Neither study contains a device capable of independently determining the truth of participants' partner histories.

### Jaccard (2004) and Bell (2010)

Jaccard's 'within one partner' percentages are published source summary results. Exact-match percentages were reconstructed in the article from the original Table 2, and are recorded to one decimal place here. Without Table 2's individual cell counts in this package, the program **plots those percentages rather than independently re-deriving exact-match percentages from the original distribution**. Weekly self-reports are a stronger but imperfect comparator.

Bell's declining cumulative lifetime reports are logically inconsistent if the same metric was used at both waves; however, the observations cannot by themselves reveal whether earlier reports were inflated, later reports omitted events, or both.

### Natsal-3 (Mitchell et al., 2019)

The file `mitchell_2019_adjustments.csv` transcribes four stages of the published mean gap and their original 95% confidence intervals from Table 1:

| Stage | Gap | 95% CI |
| --- | ---: | --- |
| Original lifetime | 7.02 | 4.97–9.08 |
| Cap at sex-specific 99th percentile | 5.47 | 4.92–6.01 |
| Plus counting/estimation adjustment | 3.24 | 2.81–3.68 |
| Plus sexual-attitudes adjustment | 2.63 | 2.22–3.04 |

The final stage means **capping plus adjustment for both counting strategy and attitudes**. Plotting published confidence intervals is not estimating them from the CSV's four means. The original study involved survey weights, clustering, and model adjustment; those cannot be reproduced without the full original participant-level dataset and methods. The observed 62.54% attenuation of a reported gap is **not an estimate of how much of the gap was caused by lying**.

### Brewer et al. (2000)

The '4%' statistic describes **the fraction of observed sex workers younger than 18** in the cited source population; it does not state that 4% of all women engage in prostitution. The separate prevalence estimates are approximately 23 and 22.1 full-time-equivalent sex workers per 100,000 population in the model. These are distinct denominators and phenomena. The archive does not recreate Brewer's complex extrapolation from unavailable microdata.

## Interpretation

The package can demonstrate arithmetic and accurately communicate study summaries. It cannot establish whether a given man or woman exaggerated or concealed their count, whether aggregate estimates exactly match real-world totals, or whether observational associations reflect a single causal mechanism. Reviewers should consult the linked originals to contest transcriptions or interpretation.
