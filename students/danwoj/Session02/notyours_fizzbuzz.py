for i in range(101):
	if i==0:
		False
	elif i%3 == 0:
		if i%5 == 0:
			print(i, 'FizzBuzz')
		else:
			print(i, 'Fizz')
	elif i%5 == 0:
		print(i, 'Buzz')
	else:
		print(i)