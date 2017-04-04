class ThreeGamesAccumulator():
    def combinationsForThreeGames(self, no_games):
        return [(x,y,z) for x in ['H','D','A'] for y in ['H','D','A'] for z in ['H','D','A']]
