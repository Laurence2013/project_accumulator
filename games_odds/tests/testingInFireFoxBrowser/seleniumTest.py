from django.test import TestCase
from selenium import webdriver

class testingFirefoxBrowser(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_01_runFirefoxBrowser(self):
        self.driver.get('http://www.google.com')
        self.assertEqual('Google', self.driver.title)

    def tearDown(self):
        self.driver.close()
