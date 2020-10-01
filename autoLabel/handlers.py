
class Handler:
	def callback(self,prefix,name,*args):
		method =getattr(self,prefix+name,None)
		if callable(method): return method(*args)
	def start(self,name):
		self.callback('start_',name)
	def end(self,name):
		self.callback('end_',name)
	#用c++就是　func=std.bind(substitution,(隐藏的self,name),_1)
	def sub(self,name):
		def substitution(match):
			result = self.callback('sub_',name,match)
			if result is None : 
				result =match.group(0)	
			return result
		return substitution

class HTMLRenderer(Handler):
	def start_paragraph(self):
		print('<p>')
	def end_paragraph(self):
		print('</p>')
	def sub_emphasis(self,match):
		return '<em>{}</em>'.format(match.group(1))
	def feed(self,data):
		print(data)
