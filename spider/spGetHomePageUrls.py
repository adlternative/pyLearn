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


lastTime = ''
# 新文章列表
newArticleList = []
# newArticleList.sort()
# 获取初始html
bs = getNewArticleFromHome(True, "https://blog.csdn.net/weixin_43574962")
if bs:
    articleCount = bs.find('span', {'class': 'count'})
    if articleCount:
        articleCount = int(articleCount.get_text())
    pageSize = articleCount // 40
    if pageSize == 0:
        articles = bs.findAll('div', {'class': 'article-item-box csdn-tracking-statistics'})
        for i, article in enumerate(articles):
            # print(i,article)
            title_original_href = article.find('a')
            original = title_original_href.find('span')
            if original:
                original = original.get_text()
            title = title_original_href.get_text()

            href = title_original_href['href']
            # print(title,end='')
            # print(href)
            # print(original)
            # original=
            # print(href['href'])   
            settop = article.find('img', {'class': 'settop'})
            if settop:
                settop=True
            else:
                settop=False

            #     print(settop)
            date = article.find('span', {'class': 'date'})
            if date:
                date=date.get_text()
            #     print(date)

            rs_num = article.findAll('span', {'class': 'read-num'})
            read_num = speak_num = '0'
            if rs_num:
                # print("阅读", rs_num[0].get_text())
                read_num = rs_num[0].get_text()
                if len(rs_num) == 2:
                    speak_num = rs_num[1].get_text()
                    # print("评论",rs_num[1].get_text())
            content = article.find('p', {'class': 'content'})
            if content:
                content=content.get_text()
            #     print(content.get_text(),end='')
            #
            index = i

            if settop:
                if lastTime < date:
                      newArticleList.append(
                            ArticleBox(href=href, content=content, date=date, readnum=read_num, speaknum=speak_num,
                               settop=settop, index=index, original=original, title=title))
            else:
                continue
for ii in newArticleList:
    print("=================")
    print(ii.index)
    print(ii.original)
    print(ii.title)
    print(ii.settop)
    print(ii.date)
    print(ii.content)
    print(ii.href)
    print(ii.readnum)
    print(ii.speaknum)
