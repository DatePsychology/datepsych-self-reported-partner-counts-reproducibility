#!/usr/bin/env python3
"""Recreate nine descriptive figures and numerical checks for the *first* critique.

COMPANION ARTICLE: Can We Trust Self-Reported Sexual Partner Counts?
https://datepsych.substack.com/p/can-we-trust-self-reported-sexual

The input data are *published, rounded summaries* in ./data/*.csv.  This is
not a participant-level replication, and it does not prove true sexual counts.

Run: python reproduce_self_report_counts.py
Outputs: figures/figure_01_...png to figures/figure_09_...png,
         reconstruction_results.txt, reconstruction_checks.csv.
"""
from __future__ import annotations

import csv
from pathlib import Path
import math

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, FancyBboxPatch
import numpy as np
from scipy.stats import f as f_distribution

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
FIGURES = ROOT / 'figures'
FIGURES.mkdir(parents=True, exist_ok=True)

INK = '#1C2A36'
TEAL = '#467E87'
OCHRE = '#A68066'
LIGHT = '#F7F5F1'
MUTED = '#5F6D78'
GRID = '#D9DEE1'

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 11,
    'axes.titlesize': 16, 'axes.labelsize': 11,
    'axes.spines.top': False, 'axes.spines.right': False,
    'figure.facecolor': LIGHT, 'axes.facecolor': LIGHT,
    'savefig.facecolor': LIGHT, 'axes.edgecolor': '#BFC8CC',
    'xtick.color': MUTED, 'ytick.color': MUTED,
    'text.color': INK, 'axes.labelcolor': INK,
})


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding='utf-8', newline='') as fh:
        return list(csv.DictReader(fh))


def value(rows, **criteria):
    matches = [r for r in rows if all(r[k] == v for k, v in criteria.items())]
    if len(matches) != 1:
        raise AssertionError(f'Expected one row for {criteria}, got {len(matches)}')
    return matches[0]


def figure(title: str, subtitle: str, size=(11, 6.2), extra_top=0.0):
    fig, ax = plt.subplots(figsize=size)
    fig.subplots_adjust(left=.10, right=.955, top=.74-extra_top, bottom=.19)
    fig.text(.10, .945, title, fontsize=18, fontweight='bold', color=INK, va='top')
    fig.text(.10, .876, subtitle, fontsize=10.5, color=MUTED, va='top')
    ax.set_axisbelow(True)
    ax.grid(axis='y', color=GRID, linewidth=.8)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#C8CDD1')
    ax.tick_params(axis='both', length=0, pad=8)
    return fig, ax


def save(fig, name):
    path = FIGURES / name
    fig.savefig(path, dpi=155, metadata={'Software': 'Matplotlib; summary-data reconstruction'})
    plt.close(fig)
    return path


def key_legend(fig, items, y=.823):
    fig.legend(handles=[Patch(facecolor=color, label=label) for label, color in items],
               loc='upper left', bbox_to_anchor=(.10, y), ncol=len(items),
               frameon=False, fontsize=10.5, borderaxespad=0, handlelength=1.5,
               columnspacing=1.8)


def grouped_bars(ax, groups, series, lookup, colors=(INK, TEAL), width=.34,
                 top_extra=.13, fmt='{:.1f}', ylim=None):
    x = np.arange(len(groups), dtype=float)
    vals = []
    for i, s in enumerate(series):
        arr = [lookup(g, s) for g in groups]
        vals.extend(arr)
        bx = x + (i-(len(series)-1)/2)*width
        bars = ax.bar(bx, arr, width=width*.96, color=colors[i], zorder=3)
        for bar, y in zip(bars, arr):
            ax.text(bar.get_x()+bar.get_width()/2, y+max(vals)*.024,
                    fmt.format(y), ha='center', va='bottom', color=INK,
                    fontweight='bold', fontsize=10, zorder=5)
    ax.set_xticks(x, groups)
    upper = ylim if ylim is not None else max(vals)*(1+top_extra)
    ax.set_ylim(0, upper)


