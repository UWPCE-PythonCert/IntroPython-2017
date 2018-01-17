#!/usr/bin/env python
import sys
import copy
from textwrap import dedent


class Donor():
    # Keep track of individual donors and their history of donations

    def __init__(self, name):
        self.donations = []
        self.name = ''.join(name)  # should we check input?

    def add_donation(self, amt):
        self.donations.append(float(amt))

    def generate_letter(self):
        '''
        Generate a formatted thank you note to a donor and return
        the string of the thank you note for printing or writing.
        '''
        fs = "Thank you, {0}, for your generosity and recent gift of ${1:.2f}."
        return fs.format(self.name, self.most_recent_donation)

    def mult_donations(self, factor):
        self.donations = list(map(lambda x: x * factor, self.donations))

    def filter_donations(self, min_donation, max_donation):
        if min_donation > max_donation:
            (min_donation, max_donation) = (max_donation, min_donation)
        self.donations = list(filter(lambda x: x > min_donation and
                                     x < max_donation, self.donations))

    @property
    def sum_donations(self):
        return sum(self.donations)

    @property
    def count_donations(self):
        return len(self.donations)

    @property
    def most_recent_donation(self):
        return round(self.donations[-1], 2)

    @property
    def average_donation(self):
        return round(self.sum_donations / self.count_donations, 2)