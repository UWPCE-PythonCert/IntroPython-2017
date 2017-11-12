#!/usr/bin/python

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

def mainloop():

	print('{name} is from {city}, and he likes, {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta'.format(**food_prefs))

	print(dict([(i, hex(i)) for i in range(16)]))

	print({i: hex(i) for i in range(16)})

	print({key: val.count('a') for key, val in food_prefs.items()})

	s2 = {i for i in range(20) if i % 2 == 0}

	s3 = {i for i in range(20) if i % 3 == 0}

	s4 = {i for i in range(20) if i % 4 == 0}

	print('s2: ', s2)
	print('s3: ', s3)
	print('s4: ', s4)

	seq = [2, 3, 4]

	set_list = [set() for i in seq]

	for i, j in zip(seq, set_list):
		[j.add(k) for k in range(21) if not j % i]

	print(set_list)

	n = 5
	divisors = range(2, n + 1)
	print("divisors ", divisors)
#	# create a list of empty sets
#	sets = [set() for i in divisors]
#	print(sets)

#	for i, st in zip(divisors, sets):
#		[st.add(j) for j in range(21) if not j % i]
#
#	print("\nHere are all the sets:\n", sets)

if __name__ == '__main__':
	mainloop()


#	Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

#        Do this with one set comprehension for each set.