from django.test import TestCase
from django.urls import reverse
from django.test.client import RequestFactory
from games_odds.views import William_Hill_Games_0
from games_odds.william_hill_base import WilliamHillBase

class testingWilliamHillGame0(TestCase, WilliamHillBase):
    def setUp(self):
        self.factory = RequestFactory()

'''
This is the 1st part of the test, this is to test the refresh_no. Either 0 or 1. 0 get current games and odds and 1 as refresh by getting games and odds
'''

    def test_william_hill_view_as_200_and_refresh_no_is_0(self):
        request = self.factory.get(reverse('william_hill_0', args=[0]))
        response = William_Hill_Games_0.as_view()(request,0)
        self.assertEqual(response.status_code, 200)

    def test_william_hill_view_as_200_and_refresh_no_is_1(self):
        request = self.factory.get(reverse('william_hill_0', args=[1]))
        response = William_Hill_Games_0.as_view()(request,1)
        self.assertEqual(response.status_code, 200)

    def test_william_hill_view_as_200_and_refresh_no_is_2(self):
        request = self.factory.get(reverse('william_hill_0', args=[2]))
        response = William_Hill_Games_0.as_view()(request,2)
        self.assertEqual(response.status_code, 200)

    def test_william_hill_view_as_200_and_refresh_no_is_3(self):
        request = self.factory.get(reverse('william_hill_0', args=[3]))
        response = William_Hill_Games_0.as_view()(request,3)
        self.assertEqual(response.status_code, 200)

    def test_get_current_url_and_date(self):
        get_date = self.get_date('william_hill_0')
        print(get_date)
'''
This is the 2nd part of the test, this is to test the url name wether william_hill_0 or william_hill_1
'''
