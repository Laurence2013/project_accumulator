from django.test import TestCase
from accumulator.models import Game, Odd
from accumulator.combinations.threeGamesAccumulator import ThreeGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator
from decimal import Decimal

''' This is the 7th behavioural test '''

class TestingBreakListIntoEqualChunksShould(TestCase, GeneralGamesAccumulator, ThreeGamesAccumulator):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=3, games='St Pauli vs Karlsruhe', time='19:45:00', date_of_game='2017-02-27')

        Odd.objects.create(id=1, home_odds=0.91, draw_odds=2.75, away_odds=3.00,
        games=Game.objects.get(pk=1))
        Odd.objects.create(id=2, home_odds=1.30, draw_odds=2.00, away_odds=2.20,
        games=Game.objects.get(pk=2))
        Odd.objects.create(id=3, home_odds=1.05, draw_odds=2.10, away_odds=2.75,
        games=Game.objects.get(pk=3))

        self.games = Game.objects.values_list('pk', flat = True)
        self.get_combo = self.combinationsForThreeGames()
        self.combos = self.get_per_outcome(self.get_combo)
        self.get_games = self.get_game_combinations(self.get_combo, self.games)
        self.match = int(len(self.get_games))
        self.game = int(len(self.combos))
        self.new_combo = self.combine_combo_list_with_game_list(self.combos, self.get_games, self.match, self.game)
        self.get_num = list(self.break_list_into_equal_chunks(self.new_combo,3))
        self.get_odds_combo = self.get_length_of_combo(self.get_num,27, 3)
        self.get_all_odds_combo = self.get_combined_games(self.get_odds_combo)
        self.get_combined_decimals = list(self.break_list_into_equal_chunks(self.get_all_odds_combo, 3))

    def test_AtIndex_0_ItShouldBe_091_130_105(self):
        myList = [Decimal('0.91'), Decimal('1.30'), Decimal('1.05')]
        self.assertListEqual(myList, self.get_combined_decimals[0])

    def test_AtIndex_1_ItShouldBe_091_130_210(self):
        myList = [Decimal('0.91'), Decimal('1.30'), Decimal('2.10')]
        self.assertListEqual(myList, self.get_combined_decimals[1])

    def test_AtIndex_2_ItShouldBe_091_130_275(self):
        myList = [Decimal('0.91'), Decimal('1.30'), Decimal('2.75')]
        self.assertListEqual(myList, self.get_combined_decimals[2])

    def test_AtIndex_3_ItShouldBe_091_200_105(self):
        myList = [Decimal('0.91'), Decimal('2.00'), Decimal('1.05')]
        self.assertListEqual(myList, self.get_combined_decimals[3])
