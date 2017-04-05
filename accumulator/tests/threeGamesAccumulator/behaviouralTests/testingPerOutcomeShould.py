from django.test import TestCase
from accumulator.combinations.threeGamesAccumulator import ThreeGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 1st behavioural test '''

class TestingPerOutcomeShould(TestCase, ThreeGamesAccumulator, GeneralGamesAccumulator):
    def setUp(self):
        self.games = {
            'myGame1':{'id': 1, 'game': 'Fiorentina vs Torino'},
            'myGame2':{'id': 2, 'game': 'Arouca vs Belenenses'},
            'myGame3':{'id': 3, 'game': 'St Pauli vs Karlsruhe'},
        }
        self.get_combo = self.combinationsForThreeGames()
        self.combo = self.get_per_outcome(self.get_combo)

    def test_LoopIndex_0_AndCompareThatTupleIs_1_And_Tuple1Is_H(self):
        self.assertEqual([int(1),str('H')], self.combo[0])

    def test_LoopIndex_1_AndCompareThatTupleIs_1_And_Tuple1Is_H(self):
        self.assertEqual([int(1),str('H')], self.combo[1])

    def test_LoopIndex_2_AndCompareThatTupleIs_1_And_Tuple1Is_H(self):
        self.assertEqual([int(1),str('H')], self.combo[2])

    def test_LoopIndex_3_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(2),str('H')], self.combo[3])

    def test_LoopIndex_4_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(2),str('H')], self.combo[4])

    def test_LoopIndex_5_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(2),str('D')], self.combo[5])

    def test_GetLengthOfCombo(self):
        self.assertEqual(81, len(self.combo))
