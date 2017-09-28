from django.test import TestCase
from django.urls import reverse
from django.test.client import RequestFactory
from games_odds.views import William_Hill_Games_1
from games_odds.william_hill_base import WilliamHillBase
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill

'''
This is testing no 1
This is testing the refresh_no sent, 1 is to refresh and get all games and odds
0 is to just get the current csv files in system
2 and 3 are doing nothing
'''

class TestingWilliamHillGame1(TestCase, WilliamHillBase, ScrapingWilliamHill):
    def setUp(self):
        self.factory = RequestFactory()

    def test_william_hill_view_as_200_and_refresh_no_is_0(self):
        request = self.factory.get(reverse('william_hill_1', args=[0]))
        response = William_Hill_Games_1.as_view()(request,0)
        self.assertEqual(response.status_code, 200)

    def test_william_hill_view_as_200_and_refresh_no_is_1(self):
        request = self.factory.get(reverse('william_hill_1', args=[1]))
        response = William_Hill_Games_1.as_view()(request,1)
        self.assertEqual(response.status_code, 200)

    def test_william_hill_view_as_200_and_refresh_no_is_2(self):
        request = self.factory.get(reverse('william_hill_1', args=[2]))
        response = William_Hill_Games_1.as_view()(request,2)
        self.assertEqual(response.status_code, 200)

    def test_william_hill_view_as_200_and_refresh_no_is_3(self):
        request = self.factory.get(reverse('william_hill_1', args=[3]))
        response = William_Hill_Games_1.as_view()(request,3)
        self.assertEqual(response.status_code, 200)
