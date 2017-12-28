from django.test import TestCase
from games_odds.coral_base import Coral_Base

class IntegrationTest(TestCases):
    def test_01_GetCoralWebsiteTitle(self):
        title = 'Football Betting Odds | UK & International Odds | Coral'
        self.coral.initiateWebdriver()
        get_title = self.coral.get_website_title(self.coralUrl)
        self.coral.sleep_then_kill_browser()
        self.assertEqual(title, get_title)

    @patch.object(Coral_Base, 'get_website_title')
    def test_02_GettingWebsiteTitle(self, mock_get_website_title):
        mock_get_website_title.return_value = 'http://sports.coral.co.uk/football'
        get_url = self.coral.get_website_title(self.coralUrl)
        self.assertEqual(self.coralUrl, get_url)

    def test_06_getTomorrowsMatches(self):
        self.coral.initiateWebdriver()
        get_games = self.coral.get_tomorrows_matches(self.coralUrl)
        for game in get_games:
            print(game)
        self.coral.sleep_then_kill_browser()

    def test_07_getFutureMatches_a(self):
        self.coral.initiateWebdriver()
        get_games = self.coral.get_future_matches_a(self.coralUrl)
        for game in get_games:
            print(game)
        self.coral.sleep_then_kill_browser()

    def test_08_getFutureMatches_b(self):
        self.coral.initiateWebdriver()
        get_games = self.coral.get_future_matches_b(self.coralUrl)
        for game in get_games:
            print(game)
        self.coral.sleep_then_kill_browser()

    def test_09_getFutureMatches_c(self):
        self.coral.initiateWebdriver()
        get_games = self.coral.get_future_matches_c(self.coralUrl)
        for game in get_games:
            print(game)
        self.coral.sleep_then_kill_browser()

    def test_10_getFutureMatches_d(self):
        self.coral.initiateWebdriver()
        get_games = self.coral.get_future_matches_d(self.coralUrl)
        for game in get_games:
            print(game)
        self.coral.sleep_then_kill_browser()
