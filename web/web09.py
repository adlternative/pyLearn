from urllib.request import urlopen
from bs4 import BeautifulSoup
text = urlopen("https://blog.csdn.net/adlatereturn/article/details/108046579").read().decode()
# with open('f.txt','w') as fd:
# 	fd.write(str(text))
# print(text)
soup = BeautifulSoup(text,'html.parser')
jobs =set()
print(soup.body.main.div.article.div.div)
# exit(0)

# for job in soup.body.main.div.article.div.div:
	# jobs.add('{}'.format(job.p.string)
	# print(job)
# print('\n'.join(sorted(jobs,key=str.lower)))