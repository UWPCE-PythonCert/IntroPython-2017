#!/usr/bin/env python3

"""
Kathryn Egan

This program manages donors and their donations for
Miuvenile Care, a charity organizaiton for disadvantaged
kittens.
"""


DONORS = {
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


def main():
    """ Module that drives main menu."""
    options = {
        '1': {
            'prompt': 'Send a Thank You',
            'function': print_thank_you},
        '2': {
            'prompt': 'Create a Report',
            'function': print_report},
        '3': {
            'prompt': 'Write Thank Yous',
            'function': write_thank_yous},
        '4': {
            'prompt': 'Quit',
            'function': exit_program}}
    while True:
        print('Please choose from the following options:')
        prompt = '\n'.join(['{} {}'.format(
            num, option['prompt']) for num, option in options.items()])
        answer = safe_input(prompt + '\n>')
        if answer in options:
            options[answer]['function']()


def safe_input(prompt):
    """ Translates keyboard interrupts and end of file
    errors to exit options to Ensure that program exits gracefully.
    Args:
        prompt (str) : user input
    Returns:
        str : exit option if error is encountered otherwise input
    """
    try:
        answer = input(prompt)
    except (KeyboardInterrupt, EOFError):
        return '4'  # returns the option that quits the program
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
    while True:
        donor = input(
            'Who donated? (Enter LIST to see current list of donors)\n>')
        if not donor:
            continue
        if donor.upper() != 'LIST':
            break
        print()
        print('Current donors:')
        print('\n'.join(sorted(DONORS)))
        print()
    donor = ' '.join(donor.split()).title()
    donation = get_donation()
    DONORS.setdefault(donor, []).append(donation)
    thankyou = get_thank_you(donor, [donation])
    print('-' * 80)
    print(thankyou)
    print('-' * 80)


def get_donation():
    """ Prompts user for and returns donation amount.
    Will passive aggressively make a thank you for a
    zero-dollar amount.
    Returns:
        float : amount donated"""
    while True:
        donation = input('How much was donated?\n>')
        try:
            donation = float(donation.strip('$'))
            return donation
        except ValueError:
            print('{} is not a valid amount.'.format(donation))
            print('Please try again.')


# test written
def get_thank_you(donor, donations):
    """ Returns a thank you message for the donor based
    off given donation if any, otherwise all donations
    in database.
    Args:
        donor (str) : name of donor
        donation (None or float) : specified donation
    Returns:
        str : thank you message for donor
    """
    total = sum(donations)
    num = len(donations)
    # build up elements of thank you message
    substrings = {
        'donor': donor,
        's': 's' if num > 1 else '',
        'and': ' and ' if num > 1 else '',
        'first': ', '.join([
            dollar(d) for d in donations[:-1]]),
        'rest': dollar(donations[-1]),
        'totalling': '' if num < 2 else ', totalling {}{},'.format(
            'an incredible ' if total > 500 else '', dollar(total))}
    message = \
        'Dear {donor},\nThank you for your generous gift{s} of ' +\
        '{first}{and}{rest}. Your donation{s}{totalling} will ' +\
        'go towards feeding homeless kittens in Seattle. ' +\
        'From the bottom of our hearts, we at Miuvenile Care thank you.\n\n' +\
        'Regards,\nBungelina Bigglesnorf\nChairwoman, Miuvenile Care'
    message = message.format(**substrings)
    return message


# test written
def dollar(amount):
    """ Returns amount in dollar format. Removes trailing
    .00s to create a clean amount.
    Args:
        amount (float) : dollar amount to format
    Returns:
        str : dollar amount as a string
    """
    return '${:,.2f}'.format(amount).replace('.00', '')


def print_report():
    """ Prints a report showing donors and donation data to console."""
    report = create_report()
    print()
    print(report)
    print()


# test written
def create_report():
    """ Returns tabular representation of donors, total donations
    per donor, number of donations per donor, and average size
    of gift.
    Returns:
        str : donor data as table
    """
    headers = [
        'Donor Name' + ' ' * 10, 'Total Given', 'Num Gifts', 'Average Gift']
    report = [' | '.join(headers)]
    line_length = sum([len(h) for h in headers]) + len(headers) * 2 + 1
    report.append('-' * line_length)
    for donor in sorted(DONORS, key=by_donation, reverse=True):
        donations = DONORS[donor]
        values = [
            donor, sum(donations), len(donations),
            sum(donations) / len(donations)]
        functions = [
            format_name, format_dollar, format_number, format_dollar]
        row = []
        for header, value, function in zip(headers, values, functions):
            row.append(function(value, len(header)))
        report.append(' '.join(row))
    return '\n'.join(report)


def format_name(donor, width):
    """ Formats donor name for tabular report.
    Any name longer than the column width will be
    truncated with ellipses.
    Args:
        donor (str) : donor name
        width (int) : width of column
    Returns:
        str : donor formatted for column
    """
    donor = donor[:width - 3] + '...' if len(donor) > width else donor
    donor += ' ' * (width + 1 - len(donor))
    return donor


def format_dollar(dollar, width):
    """ Formats dollar for tabular report.
    Any amount equal or greater than 1M will be
    truncated to '$999,999.99+'.
    Args:
        dollar (float) : dollar amount
        width (int) : width of column
    Returns:
        str : dollar amount formated for column
    """
    if dollar > 999999.99:
        return '$999,999.99+'
    dollar = '{:,.2f}'.format(dollar)
    dollar = '${}{}'.format(' ' * (width - len(str(dollar))), dollar)
    return dollar


def format_number(number, width):
    """ Formats number for tabular report.
    Any amount equal ro greater than 1M will
    be truncated to '999,999+'.
    Args:
        number (float) : number to format
        width (int) : width of column
    Returns:
        str : dollar amount formated for column
    """
    if number > 9999999:
        number = '999,999+'
    else:
        number = '{:,}'.format(number)
    number = ' ' * (width + 2 - len(number)) + number + ' '
    return number


def write_thank_yous():
    """ Writes thank yous to all donors in individual
    files in a ThankYous folder in the program's cwd."""
    import os
    print('Writing new thank yous to all donors...')
    for donor in DONORS:
        thankyou = get_thank_you(donor, DONORS[donor])
        if not os.path.exists('ThankYous'):
            os.mkdir('ThankYous')
        with open(os.path.join('ThankYous', donor + '.txt'), 'w') as f:
            f.write(thankyou)
    print('Thank yous written to\n{}'.format(
        os.path.join(os.getcwd(), 'ThankYous')))


def by_donation(donor):
    """ Returns the sum of the donations for given donor.
    Args:
        donor (str) : donor name
    Returns:
        float : sum of all donations for given donor
    """
    return sum(DONORS[donor])


if __name__ == '__main__':
    main()
