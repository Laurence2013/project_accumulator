from collections import OrderedDict
from decimal import Decimal
from accumulator.models import *
from games_odds.models import *

class AccumulatorPageGames():
    def get_games(self, games, odds):
        bgames = []
        for game in range(0, len(games), 2):
            bgames.append(games[game:game + 2])
        for g in bgames:
            g.extend([g[0]])

        print()
        for odd in odds:
            od = OrderedDict(sorted(odd.items(), reverse=True))
            print(od)
        # for k,v in odds.items():
        #     print(k,v)

        # for g in range(0,len(games)):
        #    for d in range(0,len(odds)):
        #       if games[g][0] is odds[d][0]:
        #          odds_games.append(games[g] + odds[d])
        # print(odds_games)
        return None

    def get_ammended_games(self, games):
        final_games = []
        for g in games:
           for h in g:
              if not isinstance(h, int):
                 final_games.append(h)
        return final_games

    def get_final_game(self, games):
        for n, i in enumerate(games):
           if isinstance(i, Decimal):
              games[n] = float(i)
        return games

    def filter_accumulator(self, get_accumulator):
        game_id = []
        for g in range(0, len(get_accumulator)):
            game = Game.objects.values_list('id').filter(games = get_accumulator[g])
            for n in game:
                for m in n:
                    game_id.append(m)
        return game_id

    def calculate_total_stake(self, stake, num_of_games):
        return num_of_games * stake

    def comebined_calculations(self, combined_decimals, get_stake, len_games):
        if len_games is 2:
            return self.calculateOddsForTwoMatches(combined_decimals, get_stake)
        elif len_games is 3:
            return self.calculateOddsForThreeMatches(combined_decimals, get_stake)
        elif len_games is 4:
            return self.calculateOddsForFourMatches(combined_decimals, get_stake)

    def combinations_below_stake(self, get_all_combinations, total_stake, len_games):
        count = 0
        for combo in get_all_combinations:
            if combo[-1] < total_stake:
                count += 1
        return (count, len_games - count)

    def calculate_percent(self, get_all_combinations, total_stake):
        counter_below = 0
        counter_above = 0
        for combo in get_all_combinations:
            if combo[2] < total_stake:
                counter_below += 1
            else:
                counter_above += 1
        return [round((counter_below / total_stake * 100), 2), round((counter_above / total_stake * 100), 2)]

    def getting_matches_and_odds_from_db(self, bookie_list_id):
        print(bookie_list_id)
        bookie_id = None
        for b_id in bookie_list_id:
            bookie_id = b_id
        return bookie_id

    def get_bookies_ids(self, get_ids):
        getids = None
        for wh in get_ids.values():
            getids = wh
        return getids

    def extract_and_get_games(self,bookies_games):
        games = []
        for b_games in bookies_games:
           for each_match in list(b_games.values()):
              games.append(each_match)
        return games

    def extract_by_getting_odds(self, WilliamHillOdds, get_games_id):
        get_odds = []
        for game_id in get_games_id:
            for each_game in list(game_id.values()):
                get_odds.append(WilliamHillOdds.objects.values('home_odds','draw_odds','away_odds').get(games_id=each_game))
        return get_odds
