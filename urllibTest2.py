#~ coding=utf-8
#~ 使用Pyton内建模块 urllib 请求一个 URL 代码示例
import ssl
 
from urllib.request import Request
from urllib.request import urlopen
 
#使用ssl创建未经验证的上下文，在urlopen中传入上下文参数
context = ssl._create_unverified_context()
 
#~ HTTP请求
request = Request(url = 'https://me.csdn.net/adlatereturn',
				  method = 'GET',
				  headers = {'Host':'me.csdn.net'},
				  data = None)
			
#~ HTTP响应
response = urlopen(request, context=context)
headers = response.info()#响应头
content = response.read().decode('utf-8')#响应体
code = response.getcode()#状态码
 
print('headers='+str(headers)+'\n\n')
print('content='+str(content)+'\n\n')
print('code='+str(code)+'\n')