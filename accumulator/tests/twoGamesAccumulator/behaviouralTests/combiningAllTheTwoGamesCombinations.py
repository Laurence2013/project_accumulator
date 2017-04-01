from django.test import TestCase
from accumulator.models import Game
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator

''' This is the 3rd behavioural test '''

class CombiningAllTheTwoGamesCombinations(TestCase, TwoGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForTwoGames(len(self.games))
        self.get_games = self.getGameCombinations(self.get_combo, self.games)
        self.combos = self.getPerOutcome(self.get_combo)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = self.combineComboListWithGameList(self.combos, self.get_games, self.match, self.game)
        self.getNum = list(self.breakListIntoEqualChunks(self.new_combo, 2))
        self.getOddsCombo = self.getLengthOfCombo(self.getNum,9)

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
        listCombo = [(1, 1, 'H'), (2, 1, 'H')]
        self.assertListEqual(listCombo, self.getNum[0])

    def test_BreakListInto_2_EqualChunksIndex_1(self):
        listCombo = [(1, 2, 'H'), (2, 2, 'D')]
        self.assertListEqual(listCombo, self.getNum[1])

    def test_GetMergingOfTwoOutcomesIndex_0_0_0(self):
        self.assertEqual(1, self.getNum[0][0][0])

    def test_GroupTwoMatchesForOddsTableIndex_0(self):
        self.assertEqual([1,'H',2,'H'], self.getOddsCombo[0])

    def test_GroupTwoMatchesForOddsTableIndex_1(self):
        self.assertEqual([1,'H',2,'D'], self.getOddsCombo[1])

    def test_GroupTwoMatchesForOddsTableIndex_2(self):
        self.assertEqual([1,'H',2,'A'], self.getOddsCombo[2])

    def test_GroupTwoMatchesForOddsTableIndex_3(self):
        self.assertEqual([1,'D',2,'H'], self.getOddsCombo[3])
