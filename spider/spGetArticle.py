from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib.error import HTTPError
from urllib.error import URLError
import configparser
import os, sys


class spider:
    def __init__(self, cfg, url, fd=sys.stdout):
        self.cfg = cfg
        self.url = url
        self.fd = fd

    def bsStart(self, writeTofile):
        try:
            html = urlopen(self.url)
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
            self.bs = bs
            if writeTofile:
                fd2 = open('tt.txt', "w+")
                fd2.write(str(bs))
                fd2.close()
        except Exception as e:
            print(e)
            return None

    def getBloger(self):
        # print("作者:", bloger.get_text())
        return self.bs.find('span', {'class': 'name '})or self.bs.find('span', {'class': 'name vip-name'})

    def printBloger(self):
        bloger = self.getBloger()
        if bloger:
            name =bloger.get_text()
            self.fd.write("<div class='name 'username='{}'>博主:{}</div><br>\n".format(name,name))
    def getTime(self):
        return self.bs.find('span', {"class": "time"})

    def printTime(self):
        time = self.getTime()
        if time:
            self.fd.write("<div class ='time' >时间:{}</div ><br>\n".format(time.get_text()))
    def printUrl(self):
            fd.write("<a href='{}'>原文链接</a><br>\n".format(self.url))

    def getOriginal(self):
        original = self.bs.find('div', {'class': 'creativecommons'})
        if original:
            label = "原创"
        else:
            label = "转发"
        return label

    def printOriginal(self):
        # 是否原创
        label = self.getOriginal()
        self.fd.write("<div class ='original' >{}</div ><br>\n".format(label))

    def getTitle(self):
        return self.bs.find('', {"class": "title-article"})

    def printTitle(self):
        title = self.getTitle()
        if(title):
            self.fd.write(str(title))

    def getArticle(self):
        return self.bs.find_all('article')

    def printArticle(self):
        article = self.getArticle()
        if(article):
            for line in article:
                self.fd.write(str(line))

    def writeTohtml(self):
        for i in self.cfg:
            func = getattr(self, 'print' + i)
            if (func):
                func()
        self.printUrl()


def getBloger(bs):
    # print("作者:", bloger.get_text())
    # return bs.find('p', {'class': 'blog-name'})
    return bs.find('span', {'class': 'name '})


def getTime(bs):
    return bs.find('span', {"class": "time"})


def getOriginal(bs):
    original = bs.find('div', {'class': 'creativecommons'})
    if original:
        label = "原创"
    else:
        label = "转发"
    return label


def getTitle(bs):
    return bs.find('', {"class": "title-article"})


def getArticle(url):
    try:
        fd = open('text.html', "w+")
    except Exception as e:
        print(e)
        fd.close()
        return None

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
        # fd2=open('tt.txt',"w+")
        # fd2.write(str(bs))
        # fd2.close()
    except Exception as e:
        print(e)
        return None
    # 标题
    title = getTitle(bs)
    fd.write(str(title))
    # 文章
    for sibling in bs.find_all('article'):
        fd.write(str(sibling))
    # 作者
    bloger = getBloger(bs)
    fd.write("<div class='name 'username='{}'>博主:{}</div><br>\n".format(bloger.get_text(), bloger.get_text()))
    # 发布时间
    time = getTime(bs)
    fd.write("<div class ='time' >时间:{}</div ><br>\n".format(time.get_text()))
    # 是否原创
    label = getOriginal(bs)
    fd.write("<div class ='original' >{}</div ><br>\n".format(label))
    # 原文链接
    fd.write("<a href='{}'>原文链接</a><br>\n".format(url))
    fd.close()


if __name__ == '__main__':
    cf = configparser.ConfigParser()
    cf.read("./config.ini")
    requests = []
    try:
        URLcfg = cf['URL']
        Requestcfg = cf['REQUESTS']
        # print(cf['REQUESTS'])

    except KeyError as e:
        print("配置文件config.ini中没有:%s" % e)
        exit(-1)

    try:
        if Requestcfg.getboolean('Title'):
            requests.append('Title')
        if Requestcfg.getboolean('Article'):
            requests.append('Article')
        if Requestcfg.getboolean('Bloger'):
            requests.append('Bloger')
        if Requestcfg.getboolean('Original'):
            requests.append('Original')
        if Requestcfg.getboolean('Time'):
            requests.append('Time')

        url = URLcfg.get('Url')
        if not url:
            print("配置文件config.ini中没有url")
            exit(-1)
    except IndentationError as e:
        print(e)
        exit(-1)
    except KeyError as e:
        print("配置文件config.ini中没有:%s" % e)
        exit(-1)
    except ValueError as e:
        print("配置文件config.ini中value配置错误\n%s" % e)
        exit(-1)

    try:
        fd = open("1.html", "w+")
    except Exception as e:
        print(e)
    sp = spider(requests, url, fd)
    sp.bsStart(False)
    sp.writeTohtml()
    fd.close()
    # getArticle('https://blog.csdn.net/qq_41683065/article/details/108702408')

# https://blog.csdn.net/kdongyi/article/details/82343712
# https://blog.csdn.net/junjun5156/article/details/70156286
