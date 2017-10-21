from django.test import TestCase
from games_odds.models import *
from accumulator.models import *
from decimal import Decimal
from accumulator.accumulatorPageGames.accumulatorPageGames import AccumulatorPageGames

class TestingGettingMatchesAndOddsFromDb(TestCase):
    def setUp(self):
        self.whlist = [WilliamHillOdds0, WilliamHillOdds1, WilliamHillOdds2]
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

    def test_04_count_length_of_WilliamHillGames0(self):
        get_length = WilliamHillGames0.objects.count()
        self.assertEqual(3, get_length)

    def test_05_get_odds_id_89_from_WilliamHillGames0_where_id_is_89(self):
        odds = {'away_odds': Decimal('0.04'), 'home_odds': Decimal('16.00'), 'draw_odds': Decimal('10.00')}
        get_games_id = WilliamHillGames0.objects.get(id=89)
        get_odds = WilliamHillOdds0.objects.values('home_odds','draw_odds','away_odds').get(games_id=get_games_id.id)
        self.assertEqual(odds, get_odds)

    def test_06_get_odds_id_90_from_WilliamHillGames0_where_id_is_90(self):
        odds = {'away_odds': Decimal('1.88'), 'home_odds': Decimal('1.45'), 'draw_odds': Decimal('2.00')}
        get_games_id = WilliamHillGames0.objects.get(id=90)
        get_odds = WilliamHillOdds0.objects.values('home_odds','draw_odds','away_odds').get(games_id=get_games_id.id)
        self.assertEqual(odds, get_odds)

    def test_07_get_odds_id_91_from_WilliamHillGames0_where_id_is_91(self):
        odds = {'away_odds': Decimal('2.40'), 'home_odds': Decimal('1.05'), 'draw_odds': Decimal('2.25')}
        get_games_id = WilliamHillGames0.objects.get(id=91)
        get_odds = WilliamHillOdds0.objects.values('home_odds','draw_odds','away_odds').get(games_id=get_games_id.id)
        self.assertEqual(odds, get_odds)

    def test_08_check_models_class_name(self):
        class_name = WilliamHillOdds0.__class__
        self.assertEqual(class_name, self.whlist[0].__class__)

    def test_09_check_models_class_name(self):
        class_name = WilliamHillOdds1.__class__
        self.assertEqual(class_name, self.whlist[1].__class__)

    def test_10_check_models_class_name(self):
        class_name = WilliamHillOdds1.__class__
        self.assertEqual(class_name, self.whlist[1].__class__)

    def test_11_testing_extract_by_getting_odds_function(self):
        odds = [{'away_odds': Decimal('0.04'), 'home_odds': Decimal('16.00'), 'draw_odds': Decimal('10.00')}, {'away_odds': Decimal('1.88'), 'home_odds': Decimal('1.45'), 'draw_odds': Decimal('2.00')}, {'away_odds': Decimal('2.40'), 'home_odds': Decimal('1.05'), 'draw_odds': Decimal('2.25')}]

        accumulatorGames = AccumulatorPageGames()
        get_games_id = WilliamHillGames0.objects.values('id')
        get_odds = accumulatorGames.extract_by_getting_odds(self.whlist[0], get_games_id)
        self.assertEqual(odds, get_odds)
