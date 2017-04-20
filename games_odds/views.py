from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from accumulator.models import Game, Odd
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from games_odds.mainViewsApi.main_views_api import MainViewsApi

'''
This is what happens at the back, this manages all the games and odds
'''

class ManageMatchesAndOdds(View, MainViewsApi, ScrapingWilliamHill, DecimalToFractionAndStoreInDb, CombineOddsWithItsMatch):
    base_dir = settings.BASE_DIR
    tbody_ids_link_0 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_0.csv'
    tbody_ids_link_1 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_1.csv'
    tbody_ids_link_2 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_2.csv'
    tbody_ids_link_3 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_3.csv'
    tbody_ids_link_4 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_4.csv'
    tbody_ids_link_5 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_5.csv'
    tbody_ids_link_6 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_6.csv'

    span_ids_link_0 = base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_0.csv'

    get_match_odds_link_0 = base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_0.csv'

    def get(self, request, *args, **kwargs):
        links_0 = self.get_tbody(self.tbody_ids_link_0, 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html')
        if len(links_0) > 0:
            self.save_file(self.tbody_ids_link_0, links_0)
            not_empty1 = self.check_file_not_empty(self.tbody_ids_link_0)
            print(not_empty1)

        if not_empty1 is True:
            self.get_span_ids('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html', self.tbody_ids_link_0)
            self.save_file(self.span_ids_link_0, ScrapingWilliamHill.span_id_lists)
            not_empty2 = self.check_file_not_empty(self.span_ids_link_0)
            self.clear_list()
            print(not_empty2)

        if not_empty2 is True:
            match_odds = self.get_all_odds_for_match('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html', self.tbody_ids_link_0)
            self.save_file(self.get_match_odds_link_0, match_odds)
            not_empty3 = self.check_file_not_empty(self.get_match_odds_link_0)
            print(not_empty3)

        if not_empty3 is True:
            get_match = self.get_match(self.span_ids_link_0)
            get_odds = self.convert_fraction_to_decimal(self.get_match_odds_link_0)
            get_converts = self.create_new_list(get_odds)
            get_combined = self.combine_odds_match(get_match, get_converts)
            print(get_combined)

        return HttpResponse('Hello world for manage_matches!')
