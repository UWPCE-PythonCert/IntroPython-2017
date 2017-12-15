#!/usr/bin/env python3

"""
Kathryn Egan

This program manages donors and their donations for
Miuvenile Care, a charity organizaiton for disadvantaged
kittens.
"""
import os
import sys
from MailroomTools import Donor
from MailroomTools import DonorList


donors = {
    'Benedict Cumberbatch': [200000.0],
    'Elon Musk': [10000.0, 150000.0, 100000.0],
    'Dad': [20.0, 5.0],
    'Donald Trump': [2.81],
    'Billy Neighbor': [.54, .01, .25]}
DONORS = DonorList.from_dictionary(donors)

# with open('donor_file.txt', 'r') as fin:
#     DONORS = DonorList.read_from(fin)


def main():
    """ Module that drives main menu."""
    options = {
        'Send a Thank You': print_thank_you,
        'Create a Report': print_report,
        'Project Donations': project_donations,
        'Write Thank Yous': write_thank_yous,
        'Donors to File': donors_to_file,
        'Quit': exit_program}
    print_menu(options)
    while True:
        answer = safe_input('>')
        try:
            answer = list(options)[int(answer) - 1]
        except (IndexError, ValueError):
            if answer.strip().upper() == 'MENU':
                print_menu(options)
            else:
                invalid(answer)
        else:
            options[answer]()


def print_menu(options):
    print('\t-------- MENU --------')
    print('\n'.join([
        '\t|{} {}'.format(str(i + 1), option)
        for i, option in enumerate(options)]))


def safe_input(prompt):
    """ Gracefully exits program if Keyboard Interrupt or
    EOFError are encountered. Otherwise, returns user input.
    Args:
        prompt (str) : prompt for user
    Returns:
        str : raw user input
    """
    try:
        raw = input(prompt)
    except (KeyboardInterrupt, EOFError):
        print('\nExiting...')
        sys.exit()
    return raw


def exit_program():
    """ Exits program. Prompts user to write donor info to file. """
    answer = safe_input(
        'Would you like to write donor information to file? Y/N\n>')
    if answer.upper() == 'Y':
        donors_to_file()
    print('Exiting...')
    sys.exit()


def print_thank_you():
    """ Prompts user for donor name and amount and prints thank
    you note to the console. Donation amount must be numerical."""
    name = get_name()
    donation = get_number('Enter donation:')
    donor = Donor(name, donation)
    DONORS.update(donor)
    print()
    print(donor.thank())
    print()


def get_name():
    """ Prompts user for and returns donor name.
    Returns:
        str : donor name
    """
    print('Enter donor name or LIST to see current list of donors:')
    while True:
        name = safe_input('>')
        if not name.strip():
            invalid(name)
        elif name.strip().upper() == 'LIST':
            print()
            print('Current donors:')
            print('\n'.join([str(d.name) for d in sorted(DONORS.donors)]))
            print()
        else:
            break
    return name


def get_number(prompt):
    """ Prompts user for and returns donation amount.
    Returns:
        float : amount donated
    """
    print(prompt)
    while True:
        number = safe_input('>').strip()
        number = number.strip('$')
        try:
            number = float(number)
        except ValueError:
            pass
        else:
            if number > 0:
                return number
        invalid(number, 'Amount must be > 0')


def invalid(value, clarification=None):
    print('INVALID ENTRY: "{}"'.format(value))
    if clarification:
        print(clarification)


def print_report():
    """ Prints a report showing donors and donation amounts to console."""
    print()
    print(DONORS.report())
    print()


def write_thank_yous():
    """ Writes thank yous to all donors in individual
    files in a thank_yous folder in the program's cwd."""
    directory = 'ThankYous'
    if not os.path.exists(directory):
        os.mkdir(directory)
    for donor in DONORS:
        with open(os.path.join(directory, donor.name + '.txt'), 'w') as f:
            try:
                thank_you = donor.thank(all_donations=True)
            except ValueError:
                pass
            f.write(thank_you)
    print('Thank yous written to\n{}'.format(
        os.path.join(os.getcwd(), directory)))


def get_min_max(version):
    while True:
        ans = safe_input('Apply to {}? Y/N\n>'.format(version))
        if ans.strip().upper() == 'Y':
            return get_number('Apply to values {}: '.format(
                'over' if version == 'minimum' else 'under'))
        return


def project_donations():
    while True:
        name = get_name()
        try:
            donor = DONORS[name]
        except KeyError:
            invalid(name, 'Name not found.')
        else:
            break
    factor = get_number('Enter factor:')
    minimum = get_min_max('minimum')
    maximum = get_min_max('maximum')
    projected = donor.multiply(factor, minimum, maximum)
    substrings = {
        'name': donor.name,
        'curr_total': '${:,.2f}'.format(donor.total),
        'proj_total': '${:,.2f}'.format(projected.total),
        'diff': '${:,.2f}'.format(projected.total - donor.total),
        'factor': '{}x'.format(factor),
        'min': ' >= ${:,.2f}'.format(minimum) if minimum else '',
        'max': ' <= ${:,.2f}'.format(maximum) if maximum else '',
        'and': ' and' if minimum is not None and maximum is not None else ''}
    report = \
        'PROJECTION:' +\
        '\nDonor name: {name}' +\
        '\nCurrent total: {curr_total}' +\
        '\nProjected total ({factor} donations{min}{and}{max}): {proj_total}' +\
        '\nDifference: +{diff}'
    print(report.format(**substrings))


def donors_to_file():
    """ Writes current donors and their donations to csv. """
    filename = 'donor_file.txt'
    with open(filename, 'w') as outfile:
        DONORS.write_to(outfile)
    print('Donor file written to\n{}'.format(
        os.path.join(os.getcwd(), filename)))


if __name__ == '__main__':
    main()
