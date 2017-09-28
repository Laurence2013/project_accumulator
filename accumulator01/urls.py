from django.conf.urls import include, url
from django.contrib import admin
from accumulator.views import AccumulatorPageGamesView
from games_odds.views import Bookies, Main_William_Hill, William_Hill_Games_0, William_Hill_Games_1, William_Hill_Games_2, William_Hill_Games_3

urlpatterns = [
    url(r'^index/$', AccumulatorPageGamesView.as_view(), name='view'),
    url(r'^bookies/$', Bookies.as_view(), name='bookies'),
    url(r'^william_hill/$', Main_William_Hill.as_view(), name='william_hill'),
    url(r'^william_hill_games_0/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_0.as_view(), name='william_hill_0'),
    url(r'^william_hill_games_1/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_1.as_view(), name='william_hill_1'),
    url(r'^william_hill_games_2/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_2.as_view(), name='william_hill_2'),
    url(r'^william_hill_games_3/(?P<refresh_no>[0-9]+|0)/$', William_Hill_Games_3.as_view(), name='william_hill_3'),
    url(r'^admin/', admin.site.urls),
]
