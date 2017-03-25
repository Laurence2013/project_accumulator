from django.shortcuts import render
from accumulator.models import Game, Odd
from django.views.generic import ListView

class IndexPageGamesView(ListView):
    model = Odd
    template_name = "accumulator/index.html"
    context_object_name = 'games'

    def get_odds(self):
        odds = Odd.objects.values_list('id','home_odds','draw_odds','away_odds')
        oddsList = []
        for o in range(0,len(odds)):
           for j in range(0,len(odds[o])):
              if not isinstance(odds[o][j],int):
                 oddsList.append(float(odds[o][j]))
              else:
                 oddsList.append(odds[o][j])
        return oddsList

    def chunks(self,listOdds,oddslen):
        for i in range(0, len(listOdds), oddslen):
            yield listOdds[i:i+oddslen]

    def get_context_data(self, **kwargs):
        context = super(IndexPageGamesView, self).get_context_data(**kwargs)
        context['odds'] = list(self.chunks(self.get_odds(),4))
        return context

def combinationsForTwoGames(no_games):
    if no_games is 2:
        combos = [(x,y) for x in ['H','D','A'] for y in ['H','D','A']]
    return combos

def combinationsForThreeGames(no_games):
    if no_games is 3:
        combos = [(x,y,z) for x in ['H','D','A'] for y in ['H','D','A'] for z in ['H','D','A']]
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
