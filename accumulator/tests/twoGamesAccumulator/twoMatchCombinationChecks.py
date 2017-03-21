from django.test import TestCase
from accumulator.views import combinationsForTwoGames, getPerOutcome

class TwoMatchCombinations(TestCase):
    def setUp(self):
        self.games = {
            'myGame1':{'id': 1, 'game': 'Fiorentina vs Torino'},
            'myGame2':{'id': 2, 'game': 'Arouca vs Belenenses'},
        }

    def test_LoopIndex_0_AndCompareThatTuple0Is_1_And_Tuple1Is_H(self):
        get_combo = combinationsForTwoGames(len(self.games))
        combo = getPerOutcome(get_combo)
        self.assertEqual([int(1),str('H')], combo[0])

    def test_LoopIndex_1_AndCompareThatTuple0Is_1_And_Tuple1Is_H(self):
        get_combo = combinationsForTwoGames(len(self.games))
        combo = getPerOutcome(get_combo)
        self.assertEqual([int(1),str('H')], combo[1])

    def test_LoopIndex_2_AndCompareThatTuple0Is_2_And_Tuple1Is_H(self):
        get_combo = combinationsForTwoGames(len(self.games))
        combo = getPerOutcome(get_combo)
        self.assertEqual([int(2),str('H')], combo[2])

    def test_LoopIndex_3_AndCompareThatTuple0Is_2_And_Tuple1Is_D(self):
        get_combo = combinationsForTwoGames(len(self.games))
        combo = getPerOutcome(get_combo)
        self.assertEqual([int(2),str('D')], combo[3])

    def test_LoopIndex_4_AndCompareThatTuple0Is_3_And_Tuple1Is_H(self):
        get_combo = combinationsForTwoGames(len(self.games))
        combo = getPerOutcome(get_combo)
        self.assertEqual([int(3),str('H')], combo[4])

    def test_LoopIndex_5_AndCompareThatTuple0Is_3_And_Tuple1Is_A(self):
        get_combo = combinationsForTwoGames(len(self.games))
        combo = getPerOutcome(get_combo)
        self.assertEqual([int(3),str('A')], combo[5])

    def test_LoopIndex_6_AndCompareThatTuple0Is_4_And_Tuple1Is_D(self):
        get_combo = combinationsForTwoGames(len(self.games))
        combo = getPerOutcome(get_combo)
        self.assertEqual([int(4),str('D')], combo[6])

    def test_LoopIndex_7_AndCompareThatTuple0Is_4_And_Tuple1Is_H(self):
        get_combo = combinationsForTwoGames(len(self.games))
        combo = getPerOutcome(get_combo)
        self.assertEqual([int(4),str('H')], combo[7])
