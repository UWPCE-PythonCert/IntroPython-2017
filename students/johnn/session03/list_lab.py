#!/usr/bin/env python


fruit_list = [ "Apples", "Pears", "Oranges", "Peaches" ]
print("Original list: ", fruit_list)

# add a fruit to the end
new_fruit=input("Enter a new fruit: ")
fruit_list.append(new_fruit)
print("Current list:", fruit_list)

# pick a fruit 
num_fruit=len(fruit_list)
selection=int(input("Enter a number from 1 to "+str(num_fruit)+": "))
print("Fruit#",selection,"is",fruit_list[selection-1],"!")

# add a fruit to the front
selection=input("Enter another fruit: ")
fruit_list=[selection]+fruit_list
print("Fruit in the front is: ",fruit_list)

# add a fruit to the front, redux
selection=input("Enter yet another fruit: ")
fruit_list.insert(0,selection)
print("Yet another fruit in the front: ",fruit_list)

# print the "P" fruits
print("\"P\" Fruits:")
for fruit in fruit_list:
	if fruit.lower().startswith("p"):
		print(fruit)
print("Just in case you forgot:", fruit_list)

# delete the last one
print("Killing the slow fruit")
del fruit_list[-1]
print("New herd:", fruit_list)

# make a list twice as big
big_list=list(fruit_list*2)
print("Bigger list:", big_list)

# pick and delete a fruit
match_found=False
while not match_found:
	selection=input("Enter the name of a fruit from the list: ")
	for index, fruit in enumerate(big_list):
		if fruit == selection:
			print("deleting", index)
			match_found=True
			del big_list[index]

print("Big list fruit left:",big_list)

# which fruit do you like?
bad_fruit_list=[]
print("starting fruit:",fruit_list)

# build the bad fruit list
for fruit in fruit_list:
	selection=input("Do you like "+fruit.lower()+"? ").lower()
	if selection in ["n", "no"]:
		print("adding",fruit,"to the bad fruit list")
		bad_fruit_list.append(fruit)

# fruit you don't like
print("bad fruit:",bad_fruit_list)

# find which fruit match
delete_list=[]
for index, fruit in enumerate(fruit_list):
	for bad in bad_fruit_list:
		if bad == fruit:
			#print(fruit,"are bad!")
			delete_list.append(index)

# deleted them from the end so you don't re-order the list
for index in reversed(delete_list):
	del fruit_list[index]

# what's left
print("good fruit: ",fruit_list)

# make a duplicate list object
list_copy = list(fruit_list)

# reverse them
for index, entry in enumerate(list_copy):
	backwards=entry[::-1]
	list_copy[index]=backwards

# delete last from the original
del fruit_list[-1]

# print them all
print("list copy:",list_copy)
print("list orig:",fruit_list)

