import struct,pickle
x=int(input("输入"))

y=struct.pack('i',x)
print(y)

fp=open("a.txt","wb")
fp.write(y)
fp.close()

# fp=open("a.txt","r")
i=12345
f=2123.213
b=False
string =struct .pack('if?',i,f,b)
fp=open("a.txt","wb")
fp.write(string)
fp.close()

fp=open("a.txt","rb")
string=fp.read()
sw,qq,e=struct.unpack('if?',string)
print(sw,qq,e)
fp.close()
exit

fp=open("a.txt","wb")
# fp.write(string)
pickle.dump(i,fp)
pickle.dump(f,fp)
pickle.dump(b,fp)
fp.close()
fp=open("a.txt","rb")

while True:	
	if(fp):
		try:
			ppq=pickle.load(fp)
			print(ppq)
		except EOFError:
			fp.close()
			break
	

