import keyword
def  CirArea(r):
    area =3.14*r*r
    print("the area of circle is",area)
    
def TriArea(b,h):
    area =1.0/2*b*h
    print("the area of reacangle is:")
    return area

CirArea(4)
print(TriArea(3,4))
print(keyword.kwlist)
string = "sad"
print(string)
print(type("SAd"))
m=121318937129479734197439327937491832479413211111111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
n=1213189371294797341974393279374918324794132
print(m*n)
g=''''py'Pro'''
print(g)


x=[6,2,3,4,1]

for i in range (len(x)-1):
    print('i=',i)
    for  j in range (i+1,len(x),1) :
        print('j=',j)
        if(x[i] >x[j]):
            t=x[i]
            x[i]=x[j]
            x[j]=t

print(x)

str = 'as可怜djk'
qq =str.encode('utf-8')
print(qq)
c=qq.decode('utf-8')
print(c)
print("\t%d\n%d%s"%(1,2,"SAd"))

print(12.0//5)
print('a'*10)
print("sad"*10)
print(2**3)
x=y=4
x,y,z =1,2,3
# x=input("input your number :")
# string =input("input your str:")
# print(x,string)
# p=1
# print(type(p))
# print(p)
p=int(input("sad :"))
print(type(p))
print(p)
print(x,y,sep=':')
print(x,y,sep=':',end='%')
print("sum=%d"%x)
year =1
month =1
day =1
print('%04d-%02d-%02d'%(year,month,day))

alist = ['phy','chem',201,2.3]
print(type(alist[-4]))
alist.append(1)
alist.extend([1,2])
del alist[2]
print(alist),
alist.pop(),
print(
alist.index(1,2,7),
alist.count(1),
alist
)
blist = [6,1,2,3,4,5]
print(sorted(blist,reverse=True))
while(True):
 print("silly")
