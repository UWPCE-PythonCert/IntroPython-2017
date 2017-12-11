#!/usr/bin/env python3
"""
Mailroom project for Intro to Python Class
"""

class Donor(object):
    """ Donor class responsible for handling donor information
    """
    _donorname = None

    def __init__(self, donor_name):
        self.name = donor_name
        self.donations = []


    @property
    def name(self):
        """ donor name getter """
        return self._donorname


    @name.setter
    def name(self, donor_name):
        """ donor name setter
        :param donor_name: donor name
        :type: str
        """
        self._donorname = donor_name


    def get_donations(self):
        """ donation getter """
        return self.donations


    def add_donation(self, amount):
        """ add donation to list of donations
        :param amount: donation amount
        :type: int
        """
        self.donations.append(amount)


    def get_donation_total(self):
        """ return total amount of donations by donor """
        return sum(self.donations)


    def get_total_donations(self):
        """ return total number of donations by donor """
        return len(self.donations)


    def get_average_donation(self):
        """ return the average donation amount
        :return: average donation if there are donations; 0 if not
        :rtype: float or int
        """
        if self.get_total_donations() != 0:
            return self.get_donation_total()/self.get_total_donations()
        else:
            return 0



REPORT_HEADER = "{donor: <50}| {total: <12}| {num: <10}| {avg: <12}"
REPORT_LINE = "{0: <50} ${1: 12.2f}{2: 12d}{3: 14.2f}"

class Mailroom(object):
    """ Mailroom class responsible for handling donation records
    """
    def __init__(self):
        self.donors = []
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


    def add_donation(self, donor_name, donation):
        """ adds a new donation to tracked donations
        :param donor_name: name of donor
        :type: str

        :param donation: amount of the donation
        :type: int

        :return: thank you letter
        :rtype: str
        """
        donor = self.get_or_initialize_donor(donor_name)
        donor.add_donation(donation)
        return self.send_thanks(donor)


    def get_or_initialize_donor(self, donor_name):
        """ returns donor object from existing donor list or
            creates and returns new donor object
        :param donor_name: name of donor
        :type: str

        :return: donor object
        :rtype: Donor
        """
        donor = None

        for donor_obj in self.donors:
            if donor_obj.name == donor_name:
                donor = donor_obj
                break

        if donor is None:
            donor = Donor(donor_name)
            self.donors.append(donor)

        return donor


    def send_thanks(self, donor):
        """ Returns thank you letter given a donor and donation
        :param donor: donor object for donor
        :type: Donor object

        :return: thank you letter
        :rtype: str
        """
        return "\n\nDear {},\nThank you for your donation of " \
               "{}.\n\n".format(donor.name, donor.get_donations()[-1])


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

        report += ("\n".join(REPORT_LINE.format(donor.name,
                                                donor.get_donation_total(),
                                                donor.get_total_donations(),
                                                donor.get_average_donation())
                            for donor in self.sort_donors_by_donation()))


        report += "\n\n"
        return report


    def sort_donors_by_donation(self):
        """ Returns list of donors sorted by descending donation amounts
        :return: list of donors sorted by donation amounts
        :rtype: list
        """
        donor_dict = {}

        for donor in self.donors:
            donor_dict.setdefault(donor.get_donation_total(), []).append(donor)

        donors = []

        for amount in reversed(sorted(donor_dict)):
            donors += donor_dict[amount]

        return donors


if __name__ == "__main__":
    DONORS = {
        "George Washington": [1],
        "John Adams": [3],
        "Thomas Jefferson": [3],
        "John Quincy Adams": [2],
        "James Madison": [1]
    }

    mailroom_obj = Mailroom()

    menu = mailroom_obj.get_menu()
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
                name_of_donor = input("Enter full name: ")
                donation_amount = input("Enter a donation amount: ")
                print(mailroom_obj.add_donation(name_of_donor,
                                                int(donation_amount)))
            elif choice == 2:
                print(mailroom_obj.report())
            else:
                QUIT = True

        except ValueError:
            print("Invalid choice '{}'".format(choice))
