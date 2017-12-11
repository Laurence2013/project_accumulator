import time
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestingFirefoxBrowser(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.baseUrl = 'http://sports.coral.co.uk/football'

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
        print(team_name)

    # Here how to loop through a list of elements

    def tearDown(self):
        time.sleep(3)
        self.driver.close()
