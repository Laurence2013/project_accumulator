from django.conf import settings
from games_odds.models import *
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb

class SaveGamesOddsIntoDb(CombineOddsWithItsMatch, DecimalToFractionAndStoreInDb):
    def __init__(self, link_no, csv_list):
        self.link_no = link_no
        self.csv_list = csv_list

    def check_csv_name_with_csv_file(self):
        pass
