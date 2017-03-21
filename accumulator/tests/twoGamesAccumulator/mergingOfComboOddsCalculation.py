from django.test import TestCase
from accumulator.views import index
from decimal import Decimal
from accumulator.models import Game, Odd
from accumulator.views import *

class MergingOfComboOddsCalculation(TestCase):
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
        self.getAllCombinations = mergePerGameWithOdds(self.getOddsCombo, self.getCombinedDecimals, self.getCombinedCalculation)

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_0(self):
        index0List = ([1, 'H', 2, 'H'], [Decimal('0.91'), Decimal('1.30')], Decimal('3.3930'))
        self.assertTupleEqual(index0List, self.getAllCombinations[0])

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_1(self):
        index1List = ([1, 'H', 2, 'D'], [Decimal('0.91'), Decimal('2.00')], Decimal('4.7300'))
        self.assertTupleEqual(index1List, self.getAllCombinations[1])

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_2(self):
        index2List = ([1, 'H', 2, 'A'], [Decimal('0.91'), Decimal('2.20')], Decimal('5.1120'))
        self.assertTupleEqual(index2List, self.getAllCombinations[2])

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_3(self):
        index3List = ([1, 'D', 2, 'H'], [Decimal('2.75'), Decimal('1.30')], Decimal('7.6250'))
        self.assertTupleEqual(index3List, self.getAllCombinations[3])

    def test_CombineTwoMatchesWithItsOddsAndCalculationAtIndex_4(self):
        index4List = ([1, 'D', 2, 'D'], [Decimal('2.75'), Decimal('2.00')], Decimal('10.2500'))
        self.assertTupleEqual(index4List, self.getAllCombinations[4])
