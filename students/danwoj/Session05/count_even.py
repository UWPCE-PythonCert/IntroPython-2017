#!/usr/bin/python

given_list = [2, 1, 2, 3, 4]

def count_evens(nums):
   comprehension = [x for x in nums if x % 2 == 0]
   print(len(comprehension))

def mainloop():

	count_evens(given_list)

if __name__ == '__main__':
	mainloop()