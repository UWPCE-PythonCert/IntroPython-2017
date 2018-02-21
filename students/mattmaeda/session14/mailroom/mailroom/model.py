#!/usr/bin/env python
"""
Data model for mailroom package
"""

import json

THANK_YOU_LETTER = """
Dear {0:s},

Thank you for your donation of ${1:.2f}.
"""

REPORT_HEADER = "{donor: <50}| {total: <12}| {num: <10}| {avg: <12}"
REPORT_LINE = "{0: <50} ${1: 12.2f}{2: 12d}{3: 14.2f}"


class Donor(object):
    """
    Donor class responsible for handling donor information
    """
    _donorname = None

    def __init__(self, donor_name, initial_donations=None):
        self.name = donor_name
        if initial_donations is None:
            initial_donations = []
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


    @property
    def total_donations(self):
        """ donation getter """
        return sum(self.donations)


    @property
    def avg_donations(self):
        """ get average donations """
        return self.total_donations / len(self.donations)


    @property
    def num_donations(self):
        """ get number of donations """
        return len(self.donations)


    @property
    def last_donation(self):
        """ get the last donation made by donor """
        try:
            return self.donations[-1]
        except IndexError:
            return None


    def add_donation(self, amount):
        """ add donation to the list of donations """
        self.donations.append(amount)


class DonorDB(object):
    """
    Database that holds all donor information
    """

    def __init__(self, donors=None):
        if donors is None:
            donors = {}
        self.donor_data = {d.name: d for d in donors}


    def save_to_file(self, filename):
        """
        output donor information to file
        """
        output = {k: v.donations for k, v in self.donor_data.items()}
        with open(filename, "w") as outfile:
            json.dump(output, outfile)


    @classmethod
    def load_from_file(cls, filename):
        """
        Load DB from JSON file
        """
        with open(filename) as infile:
            donors = json.load(infile)

        return cls([Donor(*d) for d in donors.items()])


    @property
    def donors(self):
        """
        get donation values
        """
        return self.donor_data.values()


    def get_donor(self, name):
        """
        get donor by name

        :param name: name

        :return: donor object; None if not found
        :rtype: Donor
        """
        return self.donor_data.get(name)


    def add_donor(self, name):
        """
        Add new donor to DB

        :param name: donor name

        :return: donor object
        :rtype: Donor
        """
        donor = Donor(name)
        self.donor_data[name] = donor
        return donor


    @staticmethod
    def send_letter(donor):
        """
        Generate thank you letter

        :param donor: donor object

        :return: formatted thank you letter
        :rtype: String
        """
        return THANK_YOU_LETTER.format(donor.name, donor.last_donation)


    def get_donor_report(self):
        """
        Generate sorted list of donors from largest donation total to the least

        :return: formatted donation report
        :rtype: String
        """
        donor_dict = {}

        for donor in self.donor_data.values():
            donor_dict.setdefault(donor.total_donations, []).append(donor)

        report = "\n"
        report += (REPORT_HEADER.format(donor="Donor Name",
                                        total="Total Given",
                                        num="Num Gifts",
                                        avg="Average Gift"))
        report += "\n"
        report += "-" * 90
        report += "\n"


        for amount in reversed(sorted(donor_dict)):
            for donor in donor_dict[amount]:
                report += (REPORT_LINE.format(donor.name,
                                              donor.total_donations,
                                              donor.num_donations,
                                              donor.avg_donations))
                report += "\n"

        report += "\n\n"
        return report
