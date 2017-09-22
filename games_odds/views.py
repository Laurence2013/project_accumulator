from django.core.urlresolvers import resolve
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from games_odds.mainViewsApi.main_views_api import MainViewsApi
from games_odds.models import TimeOfRefreshWilliamHill0, TimeOfRefreshWilliamHill1
from games_odds.william_hill_base import WilliamHillBase

class Bookies(TemplateView):
    template_name = 'accumulator/bookies.html'

    def get_context_data(self, **kwargs):
        context = super(Bookies, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

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
            current_url = resolve(request.path_info).url_name
            get_refresh_date = self.get_date(current_url)
            is_refresh = self.empty_csv_files(self.tbody_ids_link_0, self.span_ids_link_0, self.get_match_odds_link_0)
            if is_refresh is True:
                context = self.get_context(self.william_hill_link, self.tbody_ids_link_0, self.span_ids_link_0, self.get_match_odds_link_0, get_refresh_date)
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            get_file_count = self.get_empty_files(self.tbody_ids_link_0, self.span_ids_link_0, self.get_match_odds_link_0)
            if get_file_count[0] == 3:
                get_refresh_date = TimeOfRefreshWilliamHill0.objects.last()
                context = {
                    'games': self.combine_matches_odds_2(self.span_ids_link_0, self.get_match_odds_link_0),
                    'get_refresh_date': get_refresh_date,
                }
                return render(request, self.template_name, self.get_context_data(**context))
            if get_file_count[1] == 3:
                get_refresh_date = TimeOfRefreshWilliamHill0.objects.last()
                context = self.get_context(self.william_hill_link, self.tbody_ids_link_0, self.span_ids_link_0, self.get_match_odds_link_0, get_refresh_date)
                return render(request, self.template_name, self.get_context_data(**context))
            if get_file_count[1] < 3 or get_file_count[0] < 3:
                is_empty = self.empty_csv_files(self.tbody_ids_link_0, self.span_ids_link_0, self.get_match_odds_link_0)
                get_refresh_date = TimeOfRefreshWilliamHill0.objects.last()
                if is_empty is True:
                    context = self.get_context(self.william_hill_link, self.tbody_ids_link_0, self.span_ids_link_0, self.get_match_odds_link_0, get_refresh_date)
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
            current_url = resolve(request.path_info).url_name
            get_refresh_date = self.get_date(current_url)
            is_refresh = self.empty_csv_files(self.tbody_ids_link_1, self.span_ids_link_1, self.get_match_odds_link_1)
            if is_refresh is True:
                context = self.get_context(self.william_hill_link, self.tbody_ids_link_1, self.span_ids_link_1, self.get_match_odds_link_1, get_refresh_date)
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            get_file_count = self.get_empty_files(self.tbody_ids_link_1, self.span_ids_link_1, self.get_match_odds_link_1)
            if get_file_count[0] == 3:
                get_refresh_date = TimeOfRefreshWilliamHill1.objects.last()
                context = {
                    'games': self.combine_matches_odds_2(self.span_ids_link_1, self.get_match_odds_link_1),
                    'get_refresh_date': get_refresh_date,
                }
                return render(request, self.template_name, self.get_context_data(**context))
            if get_file_count[1] == 3:
                get_refresh_date = TimeOfRefreshWilliamHill1.objects.last()
                context = self.get_context(self.william_hill_link, self.tbody_ids_link_1, self.span_ids_link_1, self.get_match_odds_link_1, get_refresh_date)
                return render(request, self.template_name, self.get_context_data(**context))
            if get_file_count[1] < 3 or get_file_count[0] < 3:
                is_empty = self.empty_csv_files(self.tbody_ids_link_1, self.span_ids_link_1, self.get_match_odds_link_1)
                get_refresh_date = TimeOfRefreshWilliamHill1.objects.last()
                if is_empty is True:
                    context = self.get_context(self.william_hill_link, self.tbody_ids_link_1, self.span_ids_link_1, self.get_match_odds_link_1, get_refresh_date)
            return render(request, self.template_name, self.get_context_data(**context))

# tbody_ids_link_1 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_1.csv'
# tbody_ids_link_2 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_2.csv'
# tbody_ids_link_3 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_3.csv'
# tbody_ids_link_4 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_4.csv'
# tbody_ids_link_5 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_5.csv'
# tbody_ids_link_6 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_6.csv'
