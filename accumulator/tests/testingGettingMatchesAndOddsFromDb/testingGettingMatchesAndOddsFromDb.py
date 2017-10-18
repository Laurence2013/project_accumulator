from django.tests import TestCase
from games_odds.models import *
from accumulator.accumulatorPageGames import accumulatorPageGames

class TestingGettingMatchesAndOddsFromDb(TestCase):
    def setUp(self):
        WilliamHillDailyMatche.objects.create(id=66, date_of_games='Today 12 Oct 17', date_updated='2017-10-12 17:02:20', bookies_id=1, wh_csv_links_id=1)
        WilliamHillGames0.objects.create(id=89, games='ARC Oleiros   v   Sporting Lisbon', date_updated='2017-10-12 16:57:18', url_game_link_id=1)
        WilliamHillOdds0.objects.create(id=89, home_odds=16.00, draw_odds=10.00, away_odds=0.04, date_updated='2017-10-12 16:57:20', games_id=89)

    def get_unique_id_from_user_selection_of_bookies_match_date_from_home_page(self):
        accumGames = AccumulatorPageGames()
        match_day_id = accumGames.getting_matches_and_odds_from_db(66):
        self.assertEqual(match_day_id,wh_unique_match_id)
