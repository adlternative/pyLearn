from urllib.request import urlopen
from html.parser import HTMLParser

# def isjob(url):
# 		try:
# 		# print(url.split('/'))
# 			a, b, c, d = url.split('/')
# 		except ValueError:
# 			return False

# def isjob(url):
# 		try:
# 		# print(url.split('/'))
# 			a, b, c, d = url.split('/')
# 		except ValueError:
# 			return False
# 		return a == d == '' and b == 'jobs' and c.isdigit()
# #  /jobs/324/ 

class Scraper(HTMLParser):
		in_link = False
		def handle_starttag(self,tag,attrs):

			attrs=dict(attrs)
			# if tag == 'a':
				# print(attrs)
			url=attrs.get('href','')
			if tag == 'a' :#and isjob(url)
					self.url =url
					self.in_link =True
					self.chunks=[]
		def handle_data(self,data):
			if self.in_link:
				self.chunks.append(data)
		def handle_endtag(self,tag):
			if tag =='a' and self.in_link:
				print('{}({})'.format(''.join(self.chunks),self.url))
				self.in_link=False 
		return a == d == '' and b == 'jobs' and c.isdigit()
#  /jobs/324/ 

class Scraper(HTMLParser):
		in_link = False
		def handle_starttag(self,tag,attrs):

			attrs=dict(attrs)
			# if tag == 'a':
				# print(attrs)
			url=attrs.get('href','')
			if tag == 'a' :#and isjob(url)
					self.url =url
					self.in_link =True
					self.chunks=[]
		def handle_data(self,data):
			if self.in_link:
				self.chunks.append(data)
		def handle_endtag(self,tag):
			if tag =='a' and self.in_link:
				print('{}({})'.format(''.join(self.chunks),self.url))
				self.in_link=False 
text= urlopen('https://blog.csdn.net/qq_33564134/article/details/89297840?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160147525619724848356547%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160147525619724848356547&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v3~pc_rank_v2-6-89297840.first_rank_ecpm_v3_pc_rank_v2&utm_term=%E7%88%ACCSDN%E5%8D%9A%E5%AE%A2&spm=1018.2118.3001.4187').read().decode()
print(text)
# parser=Scraper()
# parser.feed(text)
# parser.close()