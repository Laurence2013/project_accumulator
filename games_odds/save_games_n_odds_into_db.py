from django.conf import settings
from games_odds.models import WilliamHillCsvLinks
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch

class SaveGamesNOddsIntoDb(CombineOddsWithItsMatch):
    def check_db_csv_name_with_csv_file(self, link_no):
        base_dir = settings.BASE_DIR
        get_url = WilliamHillCsvLinks.objects.get(url_name=link_no)
        get_match_odds_file_path_0 = base_dir + "/games_odds/williamHillFiles/tag_name_span_attr_ids/" + get_url.ids_for_tag_span_link_csv
        return str(get_match_odds_file_path_0)

    def get_games_from_csv_file(self):
        get_csv_file_path = self.check_db_csv_name_with_csv_file(str('link_0'))
        get_matches = self.get_match(get_csv_file_path)
        return get_matches
