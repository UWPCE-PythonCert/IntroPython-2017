#! /usr/bin/env python

# mailroom.py
# The program: has a data structure that
# holds a list of donors and a history of the amounts
# they have donated.
# Prompt the user to choose from a menu of 3 actions: “Send a Thank You”,
# “Create a Report” or “quit”)
# Sending a Thank You:
# If the user selects ‘Send a Thank You’, prompt for a Full Name.
# If the user types ‘list’, show them a list of the donor names and re-prompt
# If the user types a name not in the list, add that name to the data structure
# and use it.
# If the user types a name in the list, use it.
# Once a name has been selected, prompt for a donation amount.
# Turn the amount into a number – it is OK at this point for the program to
# crash
# if someone types a bogus amount.
# Once an amount has been given, add that amount to the donation history of the
# selected user.
# Use string formatting to compose an email thanking the donor for their
# generous donation. Print the email to the terminal and return to the original
# prompt.
# It is fine (for now) to forget new donors once the script quits running.
# Creating a Report:# If the user selected “Create a Report”, print a list of
# your donors, sorted by total historical donation amount.
# Include Donor Name, total donated, number of donations and average donation
# amount
# as values in each row. Print out the summary info.
# Using string formatting, format the output rows as nicely as possible.
# The end result should be tabular (values in each column should align with
# those above and below)
# After printing this report, return to the original prompt.
# At any point, the user should be able to quit their current task and return
# to the original prompt.
# From the original prompt, the user should be able to quit the script cleanly

from textwrap import dedent
import sys
import math


def get_donor_db():
    return {'william gates iii': ("William Gates III", [653772.32, 12.17]),
            'jeff bezos': ("Jeff Bezos", [877.33]),
            'paul allen': ("Paul Allen", [663.23, 43.87, 1.32]),
            'mark zuckerberg': ("Mark Zuckerberg",
                                [1663.23, 4300.87, 10432.0]),
            }


donor_db = get_donor_db()


class Donor():
    def list_donors(self):
        """
        Create a list of the donors as a string, so they can be printed
        """
        listing = ["Donor list:"]
        for donor in donor_db.values():
            listing.append(donor[0])
        return "\n".join(listing)

    def find_donor(self, name):
        """
        find a donor in the donor db

        :param: the name of the donor

        :returns: The donor data structure -- None if not in the donor_db
        """
        key = name.strip().lower()
        return donor_db.get(key)

    def gen_letter(self, donor):
        """
        Generate a thank you letter for the donor

        :param: donor tuple

        :returns: string with letter
        """
        return dedent('''Dear {0:s},

              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team
              '''.format(donor[0], donor[1][-1]))

    def add_donor(self, name):
        """
        Add a new donor to the donor db

        :param: the name of the donor

        :returns: the new Donor data structure
        """
        name = name.strip()
        donor = (name, [])
        donor_db[name.lower()] = donor
        return donor

    def generate_donor_report(self):
        """
        Generate the report of the donors and amounts donated.

        :returns: the donor report as a string.
        """
        # First, reduce the raw data into a summary list view
        report_rows = []
        for (name, gifts) in donor_db.values():
            total_gifts = sum(gifts)
            num_gifts = len(gifts)
            avg_gift = total_gifts / num_gifts
            report_rows.append((name, total_gifts, num_gifts, avg_gift))

        # sort the report data
        report_rows.sort()
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)
        for row in report_rows:
            report.append(
                "{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
        return "\n".join(report)

    def save_letters_to_disk(self):
        """
        make a letter for each donor, and save it to disk.
        """
        for donor in donor_db.values():
            letter = self.gen_letter(donor)
            # I don't like spaces in filenames...
            filename = donor[0].replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)

    def print_donor_report(self):
        print(self.generate_donor_report())


class Usr_input(Donor):
    '''
    All of the user input associated actions have been put here.
    '''

    def main_menu_selection(self):
        """
        Print out the main application menu and then read the user input.
        """
        action = input(dedent('''
          Choose an action:

          1 - Send a Thank You
          2 - Create a Report
          3 - Send letters to everyone
          4 - Quit

          > '''))
        return action.strip()

    def send_thank_you(self):
        """
        Execute the logic to record a donation and generate a thank
        you message.
        """
        # Read a valid donor to send a thank you from, handling special
        # commands to let the user navigate as defined.
        while True:
            name = input(
                "Enter a donor's name (or list to see all donors"
                "or 'menu' to exit)> ").strip()
            if name == "list":
                print(Donor.list_donors(self))
            elif name == "menu":
                return
            else:
                break

        # Now prompt the user for a donation amount to apply. Since this is
        # also an exit point to the main menu, we want to make sure this is
        # done before mutating the db.
        while True:
            amount_str = input(
                "Enter a donation amount (or 'menu' to exit)> ").strip()
            if amount_str == "menu":
                return
            # Make sure amount is a valid amount before leaving the input loop
            try:
                amount = float(amount_str)
                # extra check here -- unlikely that someone will type
                # "NaN", but it IS possible, and it is a valid floating
                # point number:
                # http://en.wikipedia.org/wiki/NaN
                if math.isnan(amount) or math.isinf(amount)\
                   or round(amount, 2) == 0.00:
                    raise ValueError
            # in this case, the ValueError could be raised by the
            # float() call, or by the NaN-check
            except ValueError:
                print("error: donation amount is invalid\n")
            else:
                break

        # If this is a new user, ensure that the database has the necessary
        # data structure.
        donor = Donor.find_donor(self, name)
        if donor is None:
            donor = Donor.add_donor(self, name)

        # Record the donation
        donor[1].append(amount)
        print(Donor.gen_letter(self, donor))

    def quit(self):
        sys.exit(0)


if __name__ == "__main__":
    donor_db = get_donor_db()
    input_obj = Usr_input()
    donor_obj = Donor()
    # running = True
    selection_dict = {"1": input_obj.send_thank_you,
                      "2": donor_obj.print_donor_report,
                      "3": donor_obj.save_letters_to_disk,
                      "4": input_obj.quit}
    while True:
        selection = input_obj.main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")
