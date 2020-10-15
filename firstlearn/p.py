b = ['aa', 'sad']

b[0] = r'sad'
print(b)

m = ['1', '2', '3']
m.append('1')
m.insert(0, 'sa')
del m[0]
p = m.pop(1)
print(p)
m.remove('1')
print(m)
n = ['asd', 'sad', 'sadd']
m = n
print(m is n)
m[1] = 'csda'
print(n)
m = n[:]
m[1] = 'csdn'
print(n)

s = {1: 2, 3: '4'}

for i in s.keys():
    print(i)

def func(dic):
    dic['sad']='sad'

d={}
func(d)
print(d.get('sad'))


def func():
    a=1
    b=2
    c=3
    d=4
    return (a,b,c,d)
q=func()
