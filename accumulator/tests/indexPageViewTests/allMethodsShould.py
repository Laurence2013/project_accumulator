from django.test import TestCase
from accumulator.views import IndexPageGamesView

class AllMethodsShould(TestCase):
    def test_AllBeFromDecimalToFloatingOrInteger(self):
        compareList = [1, 0.91, 2.75, 3.0, 2, 1.3, 2.0, 2.2, 3, 1.05, 2.1, 2.75]
        self.assertListEqual(compareList, get_odds())
