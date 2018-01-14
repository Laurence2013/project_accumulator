import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from xvfbwrapper import Xvfb
from accumulator.models import *
from games_odds.sorting_matches_coral import SortingMatchesInCoral
from django.core.serializers.json import DjangoJSONEncoder

class Coral_Base:
    # display = Xvfb()
    # display.start()

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

    def get_tomorrows_matches(self, url):
        tomorrow_matches_list = list()
        self.driver.get(url)
        change_to_decimal = self.driver.find_element_by_id('site_pref_decimal')
        time.sleep(5)
        change_to_decimal.click()
        time.sleep(5)
        feat_tomorrows = self.driver.find_element_by_id('feat-tomorrows')
        time.sleep(5)
        feat_tomorrows.click()
        time.sleep(5)
        tomorrows_feat_matches = self.driver.find_elements_by_class_name('featured-match')

        for t_matches in tomorrows_feat_matches:
            tomorrow_matches_list.append(t_matches.text)
        return tomorrow_matches_list

    def get_future_matches_a(self, url):
        future_matches_a_list = list()
        self.driver.get(url)
        change_to_decimal = self.driver.find_element_by_id('site_pref_decimal')
        time.sleep(5)
        change_to_decimal.click()
        time.sleep(5)
        feat_tomorrows = self.driver.find_element_by_id('feat-future-dropdown')
        time.sleep(5)
        feat_tomorrows.click()
        time.sleep(5)
        future_a_features = self.driver.find_element(By.XPATH, '//ul[@class="next-matches-dropdown"]/li[1]//a')
        time.sleep(5)
        future_a_features.click()
        time.sleep(5)
        future_matches_a = self.driver.find_elements_by_class_name('featured-match')

        for f_a_matches in future_matches_a:
            future_matches_a_list.append(f_a_matches.text)
        return future_matches_a_list

    def get_future_matches_b(self, url):
        future_matches_b_list = list()
        self.driver.get(url)
        change_to_decimal = self.driver.find_element_by_id('site_pref_decimal')
        time.sleep(5)
        change_to_decimal.click()
        time.sleep(5)
        feat_tomorrows = self.driver.find_element_by_id('feat-future-dropdown')
        time.sleep(5)
        feat_tomorrows.click()
        time.sleep(5)
        future_b_features = self.driver.find_element(By.XPATH, '//ul[@class="next-matches-dropdown"]/li[2]//a')
        time.sleep(5)
        future_b_features.click()
        time.sleep(5)
        future_matches_b = self.driver.find_elements_by_class_name('featured-match')

        for f_b_matches in future_matches_b:
            future_matches_b_list.append(f_b_matches.text)
        return future_matches_b_list

    def get_future_matches_c(self, url):
        future_matches_c_list = list()
        self.driver.get(url)
        change_to_decimal = self.driver.find_element_by_id('site_pref_decimal')
        time.sleep(5)
        change_to_decimal.click()
        time.sleep(5)
        feat_tomorrows = self.driver.find_element_by_id('feat-future-dropdown')
        time.sleep(5)
        feat_tomorrows.click()
        time.sleep(5)
        future_c_features = self.driver.find_element(By.XPATH, '//ul[@class="next-matches-dropdown"]/li[3]//a')
        time.sleep(5)
        future_c_features.click()
        time.sleep(5)
        future_matches_c = self.driver.find_elements_by_class_name('featured-match')

        for f_c_matches in future_matches_c:
            future_matches_c_list.append(f_c_matches.text)
        return future_matches_c_list

    def get_future_matches_d(self, url):
        future_matches_d_list = list()
        self.driver.get(url)
        change_to_decimal = self.driver.find_element_by_id('site_pref_decimal')
        time.sleep(5)
        change_to_decimal.click()
        time.sleep(5)
        feat_tomorrows = self.driver.find_element_by_id('feat-future-dropdown')
        time.sleep(5)
        feat_tomorrows.click()
        time.sleep(5)
        future_d_features = self.driver.find_element(By.XPATH, '//ul[@class="next-matches-dropdown"]/li[4]//a')
        time.sleep(5)
        future_d_features.click()
        time.sleep(5)
        future_matches_d = self.driver.find_elements_by_class_name('featured-match')

        for f_d_matches in future_matches_d:
            future_matches_d_list.append(f_d_matches.text)
        return future_matches_d_list

    def sleep_then_kill_browser(self):
        time.sleep(1)
        self.driver.close()

    def get_coral_match_day_games(self, coral_db_match_list, coral_db_odds_list, matchday_games_id, coral_json):
        if coral_db_match_list.objects.count() >= 1 and coral_db_odds_list.objects.count() >= 1:
            get_todays_matches_dict = dict()
            get_match_day_dates = CoralDailyMatche.objects.values_list('dates_of_games', flat = True).get(dates_id = matchday_games_id)
            get_odds = coral_db_odds_list.objects.values_list('match', 'home_odds', 'draw_odds', 'away_odds')
            get_games = coral_db_match_list.objects.values_list('id','games')
            adjust_matches_1 = get_match_day_dates.replace("'", "")
            adjust_matches_2 = adjust_matches_1.replace(" ","_")

            for each_odds in range(0, len(get_odds)):
                if get_odds[each_odds][0] == get_games[each_odds][0]:
                    get_todays_matches_dict[each_odds] = [get_games[each_odds][1], get_odds[each_odds][1], get_odds[each_odds][2], get_odds[each_odds][3]]

            s = json.dumps(get_todays_matches_dict, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
            with open(self.base_dir + coral_json, "w") as f:
                f.write(s)

            return adjust_matches_2
        return None

    def save_coral_matches_and_odds(self, coral_db_match_list, coral_db_odds_list, matchday_games_id, coral_url):
        sorting_matches = SortingMatchesInCoral()
        coral_db_match_list.objects.all().delete()
        coral_db_odds_list.objects.all().delete()
        get_matches_1 = list()
        get_odds_1 = list()
        self.initiateWebdriver()
        get_games = self.__daily_matches_func_name(matchday_games_id, coral_url)
        self.sleep_then_kill_browser()
        get_todays_games_2 = sorting_matches.sorting_each_games_data(get_games)
        get_odds = sorting_matches.seperating_odds(get_todays_games_2)
        get_matches = sorting_matches.seperating_games(get_todays_games_2)
        get_match_day_id = CoralDailyMatche.objects.values_list('id', flat = True).get(dates_id = matchday_games_id)
        get_match_day_dates = CoralDailyMatche.objects.values_list('dates_of_games', flat = True).get(dates_id = matchday_games_id)
        get_match_id = coral_db_match_list.objects.values_list('id', flat = True)

        for each_match in get_matches:
            get_matches_1.append(' '.join(each_match))

        for each_odds in range(0, len(get_odds)):
            home = get_odds[each_odds][0]
            draw = get_odds[each_odds][1]
            away = get_odds[each_odds][2]
            odds = [float(home), float(draw), float(away)]
            get_odds_1.append(odds)

        for each_matches in get_matches_1:
            save_each_match = coral_db_match_list(games = each_matches, match_day_id_id = get_match_day_id)
            save_each_match.save()

        count = 0
        for each_odds in range(0, len(get_odds_1)):
            get_odds_1[each_odds].append(get_match_id[count])
            count += 1

        for each_odds in get_odds_1:
            save_each_odds = coral_db_odds_list(home_odds = each_odds[0], draw_odds = each_odds[1], away_odds = each_odds[2], match_id = each_odds[3], games_id = get_match_day_id)
            save_each_odds.save()

        return get_match_day_dates

    def __daily_matches_func_name(self, matchday_games_id, coral_url):
        if int(matchday_games_id) is 1:
            return self.get_todays_matches(coral_url)
        if int(matchday_games_id) is 2:
            return self.get_tomorrows_matches(coral_url)
        if int(matchday_games_id) is 3:
            return self.get_future_matches_a(coral_url)
        if int(matchday_games_id) is 4:
            return self.get_future_matches_b(coral_url)
