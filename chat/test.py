# s={1:"asd",2:"#"}
# s[1]='ad'
# if 1 in s:
#   print(s[1])
# s=['ads','asd']
# p="*".join(s)
# print(p)
dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索','func':None}

print ("Value : %s" %  dict.setdefault('func', "?"))
print ("Value : %s" %  dict.setdefault('runoob', "?"))
print ("Value : %s" %  dict.setdefault('runoob', None))
print ("Value : %s" %  dict.setdefault('Taobao', '淘宝'))

childen ={}
s=[]
s.append(1)
print(s)
childen.setdefault(1,[]).append(1)
childen.setdefault(2,[]).append(1)
print(childen)

print('<p><a href ={id}{subject}></a></p>'.format_map({'id': 3, 'reply_to': None, 'sender': 'adl', 'subject': '闲聊', 'text': '你是谁'}))