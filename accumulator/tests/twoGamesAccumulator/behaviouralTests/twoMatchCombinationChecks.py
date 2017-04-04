from django.test import TestCase
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator

''' This is the 1st behavioural test '''

class TwoMatchCombinationsChecks(TestCase, TwoGamesAccumulator):
    def setUp(self):
        self.games = {
            'myGame1':{'id': 1, 'game': 'Fiorentina vs Torino'},
            'myGame2':{'id': 2, 'game': 'Arouca vs Belenenses'},
        }
        self.get_combo = self.combinationsForTwoGames(len(self.games))
        self.combo = self.getPerOutcome(self.get_combo)

    def test_LoopIndex_0_AndCompareThatTupleIs_1_And_Tuple1Is_H(self):
        self.assertEqual([int(1),str('H')], self.combo[0])

    def test_LoopIndex_1_AndCompareThatTupleIs_1_And_Tuple1Is_H(self):
        self.assertEqual([int(1),str('H')], self.combo[1])

    def test_LoopIndex_2_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(2),str('H')], self.combo[2])

    def test_LoopIndex_3_AndCompareThatTupleIs_2_And_Tuple2Is_D(self):
        self.assertEqual([int(2),str('D')], self.combo[3])

    def test_LoopIndex_4_AndCompareThatTupleIs_3_And_Tuple3Is_H(self):
        self.assertEqual([int(3),str('H')], self.combo[4])

    def test_LoopIndex_5_AndCompareThatTupleIs_3_And_Tuple3Is_A(self):
        self.assertEqual([int(3),str('A')], self.combo[5])

    def test_LoopIndex_6_AndCompareThatTupleIs_4_And_Tuple4Is_D(self):
        self.assertEqual([int(4),str('D')], self.combo[6])

    def test_LoopIndex_7_AndCompareThatTupleIs_4_And_Tuple4Is_H(self):
        self.assertEqual([int(4),str('H')], self.combo[7])
