from django.conf import settings
from games_odds.models import WilliamHillCsvLinks
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch

class SaveOddsIntoDb():
    def check_db_csv_name_with_csv_file(self, link_no):
        get_match_odds_file_path = self.get_ids_for_tag_span_link_csv(link_no)
        return get_match_odds_file_path

    def get_ids_for_tag_span_link_csv(self, link_no):
        base_dir = settings.BASE_DIR
        get_url = WilliamHillCsvLinks.objects.get(url_name=link_no)
        get_match_odds_file_path_0 = base_dir + "/games_odds/williamHillFiles/get_match_odds/" + get_url.get_match_odds_link_csv
        return get_match_odds_file_path_0
