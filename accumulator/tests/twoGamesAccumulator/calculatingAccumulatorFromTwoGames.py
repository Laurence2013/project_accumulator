from django.test import TestCase
from accumulator.views import index
from decimal import Decimal
from accumulator.models import Game, Odd
from accumulator.views import combinationsForTwoGames, getGameCombinations, getPerOutcome, combineComboListWithGameList, breakListIntoEqualChunks, getIdAndOutcome, getLengthOfCombo, getTwoCombinedGames, calculateOddsForTwoMatches

class CalculatingAccumulatorFromTwoGames(TestCase):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        Odd.objects.create(id=1, home_odds=0.91, draw_odds=2.75, away_odds=3.00,
        games=Game.objects.get(pk=1))
        Odd.objects.create(id=2, home_odds=1.30, draw_odds=2.00, away_odds=2.20,
        games=Game.objects.get(pk=2))

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = combinationsForTwoGames(len(self.games))
        self.get_games = getGameCombinations(self.get_combo, self.games)
        self.combos = getPerOutcome(self.get_combo)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = combineComboListWithGameList(self.combos, self.get_games, self.match, self.game)
        self.getNum = list(breakListIntoEqualChunks(self.new_combo, 2))
        self.getOddsCombo = getLengthOfCombo(self.getNum,9)
        self.getAllOddsCombo = getTwoCombinedGames(self.getOddsCombo)
        self.getCombinedDecimals = list(breakListIntoEqualChunks(self.getAllOddsCombo, 2))
        self.getCombinedCalculation = calculateOddsForTwoMatches(self.getCombinedDecimals)

    def test_GetCalculationOfTwoGamesIndex_0(self):
        self.assertEqual(Decimal('3.3930'), self.getCombinedCalculation[0])

    def test_GetCalculationOfTwoGamesIndex_1(self):
        self.assertEqual(Decimal('4.7300'), self.getCombinedCalculation[1])

    def test_GetCalculationOfTwoGamesIndex_2(self):
        self.assertEqual(Decimal('5.1120'), self.getCombinedCalculation[2])

    def test_GetCalculationOfTwoGamesIndex_3(self):
        self.assertEqual(Decimal('7.6250'), self.getCombinedCalculation[3])
