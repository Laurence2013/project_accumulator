import json
from django.conf import settings
from django.shortcuts import render
from accumulator.models import *
from django.views.generic import TemplateView
from decimal import Decimal
from django.core import serializers
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator
from accumulator.combinations.threeGamesAccumulator import ThreeGamesAccumulator
from accumulator.combinations.fourGamesAccumulator import FourGamesAccumulator
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator
from accumulator.accumulatorPageGames.accumulatorPageGames import AccumulatorPageGames

class AccumulatorPageGamesView(TemplateView, TwoGamesAccumulator, ThreeGamesAccumulator, FourGamesAccumulator, AccumulatorPageGames, GeneralGamesAccumulator):
    template_name = "accumulator/index.html"
    template_bookies = "accumulator/bookies.html"
    games = Game.objects.values_list('id','games')
    match_info = MatchInfo.objects.values_list('daily_matches', 'combinations')
    odds = Odd.objects.values_list('id','home_odds','draw_odds','away_odds')
    get_bookies = Bookie.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AccumulatorPageGamesView, self).get_context_data(**kwargs)
        context['infos'] = self.match_info
        context['bookies'] = self.get_bookies
        context['odds'] = list(self.break_list_into_equal_chunks(self.get_final_game(self.get_ammended_games(self.get_games())),4))
        return context

    def get(self, request, *args, **kwargs):
        base_dir = settings.BASE_DIR
        if kwargs.get('slug'):
            bookie = kwargs.get('slug')
            bookie_name = Bookie.objects.get(bookies_name=bookie)
            bookie_games = WilliamHillDailyMatche.objects.all().filter(bookies=bookie_name)
            bookie_games = serializers.serialize('json', bookie_games)
            daily_games = json.dumps(bookie_games)
            with open(base_dir + '/accumulator/static/json/daily_match_dates.json', 'w') as f:
                f.write(daily_games)

        return render(request, self.template_name, self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        try:
            request.method == "POST"
            get_accumulator = request.POST.getlist("accumulator")
            get_stake = request.POST.get("stake")
            games = self.filter_accumulator(get_accumulator)

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
            get_all_odds_combo = self.get_combined_games(get_odds_combo)
            get_combined_decimals = list(self.break_list_into_equal_chunks(get_all_odds_combo, len(games)))
            get_combined_calculation = self.comebined_calculations(get_combined_decimals, int(get_stake), len(games))
            get_all_combinations = self.merge_per_game_with_odds(get_odds_combo, get_combined_decimals, get_combined_calculation)
            total_stake = self.calculate_total_stake(int(get_stake), int(len(get_combo)))
            combinations_below_stake = self.combinations_below_stake(get_all_combinations, total_stake, len_combo)
            cal_in_percent = self.calculate_percent(get_all_combinations, total_stake)

            context = {
                'combinations': get_all_combinations,
                'match': get_accumulator,
                'stake': get_stake,
                'total_games': int(len(get_combo)),
                'total_stake': total_stake,
                'calculation': combinations_below_stake,
                'length_combo': len(games),
                'calc_in_percent': cal_in_percent,
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
