from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.fourGamesAccumulator import FourGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 4th behavioural test '''

class TestingBreakListIntoEqualChunksShould(TestCase, GeneralGamesAccumulator, FourGamesAccumulator):
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
        self.get_num = list(self.break_list_into_equal_chunks(self.new_combo, 4))

    def test_AtIndex_0_ItShouldBe_41H_51H_61H_71H(self):
        testList = [(4, 1, 'H'), (5, 1, 'H'), (6, 1, 'H'), (7, 1, 'H')]
        self.assertListEqual(testList, self.get_num[0])

    def test_AtIndex_1_ItShouldBe_42H_52H_62H_72D(self):
        testList = [(4, 2, 'H'), (5, 2, 'H'), (6, 2, 'H'), (7, 2, 'D')]
        self.assertListEqual(testList, self.get_num[1])

    def test_AtIndex_2_ItShouldBe_43H_53H_63H_73A(self):
        testList = [(4, 3, 'H'), (5, 3, 'H'), (6, 3, 'H'), (7, 3, 'A')]
        self.assertListEqual(testList, self.get_num[2])

    def test_AtIndex_3_ItShouldBe_44H_54H_64D_74H(self):
        testList = [(4, 4, 'H'), (5, 4, 'H'), (6, 4, 'D'), (7, 4, 'H')]
        self.assertListEqual(testList, self.get_num[3])

    def test_AtIndex_4_ItShouldBe_45H_55H_65D_75D(self):
        testList = [(4, 5, 'H'), (5, 5, 'H'), (6, 5, 'D'), (7, 5, 'D')]
        self.assertListEqual(testList, self.get_num[4])

    def test_AtIndex_5_ItShouldBe_46H_56H_66D_76A(self):
        testList = [(4, 6, 'H'), (5, 6, 'H'), (6, 6, 'D'), (7, 6, 'A')]
        self.assertListEqual(testList, self.get_num[5])

    def test_GetLengthOfGetNum(self):
        self.assertEqual(81, len(self.get_num))
