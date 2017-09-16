from django.conf.urls import include, url
from django.contrib import admin
from accumulator.views import AccumulatorPageGamesView
from games_odds.views import ManageMatchesAndOdds, Main_William_Hill

urlpatterns = [
    url(r'^index/$', AccumulatorPageGamesView.as_view(), name='view'),
    url(r'^manage_matches/', ManageMatchesAndOdds.as_view(), name='matches'),
    url(r'^william_hill/$', Main_William_Hill.as_view(), name='william_hill'),
    url(r'^admin/', admin.site.urls),
]
