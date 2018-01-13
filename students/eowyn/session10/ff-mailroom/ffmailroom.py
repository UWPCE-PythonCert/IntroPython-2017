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
        return round(sum(self.donations), 2)

    @property
    def count_donations(self):
        return len(self.donations)

    @property
    def most_recent_donation(self):
        return round(self.donations[-1], 2)

    @property
    def average_donation(self):
        return round(self.sum_donations / self.count_donations, 2)


class Transactions():
    # Collect list of Donor objects and generate reports

    def __init__(self):
        self.all_donors = []

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
        for i in self.all_donors:
            if i.name == name:
                return i

    def list_names(self):
        return ("Donor Names:\n" +
                '\n'.join([i.name for i in self.all_donors]))

    def generate_report_data(self):
        names = [i.name for i in self.all_donors]
        totals = [i.sum_donations for i in self.all_donors]
        counts = [i.count_donations for i in self.all_donors]
        averages = [i.average_donation for i in self.all_donors]
        report_data = list(zip(names, totals, counts, averages))
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
        total = 0
        for i in self.all_donors:
            total += i.sum_donations
        return total

    def challenge(self, factor, min_donation=0,
                  max_donation=float('inf')):
        if self.total_donations == 0:
            return 0
        new_transactions = copy.deepcopy(self)
        for i in new_transactions.all_donors:
            i.filter_donations(min_donation, max_donation)
        return (factor - 1) * new_transactions.total_donations




class Mailroom():

    # --------------------------------------------------------------
    # Following are helper functions to control program flow
    # -------------------------------------------------------------------

    def safe_input(self):
        return None

    def quit_code(self):
        sys.exit()

    def return_to_menu(self):
        ''' Return True to trigger exit out of sub-loop'''
        return True

    # --------------------------------------------------------------
    # Following are helper functions for accepting and responding to
    # keyboard input
    # ----------------------------------------------------------------

    def __init__(self, transactions):
        self.transactions = transactions

    def update_donors(self):
        '''
        Add new donation to DONORS; if new donor, add to DONOR.
        Then print a thank-you note for the donation.
        '''
        try:
            (fullname, amount) = self.collect_donor_input()
        except TypeError:
            pass
        else:
            letter = self.transactions.add_donor(fullname, amount)
            print(letter)

    def collect_donor_input(self):
        ''' Get name and donation amount to add to DONORS'''
        fullname = input("Enter a donor name (new or existing):\n")
        try:
            amount = float(input("Donation amount: "))
            return (fullname, amount)
        except ValueError:
            print("Invalid Numeric Input!")

    def get_user_input(self, prompt_string):
        ''' Print a prompt_string, return keyboard input if no exceptions'''
        try:
            answer = input(prompt_string)
        except (EOFError, KeyboardInterrupt, TypeError):
            return None
        else:
            return answer

    def select_action(self, arg_dict, answer):
        ''' Execute an action from arg_dict that corresponds to answer.
        Return None if action was executed and False if an error occurs'''
        try:
            return arg_dict[answer]()
        except (KeyError):
            return False

    def list_donors(self):
        print(self.transactions.list_names())

    def generate_table(self):
        self.transactions.print_donor_records()

    def generate_projection(self):

        try:
            (factor, min_donation, max_donation) = self.collect_challenge_input()
        except TypeError:
            return
        else:
            if self.transactions.total_donations == 0:
                print("Too few donations to compute projection.")
                return
            else:
                amount = self.transactions.challenge(factor, min_donation, max_donation)
                #  This code is broken somehow:
                print(dedent('''Projected contribution needed to match
                            donations between ${0:.2f} - ${1:.2f}
                            by a multiplier of {2} is total of: ${3:.2f}
                            '''.format(min_donation, max_donation,
                                       factor, amount)))
                return

    def collect_challenge_input(self):
        ''' Get factor and filter params for challenge/matching'''
        try:
            factor = float(input("Enter a match multiplier:\n"))
            min_donation = float(input("Min donation amount:\n"))
            max_donation = float(input("Max donation amount:\n"))
            return (factor, min_donation, max_donation)
        except ValueError:
            print("Invalid Numeric Input!")
    # --------------------------------------------------------------
    # Following are primary actions called by MAINLOOP
    # --------------------------------------------------------------

    def send_letters(self):
        ''' Send thank you notes to everyone in the DONORS dict'''
        for donor in self.transactions.all_donors:
            outfile = donor.name.replace(" ", "_") + '.txt'
            with open(outfile, 'w') as f:
                f.write(donor.generate_letter())
        print("Successfully saved letters for each donor.")

    def run_interactive_loop(self, arg_dict, prompt_string):
        while True:
            answer = self.get_user_input(prompt_string)
            if answer:
                result = self.select_action(arg_dict, answer)
                if result:
                        return

    def thank_you_loop(self):
        ''' Primary loop to update and thank DONORS
        update DONORS, print donor names, or return to main menu
        '''
        arg_dict = {"1": self.update_donors,
                    "2": self.list_donors,
                    "3": self.return_to_menu}
        prompt_string = """To send a thank you, select one:\n
        (1) Update donor and send thank-you\n
        (2) List all existing DONORS\n
        (3) Return to main menu\n >"""
        self.run_interactive_loop(arg_dict, prompt_string)

    def print_report_loop(self):
        ''' Primary reporting loop
        "generate report table" or "return to main menu"
        '''
        arg_dict = {"1": self.generate_table, "2": self.return_to_menu}
        prompt_string = """Select one:\n
        (1) Generate a summary report\n
        (2) Return to the main menu\n"""
        self.run_interactive_loop(arg_dict, prompt_string)

    def projections_loop(self):
        '''
        Create projected amount to match past donations given
        a multiplying factor and a range of donations
        '''
        arg_dict = {"1": self.generate_projection,
                    "2": self.return_to_menu}
        prompt_string = """Select one:\n
        (1) Generate a projected "challenge" amount\n
        (2) Return to the main menu\n"""
        self.run_interactive_loop(arg_dict, prompt_string)
    # --------------------------------------------------------------
    # The MAINLOOP to control the entire program
    # -------------------------------------------------------------------

    def mainloop(self):
        ''' main interactive loop
        "send a thank you" "create a report" or "quit"
        '''
        arg_dict = {"1": self.thank_you_loop,
                    "2": self.print_report_loop,
                    "3": self.send_letters,
                    "4": self.projections_loop,
                    "5": self.quit_code}
        prompt_string = """Select from one of these options: \n
        (1) Add/Update Donor and Send a Thank You\n
        (2) Create a Report\n
        (3) Send letters to everyone\n
        (4) Generate projection amount to match existing donations\n
        (5) Quit\n>"""
        self.run_interactive_loop(arg_dict, prompt_string)


if __name__ == "__main__":
    Mailroom(Transactions()).mainloop()
