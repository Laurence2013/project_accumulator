from django.test import TestCase
from accumulator.views import IndexPageGamesView
from accumulator.models import *
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

    def test_CombiningTheGamesWithItsHomeDrawAndAwayOddsIndex_0(self):
        comboGame = (1, 'Fiorentina vs Torino', 1, Decimal('0.91'), Decimal('2.75'), Decimal('3.00'))
        self.assertTupleEqual(comboGame, self.get_games()[0])

    def test_CombiningTheGamesWithItsHomeDrawAndAwayOddsIndex_1(self):
        comboGame = (2, 'Arouca vs Belenenses', 2, Decimal('1.30'), Decimal('2.00'), Decimal('2.20'))
        self.assertTupleEqual(comboGame, self.get_games()[1])

    def test_CombiningTheGamesWithItsHomeDrawAndAwayOddsIndex_2(self):
        comboGame = (3, 'St Pauli vs Karlsruhe', 3, Decimal('1.05'), Decimal('2.10'), Decimal('2.75'))
        self.assertTupleEqual(comboGame, self.get_games()[2])
    
