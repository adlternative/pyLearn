from copy import deepcopy
template = '''<head><title>{title}</title></head>
<body>
<h1>{title}</h1>
<p>{text}</p>
</body>
 '''
data = {'title': "sad", 'text': "welcome"}

print(template.format_map(data))

d = {}
d['sad'] = 'asd'
d['asd'] = 42
d['asd'] = 42
print(d)
d.clear()
x = {}
x['key'] = 'value'
y = x.copy()
print(y)
x['key'] = 'vale'
del x['key']
# x.clear()
print(y)
p = {'sad': 'sad', 'qwe': ['1', '2', '3']}
q = p.copy()
q['sad'] = 'wqe'
q['qwe'].remove('1')
print(q)
print(p)

d = {}
d['asd'] = ['sad', 'sdad']
c = d.copy()
dc = deepcopy(d)
d['asd'].append('sadd')
print(c)
print(d)
print(dc)
i = 1
print("sad%d" % i)
r = {}
r.fromkeys(['sad', 'sadd'])
print(r)
rr = dict.fromkeys(['sad', 'saddd'], '(now)')
print(rr)
print(rr.get('fda'))

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '213',
        'addr': 'Bar steet 213'
    },
    'Alisce': {
        'phone': '231',
        'addr': 'Bat com 1231'
    },

}

labels = {
    'phone': 'phoneNumber',
    'addr': 'address'
}
# name =input('name: ')
# request =input('Phone number(p) or address(a)')
# key =request
# if(request=='p'):key ='phone'
# if(request=='a'):key ='addr'

# if name in people:
# print("{}'s {} is {}".format(name,labels[key],people[name][key]))

# person =people.get(name,{})

# label =labels.get(key,key)
# result =person.get(key,'not available')
# print("{}'s {} is {}".format(name,label,result))

dd = {'title': 'py web', 'url': 'http://www.py.com', 'spam': 0}
print(dd.items())
print(dd.keys())
print(dd.values())

print(('title', 'py web') in dd.items())
print(list(dd.items()))
dd.pop('title')
dd.popitem()
print(dd.items())
e = {}
e.setdefault('name', 'N/A')
e['name'] = 'ga'
print(e)
e.setdefault('w')  # ,'N/A'
e.update({'name': 'sad'})
