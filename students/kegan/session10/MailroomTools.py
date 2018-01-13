"""
Kathryn Egan
"""
import functools


@functools.total_ordering
class Donor:

    def __init__(self, name, *donations):
        """ Initializes Donor object with given name and
        list of donations. Will not accept donations <= 0.
        Will raise ValueError if there are no donations > 0
        in arguments.
        Args:
            name (str) : name of donor
            donations (args) : donations as arguments
        """
        self._name = self.clean_name(name)
        self._donations = self.intake_donations(*donations)
        if not self._donations:
            raise ValueError(
                '{} must have at least one donation > 0'.format(self._name))

    @property
    def name(self):
        """ Returns name of donor.
        Returns:
            str : name of donor
        """
        return self._name

    @property
    def total(self):
        """ Returns total donated.
        Returns:
            float : total donated
        """
        return sum(self.donations)

    @property
    def num(self):
        """ Returns number of donations made.
        Returns:
            int : number of donations made
        """
        return len(self.donations)

    @property
    def average(self):
        """ Returns average donation.
        Returns:
            float : average donation
        """
        return self.total / self.num

    @property
    def donations(self):
        """ Returns donations for this donor.
        Returns:
            list : list of donations
        """
        return self._donations

    @donations.setter
    def donations(self, donations):
        """ Sets donations.
        Args:
            donations (args) : donations as arguments
        """
        self._donations = self.intake_donations(*donations)

    @name.setter
    def name(self, name):
        """ Sets donor name.
        Args:
            name (str) : donor name
        """
        self._name = self.clean_name(name)

    @staticmethod
    def clean_name(name):
        """ Cleans given name.
        Args:
            name (str) : donor name
        Returns:
            str : cleaned name
        """
        return ' '.join(name.split()).title()

    @staticmethod
    def intake_donations(*donations):
        """ Processes given donations and returns
        list of donations that are number > 0
        Args:
            donations (args) : donations as arguments
        Returns:
            list : donations > 0 as list
        """
        processed = []
        for item in donations:
            try:
                item = float(item)
            except ValueError:
                pass
            else:
                if item > 0:
                    processed.append(item)
        return processed

    def thank(self, all_donations=False):
        """ Returns personalized thank you message for this donor.
        Thanks donor for all donations if all_donations is True.
        Args:
            all_donations (bool) : thank donor for all donations
        Returns:
            str : thank you message for donor
        """
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
        """ Adds passed donations to this donor.
        Args:
            donations (args) : donations as arguments
        """
        donations = self.intake_donations(*donations)
        self._donations.extend(donations)

    def __str__(self):
        """ Returns this donor as a string.
        Returns:
            str : donor as string
        """
        donations = ', '.join([
            '${:,.2f}'.format(d) for d in self.donations])
        return '{}: {}'.format(self.name, donations)

    def __repr__(self):
        """ Returns representation of this donor.
        Returns:
            str : representation of this donor
        """
        donations = ', '.join([
            str(d) for d in self.donations])
        return 'Donor("{}", {})'.format(self.name, donations)

    def __eq__(self, other):
        """ Returns whether this donor is equal to other in
        both name and all donations.
        Args:
            other (Donor) : donor to compare
        Returns:
            bool : True if other donor is equal to this donor
        """
        return (
            self.name == other.name and
            self.donations == other.donations)

    def __lt__(self, other):
        """ Returns whether this donor is less than
        other. Compares name and donations.
        Args:
            other (Donor) : donor to compare
        Returns:
            bool : True if this donor is less than other
        """
        return (
            self.name < other.name and
            self.donations < other.donations)

    def __contains__(self, donation):
        """ Returns whether given donation amount
        has been donated by this donor.
        Args:
            donation (int or float) : donation to search for
        Returns:
            bool :
                True if donation is in donation list
                False otherwise
        """
        return donation in self.donations

    def multiply(self, factor, min_donation=None, max_donation=None):
        donations = map(lambda d: self.apply_factor(
            d, factor, min_donation, max_donation), self.donations)
        return Donor(self.name, *donations)

    @staticmethod
    def apply_factor(d, factor, min_donation, max_donation):
        within_min = True if min_donation is None else d >= min_donation
        within_max = True if max_donation is None else d <= max_donation
        return d * factor if within_min and within_max else d


