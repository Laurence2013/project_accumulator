from django.test import TestCase
from accumulator.models import Game, Odd
from decimal import Decimal

class Combinations(TestCase):
    def setUp(self):
        Game.objects.create(id=1, games='Fiorentina vs Torino', time='19:45:00', date_of_game='2017-02-27')
        Game.objects.create(id=2, games='Arouca vs Belenenses', time='19:45:00', date_of_game='2017-02-27')

        Odd.objects.create(id=1, home_odds=0.91, draw_odds=2.75, away_odds=3.00,
        games=Game.objects.get(pk=1))
        Odd.objects.create(id=3, home_odds=1.30, draw_odds=2.00, away_odds=2.20,
        games=Game.objects.get(pk=2))

    def test_GetTheFirstGameFromAccumulatorGameTable(self):
        game = Game.objects.get(id=1)
        match = str(game)
        self.assertEqual('Fiorentina vs Torino', match)

    def test_GetTheSecondGameFromAccumulatorGameTable(self):
        game = Game.objects.get(id=2)
        match = str(game)
        self.assertEqual('Arouca vs Belenenses', match)

    def test_ThatTheOddsTableIsEqualTo_FiorentinaVsTorino(self):
        odd = Odd.objects.get(id=1)
        match = str(odd)
        self.assertEqual('Fiorentina vs Torino', match)

    def test_ThatTheOddsTableIsEqualTo_AroucoVsBelenenses(self):
        game = Game.objects.get(id=2)
        match = str(game)
        self.assertEqual('Arouca vs Belenenses', match)

    def test_ThatTheHomeOddsIs_091(self):
        odd = Odd.objects.get(id=1)
        self.assertEqual(Decimal('0.91'), odd.home_odds)

    def test_ThatTheDrawOddsIs_275(self):
        odd = Odd.objects.get(id=1)
        self.assertEqual(Decimal('2.75'), odd.draw_odds)

    def test_ThatTheAwayOddsIs_300(self):
        odd = Odd.objects.get(id=1)
        self.assertEqual(Decimal('3.00'), odd.away_odds)

    def test_ThatTheHomeOddsIs_130(self):
        odd = Odd.objects.get(id=3)
        self.assertEqual(Decimal('1.30'), odd.home_odds)

    def test_ThatTheDrawOddsIs_200(self):
        odd = Odd.objects.get(id=3)
        self.assertEqual(Decimal('2.00'), odd.draw_odds)

    def test_ThatTheAwayOddsIs_220(self):
        odd = Odd.objects.get(id=3)
        self.assertEqual(Decimal('2.20'), odd.away_odds)
