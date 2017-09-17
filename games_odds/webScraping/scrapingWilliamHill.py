import os
import csv
import re
from accumulator.combinations.generalGamesAccumulator import GeneralGamesAccumulator
from urllib.request import urlopen
from bs4 import BeautifulSoup

class ScrapingWilliamHill(GeneralGamesAccumulator):
    span_id_lists = []

    def get_daily_matches_dates(self, url):
        get_daily_matches_dates = list()
        try:
            html = urlopen(url)
            soup = BeautifulSoup(html.read(), "html5lib")
            games = soup.find('div',{'class':'paginationDailyMatches'}).findAll('span')[:7]
            for game in games:
                get_daily_matches_dates.append(game.get_text())
        except Exception as e:
            print('ExceptionError' + str(e))
            return None
        return get_daily_matches_dates

    def get_file_size(self, file_size):
        try:
            size = os.path.getsize(file_size)
        except Exception as e:
            print('ExceptionError' + str(e))
            return None
        return size

    def empty_files(self, files):
        try:
            for empty_files in files:
                open(empty_files, 'w').close()
        except Exception as e:
            print('ExceptionError' + str(e))
            return None
        return True

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
