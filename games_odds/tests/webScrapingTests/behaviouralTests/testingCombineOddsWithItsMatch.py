from django.test import TestCase
from django.conf import settings
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb

'''
This is the 7th Behavioural test
'''

class TestingCombineOddsWithItsMatch(TestCase, CombineOddsWithItsMatch, DecimalToFractionAndStoreInDb):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.get_span_ids_link_1 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/span_ids_link_1.csv'
        self.tbody_link_1_odds = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_link_1_odds.csv'
        self.get_match = self.get_match(self.get_span_ids_link_1)
        self.get_odds = self.convert_fraction_to_decimal(self.tbody_link_1_odds)
        self.get_converts = self.create_new_list(self.get_odds)

    def test_GetIndex_0_AndMakeSureThatLengthIsGreaterThan_0(self):
        self.assertGreater(len(self.get_match),0)

    def test_CheckThatLengthOfoddsListIsEqualToGetMatchList(self):
        self.assertEqual(len(self.get_match), len(self.get_converts))

    def test_CheckThatIndex_0_IsSimilar(self):
        tuple_combo = ('Norwich \xa0 v \xa0\xa0Brighton', [1.38, 2.5, 1.8])
        get_combined = self.combine_odds_match(self.get_match, self.get_converts)
        self.assertTupleEqual(tuple_combo, get_combined[0])

    def test_CheckThatIndex_1_IsSimilar(self):
        tuple_combo = ('Sevilla \xa0 v \xa0\xa0Granada', [0.2, 6.0, 11.0])
        get_combined = self.combine_odds_match(self.get_match, self.get_converts)
        self.assertTupleEqual(tuple_combo, get_combined[1])

    def test_CheckThatIndex_3_IsSimilar(self):
        tuple_combo = ('FC Koln \xa0 v \xa0\xa0Hoffenheim', [2.1, 2.5, 1.2])
        get_combined = self.combine_odds_match(self.get_match, self.get_converts)
        self.assertTupleEqual(tuple_combo, get_combined[2])

    def test_CheckThatIndex_4_IsSimilar(self):
        tuple_combo = ('Nancy \xa0 v \xa0\xa0Marseille', [2.4, 2.3, 1.15])
        get_combined = self.combine_odds_match(self.get_match, self.get_converts)
        self.assertTupleEqual(tuple_combo, get_combined[3])

    def test_CheckThatIndex_5_IsSimilar(self):
        tuple_combo = ('Heerenveen \xa0 v \xa0\xa0Willem II', [0.75, 2.75, 3.0])
        get_combined = self.combine_odds_match(self.get_match, self.get_converts)
        self.assertTupleEqual(tuple_combo, get_combined[4])
