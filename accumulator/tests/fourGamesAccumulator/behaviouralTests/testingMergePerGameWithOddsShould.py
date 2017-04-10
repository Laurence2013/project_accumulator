from django.test import TestCase
from accumulator.models import Game, Odd
from accumulator.combinations.fourGamesAccumulator import FourGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator
from decimal import Decimal

''' This is the 9th behavioural test '''

class TestingMergePerGameWithOddsShould(TestCase, GeneralGamesAccumulator, FourGamesAccumulator):
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
        self.get_all_combinations = self.merge_per_game_with_odds(self.get_odds_combo, self.get_combined_decimals, self.get_combined_calculation)

    def test_CombineFourMatchesWithItsOddsAndCalculationAtIndex_0(self):
        finalList = ([4, 'H', 5, 'H', 6, 'H', 7, 'H'], [Decimal('4.33'), Decimal('1.44'), Decimal('1.95'), Decimal('1.75')], Decimal('20.28'))
        self.assertTupleEqual(finalList, self.get_all_combinations[0])

    def test_CombineFourMatchesWithItsOddsAndCalculationAtIndex_1(self):
        finalList = ([4, 'H', 5, 'H', 6, 'H', 7, 'D'], [Decimal('4.33'), Decimal('1.44'), Decimal('1.95'), Decimal('3.20')], Decimal('37.91'))
        self.assertTupleEqual(finalList, self.get_all_combinations[1])

    def test_CombineFourMatchesWithItsOddsAndCalculationAtIndex_2(self):
        finalList = ([4, 'H', 5, 'H', 6, 'H', 7, 'A'], [Decimal('4.33'), Decimal('1.44'), Decimal('1.95'), Decimal('4.80')], Decimal('57.36'))
        self.assertTupleEqual(finalList, self.get_all_combinations[2])

    def test_CombineFourMatchesWithItsOddsAndCalculationAtIndex_3(self):
        finalList = ([4, 'H', 5, 'H', 6, 'D', 7, 'H'], [Decimal('4.33'), Decimal('1.44'), Decimal('3.20'), Decimal('1.75')], Decimal('33.92'))
        self.assertTupleEqual(finalList, self.get_all_combinations[3])

    def test_CombineFourMatchesWithItsOddsAndCalculationAtIndex_4(self):
        finalList = ([4, 'H', 5, 'H', 6, 'D', 7, 'D'], [Decimal('4.33'), Decimal('1.44'), Decimal('3.20'), Decimal('3.20')], Decimal('62.85'))
        self.assertTupleEqual(finalList, self.get_all_combinations[4])
