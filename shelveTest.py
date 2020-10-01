import shelve
s= shelve.open('a.data')
# s['x']=['a','b','c']
# temp =s['x']
# temp.append('d')
# s['x']=temp
print(s['x'])
# s['x']=['a','b','c']
# s['x'].append('d')
