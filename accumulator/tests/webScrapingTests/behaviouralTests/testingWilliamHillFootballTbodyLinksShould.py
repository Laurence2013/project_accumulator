import os
from django.conf import settings
from django.test import TestCase
from accumulator.webScraping.scrapingWilliamHill import ScrapingWilliamHill

'''
This is the 2nd behavioural test

This must be executed SECOND in order for the span(s) file to work by using tbody files
'''

class TestingWilliamHillFootballTbodyLinksShould(TestCase, ScrapingWilliamHill):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.tbody_ids_link_0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_ids_link_0.csv'
        self.tbody_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_ids_link_1.csv'
        self.get_links_0 = (self.get_tbody_ids('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/1/Football.html'))
        self.get_links_1 = (self.get_tbody_ids('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/2/Football.html'))

    def test_CheckThat_Get_Links_0_IsGreaterThan_0(self):
        self.assertGreater(len(self.tbody_ids_link_0), 0)

    def test_Save_Get_Links_0_IntoFile(self):
        self.save_file(self.tbody_ids_link_0, self.get_links_0)
        self.assertGreater(os.path.getsize(self.tbody_ids_link_0), 0)

    def test_CheckThat_Get_Links_1_IsGreaterThan_0(self):
        self.assertGreater(len(self.tbody_ids_link_1), 0)

    def test_Save_Get_Links_1_IntoFile(self):
        self.save_file(self.tbody_ids_link_1, self.get_links_1)
        self.assertGreater(os.path.getsize(self.tbody_ids_link_1), 0)
