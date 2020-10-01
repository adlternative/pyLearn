import hello,sys,pprint,copy                      #1
import os                                         #2
# pprint.pprint(sys.path)                         #3
# hello.test()                                    #4
                                                  #5
# pprint.pprint([n for n in dir(copy)])           #6
# pprint.pprint(copy.__all__)                     #7
# print(copy.__doc__,copy.__file__)               #8
print(sys.platform,sys.argv[0],sys.path)          #9
args = sys.argv[1:]                               #10
args.reverse()                                    #11
print('*'.join(args))                             #12
# i =sys.stdins                                   #13
# sys.modules                                     #14
print(os.pathsep,os.sep,os.linesep,os.urandom(10))#15
# os.system('ps -aux | grep hello.py')            #16
# os.execv("/usr/bin/python3.6",("/usr/bin/python3.6",'/home/adl/桌面/pyLearn/hello2.py', 'asd', 'sda'))#17
args=r'-l -a'                                     #18
args=args.strip().split(' ')                      #19
# os.execlp(r"/bin/ls",'ls',*args)                #20
pid=os.fork()                                     #21
                                                  #22
if pid == 0:                                      #23
	print("san pid%d"%os.getpid())                   #24
	# os.execlp("python3.6", "python3.6", 'hello.py')#25
	# os.execlp("/home/adl/下载/pycharm-2020.2.2/bin/pycharm.sh", "pycharm.sh")#26
else :                                            #27
	print("father pid%d"%os.getpid())                #28
# /home/adl/下载/pycharm-2020.2.2/bin/pycharm.sh    #29
                                                  #30
