import datetime
from django.test import TestCase
from games_odds.william_hill_base import WilliamHillBase
from games_odds.models import TimeOfRefreshWilliamHill1

class TestingRefreshDateAndTime1(TestCase, WilliamHillBase):
    def setUp(self):
        refresh_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        TimeOfRefreshWilliamHill1.objects.all()
        refresh = TimeOfRefreshWilliamHill1(william_hill_id=str('william_hill_1'), date_of_refresh=refresh_time)
        refresh.save()
        self.get_refresh_date_0 = TimeOfRefreshWilliamHill1.objects.last()

    def test_get_last_date_for_TimeOfRefreshWilliamHill0(self):
        get_refresh_date = self.get_refresh(str('TimeOfRefreshWilliamHill1'))
        self.assertEqual(self.get_refresh_date_0, get_refresh_date)
