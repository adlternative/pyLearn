from asyncore import dispatcher
import asyncore
import socket


class ChatServer(dispatcher):
    def __init__(self, port):
        super().__init__()
        #dispatch.__init(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        conn, addr = self.accept()
        print('Connection attempt from', addr[0])
if __name__ == '__main__':
  s = ChatServer(5005)
  try:
     asyncore.loop()
  except KeyboardInterrupt:
      pass
