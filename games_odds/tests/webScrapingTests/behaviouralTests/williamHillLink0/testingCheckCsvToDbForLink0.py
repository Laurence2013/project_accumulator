from django.test import TestCase
from games_odds.models import WilliamHillCsvLinks

class TestingCheckCsvToDbForLink0(TestCase):
    def setUp(self):
        WilliamHillCsvLinks.objects.create(id=1,
        url_name = str('link_0'), get_match_odds_link_csv = str('get_match_odds_link_0.csv'), ids_for_tag_span_link_csv = str('ids_for_tag_span_link_0.csv'), ids_for_tag_tbody_link_csv = str('ids_for_tag_tbody_link_0.csv'))

    def test_01_check_link_0_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_0'))
        self.assertEqual(str('link_0'), get_url.url_name)

    def test_02_check_get_match_odds_link_csv_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_0'))
        self.assertEqual(str('get_match_odds_link_0.csv'), get_url.get_match_odds_link_csv)

    def test_03_check_ids_for_tag_span_link_csv_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_0'))
        self.assertEqual(str('ids_for_tag_span_link_0.csv'), get_url.ids_for_tag_span_link_csv)

    def test_04_check_ids_for_tag_tbody_link_csv_is_in_db(self):
        get_url = WilliamHillCsvLinks.objects.get(url_name=str('link_0'))
        self.assertEqual(str('ids_for_tag_tbody_link_0.csv'), get_url.ids_for_tag_tbody_link_csv)
