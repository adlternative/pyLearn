# f=open('c.txt','w')
# f.write('hello')
# f.close()
# f=open('c.txt','r')
# s=f.read(3)
# print(s)
# s=f.read()
# print(s)
import sys,io,fileinput
# text = sys.stdin.read()
# word = text.split()
# wordcount =len(word)
# print('wordcount',wordcount)
# f = open('c.txt','r+')
# cnt =f.write('012345678901234567890')
# print(cnt)
# cnt =f.seek(5)
# print(cnt)
# f.write('i am  grut')
# f.close()
# f = open('c.txt','r')
# f.seek(io.SEEK_SET)
# print(f.read(),f.tell())
# f.seek(io.SEEK_SET)
# print(f.readline())
# f.close()
# with open('c.txt')as f:
#     for char in f.read():
#         print(char,end=' ')
# print('\n')
with open('c.txt')as f:
	for line in f.readlines():
		print(line,end='')
	

# with open('c.txt')as f:
#     while True:
#         char =f.read(1)
#         if not char:break
#         print(char,end='*')
for line in fileinput.input('c.txt'):	
	print(line,end='')
	