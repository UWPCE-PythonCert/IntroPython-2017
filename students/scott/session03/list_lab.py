#!/usr/bin/env python

# Series 1

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']


response = input("please provide a fruit name to add to the fruits list! ")
fruits.append(response)


response = input("What number fruit in the fruits list do you want to see? ")
response = int(response)
print(fruits[response-1])


fruits = ['limes'] + fruits
print(fruits)


fruits.insert(0, 'tomatoes')
print(fruits)

for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit)


# Series 2

print(fruits)
fruits.pop()
print(fruits)

d_fruits = fruits * 2

print("All the fruits are: ", fruits)

response = input("What fruit would you like gone from all the stores? ")

while response in d_fruits:
	d_fruits.remove(response)

print(d_fruits)


