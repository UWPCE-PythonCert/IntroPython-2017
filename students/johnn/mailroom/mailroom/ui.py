#!/usr/bin/env python3

"""
menu system for donor program
"""

import sys
from mailroom import security
from mailroom.donors import Donors, Donor, save_donor_file, load_donor_file
import logging

# 2018-02-11T00:04:31.921864-06:00
log_level = logging.DEBUG
logging.basicConfig(filename='donor.log',
                    filemode='a',
                    format='%(asctime)s %(levelname)s %(module)s %(user)s %(message)s',
                    level=log_level)

def safe_input(prompt=">"):
    """ Generic input routine. """
    # return null if anything goes wrong
    try:
        selection = input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        # don't exit the program on ctrl-c, ctrl-d
        selection = ""
    return selection


def print_lines(lines=2, dest=sys.stdout):
    """ Print variable number of linefeeds for clarity. """

    for _ in range(lines):
        print("", file=dest)


def user_login():
    """ stub for user login """
    security.user = safe_input("Enter your username: ")
    logging.debug("user logged in", extra={ 'user': security.user})


def user_logout():
    """ stub for user logout """
    logging.debug("user logged out", extra={ 'user': security.user})
    security.user = None


def list_donors(donors, dest=sys.stdout):
    """
    provide a formatted list of donors
    """

    # print report header
    #      index    name   total gvn #gifts  avg gift
    print("{0:20} | {1:14} | {2:9} | {3:12}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift"), file=dest)
    print("-"*72, file=dest)

    for _, did, _, _ in donors:

        donor = donors.get_donor(did)

        #                 name     total gvn    #gifts    avg gift
        print("{0:20}  ${1:14,.2f}   {2:9.0f}  ${3:12,.2f}".format(
            donor.full_name,
            donor.total_donations,
            donor.number_donations,
            donor.average_donations), file=dest)
    logging.debug("listed donors", extra={ 'user': security.user})


def get_donation_amount(donor):
    """ Get a donation. """

    menu = "\n"
    menu += "GIFT ENTRY (ammount)\n"
    menu += "-----------------------\n"
    menu += "\n"
    menu += "Enter the numeric amount {informal_name} has donated or\n"
    menu += "(q)uit to return to cancel the donation and\n"
    menu += "return to the previous menu.\n"
    menu += "\n"

    amount = 0
    while amount == 0:

        print_lines()

        selection = safe_input("Donation amount or (q)uit: ")

        # let them bail if they want
        if selection.lower() in ["q", "quit"]:
            return None

        # protect against non numeric input
        try:
            amount = float(selection)
            return amount
        except ValueError:
            print_lines()
            print("The value must be numeric.  Please try again or (q)uit.")


def create_thank_you(donor, hint="wonderful"):
    """ Create a thank you letter. """

    letter = "\n"
    letter += "Dearest {},\n"
    letter += "\n"
    letter += "We are are grateful for the generious donation on the behalf\n"
    letter += "of the {} family.\n"
    letter += "\n"
    letter += "It is through the donations of {} patrions like yourself that\n"
    letter += "allows us to continue to support the community.\n"
    letter += "\n"
    letter += "Sincerely,\n"
    letter += "\n"
    letter += "Tux Humboldt\n"
    letter += "Shark Loss Prevention Institue\n"

    logging.debug("created thank you letter for {}".format(donor.full_name),
        extra={ 'user': security.user})
    return letter.format(donor.full_name, donor.last_name, hint)


def print_thank_you(donor, hint="wonderful", dest=sys.stdout):
    """ Print a thank you letter. """

    # TODO switch to write
    letter = create_thank_you(donor, hint)

    print_lines(2, dest)
    print("-"*80, file=dest)

    print(letter, file=dest)

    print("-"*80, file=dest)
    print_lines(2, dest)


