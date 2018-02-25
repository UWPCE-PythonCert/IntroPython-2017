#!/usr/bin/env python
"""
models for the mailroom program.

This is where the program logic is.

This version has been made Object Oriented.
"""

# handy utility to make pretty printing easier
from textwrap import dedent

import json
import logging

print('name', __name__)

class Donor:
    """
    class to hold the information about a single donor
    """

    def __init__(self, name, donations=None, logger=None):
        """
        create a new Donor object

        :param name: the full name of the donor

        :param donations=None: iterable of past donations
        """
        # note that if you log to logging here, rather than self.logger,
        # you will be using the root logger, rather than the mailroom.model
        # logger.
        self.logger = logger or logging.getLogger(__name__)
        self.norm_name = self.normalize_name(name)
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)
        try:
            self.logger.info('creating new donor, %s, with %d donations', name, len(donations))
        except TypeError:
            self.logger.info('creating new donor, %s, with no donations', name)
        else:
            [self.logger.debug('%d donation $%.2f', ind+1, amount) for ind, amount in enumerate(donations)]

    @staticmethod
    def normalize_name(name):
        """
        return a normalized version of a name to use as a comparison key

        simple enough to not be in a method now, but maybe you'd want to make it fancier later.
        """
        return name.lower().strip()

    @property
    def last_donation(self):
        """
        The most recent donation made
        """
        try:
            return self.donations[-1]
        except IndexError:
            return None

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def average_donation(self):
        return self.total_donations / len(self.donations)

    def add_donation(self, amount):
        """
        add a new donation
        """
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError("Donation must be greater than zero")
        self.donations.append(amount)

    def gen_letter(self):
        """
        Generate a thank you letter for the donor

        :param: donor tuple

        :returns: string with letter

        note: This doesn't actually write to a file -- that's a separate
              function. This makes it more flexible and easier to test.
        """
        return dedent('''Dear {0:s},

              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team
              '''.format(self.name, self.last_donation)
                      )


class DonorDB:
    """
    encapsulation of the entire database of donors and data associated with them.
    """

    def __init__(self, donors=None, logger=None):
        """
        Initialize a new donor database

        :param donors=None: iterable of Donor objects
        """
        self.logger = logger or logging.getLogger(__name__)
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name: d for d in donors}

    @classmethod
    def load_from_file(cls, filename):
        """
        loads a donor database from a json file
        """
        with open(filename) as infile:
            donors = json.load(infile)
        db = cls([Donor(*d) for d in donors])
        return db

    @property
    def donors(self):
        """
        an iterable of all the donors
        """
        return self.donor_data.values()

    def list_donors(self):
        """
        creates a list of the donors as a string, so they can be printed

        Not calling print from here makes it more flexible and easier to
        test
        """
        listing = ["Donor list:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def find_donor(self, name):
        """
        find a donor in the donor db

        :param: the name of the donor

        :returns: The donor data structure -- None if not in the self.donor_data
        """
        return self.donor_data.get(Donor.normalize_name(name))

    def add_donor(self, name):
        """
        Add a new donor to the donor db

        :param: the name of the donor

        :returns: the new Donor data structure
        """
        print('logger', type(self.logger), self.logger)
        print(repr(self.logger))
        self.logger.info('add a donor')
        donor = Donor(name)
        self.donor_data[donor.norm_name] = donor
        return donor

    @staticmethod
    def sort_key(item):
        # used to sort on name in self.donor_data
        return item[1]

    def generate_donor_report(self):
        """
        Generate the report of the donors and amounts donated.

        :returns: the donor report as a string.
        """
        # First, reduce the raw data into a summary list view
        report_rows = []
        for donor in self.donor_data.values():
            name = donor.name
            gifts = donor.donations
            total_gifts = donor.total_donations
            num_gifts = len(gifts)
            avg_gift = donor.average_donation
            report_rows.append((name, total_gifts, num_gifts, avg_gift))

        # sort the report data
        report_rows.sort(key=self.sort_key)
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)
        for row in report_rows:
            report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
        return "\n".join(report)

    def save_letters_to_disk(self):
        """
        make a letter for each donor, and save it to disk.
        """
        print("Saving letters:")
        for donor in self.donor_data.values():
            print("donor:", donor.name)
            letter = donor.gen_letter()
            # I don't like spaces in filenames...
            filename = donor.name.replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)
