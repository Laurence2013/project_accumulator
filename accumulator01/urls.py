from django.conf.urls import include, url
from django.contrib import admin
from accumulator.views import AccumulatorPageGamesView

urlpatterns = [
    url(r'^index/$', AccumulatorPageGamesView.as_view(), name='view'),
    url(r'^admin/', admin.site.urls),
]
