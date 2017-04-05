class GeneralGamesAccumulator():
    def get_per_outcome(self, combinations):
        count = 1
        comboList = []
        while count <= len(combinations):
            for x in combinations[count - 1]:
                comboList.append([count, x])
            count += 1
        return comboList

    def get_game_combinations(self, combos, games):
        gameList = []
        for c in range(len(combos)):
            for g in games:
                gameList.append([g])
        return gameList

    def combine_combo_list_with_game_list(self, matchList, gameList, match_len, game_len):
        merge_combo_matches = []
        count = 1
        if match_len == game_len:
            while count <= match_len:
                merge_combo_matches.append(tuple(gameList[count - 1] + matchList[count - 1]))
                count += 1
        else:
            return False
        return merge_combo_matches
