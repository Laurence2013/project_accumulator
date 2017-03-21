from django.test import TestCase
from accumulator.views import index
from accumulator.models import Game, Odd
from accumulator.views import combinationsForTwoGames, getGameCombinations, getPerOutcome, combineComboListWithGameList, breakListIntoEqualChunks, getIdAndOutcome, getLengthOfCombo

class CombiningAllTheTwoGamesCombinations(TestCase):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = combinationsForTwoGames(len(self.games))
        self.get_games = getGameCombinations(self.get_combo, self.games)
        self.combos = getPerOutcome(self.get_combo)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = combineComboListWithGameList(self.combos, self.get_games, self.match, self.game)

    def test_GetTheFirstIndex_0_1_WhereItsValueIs_1(self):
        self.assertEqual(1, self.new_combo[0][1])

    def test_GetTheFirstIndex_1_1_WhereItsValueIs_1(self):
        self.assertEqual(1, self.new_combo[1][1])

    def test_GetTheFirstIndex_2_1_WhereItsValueIs_2(self):
        self.assertEqual(2, self.new_combo[2][1])

    def test_GetTheFirstIndex_3_1_WhereItsValueIs_2(self):
        self.assertEqual(2, self.new_combo[3][1])

    def test_GetTheFirstIndex_4_1_WhereItsValueIs_3(self):
        self.assertEqual(3, self.new_combo[4][1])

    def test_GetTheFirstIndex_5_1_WhereItsValueIs_3(self):
        self.assertEqual(3, self.new_combo[5][1])

    def test_BreakListInto_2_EqualChunksIndex_0(self):
        getNum = list(breakListIntoEqualChunks(self.new_combo, 2))
        listCombo = [(1, 1, 'H'), (2, 1, 'H')]
        self.assertListEqual(listCombo, getNum[0])

    def test_BreakListInto_2_EqualChunksIndex_1(self):
        getNum = list(breakListIntoEqualChunks(self.new_combo, 2))
        listCombo = [(1, 2, 'H'), (2, 2, 'D')]
        self.assertListEqual(listCombo, getNum[1])

    def test_GetMergingOfTwoOutcomesIndex_0_0_0(self):
        getNum = list(breakListIntoEqualChunks(self.new_combo, 2))
        self.assertEqual(1, getNum[0][0][0])

    def test_GroupTwoMatchesForOddsTableIndex_0(self):
        getNum = list(breakListIntoEqualChunks(self.new_combo, 2))
        getOddsCombo = getLengthOfCombo(getNum,9)
        self.assertEqual([1,'H',2,'H'], getOddsCombo[0])

    def test_GroupTwoMatchesForOddsTableIndex_1(self):
        getNum = list(breakListIntoEqualChunks(self.new_combo, 2))
        getOddsCombo = getLengthOfCombo(getNum,9)
        self.assertEqual([1,'H',2,'D'], getOddsCombo[1])

    def test_GroupTwoMatchesForOddsTableIndex_2(self):
        getNum = list(breakListIntoEqualChunks(self.new_combo, 2))
        getOddsCombo = getLengthOfCombo(getNum,9)
        self.assertEqual([1,'H',2,'A'], getOddsCombo[2])

    def test_GroupTwoMatchesForOddsTableIndex_3(self):
        getNum = list(breakListIntoEqualChunks(self.new_combo, 2))
        getOddsCombo = getLengthOfCombo(getNum,9)
        self.assertEqual([1,'D',2,'H'], getOddsCombo[3])
