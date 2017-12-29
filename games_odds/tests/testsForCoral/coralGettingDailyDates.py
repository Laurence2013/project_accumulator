from mock import Mock, patch
from django.test import TestCase
from games_odds.coral_base import Coral_Base

class CoralGettingDailyDates(TestCase):
    def setUp(self):
        self.coral = Coral_Base()
        self.coralUrl = 'http://sports.coral.co.uk/football'
        self.todays_matches = ['Todays Matches', 'Tomorrows Matches', '21st of Dec 2017', '22st of Dec 2017', '23st of Dec 2017', 'Future Matches']

    def test_01_GetCoralWebsiteTitle(self):
        title = 'Football Betting Odds | UK & International Odds | Coral'
        self.coral.get_website_title = Mock()
        self.coral.get_website_title.return_value = title
        get_title = self.coral.get_website_title(self.coralUrl)
        self.assertEqual(title, get_title)

    def test_02_GettingDailyMatchDates(self):
        self.coral.get_daily_match_dates = Mock()
        self.coral.get_daily_match_dates.return_value = self.todays_matches
        get_todays_matches = self.coral.get_daily_match_dates(self.todays_matches)
        self.assertEqual(self.todays_matches, get_todays_matches)

    def test_03_GettingDailyMatchDates(self):
        self.coral.get_daily_match_dates = Mock()
        self.coral.get_daily_match_dates.side_effect = self.todays_matches
        get_todays_matches = self.coral.get_daily_match_dates(self.todays_matches)
        self.assertEqual(self.todays_matches[0], get_todays_matches)
        get_todays_matches = self.coral.get_daily_match_dates(self.todays_matches)
        self.assertEqual(self.todays_matches[1], get_todays_matches)
        get_todays_matches = self.coral.get_daily_match_dates(self.todays_matches)
        self.assertEqual(self.todays_matches[2], get_todays_matches)

    def test_04_GetTodaysMatches(self):
        todays_matches_list = ['', '', '', '', 'Today 7:45pm\nLIVE\nChelsea v Bournemouth\n1.28\n5.50\n10.00\n+169', 'Today 8:00pm\nLIVE\nBristol City v Man Utd\n6.00\n4.20\n1.53\n+173']
        self.coral.get_todays_matches = Mock()
        self.coral.get_todays_matches.return_value = todays_matches_list
        get_games = self.coral.get_todays_matches(self.coralUrl)
        self.assertEqual(todays_matches_list, get_games)

    def test_05_GetTomorrowsMatches(self):
        tomorrows_match_list = ['', '', 'Fri 7:45pm\nLIVE\nCardiff v Preston\n2.10\n3.25\n3.70\n+171', 'Fri 7:45pm\nLIVE\nMillwall v QPR\n2.10\n3.30\n3.60\n+167', 'Fri 7:45pm\nLIVE\nDoncaster v Rochdale\n2.15\n3.30\n3.50\n+167']
        self.coral.get_tomorrows_matches = Mock()
        self.coral.get_tomorrows_matches.return_value = tomorrows_match_list
        get_games = self.coral.get_tomorrows_matches(self.coralUrl)
        self.assertEqual(tomorrows_match_list, get_games)

    def test_06_GetFutureMatches_a(self):
        future_matches_a = ['', '', 'Sat 3:00pm\nLIVE\nHuddersfield v Burnley\n2.35\n2.90\n3.40\n+171', 'Sat 3:00pm\nLIVE\nLiverpool v Leicester\n1.30\n5.50\n10.00\n+170', 'Sat 3:00pm\nLIVE\nNewcastle v Brighton\n2.10\n3.10\n3.80\n+167', 'Sat 3:00pm\nLIVE\nWatford v Swansea\n1.67\n3.60\n5.50\n+167']
        self.coral.get_future_matches_a = Mock()
        self.coral.get_future_matches_a.return_value = future_matches_a
        get_games = self.coral.get_future_matches_a(self.coralUrl)
        self.assertEqual(future_matches_a, get_games)

    def test_07_GetFutureMatches_b(self):
        future_matches_b = ['', '', 'Sun 12:00pm\nLIVE\nCrystal Palace v Man City\n11.00\n5.80\n1.25\n+167', 'Sun 4:30pm\nLIVE\nWest Brom v Arsenal\n4.50\n3.70\n1.75\n+167', 'Sun 8:00am\nLIVE\nCentral Coast Mariners v Wellington Phoenix\n1.80\n3.50\n3.80\n+149']
        self.coral.get_future_matches_b = Mock()
        self.coral.get_future_matches_b.return_value = future_matches_b
        get_games = self.coral.get_future_matches_b(self.coralUrl)
        self.assertEqual(future_matches_b, get_games)

    def test_08_GetFutureMatches_c(self):
        future_matches_c = ['', '', 'Mon 12:00pm\nLIVE\nCrystal Palace v Man City\n11.00\n5.80\n1.25\n+167', 'Sun 4:30pm\nLIVE\nWest Brom v Arsenal\n4.50\n3.70\n1.75\n+167', 'Sun 8:00am\nLIVE\nCentral Coast Mariners v Wellington Phoenix\n1.80\n3.50\n3.80\n+149']
        self.coral.get_future_matches_c = Mock()
        self.coral.get_future_matches_c.return_value = future_matches_c
        get_games = self.coral.get_future_matches_c(self.coralUrl)
        self.assertEqual(future_matches_c, get_games)

    def test_09_GetFutureMatches_d(self):
        future_matches_d = ['', '', 'Tue 12:00pm\nLIVE\nCrystal Palace v Man City\n11.00\n5.80\n1.25\n+167', 'Sun 4:30pm\nLIVE\nWest Brom v Arsenal\n4.50\n3.70\n1.75\n+167', 'Sun 8:00am\nLIVE\nCentral Coast Mariners v Wellington Phoenix\n1.80\n3.50\n3.80\n+149']
        self.coral.get_future_matches_d = Mock()
        self.coral.get_future_matches_d.return_value = future_matches_d
        get_games = self.coral.get_future_matches_d(self.coralUrl)
        self.assertEqual(future_matches_d, get_games)

    @patch('games_odds.coral_base.webdriver')
    def test_10_TestingWebDriverFirefox(self, mock_webDriver):
        self.coral.initiateWebdriver()
        mock_webDriver.Firefox.assert_called_once()

    @patch('games_odds.coral_base.webdriver.Firefox')
    def test_11_TestingWebDriverUrl(self, mock_website):
        self.coral.initiateWebdriver()
        self.coral.get_website_title(self.coralUrl)
        mock_website.assert_called()
