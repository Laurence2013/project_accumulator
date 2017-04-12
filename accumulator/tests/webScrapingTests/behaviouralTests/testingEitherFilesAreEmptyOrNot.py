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
        self.tbody_ids_link_0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_ids_link_0.csv'
        self.tbody_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_ids_link_1.csv'
        self.span_ids_link_0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_0.csv'
        self.span_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_1.csv'

    def test_CheckThatTbodyIdsLink_0_FileIsEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.tbody_ids_link_0), 0)
        except AssertionError as e:
            with open(self.tbody_ids_link_0, "w"):
                pass
            self.assertEqual(os.path.getsize(self.tbody_ids_link_0), 0)

    def test_CheckThatTbodyIdsLink_1_FileIsEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.tbody_ids_link_1), 0)
        except AssertionError as e:
            with open(self.tbody_ids_link_1, "w"):
                pass
            self.assertEqual(os.path.getsize(self.tbody_ids_link_1), 0)

    def test_CheckThatSpanIdsLink_0_FileIsEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.span_ids_link_0), 0)
        except AssertionError as e:
            with open(self.span_ids_link_0, "w"):
                pass
            self.assertEqual(os.path.getsize(self.span_ids_link_0), 0)

    def test_CheckThatSpanIdsLink_1_FileIsEmptyOrNot(self):
        try:
            self.assertEqual(os.path.getsize(self.span_ids_link_1), 0)
        except AssertionError as e:
            with open(self.span_ids_link_1, "w"):
                pass
            self.assertEqual(os.path.getsize(self.span_ids_link_1), 0)
