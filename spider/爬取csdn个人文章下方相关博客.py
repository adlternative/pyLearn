from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
from collections import deque

random.seed(datetime.datetime.now())

pages = set()
bfsQue = deque()


# 'https://blog.csdn.net/adlatereturn/article/details/108889759'
# 打印下方所有博客
def printLinks(articleUrl):
    html = urlopen(articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find('div', {'class', 'recommend-box insert-baidu-box'}).find_all('a', href=re.compile(
            r'^https://blog\.csdn\.net/.+?/article/details/.+$')):
        # print(link)
        if 'href' in link.attrs:
            print(link.attrs['href'])


# 从第一个博客开始继续遍历第一个博客，直到找到相同文章（其实可以不用），形同dfs
def getLinksTravelDfs(articleUrl):
    global pages
    html = urlopen(articleUrl)
    # html = urlopen('http://https://blog.csdn.net/{}'.format(article))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find('div', {'class', 'recommend-box insert-baidu-box'}).find_all('a', href=re.compile(
            r'^https://blog\.csdn\.net/.+?/article/details/.+$')):
        # print(link)
        if 'href' in link.attrs:
            newPage = link.attrs['href']
            if newPage not in pages:
                print(newPage)
                pages.add(newPage)
                getLinksTravelDfs(newPage)
            else:
                print('well , i find a multiple page:{}! !', newPage)
                exit(1)


def getLinksTravelBfs(articleUrl):
    global pages
    global bfsQue
    bfsQue.append(articleUrl)
    curUrl = articleUrl
    print('the begin page is %s ' % curUrl)
    while (len(bfsQue)!=0):
        curUrl = bfsQue[0]
        html = urlopen(curUrl)
        bs = BeautifulSoup(html, 'html.parser')
        for link in bs.find('div', {'class', 'recommend-box insert-baidu-box'}).find_all('a', href=re.compile(
                r'^https://blog\.csdn\.net/.+?/article/details/.+$')):
            if 'href' in link.attrs:
                newPage = link.attrs['href']
                if (newPage not in pages) and (newPage not in bfsQue):
                    print('newPage is {}'.format(newPage))
                    bfsQue.append(newPage)  # 将每次几个新的url加入到队列
        outPage = bfsQue.popleft()
        print('the %s has been travel'%outPage)
        pages.add(outPage)


# 获得所有
def getLinks(articleUrl):
    html = urlopen(articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'class', 'recommend-box insert-baidu-box'}).find_all('a', href=re.compile(
        r'^https://blog\.csdn\.net/.+?/article/details/.+$'))


def getLinksTravelRandom():
    dep = 6
    while dep and (len(links) > 0):
        dep -= 1
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)


def listTest():
    l = [1, 2, 3, 4]
    l.pop()
    print(l)


if __name__ == '__main__':
    # links = getLinkRandom('https://blog.csdn.net/dixianjing9181/article/details/102010844')
    # listTest()
    # startUrl = 'https://blog.csdn.net/adlatereturn/article/details/106845518'
    # pages.add(startUrl)
    # getLinksTravelDfs(startUrl)

    getLinksTravelBfs('https://blog.csdn.net/adlatereturn/article/details/106845518')
