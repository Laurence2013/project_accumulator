import datetime
from django.test import TestCase
from games_odds.william_hill_base import WilliamHillBase
from games_odds.models import TimeOfRefreshWilliamHill0

class TestingRefreshDateAndTime0(TestCase, WilliamHillBase):
    def setUp(self):
        refresh_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        TimeOfRefreshWilliamHill0.objects.all()
        refresh = TimeOfRefreshWilliamHill0(william_hill_id=str('william_hill_0'), date_of_refresh=refresh_time)
        refresh.save()
        self.get_refresh_date_0 = TimeOfRefreshWilliamHill0.objects.last()

    def test_get_last_date_for_TimeOfRefreshWilliamHill0(self):
        get_refresh_date = self.get_refresh(str('TimeOfRefreshWilliamHill0'))
        self.assertEqual(self.get_refresh_date_0, get_refresh_date)
