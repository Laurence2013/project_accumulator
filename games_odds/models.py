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

class WilliamHillCsvLinks(models.Model):
    url_name = models.CharField(max_length = 50)
    get_match_odds_link_csv = models.CharField(max_length = 100)
    ids_for_tag_span_link_csv = models.CharField(max_length = 100)
    ids_for_tag_tbody_link_csv = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.url_name

# class CoralCsvLinks(models.Model):
#     url_name = models.CharField(max_length = 50, blank=True)
#     get_match_odds_link_csv = models.CharField(max_length = 100, blank=True)
#     ids_for_tag_span_link_csv = models.CharField(max_length = 100, blank=True)
#     ids_for_tag_tbody_link_csv = models.CharField(max_length = 100, blank=True)
#     date_updated = models.DateTimeField(auto_now_add = True, blank=True)
#
#     def __str__(self):
#         return self.url_name

class WilliamHillGames0(models.Model):
    url_game_link = models.ForeignKey(WilliamHillCsvLinks, on_delete = models.CASCADE)
    games = models.CharField(max_length = 300)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class WilliamHillGames1(models.Model):
    url_game_link = models.ForeignKey(WilliamHillCsvLinks, on_delete = models.CASCADE)
    games = models.CharField(max_length = 300)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class WilliamHillGames2(models.Model):
    url_game_link = models.ForeignKey(WilliamHillCsvLinks, on_delete = models.CASCADE)
    games = models.CharField(max_length = 300)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class WilliamHillGames3(models.Model):
    url_game_link = models.ForeignKey(WilliamHillCsvLinks, on_delete = models.CASCADE)
    games = models.CharField(max_length = 300)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class WilliamHillGames4(models.Model):
    url_game_link = models.ForeignKey(WilliamHillCsvLinks, on_delete = models.CASCADE)
    games = models.CharField(max_length = 300)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class WilliamHillGames5(models.Model):
    url_game_link = models.ForeignKey(WilliamHillCsvLinks, on_delete = models.CASCADE)
    games = models.CharField(max_length = 300)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class WilliamHillGames6(models.Model):
    url_game_link = models.ForeignKey(WilliamHillCsvLinks, on_delete = models.CASCADE)
    games = models.CharField(max_length = 300)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.games

class WilliamHillOdds0(models.Model):
    games = models.ForeignKey(WilliamHillGames0, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class WilliamHillOdds1(models.Model):
    games = models.ForeignKey(WilliamHillGames1, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class WilliamHillOdds2(models.Model):
    games = models.ForeignKey(WilliamHillGames2, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class WilliamHillOdds3(models.Model):
    games = models.ForeignKey(WilliamHillGames3, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class WilliamHillOdds4(models.Model):
    games = models.ForeignKey(WilliamHillGames4, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class WilliamHillOdds5(models.Model):
    games = models.ForeignKey(WilliamHillGames5, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)

class WilliamHillOdds6(models.Model):
    games = models.ForeignKey(WilliamHillGames6, on_delete = models.CASCADE)
    home_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    draw_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    away_odds = models.DecimalField(max_digits = 5, decimal_places = 2)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.games)
