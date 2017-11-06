#!/usr/bin/env python3

"""
Mailroom Exercise, session 5
exception handling, comprehensions
"""
import math

# define global donor dict and $
donors_dict = {
    'Hermione Granger': [43.01, 13.17],
    'Molly Weasley':[87.03],
    'Luna Lovegood':[61.03, 44.87, 27.77],
    'Sybill Trelawney':[77.56, 33.45,  756.32]
    }

# create a function for the main menu
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
        donor_input = input('''
        Enter a donor's name.

        *or*
        Select 1. - View donor list
        Select 2. - Return to main menu

        >
        ''').strip()

        if donor_input == '1':
                print_donors_list()
        elif donor_input == '2':
            return
        else:
            break

    while True:
        amount = input("Enter a donation amount > ").strip()
        if amount == "quit":
            return
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid entry! Please enter a number!")
        else:
            break

    donors_dict[donor_input] = amount
    # donors.append((donor_input, amount))
    print(write_thankyou(donor_input, amount))
    print(send_thankyou())
    return

# def find_donor(name):
#    for donor in donors:
        # do a case-insenstive compare
        # if name.strip().lower() == donor[0].lower():
#            return donor
#    return None


# loop through the donor list and print the 0th element of the list
def print_donors_list():
    print("Donors:\n")
    for key in donors_dict:
        print(key)

# this forces the first item, not the 0th item, to be the first item
def sort_key(item):
    return item[1]

# print donor report
def print_report():
    # create a row for each donor
    report_rows = []

    for keys, values in donors_dict.items():
        total_gifts = sum(values)
        num_gifts = len(values)
        avg_gift = total_gifts / num_gifts
        report_rows.append((keys, total_gifts, num_gifts, avg_gift))


    # sort the report data using sort_key function
    report_rows.sort(key=sort_key)

    # print table with spaces for formatting
    print("{:30s}  {:10s}  {:10s}  {:10s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("*" * 66)
#    for row in report_rows:
#        print("{:30s}   {:10f}   {:10d}   {:10f}".format(*row))

    rows = [print("{:30s}   {:10f}   {:10d}   {:10f} ".format(*row)) for row in report_rows]
    # print(rows(range[0,len(rows)])


if __name__ == "__main__":
    running = True
    while running:
        selection = main_menu()
        if selection == "1":
            send_thankyou()
        elif selection == "2":
            print_report()
        elif selection == "3" or "quit":
            running = False
        else:
            print("error: invalid selection!")

# TO DO
# fix Create a Report function
