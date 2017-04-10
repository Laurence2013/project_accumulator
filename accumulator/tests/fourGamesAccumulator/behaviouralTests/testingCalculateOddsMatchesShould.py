from django.test import TestCase
from accumulator.models import Game, Odd
from accumulator.combinations.fourGamesAccumulator import FourGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator
from decimal import Decimal

''' This is the 8th behavioural test '''

class TestingCalculateOddsMatchesShould(TestCase, GeneralGamesAccumulator, FourGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=4, games='Crystal Palace vs Arsenal', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=5, games='Real Sociedad vs Sporting Gijon', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=6, games='Maritimo vs Chaves', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=7, games='Defensa y Justicia vs Olimpio Bahia Blanca', time='19:45:00', date_of_game='2017-02-27')

        Odd.objects.create(id=4, home_odds=4.33, draw_odds=3.60, away_odds=1.80, games=Game.objects.get(pk=4))
        Odd.objects.create(id=5, home_odds=1.44, draw_odds=4.50, away_odds=7.00, games=Game.objects.get(pk=5))
        Odd.objects.create(id=6, home_odds=1.95, draw_odds=3.20, away_odds=4.00, games=Game.objects.get(pk=6))
        Odd.objects.create(id=7, home_odds=1.75, draw_odds=3.20, away_odds=4.80, games=Game.objects.get(pk=7))

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForFourGames()
        self.combos = self.get_per_outcome(self.get_combo)
        self.get_games = self.get_game_combinations(self.get_combo, self.games)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = self.combine_combo_list_with_game_list(self.combos, self.get_games, self.match, self.game)
        self.get_num = list(self.break_list_into_equal_chunks(self.new_combo,4))
        self.get_odds_combo = self.get_length_of_combo(self.get_num,81, 4)
        self.get_all_odds_combo = self.get_combined_games(self.get_odds_combo)
        self.get_combined_decimals = list(self.break_list_into_equal_chunks(self.get_all_odds_combo, 4))
        self.get_combined_calculation = self.calculateOddsForFourMatches(self.get_combined_decimals, 1)

    def test_GetCalculationOfThreeGamesIndex_0_WithStakeAt_1_Pound(self):
        self.assertEqual(Decimal('20.28'), self.get_combined_calculation[0])

    def test_GetCalculationOfThreeGamesIndex_1_WithStakeAt_1_Pound(self):
        self.assertEqual(Decimal('37.91'), self.get_combined_calculation[1])

    def test_GetCalculationOfThreeGamesIndex_2_WithStakeAt_1_Pound(self):
        self.assertEqual(Decimal('57.36'), self.get_combined_calculation[2])

    def test_GetCalculationOfThreeGamesIndex_3_WithStakeAt_1_Pound(self):
        self.assertEqual(Decimal('33.92'), self.get_combined_calculation[3])
