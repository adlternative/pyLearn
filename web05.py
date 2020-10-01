import socket
import select
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
fdmap = {s.fileno(): s}

s.listen(5)
p = select.poll()
''' 对象 '''
p.register(s)
while True:
		events = p.poll()
		''' 函数 '''
		for fd, event in events:
			if fd in fdmap:
				if(fd ==s.fileno()):
					c, addr = s.accept()
					print('got connect from', addr)
					p.register(c)
					fdmap[c.fileno()] = c
				elif event&select.POLLIN:
					data =fdmap[fd].recv(1024)
					if not data:
						print(fdmap[fd].getpeername(),'disconnected')
						p.unregister(fd)	
						del fdmap[fd]
					else:
						print(data)

