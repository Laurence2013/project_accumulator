from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from django.test.client import RequestFactory
from games_odds.views import William_Hill_Games_0
from games_odds.mainViewsApi.main_views_api import MainViewsApi
from games_odds.william_hill_base import WilliamHillBase
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill

'''
This is testing no 2b
This is testing the refresh_no sent, sending 1 and get_match_odds_link_0.csv is not empty after refresh
'''

class TestingWilliamHillCsvFileIsTrueAfterRefresh0(TestCase, MainViewsApi, WilliamHillBase, ScrapingWilliamHill):
    def setUp(self):
        self.factory = RequestFactory()
        self.base_dir = settings.BASE_DIR

    def test_william_hill_view_as_200_and_refresh_no_is_1(self):
        request = self.factory.get(reverse('william_hill_0', args=[1]))
        response = William_Hill_Games_0.as_view()(request,1)
        self.assertEqual(response.status_code, 200)

    def test_empty_1_file_is_false(self):
        file_link = self.base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_0.csv'
        get_file_size = self.check_file_not_empty(file_link)
        self.assertTrue(get_file_size)
