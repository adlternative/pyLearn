from socketserver import TCPServer,ForkingMixIn,StreamRequestHandler

class Server(ForkingMixIn,TCPServer):pass
class Handler(StreamRequestHandler):
	def handle(self):
		addr =self.request.getpeername()	
		print("got connection from",addr)
		self.wfile.write('thank you for connection')
server =TCPServer(('',12345),Handler)
server.serve_forever()