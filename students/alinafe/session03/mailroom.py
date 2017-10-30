#!/usr/local/bin python3
"""
Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated. 
This structure should be populated at first with at least five donors, with between 1 and 3 donations each.

You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
"""


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

def mainloop():


if __name__ == '__main__':
    print()
    mainloop()