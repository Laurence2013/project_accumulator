from django.shortcuts import render
from accumulator.models import Game, Odd
from django.views.generic import TemplateView, RedirectView
from decimal import Decimal
from accumulator.combinations.twoGamesAccumulator import TwoGamesAccumulator

class IndexPageGamesView(TemplateView, RedirectView, TwoGamesAccumulator):
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
              games[n] = round(i, 2)
        return games

    def get_context_data(self, **kwargs):
        context = super(IndexPageGamesView, self).get_context_data(**kwargs)
        context['odds'] = list(self.breakListIntoEqualChunks(self.get_final_game
        (self.get_ammended_games(self.get_games())),4))
        return context

    def get_redirect_url(self, *args, **kwargs):
        return super(IndexPageGamesView, self).get_redirect_url(*args, **kwargs)
