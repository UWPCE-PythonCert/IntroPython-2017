#! /usr/bin/env python

'''
test_mailroom.py
Excercise in testing mailroom.py using pytest
'''

import mailroom
import pytest
import sys
from textwrap import dedent
import os


def test_goodbye_fail():
    '''
    Use an invalid value to get the test to fail
    Expected result - fail
    '''
    result = mailroom.goodbye()
    assert result == ('uit')


def test_goodbye_pass():
    '''
    Provide a valid input, ('quit')
    '''
    result = mailroom.goodbye()
    assert result == ('quit')


def test_print_donors(capsys):
    '''
    This test captures stdout and asserts that there is an entry from
    the donor_db in the screen output.
    Saw this on stackoverflow.com.... seems to resolve the issue
    of testing screen output.
    '''
    mailroom.print_donors()
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    donor = list(mailroom.donor_db.keys())
    assert out.find(donor[0])


def test_find_donor_key():
    '''
    Input a valid user from the mailroom.donor_db
    '''
    result = mailroom.find_donor('William Gates, III')
    assert result == 'William Gates, III'


def test_find_donor_nonexistant():
    result = mailroom.find_donor('Eric Adams')
    assert result is None


def test_main_menu_selection_t():
    '''
    Pass the test by giving a user input of 't'
    Simulate user input of 't'
    :data - a text file
            in the current directory, (test_main_menu_selection_t_inputs.txt),
            is used as input data.
            The value that the user would input is simulated
            by making a one line entry into the file.
            Example: for a user input of 't', enter the single
            character 't' on the first line, (no quotes).

    Saw this solution to the 'input' issue on stackoverflow.
    Seems to work
    '''
    orig_stdin = sys.stdin
    with open("test_main_menu_selection_t_inputs.txt") as sys.stdin:
        result = mailroom.main_menu_selection()
    sys.stdin = orig_stdin
    assert result == "t"


def test_gen_letter():
    '''
    Input a valid donor and assert that the letter is returned
    '''
    letter = dedent('''
          Dear {}

          Thank you for your very kind donation of ${:.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Team
          ''')
    donor_list = list(mailroom.donor_db.keys())
    donor = donor_list[0]
    result = mailroom.gen_letter(donor)
    assert result == letter.format(donor, mailroom.donor_db[donor][-1])


def test_send_thank_you_list_menu(capsys):
    '''
    Simulate user input of 'list' and the 'menu', (to force a return)
    :data - a text file
            in the current directory, (test_send_thank_you_list_inputs.txt),
            is used as input data.
            The value that the user would input is simulated
            by making a one entry into the file per user input.
            Example: for a user input of 'list', enter 'list'
            on the first line, (no quotes).
            Enter 'menu' on the second line for the second user
            input, (this also forces a return).
    Modified from a solution to the 'input' issue on stackoverflow.
    Seems to work.
    '''
    orig_stdin = sys.stdin
    with open("test_send_thank_you_list_inputs.txt") as sys.stdin:
        result = mailroom.send_thank_you()
    sys.stdin = orig_stdin
    test_print_donors(capsys)
    assert result is None


def test_send_thank_you_donor_existing_menu():
    ''' Simulate a user input of an existing donor.
    After the expected result simulate a user input of 'menu'.
    This will cause the function to return.
    :Data file = test_send_thank_you_donor_existing_menu.txt in
                 current working directory
    '''
    orig_stdin = sys.stdin
    with open("test_send_thank_you_donor_existing_menu.txt") as sys.stdin:
        result = mailroom.send_thank_you()
    sys.stdin = orig_stdin
    assert result is None


def test_send_thank_you_donor_existing_amount_no_write():
    '''Simulate a user input of an existing donor.
    Simulate a user input of a donation amount.
    :Data file = test_send_thank_you_donor_existing_amount_no_write.txt
                 in current working directory
    '''
    orig_stdin = sys.stdin
    with open("test_send_thank_you_donor_existing_amount_no_write.txt") \
            as sys.stdin:
        result = mailroom.send_thank_you()
    sys.stdin = orig_stdin
    with open("test_send_thank_you_donor_existing_amount_no_write.txt") \
            as f:
        donor = f.readline()
        donor = donor.strip()
        amount = f.readline()
    assert mailroom.donor_db[donor][-1] == float(amount)
    assert result is None


def test_send_thank_you_new_donor_amount_no_write():
    '''Simulate a user input of a new donor.
    Simulate a user input of a donation amount.
    :Data file = test_send_thank_you_new_donor_amount_no_write.txt
                 First line of file = new donor name
                 Second line of file = donation amount (float)
                 Third line of file = n, (no quotes)
                 File is in current working directory
    '''
    orig_stdin = sys.stdin
    with open("test_send_thank_you_new_donor_amount_no_write.txt") \
            as sys.stdin:
        result = mailroom.send_thank_you()
    sys.stdin = orig_stdin
    with open("test_send_thank_you_donor_existing_amount_no_write.txt") \
            as f:
        donor = f.readline()
        donor = donor.strip()
        amount = f.readline()
    assert mailroom.donor_db[donor][-1] == float(amount)
    assert result is None


def test_send_thank_you_print_letter_no_write(capsys):
    '''
    Data file = test_send_thank_you_donor_existing_amount_no_write.txt
    Testing that the thank you letter is printed, (look for the donor
    in the console output)
    '''
    orig_stdin = sys.stdin
    with open("test_send_thank_you_donor_existing_amount_no_write.txt") \
            as sys.stdin:
        mailroom.send_thank_you()
    sys.stdin = orig_stdin
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    donor = list(mailroom.donor_db.keys())
    assert out.find(donor[0])


def test_send_thank_you_write_letter_to_file():
    '''
    Test if the thank you letter is written to a file
    Data file = test_send_thank_you_write_letter_to_file
                First line = existing donor
                Second line = donation amount
                Third line = y, (no quotes)
    '''
    orig_stdin = sys.stdin
    with open("test_send_thank_you_write_letter_to_file.txt") \
            as f:
            donor = f.readline().strip()
    if os.path.isfile("./" + donor + ".txt"):
        os.remove("./" + donor + ".txt")
    with open("test_send_thank_you_write_letter_to_file.txt") \
            as sys.stdin:
        mailroom.send_thank_you()
    sys.stdin = orig_stdin
    result = os.path.isfile("./" + donor + ".txt")
    assert result is True

# ----  to do list
# write tests for :
#    sort_keys()
#    print_donor_report()
