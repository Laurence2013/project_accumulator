class ThreeMatchAccumulator():
    def combinationsForThreeGames(self, no_games):
        if no_games is 3:
            combos = [(x,y,z) for x in ['H','D','A'] for y in ['H','D','A'] for z in ['H','D','A']]
        return combos
