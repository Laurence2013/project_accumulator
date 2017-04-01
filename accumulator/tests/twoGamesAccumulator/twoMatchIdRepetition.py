from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator

class TwoMatchIdRepetition(TestCase, TwoGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForTwoGames(len(self.games))
        self.get_games = self.getGameCombinations(self.get_combo, self.games)

    def test_GetGameFromIndex_0_AndAssertIfItIsEqualTo_1(self):
        self.assertEqual([1],self.get_games[0])

    def test_GetGameFromIndex_1_AndAssertIfItIsEqualTo_2(self):
        self.assertEqual([2],self.get_games[1])

    def test_GetGameFromIndex_2_AndAssertIfItIsEqualTo_1(self):
        self.assertEqual([1],self.get_games[2])

    def test_GetGameFromIndex_3_AndAssertIfItIsEqualTo_2(self):
        self.assertEqual([2],self.get_games[3])

    def test_GetGameFromIndex_4_AndAssertIfItIsEqualTo_1(self):
        self.assertEqual([1],self.get_games[4])
