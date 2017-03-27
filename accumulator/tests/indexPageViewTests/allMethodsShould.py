from django.test import TestCase
from accumulator.views import IndexPageGamesView
from accumulator.models import Game, Odd
from decimal import Decimal

class AllMethodsShould(TestCase, IndexPageGamesView):
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

        self.odds_games = [(1, 'Fiorentina vs Torino', 1, Decimal('0.91'), Decimal('2.75'), Decimal('3.00')), (2, 'Arouca vs Belenenses', 2, Decimal('1.30'), Decimal('2.00'), Decimal('2.20')), (3, 'St Pauli vs Karlsruhe', 3, Decimal('1.05'), Decimal('2.10'), Decimal('2.75'))]

        self.comboGames = ['Fiorentina vs Torino', Decimal('0.91'), Decimal('2.75'), Decimal('3.00'), 'Arouca vs Belenenses', Decimal('1.30'), Decimal('2.00'), Decimal('2.20'), 'St Pauli vs Karlsruhe', Decimal('1.05'), Decimal('2.10'), Decimal('2.75')]

        self.finalComboGames = ['Fiorentina vs Torino', 0.91, 2.75, 3.0, 'Arouca vs Belenenses', 1.3, 2.0, 2.2, 'St Pauli vs Karlsruhe', 1.05, 2.1, 2.75]

        self.finalAccumulator = [['Fiorentina vs Torino', 0.91, 2.75, 3.0], ['Arouca vs Belenenses', 1.3, 2.0, 2.2], ['St Pauli vs Karlsruhe', 1.05, 2.1, 2.75]]

    def test_CombiningTheGamesWithItsHomeDrawAndAwayOddsIndex_0(self):
        comboGame = (1, 'Fiorentina vs Torino', 1, Decimal('0.91'), Decimal('2.75'), Decimal('3.00'))
        self.assertTupleEqual(comboGame, self.get_games()[0])

    def test_CombiningTheGamesWithItsHomeDrawAndAwayOddsIndex_1(self):
        comboGame = (2, 'Arouca vs Belenenses', 2, Decimal('1.30'), Decimal('2.00'), Decimal('2.20'))
        self.assertTupleEqual(comboGame, self.get_games()[1])

    def test_CombiningTheGamesWithItsHomeDrawAndAwayOddsIndex_2(self):
        comboGame = (3, 'St Pauli vs Karlsruhe', 3, Decimal('1.05'), Decimal('2.10'), Decimal('2.75'))
        self.assertTupleEqual(comboGame, self.get_games()[2])

    def test_GetGamesAndOddsByNotIncludingPrimaryKeys(self):
        self.assertListEqual(self.comboGames, self.get_ammended_games(self.odds_games))

    def test_ChangeAllTheElementsThatHasDecimals(self):
        self.assertListEqual(self.finalComboGames, self.get_final_game(self.comboGames))

    def test_GetListAndSplitItIntoEqualParts(self):
        self.assertListEqual(self.finalAccumulator, list(self.breakListIntoEqualChunks(self.finalComboGames, 4)))
