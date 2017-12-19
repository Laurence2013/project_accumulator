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
        todays_matches = ['Todays Matches', 'Tomorrows Matches']
        self.coral.get_daily_match_dates = Mock()
        self.coral.get_daily_match_dates.return_value = todays_matches
        get_todays_matches = self.coral.get_daily_match_dates(todays_matches)
        self.assertEqual(todays_matches, get_todays_matches)

    def test_04_GettingDailyMatchDates(self):
        self.coral.initiateWebdriver()
        get_matches = self.coral.get_daily_match_dates(self.coralUrl)
        self.coral.sleep_then_kill_browser()
        print()
        for match in get_matches:
            print(match)
