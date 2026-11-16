# Can We Trust Self-Reported Sexual Partner Counts? — Reproducibility Materials

**Companion article:** [Can We Trust Self-Reported Sexual Partner Counts?](https://datepsych.substack.com/p/can-we-trust-self-reported-sexual) — *What Date Psychology Gets Right—and Wrong About the Evidence* (Revisiting Datepsych, 10 November 2026).


The article reviews Date Psychology's [“Is Self Reported Sexual Partner Data Accurate?”](https://datepsychology.com/is-self-reported-sexual-partner-data-accurate/) (2022; subsequently updated). This repository records published summary statistics, reproduces the **nine figures** accompanying the broader critique, and recalculates several numerical claims: Morris's ratio of totals versus ratio of subgroup means; unequal trimming of male and female respondents; numerical heaping; the association between survey mode and reported means; prospective and longitudinal consistency; the 2013 experimental contrast; and the Natsal-3 adjustment sequence.

## What “reproducibility” means here

**This is a transparent reconstruction from published rounded aggregates, not a replication from the original individual-level data.** You can inspect and change every numeric input and regenerate the nine figures and arithmetic checks. You **cannot** use this package to verify each respondent's actual sexual history, re-estimate unreported distributions, reconstruct a randomization procedure, or refit original regressions and complex-survey models. *Matching an aggregate mean is not a test of individual accuracy.*

The figures reproduce the **published article's plotted quantities**. Their colors, type, exact spacing, and graphical style are newly generated and may differ from the PNGs embedded in the Substack post. The reported inputs and analytical qualifications are the same. No copyrighted full-text study files or respondent records are included.

## Repository contents

| Path | Purpose |
| --- | --- |
| [`reproduce_self_report_counts.py`](reproduce_self_report_counts.py) | One-command figure generation and statistical checks; all inputs read from CSV files. |
| [`data/`](data/) | 17 small, documented CSV files holding summary statistics, item coding definitions, source references, and a **clearly hypothetical** aggregate-accuracy example. |
| [`figures/`](figures/) | Nine generated PNG figures, matching the nine numbered visuals in the broader article. |
| [`reconstruction_results.txt`](reconstruction_results.txt) | Human-readable reference output containing 23 numerical checks. |
| [`reconstruction_checks.csv`](reconstruction_checks.csv) | Machine-readable calculated results, formulas, and study attributions. |
| [`CLAIM_AND_FIGURE_MAP.md`](CLAIM_AND_FIGURE_MAP.md) | Article section ↔ source ↔ data input ↔ chart/check crosswalk with evidence limits. |
| [`METHODS_AND_LIMITATIONS.md`](METHODS_AND_LIMITATIONS.md) | Precise calculation and inference boundaries. |
| [`tests/test_reconstructions.py`](tests/test_reconstructions.py) | Standard-library `unittest` tests for calculations, chart outputs, and provenance. |
| [`requirements.txt`](requirements.txt) | Python dependencies. |
| [`.gitignore`](.gitignore) | Excludes Python cache files. |

## Reproduce the numerical checks and figures

Use Python **3.10 or later** and run the following commands in the repository root:

```bash
python -m pip install -r requirements.txt
python reproduce_self_report_counts.py
python -m unittest discover -s tests -v
```

The script overwrites `figures/figure_*.png`, `reconstruction_results.txt`, and `reconstruction_checks.csv` in your local checkout. It does **not** download anything from the internet or use any private data. The script uses deterministic CSV inputs and does not perform stochastic simulations.

## Figures

| Article figure | Reproducible file | Published result and key caveat |
| --- | --- | --- |
| 1. Morris's ratios | [`figure_01_morris_ratios.png`](figures/figure_01_morris_ratios.png) | Ratios of **reported partnership totals**: 3.22, 1.19, 10.12; not accuracy estimates. |
| 2. Morris's retention | [`figure_02_morris_retention.png`](figures/figure_02_morris_retention.png) | Under-20 subgroup retains 80.6% of men, 97.1% of women, 89.2% overall; it does not identify truthful respondents. |
| 3. Brown et al. mode samples | [`figure_03_brown_modes.png`](figures/figure_03_brown_modes.png) | Lifetime means in separate telephone and web samples; mode is **not randomized**. |
| 4. Turchik & Garske codes | [`figure_04_turchik_codes.png`](figures/figure_04_turchik_codes.png) | Item-specific category 4 means 10+ people for Item 1, 51+ episodes for Item 9, and an unprinted threshold for Item 8; **not** comparable 10+ partner subgroups. |
| 5. Alexander & Fisher (2003) | [`figure_05_alexander_fisher_2003.png`](figures/figure_05_alexander_fisher_2003.png) | Experimental partner means; the sex-by-condition test for this outcome was **nonsignificant (F < 1)**. |
| 6. Fisher (2013) | [`figure_06_fisher_2013.png`](figures/figure_06_fisher_2013.png) | Sex-by-condition interaction **F(1,284)=4.57, p=.033**; a distinct within-condition contrast is **not** the interaction. |
| 7. Jaccard et al. | [`figure_07_jaccard_recall.png`](figures/figure_07_jaccard_recall.png) | Exact agreement versus ±1 partner agreement against weekly self-reports, among the multiple-partner subgroup. |
| 8. Bell et al. | [`figure_08_bell_consistency.png`](figures/figure_08_bell_consistency.png) | Proportions with decreasing cumulative lifetime reports across follow-ups. Contradiction does not tell which report is true. |
| 9. Mitchell et al. | [`figure_09_mitchell_adjustments.png`](figures/figure_09_mitchell_adjustments.png) | Sequential mean gap 7.02 → 5.47 → 3.24 → 2.63 with **published 95% CIs**; adjustments do **not** causally identify dishonesty. |

## Selected numerical reconstructions

- **Morris (1993):** 5,852 / 4,921 = **1.189** (ratio of under-20 reported partnership **totals**). The corresponding selected-group means are 5,852/1,363 = **4.29** (men) and 4,921/1,792 = **2.75** (women), with ratio **1.56**. These are different quantities, neither independently validated.
- **Morris retention:** 1,363/1,691 = **80.6%** men, 1,792/1,845 = **97.1%** women, and 3,155/3,536 = **89.2%** combined.
- **Wiederman (1997):** 194/226 = **85.8%** men and 53/64 = **82.8%** women reported multiples of five in the specified >15 subgroup. This is heaping, **not proof of upward bias**.
- **Brown & Sinclair (1999):** 29.4% of 85 men versus 4.4% of 90 women in a selected high-count subgroup corresponds approximately to 25 men versus 4 women using rough approximation. These inferred counts are approximate, not newly observed.
- **Brown et al. (2017):** Male/female mean ratio ≈ **2.85** (telephone) versus **1.76** (web). The samples were not experimentally assigned to mode.
- **Fisher (2013):** Based on rounded cell means, the difference-in-differences is **1.54** partner reports. The published adjusted interaction statistic, rather than the rounded means alone, provides the reported inference.
- **Mitchell et al. (2019):** (7.02 − 2.63)/7.02 = **62.5% attenuation** of the sex gap across capping and statistical adjustments; **not** 62.5% of respondents demonstrated inaccurate or dishonest reporting.

The [full mapping](CLAIM_AND_FIGURE_MAP.md) notes which of the article's criticisms concern **misreading** of a table or denominator and which require external validation that the published studies did not provide.

## Key source references

The full reference list and interpretations are in the [companion article](https://datepsych.substack.com/p/can-we-trust-self-reported-sexual). For the nine figures and associated numerical checks, the primary source locations are also recorded **per CSV row** and in [`data/source_register.csv`](data/source_register.csv). The main works are:

- Morris (1993), [*Nature*, Table 2](https://doi.org/10.1038/365437a0).
- Wiederman (1997), [*Journal of Sex Research*](https://doi.org/10.1080/00224499709551905).
- Brown & Sinclair (1999), [*Journal of Sex Research*](https://doi.org/10.1080/00224499909551999); Brown et al. (2017), [book chapter](https://www.researchgate.net/publication/333598739_Multiple_partners_multiple_strategies_multiple_causes).
- Turchik & Garske (2009), [*Archives of Sexual Behavior*, Table 2 and Appendix](https://doi.org/10.1007/s10508-008-9388-z).
- Michele G. Alexander & Terri D. Fisher (2003), [*Journal of Sex Research*](https://doi.org/10.1080/00224490309552164); Terri D. Fisher (2013), [*Sex Roles*](https://doi.org/10.1007/s11199-013-0266-3).
- Jaccard et al. (2004), [*Journal of Health Psychology*, Tables 2–3](https://doi.org/10.1177/1359105304045354).
- Bell et al. (2010), [*Sexually Transmitted Diseases*, Table 2](https://doi.org/10.1097/OLQ.0b013e3181d13ed8).
- Mitchell et al. (2019), [*Journal of Sex Research*, Table 1; open-access version](https://pmc.ncbi.nlm.nih.gov/articles/PMC6326215/).
- Brewer et al. (2000), [*PNAS*, prostitution-prevalence calculation](https://pmc.ncbi.nlm.nih.gov/articles/PMC17351/).

**Authorship clarification:** *Michele G. Alexander* is coauthor of the 2003 experimental paper; **Date Psychology** is the subject of the critique. They should not be conflated.

## Citation / license / corrections

If citing these materials, link to the [companion Substack article](https://datepsych.substack.com/p/can-we-trust-self-reported-sexual) and this repository. Numeric inputs are attributed to their original publications; each publication retains its own copyright and reuse terms. The plotting and arithmetic code is newly prepared for transparency; no original participant-level data or study PDFs are redistributed.

Corrections or alternative interpretations are welcome if supported by the original source tables and transparent calculations. The intent is to make the critique **auditable**, not to claim that all referenced analyses were independently reproduced.
