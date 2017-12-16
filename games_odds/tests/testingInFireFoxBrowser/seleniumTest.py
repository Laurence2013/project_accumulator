import time
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestingFirefoxBrowser(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.baseUrl = 'http://sports.coral.co.uk/football'
        self.coralDailyGames = ['Todays matches', 'Tomorrow matches', '2017-12-13', '2017-12-14', '2017-12-15', 'Future matches']
        self.coralBookieName = 'Coral'

    def test_01_OpenFirefoxBrowser(self):
        title = 'Football Betting Odds | UK & International Odds | Coral'
        self.driver.get(self.baseUrl)
        self.assertEqual(title, self.driver.title)

    def test_02_ChangeFromFractionsToDecimal(self):
        self.driver.get(self.baseUrl)
        decimal = self.driver.find_element_by_id('site_pref_decimal')
        self.assertIsNotNone(decimal)

    def test_03_ClickOnDecimalLink(self):
        self.driver.get(self.baseUrl)
        decimal = self.driver.find_element_by_id('site_pref_decimal')
        decimal.click()
        team_name = self.driver.find_element(By.XPATH, '//div[@class="matches"]/div[8]//a/span').text
        self.assertEqual('AZ Alkmaar v Cambuur', team_name)

    def test_04_LoopingThroughAllDailyMatches(self):
        leagues = list()
        self.driver.get(self.baseUrl)
        decimal = self.driver.find_element_by_id('site_pref_decimal')
        decimal.click()
        leagues = self.driver.find_elements_by_class_name('block-title')
        for league in leagues:
            print(league.text)

    def test_05_LoopingThroughAllDailyMatchesInList(self):
        todays_league = list()
        self.driver.get(self.baseUrl)
        decimal = self.driver.find_element_by_id('site_pref_decimal')
        decimal.click()
        # leagues = self.driver.find_element(By.XPATH,'//div[@id="ob-evs-for-type-435"]/div[1]/div/span[2]').text
        leagues = self.driver.find_elements_by_class_name('featured-match')
        for league in leagues:
            todays_league.append(league.text)

        for today_league in todays_league:
            print(today_league)

    def test_06_ClickOnTomorrowsMatches(self):
        self.driver.get(self.baseUrl)
        tomorrowMatches = self.driver.find_element_by_id('feat-tomorrows')
        tomorrowMatches.click()

    def test_07_ClickOnFutureMatches(self):
        self.driver.get(self.baseUrl)
        futureMatches = self.driver.find_element_by_id('feat-future-dropdown')
        futureMatches.click()
        firstMatchDates = self.driver.find_element_by_id('2017-12-13')
        firstMatchDates.click()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()
