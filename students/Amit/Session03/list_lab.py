#! /usr/bin/env python

# Series 1

list1 = ["Apples", "Pears", "Oranges" , "Peaches" ]

"""Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”."""

print(list1)

add_fruit = input("Type of fruit that you would like to add >")

list1.append(add_fruit)

print(list1)

fruit_number = int(input("Which fruit number > "))

print(list1[fruit_number - 1])

add_fruit2 = input("Type of fruit that you would like to add >")

list1.insert(0, add_fruit2)

print(list1)


print()
for fruit in list1:
    if fruit[0].upper() == "P":
       print(fruit)
print()


# Series 2

print("Here are all the furits:- ", list1)

dup_fruits = list1

dup_fruits = list1 * 2

del_fruit = input("Which fruit you would like to delete>")

while del_fruit in dup_fruits:
    dup_fruits.remove(del_fruit)

print("List with deleted fruit",dup_fruits)


#Series 3

for fruit in list1:
    ans = input("Please Enter Yes or No as answer"
                "Do you like {} ?".format(fruit))
    if ans[0].lower() == 'n':
        while fruit in list1:
            list1.remove(fruit)
    elif ans[0].lower() == 'y':
        pass
    else:
        print("Enter either yes or no")

print(list1)

#Series 4

rev_fruits = []

for fruit in list1:
    rev_fruits.append(fruit[::-1])

print(rev_fruits)

rev_fruits = list1[:]
for i, fruit in enumerate(rev_fruits):
    rev_fruits[i] = fruit[::-1]

print(rev_fruits)


rev_fruits = list1[:]
list1 = list1[:-1]

print(list1)
print(rev_fruits)