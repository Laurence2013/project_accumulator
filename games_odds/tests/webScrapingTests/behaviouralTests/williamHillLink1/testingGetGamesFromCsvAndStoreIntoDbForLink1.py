import shutil
from django.test import TestCase
from django.conf import settings
from games_odds.models import WilliamHillCsvLinks
from games_odds.models import WilliamHillGames1
from games_odds.save_games_into_db import SaveGamesIntoDb
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch

'''
This is 2nd scenario, if user or admin clicked on link_1 then the csv file for games or matches is checked in database:
1 - ids_for_tag_span_link_1.csv checked with the csv file ids_for_tag_span_link_1.csv which is stored in tag_name_span_attr_ids folder
2 - Open get_match_odds_link_1.csv and start looping each games and stored into list or tuple
3 - Each game in list or tuple is saved into db = WilliamHillGames1
'''

class TestingGetGamesFromCsvAndStoreIntoDbForLink1(TestCase, SaveGamesIntoDb, CombineOddsWithItsMatch):
    def setUp(self):
        WilliamHillCsvLinks.objects.create(id=2,
        url_name = str('link_1'), get_match_odds_link_csv = str('get_match_odds_link_1.csv'), ids_for_tag_span_link_csv = str('ids_for_tag_span_link_1.csv'), ids_for_tag_tbody_link_csv = str('ids_for_tag_tbody_link_1.csv'))

    def test_01_copy_ids_for_tag_span_link_1_to_testingFile_folder(self):
        base_dir = settings.BASE_DIR
        save_to_testing_files = base_dir + "/games_odds/tests/webScrapingTests/testingFiles/"
        shutil.copy(base_dir + "/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_1.csv", save_to_testing_files)

    def test_02_check_link_1_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_1'))
        self.assertEqual(str('link_1'), get_url.url_name)

    def test_03_check_ids_for_tag_span_link_csv_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_1'))
        self.assertEqual(str('ids_for_tag_span_link_1.csv'), get_url.ids_for_tag_span_link_csv)

    def test_04_check_that_ids_for_tag_span_link_1_csv_is_stored_in_tag_name_span_attr_ids_folder(self):
        base_dir = settings.BASE_DIR
        ids_for_tag_span_link_1 = self.check_db_csv_name_with_csv_file(str('link_1'))
        self.assertEqual(base_dir + "/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_1.csv", ids_for_tag_span_link_1)

    def test_05_check_both_csv_files_ids_for_tag_span_link_1_is_the_same(self):
        base_dir = settings.BASE_DIR
        get_testing_files = base_dir + "/games_odds/tests/webScrapingTests/testingFiles/ids_for_tag_span_link_1.csv"
        get_testing_files_matches = self.get_match(get_testing_files)
        get_testing_files_list_of_matches = self.store_csv_files_into_list(get_testing_files_matches)

        get_ids_for_tag_span_link_1 = self.get_games_from_csv_file(str('link_1'))
        get_ids_for_tag_span_link_1_list = self.store_csv_files_into_list(get_ids_for_tag_span_link_1)
        self.assertListEqual(get_testing_files_list_of_matches, get_ids_for_tag_span_link_1_list)

    def test_06_store_list_of_matches_into_db(self):
        get_ids_for_tag_span_link_1 = self.get_games_from_csv_file(str('link_1'))
        get_ids_for_tag_span_link_1_list = self.store_csv_files_into_list(get_ids_for_tag_span_link_1)
        store_tag_span_link_1_list = WilliamHillGames1(games=get_ids_for_tag_span_link_1_list, url_game_link_id=2)
        store_tag_span_link_1_list.save()
        tag_span_game_list = list(store_tag_span_link_1_list.games)
        self.assertGreater(len(tag_span_game_list), 0)
