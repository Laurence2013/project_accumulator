from django.test import TestCase
from decimal import Decimal
from accumulator.models import Game, Odd
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 5th behavioural test '''

class MergeTheCombinedGamesAndTheOdds(TestCase, TwoGamesAccumulator, GeneralGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        Odd.objects.create(id=1, home_odds=0.91, draw_odds=2.75, away_odds=3.00,
        games=Game.objects.get(pk=1))
        Odd.objects.create(id=2, home_odds=1.30, draw_odds=2.00, away_odds=2.20,
        games=Game.objects.get(pk=2))

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForTwoGames()
        self.get_games = self.get_game_combinations(self.get_combo, self.games)
        self.combos = self.get_per_outcome(self.get_combo)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = self.combine_combo_list_with_game_list(self.combos, self.get_games, self.match, self.game)
        self.get_num = list(self.break_list_into_equal_chunks(self.new_combo, 2))
        self.get_odds_combo = self.get_length_of_combo(self.get_num,9, 2)
        self.get_all_odds_combo = self.get_combined_games(self.get_odds_combo)
        self.get_combined_decimals = list(self.break_list_into_equal_chunks(self.get_all_odds_combo, 2))

    def test_GetCombinedDecimalsFromIndex_0(self):
        self.assertEqual([Decimal('0.91'), Decimal('1.30')], self.get_combined_decimals[0])

    def test_GetCombinedDecimalsFromIndex_1(self):
        self.assertEqual([Decimal('0.91'), Decimal('2.00')], self.get_combined_decimals[1])

    def test_GetCombinedDecimalsFromIndex_2(self):
        self.assertEqual([Decimal('0.91'), Decimal('2.20')], self.get_combined_decimals[2])

    def test_GetCombinedDecimalsFromIndex_3(self):
        self.assertEqual([Decimal('2.75'), Decimal('1.30')], self.get_combined_decimals[3])

    def test_GetCombinedDecimalsFromIndex_4(self):
        self.assertEqual([Decimal('2.75'), Decimal('2.00')], self.get_combined_decimals[4])
