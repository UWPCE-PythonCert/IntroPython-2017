#!/usr/bin/env python

'''
This is the class exercise that renders the sample HTML file called 'exercise_html.html'
'''

class Element():

	tag = 'html'
	indent = '  '

	def __init__(self, content = None):
		if content is None:
			self.content = []
		else:
			self.content = [content]

	def append(self, content):
		self.content.append(content)

	def render(self, file_object):

		file_object.write('<' + self.tag + '>\n')
		for each in self.content:
			file_object.write(each)
		file_object.write('\n</' + self.tag + '>\n')

class Body(Element):
	tag = 'body'

class Para(Element):
	tag = 'p'

class Html(Element):
	tag = 'html'




def mainloop():
	print('run')

if __name__ == '__main__':
	mainloop()

