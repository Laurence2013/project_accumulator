from django.conf.urls import include, url
from django.contrib import admin
from accumulator.views import AccumulatorPageGamesView
from games_odds.views import Bookies, Main_William_Hill, William_Hill_Games_0, William_Hill_Games_1, William_Hill_Games_2, William_Hill_Games_3, William_Hill_Games_4, William_Hill_Games_5, William_Hill_Games_6, SortGamesOddsIntoDb

urlpatterns = [
    url(r'^index/$', AccumulatorPageGamesView.as_view(), name='view'),
    url(r'^bookies/$', Bookies.as_view(), name='bookies'),
    url(r'^william_hill/$', Main_William_Hill.as_view(), name='william_hill'),
    url(r'^william_hill_games_0/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_0.as_view(), name='william_hill_0'),
    url(r'^william_hill_games_1/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_1.as_view(), name='william_hill_1'),
    url(r'^william_hill_games_2/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_2.as_view(), name='william_hill_2'),
    url(r'^william_hill_games_3/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_3.as_view(), name='william_hill_3'),
    url(r'^william_hill_games_4/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_4.as_view(), name='william_hill_4'),
    url(r'^william_hill_games_5/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_5.as_view(), name='william_hill_5'),
    url(r'^william_hill_games_6/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_6.as_view(), name='william_hill_6'),

    url(r'^sort_games_into_db/(?P<link_no>[a-z_0-9]+|0)/$', SortGamesOddsIntoDb.as_view(), name='sort_games_into_db'),
    url(r'^admin/', admin.site.urls),
]
