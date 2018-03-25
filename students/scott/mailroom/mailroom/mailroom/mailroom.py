#!/usr/bin/env python3

"""this program will store donor information,
and allow users to send a thank you to a specific donor,
create a report of donations, or quit the program"""

from textwrap import dedent  # nifty utility!
import math

donors_list = {
    "Paul": [100000, 1200000, 750000, 25000],
    "Clark": [20000, 43126],
    "Jerry": [1292, 6788, 128, 9827],
    "Arthur": [11, 2000000, 1000001, 45],
    "Martha": [50, 100],
    "Jim": [4567, 1999, 43213]
}


def bad_input(response):
    print("Invalid entry. Please select 1, 2 or 3 '{}'".format(response))


def note():
    donor = input("Who has made the donation?: ")
    if donor not in donors_list:
        donors_list[donor] = []

    donation = input("How much did they donate?: ")
    donors_list[donor].append(int(donation))

    print("Dear {},\nMuch thanks for your "
          "generous donation of ${}.\n\n".format(donor, donation))
    print("Your contribution will enable future generations to autonomize their day-to-day lives, without being ruthlessly slaughtered by the AI they create.")
    print()
    print(" We look forward to interacting with you in the future!")
    print()
    print("Sincerely, ")
    print("Dr. Egbert P. Sloanbody III")


def report():
    print("\n\n")
    print("{msg1: <50}| {msg2: <12}| "
          "{msg3:<10}| {msg4: <12}".format(msg1="Donor Name",
                                           msg2="Total Given",
                                           msg3="Num Gifts",
                                           msg4="Average Gift"))
    print("-" * 90)
    for donor in _get_sorted_donors():
        money = donors_list[donor]
        total = sum(money)
        num = len(money)
        avg = total/num
        print("{d: <50} ${t: 12.2f}{n: 12d}{a: 14.2f}".format(d=donor,
                                                              t=total,
                                                              n=num,
                                                              a=avg))
    print("\n\n")


def _get_sorted_donors():
    totals = {}
    sorted_donors = []
    for d in donors_list.keys():
        total = sum(donors_list[d])
        if total in totals:
            totals[total].append(d)
        else:
            totals[total] = [d]

    for total in reversed(sorted(totals.keys())):
        sorted_donors += totals[total]

    return sorted_donors


if __name__ == "__main__":
    quit = False

    while not quit:
        print("")
        print("1. Send a Thank You")
        print("2. Create a Report")
        print("3. Quit Program")
        print("")
        response = input("Enter your selection: ")

        try:
            choice = int(response)
            if choice < 0 or choice > 3:
                bad_input(choice)

            elif choice == 1:
                note()
            elif choice == 2:
                report()
            else:
                quit = True

        except ValueError:
            bad_input(response)
