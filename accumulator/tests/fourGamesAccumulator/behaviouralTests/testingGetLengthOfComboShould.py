from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.fourGamesAccumulator import FourGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 5th behavioural test '''

class TestingGetLengthOfComboShould(TestCase, GeneralGamesAccumulator, FourGamesAccumulator):
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
        self.get_num = list(self.break_list_into_equal_chunks(self.new_combo,4))
        self.get_odds_combo = self.get_length_of_combo(self.get_num, 81, 4)

    def test_Index_0_TheOutcomeShouldBe_4H_5H_6H_7H(self):
        testList = [4, 'H', 5, 'H', 6, 'H', 7, 'H']
        self.assertListEqual(testList, self.get_odds_combo[0])

    def test_Index_1_TheOutcomeShouldBe_4H_5H_6H_7D(self):
        testList = [4, 'H', 5, 'H', 6, 'H', 7, 'D']
        self.assertListEqual(testList, self.get_odds_combo[1])

    def test_Index_2_TheOutcomeShouldBe_4H_5H_6H_7A(self):
        testList = [4, 'H', 5, 'H', 6, 'H', 7, 'A']
        self.assertListEqual(testList, self.get_odds_combo[2])

    def test_Index_3_TheOutcomeShouldBe_4H_5H_6D_7H(self):
        testList = [4, 'H', 5, 'H', 6, 'D', 7, 'H']
        self.assertListEqual(testList, self.get_odds_combo[3])

    def test_Index_4_TheOutcomeShouldBe_4H_5H_6D_7D(self):
        testList = [4, 'H', 5, 'H', 6, 'D', 7, 'D']
        self.assertListEqual(testList, self.get_odds_combo[4])

    def test_Index_5_TheOutcomeShouldBe_4H_5H_6D_7A(self):
        testList = [4, 'H', 5, 'H', 6, 'D', 7, 'A']
        self.assertListEqual(testList, self.get_odds_combo[5])

    def test_GetLengthOfGetOddsCombo(self):
        self.assertEqual(81, len(self.get_odds_combo))
