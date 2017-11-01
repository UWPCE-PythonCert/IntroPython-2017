#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# list_lab.py

# Series 1
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
# Copies for later use
fruit_series3 = fruit[:]
fruit_series4 = fruit[:]



print("Fruit in list: ",fruit)

new_fruit = str(input("Enter another fruit: ")).strip()

fruit.append(new_fruit)

print("Fruit in list is now: ",fruit)

number_of_fruit=len(fruit)

print("Now give me a number between 1 and {n:}.".format(n=number_of_fruit))

fruit_number_choice = int(input("Number choice: "))

print("The fruit you chose is: {d:}".format(d=fruit[fruit_number_choice-1]))

# Add fruit to the beginning:
fruit = ['Banana'] + fruit
print("fruit list is now:", fruit)

fruit.insert(0,'Nectarine')
print("After insert, fruit is now: ",fruit)

# Display fruit beginning with 'P':
for x in fruit:
    if x[0] == 'P':
        print(x)

# Series 2
# Display the list from above

print("List from Series 1:", fruit)

# Remove the last fruit:
fruit.pop()
print("After removing the last fruit, the list is now: ", fruit)

# Ask user for fruit to delete.
delete_fruit = str(input("Enter a fruit you want to delete from list: "))

fruit.remove(delete_fruit)
print("After deleting fruit, the list is now: ", fruit)

# Series 3
# Reset fruit to list from the beginning of Series 1
fruit_series3

for choice in fruit:
    ask = str(input("Do you like {d:} (Enter 'yes' or 'no')?".format(d=choice)))
    while ask.lower() not in ('yes', 'no'):
        ask = str(input("Your answer was not 'yes' or 'no'.  Please enter one of these responses: "))
    if ask == 'yes':
        fruit.remove(choice)

print("After reviewing the list, the entries are now: ",fruit)


# Series 4
fruit = fruit_series4[:]
print("fruit list is: ", fruit)
print("fruit list for Series 4 is: ", fruit_series4)

i = 0
for item in fruit_series4:
    fruit[i]=item[::-1]
    i += 1

print("Original list: ", fruit_series4)
print("Modified list: ", fruit)

