from mock import Mock, patch
from django.test import TestCase
from games_odds.sorting_matches_coral import SortingMatchesInCoral

'''
These are the set of behaviours that I expect to happen:-
'''

class CoralSortingMatches(TestCase):
    def setUp(self):
        self.coral = SortingMatchesInCoral()
        self.todays_matches_list = ['', '', '', '', 'Today 7:45pm\nLIVE\nChelsea v Bournemouth\n1.28\n5.50\n10.00\n+169', 'Today 8:00pm\nLIVE\nBristol City v Man Utd\n6.00\n4.20\n1.53\n+173']

    def test_01_sortingEachGamesNeededData(self):
        '''
        01 - To test that the specified match or matches, is correctly setup via comparing that the tested and the testee have the right number of inner lists within a list
        '''
        expected_todays_match_list = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', '10.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53']]
        get_matches = self.coral.sorting_each_games_data(self.todays_matches_list)
        self.assertEqual(expected_todays_match_list, get_matches)

    def test_02_seperating_odds_from_games(self):
        '''
        02 - To seperate the odds from the games by placing the odds into another list
        '''
        expected_todays_match_list = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', '10.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53']]
        get_matches = self.coral.sorting_each_games_data(self.todays_matches_list)
        get_odds = self.coral.seperating_odds(get_matches)
        self.assertEqual([['1.28', '5.50', '10.00'], ['6.00', '4.20', '1.53']], get_odds)

    def test_03_seperating_games_from_odds(self):
        '''
        03 - To seperate the games from the odds by placing the games into another lists
        '''
        expected_todays_match_list = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', '10.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53']]
        get_matches = self.coral.sorting_each_games_data(self.todays_matches_list)
        get_games = self.coral.seperating_games(get_matches)
        self.assertEqual([['Chelsea', 'v', 'Bournemouth'], ['Bristol', 'City', 'v', 'Man', 'Utd']], get_games)

    def test_04_testing_inner_lists(self):
        '''
        04 - Testing different number of inner lists from a list, we are going to test a list with 3 inner lists and get 3 matches without their odds
        '''
        expected_todays_match_list = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', '10.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53'], ['Cardiff', 'City', 'v', 'Sheffield', 'Wednesday', '1.28', '5.50', '10.00']]
        get_matches = self.coral.sorting_each_games_data(self.todays_matches_list)
        get_games = self.coral.seperating_games(get_matches)
        print(get_games)
        self.assertEqual([['Chelsea', 'v', 'Bournemouth'], ['Bristol', 'City', 'v', 'Man', 'Utd'], ['Cardiff', 'City', 'v', 'Sheffield', 'Wednesday']], get_games)

    # def test_04_testing_foreign_keys_for_games(self):
    #     '''
    #     04 - To test that the Games ID is called as a foriegn key by calling a specific set of odds
    #     '''
    #     pass
    #
    # def test_05_testing_foreign_keys_for_odds(self):
    #     '''
    #     05 - To test that the odds is called correctly from the specified game, from the games table. This is done by its odds foreign key id that was setup
    #     '''
    #     pass
