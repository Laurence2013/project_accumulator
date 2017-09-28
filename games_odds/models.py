from django.db import models

class TimeOfRefreshWilliamHill0(models.Model):
    date_of_refresh = models.CharField(max_length = 100)
    william_hill_id = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.date_of_refresh

class TimeOfRefreshWilliamHill1(models.Model):
    date_of_refresh = models.CharField(max_length = 100)
    william_hill_id = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.date_of_refresh

class TimeOfRefreshWilliamHill2(models.Model):
    date_of_refresh = models.CharField(max_length = 100)
    william_hill_id = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.date_of_refresh

class TimeOfRefreshWilliamHill3(models.Model):
    date_of_refresh = models.CharField(max_length = 100)
    william_hill_id = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.date_of_refresh

class TimeOfRefreshWilliamHill4(models.Model):
    date_of_refresh = models.CharField(max_length = 100)
    william_hill_id = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.date_of_refresh

class TimeOfRefreshWilliamHill5(models.Model):
    date_of_refresh = models.CharField(max_length = 100)
    william_hill_id = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.date_of_refresh

class TimeOfRefreshWilliamHill6(models.Model):
    date_of_refresh = models.CharField(max_length = 100)
    william_hill_id = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.date_of_refresh

class GameUrlLink0(models.Model):
    games = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class GameUrlLink1(models.Model):
    games = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class GameUrlLink2(models.Model):
    games = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class GameUrlLink3(models.Model):
    games = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class GameUrlLink4(models.Model):
    games = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class GameUrlLink5(models.Model):
    games = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class GameUrlLink6(models.Model):
    games = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class OddsGameUrlLink0(models.Model):
    games = models.ForeignKey(GameUrlLink0, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class OddsGameUrlLink1(models.Model):
    games = models.ForeignKey(GameUrlLink1, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class OddsGameUrlLink2(models.Model):
    games = models.ForeignKey(GameUrlLink2, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class OddsGameUrlLink3(models.Model):
    games = models.ForeignKey(GameUrlLink3, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class OddsGameUrlLink4(models.Model):
    games = models.ForeignKey(GameUrlLink4, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class OddsGameUrlLink5(models.Model):
    games = models.ForeignKey(GameUrlLink4, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class OddsGameUrlLink6(models.Model):
    games = models.ForeignKey(GameUrlLink5, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

# class OddsGameTimeUpdateUrlLink0(models.Model):
