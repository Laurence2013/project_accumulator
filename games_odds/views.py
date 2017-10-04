from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.conf import settings
from django.contrib import messages
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from games_odds.mainViewsApi.main_views_api import MainViewsApi
from games_odds.william_hill_base import WilliamHillBase
from games_odds.save_games_n_odds_into_db import SaveGamesNOddsIntoDb

class Bookies(TemplateView):
    template_name = 'accumulator/bookies.html'

    def get_context_data(self, **kwargs):
        context = super(Bookies, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        storage = messages.get_messages(request)
        context = {'message': storage}
        return render(request, self.template_name, self.get_context_data(**context))

class Main_William_Hill(TemplateView, ScrapingWilliamHill):
    template_name = 'accumulator/william_hill/main_william_hill.html'

    def get_context_data(self, **kwargs):
        context = super(Main_William_Hill, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        get_match_dates = str('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/Football.html')

        get_matches = self.get_daily_matches_dates(get_match_dates)
        context = { 'get_matches': get_matches, }
        return render(request, self.template_name, self.get_context_data(**context))

class William_Hill_Games_0(WilliamHillBase, TemplateView, MainViewsApi, ScrapingWilliamHill, DecimalToFractionAndStoreInDb, CombineOddsWithItsMatch):
    template_name = 'accumulator/william_hill/william_hill_0.html'
    base_dir = settings.BASE_DIR

    tbody_ids_link_0 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_0.csv'
    span_ids_link_0 = base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_0.csv'
    get_match_odds_link_0 = base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_0.csv'
    william_hill_link = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html'

    def get_context_data(self, **kwargs):
        context = super(William_Hill_Games_0, self).get_context_data(**kwargs)
        return context

    def get(self, request, refresh_no, *args, **kwargs):
        if int(refresh_no) is int(1):
            context = self.get_web_details_0(request.path_info, self.william_hill_link, self.tbody_ids_link_0, self.span_ids_link_0, self.get_match_odds_link_0)
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            context = self.get_web_details_1(self.william_hill_link, self.tbody_ids_link_0, self.span_ids_link_0, self.get_match_odds_link_0, str('TimeOfRefreshWilliamHill0'))
            return render(request, self.template_name, self.get_context_data(**context))

class William_Hill_Games_1(WilliamHillBase, TemplateView, MainViewsApi, ScrapingWilliamHill, DecimalToFractionAndStoreInDb, CombineOddsWithItsMatch):
    template_name = 'accumulator/william_hill/william_hill_1.html'
    base_dir = settings.BASE_DIR

    tbody_ids_link_1 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_1.csv'
    span_ids_link_1 = base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_1.csv'
    get_match_odds_link_1 = base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_1.csv'
    william_hill_link = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/1/Football.html'

    def get_context_data(self, **kwargs):
        context = super(William_Hill_Games_1, self).get_context_data(**kwargs)
        return context

    def get(self, request, refresh_no, *args, **kwargs):
        if int(refresh_no) is int(1):
            context = self.get_web_details_0(request.path_info, self.william_hill_link, self.tbody_ids_link_1, self.span_ids_link_1, self.get_match_odds_link_1)
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            context = self.get_web_details_1(self.william_hill_link, self.tbody_ids_link_1, self.span_ids_link_1, self.get_match_odds_link_1, str('TimeOfRefreshWilliamHill1'))
            return render(request, self.template_name, self.get_context_data(**context))

class William_Hill_Games_2(WilliamHillBase, TemplateView, MainViewsApi, ScrapingWilliamHill, DecimalToFractionAndStoreInDb, CombineOddsWithItsMatch):
    template_name = 'accumulator/william_hill/william_hill_2.html'
    base_dir = settings.BASE_DIR

    tbody_ids_link_2 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_2.csv'
    span_ids_link_2 = base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_2.csv'
    get_match_odds_link_2 = base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_2.csv'
    william_hill_link = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/2/Football.html'

    def get_context_data(self, **kwargs):
        context = super(William_Hill_Games_2, self).get_context_data(**kwargs)
        return context

    def get(self, request, refresh_no, *args, **kwargs):
        if int(refresh_no) is int(1):
            context = self.get_web_details_0(request.path_info, self.william_hill_link, self.tbody_ids_link_2, self.span_ids_link_2, self.get_match_odds_link_2)
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            context = self.get_web_details_1(self.william_hill_link, self.tbody_ids_link_2, self.span_ids_link_2, self.get_match_odds_link_2, str('TimeOfRefreshWilliamHill2'))
            return render(request, self.template_name, self.get_context_data(**context))

class William_Hill_Games_3(WilliamHillBase, TemplateView, MainViewsApi, ScrapingWilliamHill, DecimalToFractionAndStoreInDb, CombineOddsWithItsMatch):
    template_name = 'accumulator/william_hill/william_hill_3.html'
    base_dir = settings.BASE_DIR

    tbody_ids_link_3 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_3.csv'
    span_ids_link_3 = base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_3.csv'
    get_match_odds_link_3 = base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_3.csv'
    william_hill_link = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/3/Football.html'

    def get_context_data(self, **kwargs):
        context = super(William_Hill_Games_3, self).get_context_data(**kwargs)
        return context

    def get(self, request, refresh_no, *args, **kwargs):
        if int(refresh_no) is int(1):
            context = self.get_web_details_0(request.path_info, self.william_hill_link, self.tbody_ids_link_3, self.span_ids_link_3, self.get_match_odds_link_3)
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            context = self.get_web_details_1(self.william_hill_link, self.tbody_ids_link_3, self.span_ids_link_3, self.get_match_odds_link_3, str('TimeOfRefreshWilliamHill3'))
            return render(request, self.template_name, self.get_context_data(**context))

class William_Hill_Games_4(WilliamHillBase, TemplateView, MainViewsApi, ScrapingWilliamHill, DecimalToFractionAndStoreInDb, CombineOddsWithItsMatch):
    template_name = 'accumulator/william_hill/william_hill_4.html'
    base_dir = settings.BASE_DIR

    tbody_ids_link_4 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_4.csv'
    span_ids_link_4 = base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_4.csv'
    get_match_odds_link_4 = base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_4.csv'
    william_hill_link = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/4/Football.html'

    def get_context_data(self, **kwargs):
        context = super(William_Hill_Games_4, self).get_context_data(**kwargs)
        return context

    def get(self, request, refresh_no, *args, **kwargs):
        if int(refresh_no) is int(1):
            context = self.get_web_details_0(request.path_info, self.william_hill_link, self.tbody_ids_link_4, self.span_ids_link_4, self.get_match_odds_link_4)
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            context = self.get_web_details_1(self.william_hill_link, self.tbody_ids_link_4, self.span_ids_link_4, self.get_match_odds_link_4, str('TimeOfRefreshWilliamHill4'))
            return render(request, self.template_name, self.get_context_data(**context))

class William_Hill_Games_5(WilliamHillBase, TemplateView, MainViewsApi, ScrapingWilliamHill, DecimalToFractionAndStoreInDb, CombineOddsWithItsMatch):
    template_name = 'accumulator/william_hill/william_hill_5.html'
    base_dir = settings.BASE_DIR

    tbody_ids_link_5 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_5.csv'
    span_ids_link_5 = base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_5.csv'
    get_match_odds_link_5 = base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_5.csv'
    william_hill_link = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/5/Football.html'

    def get_context_data(self, **kwargs):
        context = super(William_Hill_Games_5, self).get_context_data(**kwargs)
        return context

    def get(self, request, refresh_no, *args, **kwargs):
        if int(refresh_no) is int(1):
            context = self.get_web_details_0(request.path_info, self.william_hill_link, self.tbody_ids_link_5, self.span_ids_link_5, self.get_match_odds_link_5)
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            context = self.get_web_details_1(self.william_hill_link, self.tbody_ids_link_5, self.span_ids_link_5, self.get_match_odds_link_5, str('TimeOfRefreshWilliamHill5'))
            return render(request, self.template_name, self.get_context_data(**context))

class William_Hill_Games_6(WilliamHillBase, TemplateView, MainViewsApi, ScrapingWilliamHill, DecimalToFractionAndStoreInDb, CombineOddsWithItsMatch):
    template_name = 'accumulator/william_hill/william_hill_6.html'
    base_dir = settings.BASE_DIR

    tbody_ids_link_6 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_6.csv'
    span_ids_link_6 = base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_6.csv'
    get_match_odds_link_6 = base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_6.csv'
    william_hill_link = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/6/Football.html'

    def get_context_data(self, **kwargs):
        context = super(William_Hill_Games_6, self).get_context_data(**kwargs)
        return context

    def get(self, request, refresh_no, *args, **kwargs):
        if int(refresh_no) is int(1):
            context = self.get_web_details_0(request.path_info, self.william_hill_link, self.tbody_ids_link_6, self.span_ids_link_6, self.get_match_odds_link_6)
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            context = self.get_web_details_1(self.william_hill_link, self.tbody_ids_link_6, self.span_ids_link_6, self.get_match_odds_link_6, str('TimeOfRefreshWilliamHill6'))
            return render(request, self.template_name, self.get_context_data(**context))

class SortGamesOddsIntoDb(View, SaveGamesNOddsIntoDb):
    def get(self, request, link_no, *args, **kwargs):
        if link_no == str('link_0'):
            games_from_csv_file = self.get_games_from_csv_file(link_no, str('ids_for_tag_span_link_0'))
            isStored = self.store_games_or_odds_into_db(link_no, games_from_csv_file)
            if isStored is True:
                messages.success(request, 'You have successfully added to database')
            else:
                messages.error(request, 'Something went wrong, nothing was added to the database!')
            return redirect('bookies')
