from django.test import TestCase
from accumulator.models import Game
from accumulator.views import combinationsForTwoGames, getPerOutcome, getGameCombinations, combineComboListWithGameList

class TwoMatchCombinations(TestCase):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        self.games = {
            'myGame1':{'id': 1, 'game': 'Fiorentina vs Torino'},
            'myGame2':{'id': 2, 'game': 'Arouca vs Belenenses'},
        }

    def test_GetGameIdsAndTheOutcomeOfCombinationLengthIs_9(self):
        games = Game.objects.values_list('pk', flat = True)
        get_combo = combinationsForTwoGames(len(games))
        self.assertEqual(9, len(get_combo))

    def test_CheckThatTheFirstTupleIs_H_H(self):
        get_combo = combinationsForTwoGames(len(self.games))
        self.assertEqual(('H','H'), get_combo[0])

    def test_TurnTheFirstFirstTupleTurnFrom_H_to_h(self):
        get_combo = combinationsForTwoGames(len(self.games))
        self.assertEqual(('h'), get_combo[0][0].lower())

    def test_CheckThatTheLengthOfTheCombinationInListIs_18(self):
        games = Game.objects.values_list('pk', flat = True)
        get_combo = combinationsForTwoGames(len(games))
        combos = getPerOutcome(get_combo)
        self.assertEqual(18, len(combos))

    def test_ReturnFalseWhenMatchListAndGameListAreBothNotEqualTo_18(self):
        games = Game.objects.values_list('pk', flat = True)
        get_combo = combinationsForTwoGames(len(games))
        get_games = getGameCombinations(get_combo,games)
        combos = getPerOutcome(get_combo)
        new_combo = combineComboListWithGameList(combos, get_games, 12, 18)
        self.assertFalse(new_combo)

    def test_GetPrimaryKeysFromIndex_0(self):
        game = Game.objects.values_list('id', flat = True)
        self.assertEqual(int(1), game[0])

    def test_GetPrimaryKeysFromIndex_1(self):
        game = Game.objects.values_list('id', flat = True)
        self.assertEqual(int(2), game[1])
