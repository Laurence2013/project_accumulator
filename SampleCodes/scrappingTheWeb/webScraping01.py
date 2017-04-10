from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except Exception as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        nameList = bsObj.findAll("span", {"class":"green"})
    except AttributeError as e:
        return None
    return nameList

nameList = getTitle('http://www.pythonscraping.com/pages/warandpeace.html')
if nameList is None:
    print('Title could not be found')
else:
    for name in nameList:
        print(name.get_text())
