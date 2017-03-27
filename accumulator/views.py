from django.shortcuts import render
from accumulator.models import Game, Odd
from django.views.generic import TemplateView
from decimal import Decimal

class IndexPageGamesView(TemplateView):
    template_name = "accumulator/index.html"
    games = Game.objects.values_list('id','games')
    odds = Odd.objects.values_list('id','home_odds','draw_odds','away_odds')

    def get_games(self):
        odds_games = []
        for g in range(0,len(self.games)):
           for d in range(0,len(self.odds)):
              if self.games[g][0] is self.odds[d][0]:
                 odds_games.append(self.games[g] + self.odds[d])
        return odds_games

    def get_ammended_games(self, games):
        final_games = []
        for g in games:
           for h in g:
              if not isinstance(h, int):
                 final_games.append(h)
        return final_games

    def get_final_game(self, games):
        for n, i in enumerate(games):
           if isinstance(i, Decimal):
              games[n] = float(i)
        return games

    def breakListIntoEqualChunks(self, matchList, match_len):
        for i in range(0, len(matchList), match_len):
            yield matchList[i: i + match_len]

    def get_context_data(self, **kwargs):
        context = super(IndexPageGamesView, self).get_context_data(**kwargs)
        context['odds'] = list(self.breakListIntoEqualChunks(self.get_final_game
        (self.get_ammended_games(self.get_games())),4))
        return context

def combinationsForTwoGames(no_games):
    if no_games is 2:
        combos = [(x,y) for x in ['H','D','A'] for y in ['H','D','A']]
    return combos

def getPerOutcome(combos):
    count = 1
    comboList = []
    while count <= len(combos):
        for x in combos[count - 1]:
            comboList.append([count, x])
        count += 1
    return comboList

def getGameCombinations(combos, games):
    gameList = []
    for c in range(len(combos)):
        for g in games:
            gameList.append([g])
    return gameList

def combineComboListWithGameList(matchList, gameList, match_len, game_len):
    merge_combo_matches = []
    count = 1
    if match_len == game_len:
        while count <= match_len:
            merge_combo_matches.append(tuple(gameList[count - 1] + matchList[count - 1]))
            count += 1
    else:
        return False
    return merge_combo_matches

def breakListIntoEqualChunks(matchList, match_len):
    for i in range(0, len(matchList), match_len):
        yield matchList[i: i + match_len]

def getLengthOfCombo(matchList,matchLen):
    getOdds = []
    for m in range(0,matchLen):
        getOdds.append(getIdAndOutcome(matchList,m))
    return getOdds

def getIdAndOutcome(matchList, matchLen):
    getOdds = []
    for i in range(0,2):
        for j in range(0,3,2):
            getOdds.append(matchList[matchLen][i][j])
    return getOdds

def getTwoCombinedGames(matchList):
    calculate = []
    for m in range(0,len(matchList)):
       for n in range(0, len(matchList[m])):
          if isinstance(matchList[m][n], int) is True:
             game_id = Odd.objects.get(pk = matchList[m][n])
          else:
             if matchList[m][n] is 'H':
                calculate.append(game_id.home_odds)
             if matchList[m][n] is 'D':
                calculate.append(game_id.draw_odds)
             if matchList[m][n] is 'A':
                calculate.append(game_id.away_odds)
    return calculate

def calculateOddsForTwoMatches(oddsList):
    calculate = []
    for c in range(0, len(oddsList)):
        odds1 = oddsList[c][0]
        odds2 = oddsList[c][1]
        calc = 1 * (odds1 + 1) * (odds2 + 1) - 1
        calculate.append(calc)
    return calculate

def mergePerGameWithOdds(combinations, odds, calculation):
    combination = list(zip(combinations, odds, calculation))
    return combination