@functools.total_ordering
class DonorList:

    def __init__(self, *donors):
        """ Initializes list of donors.
        Args:
            donors (args) : donors as arguments
        """
        self._donors = [donor for donor in donors]

    @classmethod
    def from_dictionary(cls, dict):
        """ Returns DonorList from given dictionary.
        Args:
            dict (dic str: list) :
                dictionary of donor names mapped to donations as list
        Returns:
            DonorList : dictionary as DonorList object
        """
        donors = [Donor(name, *donations) for name, donations in dict.items()]
        return cls(*donors)

    @classmethod
    def read_from(cls, filein):
        """ Returns DonorList from given TextIOWrapper object.
        Args:
            filein (TextIOWrapper) : open file
        Returns:
            DonorList : file contents as DonorList object
        """
        donors = []
        for line in filein.readlines():
            line = line.split(',')
            try:
                name = line[0].strip()
            except IndexError:
                continue
            else:
                str_donations = [
                    item.strip().strip('$') for item in line[1:]]
            donations = []
            for d in str_donations:
                try:
                    d = float(d)
                except TypeError:
                    continue
                donations.append(d)
            donors.append(Donor(name, *donations))
        return cls(*donors)

    @property
    def donor_names(self):
        """ Returns donor names as list.
        Returns:
            list of str : list of donor names
        """
        return [donor.name for donor in self.donors]

    @property
    def donors(self):
        """ Returns donors.
        Returns:
            list : list of donors
        """
        return self._donors

    @donors.setter
    def donors(self, donors):
        """ Sets donor list to given donors.
        Args:
            donors (list) : list of donors
        """
        self._donors = donors

    def add(self, donor):
        """ Adds given donor to donor list.
        Args:
            donor (Donor) : donor to add to donor list
        """
        self._donors.append(donor)

    def sort_by(self, key, low_to_high=False):
        """ Returns new DonorList sorted by given key.
        Keys may be one of total, average, or num. Sort
        from low to high if keyword low_to_high is True.
        Args:
            low_to_high (bool) : sort low to high
        Returns:
            DonorList : new DonorList sorted by given key
        """
        functions = {
            'total': lambda donor: donor.total,
            'average': lambda donor: donor.average,
            'num': lambda donor: donor.num}
        if key not in functions:
            raise KeyError('Invalid argument {}'.format(key))
        return DonorList(*sorted(
            self.donors, key=functions[key], reverse=not low_to_high))

    def __getitem__(self, name):
        """ Returns Donor object matching given name.
        Raises ValueError if donor with given name
        does not exist.
        Args:
            name (str) : name to search for
        Returns:
            Donor : donor with name matching given name
        """
        name = Donor.clean_name(name)
        for donor in self.donors:
            if donor.name == name:
                return donor
        raise KeyError('{} not found'.format(name))

    def update(self, donor):
        """ Updates list with given donor. If donor
        with matching name exists, adds given donations
        to existing donor. Otherwise, adds donor.
        Args:
            donor (Donor) : donor to update or add to list
        """
        for d in self.donors:
            if d.name == donor.name:
                d.add(*donor.donations)
                return True
        self.add(donor)

    def __len__(self):
        """ Returns number of donors.
        Returns:
            int : number of donors
        """
        return len(self.donors)

    def __contains__(self, donor):
        """ Returns whether donor list contains
        given donor. If given donor is a Donor
        object, compares name and donations.
        If given donor is a str object, compares
        name only.
        Args:
            donor (Donor or str) : Donor object or donor name
        Returns:
            bool :
                True if given donor or donor name is in donor list
                False otherwise
        """
        for d in self.donors:
            if hasattr(donor, 'name'):
                if d == donor:
                    return True
            elif d.name == donor:
                return True
        return False

    def __iter__(self):
        """ Provides iterator over donor list. """
        for donor in self.donors:
            yield donor

    def __eq__(self, other):
        """ Returns whether this donor list has all the
        same donors as the other donor list.
        Args:
            other (DonorList) : DonorList to compare
        Returns:
            bool : True if both lists share donors, False otherwise
        """
        return list(self) == list(other)

    def __lt__(self, other):
        """ Returns whether this donor list evaluates to
        less than the other donor list.
        Args:
            other (DonorList) : DonorList to compare
        Returns:
            bool : True if this list is less than other, False otherwise
        """
        return list(self) < list(other)

    def __str__(self):
        """ Returns this donor list as a string.
        Returns:
            str : donor list as string
        """
        return 'Donors:\n{}'.format(
            '\n'.join([str(donor) for donor in self.donors]))

    def __repr__(self):
        """ Returns representation of this donor list.
        Returns:
            str : representation of donor list
        """
        return 'DonorList({})'.format(
            ', '.join([repr(donor) for donor in self.donors]))

    def write_to(self, outfile):
        """ Writes donor information to given file.
        Args:
            outfile (TextIOWrapper) : open file
        """
        for donor in self:
            outfile.write('{}'.format(donor.name))
            if not donor.donations:
                outfile.write(',None')
            for donation in donor.donations:
                outfile.write(',{:.2f}'.format(donation))
            outfile.write('\n')

    def report(self):
        """ Returns report showing donor names, totals given,
        number of gifts and average gift.
        Returns:
            str : donor report
        """
        report = []
        columns = [
            ('Donor Name', 20, self.name, lambda d: d.name),
            ('Total Given', 12, self.dollar, lambda d: d.total),
            ('Num Gifts', 10, self.number, lambda d: d.num),
            ('Average Gift', 13, self.dollar, lambda d: d.average)]
        headers = '| '.join([
            c + ' ' * (w - len(c)) for c, w, _, _ in columns])
        report.append(headers)
        report_width = sum([c[1] for c in columns]) + (len(columns) - 1) * 2
        report.append('-' * (report_width - 1))
        for donor in self.sort_by('total'):
            row = [
                form(yld(donor), width)
                for (_, width, form, yld) in columns]
            report.append(' '.join(row))
        return '\n'.join(report)

    @staticmethod
    def name(name, width):
        """ Returns name for use in report.
        Args:
            name (str) : name to process
            width (int) : width of column
        Returns:
            str : processed name
        """
        name = name[:width - 4] + '...' if len(name) > width else name
        return name + ' ' * (width - len(name))

    @staticmethod
    def dollar(d, width):
        """ Returns dollar amount for use in report.
        Args:
            d (float) : dollar amount to process
        Returns:
            str : processed dollar amount
        """
        d = '999,999.99+' if d > 999999.99 else '{:,.2f}'.format(d)
        return '${}{}'.format(' ' * (width - len(str(d)) - 1), d)

    @staticmethod
    def number(n, width):
        """ Returns numerical amount for use in report.
        Args:
            n (float) : numerical amount to process
        Returns:
            str : processed numerical amount
        """
        n = '999,999+' if n > 9999999 else'{:,}'.format(n)
        return ' ' * (width + 1 - len(n)) + n + ' '

    def challenge_all(self, factor, min_donation=None, max_donation=None):
        donors = map(lambda d: d.multiply(
            factor, min_donation, max_donation), self.donors)
        return DonorList(*donors)

    def challenge_donor(
            self, name, factor, min_donation=None, max_donation=None):
        return self[name].multiply(factor, min_donation, max_donation)
