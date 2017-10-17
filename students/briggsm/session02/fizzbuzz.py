#fizzbuzz

for n in range(100):
    o = n+1
    if o%3 == 0 and o%5 == 0:
        print ("fizzbuzz")
    elif o%3 == 0:
        print ("fizz")
    elif o%5 == 0:
        print ("buzz")
    else:
        print (o)