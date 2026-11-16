"""Fast, deterministic smoke tests.  Run: python -m unittest discover -s tests -v"""
import csv
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'

def read(name):
    with (DATA/name).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))

class ReproductionTests(unittest.TestCase):
    def test_nine_figures_exist(self):
        figs=list((ROOT/'figures').glob('figure_*.png'))
        self.assertEqual(len(figs),9)
        self.assertTrue(all(p.stat().st_size>20000 for p in figs))

    def test_morris_retention_and_totals(self):
        d={x['sex']:x for x in read('morris_1993_retention.csv')}
        self.assertAlmostEqual(100*int(d['Men']['included_under_20'])/int(d['Men']['all_respondents']),80.6032,places=3)
        self.assertAlmostEqual(100*int(d['Women']['included_under_20'])/int(d['Women']['all_respondents']),97.127,places=2)
        t={x['sex']:x for x in read('morris_1993_partner_totals.csv')}
        ratio=int(t['Men']['partnership_total'])/int(t['Women']['partnership_total'])
        mean_ratio=(int(t['Men']['partnership_total'])/int(t['Men']['respondents']))/(int(t['Women']['partnership_total'])/int(t['Women']['respondents']))
        self.assertAlmostEqual(ratio,1.19,places=2)
        self.assertAlmostEqual(mean_ratio,1.56,places=2)
        self.assertGreater(mean_ratio,ratio)

    def test_wiederman_not_just_male_heaping(self):
        d={r['sex']:r for r in read('wiederman_1997_heaping.csv')}
        self.assertAlmostEqual(100*int(d['Men']['multiple_of_five_reports'])/int(d['Men']['all_reporting_more_than_15']),85.8,places=1)
        self.assertAlmostEqual(100*int(d['Women']['multiple_of_five_reports'])/int(d['Women']['all_reporting_more_than_15']),82.8,places=1)

    def test_mitchell_confidence_intervals_and_attenuation(self):
        rows=read('mitchell_2019_adjustments.csv')
        for r in rows:
            self.assertLess(float(r['ci95_lower']),float(r['difference_men_minus_women']))
            self.assertGreater(float(r['ci95_upper']),float(r['difference_men_minus_women']))
        first=float(rows[0]['difference_men_minus_women']); last=float(rows[-1]['difference_men_minus_women'])
        self.assertAlmostEqual(100*(first-last)/first,62.54,places=2)
        self.assertEqual([r['difference_men_minus_women'] for r in rows],['7.02','5.47','3.24','2.63'])

    def test_fisher_experiment_and_reported_test_distinction(self):
        tests=read('published_tests.csv')
        t2003=next(t for t in tests if t['study']=='Alexander & Fisher 2003')
        self.assertEqual(t2003['f_value'],'')
        self.assertEqual(t2003['reported_p'],'F < 1')
        study2013=[t for t in tests if t['study']=='Fisher 2013']
        self.assertEqual(len(study2013),2)
        self.assertEqual({t['f_value'] for t in study2013},{'4.57','6.94'})
        self.assertAlmostEqual((3.35-2.70)-(1.96-2.85),1.54)

    def test_jaccard_exact_below_within_one(self):
        d=read('jaccard_2004_recall.csv')
        self.assertEqual(len(d),4)
        self.assertTrue(all(float(r['exact_agreement_pct'])<float(r['within_one_partner_pct']) for r in d))

    def test_turchik_not_mislabelled(self):
        d={r['item']:r for r in read('turchik_2009_code4_thresholds.csv')}
        self.assertEqual(d['1']['unit'],'people')
        self.assertEqual(d['9']['unit'],'episodes')
        self.assertEqual(d['8']['raw_frequency_category'],'Not printed')
        self.assertTrue(all(r['period']=='Past 6 months' for r in d.values()))

    def test_article_identification(self):
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        self.assertIn('can-we-trust-self-reported-sexual',readme)
        self.assertIn('not** the distinct article',readme)

if __name__=='__main__':
    unittest.main()
