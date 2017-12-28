from mock import Mock
from mock import MagicMock
from mock import patch
from django.test import TestCase
from SampleCodes.PracticeMocks.coral_base import Coral_Base

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

    def test_05_MockTestExampleSideEffects(self):
        listNum = [5,4,3,2,1]
        self.coral.test_mock_iteratble = Mock()
        self.coral.test_mock_iteratble.side_effect = listNum
        myNum = self.coral.test_mock_iteratble(listNum)
        self.assertEqual(5, myNum)
        myNum = self.coral.test_mock_iteratble(listNum)
        self.assertEqual(4, myNum)
        myNum = self.coral.test_mock_iteratble(listNum)
        self.assertEqual(3, myNum)

    def test_06_MockTestExampleReturnValue(self):
        listNum = [5,4,3,2,1]
        self.coral.test_mock_iteratble = Mock()
        self.coral.test_mock_iteratble.return_value = listNum
        myNum = self.coral.test_mock_iteratble(listNum)
        self.assertEqual([5,4,3,2,1], myNum)
        myNum = self.coral.test_mock_iteratble(listNum)

    def test_07_GettingDailyMatchDates(self):
        self.coral.initiateWebdriver()
        get_matches = self.coral.get_daily_match_dates(self.coralUrl)
        self.coral.sleep_then_kill_browser()
        print()
        for match in get_matches:
            print(match)

    @patch("games_odds.coral_base.Coral_Base.initiateWebdriver")
    def test_13_testing(self, mock_webDriverFirefox):
        self.coral.initiateWebdriver.testM.testN()
        self.assertEqual(mock_webDriverFirefox.testM.testN.call_count, 1)

    # This is how you mock a class
    @patch("games_odds.coral_base.Coral_Base")
    def test_11_testing(self, someClass):
        self.assertEqual(someClass, someClass)

    @patch('games_odds.coral_base.Coral_Base.get_website_title')
    def test_12_TestingWebDriverUrl(self, mock_webDriver_url):
        self.coral.get_website_title.return_value = self.coralUrl
        get_title = self.coral.get_website_title(self.coralUrl)
        self.assertEqual(self.coralUrl, get_title)

    @patch('games_odds.coral_base.Coral_Base.test')
    def test_13_TestingWebDriverUrl(self, mock_site):
        print()
        print(mock_site)
        self.coral.test.return_value = 'hello2'
        print(self.coral.test())
        # self.coral.get_website_title(self.coralUrl)
        mock_site.assert_called()

    @patch.object(Coral_Base, 'get_website_title')
    def test_02_GettingWebsiteTitle(self, mock_get_website_title):
        mock_get_website_title.return_value = 'http://sports.coral.co.uk/football'
        get_url = self.coral.get_website_title(self.coralUrl)
        self.assertEqual(self.coralUrl, get_url)
