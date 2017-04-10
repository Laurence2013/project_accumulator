class FourGamesAccumulator():
    def combinationsForFourGames(self):
        return [(w,x,y,z) for w in ['H','D','A'] for x in ['H','D','A'] for y in ['H','D','A'] for z in ['H','D','A']]

    def calculateOddsForFourMatches(self, oddsList, stake):
        calculate = []
        for c in range(0, len(oddsList)):
            odds1 = oddsList[c][0]
            odds2 = oddsList[c][1]
            odds3 = oddsList[c][2]
            odds4 = oddsList[c][3]
            #calc = (stake * (odds1 + 1) * (odds2 + 1) * (odds3 + 1)) - stake
            calc = (stake * odds1 * odds2 * odds3 * odds4) - stake
            calculate.append(round(calc,2))
        return calculate
