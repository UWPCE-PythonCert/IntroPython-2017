#fizzbuzz

count=0

while count<=100:
	if count%3==0:
		print("Fizz")
	elif count%5==0:
	    print("BANG")
	else:
		print(count)
	count=count+1
print("I'm Done")