from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
  print(name.get_text())
# print(bs)
# print(type(nameList))
nameList = bs.find_all(text='the prince')
for name in nameList:
  print(name)