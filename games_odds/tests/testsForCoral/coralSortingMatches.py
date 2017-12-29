from mock import Mock, patch
from django.test import TestCase
from games_odds.sorting_matches_coral import SortingMatchesInCoral

class CoralSortingMatches(TestCase):
    def setUp(self):
        self.coral = SortingMatchesInCoral()
        self.todays_matches_list = ['', '', '', '', 'Today 7:45pm\nLIVE\nChelsea v Bournemouth\n1.28\n5.50\n10.00\n+169', 'Today 8:00pm\nLIVE\nBristol City v Man Utd\n6.00\n4.20\n1.53\n+173']

    def test_01_SortingEachGamesNeededData(self):
        expected_todays_match_list = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', '10.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53']]
        get_matches = self.coral.sorting_each_games_data(self.todays_matches_list)
        self.assertEqual(expected_todays_match_list, get_matches)
