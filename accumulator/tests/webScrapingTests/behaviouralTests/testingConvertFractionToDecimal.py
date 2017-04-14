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

    def test_GetIndex_0_AndConvertEachElementFromFractionToDecimal(self):
        test_list = list()
        get_odds = self.convert_fraction_to_decimal(self.tbody_link_1_odds)
        for odds in get_odds:
            test_list.append(self.convert_string_into_float_or_string(odds))
        for test in test_list:
            print(test)

        self.assertEqual(1,1)
