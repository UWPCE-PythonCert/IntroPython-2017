#!/usr/bin/env python3

"""
Kathryn Egan

This program manages donors and their donations for
Miuvenile Care, a charity organizaiton for disadvantaged
kittens.
"""
import os
import functools


@functools.total_ordering
class Donor:

    def __init__(self, name, donations=[]):
        self._name = self.normalize_name(name)
        self._donations = self.intake_donations(donations)

    @property
    def name(self):
        return self._name

    @property
    def total(self):
        return sum(self.donations)

    @property
    def num(self):
        return len(self.donations)

    @property
    def average(self):
        return self.total / self.num

    @property
    def donations(self):
        return self._donations

    @donations.setter
    def donations(self, donation):
        self._donations = self.intake_donations(donation)

    @name.setter
    def name(self, name):
        self._name = self.normalize_name(name)

    @property
    def last(self):
        if self.donations:
            return self.donations[-1]

    @staticmethod
    def normalize_name(name):
        return ' '.join(name.split()).title()

    @staticmethod
    def intake_donations(donations):
        processed = []
        try:
            donation = float(donations)
        # not a float (is a list - hopefully)
        except TypeError:
            for d in donations:
                processed.append(float(d))
        else:
            processed.append(donation)
        return processed

    def thankyou(self, all_donations=False):
        num = self.num if all_donations else 1
        first = self.donations[:-1] if all_donations else []
        rest = self.donations[-1]
        substrings = {
            'donor': self.name,
            's': 's' if num > 1 else '',
            'and': ' and ' if num > 1 else '',
            'first': ', '.join(['${:,.2f}'.format(d) for d in first]),
            'rest': '${:,.2f}'.format(rest),
            'totalling':
                '' if num < 2 else
                ', totalling {}{},'.format(
                    'an incredible ' if self.total > 500
                    else '', '${:,.2f}'.format(self.total))}
        message = \
            'Dear {donor},\nThank you for your generous gift{s} of ' +\
            '{first}{and}{rest}. Your donation{s}{totalling} will ' +\
            'go towards feeding homeless kittens in Seattle. ' +\
            'From the bottom of our hearts, we at Miuvenile Care thank you.' +\
            '\n\nRegards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care'
        return message.format(**substrings)

    def add(self, donation):
        donation = self.intake_donations(donation)
        self._donations.extend(donation)

    def __str__(self):
        donations = ', '.join([
            '${:,.2f}'.format(d) for d in self.donations])
        return '{}: {}'.format(self.name, donations)

    def __repr__(self):
        donations = '[' + ', '.join([
            str(d) for d in self.donations]) + ']'
        return 'Donor("{}", {})'.format(self.name, donations)

    def __eq__(self, other):
        try:
            return (
                self.name == other.name and
                self.donations == other.donations)
        except AttributeError:
            return self.name == other

    def __lt__(self, other):
        try:
            return (
                self.name < other.name and
                self.donations < other.donations)
        except AttributeError:
            return self.name < other

    def __contains__(self, donation):
        return donation in self.donations


@functools.total_ordering
class DonorList:

    def __init__(self, *args):
        self._donors = [donor for donor in args]

    @classmethod
    def from_file(cls, filein):
        for line in filein.readlines():
            try:
                line = line.split(',')
                name = line[0].strip()
                str_donations = [
                    item.strip().strip('$') for item in line[1:]]
            except ValueError:
                continue
            donations = []
            for d in str_donations:
                try:
                    d = float(d)
                except TypeError:
                    continue
                donations.append(d)
            donor = Donor(name, donations)
            cls.add(donor)

    @property
    def donor_names(self):
        return [donor.name for donor in self.donors]

    @property
    def donors(self):
        return self._donors

    @donors.setter
    def donors(self, donors):
        self._donors = donors

    def get_thankyou(self, name):
        return self[name].thankyou

    def add(self, donor):
        self.donors.append(donor)

    def remove(self, name):
        removed = []
        for donor in self.donors:
            if donor.name == name:
                continue
            removed.append(donor)
        if len(removed) == len(self.donors):
            raise ValueError('{} does not exist'.format(name))
        self.donors = removed

    def sort_by(self, key, low_to_high=False):
        functions = {
            'total': lambda donor: donor.total,
            'average': lambda donor: donor.average,
            'num': lambda donor: donor.num}
        if key not in functions:
            raise KeyError('Invalid argument {}'.format(key))
        return DonorList(*sorted(
            self.donors, key=functions[key], reverse=not low_to_high))

    def write_thankyous(self, directory):
        print('Writing new thank yous to all donors...')
        for donor in self.donors:
            with open(os.path.join(directory, donor.name + '.txt'), 'w') as f:
                f.write(donor.thankyou(all_donations=True))

    def __getitem__(self, name):
        for donor in self.donors:
            if donor.name == name:
                return donor
        raise ValueError('{} not found'.format(name))

    def __setitem__(self, name, donations):
        for donor in self.donors:
            if donor.name == name:
                donor.donations = donations
                return
        raise ValueError('{} not found'.format(name))

    def __len__(self):
        return len(self.donors)

    def __contains__(self, donor):
        try:
            name = donor.name
        except AttributeError:
            name = name
        for d in self.donors:
            if d.name == name:
                return True
        return False

    def __iter__(self):
        for donor in self.donors:
            yield donor

    def __eq__(self, other):
        return list(self) == list(other)

    def __lt__(self, other):
        return list(self) < list(other)

    def __str__(self):
        return 'Donors:\n{}'.format(
            '\n'.join([str(donor) for donor in self.donors]))

    def __repr__(self):
        return 'DonorList({})'.format(
            ', '.join([repr(donor) for donor in self.donors]))


