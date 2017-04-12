import os
import pathlib
from django.conf import settings
from django.test import TestCase
from accumulator.webScraping.scrapingWilliamHill import ScrapingWilliamHill

class TestingWilliamHill(TestCase):
    def setUp(self):
        base_dir = settings.BASE_DIR
        self.tbody_ids = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/tbody_ids.csv'
        self.span_ids = base_dir + '/accumulator/tests/webScrapingTests/testingFiles/span_ids.csv'

    def test_CheckThatTbodyIdsExist(self):
        path_to_file = pathlib.Path(self.tbody_ids)
        self.assertTrue(path_to_file.is_file())

    def test_CheckThatSpanIdsExist(self):
        path_to_file = pathlib.Path(self.span_ids)
        self.assertTrue(path_to_file.is_file())
