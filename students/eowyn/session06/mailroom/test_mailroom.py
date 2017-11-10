#!/usr/bin/env python

import mailroom
import pytest


def test_safeinput():
    result = mailroom.safe_input()
    assert result is None


def test_return_to_menu():
    result = mailroom.return_to_menu()
    assert result is True



def test_generate_letter():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    output = 'Thank you, Margaret Atwood, for your generosity and recent gift of $555.'
    assert mailroom.generate_letter('Margaret Atwood') == output



def test_generate_report_data():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    output = [('Heinz the Baron Krauss von Espy', 3800, 2, 1900),
              ('Fred Armisen', 1662, 3, 554),
              ('Margaret Atwood', 855, 2, 428)]
    assert mailroom.generate_report_data() == output


def test_setup_table():
        ''' this is not working'''
    output = """
    'Donor Name                              |
    Total Given |Num Gifts |Average Gift'\n,
    '----------------------------------------
    -------------------------------------'"""
    assert mailroom.setup_table() == output



def test_setup_body():
    ''' this is not working'''
    list_data = mailroom.generate_report_data()
    output = """'Heinz the Baron Krauss von Espy         $  3800.00        2      $  1900.00   \nFred Armisen                            $  1662.00
3      $   554.00   \nMargaret Atwood                         $   855.00        2      $   428.00   \n'
"""
    assert mailroom.setup_body(list_data) == output

def test_remove_inputquotes():
    output = 'hello'
    assert mailroom.remove_inputquotes("hello") == output



def test_retrieve_donor_exists():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    name = "Margaret Atwood"
    output = [300, 555]
    assert mailroom.retrieve_donations(name) == output

def test_retrieve_donations_new():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    name = "Paul Simon"
    output = None
    assert mailroom.retrieve_donations(name) == output


def test_add_donation_new():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    name = "Bob Mueller"
    amount = 500
    mailroom.add_donation(name, amount)
    assert mailroom.retrieve_donations(name) == [amount]


def test_add_donation_existing():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    name = "Fred Armisen"
    amount = 500
    mailroom.add_donation(name, amount)
    assert mailroom.retrieve_donations(name) == [240, 422, 1000, 500]


def test_select_action1():
    ''' not sure how to test if correct action was completed'''
    pass


