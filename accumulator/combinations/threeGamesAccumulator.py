class ThreeGamesAccumulator():
    def combinationsForThreeGames(self):
        return [(x,y,z) for x in ['H','D','A'] for y in ['H','D','A'] for z in ['H','D','A']]

    def getLengthOfCombo(self, matchList,matchLen):
        getOdds = []
        for m in range(0,matchLen):
            getOdds.append(self.__getIdAndOutcome(matchList,m))
        return getOdds

    def __getIdAndOutcome(self, matchList, matchLen):
        getOdds = []
        for i in range(0,3):
            for j in range(0,3,2):
                getOdds.append(matchList[matchLen][i][j])
        return getOdds
