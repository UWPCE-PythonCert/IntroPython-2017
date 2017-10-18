#!/usr/bin/env python
"""this program will store donor information, and allow users to send a thank you to a specific donor, create a report of donations, or quit the program"""




#Set up initial data structure (use list since it needs to be mutable)
donors = ['Paul', 'Jerry', 'Paul', 'Jimmy', 'Clark', 'Terry', 'Arthur', 'Clark', 'Jim', 'Martha', 'Martha']

Paul = [100000, 1200000, 750000, 25000]
Jerry = [20000, 43126]
Clark = [1292, 6788, 128, 9827]
Terry = [11, 2000000, 1000001, 45]
Arthur = [50, 100]
Jim = [4567, 1999, 43213]
Martha = [3500000, 49]


# Prompt the user for what they want to do

# Define some variables

choice = 0
name = ""

## Text menu in Python

def print_menu():  # These are the options in the menu
    print(20* "*" +' MENU ' + 20* "*")
    print("1. Send a thank you note")
    print("2. Create a report")
    print("3. Quit program")
    print(20* "*" +' MENU ' + 20* "*")

def get_action(): # this is getting the input from the user on what they want to do
    print_menu()
    choice = input("What would you like to do? ")

def take_action():    
    choice = int(input("What would you like to do? "))
    if choice == 1:
        print("Let's send a thank you note \n")
        name = input("Who do you want to send a thank you note to? ")
        get_name()
    elif choice == 2:
        print("Let's create a report")
    elif choice == 3:
        print("Ending program")
        exit()
    else:
        print("That isn't a valid selection. Please try again")


# Get the name from the user; if the name isn't in the donors list, add it
def get_name():
    name = input("Who do you want to send a thank you note to? Enter a Full Name, or 'list' to get a list of donors. ")
    if name in donors:
        print(name)
    elif name == "list":
        print(donors)
        name = input("Which of those would you like to send a thank you note to? ")
    else:
        donors.append(name)

# Write a thank you note to a specific donor

def note():
    name = input("Enter name please. ")
    name = name.title()
    amount = input("Enter a donation amount please. ")
    amount = str(amount)
    print(f"Dear {name}, ".format())
    print()
    print(f"Thank you for your generous donation of ${amount} to AI research at the Foundation for Future Development and Security of Humans in light of Ariticial Intelligence (FFDSHAI).")
    print()
    print("Your contribution will enable future generations to autonomize their day-to-day lives, without being ruthlessly slaughtered by the AI they create.")
    print()
    print(" We look forward to interacting with you in the future!")
    print()
    print("Sincerely, ")
    print("Dr. Egbert P. Sloanbody III")


def report():
    donor = name
    total = sum(Paul)
    gift_count = 3
    avg_gift = round(total/gift_count, 2)
    print("Donor Name\t | Total Given\t | Num Gifts\t | Average Gift")
    print(f"{donor}\t\t | {total}\t | {gift_count}\t\t | {avg_gift}".format())

take_action()



