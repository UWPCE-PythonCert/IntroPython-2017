#!/usr/bin/env python3

def fruit_lst():
	'''
	Playing with list and fruit
	'''
	fruits = ['Apple', 'Pears', 'Orange','Peaches']
	print(fruits)

	new_fruit = input('Please, add a fruit to the list\n')
	fruits.append(new_fruit)
	print(fruits)

	
	bool = True
	nb_fruits = len(fruits)
	while bool:
		number = input('Please give a number between 1 and {}\n'.format(nb_fruits))
		try:
			number = int(number)
			if number <= nb_fruits:
				number -= 1
				bool = False
			else:
				print('Not enough fruits!\n')
		except:
			print('Wrong input !\n')

	print( '{} is fruit {}\n'.format(str(number + 1), fruits[number]) )

	fruits = ['Raspberry'] + fruits
	print(fruits)

	fruits.insert(0, 'Strawberry')
	print(fruits)

	

if __name__ == '__main__':
	fruit_lst()