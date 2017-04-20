from django.conf.urls import include, url
from django.contrib import admin
from accumulator.views import AccumulatorPageGamesView
from games_odds.views import ManageMatchesAndOdds

urlpatterns = [
    url(r'^index/$', AccumulatorPageGamesView.as_view(), name='view'),
    url(r'^manage_matches/', ManageMatchesAndOdds.as_view(), name='matches'),
    url(r'^admin/', admin.site.urls),
]
