from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.fourGamesAccumulator import FourGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 3rd behavioural test '''

class TestingCombineComboListWithGameListShould(TestCase, GeneralGamesAccumulator, FourGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=4, games='Crystal Palace vs Arsenal', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=5, games='Real Sociedad vs Sporting Gijon', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=6, games='Maritimo vs Chaves', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=7, games='Defensa y Justicia vs Olimpio Bahia Blanca', time='19:45:00', date_of_game='2017-02-27')

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForFourGames()
        self.combos = self.get_per_outcome(self.get_combo)
        self.get_games = self.get_game_combinations(self.get_combo, self.games)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = self.combine_combo_list_with_game_list(self.combos, self.get_games, self.match, self.game)
    
    def test_ThatIndex_0_IsEqualToTuple_0_WhichIs_4_1_H(self):
        self.assertEqual((4, 1, 'H'), self.new_combo[0])

    def test_ThatIndex_1_IsEqualToTuple_0_WhichIs_5_1_H(self):
        self.assertEqual((5, 1, 'H'), self.new_combo[1])

    def test_ThatIndex_2_IsEqualToTuple_0_WhichIs_6_1_H(self):
        self.assertEqual((6, 1, 'H'), self.new_combo[2])

    def test_ThatIndex_3_IsEqualToTuple_0_WhichIs_7_2_H(self):
        self.assertEqual((7, 1, 'H'), self.new_combo[3])

    def test_ThatIndex_4_IsEqualToTuple_0_WhichIs_4_2_H(self):
        self.assertEqual((4, 2, 'H'), self.new_combo[4])

    def test_ThatIndex_5_IsEqualToTuple_0_WhichIs_5_2_H(self):
        self.assertEqual((5, 2, 'H'), self.new_combo[5])

    def test_ThatIndex_6_IsEqualToTuple_0_WhichIs_6_3_H(self):
        self.assertEqual((6, 2, 'H'), self.new_combo[6])

    def test_ThatIndex_7_IsEqualToTuple_0_WhichIs_7_3_D(self):
        self.assertEqual((7, 2, 'D'), self.new_combo[7])

    def test_ThatIndex_8_IsEqualToTuple_0_WhichIs_4_3_H(self):
        self.assertEqual((4, 3, 'H'), self.new_combo[8])

    def test_ThatIndex_9_IsEqualToTuple_0_WhichIs_5_3_H(self):
        self.assertEqual((5, 3, 'H'), self.new_combo[9])

    def test_ThatIndex_10_IsEqualToTuple_0_WhichIs_6_3_H(self):
        self.assertEqual((6, 3, 'H'), self.new_combo[10])

    def test_ThatIndex_11_IsEqualToTuple_0_WhichIs_7_3_A(self):
        self.assertEqual((7, 3, 'A'), self.new_combo[11])