# FIGURE 1: Morris ratios represent reported total partnerships, not mean or accuracy.
morris_ratios = read_csv('morris_1993_ratios.csv')
ratio_groups = [r['group'] for r in morris_ratios]
ratio_vals = [float(r['reported_male_to_female_total_ratio']) for r in morris_ratios]
fig, ax = figure('Where Morris located the excess',
                 'Morris (1993), Table 2  |  Ratio of reported opposite-sex partnership totals')
ax.bar(range(3), ratio_vals, color=[TEAL, TEAL, OCHRE], width=.58, zorder=3)
ax.axhline(1, ls='--', lw=1.4, color=MUTED, alpha=.7, zorder=1)
for i, v in enumerate(ratio_vals):
    ax.text(i, v+.23, f'{v:.2f}:1', ha='center', fontweight='bold', fontsize=12)
ax.set_xticks(range(3), ['All respondents', 'Under 20 partners', '20+ partners'])
ax.set_ylim(0, 12)
ax.set_ylabel('Male / female reported partnership totals')
fig.text(.10,.055, 'This is not a comparison of verified individual counts or sex-specific group means.',
         fontsize=10, color=MUTED)
save(fig, 'figure_01_morris_ratios.png')

# FIGURE 2: subgroup retention denominators matter.
morris_retention = read_csv('morris_1993_retention.csv')
ret = {r['sex']: 100*int(r['included_under_20'])/int(r['all_respondents']) for r in morris_retention}
ret['Combined'] = 100*sum(int(r['included_under_20']) for r in morris_retention)/sum(int(r['all_respondents']) for r in morris_retention)
fig, ax = figure('An unevenly selected “90%”',
                 'Morris (1993)  |  Respondents remaining after excluding 20+ reported partners')
bars=ax.bar(['Men','Women','Combined'],[ret[k] for k in ('Men','Women','Combined')],
            color=[INK,TEAL,OCHRE],width=.6,zorder=3)
for b,k in zip(bars,('Men','Women','Combined')):
    ax.text(b.get_x()+b.get_width()/2,b.get_height()+1.4,f'{ret[k]:.1f}%',
            ha='center',fontweight='bold',fontsize=12)
ax.set_ylim(0,108); ax.set_ylabel('Percent of each group retained')
fig.text(.10,.055,'Retained respondents are not thereby shown to have reported accurately.',
         fontsize=10,color=MUTED)
save(fig,'figure_02_morris_retention.png')

# FIGURE 3: Brown 2017, *non-randomized* modes.
brown=read_csv('brown_2017_mode_means.csv')
fig,ax=figure('Mode differences are not necessarily mode effects',
              'Brown et al. (2017)  |  Separate telephone and web samples; no random allocation')
key_legend(fig,[('Men',INK),('Women',TEAL)])
grouped_bars(ax,['Telephone','Web'],['Men','Women'],
             lambda mode,sex: float(value(brown,mode=mode,sex=sex)['mean_lifetime_partners']),ylim=19,fmt='{:.1f}')
ax.set_ylabel('Mean reported lifetime partners')
fig.text(.10,.055,'Telephone n = 1,393; web n = 1,675 (total sample sizes, not sex-specific).',
         fontsize=10,color=MUTED)
save(fig,'figure_03_brown_modes.png')

# FIGURE 4: Turchik ordinal code's semantic meaning is item-specific.
turchik=read_csv('turchik_2009_code4_thresholds.csv')
fig=plt.figure(figsize=(11,5.65),facecolor=LIGHT)
fig.text(.075,.94,'Why code “4” is not a 10+ partner subgroup',fontweight='bold',fontsize=18,va='top')
fig.text(.075,.865,'Turchik & Garske (2009), Appendix  |  One ordinal code, different questions and units',
         color=MUTED,fontsize=10.5,va='top')
