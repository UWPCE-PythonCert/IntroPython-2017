#!/usr/bin/env python

'''
This is the class exercise that renders the sample HTML file called 'exercise_html.html'
'''

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)


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

		try:
			content.render(out_file)
		except AttributeError:
			outfile.write(str(content))

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
	print('ran')


if __name__ == '__main__':
	mainloop()

