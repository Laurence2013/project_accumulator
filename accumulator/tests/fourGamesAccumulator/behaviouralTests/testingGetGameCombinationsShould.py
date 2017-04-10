from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.fourGamesAccumulator import FourGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 2nd behavioural test '''

class TestingGetGameCombinationsShould(TestCase, FourGamesAccumulator, GeneralGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=4, games='Crystal Palace vs Arsenal', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=5, games='Real Sociedad vs Sporting Gijon', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=6, games='Maritimo vs Chaves', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=7, games='Defensa y Justicia vs Olimpio Bahia Blanca', time='19:45:00', date_of_game='2017-02-27')

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForFourGames()
        self.combos = self.get_per_outcome(self.get_combo)
        self.get_games = self.get_game_combinations(self.get_combo, self.games)

    '''
    [[4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7], [4], [5], [6], [7]]
    '''

    def test_GetGamesListAtIndex_0(self):
        self.assertEqual([4], self.get_games[0])

    def test_GetGamesListAtIndex_1(self):
        self.assertEqual([5], self.get_games[1])

    def test_GetGamesListAtIndex_2(self):
        self.assertEqual([6], self.get_games[2])

    def test_GetGamesListAtIndex_3(self):
        self.assertEqual([7], self.get_games[3])

    def test_GetGamesListAtIndex_4(self):
        self.assertEqual([4], self.get_games[4])

    def test_GetGamesListAtIndex_5(self):
        self.assertEqual([5], self.get_games[5])

    def test_GetGamesListAtIndex_6(self):
        self.assertEqual([6], self.get_games[6])

    def test_GetGamesListAtIndex_7(self):
        self.assertEqual([7], self.get_games[7])

    def test_GetGamesListAtIndex_4(self):
        self.assertEqual([4], self.get_games[8])

    def test_GetGamesListAtIndex_5(self):
        self.assertEqual([5], self.get_games[9])

    def test_GetGamesListAtIndex_6(self):
        self.assertEqual([6], self.get_games[10])

    def test_GetGamesListAtIndex_7(self):
        self.assertEqual([7], self.get_games[11])

    def test_GetLengthOfGetGames(self):
        self.assertEqual(324, len(self.get_games))
