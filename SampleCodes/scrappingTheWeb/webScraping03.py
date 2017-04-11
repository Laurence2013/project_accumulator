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
        # for child in bsObj.find('table', {'id':'giftList'}).findAll('tr', {'class':'gift'}):
        for child in bsObj.find('table',{'id':'giftList'}).descendants:
            print(child)
    except AttributeError as e:
        return None

def getTitle_0(url):
    try:
        html = urlopen(url)
    except Exception as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        # for child in bsObj.find('table', {'id':'giftList'}).findAll('tr', {'class':'gift'}):
        for child in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
            print(child)
    except AttributeError as e:
        return None

def getTitle_1(url):
    try:
        html = urlopen(url)
    except Exception as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        # for child in bsObj.find('table', {'id':'giftList'}).findAll('tr', {'class':'gift'}):
        # for child in bsObj.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text():
        #     print(child)
        get_parent = bsObj.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
    except AttributeError as e:
        return None
    return get_parent

get_parent = getTitle_1('http://www.pythonscraping.com/pages/page3.html')
print(get_parent)
