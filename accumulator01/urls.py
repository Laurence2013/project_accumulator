from django.conf.urls import include, url
from django.contrib import admin
from accumulator.views import JsonAsView, GetBookiesDailyGames, AccumulatorPageGamesView, GamesJsonAsView, GetAllCombinations
from games_odds.views import Bookies, Main_William_Hill, William_Hill_Games_0, William_Hill_Games_1, William_Hill_Games_2, William_Hill_Games_3, William_Hill_Games_4, William_Hill_Games_5, William_Hill_Games_6, SortGamesOddsIntoDb, Coral_Games, GetAllCoralGameDates, GetAllCoralMatchDayGames, Get_Coral_Matches_0, Get_Coral_Matches_1, Get_Coral_Matches_2, Get_Coral_Matches_3

urlpatterns = [
    url(r'^index/$', AccumulatorPageGamesView.as_view(), name='accumulator'),
    url(r'^index/(?P<slug>[\w\s]+)/$', AccumulatorPageGamesView.as_view(), name='accumulator_bookies_name'),

    url(r'^index/(?P<slug>[\w\s]+|0)/daily_match_dates/$', JsonAsView.as_view(), name='json'),
    url(r'^index/(?P<slug>[\w\s]+)/combos/$', GetAllCombinations.as_view(), name='get_all_combinations'),
    url(r'^index/(?P<games_json>[\w\s]+)/daily_match_games/$', GamesJsonAsView.as_view(), name='games_json'),
    url(r'^index/(?P<slug>[\w\s]+)/(?P<daily_games_id>[\d]+)/$', GetBookiesDailyGames.as_view(), name='bookies_daily_games_id'),

    url(r'^bookies/$', Bookies.as_view(), name='bookies'),
    url(r'^william_hill/(?P<update_no>[0-1]+|0)/$', Main_William_Hill.as_view(), name='william_hill'),
    url(r'^william_hill_update/(?P<update_no>[0-9]+|0)/$', Main_William_Hill.as_view(), name='william_hill_update'),

    url(r'^bookies/coral/(?P<update_no>[0-1]+|0)/$', Coral_Games.as_view(), name='coral'),
    url(r'^bookies/coral/(?P<coral_game_dates>[0-1]+)/coral_matchday_dates/$', GetAllCoralGameDates.as_view(), name='coral_game_dates'),
    url(r'^bookies/coral/(?P<update_no>[0-1]+|0)/(?P<matchday_games_id>[0-9]+)/$', GetAllCoralMatchDayGames.as_view(), name='matchday_games_id'),
    url(r'^bookies/coral/(?P<update_no>[0-1]+|0)/(?P<matchday_games_id>[0-9]+)/coral_matches_0/$', Get_Coral_Matches_0.as_view(), name='coral_matches_0'),
    url(r'^bookies/coral/(?P<update_no>[0-1]+|0)/(?P<matchday_games_id>[0-9]+)/coral_matches_1/$', Get_Coral_Matches_1.as_view(), name='coral_matches_1'),
    url(r'^bookies/coral/(?P<update_no>[0-1]+|0)/(?P<matchday_games_id>[0-9]+)/coral_matches_2/$', Get_Coral_Matches_2.as_view(), name='coral_matches_2'),
    url(r'^bookies/coral/(?P<update_no>[0-1]+|0)/(?P<matchday_games_id>[0-9]+)/coral_matches_3/$', Get_Coral_Matches_3.as_view(), name='coral_matches_3'),
    # url(r'^bookies/corals/(?P<match_day>[\w\s]+)/$', Get_Coral_Matches_0.as_view(), name='coral_matches_0'),
    # url(r'^bookies/coral/(?P<coral_game_dates>[\w\s]+)/coral_matchday_dates/$', GetAllCoralGameDates.as_view(), name='coral_game_dates'),

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
