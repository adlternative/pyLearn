from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://blog.csdn.net/adlatereturn/article/details/108732422')
bs = BeautifulSoup(html, 'html.parser')
# for child in bs.find('table',{'id':'giftList'}).children:#descendants
#   print(child)

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# for sibling in bs.find('article', {'class':'baidu_pl'}).children:
#   print(sibling)
for sibling in bs.find_all('article'):
  print(sibling.get_text())
