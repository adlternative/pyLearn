#!usr/bin/python
#coding: utf-8

'''
Created on 2018年5月9日
@author: kaki
使用python爬取csdn个人博客信息
'''

import urllib
import re
import sys
from urllib import request

# from urllib.request import Request
# from urllib.request import urlopen


# 当前的博客列表页号
page_num = 1
# 不是最后列表的一页
notLast = []


account = str(input('print csdn id:'))

# 首页地址
baseUrl = 'http://blog.csdn.net/'+account
# 连接页号，组成爬取的页面网址
myUrl = baseUrl+'/article/list/'+str(page_num)

# 伪装成浏览器访问，直接访问的话csdn会拒绝
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
# 构造请求
req = request.Request(myUrl, headers=headers)

# 访问页面
myResponse = request.urlopen(req)
myPage = myResponse.read()
type = sys.getfilesystemencoding()
myPage = myPage.decode("UTF-8").encode(type)

# 获取总体信息
# 利用正则表达式来获取博客的标题
title = re.findall('<title>(.*?)</title>', myPage, re.S)
titleList = []
for items in title:
    titleList.append(str(items).lstrip().rstrip())
print('%s %s' % ('标题'.decode('utf8').encode('gbk'), titleList[0]))

# 利用正则表达式来获取博客的数量
num = re.findall('<dd><span class="count">(.*?)</span></dd>', myPage, re.S)
numList = []
for items in num:
    numList.append(str(items).lstrip().rstrip())

# 利用正则表达式来获取粉丝的数量
fan = re.findall(
    '<dd id=\'fan\'><span class="count">(.*?)</span></dd>', myPage, re.S)
fanList = []
for items in fan:
    fanList.append(str(items).lstrip().rstrip())

# 输出原创、粉丝、喜欢、评论数
print( '%s %s %s %s %s %s %s %s' % ('原创'.decode('utf8').encode('gbk'), numList[0], '粉丝'.decode('utf8').encode('gbk'), fanList[0], '喜欢'.decode('utf8').encode('gbk'), numList[1], '评论'.decode('utf8').encode('gbk'), numList[2]))

# 利用正则表达式来获取访问量
fangwen = re.findall('<dd title="(.*?)">', myPage, re.S)
fangwenList = []
for items in fangwen:
    fangwenList.append(str(items).lstrip().rstrip())

# 利用正则表达式来获取排名
paiming = re.findall('<dl title="(.*?)">', myPage, re.S)
paimingList = []
for items in paiming:
    paimingList.append(str(items).lstrip().rstrip())

# 输出总访问量、积分、排名
print ('%s %s %s %s %s %s' % ('总访问量'.decode('utf8').encode('gbk'), fangwenList[0], '积分'.decode('utf8').encode('gbk'), fangwenList[1], '排名'.decode('utf8').encode('gbk'), paimingList[0]))


# 获取每一页的信息
while not notLast:

    # 首页地址
    baseUrl = 'http://blog.csdn.net/'+account
    # 连接页号，组成爬取的页面网址
    myUrl = baseUrl+'/article/list/'+str(page_num)

    # 伪装成浏览器访问，直接访问的话csdn会拒绝
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    # 构造请求
    req = request.Request(myUrl, headers=headers)

    # 访问页面
    myResponse = request.urlopen(req)
    myPage = myResponse.read()
    type = sys.getfilesystemencoding()
    myPage = myPage.decode("UTF-8").encode(type)

    # 在页面中查找最后一页，这里我用了我博客的最后一页的一个标签
    notLast = re.findall('android.media.projection', myPage, re.S)

    print ('-----------------------------the %d page---------------------------------' % (page_num,))

    # 利用正则表达式来获取博客的标题
    title = re.findall(
        '<span class="article-type type-1">(.*?)</a>', myPage, re.S)

    titleList = []
    for items in title:
        titleList.append(str(items)[32:].lstrip().rstrip())

    # 利用正则表达式获取博客的访问量
    view = re.findall('<span class="read-num">(.*?)</span>', myPage, re.S)

    viewList = []
    for items in view:
        viewList.append(str(items).lstrip().rstrip())

    # 将结果输出
    for n in range(len(titleList)):
        print( '%s %s %s' % (viewList[n*2-2], viewList[n*2-1], titleList[n]))

    # 页号加1
    page_num = page_num + fushang