for i,(item,short,detail) in enumerate([
    ('1','10+ people','Partners in sexual activity short of oral, vaginal, or anal sex'),
    ('9','51+ episodes','Vaginal intercourse without a condom'),
    ('8','Not printed','Partners involving oral, vaginal, or anal sex'),
]):
    row=value(turchik,item=item)
    y=.68-.205*i
    card=FancyBboxPatch((.074,y-.072),.85,.143,boxstyle='round,pad=0.01,rounding_size=0.015',
                       transform=fig.transFigure,facecolor='#EDF1F2' if i!=1 else '#F3F0EC',
                       edgecolor=GRID,linewidth=.8)
    fig.add_artist(card)
    fig.text(.095,y,f'ITEM {item}',fontweight='bold',fontsize=11,va='center',color=TEAL)
    fig.text(.218,y,short,fontweight='bold',fontsize=14,va='center')
    fig.text(.445,y,detail,fontsize=10.3,va='center',color=INK)
fig.text(.08,.055,'Same code ≠ same respondents, frequency, or behavioral measure.',
         fontsize=11,fontweight='bold')
save(fig,'figure_04_turchik_codes.png')

# FIGURE 5: Alexander & Fisher 2003 nonsignificant sex-by-condition effect for partners.
af=read_csv('alexander_fisher_2003_means.csv')
fig,ax=figure('The 2003 experiment: a suggestive, nonsignificant pattern',
              'Alexander & Fisher (2003)  |  Partner count sex-by-condition F < 1')
key_legend(fig,[('Men',INK),('Women',TEAL)])
grouped_bars(ax,['Exposure threat','Anonymous','Bogus pipeline'],['Men','Women'],
             lambda cond,sex:float(value(af,condition=cond,sex=sex)['reported_partner_mean']),
             ylim=5.9,fmt='{:.1f}')
ax.set_ylabel('Mean reported partners')
fig.text(.10,.055,'Published rounded means; a patterned difference is not by itself a significant interaction.',
         color=MUTED,fontsize=10)
save(fig,'figure_05_alexander_fisher_2003.png')

# FIGURE 6: Fisher 2013 a significant sex*condition interaction.
fisher=read_csv('fisher_2013_means.csv')
fig,ax=figure('The 2013 experiment: opposite-direction changes',
              'Fisher (2013)  |  Sex × condition interaction: F(1, 284) = 4.57, p = .033')
key_legend(fig,[('Men',INK),('Women',TEAL)])
grouped_bars(ax,['No bogus pipeline','Bogus pipeline'],['Men','Women'],
             lambda cond,sex:float(value(fisher,condition=cond,sex=sex)['reported_partner_mean']),
             ylim=4.25,fmt='{:.2f}')
ax.set_ylabel('Mean reported lifetime partners')
fig.text(.10,.055,'Changing reports under an experimental condition does not independently verify their truth.',
         fontsize=10,color=MUTED)
save(fig,'figure_06_fisher_2013.png')

# FIGURE 7: Jaccard multiple-partner subset, exact != within one.
jaccard=read_csv('jaccard_2004_recall.csv')
fig,ax=figure('“Within one” is not the same as exact recall',
              'Jaccard et al. (2004), Tables 2–3  |  Multiple-partner subset; weekly-record benchmark')
key_legend(fig,[('Exact agreement',INK),('Within ±1 partner',TEAL)])
groups=[r['window_months'] for r in jaccard]
labels=[f'{n} month'+('s' if int(n)>1 else '') for n in groups]
lookup_j={n:{'Exact agreement':float(r['exact_agreement_pct']),
             'Within ±1 partner':float(r['within_one_partner_pct'])}
          for n,r in zip(groups,jaccard)}
grouped_bars(ax,groups,['Exact agreement','Within ±1 partner'],
             lambda x,s:lookup_j[x][s],ylim=110,fmt='{:.1f}%')
ax.set_xticklabels(labels)
ax.set_ylabel('Percent of respondents (%)')
fig.text(.10,.055,'Exact percentages were reconstructed in the article; weekly self-reports are not ground truth.',
         fontsize=10,color=MUTED)
save(fig,'figure_07_jaccard_recall.png')

# FIGURE 8: Bell longitudinal count declines.
bell=read_csv('bell_2010_decreasing_lifetime_counts.csv')
fig,ax=figure('Inconsistency within the same cohort',
              'Bell et al. (2010), Table 2  |  Later “lifetime” count below an earlier count')
