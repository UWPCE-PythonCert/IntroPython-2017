#!/usr/bin/env python3

def inputName(message):
  while True:
    try:
       userInput = str(input(message))
       userInput = userInput.capitalize()
    except ValueError:
       print("Not an string! Try again.")
       continue
    else:
       return userInput
       break

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an number! Try again.")
       continue
    else:
       return userInput
       break

fruit=["Apples", "Pears", "Oranges", "Peaches"]

print(fruit)

askForFruit=inputName("Enter another fruit: ")
fruit.append(askForFruit)

print(fruit)

while True:
    try:
        newFruitNumber = inputNumber("Enter a number equal to or less than {}: ".format(fruit.index(fruit[-1])))
    except ValueError:
        print("That number is out of Range!")
    else:
        if 0 <= newFruitNumber < fruit.index(fruit[-1]):
            print(newFruitNumber)
            break
        else:
            print("Out of range. Try Again")

fruit= ["Grape"] +fruit
fruit.insert(0, 'Pine Apple')
