from selenium import webdriver

class Coral_Base:
    todays_matches_list = list()

    def _webdriver_firefox(self):
        driver = webdriver.Firefox()
        return driver

    def _base_url(self):
        baseUrl = 'http://sports.coral.co.uk/football'
        return baseUrl

    # Get todays matches
    def get_todays_matches(self):
        driver = self._webdriver_firefox()
        driver.get(self._base_url())
        change_to_decimal = driver.find_element_by_id('site_pref_decimal')
        change_to_decimal.click()
        daily_featured_matches = driver.find_elements_by_class_name('featured-match')

        for d_matches in daily_featured_matches:
            self.todays_matches_list.append(d_matches.text)

        driver.close()

    def get_todays_matches_list(self):
        return self.todays_matches_list

    # Get tomorrows matches
    # Get future matches a
    # Get future matches b
    # Get future matches c
    # Get future matches d
