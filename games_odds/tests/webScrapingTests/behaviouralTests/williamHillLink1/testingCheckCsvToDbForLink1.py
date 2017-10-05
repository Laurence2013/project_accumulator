from django.test import TestCase
from games_odds.models import WilliamHillCsvLinks

'''
This is 1st scenario, from the id chosen from the html page from user side or admin side, according to what the user clicked on or admin clicked on,
for example they clicked on id link_1 then link_1 is checked against the database and its csv files are checked
'''

class TestingCheckCsvToDbForLink1(TestCase):
    def setUp(self):
        WilliamHillCsvLinks.objects.create(id=2,
        url_name = str('link_1'), get_match_odds_link_csv = str('get_match_odds_link_1.csv'), ids_for_tag_span_link_csv = str('ids_for_tag_span_link_1.csv'), ids_for_tag_tbody_link_csv = str('ids_for_tag_tbody_link_1.csv'))

    def test_01_check_link_0_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_1'))
        self.assertEqual(str('link_1'), get_url.url_name)

    def test_02_check_get_match_odds_link_csv_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_1'))
        self.assertEqual(str('get_match_odds_link_1.csv'), get_url.get_match_odds_link_csv)

    def test_03_check_ids_for_tag_span_link_csv_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_1'))
        self.assertEqual(str('ids_for_tag_span_link_1.csv'), get_url.ids_for_tag_span_link_csv)

    def test_04_check_ids_for_tag_tbody_link_csv_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_1'))
        self.assertEqual(str('ids_for_tag_tbody_link_1.csv'), get_url.ids_for_tag_tbody_link_csv)
