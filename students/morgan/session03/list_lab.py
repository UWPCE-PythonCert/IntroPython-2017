#!/usr/bin/env python3
# $ ./list_lab.py
# chmod +x list_lab.py

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruit)

new_fruit = input("What's fruit would you like to add?\n"
            "> ")

fruit.append(new_fruit)

print(fruit)
    
number = int(input("What's your number?\n"
            "> "))

print(number, fruit[number-1])

newest_fruit = []
newest_fruit.append(input("What's fruit would you like to add?\n"
            "> "))
print(newest_fruit)
added_fruit_list = newest_fruit + fruit
print(added_fruit_list)

added_fruit_list.insert(0, input("What's fruit would you like to add?\n"
            "> "))

for x in range(len(added_fruit_list)):
    if str.lower(added_fruit_list[x][0:1]) == 'p':
        print(added_fruit_list[x])


# Series 2

print(added_fruit_list)

added_fruit_list = added_fruit_list[:-1]
print(added_fruit_list)


remove_fruit = input("What's fruit would you like to remove?\n"
            "> ")

print(remove_fruit)
print(added_fruit_list[0])

for thing in added_fruit_list:
    if str.lower(thing) == str.lower(remove_fruit):
        added_fruit_list.remove(thing)

print(added_fruit_list)

# Series 3

on = True
for thing in added_fruit_list[:]:
    
    while on == True:
        x = input('Do you like ' + thing + '?\n')
        if str.lower(x) == 'no':
            added_fruit_list.remove(thing)
            break
        elif str.lower(x) == 'yes':
            break
        else:
            print("Please enter 'yes' or 'no'\n")

print(added_fruit_list)

# Series 4


reverse_fruit = fruit[:]

i = 0
while i < len(reverse_fruit):
    reverse_fruit[i] = reverse_fruit[i][::-1]
    i += 1

del fruit[-1:]
print(fruit)
print(reverse_fruit)

input('wait')