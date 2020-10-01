import os
pid=os.fork()

if pid == 0:
	# print("san pid%d"%os.getpid())
	# os.execlp("python3.6", "python3.6", 'hello.py') 
	os.execlp("/home/adl/下载/pycharm-2020.2.2/bin/pycharm.sh", "pycharm.sh") 
else :
	
	pass
	os.wait()
	# print("father pid%d"%os.getpid())