def data_entry(donors):
    """ Enter new donation and send thank you. """

    menu = "\n"
    menu += "DONATION ENTRY (Donor Name)\n"
    menu += "---------------------------\n"
    menu += "\n"
    menu += "Enter the full name (first last) of the donor\n"
    menu += "for whom you would like to enter a donation,\n"
    menu += "(l)ist to see a list of the existing donors, or\n"
    menu += "(q)uit to return to the previous menu.\n"
    menu += "\n"

    while True:

        print_lines()

        print(menu)
        selection = safe_input("Donor Name, (l)ist or (q)uit: ")

        # check for a quit directive
        if selection.lower() in ["q", "quit"]:
            return

        # check for a list directive
        if selection.lower() in ["l", "list"]:
            list_donors(donors)
            continue

        # protect against no entry
        if not selection:
            continue

        # reject blatantly bad input
        if len(selection.split()) < 2:
            print("You must enter both a first and last name.")
            continue

        # find any records that match the input
        matches = donors.match_donor(selection)

        if not matches:
            # if there are no matches, go ahead and create a donor record
            donor = Donor(full_name=selection)
            donors.add_donor(donor)
            hint = "new"

        if len(matches) == 1:
            # if there is an exact match, let's use that one
            donor = donors.get_donor(matches[0][1])
            hint = "existing"

        # TODO: Add confirmation logic and allow them to ignore a current
        #       record and add a new record anyway.

        # prompt for new donation, cancel if None returned
        new_donation = get_donation_amount(donor)
        if new_donation is None:
            print_lines()
            print("Donation cancelled!")
            return

        # update the donor with the new donation
        donor.add_donation(new_donation)

        # thank the donor for the new donation
        print_thank_you(donor, hint)


def thank_all_donors(donors, dest_override=None):
    """ loop through donors, open file, print a thank you letter. """

    for _, did, _, _ in donors:

        donor = donors.get_donor(did)

        file_name = "_".join(
            filter(None, ["thank_you",
                          donor.last_name,
                          donor.suffix,
                          donor.first_name])).lower()
        file_name = file_name.replace(" ", "_")
        if not dest_override:
            dest = open(file_name, "w")
        else:
            dest = dest_override
        print_thank_you(donor, "wonderful", dest)
        if not dest_override:
            dest.close()


def main(donors):
    """ Main menu / input loop. """

    menu = "\n"
    menu += "DONATION WIZARD MAIN MENU\n"
    menu += "-------------------------\n"
    menu += "\n"
    menu += "Select from the following:\n"
    menu += "\n"
    menu += "(L)ist Donors\n"
    menu += "(E)nter/(A)dd Donation\n"
    menu += "(P)rint Donor Letters\n"
    menu += "(Q)uit\n"
    menu += "(U)ser login\n"
    menu += "User log(O)ut\n"
    menu += "\n"

    selection = None
    while selection not in ["0", "quit", "q"]:

        if security.user:
            user_hint = security.user.title()
        else:
            user_hint = "Guest User"

        print_lines()

        print(menu)
        selection = safe_input("{} (l)ist, (e)nter, (q)uit: ".format(
            user_hint)).lower()

        if selection in ["u", "login"]:
            user_login()

        if selection in ["o", "logout"]:
            user_logout()

        if selection in ["l", "list"]:
            list_donors(donors)

        if selection in ["p", "print"]:
            thank_all_donors(donors)

        # accept either send or enter
        if selection in ["s", "send", "e", "enter", "a", "add"]:
            if security.user:
                data_entry(donors)
            else:
                print("log in to edit")

        if selection in ["d", "debug"]:
            print_lines()
            print(str(donors))
            print_lines()

        if selection in ["q", "quit"]:
            saved = save_donor_file(donors)
            if saved:
                print("{} donor records saved.".format(len(
                    donors.full_name_index)))
            else:
                print("Please resolve the issues with the donor file before "
                      "exiting.")
                # if you are testing, don't get stuck in the loop
                shall_abort = safe_input("Enter 'exit' to quit anyways and "
                                         "abandon changes:")
                if 'exit' not in shall_abort:
                    # if they don't want to exit, clear the selection
                    # so we don't exit
                    selection = None

    print_lines()
    print("Thank you for using Donation Wizard!")
    print_lines()
