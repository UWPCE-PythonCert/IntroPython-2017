#!/usr/bin/env python
import sys

donors = {"John Doe": [152.33, 700], "Jane Doe": [23.19, 50, 15.99]}

def main_loop():
    """ Main menu to call different functions """
    menu_dict = {'s': thank_you,
                 'c': report,
                 'e': email_all,
                 'q': sys.exit}
    while True:
        print("\n========== Donation Management System Main Menu ==========")
        print("*                 (s) Send a Thank You                   *")
        print("*                 (c) Create a Report                    *")
        print("*                 (e) Send letters to everyone           *")
        print("*                 (q) Quit                               *")
        print("==========================================================")
        result = input("Please select a menu item: ")
        try:
            menu_dict[result]()
        except KeyError:
            print("\n*** Selected item not in the menu. Please try again. ***")

def email(n):
    """ Send donor an email with latest donation """
    return """
        Dear {},

        Thank you for your recent generous donation of ${}.
        Your support encourages our continued commitment to reaching our goal.

        Sincerely,
        The Donation Management
        """.format(n, donors.get(n)[-1])

def donor_list():
    """ List name of donors """
    return str(donors.keys())[11:-2]

def add_donor(name):
    """ Create new donor entry """
    donors[name] = []

def add_donation(name, amount):
    """ Create new donation """
    try:
        donors[name].append(float(amount))
        print("\nSending Thank You email...\n{}".format(email(name)))
    except ValueError:
        print("*** Wrong value format, please enter a valid number. ***")
        # Make sure to remove the donor if donation amount not entered correctly
        donors.pop(name)

def thank_you():
    """ Thank you function """
    while True:
        result = input("\nPlease enter full name, 'list' for current donor list, or 'q' return to the main menu: ")

        # Print donor list
        if result == "list":
            print(donor_list())
        # Back to the main menu
        elif result == "q":
            break
        # Create new donations
        else:
            # Check if donor is already in dict, if not, create a empty list for value
            if result not in donors:
                add_donor(result)
            amount = input("Please enter the amount of donation: ")
            add_donation(result, amount)

def gen_report(name):
    """ Generate report """
    total = 0.0
    for i in donors[name]:
        total += i
    # Number of donations
    don = len(donors[name])
    # Average donation
    avg = total/don
    # Print report
    return "* {: <30}{:16.2f}{: >16}{:18.2f} *".format(name, total, don, avg)

def report():
    """ Output report """
    print("\n* Donor Name                  |     Total gifted     | Donations |  Average gifted *")
    print("====================================================================================")
    for donor in donors:
        # Print report
        print(gen_report(donor))
    print("====================================================================================")

def email_all():
    """ Write a full set of letters to everyone to individual files on disk """
    for donor in donors:
        with open('{}.txt'.format(donor).replace(" ", "_"), 'w') as f_out:
            f_out.write(email(donor))
    print("\nLetters generated!")

if __name__ == '__main__':
    """ Main function """
    main_loop()
