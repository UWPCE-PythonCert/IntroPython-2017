
'''
Dev: Hiro Takechi
Subject: FizzBuzz
'''

'''
def print_fizz():
	print("Fizz")

def print_buzz():
	print("Buzz")

def print_fizzbuzz():
	print("FizzBuzz")
'''

def fizz():

	print("approach #1")

	for n in range(1,101):

		if (n % 3) == 0 and (n % 5) == 0:
			print(n, "FizzBuzz")
		elif n % 3 == 0:
			print(n, "Fizz")
		elif n % 5 == 0:
			print(n, "Buzz")
		else:
			print(n, "others")

fizz()


def fizz():

	print("approach #2")

	for n in range(1,101):

		if n % 15 == 0:
			print(n, "FizzBuzz")
		elif n % 3 == 0:
			print(n, "Fizz")
		elif n % 5 == 0:
			print(n, "Buzz")
		else:
			print(n, "others")

fizz()