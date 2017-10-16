

corner  = "+ "
horiz = "- "
vert  = '| '
fill  = '  '

def draw(n):
	horizontal 	= corner + horiz * n + corner + horiz * n + corner
	vertical 	= vert + fill * n + vert + fill *n + vert 

	print(horizontal)
	for x in range (n):
		print (vertical)
	print (horizontal)
	for x in range (n):
		print (vertical)
	print (horizontal)
	


def array(size, number):
	horizontal = (corner + horiz * size)*number+corner
	vertical   = (vert 	 + fill  * size)*number+vert

	for x in range(number):
		print(horizontal)
		for x in range(size):
			print(vertical)
	print(horizontal)

def fizzbuzz():
	for x in range(1,101):
		msg = ''
		if x % 3 ==0:
			msg += "Fizz"
		if x % 5 ==0:
			msg += 'Buzz'
		if not msg:
			msg += str(x)
		print(msg)