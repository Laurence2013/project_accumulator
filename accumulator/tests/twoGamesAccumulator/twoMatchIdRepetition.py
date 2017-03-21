from django.test import TestCase
from accumulator.models import Game
from accumulator.views import combinationsForTwoGames, getGameCombinations

class TwoMatchIdRepetition(TestCase):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

    def test_GetGameFromIndex_0_AndAssertIfItIsEqualTo_1(self):
        games = Game.objects.values_list('pk', flat = True)
        get_combo = combinationsForTwoGames(len(games))
        get_games = getGameCombinations(get_combo, games)
        self.assertEqual([1],get_games[0])
        
    def test_GetGameFromIndex_1_AndAssertIfItIsEqualTo_2(self):
        games = Game.objects.values_list('pk', flat = True)
        get_combo = combinationsForTwoGames(len(games))
        get_games = getGameCombinations(get_combo, games)
        self.assertEqual([2],get_games[1])

    def test_GetGameFromIndex_2_AndAssertIfItIsEqualTo_1(self):
        games = Game.objects.values_list('pk', flat = True)
        get_combo = combinationsForTwoGames(len(games))
        get_games = getGameCombinations(get_combo, games)
        self.assertEqual([1],get_games[2])

    def test_GetGameFromIndex_3_AndAssertIfItIsEqualTo_2(self):
        games = Game.objects.values_list('pk', flat = True)
        get_combo = combinationsForTwoGames(len(games))
        get_games = getGameCombinations(get_combo, games)
        self.assertEqual([2],get_games[3])
