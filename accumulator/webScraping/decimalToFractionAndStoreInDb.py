import csv
from fractions import Fraction

class DecimalToFractionAndStoreInDb():
    def convert_fraction_to_decimal(self, file_to_open):
        odds_list = []
        try:
            csv_file = open(file_to_open)
            csv_open = csv.reader(csv_file)
            for odds in csv_open:
                odds_list.append(odds)
        except Exception as e:
            print('ExceptionError' + str(e))
            return None
        except AttributeError as e:
            print('AttributeError' + str(e))
            return None
        except TypeError as e:
            print('TypeError' + str(e))
            return None
        finally:
            csv_file.close()
        return odds_list

    def open_matches_file(self, file_to_open):
        pass
