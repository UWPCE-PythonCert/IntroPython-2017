"""
args kwargs exercise

"""

def fun(fore_color='blue',
		back_color='red',
		link_color='yellow',
		visted_color='green'):
	print(fore_color, back_color, link_color, visted_color)
	return (fore_color, back_color, link_color, visted_color)

def fun2(*args, **kwargs):
	return (args, kwargs)