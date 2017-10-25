#!/usr/bin/env python

# Creating global fruit list
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

def series_1():
    """ Series 1 tasks """
    
    print("The current fruit list: " + str(fruits))
    
    # Append a fruit
    morefruit = input("Enter the fruit you want to add to the list: ")
    fruits.append(morefruit)
    print("The current fruit list: " + str(fruits) + '\n')
    
    # Print a fruit from the list
    indexfruit = input("Enter index of the fruit you want to display: ")
    print(fruits[int(indexfruit)-1] + '\n')
    
    # Insert a fruit at front
    insertfruit = input("Insert a fruit to the beginning of the list: ")
    fruits.insert(0, insertfruit)
    print("The current fruit list: " + str(fruits) + '\n')

    # Print all fruits start with P
    print("All fruits begin with 'P' in the list: ")
    for f in fruits:
        if f[0] == 'P':
            print(f)
    print()


def series_2():
    """ Series 2 tasks """

    # Remove the last element from the list
    print("The current fruit list: " + str(fruits))
    del fruits[-1]
    print("Deleting last fruit from the list...")
    print("The current fruit list: " + str(fruits) + '\n')

    # Creating a new list = List*2, remove all fruit name matched in the list
    print("Doubling the list...")
    fr2 = fruits*2
    print("The current fruit list: " + str(fr2))

    while True:
        removefruit = input("Please enter the fruit name you would like to remove: ")
        if removefruit not in fr2:
            print("No match, please try again.")
        else:
            while removefruit in fr2:
                fr2.remove(removefruit)
            break
    print("The current fruit list: " + str(fr2) + '\n')


def series_3():
    """ Series 3 tasks """

    # Make sure to iterate a "copy" of the list
    for fruit in fruits[:]:
        while True:
            result = input("Do you like " + fruit + "? ")
            if result == "yes":
                break
            elif result == "no":
                fruits.remove(fruit)
                break 
            else:
                print("Please type in yes or no only.")

    print("The current fruit list: " + str(fruits) + '\n')


def series_4():
    """ Series 4 tasks """

    # Make a copy of the original fruit list
    newfruits = fruits[:]

    # Reverse letters in each fruit in new list
    for l in range(len(newfruits)):
        newfruits[l] = newfruits[l][::-1]

    # Remove the last item from original list
    del fruits[-1]

    # Compare the result
    print("Original list: " + str(fruits))
    print("Copied list: " + str(newfruits))


if __name__ == "__main__":
    """ Run all series """
    series_1()
    series_2()
    series_3()
    series_4()
