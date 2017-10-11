from django.conf import settings
from games_odds.models import *
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch

class SaveGamesIntoDb(CombineOddsWithItsMatch):
    def check_db_csv_name_with_csv_file(self, link_no):
        get_match_odds_file_path = self.get_ids_for_tag_span_link_csv(link_no)
        return get_match_odds_file_path

    def get_games_from_csv_file(self, link_no):
        get_csv_file_path = self.check_db_csv_name_with_csv_file(link_no)
        get_matches = self.get_match(get_csv_file_path)
        return get_matches

    def store_csv_files_into_list(self, get_matches):
        list_of_matches = list()
        for matches in get_matches:
            list_of_matches.append(matches)
        return list_of_matches

    def get_ids_for_tag_span_link_csv(self, link_no):
        base_dir = settings.BASE_DIR
        get_url = WilliamHillCsvLinks.objects.get(url_name=link_no)
        get_match_odds_file_path_0 = base_dir + "/games_odds/williamHillFiles/tag_name_span_attr_ids/" + get_url.ids_for_tag_span_link_csv
        return get_match_odds_file_path_0

    def store_games_into_db(self, link_no, csv_list):
        if str(link_no) is 'link_0':
            WilliamHillOdds0.objects.all().delete()
        if str(link_no) is 'link_1':
            WilliamHillOdds1.objects.all().delete()
        if str(link_no) is 'link_2':
            WilliamHillOdds2.objects.all().delete()
        if str(link_no) is 'link_3':
            WilliamHillOdds3.objects.all().delete()
        if str(link_no) is 'link_4':
            WilliamHillOdds4.objects.all().delete()
        if str(link_no) is 'link_5':
            WilliamHillOdds5.objects.all().delete()
        if str(link_no) is 'link_6':
            WilliamHillOdds6.objects.all().delete()

        isTrue = self.return_games_into_db(link_no, csv_list)
        if isTrue is True:
            return True
        return False

    def return_games_into_db(self, link_no, csv_list):
        store_games_or_odds = self.store_csv_files_into_list(csv_list)
        if link_no == str('link_0'):
            get_id = WilliamHillCsvLinks.objects.get(url_name=link_no)
            for game in store_games_or_odds:
                store_tag_span_link_list = WilliamHillGames0(games=game, url_game_link_id=int(get_id.id))
                store_tag_span_link_list.save()
            if WilliamHillGames0.objects.count() >= 1:
                return True
        if link_no == str('link_1'):
            get_id = WilliamHillCsvLinks.objects.get(url_name=link_no)
            for game in store_games_or_odds:
                store_tag_span_link_list = WilliamHillGames1(games=game, url_game_link_id=int(get_id.id))
                store_tag_span_link_list.save()
            if WilliamHillGames1.objects.count() >= 1:
                return True
        if link_no == str('link_2'):
            get_id = WilliamHillCsvLinks.objects.get(url_name=link_no)
            for game in store_games_or_odds:
                store_tag_span_link_list = WilliamHillGames2(games=game, url_game_link_id=int(get_id.id))
                store_tag_span_link_list.save()
            if WilliamHillGames2.objects.count() >= 1:
                return True
        if link_no == str('link_3'):
            get_id = WilliamHillCsvLinks.objects.get(url_name=link_no)
            for game in store_games_or_odds:
                store_tag_span_link_list = WilliamHillGames3(games=game, url_game_link_id=int(get_id.id))
                store_tag_span_link_list.save()
            if WilliamHillGames3.objects.count() >= 1:
                return True
        if link_no == str('link_4'):
            get_id = WilliamHillCsvLinks.objects.get(url_name=link_no)
            for game in store_games_or_odds:
                store_tag_span_link_list = WilliamHillGames4(games=game, url_game_link_id=int(get_id.id))
                store_tag_span_link_list.save()
            if WilliamHillGames4.objects.count() >= 1:
                return True
        if link_no == str('link_5'):
            get_id = WilliamHillCsvLinks.objects.get(url_name=link_no)
            for game in store_games_or_odds:
                store_tag_span_link_list = WilliamHillGames5(games=game, url_game_link_id=int(get_id.id))
                store_tag_span_link_list.save()
            if WilliamHillGames5.objects.count() >= 1:
                return True
        if link_no == str('link_6'):
            get_id = WilliamHillCsvLinks.objects.get(url_name=link_no)
            for game in store_games_or_odds:
                store_tag_span_link_list = WilliamHillGames6(games=game, url_game_link_id=int(get_id.id))
                store_tag_span_link_list.save()
            if WilliamHillGames6.objects.count() >= 1:
                return True
