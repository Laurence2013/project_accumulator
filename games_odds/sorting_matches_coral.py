from games_odds.coral_base import Coral_Base

class SortingMatchesInCoral(Coral_Base):
    def sorting_each_games_data(self, todays_matches_list):
        test_list = list()
        test_list2 = list()
        for match in range(0, len(todays_matches_list)):
            test_list.append(todays_matches_list[match].split())

        list2 = filter(None, test_list)
        for l2 in list2:
            test_list2.append(l2)

        for test2 in range(0, len(test_list2)):
            test_list2[test2].pop(0)
            test_list2[test2].pop(0)
            test_list2[test2].pop(0)
            del test_list2[test2][-1]
        return test_list2

    def seperating_odds(self, get_odds):
        get_odds_list = list()

        for eachOdds in range(0, len(get_odds)):
            get_odds_list.append(get_odds[eachOdds][-3:])
        return get_odds_list

    def seperating_games(self, get_games):
        for eachGames in range(0, len(get_games)):
            get_games[eachGames].pop(-3)
            get_games[eachGames].pop(-2)
            get_games[eachGames].pop(-1)
        return get_games

    # def seperating_games(self, get_games):
    #     games_list = list()
    #     for eachGames in range(0, len(get_games)):
    #         games_list.append(get_games[eachGames][-3:])
    #     return games_list
