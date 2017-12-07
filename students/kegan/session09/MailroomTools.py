"""
Kathryn Egan
"""

import os
import functools


@functools.total_ordering
class Donor:

    def __init__(self, name, *donations):
        self._name = self.normalize_name(name)
        self._donations = self.intake_donations(*donations)

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
    def donations(self, donations):
        self._donations = donations

    @name.setter
    def name(self, name):
        self._name = self.normalize_name(name)

    @property
    def last(self):
        try:
            return self.donations[-1]
        except IndexError:
            pass

    @staticmethod
    def normalize_name(name):
        return ' '.join(name.split()).title()

    @staticmethod
    def intake_donations(*donations):
        processed = []
        for item in donations:
            try:
                item = float(item)
            except ValueError:
                pass
            else:
                processed.append(item)
        return processed

    def pop_last(self):
        last = self.last
        if last:
            self.donations = self.donations[:-1]
        return last

    def thankyou(self, all_donations=False):
        if not self.donations:
            raise ValueError(
                'Error: {} has no donations'.format(self.name))
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

    def add(self, *donations):
        donation = self.intake_donations(*donations)
        self._donations.extend(donation)

    def replace(self, *donations):
        self._donations = self.intake_donations(*donations)

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
    def from_dictionary(cls, dict):
        print(dict)
        donors = [Donor(name, *donations) for name, donations in dict.items()]
        return cls(donors)

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

    def add(self, donor):
        self._donors.append(donor)

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
        for donor in self.donors:
            with open(os.path.join(directory, donor.name + '.txt'), 'w') as f:
                try:
                    thankyou = donor.thankyou(all_donations=True)
                except ValueError:
                    pass
                f.write(thankyou)

    def __getitem__(self, name):
        for donor in self.donors:
            if donor.name == name:
                return donor
        raise ValueError('{} not found'.format(name))

    def replace(self, name, *donations):
        for donor in self.donors:
            if donor.name == name:
                donor.replace(*donations)
                return
        raise ValueError('{} not found'.format(name))

    def update(self, name, *donations):
        for donor in self.donors:
            if donor.name == name:
                donor.add(*donations)
                return
        self.add(Donor(name, *donations))

    def __len__(self):
        return len(self.donors)

    def __contains__(self, donor):
        for d in self.donors:
            if hasattr(donor, 'name'):
                if d == donor:
                    return True
            elif d.name == donor:
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