key_legend(fig,[('Men',INK),('Women',TEAL)])
grouped_bars(ax,['21 to 26','26 to 32','21 to 32'],['Men','Women'],
             lambda interval,sex:float(value(bell,interval=interval,sex=sex)['percent_with_lower_later_cumulative_report']),
             ylim=29,fmt='{:.1f}%')
ax.set_ylabel('Percent giving a lower later report')
fig.text(.10,.055,'This establishes a contradiction between reports—not which report was correct.',
         fontsize=10,color=MUTED)
save(fig,'figure_08_bell_consistency.png')

# FIGURE 9: Mitchell published survey confidence intervals, not fabricated intervals.
mitchell=read_csv('mitchell_2019_adjustments.csv')
fig,ax=figure('The reported gap shrinks—but does not disappear',
              'Mitchell et al. (2019), Table 1  |  Natsal-3 95% confidence intervals')
y=np.array([float(r['difference_men_minus_women']) for r in mitchell])
lower=np.array([float(r['ci95_lower']) for r in mitchell])
upper=np.array([float(r['ci95_upper']) for r in mitchell])
x=np.arange(len(y))
ax.bar(x,y,color=[INK,TEAL,TEAL,OCHRE],width=.58,zorder=3)
ax.errorbar(x,y,yerr=[y-lower,upper-y],fmt='none',ecolor=INK,
            capsize=5,elinewidth=1.5,zorder=4)
for i,n in enumerate(y):
    ax.text(i,upper[i]+.19,f'{n:.2f}',ha='center',fontsize=11,fontweight='bold')
ax.set_xticks(x,['Original gap','Cap at 99th\npercentile','+ Count/estimate\nadjustment','+ Sexual attitudes\nadjustment'])
ax.set_ylim(0,10.2)
ax.set_ylabel('Male − female mean lifetime partners')
fig.text(.10,.05,'Sequential capping/model adjustment is descriptive; it does not identify the cause of reporting error.',
         fontsize=9.8,color=MUTED)
save(fig,'figure_09_mitchell_adjustments.png')

# Numeric checks: all values derive from tracked CSVs; no participant data.
rows=[]
def record(key, number, unit, formula, provenance):
    rows.append(dict(check_id=key,value=number,unit=unit,formula=formula,provenance=provenance))

male_under=value(morris_retention,sex='Men');female_under=value(morris_retention,sex='Women')
m_n=int(male_under['included_under_20']);f_n=int(female_under['included_under_20'])
m_all=int(male_under['all_respondents']);f_all=int(female_under['all_respondents'])
record('morris_retained_men',100*m_n/m_all,'%',f'100*{m_n}/{m_all}','Morris 1993 Table 2')
record('morris_retained_women',100*f_n/f_all,'%',f'100*{f_n}/{f_all}','Morris 1993 Table 2')
record('morris_retained_combined',100*(m_n+f_n)/(m_all+f_all),'%',f'100*({m_n}+{f_n})/({m_all}+{f_all})','Morris 1993 Table 2')
mt=read_csv('morris_1993_partner_totals.csv')
mtm=int(value(mt,sex='Men')['partnership_total']); mtw=int(value(mt,sex='Women')['partnership_total'])
record('morris_under20_total_ratio',mtm/mtw,'ratio',f'{mtm}/{mtw}','Morris 1993 Table 2')
record('morris_under20_male_mean',mtm/m_n,'partners/person',f'{mtm}/{m_n}','Morris 1993 Table 2')
record('morris_under20_female_mean',mtw/f_n,'partners/person',f'{mtw}/{f_n}','Morris 1993 Table 2')
record('morris_under20_mean_ratio',(mtm/m_n)/(mtw/f_n),'ratio','male selected mean / female selected mean','Morris 1993 Table 2')
record('morris_excess_over_parity_all',100*(ratio_vals[0]-1),'%',f'100*({ratio_vals[0]} - 1)','Morris 1993 Table 2')
record('morris_excess_over_parity_under20',100*(ratio_vals[1]-1),'%',f'100*({ratio_vals[1]} - 1)','Morris 1993 Table 2')

