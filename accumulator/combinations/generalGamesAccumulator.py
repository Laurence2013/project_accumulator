from accumulator.models import *
from games_odds.models import *

class GeneralGamesAccumulator():
    def get_per_outcome(self, combinations):
        count = 1
        comboList = []
        while count <= len(combinations):
            for x in combinations[count - 1]:
                comboList.append([count, x])
            count += 1
        return comboList

    def get_game_combinations(self, combos, games):
        gameList = []
        for c in range(len(combos)):
            for g in games:
                gameList.append([g])
        return gameList

    def combine_combo_list_with_game_list(self, matchList, gameList, match_len, game_len):
        merge_combo_matches = []
        count = 1
        if match_len == game_len:
            while count <= match_len:
                merge_combo_matches.append(tuple(gameList[count - 1] + matchList[count - 1]))
                count += 1
        else:
            return False
        return merge_combo_matches

    def break_list_into_equal_chunks(self, matchList, match_len):
        for i in range(0, len(matchList), match_len):
            yield matchList[i: i + match_len]

    def get_length_of_combo(self, matchList,matchLen, maxRangeOfMatch):
        getOdds = []
        for m in range(0,matchLen):
            getOdds.append(self.__get_id_and_outcome(matchList,m, maxRangeOfMatch))
        return getOdds

    def __get_id_and_outcome(self, matchList, matchLen, maxRangeOfMatch):
        getOdds = []
        for i in range(0,maxRangeOfMatch):
            for j in range(0,3,2):
                getOdds.append(matchList[matchLen][i][j])
        return getOdds

    def get_combined_games(self, matchList, bookies_name):
        calculate = []
        for m in range(0,len(matchList)):
           for n in range(0, len(matchList[m])):
              if isinstance(matchList[m][n], int) is True:
                 game_id = bookies_name.objects.get(pk = matchList[m][n])
              else:
                 if matchList[m][n] is 'H':
                    calculate.append(game_id.home_odds)
                 if matchList[m][n] is 'D':
                    calculate.append(game_id.draw_odds)
                 if matchList[m][n] is 'A':
                    calculate.append(game_id.away_odds)
        return calculate

    def merge_per_game_with_odds(self, combinations, odds, calculation):
        combination = list(zip(combinations, odds, calculation))
        return combination
