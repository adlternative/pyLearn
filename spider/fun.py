import urllib

from bs4 import BeautifulSoup


def get_content(url):
    resp = urllib.request.urlopen(url)
    html = resp.read()
    bs = BeautifulSoup(html, "html.parser")
    return bs.textarea

s=get_content("file:///home/adl/%E6%A1%8C%E9%9D%A2/pyLearn/spider/fun.html")
print(s)