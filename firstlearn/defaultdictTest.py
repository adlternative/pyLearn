from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['c'].append(1)
print(d)
d = {}  # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)
d = {}  # A regular dictionary
# d['a'].append('sad')

a = slice(0, 10, 2)
s = 'HelloWorld'
a.indices(len(s))

for i in range(*a.indices(len(s))):
    print(s[i])
