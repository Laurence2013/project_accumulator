import csv
import re
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

    def convert_string_into_float_or_string(self, odds):
        test_list = list()
        for odd in odds:
            int_num = re.sub(r'(\d+)/(\d+)', lambda m: str(int(m.group(1))/int(m.group(2))), odd)
            found = re.findall("'(.+?)'", int_num)
            for f in found:
                if f == str('EVS'):
                    test_list.append(round(float(2.00),2))
                else:
                    test_list.append(round(float(f),2))
        return test_list

    def create_new_list(self, odds):
        test_list = list()
        for odd in odds:
            test_list.append(self.convert_string_into_float_or_string(odd))
        return test_list
