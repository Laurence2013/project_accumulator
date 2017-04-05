from accumulator.models import Odd

class TwoGamesAccumulator():
    def combinationsForTwoGames(self):
        return [(x,y) for x in ['H','D','A'] for y in ['H','D','A']]

    def getLengthOfCombo(self, matchList,matchLen):
        getOdds = []
        for m in range(0,matchLen):
            getOdds.append(self.getIdAndOutcome(matchList,m))
        return getOdds

    def getIdAndOutcome(self, matchList, matchLen):
        getOdds = []
        for i in range(0,2):
            for j in range(0,3,2):
                getOdds.append(matchList[matchLen][i][j])
        return getOdds

    def getTwoCombinedGames(self, matchList):
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

    def calculateOddsForTwoMatches(self, oddsList, stake):
        calculate = []
        for c in range(0, len(oddsList)):
            odds1 = oddsList[c][0]
            odds2 = oddsList[c][1]
            calc = (stake * (odds1 + 1) * (odds2 + 1)) - stake
            calculate.append(round(calc,2))
        return calculate

    def mergePerGameWithOdds(self, combinations, odds, calculation):
        combination = list(zip(combinations, odds, calculation))
        return combination
