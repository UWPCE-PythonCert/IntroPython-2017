#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# Program tests NameError, TypeError, SyntaxError, AttributeError
import os
# NameError test:
def name_test():
	''' This tests NameError '''
	try: 
		print(brian)
	except NameError as e:
		print("Your variable name has not been defined: ", e)

# TypeError test:
def type_test(val):
	''' This tests TypeError '''
	try:
		a=val/4
	except TypeError as e:
		print("Your type is incorrect:", e)

# SyntaxError test:
def syntax_test():
	''' This tests SyntaxError '''
	try:
		date = eval('datetime(2009, 12a, 31)')
	except SyntaxError as e:
		print("Your syntax is wrong: ", e)

# AttributeError test:
def attribute_test(attrib):
	''' This tests AttributeError '''
	try:
		attrib.size()
	except AttributeError as e:
		print("Attribute problem: ", e)



#main
os.system('clear')
print("This is a test.")
value='test'
#name_test()
#type_test(value)
#syntax_test()
attribute_test(value)

