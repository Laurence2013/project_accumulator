from django.test import TestCase
from accumulator.views import IndexPageGamesView
from accumulator.models import *

class AllMethodsShould(TestCase, IndexPageGamesView):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')

        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        Game.objects.create(id=3, games='FC Bayern vs Barcelona', time='19:45:00', date_of_game='2017-02-27')

        Odd.objects.create(id=1, home_odds=0.91, draw_odds=2.75, away_odds=3.00,
        games=Game.objects.get(pk=1))

        Odd.objects.create(id=2, home_odds=1.30, draw_odds=2.00, away_odds=2.20,
        games=Game.objects.get(pk=2))

        Odd.objects.create(id=3, home_odds=1.05, draw_odds=2.10, away_odds=2.75,
        games=Game.objects.get(pk=3))

    def test_TheLengthOfOddsList(self):
        self.assertEqual(12, len(self.get_odds()))

    def test_AllBeFromDecimalToFloatingOrInteger(self):
        compareList = [1, 0.91, 2.75, 3.0, 2, 1.3, 2.0, 2.2, 3, 1.05, 2.1, 2.75]
        self.assertListEqual(compareList, self.get_odds())
