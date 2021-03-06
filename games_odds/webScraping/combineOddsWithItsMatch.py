import csv
from accumulator.models import Game, Odd

class CombineOddsWithItsMatch():
    def get_match(self, file_to_open):
        match_list = list()
        try:
            with open(file_to_open) as f:
                for line in f:
                    match_list.append(line.strip())
        except Exception as e:
            print('ExceptionError ' + str(e))
            return None
        except AttributeError as e:
            print('AttributeError ' + str(e))
            return None
        except TypeError as e:
            print('TypeError ' + str(e))
            return None
        return match_list

    def combine_odds_match(self, match_list, odds_list):
        try:
            return [combinations for combinations in zip(match_list, odds_list)]
        except NameError as e:
            print('NameError ' + str(e))
            return None
