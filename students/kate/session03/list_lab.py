#!/usr/bin/env python3

#series 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

new = input("What's your favorite fruit?")
fruits.append(new)
print(fruits)

number = int(input("Pick a number!"))
print("you selected fruit number: {}, which is {}".format(number, fruits[number - 1]))

print("Fruits:\n", fruits)
print()

#series 2
print("All the fruits are:", fruits)
answer = input("Which fruit would you like to delete?")
while answer in fruits:
    fruits.remove(answer)
print("Here is your modified list: {}".format(fruits))

# series 3
orig_fruits = fruits[:]
for fruit in fruits[:]:
    ans = input("Do you like: %s? " % fruit)
    if ans[0].lower() == 'n':  # so they could answer y or Y or yes or Yes...
        while fruit in fruits:  # just in case there are duplicates
            fruits.remove(fruit)
    elif ans[0].lower() == 'y':
        pass
    else:
        print("please answer yes or no next time!")

print("\nHere they are with only the ones you like")
print(fruits)
print()


#series 4
# reverse the letters in each part of the list
rev_fruits = []
for fruit in fruits:
    rev_fruits.append(fruit[::-1])

print("Here they are reversed")
print(rev_fruits)
