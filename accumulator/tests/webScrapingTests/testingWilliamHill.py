import os
import pathlib
from django.conf import settings
from django.test import TestCase
from accumulator.webScraping.scrapingWilliamHill import ScrapingWilliamHill

class TestingWilliamHill(TestCase):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.tbody_ids_link_0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_ids_link_0.csv'
        self.tbody_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_ids_link_1.csv'
        self.span_ids_link_0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_0.csv'
        self.span_ids_link_1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids_link_1.csv'
        self.teams_for_tbody0_and_span0 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/team_names_from_links0_and_span0.csv'
        self.teams_for_tbody1_and_span1 = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/team_names_from_links1_and_span1.csv'

    def test_CheckThatTbodyIds_0_Exist(self):
        path_to_file = pathlib.Path(self.tbody_ids_link_0)
        self.assertTrue(path_to_file.is_file())

    def test_CheckThatTbodyIds_1_Exist(self):
        path_to_file = pathlib.Path(self.tbody_ids_link_1)
        self.assertTrue(path_to_file.is_file())

    def test_CheckThatSpanIds_0_Exist(self):
        path_to_file = pathlib.Path(self.span_ids_link_0)
        self.assertTrue(path_to_file.is_file())

    def test_CheckThatSpanIds_1_Exist(self):
        path_to_file = pathlib.Path(self.span_ids_link_1)
        self.assertTrue(path_to_file.is_file())

    def test_CheckThatTbodyIdsLink_0_SpanIdsLink_0_Exist(self):
        path_to_file = pathlib.Path(self.teams_for_tbody0_and_span0)
        self.assertTrue(path_to_file.is_file())

    def test_CheckThatTbodyIdsLink_1_SpanIdsLink_1_Exist(self):
        path_to_file = pathlib.Path(self.teams_for_tbody1_and_span1)
        self.assertTrue(path_to_file.is_file())
