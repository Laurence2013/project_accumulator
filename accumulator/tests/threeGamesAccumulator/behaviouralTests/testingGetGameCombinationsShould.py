from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.threeGamesAccumulator import ThreeGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 2nd behavioural test '''

class TestingGetGameCombinationsShould(TestCase, ThreeGamesAccumulator, GeneralGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=3, games='St Pauli vs Karlsruhe', time='19:45:00', date_of_game='2017-02-27')

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForThreeGames()
        self.combos = self.get_per_outcome(self.get_combo)
        self.get_games = self.get_game_combinations(self.get_combo, self.games)
    '''
    [[1], [2], [3], [1], [2], [3], [1], [2], [3], [1], [2], [3], [1], [2], [3], [1], [2], [3], [1], [2], [3], [1], [2], [3], [1], [2], [3]]
    '''
    def test_GetGamesListAtIndex_0(self):
        self.assertEqual([1], self.get_games[0])

    def test_GetGamesListAtIndex_1(self):
        self.assertEqual([2], self.get_games[1])

    def test_GetGamesListAtIndex_2(self):
        self.assertEqual([3], self.get_games[2])

    def test_GetGamesListAtIndex_3(self):
        self.assertEqual([1], self.get_games[3])

    def test_GetGamesListAtIndex_4(self):
        self.assertEqual([2], self.get_games[4])

    def test_GetGamesListAtIndex_5(self):
        self.assertEqual([3], self.get_games[5])

    def test_GetLengthOfGetGames(self):
        self.assertEqual(81, len(self.get_games))
