from django.shortcuts import render
from accumulator.models import Game, Odd
from django.views.generic import TemplateView, View
from decimal import Decimal
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator
from accumulator.combinations.threeGamesAccumulator import ThreeGamesAccumulator
from accumulator.accumulatorPageGames.accumulatorPageGames import AccumulatorPageGames

class AccumulatorPageGamesView(TemplateView, View, TwoGamesAccumulator, ThreeGamesAccumulator, AccumulatorPageGames):
    template_name = "accumulator/index.html"
    games = Game.objects.values_list('id','games')
    odds = Odd.objects.values_list('id','home_odds','draw_odds','away_odds')

    def get_context_data(self, **kwargs):
        context = super(AccumulatorPageGamesView, self).get_context_data(**kwargs)
        context['odds'] = list(self.breakListIntoEqualChunks(self.get_final_game
        (self.get_ammended_games(self.get_games())),4))
        return context

    def post(self, request, *args, **kwargs):
        try:
            request.method == "POST"
            get_accumulator = request.POST.getlist("accumulator")
            get_stake = request.POST.get("stake")

            games = self.filter_accumulator(get_accumulator)

            if len(games) is 2:

                get_combos = self.combinationsForTwoGames(len(games))
                combos = self.getPerOutcome(get_combos)
                get_games = self.getGameCombinations(get_combos, games)
                match = int(len(get_games))
                game = int(len(combos))
                new_combo = self.combineComboListWithGameList(combos, get_games, match, game)
                get_num = list(self.breakListIntoEqualChunks(new_combo, 2))
                get_odds_combo = self.getLengthOfCombo(get_num,int(len(get_combos)))
                get_all_odds_combo = self.getTwoCombinedGames(get_odds_combo)
                get_combined_decimals = list(self.breakListIntoEqualChunks(get_all_odds_combo, 2))
                get_combined_calculation = self.calculateOddsForTwoMatches(get_combined_decimals, int(get_stake))
                get_all_combinations = self.mergePerGameWithOdds(get_odds_combo, get_combined_decimals, get_combined_calculation)

            elif len(games) is 3:
                
                get_combos = self.combinationsForThreeGames(len(games))
                print(get_combos)


        except UnboundLocalError as e:
            print('UnboundLocalError ' + str(e))
        except AttributeError as e:
            print('AttributeError ' + str(e))
        except ValueError as e:
            print('ValueError ' + str(e))
        except TypeError as e:
            print('TypeError ' + str(e))
        else:
            total_stake = self.calculate_total_stake(int(get_stake), int(len(get_combos)))
            context = {
                'combinations': get_all_combinations,
                'match': get_accumulator,
                'stake': get_stake,
                'total_games': int(len(get_combos)),
                'total_stake': total_stake,
            }
            return render(request, self.template_name, self.get_context_data(**context))
        return render(request, self.template_name, self.get_context_data(**kwargs))
