#!/usr/bin/env python
"""
Interface to mailroom package
"""

from __future__ import print_function

import sys
import math
from mailroom import model, DATA_DIR

MENU = """
Choose an option:

1. Send Thank You
2. Create Report
3. Quit

> """

DB = model.DonorDB.load_from_file(DATA_DIR / "sample_data.json")

def get_selection():
    """ Display menu option and get user input """
    selection = input(MENU)
    return selection.strip()


def send_thank_you():
    """ Record a donation and send thank you message """
    while True:
        name = input("Enter donor's name > ").strip()
        break

    while True:
        amount = input("Enter a donation amount > ").strip()
        try:
            amount = float(amount)
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
            break
        except ValueError:
            print("Invalid amount '{}' entered.".format(amount))

    donor = DB.get_donor(name)
    if donor is None:
        donor = DB.add_donor(name)

    donor.add_donation(amount)
    print(DB.send_letter(donor))


def print_report():
    """ Print out donor report """
    print(DB.get_donor_report())


def quit_program():
    """ Exits program """
    sys.exit(0)


def main():
    """ Entry point for the entire application """
    menu_dict = {"1": send_thank_you,
                 "2": print_report,
                 "3": quit_program}

    while True:
        selection = get_selection()
        print(selection)

        try:
            menu_dict[selection]()
        except KeyError:
            print("ERROR: Selection '{}' is invalid!".format(selection))


if __name__ == "__main__":
    main()
