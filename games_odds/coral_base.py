import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from xvfbwrapper import Xvfb

class Coral_Base:
    display = Xvfb()
    display.start()

    def initiateWebdriver(self):
        self.driver = webdriver.Firefox()

    def get_website_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def get_daily_match_dates(self, url):
        daily_match_dates = list()
        self.driver.get(url)
        daily_match_dates.append(self.driver.find_element(By.XPATH, '//div[@id="feat-todays"]').text)
        daily_match_dates.append(self.driver.find_element(By.XPATH, '//div[@id="feat-tomorrows"]').text)
        click_on_future_matches = self.driver.find_element_by_id('feat-future-dropdown')
        click_on_future_matches.click()

        for n in range(1,5):
            daily_match_dates.append(self.driver.find_element(By.XPATH, '//div[@id="ob-all-matches-content"]/div[1]/div[1]/ul/li['+ str(n) +']/a').text)
        return daily_match_dates

    def get_todays_matches(self, url):
        todays_matches_list = list()
        self.driver.get(url)
        change_to_decimal = self.driver.find_element_by_id('site_pref_decimal')
        change_to_decimal.click()
        daily_featured_matches = self.driver.find_elements_by_class_name('featured-match')

        for d_matches in daily_featured_matches:
            todays_matches_list.append(d_matches.text)
        return todays_matches_list

    # Get tomorrows matches
    # Get future matches a
    # Get future matches b
    # Get future matches c
    # Get future matches d

    def sleep_then_kill_browser(self):
        time.sleep(1)
        self.driver.close()
