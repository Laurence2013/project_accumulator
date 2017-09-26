from django.test import TestCase
from django.conf import settings
from games_odds.views import William_Hill_Games_1
from games_odds.mainViewsApi.main_views_api import MainViewsApi

'''
This is testing no 4b
This is testing the refresh_no sent, sending 1 and get_match_odds_link_1.csv, ids_for_tag_span_link_1 and ids_for_tag_tbody_link_1 are not empty after refresh
'''

class TestingWilliamHillCsvFileIsTrueAfterRefresh3(TestCase, MainViewsApi):
    def setUp(self):
        self.base_dir = settings.BASE_DIR

    def test_empty_get_match_odds_link_1_file_is_false(self):
        file_link = self.base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_1.csv'
        get_file_size = self.check_file_not_empty(file_link)
        self.assertTrue(get_file_size)

    def test_empty_ids_for_tag_span_link_1_file_is_false(self):
        file_link = self.base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_1.csv'
        get_file_size = self.check_file_not_empty(file_link)
        self.assertTrue(get_file_size)

    def test_empty_ids_for_tag_tbody_link_1_file_is_false(self):
        file_link = self.base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_1.csv'
        get_file_size = self.check_file_not_empty(file_link)
        self.assertTrue(get_file_size)
