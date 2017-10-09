import shutil
from django.test import TestCase
from django.conf import settings
from games_odds.models import WilliamHillCsvLinks
from games_odds.models import WilliamHillOdds0
from games_odds.save_odds_into_db import SaveOddsIntoDb
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb

'''
This is the 3rd scenario, if user or admin clicked on link_0, then the csv file for ODDS is checked in database:
1 - get_match_odds_link_0.csv checkd with the file get_match_odds_link_0.csv which is store in get_match_odds folder
2 - Open get_match_odds_link_0.csv and start looping each odds and store into list or tuple
3 - Each odds in list or tuple is saved into db = WilliamHillOdds0
'''

class TestingGetOddsFromCsvAndStoreIntoDbForLink0(TestCase, SaveOddsIntoDb, CombineOddsWithItsMatch, DecimalToFractionAndStoreInDb):
    def setUp(self):
        WilliamHillCsvLinks.objects.create(id=1,
        url_name = str('link_0'), get_match_odds_link_csv = str('get_match_odds_link_0.csv'), ids_for_tag_span_link_csv = str('ids_for_tag_span_link_0.csv'), ids_for_tag_tbody_link_csv = str('ids_for_tag_tbody_link_0.csv'))

    def test_01_copy_get_match_odds_link_0_to_testingFile_folder(self):
        base_dir = settings.BASE_DIR
        save_to_testing_files = base_dir + "/games_odds/tests/webScrapingTests/testingFiles/"
        shutil.copy(base_dir + "/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_0.csv", save_to_testing_files)

    def test_02_check_link_0_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_0'))
        self.assertEqual(str('link_0'), get_url.url_name)

    def test_03_check_get_match_odds_link_csv_is_in_db(self):
        get_odds = WilliamHillCsvLinks.objects.get(url_name=str('link_0'))
        self.assertEqual(str('get_match_odds_link_0.csv'), get_odds.get_match_odds_link_csv)

    def test_04_check_that_get_match_odds_link_0_csv_is_stored_in_get_match_odds_folder(self):
        base_dir = settings.BASE_DIR
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        self.assertEqual(base_dir + "/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_0.csv", get_match_odds_link_0)

    def test_05_check_both_csv_files_get_match_odds_link_0_is_the_same(self):
        base_dir = settings.BASE_DIR
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_0)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        self.assertIsInstance(convert_fraction_to_decimal_2[0][0], float)

    def test_06_check_both_csv_files_get_match_odds_link_0_is_the_same(self):
        base_dir = settings.BASE_DIR
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_0)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        self.assertIsInstance(convert_fraction_to_decimal_2[0][1], float)

    def test_07_check_both_csv_files_get_match_odds_link_0_is_the_same(self):
        base_dir = settings.BASE_DIR
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_0)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        self.assertIsInstance(convert_fraction_to_decimal_2[0][2], float)

    def test_08_check_both_csv_files_get_match_odds_link_0_is_the_same(self):
        base_dir = settings.BASE_DIR
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_0)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        self.assertIsInstance(convert_fraction_to_decimal_2[1][0], float)

    def test_09_check_both_csv_files_get_match_odds_link_0_is_the_same(self):
        base_dir = settings.BASE_DIR
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_0)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        self.assertIsInstance(convert_fraction_to_decimal_2[1][1], float)

    def test_10_check_both_csv_files_get_match_odds_link_0_is_the_same(self):
        base_dir = settings.BASE_DIR
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_0)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        self.assertIsInstance(convert_fraction_to_decimal_2[1][2], float)

    def test_11_store_list_of_matches_into_db(self):
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_0)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        store_odds_into_db = WilliamHillOdds0(home_odds=convert_fraction_to_decimal_2[0][0], draw_odds=convert_fraction_to_decimal_2[0][1], away_odds=convert_fraction_to_decimal_2[0][2], games_id=1)
        store_odds_into_db.save()

        self.assertIsInstance(store_odds_into_db.home_odds, float)
        self.assertIsInstance(store_odds_into_db.draw_odds, float)
        self.assertIsInstance(store_odds_into_db.away_odds, float)

    def test_12_store_list_of_matches_into_db(self):
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_0)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        store_odds_into_db = WilliamHillOdds0(home_odds=convert_fraction_to_decimal_2[1][0], draw_odds=convert_fraction_to_decimal_2[1][1], away_odds=convert_fraction_to_decimal_2[1][2], games_id=1)
        store_odds_into_db.save()

        self.assertIsInstance(store_odds_into_db.home_odds, float)
        self.assertIsInstance(store_odds_into_db.draw_odds, float)
        self.assertIsInstance(store_odds_into_db.away_odds, float)

    def test_13_store_list_of_matches_into_db(self):
        get_match_odds_link_0 = self.check_db_odds_csv_name_with_csv_file(str('link_0'))
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_0)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        store_odds_into_db = WilliamHillOdds0(home_odds=convert_fraction_to_decimal_2[2][0], draw_odds=convert_fraction_to_decimal_2[2][1], away_odds=convert_fraction_to_decimal_2[2][2], games_id=1)
        store_odds_into_db.save()

        self.assertIsInstance(store_odds_into_db.home_odds, float)
        self.assertIsInstance(store_odds_into_db.draw_odds, float)
        self.assertIsInstance(store_odds_into_db.away_odds, float)
