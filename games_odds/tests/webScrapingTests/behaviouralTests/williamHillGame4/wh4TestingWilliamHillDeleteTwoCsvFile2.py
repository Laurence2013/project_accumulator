from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from django.test.client import RequestFactory
from games_odds.views import William_Hill_Games_4
from games_odds.mainViewsApi.main_views_api import MainViewsApi
from games_odds.william_hill_base import WilliamHillBase
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill

'''
This is testing no 3a
This is testing the refresh_no sent, sending 1 and emptying two files -> get_match_odds_link_4.csv and ids_for_tag_span_link_4.csv
Then refresh page with refresh_no 1
'''

class Wh4TestingWilliamHillDeleteTwoCsvFile2(TestCase, MainViewsApi, WilliamHillBase, ScrapingWilliamHill):
    def setUp(self):
        self.factory = RequestFactory()
        self.base_dir = settings.BASE_DIR

    def test_01_empty_2a_file_is_true(self):
        my_file = list()
        get_match_odds_link_1 = self.base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_4.csv'
        my_file.append(get_match_odds_link_1)
        is_empty_file = self.empty_files(my_file)
        self.assertTrue(is_empty_file)

    def test_02_empty_2b_file_is_true(self):
        my_file = list()
        get_match_odds_link_1 = self.base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_4.csv'
        my_file.append(get_match_odds_link_1)
        is_empty_file = self.empty_files(my_file)
        self.assertTrue(is_empty_file)

    def test_03_william_hill_view_as_200_and_refresh_no_is_1(self):
        request = self.factory.get(reverse('william_hill_4', args=[1]))
        response = William_Hill_Games_4.as_view()(request,1)
        self.assertEqual(response.status_code, 200)

    def test_04_empty_get_match_odds_link_2_file_is_false(self):
        file_link = self.base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_4.csv'
        get_file_size = self.check_file_not_empty(file_link)
        self.assertTrue(get_file_size)

    def test_05_empty_ids_for_tag_span_link_2_file_is_false(self):
        file_link = self.base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_4.csv'
        get_file_size = self.check_file_not_empty(file_link)
        self.assertTrue(get_file_size)
