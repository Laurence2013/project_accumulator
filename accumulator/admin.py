from django.contrib import admin
from .models import Game, Odd, MatchInfo, Bookie, BookiesDailyMatche

admin.site.register(Game)
admin.site.register(Odd)
admin.site.register(MatchInfo)
admin.site.register(Bookie)
admin.site.register(BookiesDailyMatche)
