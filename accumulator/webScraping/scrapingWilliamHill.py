import os
import csv
import re
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator
from urllib.request import urlopen
from bs4 import BeautifulSoup

class ScrapingWilliamHill(GeneralGamesAccumulator):
    file_path = '/home/laurence/Documents/Django_Projects/accumulator01/src/SampleCodes/scrappingTheWeb/tbody_ids.csv'
    span_ids = '/home/laurence/Documents/Django_Projects/accumulator01/src/SampleCodes/scrappingTheWeb/span_ids.csv'
    span_id_lists = []

    def get_tbody_ids(self, url):
        tbody_ids = []
        try:
            html = urlopen(url)
            soup = BeautifulSoup(html.read(), "html5lib")
            games = soup.findAll('tbody')
            for game in games:
                if 'id' in game.attrs:
                    tbody_ids.append(game.attrs['id'])
        except Exception as e:
            print('ExceptionError' + str(e))
            return None
        except AttributeError as e:
            print('AttributeError' + str(e))
            return None
        except TypeError as e:
            print('TypeError' + str(e))
            return None
        return tbody_ids

    def get_span_ids(self, url, span_file_name):
        try:
            csv_file = open(span_file_name)
            csv_open = csv.reader(csv_file)
            html = urlopen(url)
            soup = BeautifulSoup(html.read(), "html5lib")
            for row in csv_open:
                games = soup.find('tbody',{'id':row}).findAll('span',{'id':re.compile('^[0-9]')})
                for game in games:
                    if 'id' in game.attrs:
                        self.span_id_lists.append(game.get_text().strip())
        except Exception as e:
            print('ExceptionError' + str(e))
            return None
        except AttributeError as e:
            print('AttributeError' + str(e))
            return None
        finally:
            csv_file.close()

    def get_all_odds_for_match(self, url, tbody_link):
        match_odds = []
        try:
            html = urlopen(url)
            csv_file = open(tbody_link)
            csv_open = csv.reader(csv_file)
            soup = BeautifulSoup(html.read(), "html5lib")
            for odds in csv_open:
                for tbody in soup.find('tbody',{'id':odds}).findAll('div',{'class':'eventprice'}):
                    match_odds.append(tbody.get_text().strip())
            new_match_odds = list(self.break_list_into_equal_chunks(match_odds, 3))
        except Exception as e:
            print('ExceptionError' + str(e))
            return None
        except AttributeError as e:
            print('AttributeError' + str(e))
            return None
        finally:
            csv_file.close()
        return new_match_odds

    # def get_all_odds_for_match_copy(self, url, tbody_link):
    #     match_odds = []
    #     try:
    #         html = urlopen(url)
    #         csv_file = open(tbody_link)
    #         csv_open = csv.reader(csv_file)
    #         soup = BeautifulSoup(html.read(), "html5lib")
    #         for odds in csv_open:
    #             for tbody in soup.find('tbody',{'id':odds}).findAll('div',{'class':'eventprice'}):
    #                 match_odds.append(tbody.get_text().strip())
    #         new_match_odds = list(self.break_list_into_equal_chunks(match_odds, 3))
    #     except Exception as e:
    #         print('ExceptionError' + str(e))
    #         return None
    #     except AttributeError as e:
    #         print('AttributeError' + str(e))
    #         return None
    #     finally:
    #         csv_file.close()
    #     return new_match_odds

    # def get_name_of_teams(self, span_id_link, span_id_name):
    #     team_names = []
    #     try:
    #         html = urlopen(span_id_link)
    #         csv_file = open(span_id_name)
    #         csv_open = csv.reader(csv_file)
    #         soup = BeautifulSoup(html.read(), "html5lib")
    #         for span_tag_name in csv_open:
    #             team_names.append(soup.find('span',{'id':span_tag_name}).get_text())
    #     except Exception as e:
    #         print('ExceptionError' + str(e))
    #         return None
    #     except AttributeError as e:
    #         print('AttributeError' + str(e))
    #         return None
    #     except TypeError as e:
    #         print('TypeError' + str(e))
    #         return None
    #     finally:
    #         csv_file.close()
    #     return team_names

    def clear_list(self):
        self.span_id_lists.clear()


    def save_file(self, path_name, docs):
        csvFile = open(path_name, 'w+')
        try:
            writer = csv.writer(csvFile)
            for doc in docs:
                writer.writerow([doc])
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
            csvFile.close()

    # def open_csv_file(self, url, path_name):
    #     csv_file = open(path_name)
    #     csv_open = csv.reader(csv_file)
    #     for row in csv_open:
    #         try:
    #             self.get_span_ids(url, row)
    #         except Exception as e:
    #             print('ExceptionError' + str(e))
    #             return None
    #         except AttributeError as e:
    #             print('AttributeError' + str(e))
    #             return None
    #         except TypeError as e:
    #             print('TypeError' + str(e))
    #             return None
    #     csv_file.close()
