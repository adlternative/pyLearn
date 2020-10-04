import requests
url = "https://blog.csdn.net/TYUT_xiaoming/article/details/99771116"
res = requests.get(url)
res.encoding = res.apparent_encoding
# res.encoding="gbk"
html = res.text

print(html)
