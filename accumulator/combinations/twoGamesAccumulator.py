class TwoGamesAccumulator():
    def combinationsForTwoGames(self):
        return [(x,y) for x in ['H','D','A'] for y in ['H','D','A']]

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
