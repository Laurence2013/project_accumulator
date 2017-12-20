from mock import Mock
from mock import MagicMock
from mock import patch
from django.test import TestCase
from games_odds.coral_base import Coral_Base

class CoralGettingDailyDates(TestCase):
    def setUp(self):
        self.coral = Coral_Base()
        self.coralUrl = 'http://sports.coral.co.uk/football'

    def test_01_GetCoralWebsiteTitle(self):
        title = 'Football Betting Odds | UK & International Odds | Coral'
        self.coral.initiateWebdriver()
        get_title = self.coral.get_website_title(self.coralUrl)
        self.coral.sleep_then_kill_browser()
        self.assertEqual(title, get_title)

    @patch.object(Coral_Base, 'get_website_title')
    def test_02_MockTestExample(self, mock_get_website_title):
        mock_get_website_title.return_value = 'http://sports.coral.co.uk/football'
        get_url = self.coral.get_website_title(self.coralUrl)
        self.assertEqual(self.coralUrl, get_url)

    def test_03_GettingDailyMatchDates(self):
        todays_matches = ['Todays Matches', 'Tomorrows Matches', '21st of Dec 2017', '22st of Dec 2017', '23st of Dec 2017', 'Future Matches']
        self.coral.get_daily_match_dates = Mock()
        self.coral.get_daily_match_dates.return_value = todays_matches
        get_todays_matches = self.coral.get_daily_match_dates(todays_matches)
        self.assertEqual(todays_matches, get_todays_matches)

    def test_04_GettingDailyMatchDates(self):
        todays_matches = ['Todays Matches', 'Tomorrows Matches', '21st of Dec 2017', '22st of Dec 2017', '23st of Dec 2017', 'Future Matches']
        self.coral.get_daily_match_dates = Mock()
        self.coral.get_daily_match_dates.side_effect = todays_matches
        get_todays_matches = self.coral.get_daily_match_dates(todays_matches)
        self.assertEqual(todays_matches[0], get_todays_matches)
        get_todays_matches = self.coral.get_daily_match_dates(todays_matches)
        self.assertEqual(todays_matches[1], get_todays_matches)
        get_todays_matches = self.coral.get_daily_match_dates(todays_matches)
        self.assertEqual(todays_matches[2], get_todays_matches)

    def test_05_getTodaysMatches(self):
        self.coral.initiateWebdriver()
        get_games = self.coral.get_todays_matches(self.coralUrl)
        for game in get_games:
            print(game)
        self.coral.sleep_then_kill_browser()

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
