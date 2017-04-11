import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

class AccumulatorScraping():
    file_path = '/home/laurence/Documents/Django_Projects/accumulator01/src/SampleCodes/scrappingTheWeb/tbody_ids.csv'
    span_ids = '/home/laurence/Documents/Django_Projects/accumulator01/src/SampleCodes/scrappingTheWeb/span_ids.csv'
    span_id_lists = []

    def get_tbody_ids(self, url):
        tbody_ids = []
        try:
            html = urlopen(url)
        except Exception as e:
            return None
        try:
            soup = BeautifulSoup(html.read(), "html5lib")
            games = soup.findAll('tbody')
            for game in games:
                if 'id' in game.attrs:
                    tbody_ids.append(game.attrs['id'])
        except AttributeError as e:
            return None
        return tbody_ids

    def get_span_ids(self, url, tag_name):
        try:
            html = urlopen(url)
        except Exception as e:
            return None
        try:
            soup = BeautifulSoup(html.read(), "html5lib")
            games = soup.find('tbody',{'id':tag_name}).findAll('td')[2].findAll('span')
            for game in games:
                if 'id' in game.attrs:
                    self.span_id_lists.append(game.attrs['id'])
        except Exception as e:
            return None

    def open_csv_file(self, path_name):
        url = 'http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/1/Football.html'
        csv_file = open(path_name)
        csv_open = csv.reader(csv_file)
        for row in csv_open:
            self.get_span_ids(url, row)
        else:
            return True

    def save_file(self, path_name, docs):
        csvFile = open(path_name, 'w+')
        try:
            writer = csv.writer(csvFile)
            for doc in docs:
                writer.writerow([doc])
        finally:
            csvFile.close()

accumulator = AccumulatorScraping()
get_tbody_ids = accumulator.get_tbody_ids('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/1/Football.html')

if os.path.getsize(accumulator.file_path) is 0:
    file_output = accumulator.save_file(accumulator.file_path, get_tbody_ids)
else:
     open_csv_file = accumulator.open_csv_file(accumulator.file_path)
     if open_csv_file is True:
         save_files = accumulator.save_file(accumulator.span_ids, accumulator.span_id_lists)


# csv_list = accumulator.get_span_ids('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html','ip_mkt_grp_tbl_21075_9d8a08d4b13c912153e27659829a27ad')
# get_span_ids = accumulator.get_span_ids('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html')
#
# if csv_list is None:
#     print('Empty file!')
# else:
#     for cf in csv_list:
#         print(cf)
