from django.conf.urls import include, url
from django.contrib import admin
from accumulator.views import IndexPageGamesView

urlpatterns = [
    url(r'^index/$', IndexPageGamesView.as_view(), name='view'),
    url(r'^admin/', admin.site.urls),
]
