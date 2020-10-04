import ssl
from urllib.request import urlopen
from urllib.request import Request
import re
webpage = urlopen('https://blog.csdn.net/Jason_HSL/article/details/102999194')
text =webpage.read()
print(text)
# m=re.search(b'<a href="([^"]+)".*?>about</a>',text,re.IGNORECASE)
# print(m.group(1))