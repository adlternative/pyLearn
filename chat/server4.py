#! /usr/bin/python
from asyncore import dispatcher
from asynchat import async_chat
import asyncore
import socket
PORT = 5005
NAME = 'AChatRoom'
class EndSession(Exception): pass


class CommandHandler:
  def unknown(self, session, cmd):
    session.push('unknown command:{}\r\n'.format(cmd))

  def handle(self, session, line):
    if not line.strip: return
    parts=line.split(' ', 1)
    cmd=parts[0]
    try:
      line=parts[1].strip()
    except IndexError:
      line=''
    # print("the cmd is %s"%cmd,type(cmd))
    meth=getattr(self, 'do_'+ cmd, None)
    try:
      meth(session, line)
      # print("the cmd is work all right")
    except TypeError as e:
      # print(e)
      self.unknown(session, cmd)

class Room(CommandHandler):
  def __init__(self, server):
    self.server=server
    self.sessions=[]
  def add(self, session):
    self.sessions.append(session)
  def remove(self, session):
    self.sessions.remove(session)
  def broadcast(self, line):
    for session in self.sessions:
      session.push(line)
  def do_logout(self, session, line):
    raise EndSession

class LoginRoom(Room):
    def add(self, session):
      Room.add(self, session)
      session.push('Welcome to {}\r\n'.format(self.server.name))
    def unknown(self, session, cmd):
      session.push('please login\nUse "login <nick>"\r\n')
    def do_login(self, session, line):
      name=line.strip()
      if not name:
        session.push("please enter a name\r\n")
      elif name in self.server.users:
        session.push('the name"{}" is taken.\r\n'.format(name))
        session.push('please try again\r\n')
      else:
        session.name=name
        session.enter(self.server.main_room)

class ChatRoom(Room):
  def add(self, session):
    self.broadcast(session.name+'has entered the room.\r\n')
    self.server.users[session.name]=session
    Room.add(self, session)
  def remove(self, session):
    Room.remove(self, session)
    self.broadcast(session.name+'has left the room\r\n')
  def do_say(self, session, line):
    self.broadcast(session.name+':'+line+'\r\n')

  def do_look(self, session, line):
    session.push('the following are in chatroom:\r\n')
    for ses in self.sessions:
      # print(type(other))
      # if(ses is not session):
      session.push((ses.name)+'\r\n')#other.name

  def do_who(self, session, line):
    session.push('the following are logged in:\r\n')
    for name in self.server.users:
      session.push(name+'\r\n')

class LogoutRoom(Room):
  def add(self, session):
    try:
      del self.server.users[session.name]
    except KeyError:
      pass
    except AttributeError:
      pass


class ChatSession(async_chat):
    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.set_terminator("\r\n")
        self.server=server
        self.data=[]
        # self.push('welcome to %s\r\n' % self.server.name)
        self.enter(LoginRoom(server))

    def enter(self, room):
        try: cur=self.room
        except AttributeError: pass
        else: cur.remove(self)
        self.room=room
        room.add(self)

    def collect_incoming_data(self, data):
        # print(type(data),data,data.decode())
        self.data.append(data)

    def found_terminator(self):
        line=''.join(self.data)
        self.data=[]
        try:self.room.handle(self,line)
        except EndSession:self.handle_close()
        # self.server.broadcast(line)
        # print(line)

    def handle_close(self):
        async_chat.handle_close(self)
        # self.server.disconnect(self)
        self.enter(LogoutRoom(self.server))

class ChatServer(dispatcher):

    def __init__(self, port, name):
        dispatcher.__init__(self)
        # dispatch.__init(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name=name
        self.sessions=[]
        self.users ={}
        self.main_room =ChatRoom(self)

    # def disconnect(self, session):
    #     self.sessions.remove(session)
    # def broadcast(self, line):
    #     for session in self.sessions:
    #         session.push(line+'\r\n')
    def handle_accept(self):
        conn, addr=self.accept()
        # self.sessions.append(ChatSession(self, conn))
        ChatSession(self,conn)

if __name__ == '__main__':
    s=ChatServer(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print()
