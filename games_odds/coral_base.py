import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from xvfbwrapper import Xvfb

class Coral_Base:
    todays_matches_list = list()
    display = Xvfb()
    display.start()

    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_website_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def get_daily_match_dates(self):
        pass

    def sleep_then_kill_browser(self):
        time.sleep(1)
        self.driver.close()

    # Get todays matches
    # def get_todays_matches(self):
    #     driver = self._webdriver_firefox()
    #     driver.get(self._base_url())
    #     change_to_decimal = driver.find_element_by_id('site_pref_decimal')
    #     change_to_decimal.click()
    #     daily_featured_matches = driver.find_elements_by_class_name('featured-match')
    #
    #     for d_matches in daily_featured_matches:
    #         self.todays_matches_list.append(d_matches.text)
    #
    #     driver.close()
    #
    # def get_todays_matches_list(self):
    #     return self.todays_matches_list

    # Get tomorrows matches
    # Get future matches a
    # Get future matches b
    # Get future matches c
    # Get future matches d
