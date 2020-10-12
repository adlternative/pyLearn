from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import os
import sys
# 'http://pythonscraping.com/pages/page1.html'


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        # print(e)
        return None
    except URLError as e:
        # print(e)
        # print('the server could not found!')
        return None

    try:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


if __name__ == '__main__':
    title = getTitle('http://pythonscraping.com/pages/page1.html')
    if title == None:
        print('title could not be found')
    else:
        print(title)

    # html = urlopen('http://pythonscraping.com/pages/page1.html')
    # try:
    #     content = html.read().decode()
    # except AttributeError:
    #     sys.exit()
    # else:
    #     with open('a.txt',"w+")as fd:
    #       fd.write(content)

    # try :
    #   bs = BeautifulSoup(None, 'html.parser')
    # except Exception as E:
        # print(type(E))
