from django.test import TestCase
from accumulator.models import Game

class OrderOfGames(TestCase):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        self.hh_combo = [('H', 'H'), ('H', 'D'), ('H', 'A'), ('D', 'H'), ('D', 'D'), ('D', 'A'), ('A', 'H'), ('A', 'D'), ('A', 'A')]

        self.games = {
            'myGame1':{'id': 1, 'game': 'Fiorentina vs Torino'},
            'myGame2':{'id': 2, 'game': 'Arouca vs Belenenses'},
        }

    def test_AssertThatPrimaryKey_1_IdIsEqualToTheGameChosen(self):
        game = Game.objects.get(pk=1)
        myGame = {'id': game.pk, 'game': game.games}
        equalGame = {'id': 1, 'game': 'Fiorentina vs Torino'}
        self.assertDictEqual(equalGame, myGame)

    def test_AssertThatPrimaryKey_2_IdIsEqualToTheGameChosen(self):
        game = Game.objects.get(pk=2)
        myGame = {'id': game.pk, 'game': game.games}
        equalGame = {'id': 2, 'game': 'Arouca vs Belenenses'}
        self.assertDictEqual(equalGame, myGame)

    def test_LengthOfGameIsEqualToTotalGameWhichIs_2(self):
        self.assertEqual(len(self.games), len(self.hh_combo[0]))

    def test_TurnTheFirstOutcomeToLowerCase_H_to_h(self):
        self.assertEqual('h', self.hh_combo[0][0].lower())

    def test_TurnTheSecondtOutcomeLowerCase_A_to_a(self):
        self.assertEqual('h', self.hh_combo[0][1].lower())

    def test_GetHomeId_1_AndOutcome_H_AndCompareToOriginalDictionary(self):
        newDict = {'id':int(self.games['myGame1']['id']),'outcome':str(self.hh_combo[0][0].lower())}
        origDict = {'id':1, 'outcome':'h'}
        self.assertDictEqual(origDict, newDict)

    def test_TotalNumberOfGamesIs_2(self):
        no_games = Game.objects.all()
        self.assertEqual(2, len(no_games))
