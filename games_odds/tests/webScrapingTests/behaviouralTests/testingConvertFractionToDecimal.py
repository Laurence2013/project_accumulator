from django.test import TestCase
from django.conf import settings
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb

'''
This is the 6th Behavioural test
'''

class TestingConvertFractionToDecimal(TestCase, DecimalToFractionAndStoreInDb):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.tbody_link_0_odds = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_link_0_odds.csv'
        self.tbody_link_1_odds = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_link_1_odds.csv'
        self.get_odds = self.convert_fraction_to_decimal(self.tbody_link_1_odds)
        self.get_converts = self.create_new_list(self.get_odds)

    def test_01_CheckThatTheLengthIsGreaterThan_0(self):
        self.assertGreater(len(self.get_converts), 0)

    def test_02_GetIndex_0_AndCheckThatItsElementIsAFloat(self):
        self.assertIsInstance(self.get_converts[0][0], float)

    def test_03_GetIndex_1_AndCheckThatItsElementIsAFloat(self):
        self.assertIsInstance(self.get_converts[0][1], float)

    def test_04_GetIndex_2_AndCheckThatItsElementIsAFloat(self):
        self.assertIsInstance(self.get_converts[0][2], float)

    def test_05_GetIndex_3_AndCheckThatItsElementIsAFloat(self):
        self.assertIsInstance(self.get_converts[1][0], float)

    def test_06_GetIndex_4_AndCheckThatItsElementIsAFloat(self):
        self.assertIsInstance(self.get_converts[1][1], float)

    def test_07_GetIndex_5_AndCheckThatItsElementIsAFloat(self):
        self.assertIsInstance(self.get_converts[1][2], float)
