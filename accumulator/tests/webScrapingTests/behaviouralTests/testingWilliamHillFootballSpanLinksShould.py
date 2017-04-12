import os
from django.conf import settings
from django.test import TestCase
from accumulator.webScraping.scrapingWilliamHill import ScrapingWilliamHill

'''
This is the 3rd behavioural test
'''

class TestingWilliamHillFootballSpanLinksShould(TestCase, ScrapingWilliamHill):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.tbody_ids_link_0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_ids_link_0.csv'
        self.tbody_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_ids_link_1.csv'
        self.span_ids_link_0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_0.csv'
        self.span_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_1.csv'
        self.get_links_0 = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html'
        self.get_links_1 = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/1/Football.html'

    def test_Save_SpanIdsLink_0_IntoFile(self):
        self.open_csv_file(self.get_links_0, self.tbody_ids_link_0)
        self.assertGreater(len(ScrapingWilliamHill.span_id_lists), 0)

    def test_CheckThat_SpanIdsLink_0_IsGreaterThan_0(self):
        return False

    def test_CheckThat_SpanIdsLink_1_IsGreaterThan_0(self):
        return False
