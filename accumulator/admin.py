from django.contrib import admin
from .models import Game, Odd, MatchInfo, Bookie, WilliamHillDailyMatche, WilliamHillGamesWithOdds0, CoralDailyMatche, CoralGames0, CoralOdds0

admin.site.register(Game)
admin.site.register(Odd)
admin.site.register(MatchInfo)
admin.site.register(Bookie)
admin.site.register(WilliamHillDailyMatche)
admin.site.register(WilliamHillGamesWithOdds0)

admin.site.register(CoralDailyMatche)
admin.site.register(CoralGames0)
admin.site.register(CoralOdds0)
