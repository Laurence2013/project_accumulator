import os
from django.conf import settings
from django.test import TestCase
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill

'''
This is the 3rd behavioural test
'''

class TestingWilliamHillFootballSpanLinksShould(TestCase, ScrapingWilliamHill):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.tbody_ids_link_0 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_ids_link_0.csv'
        self.tbody_ids_link_1 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_ids_link_1.csv'
        self.span_ids_link_0 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/span_ids_link_0.csv'
        self.span_ids_link_1 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/span_ids_link_1.csv'
        self.get_links_0 = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/1/Football.html'
        self.get_links_1 = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/2/Football.html'

    def test_Save_SpanIdsLink_0_IntoFileAndCheckThat_SpanIdsLink_0_IsGreaterThan_0(self):
        self.get_span_ids(self.get_links_0, self.tbody_ids_link_0)
        self.assertGreater(len(ScrapingWilliamHill.span_id_lists), 0)

    def test_SaveSpanIdsLink_0_IntoCsvFile(self):
        self.get_span_ids(self.get_links_0, self.tbody_ids_link_0)
        self.save_file(self.span_ids_link_0, ScrapingWilliamHill.span_id_lists)
        self.assertGreater(os.path.getsize(self.span_ids_link_0), 0)
        self.clear_list()

    def test_Save_SpanIdsLink_1_IntoFileAndCheckThat_SpanIdsLink_1_IsGreaterThan_0(self):
        self.get_span_ids(self.get_links_1, self.tbody_ids_link_1)
        self.assertGreater(len(ScrapingWilliamHill.span_id_lists), 0)

    def test_SaveSpanIdsLink_1_IntoCsvFile(self):
        self.get_span_ids(self.get_links_1, self.tbody_ids_link_1)
        self.save_file(self.span_ids_link_1, ScrapingWilliamHill.span_id_lists)
        self.assertGreater(os.path.getsize(self.span_ids_link_1), 0)
        self.clear_list()
