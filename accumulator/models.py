from django.db import models

# Games Table
class Game(models.Model):
    games = models.CharField(max_length = 50)
    time = models.TimeField((u"Time of Game"), blank=True)
    date_of_game = models.DateField((u"Date of Game"), blank=True)
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
