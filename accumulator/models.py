from django.db import models
from games_odds.models import *

# Games Table
class Game(models.Model):
    games = models.CharField(max_length = 50)
    time = models.TimeField((u"Time of Game"), null=True)
    date_of_game = models.DateField((u"Date of Game"), null=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class Odd(models.Model):
    games = models.ForeignKey(Game, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class MatchInfo(models.Model):
    daily_matches = models.CharField(max_length = 200)
    combinations = models.CharField(max_length = 200)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.daily_matches)

class Bookie(models.Model):
    bookies_name = models.CharField(max_length = 50)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.bookies_name

class WilliamHillDailyMatche(models.Model):
    bookies = models.ForeignKey(Bookie, on_delete = models.CASCADE)
    wh_csv_links = models.ForeignKey(WilliamHillCsvLinks, on_delete = models.CASCADE)
    dates_of_games = models.CharField(max_length = 50)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.dates_of_games

class WilliamHillGamesWithOdds0(models.Model):
    match = models.CharField(max_length = 200)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    games_id = models.IntegerField(default = 0)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.match

class CoralDailyMatche(models.Model):
    bookies = models.ForeignKey(Bookie, on_delete = models.CASCADE)
    dates_of_games = models.CharField(max_length = 50)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.dates_of_games

# class CoralDailyMatche(models.Model):
#     bookies = models.ForeignKey(Bookie, on_delete = models.CASCADE)
#     coral_csv_links = models.ForeignKey(CoralCsvLinks, on_delete = models.CASCADE)
#     dates_of_games = models.CharField(max_length = 50)
#     date_updated = models.DateTimeField(auto_now_add = True)
#
#     def __str__(self):
#         return self.dates_of_games
