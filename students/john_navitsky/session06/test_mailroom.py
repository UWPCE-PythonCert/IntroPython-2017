#!/usr/bin/env python3

import mailroom
import pytest
import io
import os
from pprint import pprint


def test_true():
    assert True


def test_parse_name():
    assert mailroom.parse_name("Mary Jo Smith, IV") == {
        'full_name': 'Mary Jo Smith, IV', 
        'informal_name': 'Mary Jo Smith',
        'suffix': 'IV',
        'last_name': 'Smith',
        'first_name': 'Mary Jo' }


def test_print_lines():
    # verify the print_lines() function
    out = io.StringIO()
    mailroom.print_lines(3,out)
    output = out.getvalue()
    out.close()
    assert output == "\n\n\n"


def test_mock_input():
    # verify our mock input works
    assert mailroom.safe_input(mock=True,mock_in="foo") == "foo"


def test_print_thank_you():
    # verify the print_thank_you() function
    a_donor = {
        'full_name': 'Mary Jo Smith, IV', 
        'informal_name': 'Mary Jo Smith',
        'suffix': 'IV',
        'last_name': 'Smith',
        'first_name': 'Mary Jo' }
    out = io.StringIO()
    mailroom.print_thank_you(a_donor,"testfull",out)
    output = out.getvalue()
    out.close()
    assert "Dearest Mary Jo Smith, IV," in output


def test_thank_all_donors():
    # verify the print_thank_you() function
    test_donors = {'04cee581bd27183b30922324c454547e': {'created': '2017-11-13T06:15:06.829472Z',
                                      'donations': [{'amount': 100.0,
                                                     'date': '2017-11-13Z'},
                                                    {'amount': 150.0,
                                                     'date': '2017-11-13Z'}],
                                      'donor_id': '04cee581bd27183b30922324c454547e',
                                      'first_name': 'Joe',
                                      'full_name': 'Joe Smith',
                                      'informal_name': 'Joe Smith',
                                      'last_name': 'Smith',
                                      'suffix': ''},
 '55af71b4c7c2dd90c67bb001e1b2d99f': {'created': '2017-11-13T06:15:29.087828Z',
                                      'donations': [{'amount': 1000.0,
                                                     'date': '2017-11-13Z'}],
                                      'donor_id': '55af71b4c7c2dd90c67bb001e1b2d99f',
                                      'first_name': 'Mary Jo',
                                      'full_name': 'Mary Jo Kline, III',
                                      'informal_name': 'Mary Jo Kline',
                                      'last_name': 'Kline',
                                      'suffix': 'III'}}
    out = io.StringIO()
    mailroom.thank_all_donors(test_donors,dest_override=out)
    output = out.getvalue()
    out.close()
    assert "Dearest Mary Jo Kline, III," in output
    assert "Dearest Joe Smith," in output
    

def test_print_report():
    # verify the print_thank_you() function
    test_donors = {'04cee581bd27183b30922324c454547e': {'created': '2017-11-13T06:15:06.829472Z',
                                      'donations': [{'amount': 100.0,
                                                     'date': '2017-11-13Z'},
                                                    {'amount': 150.0,
                                                     'date': '2017-11-13Z'}],
                                      'donor_id': '04cee581bd27183b30922324c454547e',
                                      'first_name': 'Joe',
                                      'full_name': 'Joe Smith',
                                      'informal_name': 'Joe Smith',
                                      'last_name': 'Smith',
                                      'suffix': ''},
 '55af71b4c7c2dd90c67bb001e1b2d99f': {'created': '2017-11-13T06:15:29.087828Z',
                                      'donations': [{'amount': 1000.0,
                                                     'date': '2017-11-13Z'}],
                                      'donor_id': '55af71b4c7c2dd90c67bb001e1b2d99f',
                                      'first_name': 'Mary Jo',
                                      'full_name': 'Mary Jo Kline, III',
                                      'informal_name': 'Mary Jo Kline',
                                      'last_name': 'Kline',
                                      'suffix': 'III'}}
    out = io.StringIO()
    mailroom.print_report(test_donors,dest=out)
    output = out.getvalue()
    out.close()
    assert "Donor Name           | Total Given    | Num Gifts | Average Gift" in output
    assert "Joe Smith             $        250.00           2  $      125.00" in output
    assert "Mary Jo Kline, III    $      1,000.00           1  $    1,000.00" in output



#def save_donor_file(donors,donor_file="donors.json"):

