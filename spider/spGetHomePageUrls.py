from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import configparser
import os, sys
import re


def getNewArticleFromHome(writeTofile, url):
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
        if not bs:
            print("BeautifulSoup==None")
            return None
        if writeTofile:
            fd2 = open('home.txt', "w+")
            fd2.write(str(bs))
            fd2.close()
    except Exception as e:
        print(e)
        return None
    return bs


class ArticleBox:
    def __init__(self, href, content, date, readnum, speaknum, settop, index, original, title):
        self.href = href
        self.content = content
        self.date = date
        self.readnum = readnum
        self.speaknum = speaknum
        self.settop = settop
        self.index = index
        self.original = original
        self.title = title


lastTime = '2019-10-06 12:40:35'
# 新文章列表
newArticleList = []


# 10 9 8 7 6 5 4 3 找新文章ｉ,已知lastTime="2019-03-14 15:48:37"
# begin,end 均为index
def articleBsearch(articles, begin, end, lasttime):
    # print(begin)
    # print(end)
    if begin > end:
        return end
    i = (begin + end) // 2  # 17 25 29

    date = articles[i].find('span', {'class': 'date'})
    # if i ==27:
    #     print(date)
    if date:
        date = date.get_text()
    if lasttime > date:
        return articleBsearch(articles, begin, i - 1, lasttime)
    if lasttime < date:
        return articleBsearch(articles, i + 1, end, lasttime)
    else:
        return i


def getAllFromArticle(article):
    title_original_href = article.find('a')

    # 判断是否原创
    original = title_original_href.find('span')
    if original:
        original = original.get_text()

    # 获取标题
    title = list(title_original_href.stripped_strings)[1]

    # 获取url
    href = title_original_href['href']

    # 是否置顶
    settop = article.find('img', {'class': 'settop'})
    if settop:
        settop = True
    else:
        settop = False

    # 获得日期
    date = article.find('span', {'class': 'date'})
    if date:
        date = date.get_text()

    # 获得阅读数量+评论数量
    rs_num = article.findAll('span', {'class': 'read-num'})
    read_num = speak_num = '0'
    if rs_num:
        read_num = rs_num[0].get_text()
        if len(rs_num) == 2:
            speak_num = rs_num[1].get_text()

    # 获得评论数量
    content = article.find('p', {'class': 'content'})
    if content:
        content = list(content.stripped_strings)[0]

    return (href, content, date, read_num, speak_num, settop, original, title)


# 获取初始html
# https://blog.csdn.net/weixin_43574962
# https://blog.csdn.net/lyn631579741
homeUrl = "https://blog.csdn.net/lyn631579741"
bs = getNewArticleFromHome(False, homeUrl)
if bs:
    articleCount = bs.find('li', {'class': 'active margin'})
    if articleCount:
        articleCount = int(articleCount['data-type'])
    if not articleCount:
        exit(0)
    pageSize = articleCount // 40 + 1
    if articleCount % 40 == 0:
        pageSize -= 1

    if pageSize == 1:
        articles = list(bs.findAll('div', {'class': 'article-item-box csdn-tracking-statistics'}))

    else:
        h = homeUrl + '/article/list/' + '1'
        bs = getNewArticleFromHome(False,h)
        articles = bs.findAll('div', {'class': 'article-item-box csdn-tracking-statistics'})
        articles = list(articles)

        for page in range(2,pageSize+1):
            h = homeUrl + '/article/list/' + str(page)
            bs = getNewArticleFromHome(False, h)
            anotherArticles=bs.findAll('div', {'class': 'article-item-box csdn-tracking-statistics'})
            articles.extend(anotherArticles)
    beginIndex = 0
    endIndex = 0
    for i, article in enumerate(articles):
        # 确定其是第几个
        index = i
        href, content, date, readnum, speaknum, settop, original, title = getAllFromArticle(articles[i])
        # 如果置顶
        if settop:
            # 如果其是新文章
            if lastTime <= date:
                # 加入到新文章链表
                newArticleList.append(
                    ArticleBox(href=href, content=content, date=date, readnum=readnum, speaknum=speaknum,
                               settop=settop, index=index, original=original, title=title))
        else:
            # 这是第一个非置顶位置　
            beginIndex = index  # 2
            endIndex = articleCount  # 33
            break

    t = articleBsearch(articles, beginIndex, endIndex - 1, lastTime)
    for i in range(beginIndex, t + 1):
        index = i
        href, content, date, readnum, speaknum, settop, original, title = getAllFromArticle(articles[i])
        newArticleList.append(
            ArticleBox(href=href, content=content, date=date, readnum=readnum, speaknum=speaknum,
                       settop=settop, index=index, original=original, title=title))

# 打印下新的newArticleListfor art in
newArticleList.sort(key=lambda art: art.date)
for ii in newArticleList:
    print("=================")
    # print("index",ii.index)
    print("创作形式:", ii.original)
    print("标题:", ii.title)
    print("是否置顶:", ii.settop)
    print("日期:", ii.date)
    print("内容:", ii.content)
    print("url:", ii.href)
    print("阅读数量:", ii.readnum)
    print("评论数量:", ii.speaknum)
