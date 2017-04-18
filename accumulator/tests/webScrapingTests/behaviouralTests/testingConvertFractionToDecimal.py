from django.test import TestCase
from django.conf import settings
from accumulator.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb

'''
This is the 6th Behavioural test
'''

class TestingConvertFractionToDecimal(TestCase, DecimalToFractionAndStoreInDb):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.tbody_link_0_odds = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_link_0_odds.csv'
        self.tbody_link_1_odds = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_link_1_odds.csv'
        self.span_ids_link_0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_0.csv'
        self.span_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_1.csv'
        self.get_odds = self.convert_fraction_to_decimal(self.tbody_link_1_odds)
        self.get_converts = self.create_new_list(self.get_odds)

    def test_GetIndex_0_AndConvertEachElementFromFractionToDecimal(self):
        self.assertGreater(len(self.get_converts), 0)

    def test_TurnCSVFileStringIntoFloatsIndex_00(self):
        self.assertIsInstance(self.get_converts[0][0], float)

    def test_TurnCSVFileStringIntoFloatsIndex_01(self):
        self.assertIsInstance(self.get_converts[0][1], float)

    def test_TurnCSVFileStringIntoFloatsIndex_02(self):
        self.assertIsInstance(self.get_converts[0][2], float)

    def test_TurnCSVFileStringIntoFloatsIndex_10(self):
        self.assertIsInstance(self.get_converts[1][0], float)

    def test_TurnCSVFileStringIntoFloatsIndex_11(self):
        self.assertIsInstance(self.get_converts[1][1], float)

    def test_TurnCSVFileStringIntoFloatsIndex_12(self):
        self.assertIsInstance(self.get_converts[1][2], float)
