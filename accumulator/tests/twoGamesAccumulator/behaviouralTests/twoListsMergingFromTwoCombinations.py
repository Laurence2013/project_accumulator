from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 2nd behavioural test '''

class TwoListsMergingFromTwoCombinations(TestCase, TwoGamesAccumulator, GeneralGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForTwoGames()
        self.get_games = self.getGameCombinations(self.get_combo, self.games)
        self.combos = self.get_per_outcome(self.get_combo)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = self.combineComboListWithGameList(self.combos, self.get_games, self.match, self.game)

    def test_ThatIndex_0_IsEqualToTuple_0_WhichIs_1_1_H(self):
        self.assertEqual((1, 1, 'H'), self.new_combo[0])

    def test_ThatIndex_1_IsEqualToTuple_1_WhichIs_2_1_H(self):
        self.assertEqual((2, 1, 'H'), self.new_combo[1])

    def test_ThatIndex_2_IsEqualToTuple_2_WhichIs_1_2_H(self):
        self.assertEqual((1, 2, 'H'), self.new_combo[2])

    def test_ThatIndex_3_IsEqualToTuple_3_WhichIs_2_1_D(self):
        self.assertEqual((2, 2, 'D'), self.new_combo[3])

    def test_ThatIndex_4_IsEqualToTuple_4_WhichIs_1_3_H(self):
        self.assertEqual((1, 3, 'H'), self.new_combo[4])

    def test_ThatIndex_5_IsEqualToTuple_5_WhichIs_2_3_A(self):
        self.assertEqual((2, 3, 'A'), self.new_combo[5])
