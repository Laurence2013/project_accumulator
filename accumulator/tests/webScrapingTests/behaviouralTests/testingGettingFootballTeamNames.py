import os
from django.conf import settings
from django.test import TestCase
from accumulator.webScraping.scrapingWilliamHill import ScrapingWilliamHill

'''
This is the 4th behavioural test
'''

class TestingGettingFootballTeamNames(TestCase, ScrapingWilliamHill):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.span_ids_link_0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_0.csv'
        self.span_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_1.csv'
        self.team_names_from_links0_and_span0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/team_names_from_links0_and_span0.csv'
        self.team_names_from_links1_and_span1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/team_names_from_links1_and_span1.csv'
        self.get_links_0 = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/1/Football.html'
        self.get_links_1 = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/2/Football.html'

    def test_CheckThatSpanIds_0_FileIsNotEmpty(self):
        self.assertGreater(len(self.span_ids_link_0), 0)

    def test_GetTeamNamesList_ForSpanIds_0_File_AndCheckThatItIsGreaterThan_0(self):
        team_names = self.get_name_of_teams(self.get_links_0, self.span_ids_link_0)
        self.assertGreater(len(team_names), 0)

    def test_FromTeamNameList_SaveListIntoCSVFileFor_Links0_And_Span0(self):
        team_names = self.get_name_of_teams(self.get_links_0, self.span_ids_link_0)
        self.save_file(self.team_names_from_links0_and_span0, team_names)
        self.assertGreater(len(self.team_names_from_links0_and_span0), 0)

    def test_CheckThatSpanIds_1_FileIsNotEmpty(self):
        self.assertGreater(len(self.span_ids_link_0), 0)

    def test_GetTeamNamesList_ForSpanIds_1_File_AndCheckThatItIsGreaterThan_0(self):
        team_names = self.get_name_of_teams(self.get_links_1, self.span_ids_link_1)
        self.assertGreater(len(team_names), 0)

    def test_FromTeamNameList_SaveListIntoCSVFileFor_Links1_And_Span1(self):
        team_names = self.get_name_of_teams(self.get_links_1, self.span_ids_link_1)
        self.save_file(self.team_names_from_links1_and_span1, team_names)
        self.assertGreater(len(self.team_names_from_links1_and_span1), 0)


'''
Test like this team_names = self.get_name_of_teams(str('hello'), self.span_ids_link_0), these are tested in the general folder not in the behaviour folder
'''
