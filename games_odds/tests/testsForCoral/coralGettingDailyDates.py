from mock import Mock
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
        # action
        get_hello = self.coral.get_website_title(self.coralUrl)
        # assert
        self.assertEqual(self.coralUrl, get_hello)

    @patch.object(Coral_Base, 'get_website_title')
    def test_03_MockTestExample(self, mock_get_website_title):
        Coral_Base.get_website_title(self.coralUrl)
        mock_get_website_title.assert_called_with(self.coralUrl)

    def test_04_MockTestExample(self):
        self.coral.get_website_title = Mock()
        self.coral.get_website_title.return_value = self.coralUrl
        get_link = self.coral.get_website_title(self.coralUrl)
        self.assertEqual(self.coralUrl, get_link)
