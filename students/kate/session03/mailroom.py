#!/usr/bin/env python3

"""
Mailroom Exercise, session 3
"""
import math

# define global donor list and $
donors = [("Hermione Granger", [43.01, 13.17]),
            ("Molly Weasley", [87.03]),
            ("Luna Lovegood", [61.03, 44.87, 44.32]),
            ("Sybill Trelawney", [16.23, 43.87, 10.0]),
            ]

#create a function for the main menu
def main_menu():
    action = input('''
      Thank you donating to Hogwarts School. Choose an action:

      1. - Send a Thank You Owl
      2. - Create a Report
      3. - Quit

      > ''')
    return action.strip()

def write_thankyou(donor_input, amount):
    return('''
          Dear {}

          Thank you for your very donation of ${:.2f}.
          You have enabled excellemt magical instruction!

                         Sincerely,
                            -Hogwarts School of Witchcraft and Wizardy
          '''.format(donor_input, amount))

def send_thankyou():
    while True:
        donor_input = input("""
        Enter a donor's name.
        Select 1. to see all donors
        Select 2. to exit to main menu

        >
        """).strip()

        if donor_input == '1':
                print_donors()
        elif donor_input == '2':
            return
        else:
            break

    while True:
        amount = input("Enter a donation amount (or type 'quit' to exit to main menu) > ").strip()
        if amount == "quit":
            return
        else:
            amount = float(amount)
            break

    donors.append((donor_input, amount))
    print(write_thankyou(donor_input, amount))
    print(send_thankyou())
    return

def find_donor(name):
    for donor in donors:
        # do a case-insenstive compare
        if name.strip().lower() == donor[0].lower():
            return donor
    return None


# loop through the donor list and print the 0th element of the list
def print_donors():
    print("Donors:\n")
    for donor in donors:
        print(donor[0])

# this forces the first item, not the 0th item, to be the first item
def sort_key(item):
    return item[1]

# print donor report
def print_report():
    # First, reduce the raw data into a summary list view
    report_rows = []
    # establish some variables
    for (name, gifts) in donors:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data using sort_key function
    report_rows.sort(key=sort_key)

    # print table with spaces
    print("{:30s}  {:10s}  {:10s}  {:10s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("*" * 66)
    for row in report_rows:
        print("{:30s}   {:10f}   {:10d}   {:10f}".format(*row))

if __name__ == "__main__":
    running = True
    while running:
        selection = main_menu()
        if selection == "1":
            send_thankyou()
        elif selection == "2":
            print_report()
        elif selection == "3":
            running = False
        else:
            print("error: invalid selection!")
