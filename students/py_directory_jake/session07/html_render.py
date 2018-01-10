class Element():
	tag = 'html'
	indent = '  '
	def __init__(self, content=None):
		if content is None:
			self.content = []
		else:
			self.content = [content]

	def append(self, content):
		self.content.append(content)

	def render(self, file_obj):

		file_obj.write('<'+ self.tag + '>' + '</')
		for each in self.content:
			file_obj.write(each)
		file_obj.write('</'+ self.tag + '>' + '</')

class Body(Element):
	tag = 'body'

class Para(Element):
	tag = 'p'

class HTML(Element):
	tag = 'html'