class DonorReport:

    def __init__(self):
        self._columns = [
            'Donor Name', 'Total Given',
            'Num Gifts', 'Average Gift']
        self._widths = [21, 12, 10, 12]

    @property
    def report_width(self):
        return sum([
            len(h) for h in self.columns]) + len(self.columns) * 2 + 1

    def _get_header(self):
        return '| '.join([
            c + ' ' * self.width[i]
            for c, i in zip(self.columns, self.widths)]) +\
            '\n' + '-' * self.report_width

    def _format(self, item, position):
        width = self.widths[position]
        if type(item) is str:
            return self._str(item, width)
        if type(item) is float:
            return self._dollar(item, width)
        return self._number(item, width)

    def _str(self, name, width):
        name = name[:width - 3] + '...' if len(name) > width else name
        return name + ' ' * (width + 1 - len(name))

    def _dollar(self, dollar, width):
        if dollar > 999999.99:
            return '$999,999.99+'
        dollar = '{:,.2f}'.format(dollar)
        return'${}{}'.format(
            ' ' * (width - len(str(dollar))), dollar)

    def _number(self, number, width):
        if number > 9999999:
            return '999,999+'
        number = '{:,}'.format(number)
        return ' ' * (width + 2 - len(number)) + number + ' '

    @classmethod
    def report(self, donors):
        report = [self._get_header()]
        report.append('-' * self.report_width)
        for name in donors.by_donation():
            donor = donors[name]
            items = [donor.name, donor.total, donor.num, donor.average]
            report.append(' '.join([
                self.format(item, position)
                for position, item in enumerate(items)]))
        return '\n'.join(report)


donors = {
    'Benedict Cumberbatch': [200000.0],
    'Elon Musk': [10000.0, 150000.0, 100000.0],
    'Dad': [20.0, 5.0],
    'Donald Trump': [2.81],
    'Billy Neighbor': [.54, .01, .25],
    'Daenerys Stormborn of the House Targaryen, ' +
    'First of Her Name, the Unburnt, ' +
    'Queen of the Andals and the First Men, ' +
    'Khaleesi of the Great Grass Sea, Breaker of Chains, ' +
    'and Mother of Dragons': [100] * 10000000}
DONORS = DonorList(donors)
# DONORS = DonorList.from_file('donations.txt')


def main():
    """ Module that drives main menu."""
    options = {
        'Send a Thank You': print_thank_you,
        'Create a Report': print_report,
        'Write Thank Yous': write_thank_yous,
        # 'Write Donation File': write_donation_file,
        'Quit': exit_program}
    while True:
        print('Please choose from the following options:')
        answer = get_answer(options)
        if answer:
            options[answer]()


def get_answer(options):
    """ Translates keyboard interrupts and end of file
    errors to exit option to ensure that program exits gracefully.
    Args:
        prompt (str) : user input
    Returns:
        str : exit option if error is encountered otherwise input
    """
    prompt = '\n'.join([
        '{} {}'.format(str(i + 1), option)
        for i, option in enumerate(options)]) + '\n>'
    try:
        answer = input(prompt)
        answer = list(options)[int(answer) - 1]
    except (KeyboardInterrupt, EOFError):
        return 'Quit'  # returns the option that quits the program
    except (IndexError, TypeError):
        return
    else:
        return answer


def exit_program():
    """ Exits program."""
    from sys import exit
    print()
    print('Exiting...')
    exit()


def print_thank_you():
    """ Prompts user for donor name and amount and prints thank
    you note to the console. Donation amount must be numerical."""
    donor = get_donor()
    donation = get_donation()
    DONORS.add(donor, donation)
    print('-' * 80)
    print(donor.thankyou)
    print('-' * 80)


def get_donor():
    while True:
        donor = input(
            'Who donated? (Enter LIST to see current list of donors)\n>')
        if not donor:
            continue
        if donor.strip().upper() != 'LIST':
            break
        print()
        print('Current donors:')
        print(DONORS.current_donors)
        print()
    return donor


def get_donation():
    """ Prompts user for and returns donation amount.
    Will passive aggressively make a thank you for a
    zero-dollar amount.
    Returns:
        float : amount donated
    """
    while True:
        donation = input('How much was donated?\n>')
        try:
            donation = float(donation.strip('$'))
            return donation
        except ValueError:
            print('{} is not a valid amount.'.format(donation))
            print('Please try again.')


def print_report():
    """ Prints a report showing donors and donation data to console."""
    print()
    print(DonorReport.report(donors))
    print()


def write_thank_yous():
    """ Writes thank yous to all donors in individual
    files in a ThankYous folder in the program's cwd."""
    directory = 'ThankYous'
    if not os.path.exists(directory):
        os.mkdir(directory)
    DONORS.write_thankyous(directory)
    print('Thank yous written to\n{}'.format(
        os.path.join(os.getcwd(), directory)))


if __name__ == '__main__':
    main()
