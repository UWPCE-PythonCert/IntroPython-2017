#!/usr/bin/env python3

"""
Kathryn Egan

"""


DONORS = {
    'Benedict Cumberbatch': [200000.0],
    'Elon Musk': [10000.0, 150000.0, 100000.0],
    'Dad': [20.0, 5.0],
    'Donald Trump': [2.81],
    'Alley Joe': [.54, .01, .25]}


def main():
    """ Module that drives main menu."""
    options = {
        '1': {
            'prompt': 'Send a Thank You',
            'module': print_thank_you},
        '2': {
            'prompt': 'Create a Report',
            'module': print_report},
        '3': {
            'prompt': 'Quit',
            'module': exit_program}}
    while True:
        print('Please choose from the following options:')
        prompt = '\n'.join(['{} {}'.format(
            option, options[option]['prompt']) for option in options])
        answer = input(prompt + '\n>')
        if answer in options:
            options[answer]['module']()


def exit_program():
    """ Exits program with a message."""
    from sys import exit
    print('Exiting...')
    exit()


def print_thank_you():
    """ Prompts user for donor name and amount and prints thank
    you note to the console. Donation amount must be numerical."""
    while True:
        name = input(
            'Who donated? (Type LIST to see current list of donors)\n>')
        if name.upper() == 'LIST':
            print()
            print('Current donors:\n' + '\n'.join(sorted(DONORS)))
            print()
            continue
        name = ' '.join(name.split()).title()
        if name not in DONORS:
            DONORS[name] = []
        donation = get_donation()
        DONORS[name].append(donation)
        print('Dear {},'.format(name))
        print('Thank you for your donation of ${:.2f}.'.format(donation))
        print('It will go towards building our new kitten facility.')
        print('We at Miuvenile Care thank you for your support.')
        return


def get_donation():
    """ Prompts user for and returns donation amount.
    Returns:
        float : amount donated"""
    while True:
        donation = input('How much was donated?\n>')
        try:
            donation = donation.strip('$')
            donation = float(donation)
            return donation
        except ValueError:
            print('{} is not a valid amount.'.format(donation))
            print('Please try again.')


def print_report():
    """ Prints a report showing donors and donation data to console."""
    headers = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    data = []
    lengths = [len(item) for item in headers]
    # obtain data and determine ideal column lengths before making report
    for donor in sorted(DONORS, key=by_donation, reverse=True):
        donations = DONORS[donor]
        line = [
            donor, dollar(sum(donations)),
            str(len(donations)), dollar(average(donations))]
        # determine if any item is longer than current longest item
        for index in range(len(line)):
            if len(line[index]) > lengths[index]:
                lengths[index] = len(line[index])
        data.append(line)
    report = []
    report.append(print_header(headers, lengths))
    report.append('-' * (sum(lengths) + 1))
    for row in data:
        report.append(print_data(row, lengths))
    print('\n' + '\n'.join(report) + '\n')


def by_donation(donor):
    """ Returns the sum of the donations for given donor.
    Args:
        donor (str) : donor name
    Returns:
        float : sum of all donations for given donor
    """
    return sum(DONORS[donor])


def average(donations):
    """ Returns average of given donations rounded to 2 decimals.
    Args:
        donations (list of floats) : list of donations
    Returns:
        float : average of donations
    """
    avg = sum(donations) / len(donations)
    return round(avg, 2)


def dollar(amount):
    """ Returns given amount as a string. Adds
    a trailing '0' to any cent amount that is
    divisible by .1 to create a dollar format.
    Args:
        amount (float) : amount to turn into dollar format
    Returns:
        str : amount in dollar format
    """
    dollars, cents = str(amount).split('.')
    if len(cents) == 1:
        cents += '0'
    return '.'.join([dollars, cents])


def pad(string, length, orientation):
    """ Adds leading or trailing whitespace to a string
    up to a given total length. Orientation gives whether
    whitespace should be leading or trailing.
    Args:
        string (str) : string to pad with whitespace
        length (int) : desired length of string after padding
        orientation (str) :
            'leading' if you want leading whitespace
            'trailing' if you want trailing whitespace
    Returns:
        str : string padded with whitespace per specs
    """
    while len(string) < length:
        if orientation == 'trailing':
            string = string + ' '
        elif orientation == 'leading':
            string = ' ' + string
    return string


def print_header(headers, lengths):
    """ Returns the header line as a string.
    Args:
        headers (list of str) : headers
        lengths (list of int) : lengths of columns
    Returns:
        str : headers as a string
    """
    line = []
    orientations = ['trailing', 'leading', 'leading', 'leading']
    for header, length, orientation in zip(headers, lengths, orientations):
        header = pad(header, length, orientation)
        line.append(header)
    line = ' | '.join(line)
    return line


def print_data(row, lengths):
    """ Returns a row in data as a string.
    Args:
        row (list of str) : row in data
        lengths (list of int) : lengths of columns
    Returns:
        str : row of data as string
    """
    line = []
    orientations = ['trailing', 'leading', 'leading', 'leading']
    formats = ['name', 'monetary', 'numerical', 'monetary']
    for item, length, orientation, form in zip(
            row, lengths, orientations, formats):
        item = pad(item, length, orientation)
        # monetary values get WS inserted between $ and number
        if form == 'monetary':
            item = '$' + item + ' '
        # numbers are right oriented with one extra WS in front and back
        elif form == 'numerical':
            item = ' ' + item + ' '
        # names are left oriented with one extra WS trailing
        else:
            item += ' '
        line.append(item)
    return ' '.join(line).strip()


if __name__ == '__main__':
    main()
