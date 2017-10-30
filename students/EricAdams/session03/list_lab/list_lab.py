#!/usr/bin/env python

# Series 1


def display_list(seq):
    """Print each item in seq in a numbered list
"""
    i = 0    # item number in  displaying fruit list
    for x in seq:
        i += 1
        print(i, '. ', x)


def print_what_was_entered(number, fruit):
    """Print a statement saying the number and item chosen by the user
"""
    print("You entered {}, which is {}".format(number, fruits[number - 1]))


# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
print("\nSeries 1\n")
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits_orig = fruits[:]
# Display the list (plain old print() is fine…).
print(fruits)
# Ask the user for another fruit and add it to the end of the list.
answer = input("Input a fruit to add to this list> ")
fruits.append(answer.strip().title())
# Display the list.
display_list(fruits)
# Ask the user for a number and display the number back to the user and the
# fruit corresponding to that number (on a 1-is-first basis). Remember that
# Python uses zero-based indexing, so you will need to correct.
number = int(input(" Enter a number from 1 to " + str(len(fruits)) + "> "))
print_what_was_entered(number, fruits)
# Add another fruit to the beginning of the list using “+” and display the
# list.
answer = input("enter a fruit to add to the beginning of the list> ")
fruits = [answer.strip().title()] + fruits
display_list(fruits)
# Add another fruit to the beginning of the list using insert() and display
# the list.
answer = input("> enter a fruit to add to the beginning of the list> ")
fruits.insert(0, answer.strip().title())
display_list(fruits)
# Display all the fruits that begin with “P”, using a for loop.
print("The following fruits begin with P:")
for x in fruits:
    if x[0] == 'P':
        print(x)

# Series 2
print("\nSeries 2\n")
fruits = fruits_orig[:]
# Using the list created in series 1 above:
# Display the list.
display_list(fruits)
# Remove the last fruit from the list.
print("Removing the last fruit from the list")
fruits.remove(fruits[-1])
# Display the list.
display_list(fruits)
# Ask the user for a fruit to delete and find it and delete it.
answer = input("Enter the fruit you want to be deleted.> ")
answer = answer.strip().title()
print("You chose {}".format(answer))
i = 0
for x in fruits:
    if x == answer:
        fruits.remove(fruits[i])
    i += 1
display_list(fruits)
# (Bonus: Multiply the list times two. Keep asking until a match is found.
# Once found, delete all occurrences.)
print("Multipying the list by two")
fruits = fruits * 2
display_list(fruits)
statement = "Enter the fruit you want to be deleted."
while True:
    answer = input(statement)
    answer = answer.strip().title()
    print("You chose {}".format(answer))
    i = 0
    match = False
    for x in fruits:
        if x == answer:
            fruits.remove(fruits[i])
            match = True
        i += 1
    if match is True:
        break
    else:
        statement = answer + ' not found.  Try again'
display_list(fruits)


# Series 3
print("\n Series 3\n")
# Again, using the list from series 1:
fruits = fruits_orig[:]
display_list(fruits)
# Ask the user for input displaying a line like “Do you like apples?” for each
# fruit in the list (making the fruit all lowercase).
i = 0
for x in fruits:
    answer = input('Do you like {}> '.format(x.lower()))
    # For each “no”, delete that fruit from the list.
    if answer.strip().lower() == 'no':
        print('Deleting {} from the list'.format(x.lower()))
        counter = 0
        for y in fruits:
            if fruits[counter] == x:
                fruits.remove(x)
    elif answer.strip().lower() == 'yes':
        continue
    # For any answer that is not “yes” or “no”, prompt the user to answer
    # with one of those two values (a while loop is good here)
    else:
        while True:
            answer = input('Please enter a "yes" or a "no"> ')
            if answer.strip().lower() == 'yes':
                break
            if answer.strip().lower() == 'no':
                break
# Display the list.
display_list(fruits)
# Series 4
print("\n Series 4\n")
# Once more, using the list from series 1:
print('List from Series 1:')
fruits = fruits_orig[:]
display_list(fruits)
# Make a copy of the list and reverse the letters in each fruit in the copy.
copy_fruits = fruits[:]
print('Reversing the letters in each fruit, (copy_fruits')
print("copy_fruits before reversing")
print(copy_fruits)
i = 0
for x in copy_fruits:
    x = x[:: - 1]
    copy_fruits[i] = x
    i += 1
print("copy_fruits after reversing\n", copy_fruits)
# Delete the last item of the original list. Display the original list and
# the copy.
print("deleting the last item of fruits")
del fruits[-1]
print("Original list = {}\nCopy = {}".format(fruits, copy_fruits))
