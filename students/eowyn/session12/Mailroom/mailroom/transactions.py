#!/usr/bin/env python
import sys
import copy
from textwrap import dedent
from mailroom.donor import Donor
from mailroom.authorized_users import record_user

class Transactions():
    # Collect list of Donor objects and generate reports

    def __init__(self):
        self.all_donors = []

    @record_user
    def add_donor(self, name, amt):
        this_donor = self.get_donor(name)
        if this_donor:
            this_donor.add_donation(amt)
        else:
            this_donor = Donor(name)
            this_donor.add_donation(amt)
            self.all_donors.append(this_donor)
        return this_donor.generate_letter()

    def get_donor(self, name):
        for this_donor in self.all_donors:
            if this_donor.name == name:
                return this_donor

    def list_names(self):
        return ("Donor Names:\n" +
                '\n'.join([i.name for i in self.all_donors]))

    def generate_report_data(self):
        report_data = []
        for this_donor in self.all_donors:
            new_data = (this_donor.name,
                        this_donor.sum_donations,
                        this_donor.count_donations,
                        this_donor.average_donation)
            report_data.append(new_data)
        report_data = sorted(report_data,
                             key=lambda y: int(y[1]),
                             reverse=True)
        return report_data

    def setup_table(self):
        ''' Set up the donor record table headers '''
        headers = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        fs1 = '|'.join(["{:<40}", "{:<12}", "{:<10}", "{:<12}"])
        width = len(fs1.format(*headers))
        head = (fs1.format(*headers)) + '\n'
        head = head + (width * "-") + '\n'
        return head

    def setup_body(self):
        ''' Set up the donor records table body '''
        body = ""
        fs2 = ''.join(["{:<40}", "${:^12.2f}", "{:^12d}", "${:^12.2f}"])
        list_data = self.generate_report_data()
        for i in range(len(list_data)):
            entry = list_data[i]
            body = body + fs2.format(*entry) + '\n'
        return body

    def print_donor_records(self):
        ''' Pretty-print the donor records '''
        print(self.setup_table())
        print(self.setup_body())

    @property
    def total_donations(self):
        return sum( (d.sum_donations for d in self.all_donors) )

    def challenge(self, factor, min_donation=0,
                  max_donation=float('inf')):
        if self.total_donations == 0:
            return 0
        new_transactions = copy.deepcopy(self)
        for i in new_transactions.all_donors:
            i.filter_donations(min_donation, max_donation)
        return (factor - 1) * new_transactions.total_donations