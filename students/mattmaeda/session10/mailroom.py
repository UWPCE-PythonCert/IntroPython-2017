#!/usr/bin/env python3
from functools import partial

"""
Mailroom project for Intro to Python Class
"""

class Donor(object):
    """ Donor class responsible for handling donor information
    """
    _donorname = None

    def __init__(self, donor_name, initial_donations=[]):
        self.name = donor_name
        self.donations = list(initial_donations)


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
            3: "Model Matching Contribution",
            4: "Quit"
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
        for donor_obj in self.donors:
            if donor_obj.name == donor_name:
                return donor_obj

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


    def report(self, donors=None):
        """ Generates a report of donations sorted from greatest to least
        :return: donation report
        :rtype: String
        """
        if donors is None:
            donors = self.donors

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
                            for donor in self.sort_donors_by_donation(donors)))


        report += "\n\n"
        return report


    def sort_donors_by_donation(self, donors):
        """ Returns list of donors sorted by descending donation amounts
        :return: list of donors sorted by donation amounts
        :rtype: list
        """
        donor_dict = {}

        for donor in donors:
            donor_dict.setdefault(donor.get_donation_total(), []).append(donor)

        sorted_donor_list = []

        for amount in reversed(sorted(donor_dict)):
            sorted_donor_list += donor_dict[amount]

        return sorted_donor_list


    def challenge(self, factor, min_donation=None, max_donation=None):
        """ takes the donor's existing donations and applies some multiplier
        against those donations.  If min_donation is set, only apply factor if
        donation is greater than or equal to min_donation.  If max_donation is
        set, only apply factor if donation is less than or equal to
        max_donation.

        :param factor: multiplying factor
        :type: int

        :param min_donation: minimum donation amount to apply factor to
        :type: int

        :param max_donation: maximum donation amount to apply factor to
        :type: int

        :return: original and modelled report
        :rtype: list with original report and model report
        """
        updated_donor_list = list(map(partial(self.model_matching_contribution,
                                              factor=factor,
                                              min_donation=min_donation,
                                              max_donation=max_donation),
                                      self.donors))

        return [self.report(), self.report(donors=updated_donor_list)]


    def model_matching_contribution(self, donor, factor, min_donation,
                                    max_donation):
        """ Takes donations by donor and models the donor based on matching
        contributions

        :param donor: donor
        :type: Donor

        :param: factor the multiplying match
        :type: int

        :param: min_donation: the minimum donation before match takes effect
        :type: int or None

        :param: max_donation: the max a donation will be matched
        :type: int or None

        :return: new donor based on matching donation
        :rtype: Donor
        """
        new_donations = list(map(partial(self.get_donation_match,
                                         factor=factor,
                                         min_donation=min_donation,
                                         max_donation=max_donation),
                                 donor.donations))
        return Donor(donor.name, new_donations)


    def get_donation_match(self, amount, factor, min_donation, max_donation):
        if min_donation is not None and amount < min_donation:
            return amount

        if max_donation is not None and amount > max_donation:
            return amount - max_donation + (factor * max_donation)

        return amount * factor


    def main_switch(self):
        """ The main user interface to the mailroom program.  Queries user for
        desired inputs.
        """
        menu = self.get_menu()
        menu_options = "\n".join(["{}: {}".format(k, menu[k]) for k in
                                  sorted(menu.keys())])

        quit = False

        while not quit:
            print(menu_options)
            response = input("Enter your number choice: ")

            try:
                choice = int(response)
                if choice not in menu:
                    print("Invalid choice '{}'".format(choice))
                elif choice == 1:
                    name = input("Enter full name: ")
                    amount = input("Enter a donation amount: ")
                    print(self.add_donation(name, int(amount)))
                elif choice == 2:
                    print(self.report())
                elif choice == 3:
                    if len(self.donors) == 0:
                        print("\nThere are no donations.  Please enter some " \
                              "donations first.\n\n")
                    else:
                        factor = input("Enter matching multiplier: ")
                        min_d = input("Enter minimum donation (Press " \
                                      "Enter if none): ")
                        max_d = input("Enter maximum donation (Press " \
                                      "Enter if none): ")

                        if min_d == "":
                            min_donation = None
                        else:
                            min_donation = int(min_d)
                        if max_d == "":
                            max_donation = None
                        else:
                            max_donation = int(max_d)

                        reports = self.challenge(int(factor),
                                                 min_donation=min_donation,
                                                 max_donation=max_donation)

                        print("\n\n")
                        print("Current Donations")
                        print("-" * 50)
                        print(reports[0])
                        print("\n\n")
                        print("With Matching Factor: {} Min: {} " \
                              "Max: {}".format(factor, min_donation,
                                               max_donation))
                        print("-" * 50)
                        print(reports[1])
                else:
                    quit = True

            except ValueError:
                print("Invalid choice '{}'".format(response))


if __name__ == "__main__":
    mailroom_obj = Mailroom()
    mailroom_obj.main_switch()
