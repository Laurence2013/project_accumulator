from django.test import TestCase
from django.conf import settings
from accumulator.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from accumulator.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb

'''
This is the 7th Behavioural test
'''

class TestingCombineOddsWithItsMatch(TestCase, CombineOddsWithItsMatch, DecimalToFractionAndStoreInDb):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.get_span_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_1.csv'
        self.tbody_link_1_odds = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_link_1_odds.csv'
        self.get_match = self.get_match(self.get_span_ids_link_1)
        self.get_odds = self.convert_fraction_to_decimal(self.tbody_link_1_odds)
        self.get_converts = self.create_new_list(self.get_odds)

    def test_GetIndex_0_AndMakeSureThatLengthIsGreaterThan_0(self):
        self.assertGreater(len(self.get_match),0)

    def test_CheckThatLengthOfoddsListIsEqualToGetMatchList(self):
        self.assertEqual(len(self.get_match), len(self.get_converts))

    def test_CheckThatIndex_0_IsSimilar(self):
        tuple_combo = ('Middlesbrough \xa0 v \xa0\xa0Arsenal', [5.0, 3.0, 0.57])
        get_combined = self.combine_odds_match(self.get_match, self.get_converts)
        self.assertTupleEqual(tuple_combo, get_combined[0])

    def test_CheckThatIndex_1_IsSimilar(self):
        tuple_combo = ('Fulham \xa0 v \xa0\xa0Aston Villa', [0.85, 2.6, 3.2])
        get_combined = self.combine_odds_match(self.get_match, self.get_converts)
        self.assertTupleEqual(tuple_combo, get_combined[1])
