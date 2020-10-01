a_list = ['ssssad','sads',1,2]
print(a_list[1:3])
a_list.remove(1)
a_list.pop()
a_list.count(2)
'sad' in a_list
len(a_list)
print(a_list)
max(a_list)
b_list=sorted(a_list,reverse=False)
del a_list
[1,2,3]>[2,3,4]

b_list.sort()
print(b_list)
b_list.reverse()
b_list.append("sad")
b_list.extend(["saddd","boy"])
b_list.insert(1,1)
print(b_list)
b_list.index("sads")


m=1000
for a in range (2,m+1):
    s=0
    L1=[]
    for i in range(1,a):
        if a%i == 0:
            s+=i
            L1.append(i)
            if s== a:
                print("%d ites facotor are:"%a,L1)


