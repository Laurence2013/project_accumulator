from django.conf import settings
from games_odds.models import WilliamHillGames0, WilliamHillGames1, WilliamHillOdds0, WilliamHillOdds1
from games_odds.models import WilliamHillCsvLinks
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb

class SaveOddsIntoDb(DecimalToFractionAndStoreInDb):
    def check_db_odds_csv_name_with_csv_file(self, link_no):
        get_match_odds_file_path = self.get_match_odds_link_csv(link_no)
        return get_match_odds_file_path

    def get_odds_from_csv_file(self, link_no):
        get_match_odds_link_1 = self.check_db_odds_csv_name_with_csv_file(link_no)
        convert_fraction_to_decimal_1 = self.convert_fraction_to_decimal(get_match_odds_link_1)
        convert_fraction_to_decimal_2 = self.create_new_list(convert_fraction_to_decimal_1)
        return convert_fraction_to_decimal_2

    def get_match_odds_link_csv(self, link_no):
        base_dir = settings.BASE_DIR
        get_url = WilliamHillCsvLinks.objects.get(url_name=link_no)
        get_match_odds_file_path_0 = base_dir + "/games_odds/williamHillFiles/get_match_odds/" + get_url.get_match_odds_link_csv
        return get_match_odds_file_path_0

    def store_odds_into_db(self, link_no, csv_list):
        isTrue = self.return_odds_into_db(link_no, csv_list)
        if isTrue is True:
            return True
        return False

    def return_odds_into_db(self, link_no, csv_list):
        games_list = list()
        count = 0
        if link_no == str('link_0'):
            game_id = WilliamHillGames0.objects.all()
            for game in game_id:
                games_list.append(game.id)
            for game in csv_list:
                store_tag_span_link_list = WilliamHillOdds0(home_odds=game[0], draw_odds=game[1], away_odds=game[2], games_id=games_list[count])
                store_tag_span_link_list.save()
                count += 1
            if WilliamHillOdds0.objects.count() >= 1:
                return True
        if link_no == str('link_1'):
            game_id = WilliamHillGames1.objects.all()
            for game in game_id:
                games_list.append(game.id)
            for game in csv_list:
                store_tag_span_link_list = WilliamHillOdds1(home_odds=game[0], draw_odds=game[1], away_odds=game[2], games_id=games_list[count])
                store_tag_span_link_list.save()
                count += 1
            if WilliamHillOdds1.objects.count() >= 1:
                return True
