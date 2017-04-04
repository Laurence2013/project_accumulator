from itertools import count

class ThreeGamesAccumulator():
    def combinationsForThreeGames(self, no_games):
        return [(x,y,z) for x in ['H','D','A'] for y in ['H','D','A'] for z in ['H','D','A']]

    def get_per_outcome(self, combinations):
        count = 1
        comboList = []
        while count <= len(combinations):
            for x in combinations[count - 1]:
                comboList.append([count, x])
            count += 1
        return comboList
