class ThreeGamesAccumulator():
    def combinationsForThreeGames(self):
        return [(x,y,z) for x in ['H','D','A'] for y in ['H','D','A'] for z in ['H','D','A']]

    def calculateOddsForThreeMatches(self, oddsList, stake):
        calculate = []
        for c in range(0, len(oddsList)):
            odds1 = oddsList[c][0]
            odds2 = oddsList[c][1]
            odds3 = oddsList[c][2]
            calc = (stake * (odds1 + 1) * (odds2 + 1) * (odds3 + 1)) - stake
            calculate.append(round(calc,2))
        return calculate
