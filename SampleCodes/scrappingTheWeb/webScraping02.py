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
        games = bsObj.find('table', {'class': 'tableData'}).tbody.tr.findAll('td')[2].a
        # for games in bsObj.find('table', {'class': 'tableData'}).tbody.find('tr', {'class':'rowOdd'}).findAll('td')[2].a:
        #     print(games.get_text())
    except AttributeError as e:
        return None
    return games

def getTitle_0(url):
    myGames = []
    try:
        html = urlopen(url)
    except Exception as e:
        return None
    try:
        soup = BeautifulSoup(html.read(), 'html.parser')
        # games = bsObj.find('table',{'class':'tableData'}).findAll('tr',{'class':'rowOdd'})
        # for game in bsObj.find('tbody',{'id':'ip_mkt_grp_tbl_21075_9d8a08d4b13c912153e27659829a27ad'}):
        #     print(game)
            # myGames.append(game.get_text())
        # for game in soup.find('tr',{'id':'ip_row_10895386'}).findAll('td')[2].span:
        #     print(game)
        #
        # for home in soup.find('div',{'id':'ip_selection1516167620price'}):
        #     print(home)
        # for game in soup.find('tr',{'id':'ip_row_10895386'}).find('span',{'id':'10895386_mkt_namespace'}):
        #     myGames.append(game)
        # ''' Use this to print out all of the IDs '''
        # for links in soup.findAll('tbody'):
        #     if 'id' in links.attrs:
        #         print(links.attrs['id'])
        for links in soup.find('tbody',{'id':'ip_mkt_grp_tbl_21075_9d8a08d4b13c912153e27659829a27ad'}).findAll('td'):
            if 'class' in links.attrs:
                print(links.attrs['class'])
    except AttributeError as e:
        return None
    # return myGames


# games = getTitle('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/Football.html')
games = getTitle_0('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html')
# print(games[0])





#
# for game in games:
#     print(game.get_text())
