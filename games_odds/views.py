import json
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from accumulator.models import *
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from games_odds.mainViewsApi.main_views_api import MainViewsApi
from games_odds.william_hill_base import WilliamHillBase
from games_odds.save_games_into_db import SaveGamesIntoDb
from games_odds.save_odds_into_db import SaveOddsIntoDb
from games_odds.coral_base import Coral_Base
from games_odds.sorting_matches_coral import SortingMatchesInCoral

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

class GetAllCoralGameDates(View):
    template_name = 'accumulator/coral/main_coral.html'
    base_dir = settings.BASE_DIR

    def get_context_data(self, **kwargs):
        context = super(GetAllCoralGameDates, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        get_all_combinations = self.base_dir + '/games_odds/static/json/coral_game_dates.json'
        with open(get_all_combinations) as json_file:
            json_data = json.load(json_file)
        return JsonResponse(json_data)

class Get_Coral_Matches_0(View):
    base_dir = settings.BASE_DIR

    def get_context_data(self, **kwargs):
        context = super(Get_Coral_Matches_0, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        get_all_combinations = self.base_dir + '/games_odds/static/json/coral_get_matches_0.json'
        with open(get_all_combinations) as json_file:
            json_data = json.load(json_file)
        return JsonResponse(json_data)

class Get_Coral_Matches_1(View):
    base_dir = settings.BASE_DIR

    def get_context_data(self, **kwargs):
        context = super(Get_Coral_Matches_1, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        get_all_combinations = self.base_dir + '/games_odds/static/json/coral_get_matches_1.json'
        with open(get_all_combinations) as json_file:
            json_data = json.load(json_file)
        return JsonResponse(json_data)

class Get_Coral_Matches_2(View):
    base_dir = settings.BASE_DIR

    def get_context_data(self, **kwargs):
        context = super(Get_Coral_Matches_2, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        get_all_combinations = self.base_dir + '/games_odds/static/json/coral_get_matches_2.json'
        with open(get_all_combinations) as json_file:
            json_data = json.load(json_file)
        return JsonResponse(json_data)

class Get_Coral_Matches_3(View):
    base_dir = settings.BASE_DIR

    def get_context_data(self, **kwargs):
        context = super(Get_Coral_Matches_3, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        get_all_combinations = self.base_dir + '/games_odds/static/json/coral_get_matches_3.json'
        with open(get_all_combinations) as json_file:
            json_data = json.load(json_file)
        return JsonResponse(json_data)

class GetAllCoralMatchDayGames(TemplateView, SortingMatchesInCoral, Coral_Base):
    coral_db_match_list = [CoralGames0, CoralGames1, CoralGames2, CoralGames3]
    coral_db_odds_list = [CoralOdds0, CoralOdds1, CoralOdds2, CoralOdds3]
    template_name_0 = 'accumulator/coral/coral_0.html'
    template_name_1 = 'accumulator/coral/coral_1.html'
    template_name_2 = 'accumulator/coral/coral_2.html'
    template_name_3 = 'accumulator/coral/coral_3.html'
    coralUrl = 'http://sports.coral.co.uk/football'
    base_dir = settings.BASE_DIR

    def get_context_data(self, **kwargs):
        context = super(GetAllCoralMatchDayGames, self).get_context_data(**kwargs)
        return context

    def get(self, request, matchday_games_id, *args, **kwargs):
        if int(matchday_games_id) is 1:
            coral_json = "/games_odds/static/json/coral_get_matches_0.json"
            adjust_matches_2 = self.get_coral_match_day_games(self.coral_db_match_list[0], self.coral_db_odds_list[0], matchday_games_id, coral_json)
            if adjust_matches_2 is not None:
                context = {
                    'match_day': True,
                    'adjust_matches': adjust_matches_2,
                }
                return render(request, self.template_name_0, self.get_context_data(**context))
            else:
                get_coral_daily_matches = self.save_coral_matches_and_odds(self.coral_db_match_list[0], self.coral_db_odds_list[0], matchday_games_id, self.coralUrl)
                if self.coral_db_match_list[0].objects.count() >= 1 and self.coral_db_odds_list[0].objects.count() >= 1:
                    messages.success(request, 'Saving into '+ get_coral_daily_matches + ' was successfully saved into Database')
                    return redirect('bookies')

        if int(matchday_games_id) is 2:
            coral_json = "/games_odds/static/json/coral_get_matches_1.json"
            adjust_matches_2 = self.get_coral_match_day_games(self.coral_db_match_list[1], self.coral_db_odds_list[1], matchday_games_id, coral_json)
            if adjust_matches_2 is not None:
                context = {
                    'match_day': True,
                    'adjust_matches': adjust_matches_2,
                }
                return render(request, self.template_name_1, self.get_context_data(**context))
            else:
                get_coral_daily_matches = self.save_coral_matches_and_odds(self.coral_db_match_list[1], self.coral_db_odds_list[1], matchday_games_id, self.coralUrl)
                if self.coral_db_match_list[1].objects.count() >= 1 and self.coral_db_odds_list[1].objects.count() >= 1:
                    messages.success(request, 'Saving into '+ get_coral_daily_matches + ' was successfully saved into Database')
                    return redirect('bookies')

        if int(matchday_games_id) is 3:
            coral_json = "/games_odds/static/json/coral_get_matches_2.json"
            adjust_matches_2 = self.get_coral_match_day_games(self.coral_db_match_list[2], self.coral_db_odds_list[2], matchday_games_id, coral_json)
            if adjust_matches_2 is not None:
                context = {
                    'match_day': True,
                    'adjust_matches': adjust_matches_2,
                }
                return render(request, self.template_name_2, self.get_context_data(**context))
            else:
                get_coral_daily_matches = self.save_coral_matches_and_odds(self.coral_db_match_list[2], self.coral_db_odds_list[2], matchday_games_id, self.coralUrl)
                if self.coral_db_match_list[2].objects.count() >= 1 and self.coral_db_odds_list[2].objects.count() >= 1:
                    messages.success(request, 'Saving into '+ get_coral_daily_matches + ' was successfully saved into Database')
                    return redirect('bookies')

        if int(matchday_games_id) is 4:
            coral_json = "/games_odds/static/json/coral_get_matches_3.json"
            adjust_matches_2 = self.get_coral_match_day_games(self.coral_db_match_list[3], self.coral_db_odds_list[3], matchday_games_id, coral_json)
            if adjust_matches_2 is not None:
                context = {
                    'match_day': True,
                    'adjust_matches': adjust_matches_2,
                }
                return render(request, self.template_name_3, self.get_context_data(**context))
            else:
                get_coral_daily_matches = self.save_coral_matches_and_odds(self.coral_db_match_list[3], self.coral_db_odds_list[3], matchday_games_id, self.coralUrl)
                if self.coral_db_match_list[3].objects.count() >= 1 and self.coral_db_odds_list[3].objects.count() >= 1:
                    messages.success(request, 'Saving into '+ get_coral_daily_matches + ' was successfully saved into Database')
                    return redirect('bookies')

        messages.error(request, 'The Match day ID do not match, please try again for Coral')
        return redirect('bookies')

class Coral_Games(TemplateView, SortingMatchesInCoral, Coral_Base):
    coralUrl = 'http://sports.coral.co.uk/football'
    template_name = 'accumulator/coral/main_coral.html'
    base_dir = settings.BASE_DIR

    def get_context_data(self, **kwargs):
        context = super(Coral_Games, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        matchday_dates = dict()
        update_no = int(kwargs.get('update_no'))
        if update_no is 1:
            self.initiateWebdriver()
            get_match_dates = self.get_daily_match_dates(self.coralUrl)
            self.sleep_then_kill_browser()
            coral_game_dates = Bookie.objects.filter(bookies_name = 'Corel').values_list('id', flat=True)
            CoralDailyMatche.objects.all().delete()
            date_string = coral_game_dates.values_list()[0][0]
            for eachDate in range(0, len(get_match_dates)):
                save_game_dates = CoralDailyMatche(dates_of_games=get_match_dates[eachDate], dates_id = eachDate + 1, bookies_id=date_string)
                save_game_dates.save()

            check_games_are_not_null = CoralDailyMatche.objects.values('dates_of_games')
            for game in check_games_are_not_null.values_list():
                if game[2] is '':
                    messages.error(request, 'Something went wrong, nothing was added to the database! Try saving it updating it again')
                    return redirect('bookies')
            messages.success(request, 'You have successfully added to database')
            return redirect('bookies')

        if update_no is 0:
            get_dates = CoralDailyMatche.objects.values_list('dates_of_games','dates_id')

            for row in range(0, len(get_dates)):
                matchday_dates[row] = get_dates[row]

            s = json.dumps(matchday_dates, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
            with open(self.base_dir + "/games_odds/static/json/coral_game_dates.json", "w") as f:
                f.write(s)

            context = {'get_game_dates': True}
            return render(request, self.template_name, self.get_context_data(**context))
