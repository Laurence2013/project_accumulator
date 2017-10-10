from django.test import TestCase
from decimal import Decimal
from accumulator.models import Game, Odd
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 7th behavioural test '''

class MergingOfComboOddsCalculation(TestCase, TwoGamesAccumulator, GeneralGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        Odd.objects.create(id=1, home_odds=0.91, draw_odds=2.75, away_odds=3.00, games=Game.objects.get(pk=1))
        Odd.objects.create(id=2, home_odds=1.30, draw_odds=2.00, away_odds=2.20, games=Game.objects.get(pk=2))

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForTwoGames()
        self.combos = self.get_per_outcome(self.get_combo)
        self.get_games = self.get_game_combinations(self.get_combo, self.games)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = self.combine_combo_list_with_game_list(self.combos, self.get_games, self.match, self.game)
        self.get_num = list(self.break_list_into_equal_chunks(self.new_combo, 2))
        self.get_odds_combo = self.get_length_of_combo(self.get_num,9,2)
        self.get_all_odds_combo = self.get_combined_games(self.get_odds_combo)
        self.get_combined_decimals = list(self.break_list_into_equal_chunks(self.get_all_odds_combo, 2))
        self.get_combined_calculation = self.calculateOddsForTwoMatches(self.get_combined_decimals, 1)
        self.get_all_combinations = self.merge_per_game_with_odds(self.get_odds_combo, self.get_combined_decimals, self.get_combined_calculation)

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_0(self):
        index0List = ([1, 'H', 2, 'H'], [Decimal('0.91'), Decimal('1.30')], Decimal('3.39'))
        self.assertTupleEqual(index0List, self.get_all_combinations[0])

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_1(self):
        index1List = ([1, 'H', 2, 'D'], [Decimal('0.91'), Decimal('2.00')], Decimal('4.73'))
        self.assertTupleEqual(index1List, self.get_all_combinations[1])

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_2(self):
        index2List = ([1, 'H', 2, 'A'], [Decimal('0.91'), Decimal('2.20')], Decimal('5.11'))
        self.assertTupleEqual(index2List, self.get_all_combinations[2])

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_3(self):
        index3List = ([1, 'D', 2, 'H'], [Decimal('2.75'), Decimal('1.30')], Decimal('7.62'))
        self.assertTupleEqual(index3List, self.get_all_combinations[3])

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_4(self):
        index4List = ([1, 'D', 2, 'D'], [Decimal('2.75'), Decimal('2.00')], Decimal('10.25'))
        self.assertTupleEqual(index4List, self.get_all_combinations[4])
