from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.threeGamesAccumulator import ThreeGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 5th behavioural test '''

class TestingGetLengthOfComboShould(TestCase, GeneralGamesAccumulator, ThreeGamesAccumulator):
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
        self.get_num = list(self.break_list_into_equal_chunks(self.new_combo,3))
        self.get_odds_combo = self.get_length_of_combo(self.get_num,27, 3)

    def test_Index_0_TheOutcomeShouldBe_1H_2H_3H(self):
        testList = [1, 'H', 2, 'H', 3, 'H']
        self.assertListEqual(testList, self.get_odds_combo[0])

    def test_Index_1_TheOutcomeShouldBe_1H_2H_3D(self):
        testList = [1, 'H', 2, 'H', 3, 'D']
        self.assertListEqual(testList, self.get_odds_combo[1])

    def test_Index_2_TheOutcomeShouldBe_1H_2H_3A(self):
        testList = [1, 'H', 2, 'H', 3, 'A']
        self.assertListEqual(testList, self.get_odds_combo[2])

    def test_Index_3_TheOutcomeShouldBe_1H_2D_3H(self):
        testList = [1, 'H', 2, 'D', 3, 'H']
        self.assertListEqual(testList, self.get_odds_combo[3])

    def test_Index_4_TheOutcomeShouldBe_1H_2D_3D(self):
        testList = [1, 'H', 2, 'D', 3, 'D']
        self.assertListEqual(testList, self.get_odds_combo[4])

    def test_Index_5_TheOutcomeShouldBe_1H_2D_3A(self):
        testList = [1, 'H', 2, 'D', 3, 'A']
        self.assertListEqual(testList, self.get_odds_combo[5])

    def test_GetLengthOfGetOddsCombo(self):
        self.assertEqual(27, len(self.get_odds_combo))
