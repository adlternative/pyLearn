import functools
s = set(range(10))
s.add(11)
print(s)
my_set = []
for i in range(10):
    my_set.append(set(range(i, i+5)))

# help("reduce")
functools.reduce(set.union,my_set)
# print(my_set)
a=set({1,2,3})
b=set({3,4,5})
# a.add(b)
a.add(frozenset(b))
print(a)