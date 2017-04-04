from decimal import Decimal
from accumulator.models import Game

class AccumulatorPageGames():
    def get_games(self):
        odds_games = []
        for g in range(0,len(self.games)):
           for d in range(0,len(self.odds)):
              if self.games[g][0] is self.odds[d][0]:
                 odds_games.append(self.games[g] + self.odds[d])
        return odds_games

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
