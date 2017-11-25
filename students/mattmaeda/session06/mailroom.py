#!/usr/bin/env python3
"""
Mailroom project for Intro to Python Class
"""

REPORT_HEADER = "{donor: <50}| {total: <12}| {num: <10}| {avg: <12}"
REPORT_LINE = "{0: <50} ${1: 12.2f}{2: 12d}{3: 14.2f}"

class Mailroom(object):
    """ Mailroom class responsible for handling donation records
    """
    def __init__(self, donor_dict):
        self.donors = donor_dict
        self.menu = {
            1: "Send a Thank You",
            2: "Create a Report",
            3: "Quit"
        }


    def get_menu(self):
        """ Returns menu options
        :return: menu options
        :rtype: dict
        """
        return self.menu


    def thanks(self, donor, donation):
        """ Returns thank you letter given a donor and donation
        :String donor: name of the donor
        :int donation: amount of donation
        :return: thank you letter
        :rtype: String
        """
        if donor not in self.donors:
            self.donors[donor] = []

        self.donors[donor].append(int(donation))

        return "\n\nDear {},\nThank you for your donation of " \
               "{}.\n\n".format(donor, donation)


    def report(self):
        """ Generates a report of donations sorted from greatest to least
        :return: donation report
        :rtype: String
        """
        report = "\n\n"
        report += (REPORT_HEADER.format(donor="Donor Name",
                                        total="Total Given",
                                        num="Num Gifts",
                                        avg="Average Gift"))
        report += "\n"
        report += "-" * 90
        report += "\n"

        report += ("\n".join([REPORT_LINE.format(d,
                                                 sum(self.donors[d]),
                                                 len(self.donors[d]),
                                                 sum(self.donors[d])/len(self.donors[d]))
                              for d in self._get_sorted_donors()]))

        report += "\n\n"
        return report


    def _get_sorted_donors(self):
        """ Returns list of donors sorted by descending donation amounts
        :return: list of donors sorted by donation amounts
        :rtype: list
        """
        totals = {}
        for donor in self.donors.keys():
            totals.setdefault(sum(self.donors[donor]), []).append(donor)

        sorted_donors = []
        for total in reversed(sorted(totals.keys())):
            sorted_donors += totals[total]

        return sorted_donors


if __name__ == "__main__":
    DONORS = {
        "George Washington": [1],
        "John Adams": [3],
        "Thomas Jefferson": [3],
        "John Quincy Adams": [2],
        "James Madison": [1]
    }

    mailroom = Mailroom(DONORS)

    menu = mailroom.get_menu()
    menu_options = "\n".join(["{}: {}".format(k, menu[k]) for k in
                              sorted(menu.keys())])

    QUIT = False

    while not QUIT:
        print(menu_options)
        response = input("Enter your number choice: ")

        try:
            choice = int(response)
            if choice not in menu:
                print("Invalid choice '{}'".format(choice))
            elif choice == 1:
                donor_name = input("Enter full name: ")
                donation_amount = input("Enter a donation amount: ")
                print(mailroom.thanks(donor_name, donation_amount))
            elif choice == 2:
                print(mailroom.report())
            else:
                QUIT = True

        except ValueError:
            print("Invalid choice '{}'".format(choice))
