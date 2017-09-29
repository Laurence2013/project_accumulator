from django.test import TestCase
from games_odds.models import WilliamHillCsvLinks
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch

class TestingGetGamesFromCsvAndStoreIntoDbForLink0(TestCase):
    def setUp(self):
        WilliamHillCsvLinks.objects.create(id=1,
        url_name = str('link_0'), get_match_odds_link_csv = str('get_match_odds_link_0.csv'), ids_for_tag_span_link_csv = str('ids_for_tag_span_link_0.csv'), ids_for_tag_tbody_link_csv = str('ids_for_tag_tbody_link_0.csv'))
