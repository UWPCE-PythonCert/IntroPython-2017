#!/usr/bin/env python

"""this program will store donor information, 
and allow users to send a thank you to a specific donor, 
create a report of donations, or quit the program"""


from textwrap import dedent  # nifty utility!
import math

#Set up initial data structure (use list since it needs to be mutable)
donors_list = [ ("Paul", [100000, 1200000, 750000, 25000]), 
                ("Jerry", [20000, 43126]), 
                ("Clark", [1292, 6788, 128, 9827]), 
                ("Terry", [11, 2000000, 1000001, 45]), 
                ("Arthur", [50, 100] ), 
                ("Jim", [4567, 1999, 43213]), 
                ("Martha", [3500000, 49])]


def interactive_loop():

    if __name__ == "__main__":
        program_status = True
        while program_status:
            selection = start_menu()
            if selection == '1':
                get_donor()
            elif selection == '2':
                report()
            elif selection == '3':
                program_status = False
            else:
                print("Invalid entry. Please select 1, 2 or 3")


def start_menu():  # These are the options in the menu
    selection = input('''
        Make a selection--

        '1. Send a thank you note'
        '2. Create a report'
        '3. Quit program'

        ''')
    return selection


#print the names from the donors list, without the amounts of their donations

def print_list():
    for donor in donors_list:
        print(donor[0])


# Get the name from the user

# I tried using a while loop here, but can't get my head around how to order everything.....
# for some reason, if 'menu' is entered, and the user is kicked back to the start menu, entering '3' DOESN'T exit the program and I have no idea why

def get_donor():
    while True:
        donor = input("Who do you want to send a thank you note to? \nEnter a Full Name, or 'list' to get a list of donors. \nOr 'menu' to get back to the main menu. ")
        if donor == "list":
            print_list()
        elif donor == 'menu':
            start_menu()
        else:
            break

        amount = input("How much did they donate? ")



# build the thank you note based off information already entered

#  i need to move / remove the asking for donor name and donation amount....I want this part to just build the note

def note():
    donor = input("Who has made the donation? ")
    donor = donor.title()
    
    amount = str(amount)
    print(f"Dear {donor}, ".format())
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
    donor = input("Who has made the donation? ")
    total = sum(donor)
    gift_count = 3
    avg_gift = round(total/gift_count, 2)
    print("Donor Name\t | Total Given\t | Num Gifts\t | Average Gift")
    print(f"{donor}\t\t | {total}\t | {gift_count}\t\t | {avg_gift}".format())
