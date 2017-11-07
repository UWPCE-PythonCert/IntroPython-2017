#!/usr/bin/env python

donors = {"John Doe": [152.33, 700], "Jane Doe": [23.19, 50, 15.99]}


def main_loop():
    """ Main menu to call different functions """
    while True:
        print("\n========== Donation Management System Main Menu ==========")
        print("*                 (s) Send a Thank You                   *")
        print("*                 (c) Create a Report                    *")
        print("*                 (e) Send letters to everyone           *")
        print("*                 (q) Quit                               *")
        print("==========================================================")
        result = input("Please select a menu item: ")
        if result == 's':
            thank_you()
        elif result == 'c':
            report()
        elif result == 'e':
            email_all()
        elif result == 'q':
            break
        else:
            print("\n*** Selected item not in the menu. Please try again. ***\n")


def email(n):
    """ Send donor an email with latest donation """
    return """
        Dear {},

        Thank you for your recent generous donation of ${}.
        Your support encourages our continued commitment to reaching our goal.

        Sincerely,
        The Donation Management
        """.format(n, donors.get(n)[-1])


def thank_you():
    """ Thank you function """
    while True:
        result = input("\nPlease enter full name, 'list' for current donor list, or 'q' return to the main menu: ")

        # Print donor list
        if result == "list":
            print(str(donors.keys())[11:-2])
        # Back to the main menu
        elif result == "q":
            break
        # Create new donations
        else:
            # Check if donor is already in dict, if not, create a empty list for value
            if result not in donors:
                donors[result] = []
            amount = input("Please enter the amount of donation: ")
            donors[result].append(float(amount))
            print("\nSending Thank You email...\n{}".format(email(result)))

def report():
    """ Generate report """
    print("\n* Donor Name                  |     Total gifted     | Donations |  Average gifted *")
    print("====================================================================================")
    for donor in donors:
        # Total amount
        total = 0.0
        for i in donors[donor]:
            total += i
        # Number of donations
        don = len(donors[donor])
        # Average donation
        avg = total/don
        # Print report
        print("* {: <30}{:16.2f}{: >16}{:18.2f} *".format(donor, total, don, avg))
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
