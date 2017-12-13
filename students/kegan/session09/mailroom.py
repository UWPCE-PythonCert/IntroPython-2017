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


# donors = {
#     'Benedict Cumberbatch': [200000.0],
#     'Elon Musk': [10000.0, 150000.0, 100000.0],
#     'Dad': [20.0, 5.0],
#     'Donald Trump': [2.81],
#     'Billy Neighbor': [.54, .01, .25]}

with open('donor_file.txt', 'r') as fin:
    DONORS = DonorList.read_from(fin)


def main():
    """ Module that drives main menu."""
    options = {
        'Send a Thank You': print_thank_you,
        'Create a Report': print_report,
        'Write Thank Yous': write_thank_yous,
        'Donors to File': donors_to_file,
        'Quit': exit_program}
    while True:
        print('\nPlease choose from the following options:')
        prompt = '\n'.join([
            '{} {}'.format(str(i + 1), option)
            for i, option in enumerate(options)]) + '\n>'
        raw = safe_input(prompt)
        try:
            answer = list(options)[int(raw) - 1]
        except (IndexError, ValueError):
            print('{} is not valid input'.format(raw))
        else:
            options[answer]()


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
    name = get_donor()
    donation = get_donation()
    donor = Donor(name, donation)
    DONORS.update(donor)
    print()
    try:
        print(donor.thank())
    except ValueError:
        print(
            'Cannot write thank you for ' +
            '{0} because {0} has not given a donation'.format(donor.name))


def get_donor():
    """ Prompts user for and returns donor name.
    Returns:
        str : donor name
    """
    while True:
        donor = safe_input(
            'Who donated? (Enter LIST to see current list of donors)\n>')
        if not donor.strip():
            print('"{}" is not a valid name.'.format(donor))
            print('Please try again.')
            continue
        elif donor.strip().upper() == 'LIST':
            print()
            print('Current donors:')
            print('\n'.join([str(d.name) for d in sorted(DONORS.donors)]))
            print()
        else:
            break
    return donor


def get_donation():
    """ Prompts user for and returns donation amount.
    Returns:
        float : amount donated
    """
    while True:
        donation = safe_input('How much was donated?\n>')
        try:
            donation = float(donation.strip('$'))
            if donation > 0:
                return donation
        except ValueError:
            pass
        print('{} is not a valid amount.'.format(donation))
        print('Please try again.')


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


def donors_to_file():
    """ Writes current donors and their donations to csv. """
    filename = 'donor_file.txt'
    with open(filename, 'w') as outfile:
        DONORS.write_to(outfile)
    print('Donor file written to\n{}'.format(
        os.path.join(os.getcwd(), filename)))


if __name__ == '__main__':
    main()
