# Figure and claim map

**Applies to:** [Can We Trust Self-Reported Sexual Partner Counts?](https://datepsych.substack.com/p/can-we-trust-self-reported-sexual) (the *first*, broad critique), **not** the separate fake-lie-detector-focused article.

**Status meanings:** `arithmetic` = can be recomputed exactly from the transcribed values; `redrawn` = a newly rendered chart of published rounded values; `reported` = inferential statistic supplied by source researchers and not re-estimated from microdata; `interpretive` = conceptual/table-reading critique requiring the source context; `illustrative` = hypothetical demonstration, not observed data.

| Article section | Source | Input file(s) | Output(s) | Scope and limitation |
| --- | --- | --- | --- | --- |
| §2: closed-population accounting rule | Mathematical identity | `data/illustrative_aggregate_consistency.csv` | `reconstruction_results.txt` (conceptual assertion) | **Illustrative:** equal reported sex totals do not verify individual counts; full network and equal population assumptions matter. |
| §3: Morris ratio of totals | Morris (1993) Table 2 | `morris_1993_ratios.csv`, `morris_1993_partner_totals.csv` | Figure 1; `morris_under20_*` calculations | **Arithmetic + redrawn:** 1.19 total ratio, 1.56 selected-mean ratio. No criterion accuracy data. |
| §3: respondent retention | Morris (1993) Table 2 | `morris_1993_retention.csv` | Figure 2; retention checks | **Arithmetic + redrawn:** selecting respondents reporting under 20 keeps different shares of men and women. |
| §4: digit heaping | Wiederman (1997), GSS | `wiederman_1997_heaping.csv` | `wiederman_heaping_*` checks | **Arithmetic:** percentages of responses in multiples of five. Neither true counts nor sign of rounding errors is known. |
| §5: enumeration and rough estimation | Brown & Sinclair (1999) | `brown_1999_high_count_strategy.csv` | `brown_1999_rough_estimate_count_*` checks | **Approximate arithmetic:** multiplying reported percentages by subgroup n gives approximate counts. Method was not randomized. |
| §5: telephone versus web | Brown et al. (2017) | `brown_2017_mode_means.csv` | Figure 3; mode-ratio checks | **Redrawn:** comparison of distinct samples, not a controlled experimental mode effect. |
| §6: recall-window averages | Mitchell et al. (2019) Table 1 | `mitchell_2019_time_windows.csv` | `mitchell_excess_*` checks | **Arithmetic:** smaller short-window discrepancies do not isolate recall bias causally. |
| §7: the Sexual Risk Survey code interpretation | Turchik & Garske (2009), Appendix | `turchik_2009_code4_thresholds.csv` | Figure 4 | **Interpretive:** the item-specific category 4 cannot be used to form a common respondent-level '10+ lifetime partners' subgroup. No cross-tabulations were recovered or invented. |
| §8: prostitution prevalence misquotation | Brewer et al. (2000) | `brewer_2000_statistic.csv` | Study inputs | **Interpretive:** '4%' is the fraction of observed sex workers under age 18 in a source sample, *not* prevalence among all women. Model-based adjustment does not validate others' answers. |
| §9: 2003 bogus pipeline | Michele Alexander & Terri Fisher (2003) | `alexander_fisher_2003_means.csv`, `published_tests.csv` | Figure 5 | **Reported + redrawn:** sex-by-condition effect for partner numbers reported as F < 1; no exact p can be computed from that inequality alone. |
| §9: 2013 bogus pipeline | Fisher (2013) | `fisher_2013_means.csv`, `published_tests.csv` | Figure 6; difference-in-differences; F→p checks | **Reported + arithmetic:** F(1,284)=4.57, p=.033 for interaction, not to be confused with F(1,284)=6.94 within-pipeline sex contrast. |
| §10: prospective weekly vs retrospective recall | Jaccard et al. (2004) Tables 2–3 | `jaccard_2004_recall.csv` | Figure 7 | **Redrawn:** within-one percentages published, exact percentages reconstructed for article from Table 2; original weekly records not available. |
| §10: declining cumulative counts | Bell et al. (2010) Table 2 | `bell_2010_decreasing_lifetime_counts.csv` | Figure 8 | **Redrawn:** inconsistency demonstrates at least one disagreement; accuracy direction unresolved. |
| §11: Natsal-3 adjusted lifetime gap | Mitchell et al. (2019) Table 1 | `mitchell_2019_adjustments.csv` | Figure 9; 62.5% attenuation | **Reported + arithmetic:** 95% CIs transcribed, models not rerun. Sequential adjustment not a causal decomposition of dishonesty. |

Figures 1–9 use **reported observations/aggregates**, except Figure 4, which is a **semantic coding diagram**, not a statistical observation chart. None is a simulation of participants or independently verified lifetime partner counts.

## Item 1 versus Item 8 in Turchik & Garske

The article points out a measurement mismatch that changes the interpretation of an entire argument. Item 1 concerns *partners with whom sexual behavior short of oral, vaginal, or anal intercourse occurred during the previous six months*. Item 8 separately concerns *sex partners involving oral, vaginal, or anal sex*. The categories are ordinal codes with item-specific raw thresholds. Data about the distribution of Item 1 codes cannot silently be relabeled as lifetime counts, nor does Table 2 provide the joint individual-level distribution required for Date Psychology's claimed comparisons by partner-count subgroup.

## Source audit boundaries

Every provided CSV value has a declared study, table or section and outcome definition. The 2003 cell means and some other values were preserved from the article's previously prepared figures, while the Natsal-3 stage estimates and CIs were checked against Mitchell et al.'s published Table 1. Where raw denominators, model covariance matrices, participant records, or authors' code are unavailable, the archive does not invent them. Claims requiring those data are specifically identified rather than called 'replicated.'
