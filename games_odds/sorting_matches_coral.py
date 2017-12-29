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
