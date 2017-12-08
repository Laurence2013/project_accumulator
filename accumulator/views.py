import os
import json
from django.conf import settings
from django.db import connection
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from accumulator.models import *
from games_odds.models import *
from django.views.generic import View, TemplateView
from django.views.generic.base import RedirectView
from decimal import Decimal
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator
from accumulator.combinations.threeGamesAccumulator import ThreeGamesAccumulator
from accumulator.combinations.fourGamesAccumulator import FourGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator
from accumulator.accumulatorPageGames.accumulatorPageGames import AccumulatorPageGames
from accumulator.accumulatorPageGames.settersGettersBookies import SettersGettersBookies

class JsonAsView(View):
    def get_context_data(self, **kwargs):
        context = super(JsonAsView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        base_dir = settings.BASE_DIR
        json_file_0 = base_dir + '/accumulator/static/json/daily_match_dates.json'
        with open(json_file_0) as json_file:
            json_data = json.load(json_file)
            return HttpResponse(json_data, content_type='application/json')

class GamesJsonAsView(View):
    def get_context_data(self, **kwargs):
        context = super(GamesJsonAsView, self).get_context_data(**kwargs)
        return context

    def get(self, request, games_json, *args, **kwargs):
        base_dir = settings.BASE_DIR
        json_file_0 = base_dir + '/accumulator/static/json/test.json'
        with open(json_file_0) as json_file:
            json_data = json.load(json_file)
        return JsonResponse(json_data)

class GetAllCombinations(View):
    template_name = "accumulator/index.html"
    def get_context_data(self, **kwargs):
        context = super(GetAllCombinations, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        base_dir = settings.BASE_DIR
        get_all_combinations = base_dir + '/accumulator/static/json/get_all_combinations.json'
        with open(get_all_combinations) as json_file:
            json_data = json.load(json_file)
        return JsonResponse(json_data)

class GetBookiesDailyGames(View):
    bookie_game_date_id = []

    def get(self, request, *args, **kwargs):
        self.bookie_game_date_id.append(int(kwargs['daily_games_id']))
        return redirect('accumulator')

class AccumulatorPageGamesView(TemplateView, GetBookiesDailyGames, TwoGamesAccumulator, ThreeGamesAccumulator, FourGamesAccumulator, AccumulatorPageGames, GeneralGamesAccumulator):
    base_dir = settings.BASE_DIR
    template_name = "accumulator/index.html"
    games = Game.objects.values_list('id','games')
    match_info = MatchInfo.objects.values_list('daily_matches', 'combinations')
    odds = Odd.objects.values_list('id','home_odds','draw_odds','away_odds')
    get_bookies = Bookie.objects.all()
    whlist = [WilliamHillOdds0, WilliamHillOdds1, WilliamHillOdds2, WilliamHillOdds3, WilliamHillOdds4, WilliamHillOdds5, WilliamHillOdds6]
    whg = [WilliamHillGames0, WilliamHillGames1, WilliamHillGames2, WilliamHillGames3, WilliamHillGames4, WilliamHillGames5, WilliamHillGames6]
    bookies_name = SettersGettersBookies()
    main_page_load = True

    def get_context_data(self, **kwargs):
        context = super(AccumulatorPageGamesView, self).get_context_data(**kwargs)
        get_game_date_id = GetBookiesDailyGames.bookie_game_date_id
        add_games_id_to_json = list()

        if len(get_game_date_id) != 0:
            match_day_id = self.getting_matches_and_odds_from_db(get_game_date_id)
            get_ids = WilliamHillDailyMatche.objects.values('wh_csv_links').get(id=match_day_id)
            get_bookies_ids = self.get_bookies_ids(get_ids)

            if get_bookies_ids is 1:
                william_hill_games = self.whg[0]
                william_hill_odds = self.whlist[0]
            if get_bookies_ids is 2:
                william_hill_games = self.whg[1]
                william_hill_odds = self.whlist[1]
            if get_bookies_ids is 3:
                william_hill_games = self.whg[2]
                william_hill_odds = self.whlist[2]
            if get_bookies_ids is 4:
                william_hill_games = self.whg[3]
                william_hill_odds = self.whlist[3]
            if get_bookies_ids is 5:
                william_hill_games = self.whg[4]
                william_hill_odds = self.whlist[4]
            if get_bookies_ids is 6:
                william_hill_games = self.whg[5]
                william_hill_odds = self.whlist[5]
            if get_bookies_ids is 7:
                william_hill_games = self.whg[6]
                william_hill_odds = self.whlist[6]

            wh = william_hill_games.objects.values('id','games').filter(url_game_link_id=get_bookies_ids)
            get_bookie_games = self.extract_and_get_games(wh)
            get_games_id = william_hill_games.objects.values('id')
            get_odds = self.extract_by_getting_odds(william_hill_odds, get_games_id)
            self.bookies_name.set(william_hill_odds)
            turn_to_json = list(self.break_list_into_equal_chunks(self.get_final_game(self.get_ammended_games(self.get_games(get_bookie_games, get_odds))),4))

            for games in get_games_id:
                for game in games.values():
                    add_games_id_to_json.append(game)

            for turns in range(0, len(turn_to_json)):
                insert_id_into_games_odds = turn_to_json[turns]
                insert_id_into_games_odds.append(add_games_id_to_json[turns])

            self.turnGamesWithOddsIntoJson(turn_to_json)
            context['infos'] = self.match_info
            context['bookies'] = self.get_bookies
            context['each_match'] = True
            return context

        context['infos'] = self.match_info
        context['bookies'] = self.get_bookies
        context['main_page_load'] = self.main_page_load
        GetBookiesDailyGames.bookie_game_date_id = []
        return context

    def get(self, request, *args, **kwargs):
        if kwargs.get('slug'):
            bookie = kwargs.get('slug')
            if bookie == 'daily_match_dates':
                return render(request, self.template_name, self.get_context_data())
            else:
                Bookie.objects.get(bookies_name=bookie)
                bookie_name = Bookie.objects.get(bookies_name=bookie)
                bookie_games = WilliamHillDailyMatche.objects.all().filter(bookies=bookie_name)
                bookie_games = serializers.serialize('json', bookie_games)
                daily_games = json.dumps(bookie_games, ensure_ascii=False, indent=4)
                with open(self.base_dir + '/accumulator/static/json/daily_match_dates.json', 'w') as f:
                    f.write(daily_games)
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        get_all_combinations_dict = dict()
        final_chosen_games = list()
        mad_combos = False
        mad_combos2 = False
        try:
            request.method == "POST"
            get_accumulator = request.POST.getlist("accumulator")
            get_stake = request.POST.get("stake")
            games = self.filter_accumulator(get_accumulator, self.bookies_name.get())
            for games_with_odds_id in get_accumulator:
                get_games = WilliamHillGames0.objects.get(id=games_with_odds_id)
                final_chosen_games.append(get_games.games)

            if len(games) is 2:
                get_combo = self.combinationsForTwoGames()
                len_combo = 9
            if len(games) is 3:
                get_combo = self.combinationsForThreeGames()
                len_combo = 27
            if len(games) is 4:
                get_combo = self.combinationsForFourGames()
                len_combo = 81

            combos = self.get_per_outcome(get_combo)
            get_games = self.get_game_combinations(get_combo, games)
            match = int(len(get_games))
            game = int(len(combos))
            new_combo = self.combine_combo_list_with_game_list(combos, get_games, match, game)
            get_num = list(self.break_list_into_equal_chunks(new_combo, len(games)))
            get_odds_combo = self.get_length_of_combo(get_num, len_combo, len(games))
            get_all_odds_combo = self.get_combined_games(get_odds_combo, self.bookies_name.get())
            get_combined_decimals = list(self.break_list_into_equal_chunks(get_all_odds_combo, len(games)))
            get_combined_calculation = self.comebined_calculations(get_combined_decimals, int(get_stake), len(games))
            get_all_combinations = self.merge_per_game_with_odds(get_odds_combo, get_combined_decimals, get_combined_calculation)

            for row in range(0, len(get_all_combinations)):
                get_all_combinations_dict[row] = get_all_combinations[row]

            get_all_combinations_dict.update({
                'stake':get_stake,
                'match': final_chosen_games,
            })

            s = json.dumps(get_all_combinations_dict, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
            with open(self.base_dir + "/accumulator/static/json/get_all_combinations.json", "w") as f:
                f.write(s)

            total_stake = self.calculate_total_stake(int(get_stake), int(len(get_combo)))
            combinations_below_stake = self.combinations_below_stake(get_all_combinations, total_stake, len_combo)
            cal_in_percent = self.calculate_percent(get_all_combinations, total_stake)
            self.main_page_load = False
            self.turnChosenAccumulatorsToJson(get_stake, total_stake, len(games), get_all_combinations)

            if request.POST.get('get_all_accumulator') == 'True':
                mad_combos = True

            if request.POST.get('get_an_accumulator') == 'True':
                mad_combos2 = True

            context = {
                'total_games': int(len(get_combo)),
                'calculation': combinations_below_stake,
                'calc_in_percent': cal_in_percent,
                'main_page_load': self.main_page_load,
                'mad_combos': mad_combos,
                'mad_combos2': mad_combos2,
            }
            return render(request, self.template_name, self.get_context_data(**context))
        except UnboundLocalError as e:
            print('UnboundLocalError ' + str(e))
        except AttributeError as e:
            print('AttributeError ' + str(e))
        except ValueError as e:
            print('ValueError ' + str(e))
        except TypeError as e:
            print('TypeError ' + str(e))
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def turnChosenAccumulatorsToJson(self, get_stake, total_stake, no_games, get_all_combinations):
        row_dict = {}
        row_list = list()
        conn = connection.cursor()

        if no_games is 2:
            conn.execute('''CREATE TEMPORARY TABLE AccumulatorTable(team_a_id INT NOT NULL, team_a_outcome CHAR(10) NOT NULL, team_b_id INT NOT NULL, team_b_outcome CHAR(10) NOT NULL, match_odds_1 DECIMAL(5,2) NOT NULL DEFAULT 0.00, match_odds_2 DECIMAL(5,2) NOT NULL DEFAULT 0.00, gross_profit DECIMAL(5,2) NOT NULL)''')

            for row in range(0, len(get_all_combinations)):
                conn.execute('''INSERT INTO AccumulatorTable(team_a_id, team_a_outcome, team_b_id, team_b_outcome, match_odds_1, match_odds_2, gross_profit) VALUES(%s, %s, %s, %s, %s, %s, %s)''',
                (get_all_combinations[row][0][0], get_all_combinations[row][0][1], get_all_combinations[row][0][2], get_all_combinations[row][0][3], get_all_combinations[row][1][0], get_all_combinations[row][1][1], get_all_combinations[row][2]))

            conn.execute('''SELECT * FROM AccumulatorTable;''')
            for row in range(0, len(get_all_combinations)):
                row_list.append(conn.fetchone())

            for row in range(0, len(row_list)):
                row_dict[row] = row_list[row]

            s = json.dumps(row_dict, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
            with open(self.base_dir + "/accumulator/static/json/test2.json", "w") as f:
                f.write(s)

            conn.close()

    def turnGamesWithOddsIntoJson(self, turn_to_json):
        row_dict = {}
        row_list = list()
        conn = connection.cursor()
        conn.execute('''CREATE TEMPORARY TABLE GamesWithOdds(match_games VARCHAR(100) NOT NULL, home_odds DECIMAL(5,2) NOT NULL DEFAULT 0.00, draw_odds DECIMAL(5,2) NOT NULL DEFAULT 0.00, away_odds DECIMAL(5,2) NOT NULL DEFAULT 0.00, games_id INT NOT NULL);''')

        for row in range(0, len(turn_to_json)):
            conn.execute('''INSERT INTO GamesWithOdds(match_games, home_odds, draw_odds, away_odds, games_id) VALUES(%s, %s, %s, %s, %s)''',(turn_to_json[row][0], turn_to_json[row][1], turn_to_json[row][2], turn_to_json[row][3], turn_to_json[row][4]))

        conn.execute('''SELECT * FROM GamesWithOdds;''')

        for row in range(0, len(turn_to_json)):
            row_list.append(conn.fetchone())

        for row in range(0, len(row_list)):
            row_dict[row] = row_list[row]

        s = json.dumps(row_dict, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
        with open(self.base_dir + "/accumulator/static/json/test.json", "w") as f:
            f.write(s)

        conn.close()
