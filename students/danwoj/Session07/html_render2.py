#!/usr/bin/env python

'''
This is the class exercise that renders the sample HTML file called 'exercise_html.html'
'''
indent4 = '    '

class Element():

	tag = 'html'
	indent = ''

	def __init__(self, content = None):
		if content is None:
			self.content = []
		else:
			self.content = [content]

	def append(self, content):
		self.content.append(content)

	def render(self, file_object, ind=''):
		if self.tag == 'html':
			file_object.write('<!DOCTYPE html>\n')
		if self.tag == 'head':
			file_object.write(ind + self.indent + '<' + self.tag + '>\n')
			iter_self = iter(self.content)
			file_object.write(ind + self.indent + '</' + self.tag + '>\n')
			content2 = next(iter_self)
			content2.render(file_object)
			return
		file_object.write(ind + self.indent + '<' + self.tag + '>\n')
		for each in self.content:
			try:
				each.render(file_object)
			except AttributeError:
				file_object.write(ind + self.indent + indent4 + str(each))
		file_object.write('\n' + ind + self.indent + '</' + self.tag + '>')

#    def render(self, out_file, ind=""):
#        if self.tag == 'html':
#            out_file.write('<!DOCTYPE html>')
#        out_file.write('\n')
#        out_file.write(ind + '<' + self.tag + '>')
#        for each in self.content:
#            try:
#                each.render(out_file, ind + self.indent)
#            except AttributeError:
#                out_file.write('\n' + ind + self.indent + str(each))
#        if ind != "":
#            out_file.write('\n' + ind)
#        out_file.write('</' + self.tag + '>')

class Body(Element):
	tag = 'body'
	indent = indent4 * 2

class Para(Element):
	tag = 'p'
	indent = indent4 * 3

class Html(Element):
	tag = 'html'
	indent = '    '

class Head(Element):
	tag = 'head'
	indent = indent4 * 2

class OneLineTag(Element):
	tag = 'oneline'
	
	def render(self, file_object, ind=''):
		file_object.write(ind + self.indent + '<' + self.tag + '> ')
		for each in self.content:
			try:
				each.render(file_object)
			except AttributeError:
				file_object.write(str(each))
		file_object.write(' </' + self.tag + '>\n')

class Title(OneLineTag):
	tag = 'title'
	indent = indent4 * 3

def mainloop():
	print('run')

if __name__ == '__main__':
	mainloop()

