import os
from django.conf import settings
from django.test import TestCase
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill

'''
This is the 5th behavioural test
'''

class TestingByGettingAllOddsFromTbodyLink0(TestCase, ScrapingWilliamHill):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.tbody_ids_link_0 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_ids_link_0.csv'
        self.tbody_ids_link_1 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_ids_link_1.csv'
        self.tbody_ids_link_0_odds = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_link_0_odds.csv'
        self.tbody_ids_link_1_odds = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_link_1_odds.csv'
        self.get_links_0 = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/1/Football.html'
        self.get_links_1 = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/2/Football.html'

    def test_CheckThatTbodyLink_0_IsGreaterThan_0(self):
        match_odds = self.get_all_odds_for_match(self.get_links_0, self.tbody_ids_link_0)
        self.assertGreater(len(match_odds), 0)

    def test_GetAllOddsFromTbodyLink_0_AndSaveAsCsvFileAndIsGreaterThan_0(self):
        match_odds = self.get_all_odds_for_match(self.get_links_0, self.tbody_ids_link_0)
        self.save_file(self.tbody_ids_link_0_odds, match_odds)
        self.assertGreater(len(self.tbody_ids_link_0_odds), 0)

    def test_CheckThatTbodyLink_1_IsGreaterThan_0(self):
        match_odds = self.get_all_odds_for_match(self.get_links_1, self.tbody_ids_link_1)
        self.assertGreater(len(match_odds), 0)

    def test_GetAllOddsFromTbodyLink_1_AndSaveAsCsvFileAndIsGreaterThan_0(self):
        match_odds = self.get_all_odds_for_match(self.get_links_1, self.tbody_ids_link_1)
        self.save_file(self.tbody_ids_link_1_odds, match_odds)
        self.assertGreater(len(self.tbody_ids_link_1_odds), 0)
