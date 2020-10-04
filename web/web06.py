# from subprocess import Popen, PIPE

# text = open('messy.html').read()

# tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)

# tidy.stdin.write(text.encode())
# tidy.stdin.close()
# print(tidy.stdout.read().decode())
from tidylib	import tidy_document
# import requests
# from lxml import etree
# with open("messy.html") as f:
fd=open("messy.html")
document,error =tidy_document(fd.read())

