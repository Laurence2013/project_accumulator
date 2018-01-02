from mock import Mock, patch
from django.test import LiveServerTestCase
from games_odds.coral_base import Coral_Base
from games_odds.sorting_matches_coral import SortingMatchesInCoral
from games_odds.tests.testsForCoral.extendedUnitTests.testCaseExactDataTypeList import TestCaseExactDataTypeList

class CoralIntegrationGettingDailyDates(LiveServerTestCase, TestCaseExactDataTypeList, SortingMatchesInCoral):
    def setUp(self):
        self.coral_base = Coral_Base()
        self.coral = SortingMatchesInCoral()
        self.coralUrl = 'http://sports.coral.co.uk/football'
        self.expected_todays_match_list1 = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', '10.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53']]
        self.expected_todays_match_list2 = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', '10.00'], ['Bristol', 'City', 'v', 'Man', 'Utd', '6.00', '4.20', '1.53'], ['Man', 'City', 'v', 'Man', 'Utd', '1.00', '2.20', '3.53']]
        self.expected_todays_match_list3 = [['Chelsea', 'v', 'Bournemouth', '1.28', '5.50', 10.00], ['Bristol', 'City', 'v', 'Man', 'Utd', 6.00, '4.20', '1.53']]

    def test_01_SameList(self):
        list_to_test = list()
        self.coral_base.initiateWebdriver()
        getGames = self.coral_base.get_future_matches_d(self.coralUrl)
        get_matches = self.coral.sorting_each_games_data(getGames)
        self.coral_base.sleep_then_kill_browser()
        list_to_test.append(get_matches[0])
        list_to_test.append(get_matches[1])
        isTheSame = self.assertDataTypeOfListIsEqual(self.expected_todays_match_list1, list_to_test)
        self.assertTrue(isTheSame)

    def test_02_NotSameList(self):
        list_to_test = list()
        self.coral_base.initiateWebdriver()
        getGames = self.coral_base.get_future_matches_d(self.coralUrl)
        get_matches = self.coral.sorting_each_games_data(getGames)
        self.coral_base.sleep_then_kill_browser()
        list_to_test.append(get_matches[0])
        list_to_test.append(get_matches[1])
        isTheSame = self.assertDataTypeOfListIsEqual(self.expected_todays_match_list2, list_to_test)
        self.assertFalse(isTheSame)

    def test_03_seperating_odds_from_games(self):
        '''
        To seperate the games from the odds by placing them in two seperate tables, using integration testing
        '''
        pass

    # def test_03_NotSameList(self):
    #     list_to_test = list()
    #     self.coral_base.initiateWebdriver()
    #     getGames = self.coral_base.get_future_matches_d(self.coralUrl)
    #     get_matches = self.coral.sorting_each_games_data(getGames)
    #     self.coral_base.sleep_then_kill_browser()
    #     list_to_test.append(get_matches[0])
    #     list_to_test.append(get_matches[1])
    #     isTheSame = self.assertDataTypeOfListIsEqual(self.expected_todays_match_list3, list_to_test)
    #     self.assertFalse(isTheSame)
