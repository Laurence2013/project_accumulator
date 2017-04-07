from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.threeGamesAccumulator import ThreeGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 4th behavioural test '''

class TestingBreakListIntoEqualChunksShould(TestCase, GeneralGamesAccumulator, ThreeGamesAccumulator):
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
        self.get_num = list(self.break_list_into_equal_chunks(self.new_combo, 3))

    def test_AtIndex_0_ItShouldBe_11H_21H_31H(self):
        testList = [(1, 1, 'H'), (2, 1, 'H'), (3, 1, 'H')]
        self.assertListEqual(testList, self.get_num[0])

    def test_AtIndex_1_ItShouldBe_12H_22H_32H(self):
        testList = [(1, 2, 'H'), (2, 2, 'H'), (3, 2, 'D')]
        self.assertListEqual(testList, self.get_num[1])

    def test_AtIndex_2_ItShouldBe_13H_23H_33H(self):
        testList = [(1, 3, 'H'), (2, 3, 'H'), (3, 3, 'A')]
        self.assertListEqual(testList, self.get_num[2])

    def test_AtIndex_3_ItShouldBe_14H_24H_34H(self):
        testList = [(1, 4, 'H'), (2, 4, 'D'), (3, 4, 'H')]
        self.assertListEqual(testList, self.get_num[3])

    def test_AtIndex_4_ItShouldBe_15H_25H_35H(self):
        testList = [(1, 5, 'H'), (2, 5, 'D'), (3, 5, 'D')]
        self.assertListEqual(testList, self.get_num[4])

    def test_AtIndex_5_ItShouldBe_16H_26H_36H(self):
        testList = [(1, 6, 'H'), (2, 6, 'D'), (3, 6, 'A')]
        self.assertListEqual(testList, self.get_num[5])

    def test_GetLengthOfGetNum(self):
        self.assertEqual(27, len(self.get_num))
