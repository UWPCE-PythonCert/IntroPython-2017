#! /usr/bin/env python

'''
test_mailroom.py
Excercise in testing mailroom.py using pytest
'''

import mailroom
import pytest
import sys


def test_goodbye_fail():
    result = mailroom.goodbye()
    assert result == ('uit')


def test_goodbye_pass():
    result = mailroom.goodbye()
    assert result == ('quit')


def test_print_donors(capsys):
    '''
    This test captures stdout and asserts that there is an entry from
    the donor_db in the screen output.
    '''
    mailroom.print_donors()
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    donor = list(mailroom.donor_db.keys())
    # sys.stderr.write(err)
    assert out.find(donor[0])
    # assert result is None


def test_find_donor_key():
    result = mailroom.find_donor('William Gates, III')
    assert result == 'William Gates, III'


def test_find_donor_none():
    result = mailroom.find_donor('Eric Adams')
    assert result is None


def test_main_menu_selection_t():
    orig_stdin = sys.stdin
    # sys.stdin = open("preprogrammed_inputs.txt")
    with open("test_main_menu_selection_t_inputs.txt") as sys.stdin:
        pass
        result = mailroom.main_menu_selection()
    sys.stdin = orig_stdin
    assert result == "t"


# def setup_method():
#     orig_stdin = sys.stdin


# def teardown_method():
#     sys.stdin = orig_stdin




