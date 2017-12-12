#!/usr/bin/env python3

import mailroom
import pytest
import io
import os
from pprint import pprint


def test_create_donor():
    """ baseline test to verify ability to create Donor() object """
    donor = repr(mailroom.Donor())
    print(donor)
    assert donor.find("id=")
    assert donor.find("created=")

def test_sub_names():
    """
    verify we can create a donor from sub-name parts

    indirectly tests case conversion and full name attribute
    """
    donor = mailroom.Donor(first_name="joe", last_name="smith", middle_name="q", suffix="iii")
    full_name = donor.full_name
    assert full_name == "Joe Q Smith, III"

def test_full_name():
    """ test ability to create a Donor from a full_name """
    donor = mailroom.Donor(full_name="susan j adams")
    first_name = donor.first_name
    middle_name = donor.middle_name
    last_name = donor.last_name
    suffix = donor.suffix
    assert first_name == "Susan"
    assert middle_name == "J"
    assert last_name == "Adams"
    assert suffix == ""

def test_print_lines():
    """ verify the print_lines() function """
    out = io.StringIO()
    mailroom.print_lines(3,out)
    output = out.getvalue()
    out.close()
    assert output == "\n\n\n"

def test_print_thank_you():
    """ verify the print_thank_you() function """
    a_donor = mailroom.Donor( full_name= 'Mary Jo Smith, IV' )
    out = io.StringIO()
    mailroom.print_thank_you(a_donor,"testfull",out)
    output = out.getvalue()
    out.close()
    assert "Dearest Mary Jo Smith, IV," in output

def test_thank_all_donors():
    """ verify the print_thank_you() function """
    test_donor_a = mailroom.Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = mailroom.Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donors = mailroom.Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)

    out = io.StringIO()
    mailroom.thank_all_donors(test_donors,dest_override=out)
    output = out.getvalue()
    out.close()

    assert "Dearest Mary Jo Kline, III," in output
    assert "Dearest Joe Smith," in output

def test_create_donors():
    """ verify create_donors """
    test_donor_a = mailroom.Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = mailroom.Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donor_c = mailroom.Donor( full_name= "Adam Frank" )

    test_donors = mailroom.Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)
    test_donors.add_donor(test_donor_c)

    name_matches = [x[0] for x in test_donors.full_name_index]

    assert test_donors.number_donors == 3
    assert "Adam Frank" in name_matches

def test_list_donors():
    """ verify the list_donors() function """
    test_donor_a = mailroom.Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = mailroom.Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donors = mailroom.Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)
    out = io.StringIO()
    mailroom.list_donors(test_donors,dest=out)
    output = out.getvalue()
    out.close()

    print(output)
    
    assert "Donor Name           | Total Given    | Num Gifts | Average Gift" in output
    assert "Joe Smith             $        250.00           2  $      125.00" in output
    assert "Mary Jo Kline, III    $      1,000.00           1  $    1,000.00" in output

def test_save_read_file():
    """
    verify save donors and read donors 

    we create a donors object, save it, read it, then examine the contents which
    indirectly tests both save and read
    """

    test_donor_a = mailroom.Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = mailroom.Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donors = mailroom.Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)

    test_donor_file="test_donor_file"

    mailroom.save_donor_file(test_donors,donor_file=test_donor_file)

    return_donors = mailroom.load_donor_file(donor_file=test_donor_file)

    name_matches = [x[0] for x in return_donors.full_name_index]

    print(name_matches)

    assert "Joe Smith" in name_matches
    assert "Mary Jo Kline, III" in name_matches
    assert "Joe Jo Williams" not in name_matches

    os.remove(test_donor_file)

def test_match_donor():
    """ verify the match_donor search functions """
    test_donor_a = mailroom.Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = mailroom.Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donors = mailroom.Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)

    matches = test_donors.match_donor("Joe Smith")
    name_matches = [x[0] for x in matches]

    print(matches)

    assert "Joe Smith" in name_matches
    assert "Mary Jo Kline, III" not in name_matches

def test_add_donations():
    """
    test add_donations

    we test that we can add a donation as part of the constructor as well
    as via add_donation.  we also test that the donation attributes
    (number_donations, total_donations and average_donations) work 
    correctly.
    """
    test_donor = mailroom.Donor( full_name= "Joe Smith", donation=100)
    test_donor.add_donation(150)
    test_donor.add_donation(777.77)

    assert test_donor.number_donations == 3
    assert test_donor.total_donations ==  1027.77
    assert test_donor.average_donations == 342.59
