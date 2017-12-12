from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from accumulator.models import WilliamHillDailyMatche
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from games_odds.mainViewsApi.main_views_api import MainViewsApi
from games_odds.william_hill_base import WilliamHillBase
from games_odds.save_games_into_db import SaveGamesIntoDb
from games_odds.save_odds_into_db import SaveOddsIntoDb
from games_odds.coral_base import Coral_Base

class Bookies(TemplateView):
    template_name = 'accumulator/bookies.html'

    def get_context_data(self, **kwargs):
        context = super(Bookies, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        storage = messages.get_messages(request)
        context = {'message': storage}
        return render(request, self.template_name, self.get_context_data(**context))

class Main_William_Hill(TemplateView, WilliamHillBase, ScrapingWilliamHill):
    template_name = 'accumulator/william_hill/main_william_hill.html'

    def get_context_data(self, **kwargs):
        context = super(Main_William_Hill, self).get_context_data(**kwargs)
        return context

    def get(self, request, update_no, *args, **kwargs):
        get_match_dates = []
        get_match_dates.append('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/Football.html')
        if int(update_no) is 1:
            if WilliamHillDailyMatche.objects.count() >= 1 or WilliamHillDailyMatche.objects.count() == 0:
                WilliamHillDailyMatche.objects.all().delete()
                self.get_william_hill_daily_matches_dates(get_match_dates)
                get_match_games = WilliamHillDailyMatche.objects.all()
                context = { 'get_matches': get_match_games, }
                return render(request, self.template_name, self.get_context_data(**context))
        else:
            if WilliamHillDailyMatche.objects.count() == 0:
                self.get_william_hill_daily_matches_dates(get_match_dates)
            get_match_games = WilliamHillDailyMatche.objects.all()
            context = { 'get_matches': get_match_games, }
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

class SortGamesOddsIntoDb(View, SaveOddsIntoDb, SaveGamesIntoDb):
    def get(self, request, link_no, *args, **kwargs):
        isGameStored, isOddsStored = self.get_csv_file_type(link_no)
        if isGameStored is True and isOddsStored is True:
            messages.success(request, 'You have successfully added to database')
        else:
            messages.error(request, 'Something went wrong, nothing was added to the database!')
        return redirect('bookies')

    def get_csv_file_type(self, link_no):
        get_link_no = link_no[-1:]
        get_link = str('link_') + get_link_no
        games_from_csv_file = self.get_games_from_csv_file(get_link)
        odds_from_csv_file = self.get_odds_from_csv_file(get_link)
        isGamesStored = self.store_games_into_db(get_link, games_from_csv_file)
        isOddsStored = self.store_odds_into_db(get_link, odds_from_csv_file)
        return isGamesStored, isOddsStored

class Coral(View):
    def get(self, request, *args, **kwargs):
        test_list = list()
        test_list2 = list()
        coral = Coral_Base()
        coral.get_todays_matches()
        matches = coral.get_todays_matches_list()

        for match in range(0, len(matches)):
            test_list.append(matches[match].split())

        list2 = filter(None, test_list)
        for l2 in list2:
            test_list2.append(l2)

        for test2 in range(0, len(test_list2)):
            test_list2[test2].pop(0)
            test_list2[test2].pop(0)
            test_list2[test2].pop(0)

        print(test_list2)

        return HttpResponse('Hello world')
