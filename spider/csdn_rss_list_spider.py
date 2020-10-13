from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib.error import HTTPError
from urllib.error import URLError


def getUrls(articleUrl):
    urls = []
    try:
        html = urlopen(articleUrl)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(html, 'lxml')
        # with open('rss.xml', 'w+')as fd:
        #     fd.write(str(bs))
        # print(bs.title)
        for article in bs.findAll('a', text='原文链接'):
            if 'href' in article.attrs:
                url = article['href']
                urls.append(url)
                print(url)
        return urls
    except Exception as e:
        print(e)
        return None


def getArticles(urls):
    for url in urls:
        getArticle(url)


def getArticle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(html, 'html.parser')
    except Exception as e:
        print(e)
        return None
    for sibling in bs.find_all('article'):
        fd=open('sp.html',"a+")
        fd.write(str(sibling))
        fd.close()
# https://blog.csdn.net/adlatereturn/article/details/109037551
urls = getUrls('https://blog.csdn.net/adlatereturn/rss/list')
if urls:
    getArticles(urls)