wied=read_csv('wiederman_1997_heaping.csv')
for sex in ('Men','Women'):
    r=value(wied,sex=sex)
    num=int(r['multiple_of_five_reports']);den=int(r['all_reporting_more_than_15'])
    record('wiederman_heaping_'+sex.lower(),100*num/den,'%',f'100*{num}/{den}','Wiederman 1997 GSS subgroup')

strats=read_csv('brown_1999_high_count_strategy.csv')
for sex in ('Men','Women'):
    r=value(strats,sex=sex)
    record('brown_1999_rough_estimate_count_'+sex.lower(),
           int(r['subgroup_size'])*float(r['percent_reporting_rough_approximation'])/100,
           'approximate persons','subgroup size * published percent /100','Brown & Sinclair 1999')
for mode in ('Telephone','Web'):
    r_m=float(value(brown,mode=mode,sex='Men')['mean_lifetime_partners'])
    r_f=float(value(brown,mode=mode,sex='Women')['mean_lifetime_partners'])
    record('brown_2017_ratio_'+mode.lower(),r_m/r_f,'ratio','male mean / female mean','Brown et al 2017')

for row in read_csv('mitchell_2019_time_windows.csv'):
    m=float(row['male_mean']); w=float(row['female_mean'])
    record('mitchell_excess_'+row['window'].lower().replace(' ','_'),100*(m/w-1),'%',
           '100*(male mean/female mean - 1)','Mitchell 2019 Table 1')
record('mitchell_gap_reduction',100*(y[0]-y[-1])/y[0],'%',
       '(original gap - final gap)/original gap *100','Mitchell 2019 Table 1')
record('fisher_2013_diff_in_diffs',
       (3.35-2.70)-(1.96-2.85),'partners','(women pipeline - women control) - (men pipeline - men control)',
       'Fisher 2013 published rounded cell means')

for row in read_csv('published_tests.csv'):
    if row['f_value'] and row['df_numerator'] and row['df_denominator']:
        fval=float(row['f_value']);df1=int(row['df_numerator']);df2=int(row['df_denominator'])
        record('pcheck_'+row['study'].replace(' ','_').replace('&','and')+'_'+str(df2)+'_'+str(int(fval*100)),
               f_distribution.sf(fval,df1,df2),'p (unrounded)',
               f'F survival function, F={fval}, df={df1},{df2}',row['source_location'])

# A real data file is retained for the mathematical counterexample; no random simulation.
illustrative=read_csv('illustrative_aggregate_consistency.csv')
assert len(illustrative)==2
assert len({int(r['reported_total']) for r in illustrative})==1
assert all(int(r['true_total'])!=int(r['reported_total']) for r in illustrative)

with (ROOT/'reconstruction_checks.csv').open('w',encoding='utf-8',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=['check_id','value','unit','formula','provenance'])
    w.writeheader();w.writerows(rows)

with (ROOT/'reconstruction_results.txt').open('w',encoding='utf-8') as fh:
    fh.write('Can We Trust Self-Reported Sexual Partner Counts? — Reproducibility results\n')
    fh.write('='*73+'\n')
    fh.write('Published rounded summaries ONLY. Not individual-level replication.\n\n')
    for r in rows:
        fh.write(f"{r['check_id']:49} {r['value']:>12.6f} {r['unit']}\n")
    fh.write('\nCautions: Morris 1.19 is total-partnership ratio, not mean ratio.\n')
    fh.write('The 2003 study reports F < 1, so an exact p cannot be reconstructed.\n')
    fh.write('The Mitchell adjusted gap is not a causal estimate of dishonesty.\n')
    fh.write('No true lifetime histories, raw participant observations, or trial randomization\n')
    fh.write('records are available in these inputs. Figures show reported summaries.\n')

print('Created',len(list(FIGURES.glob('figure_*.png'))),'figures and',len(rows),'numeric checks.')
print('Wiederman heaping: ',*[f"{r['check_id']}={r['value']:.2f}%" for r in rows if 'wiederman_heaping' in r['check_id']])
print('Morris retained overall:',f'{ret["Combined"]:.2f}%')
print('Mitchell gap reduction:',f'{100*(y[0]-y[-1])/y[0]:.2f}%')
print('Output directory:', ROOT)
