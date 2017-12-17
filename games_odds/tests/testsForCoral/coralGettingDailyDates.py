from django.test import TestCase
from games_odds.coral_base import Coral_Base

class CoralGettingDailyDates(TestCase):
    def setUp(self):
        self.coral = Coral_Base()

    def test_01_GetCoralWebsiteTitle(self):
        title = 'Football Betting Odds | UK & International Odds | Coral'
        get_title = self.coral.get_website_title('http://sports.coral.co.uk/football')
        self.coral.sleep_then_kill_browser()
        self.assertEqual(title, get_title)
