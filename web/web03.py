from socketserver import TCPServer,ThreadingMixIn,StreamRequestHandler

class Server(ThreadingMixIn,TCPServer):pass
class Handler(StreamRequestHandler):
	def handle(self):
		addr =self.request.getpeername()	
		print("got connection from",addr)
		self.wfile.write('thank you for connection')
server =TCPServer(('',12345),Handler)
server.serve_forever()