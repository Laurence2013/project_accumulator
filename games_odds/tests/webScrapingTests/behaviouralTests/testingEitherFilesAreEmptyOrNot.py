import os
from django.conf import settings
from django.test import TestCase

'''
This is the 1st behavioural test
This one must be executed FIRST to make sure that the files are empty
The logic here needed to check if file is either empty or not for tbody_ids
'''

class TestingEitherFilesAreEmptyOrNot(TestCase):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.tbody_ids_link_0 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_ids_link_0.csv'
        self.tbody_ids_link_1 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_ids_link_1.csv'
        self.span_ids_link_0 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/span_ids_link_0.csv'
        self.span_ids_link_1 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/span_ids_link_1.csv'
        self.teams_for_tbody0_and_span0 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/team_names_from_links0_and_span0.csv'
        self.teams_for_tbody1_and_span1 = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/team_names_from_links1_and_span1.csv'
        self.tbody_link_0_odds = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_link_0_odds.csv'
        self.tbody_link_1_odds = base_dir + '/games_odds/tests/webScrapingTests/testingFiles/tbody_link_1_odds.csv'

    def test_01_CheckThatTbodyIdsLink_0_FileIsEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.tbody_ids_link_0), 0)
        except AssertionError as e:
            with open(self.tbody_ids_link_0, "w"):
                pass
            self.assertEqual(os.path.getsize(self.tbody_ids_link_0), 0)

    def test_02_CheckThatTbodyIdsLink_1_FileIsEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.tbody_ids_link_1), 0)
        except AssertionError as e:
            with open(self.tbody_ids_link_1, "w"):
                pass
            self.assertEqual(os.path.getsize(self.tbody_ids_link_1), 0)

    def test_03_CheckThatSpanIdsLink_0_FileIsEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.span_ids_link_0), 0)
        except AssertionError as e:
            with open(self.span_ids_link_0, "w"):
                pass
            self.assertEqual(os.path.getsize(self.span_ids_link_0), 0)

    def test_04_CheckThatSpanIdsLink_1_FileIsEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.span_ids_link_1), 0)
        except AssertionError as e:
            with open(self.span_ids_link_1, "w"):
                pass
            self.assertEqual(os.path.getsize(self.span_ids_link_1), 0)

    def test_05_CheckTbody_link_0_OddsIsEitherEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.tbody_link_0_odds), 0)
        except AssertionError as e:
            with open(self.tbody_link_0_odds, "w"):
                pass
            self.assertEqual(os.path.getsize(self.tbody_link_0_odds), 0)

    def test_06_CheckTbody_link_1_OddsIsEitherEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.tbody_link_1_odds), 0)
        except AssertionError as e:
            with open(self.tbody_link_1_odds, "w"):
                pass
            self.assertEqual(os.path.getsize(self.tbody_link_1_odds), 0)

        # def test_CheckThatTbody_0_AndSpanIds_0_FileIsEmptyOrNot(self):
        #     try:
        #         self.assertEqual(os.path.getsize(self.teams_for_tbody0_and_span0), 0)
        #     except AssertionError as e:
        #         with open(self.teams_for_tbody0_and_span0, "w"):
        #             pass
        #         self.assertEqual(os.path.getsize(self.teams_for_tbody0_and_span0), 0)
        #
        # def test_CheckThatTbody_1_AndSpanIds_1_FileIsEmptyOrNot(self):
        #     try:
        #         self.assertEqual(os.path.getsize(self.teams_for_tbody1_and_span1), 0)
        #     except AssertionError as e:
        #         with open(self.teams_for_tbody1_and_span1, "w"):
        #             pass
        #         self.assertEqual(os.path.getsize(self.teams_for_tbody1_and_span1), 0)
