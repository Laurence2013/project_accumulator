from django.test import TestCase
from games_odds.models import *
from accumulator.models import *
from accumulator.accumulatorPageGames.accumulatorPageGames import AccumulatorPageGames

class TestingGettingMatchesAndOddsFromDb(TestCase):
    def setUp(self):
        Bookie.objects.create(id=1, bookies_name='William Hill', date_updated='2017-10-10 21:32:11')

        WilliamHillCsvLinks.objects.create(id=1, url_name='link_0', get_match_odds_link_csv='get_match_odds_link_0.csv', ids_for_tag_span_link_csv='ids_for_tag_span_link_0.csv', ids_for_tag_tbody_link_csv='ids_for_tag_tbody_link_0.csv', date_updated='2017-10-12 17:02:20')

        WilliamHillDailyMatche.objects.create(id=66, dates_of_games='Today 12 Oct 17', date_updated='2017-10-12 17:02:20', bookies_id=1, wh_csv_links_id=1)

        WilliamHillGames0.objects.create(id=89, games='ARC Oleiros   v   Sporting Lisbon', date_updated='2017-10-12 16:57:18', url_game_link_id=1)
        WilliamHillGames0.objects.create(id=90, games='Ponte Preta   v   Santos', date_updated='2017-10-12 16:57:18', url_game_link_id=1)
        WilliamHillGames0.objects.create(id=91, games='Vitoria BA   v   Sport Recife', date_updated='2017-10-12 16:57:18', url_game_link_id=1)

        WilliamHillOdds0.objects.create(id=89, home_odds=16.00, draw_odds=10.00, away_odds=0.04, date_updated='2017-10-12 16:57:20', games_id=89)
        WilliamHillOdds0.objects.create(id=90, home_odds=1.45, draw_odds=2.00, away_odds=1.88, date_updated='2017-10-12 16:57:20', games_id=90)
        WilliamHillOdds0.objects.create(id=91, home_odds=1.05, draw_odds=2.25, away_odds=2.40, date_updated='2017-10-12 16:57:20', games_id=91)

    def test_01_get_unique_id_from_user_selection_of_bookies_match_date_from_home_page(self):
        my_num = [66]
        accumGames = AccumulatorPageGames()
        match_day_id = accumGames.getting_matches_and_odds_from_db(my_num)
        self.assertEqual(66, match_day_id)

    def test_02_get_bookies_id_and_wh_csv_links_id_from_wh_daily_matche_table_according_to_my_day_id_66(self):
        wh = {'wh_csv_links_id': 1}
        my_num = [66]
        accumGames = AccumulatorPageGames()
        match_day_id = accumGames.getting_matches_and_odds_from_db(my_num)
        get_ids = WilliamHillDailyMatche.objects.values('wh_csv_links_id').get(id=match_day_id)
        self.assertDictEqual(wh, get_ids)

    def test_03_get_games_from_wh_according_to_wh_csv_links_id(self):
        wh = {'wh_csv_links_id': 1}
        wh_list = ['ARC Oleiros \xa0 v \xa0\xa0Sporting Lisbon', 'Ponte Preta \xa0 v \xa0\xa0Santos', 'Vitoria BA \xa0 v \xa0\xa0Sport Recife']
        my_num = [66]
        accumGames = AccumulatorPageGames()
        match_day_id = accumGames.getting_matches_and_odds_from_db(my_num)
        get_ids = WilliamHillDailyMatche.objects.values('wh_csv_links_id').get(id=match_day_id)
        get_bookies_ids = accumGames.get_bookies_ids(get_ids)
        wh0 = WilliamHillGames0.objects.values('games').filter(url_game_link_id=get_bookies_ids)
        get_games = accumGames.extract_and_get_games(wh0)
        self.assertEqual(wh_list, get_games)

    def test_04_get_odds_from_wh_according_to_wh_csv_links_id(self):
        pass
