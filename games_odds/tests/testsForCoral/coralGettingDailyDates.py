from mock import Mock
from mock import MagicMock
from mock import patch
from django.test import TestCase
from games_odds.coral_base import Coral_Base

class CoralGettingDailyDates(TestCase):
    def setUp(self):
        self.coral = Coral_Base()
        self.coralUrl = 'http://sports.coral.co.uk/football'
        self.todays_matches = ['Todays Matches', 'Tomorrows Matches', '21st of Dec 2017', '22st of Dec 2017', '23st of Dec 2017', 'Future Matches']

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
        self.coral.get_daily_match_dates = Mock()
        self.coral.get_daily_match_dates.return_value = self.todays_matches
        get_todays_matches = self.coral.get_daily_match_dates(self.todays_matches)
        self.assertEqual(self.todays_matches, get_todays_matches)

    def test_04_GettingDailyMatchDates(self):
        self.coral.get_daily_match_dates = Mock()
        self.coral.get_daily_match_dates.side_effect = self.todays_matches
        get_todays_matches = self.coral.get_daily_match_dates(self.todays_matches)
        self.assertEqual(self.todays_matches[0], get_todays_matches)
        get_todays_matches = self.coral.get_daily_match_dates(self.todays_matches)
        self.assertEqual(self.todays_matches[1], get_todays_matches)
        get_todays_matches = self.coral.get_daily_match_dates(self.todays_matches)
        self.assertEqual(self.todays_matches[2], get_todays_matches)

    def test_05_getTodaysMatches(self):
        # self.coral.initiateWebdriver()
        todays_matches_list = ['', '', '', '', 'Today 7:45pm\nLIVE\nChelsea v Bournemouth\n1.28\n5.50\n10.00\n+169', 'Today 8:00pm\nLIVE\nBristol City v Man Utd\n6.00\n4.20\n1.53\n+173']
        self.coral.get_todays_matches = Mock()
        self.coral.get_todays_matches.return_value = todays_matches_list
        get_games = self.coral.get_todays_matches(self.coralUrl)
        # print(get_games)
        # self.coral.sleep_then_kill_browser()
        self.assertEqual(todays_matches_list, get_games)

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
