#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python

'''
Fizz buzz
'''

def fizz_buzz():
	for i in range(1,101):
		# multiples of 3 --> fizz; multiples of 5 --> buzz; multiples of 3 and 5 --> fizz buzz
		if i%3 == 0 and i%5 == 0:
			print("fizzbuzz")
		elif i%3 == 0 and i%5 != 0:
			print("fizz")
		elif i%3 != 0 and i%5 == 0:
			print("buzz")
		else:
			print(i)
	
#main
fizz_buzz()