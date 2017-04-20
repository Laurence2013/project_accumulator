from django.conf.urls import url
from games_odds import views

urlpatterns = [
    url(r'^$', views.manage_matches, name='manage_matches'),
]
