#!/usr/bin/env python3

import mailroom
import pytest
import io


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
