from django.test import TestCase
from games_odds.models import *
from accumulator.models import *
from decimal import Decimal
from accumulator.accumulatorPageGames.accumulatorPageGames import AccumulatorPageGames

class TestingGetGamesFunction(TestCase):
    def setUp(self):
        self.final_games_odds_list = [(89, 'ARC Oleiros \xa0 v \xa0\xa0Sporting Lisbon', 89, Decimal('16.00'), Decimal('10.00'), Decimal('0.04')),
        (90, 'Ponte Preta \xa0 v \xa0\xa0Santos', 90, Decimal('1.45'), Decimal('2.00'), Decimal('1.88')),
        (91, 'Vitoria BA \xa0 v \xa0\xa0Sport Recife', 91, Decimal('1.05'), Decimal('2.25'), Decimal('2.40'))]

        self.games = [89, 'ARC Oleiros \xa0 v \xa0\xa0Sporting Lisbon', 90, 'Ponte Preta \xa0 v \xa0\xa0Santos', 91, 'Vitoria BA \xa0 v \xa0\xa0Sport Recife']
        self.odds = [{'away_odds': Decimal('0.04'), 'draw_odds': Decimal('10.00'), 'home_odds': Decimal('16.00')},
        {'away_odds': Decimal('1.88'), 'draw_odds': Decimal('2.00'), 'home_odds': Decimal('1.45')},
        {'away_odds': Decimal('2.40'), 'draw_odds': Decimal('2.25'), 'home_odds': Decimal('1.05')}]

    def test_01_convert_games_and_odds_to_final_games_odds_list(self):
        accumulator = AccumulatorPageGames()
        wh0 = WilliamHillGames0.objects.values('id','games').filter(url_game_link_id=1)
        get_games = accumulator.get_games(self.games, self.odds)
        # self.assertEqual(self.final_games_odds_list, get_games)
