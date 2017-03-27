from django.test import TestCase
from decimal import Decimal
from accumulator.models import Game, Odd
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator

class MergeTheOddsFromTheCombinations(TestCase, TwoGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        Odd.objects.create(id=1, home_odds=0.91, draw_odds=2.75, away_odds=3.00,
        games=Game.objects.get(pk=1))
        Odd.objects.create(id=2, home_odds=1.30, draw_odds=2.00, away_odds=2.20,
        games=Game.objects.get(pk=2))

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForTwoGames(len(self.games))
        self.get_games = self.getGameCombinations(self.get_combo, self.games)
        self.combos = self.getPerOutcome(self.get_combo)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = self.combineComboListWithGameList(self.combos, self.get_games, self.match, self.game)
        self.getNum = list(self.breakListIntoEqualChunks(self.new_combo, 2))
        self.getOddsCombo = self.getLengthOfCombo(self.getNum,9)
        self.getAllOddsCombo = self.getTwoCombinedGames(self.getOddsCombo)

    def test_GettingTwoCombinedGamesFromIndex_0(self):
        self.assertEqual(Decimal('0.91'), self.getAllOddsCombo[0])

    def test_GettingTwoCombinedGamesFromIndex_1(self):
        self.assertEqual(Decimal('1.30'), self.getAllOddsCombo[1])

    def test_GettingTwoCombinedGamesFromIndex_2(self):
        self.assertEqual(Decimal('0.91'), self.getAllOddsCombo[2])

    def test_GettingTwoCombinedGamesFromIndex_3(self):
        self.assertEqual(Decimal('2.00'), self.getAllOddsCombo[3])

    def test_GettingTwoCombinedGamesFromIndex_4(self):
        self.assertEqual(Decimal('0.91'), self.getAllOddsCombo[4])

    def test_GettingTwoCombinedGamesFromIndex_5(self):
        self.assertEqual(Decimal('2.20'), self.getAllOddsCombo[5])
