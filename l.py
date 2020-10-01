class a(object):
	size ='a size '
	def __init__(self):
		self.color ='white'
		print('a init')

	def outPut(self):
		print(self.size)
class d(a):
	def __init__(self):
		self.name ='dog'
		print('d init')

	def run(self):
		print("开始",d.size)
		print(self.size,self.color,self.name)
		print("后来",d.size)#类的属性不会因为self的改变而改变
		a.outPut(self)
class c(a):
	def __init__(self ):
		# super.__init__(self)
		self.name='cat'
		print('c init ')
	def run(self):
		super(c,self).__init__
		print(c.size,self.color,self.name)
		super(c,self).outPut()
		
		

# dog =d()
# print("!",dog.size)
# # dog.run()
# dog.size='d.size'
# dog.color='bb'
# dog.run()
cc=c()
# print(cc.size,c.size)
cc.run()
