from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.threeGamesAccumulator import ThreeGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 3rd behavioural test '''

class TestingCombineComboListWithGameListShould(TestCase, GeneralGamesAccumulator, ThreeGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=3, games='St Pauli vs Karlsruhe', time='19:45:00', date_of_game='2017-02-27')

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForThreeGames()
        self.combos = self.get_per_outcome(self.get_combo)
        self.get_games = self.get_game_combinations(self.get_combo, self.games)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = self.combine_combo_list_with_game_list(self.combos, self.get_games, self.match, self.game)

    def test_ThatIndex_0_IsEqualToTuple_0_WhichIs_1_1_H(self):
        self.assertEqual((1, 1, 'H'), self.new_combo[0])

    def test_ThatIndex_1_IsEqualToTuple_0_WhichIs_2_1_H(self):
        self.assertEqual((2, 1, 'H'), self.new_combo[1])

    def test_ThatIndex_2_IsEqualToTuple_0_WhichIs_3_1_H(self):
        self.assertEqual((3, 1, 'H'), self.new_combo[2])

    def test_ThatIndex_3_IsEqualToTuple_0_WhichIs_1_2_H(self):
        self.assertEqual((1, 2, 'H'), self.new_combo[3])

    def test_ThatIndex_4_IsEqualToTuple_0_WhichIs_2_2_H(self):
        self.assertEqual((2, 2, 'H'), self.new_combo[4])

    def test_ThatIndex_5_IsEqualToTuple_0_WhichIs_3_2_D(self):
        self.assertEqual((3, 2, 'D'), self.new_combo[5])

    def test_ThatIndex_6_IsEqualToTuple_0_WhichIs_1_3_H(self):
        self.assertEqual((1, 3, 'H'), self.new_combo[6])

    def test_ThatIndex_7_IsEqualToTuple_0_WhichIs_2_3_H(self):
        self.assertEqual((2, 3, 'H'), self.new_combo[7])

    def test_ThatIndex_8_IsEqualToTuple_0_WhichIs_3_3_A(self):
        self.assertEqual((3, 3, 'A'), self.new_combo[8])
