from django.shortcuts import render
from accumulator.models import Game, Odd
from django.views.generic import TemplateView, View
from decimal import Decimal
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator

class IndexPageGamesView(TemplateView, View, TwoGamesAccumulator):
    template_name = "accumulator/index.html"
    games = Game.objects.values_list('id','games')
    odds = Odd.objects.values_list('id','home_odds','draw_odds','away_odds')

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

    def get_context_data(self, **kwargs):
        context = super(IndexPageGamesView, self).get_context_data(**kwargs)
        context['odds'] = list(self.breakListIntoEqualChunks(self.get_final_game
        (self.get_ammended_games(self.get_games())),4))
        return context

    def __filter_accumulator(self, get_accumulator):
        game_id = []
        if len(get_accumulator) is 2:
            for g in range(0, len(get_accumulator)):
                game = Game.objects.values_list('id').filter(games = get_accumulator[g])
                for n in game:
                    for m in n:
                        game_id.append(m)
        return game_id

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            get_accumulator = request.POST.getlist("Accumulator")

        games = self.__filter_accumulator(get_accumulator)
        get_combos = self.combinationsForTwoGames(len(games))
        combos = self.getPerOutcome(get_combos)
        get_games = self.getGameCombinations(get_combos, games)
        match = int(len(get_games))
        game = int(len(combos))
        new_combo = self.combineComboListWithGameList(combos, get_games, match, game)
        get_num = list(self.breakListIntoEqualChunks(new_combo, 2))
        get_odds_combo = self.getLengthOfCombo(get_num,9)
        get_all_odds_combo = self.getTwoCombinedGames(get_odds_combo)
        get_combined_decimals = list(self.breakListIntoEqualChunks(get_all_odds_combo, 2))
        get_combined_calculation = self.calculateOddsForTwoMatches(get_combined_decimals)
        get_all_combinations = self.mergePerGameWithOdds(get_odds_combo, get_combined_decimals, get_combined_calculation)

        for g in get_all_combinations:
            print(g)

        return render(request, self.template_name, self.get_context_data(**kwargs))
