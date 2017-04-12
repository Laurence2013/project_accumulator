import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

class ScrapingWilliamHill():
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

    def get_span_ids(self, url, tag_name):
        try:
            html = urlopen(url)
            soup = BeautifulSoup(html.read(), "html5lib")
            games = soup.find('tbody',{'id':tag_name}).findAll('td')[2].findAll('span')
            for game in games:
                if 'id' in game.attrs:
                    self.span_id_lists.append(game.attrs['id'])
        except Exception as e:
            return None
        except AttributeError as e:
            return None

    def get_name_of_teams(self, span_id_link, span_id_name):
        team_names = []
        try:
            html = urlopen(span_id_link)
            csv_file = open(span_id_name)
            csv_open = csv.reader(csv_file)
            soup = BeautifulSoup(html.read(), "html5lib")
            for span_tag_name in csv_open:
                team_names.append(soup.find('span',{'id':span_tag_name}).get_text())
        except Exception as e:
            print('ExceptionError' + str(e))
            return None
        except AttributeError as e:
            print('AttributeError' + str(e))
            return None
        except TypeError as e:
            print('TypeError' + str(e))
            return None
        return team_names

    def clear_list(self):
        self.span_id_lists.clear()

    def open_csv_file(self, url, path_name):
        csv_file = open(path_name)
        csv_open = csv.reader(csv_file)
        for row in csv_open:
            try:
                self.get_span_ids(url, row)
            except Exception as e:
                print('ExceptionError' + str(e))
                return None
            except AttributeError as e:
                print('AttributeError' + str(e))
                return None
            except TypeError as e:
                print('TypeError' + str(e))
                return None
        else:
            return True

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
