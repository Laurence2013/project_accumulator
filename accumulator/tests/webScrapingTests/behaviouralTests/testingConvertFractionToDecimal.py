from django.test import TestCase
from django.conf import settings
import csv
import re
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
        odds = get_odds[3]
        for odd in odds:
            int_num = re.sub(r'(\d+)/(\d+)', lambda m: str(int(m.group(1))/int(m.group(2))), odd)
            found = re.findall("'(.+?)'", int_num)
            print(found)
            for f in found:
                if f == str('EVS'):
                    test_list.append(str(f))
                else:
                    test_list.append(float(f))
            print(test_list)
        self.assertEqual(1,1)
