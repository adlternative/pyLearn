fp =open("./g.py","r")

print(fp.name, fp.mode,fp.closed)

strr =fp.readlines()
for i in strr:
    print(i)
# print(strr)
strr.clear()
strr =fp.readlines()
if len(strr)==0:
    print("no ")
fp.close()

def sadsad():
 fpp = open("./a.txt","r")
 text =fpp.read()
 lines =text.splitlines()
 col1 =[]
 col2 =[]
 for line in lines :
        part =line.split(None,1)#返回list
    # print (type(part)) 
        col1.append(part[0])
        col2.append(part[1])
 fpp.close()
 return col1 ,col2

# print(sadsad())
def write_list(filename,alist):
 fd =open(filename ,'w')
 for line in alist:
  fd.write(line+'\n')

# filename ='input.txt'
col1,col2 =sadsad()
write_list('col1.txt',col1)
write_list('col2.txt',col2) 

def func():
    fd =open("a.txt",'r')
    print (fd.readlines())
func()

