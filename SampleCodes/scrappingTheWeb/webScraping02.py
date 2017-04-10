from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getTitle(url):
    try:
        html = urlopen(url)
    except Exception as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        # gamesList = bsObj.findAll('table', {'class':'tableData'}).find('tbody').find('tr').find('td').find('a').find('span')
        # gameList = bsObj.find('table', {'class': 'tableData'}).tbody.find('tr', {'class':'rowOdd'}).td
        for games in bsObj.find('table', {'class': 'tableData'}).tbody.find('tr', {'class':'rowOdd'}).findAll('td')[2].a:
            print(games.get_text())
    except AttributeError as e:
        return None
    return games

getTitle('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/Football.html')
