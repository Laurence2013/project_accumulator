from django.test import TestCase
from accumulator.combinations.fourGamesAccumulator import FourGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator

''' This is the 1st behavioural test '''

class TestingPerOutcomeShould(TestCase, FourGamesAccumulator, GeneralGamesAccumulator):
    def setUp(self):
        self.games = {
            'myGame1':{'id': 4, 'games': 'Crystal Palace vs Arsenal'},
            'myGame2':{'id': 5, 'games': 'Real Sociedad vs Sporting Gijon'},
            'myGame3':{'id': 6, 'games': 'Maritimo vs Chaves'},
            'myGame4':{'id': 7, 'games': 'Defensa y Justicia vs Olimpio Bahia Blanca'},
        }
        self.get_combo = self.combinationsForFourGames()
        self.combo = self.get_per_outcome(self.get_combo)

    def test_LoopIndex_0_AndCompareThatTupleIs_1_And_Tuple1Is_H(self):
        self.assertEqual([int(1),str('H')], self.combo[0])

    def test_LoopIndex_1_AndCompareThatTupleIs_1_And_Tuple1Is_H(self):
        self.assertEqual([int(1),str('H')], self.combo[1])

    def test_LoopIndex_2_AndCompareThatTupleIs_1_And_Tuple1Is_H(self):
        self.assertEqual([int(1),str('H')], self.combo[2])

    def test_LoopIndex_3_AndCompareThatTupleIs_1_And_Tuple1Is_H(self):
        self.assertEqual([int(1),str('H')], self.combo[3])

    def test_LoopIndex_4_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(2),str('H')], self.combo[4])

    def test_LoopIndex_5_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(2),str('H')], self.combo[5])

    def test_LoopIndex_6_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(2),str('H')], self.combo[6])

    def test_LoopIndex_7_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(2),str('D')], self.combo[7])

    def test_LoopIndex_8_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(3),str('H')], self.combo[8])

    def test_LoopIndex_9_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(3),str('H')], self.combo[9])

    def test_LoopIndex_10_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(3),str('H')], self.combo[10])

    def test_LoopIndex_11_AndCompareThatTupleIs_2_And_Tuple2Is_H(self):
        self.assertEqual([int(3),str('A')], self.combo[11])

    def test_GetLengthOfCombo(self):
        self.assertEqual(324, len(self.combo))