def test_save_file():
    # verify the print_thank_you() function
    test_donors = {'04cee581bd27183b30922324c454547e': {'created': '2017-11-13T06:15:06.829472Z',
                                      'donations': [{'amount': 100.0,
                                                     'date': '2017-11-13Z'},
                                                    {'amount': 150.0,
                                                     'date': '2017-11-13Z'}],
                                      'donor_id': '04cee581bd27183b30922324c454547e',
                                      'first_name': 'Joe',
                                      'full_name': 'Joe Smith',
                                      'informal_name': 'Joe Smith',
                                      'last_name': 'Smith',
                                      'suffix': ''},
 '55af71b4c7c2dd90c67bb001e1b2d99f': {'created': '2017-11-13T06:15:29.087828Z',
                                      'donations': [{'amount': 1000.0,
                                                     'date': '2017-11-13Z'}],
                                      'donor_id': '55af71b4c7c2dd90c67bb001e1b2d99f',
                                      'first_name': 'Mary Jo',
                                      'full_name': 'Mary Jo Kline, III',
                                      'informal_name': 'Mary Jo Kline',
                                      'last_name': 'Kline',
                                      'suffix': 'III'}}
    test_donor_file="test_donor_file"
    mailroom.save_donor_file(test_donors,donor_file=test_donor_file)
    with open(test_donor_file) as test_data:
        test_values = test_data.read()
    assert "04cee581bd27183b30922324c454547e" in test_values
    assert "55af71b4c7c2dd90c67bb001e1b2d99f" in test_values
    
def test_load_donor_file():
    test_donors = {'04cee581bd27183b30922324c454547e': {'created': '2017-11-13T06:15:06.829472Z',
                                      'donations': [{'amount': 100.0,
                                                     'date': '2017-11-13Z'},
                                                    {'amount': 150.0,
                                                     'date': '2017-11-13Z'}],
                                      'donor_id': '04cee581bd27183b30922324c454547e',
                                      'first_name': 'Joe',
                                      'full_name': 'Joe Smith',
                                      'informal_name': 'Joe Smith',
                                      'last_name': 'Smith',
                                      'suffix': ''},
 '55af71b4c7c2dd90c67bb001e1b2d99f': {'created': '2017-11-13T06:15:29.087828Z',
                                      'donations': [{'amount': 1000.0,
                                                     'date': '2017-11-13Z'}],
                                      'donor_id': '55af71b4c7c2dd90c67bb001e1b2d99f',
                                      'first_name': 'Mary Jo',
                                      'full_name': 'Mary Jo Kline, III',
                                      'informal_name': 'Mary Jo Kline',
                                      'last_name': 'Kline',
                                      'suffix': 'III'}}
    test_donor_file="test_donor_file"
    return_dict = mailroom.load_donor_file(donor_file=test_donor_file)
    assert test_donors == return_dict
    os.remove(test_donor_file)


def test_match_donor():
    test_donors = {'04cee581bd27183b30922324c454547e': {'created': '2017-11-13T06:15:06.829472Z',
                                  'donations': [{'amount': 100.0,
                                                 'date': '2017-11-13Z'},
                                                {'amount': 150.0,
                                                 'date': '2017-11-13Z'}],
                                  'donor_id': '04cee581bd27183b30922324c454547e',
                                  'first_name': 'Joe',
                                  'full_name': 'Joe Smith',
                                  'informal_name': 'Joe Smith',
                                  'last_name': 'Smith',
                                  'suffix': ''}}
    a_donor = {
        'full_name': 'Joe Smith', 
        'informal_name': 'Joe Smith',
        'suffix': '',
        'last_name': 'Smith',
        'first_name': 'Joe' }
    return_donor = mailroom.match_donor(a_donor, test_donors)
    assert return_donor["donor_id"] == "04cee581bd27183b30922324c454547e"


def test_update_donor_match():
    test_donors = {'04cee581bd27183b30922324c454547e': {'created': '2017-11-13T06:15:06.829472Z',
                                  'donations': [{'amount': 100.0,
                                                 'date': '2017-11-13Z'},
                                                {'amount': 150.0,
                                                 'date': '2017-11-13Z'}],
                                  'donor_id': '04cee581bd27183b30922324c454547e',
                                  'first_name': 'Joe',
                                  'full_name': 'Joe Smith',
                                  'informal_name': 'Joe Smith',
                                  'last_name': 'Smith',
                                  'suffix': ''}}
    a_donor = {
        'full_name': 'Joe Smith', 
        'informal_name': 'Joe Smith',
        'suffix': '',
        'last_name': 'Smith',
        'first_name': 'Joe' }
    donation = 777.77
    mailroom.update_donor(current_donor=a_donor, donors=test_donors, new_donation=donation)
    pprint(test_donors)
    assert len(test_donors["04cee581bd27183b30922324c454547e"]["donations"]) == 3


def test_update_donor_no_match():
    test_donors = {'04cee581bd27183b30922324c454547e': {'created': '2017-11-13T06:15:06.829472Z',
                                  'donations': [{'amount': 100.0,
                                                 'date': '2017-11-13Z'},
                                                {'amount': 150.0,
                                                 'date': '2017-11-13Z'}],
                                  'donor_id': '04cee581bd27183b30922324c454547e',
                                  'first_name': 'Joe',
                                  'full_name': 'Joe Smith',
                                  'informal_name': 'Joe Smith',
                                  'last_name': 'Smith',
                                  'suffix': ''}}
    a_donor = {
        'full_name': 'Jane Jones', 
        'informal_name': 'Jane Jones',
        'suffix': '',
        'last_name': 'Jones',
        'first_name': 'Jane' }
    donation = 777.77
    mailroom.update_donor(current_donor=a_donor, donors=test_donors, new_donation=donation)
    pprint(test_donors)
    assert len(test_donors) == 2
