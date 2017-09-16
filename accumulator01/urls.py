from django.conf.urls import include, url
from django.contrib import admin
from accumulator.views import AccumulatorPageGamesView
from games_odds.views import Bookies, Main_William_Hill, William_Hill_Games_0

urlpatterns = [
    url(r'^index/$', AccumulatorPageGamesView.as_view(), name='view'),
    url(r'^bookies/$', Bookies.as_view(), name='bookies'),
    url(r'^william_hill/$', Main_William_Hill.as_view(), name='william_hill'),
    url(r'^william_hill_games_0/$', William_Hill_Games_0.as_view(), name='william_hill_0'),
    url(r'^admin/', admin.site.urls),
]
