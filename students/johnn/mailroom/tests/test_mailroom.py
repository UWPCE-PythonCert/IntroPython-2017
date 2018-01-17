#!/usr/bin/env python3

import pytest
import io
import os
from pprint import pprint
from mailroom.donors import Donor, Donors, load_donor_file, save_donor_file
from mailroom.ui import print_thank_you, print_lines, thank_all_donors, list_donors

def test_create_donor():
    """ baseline test to verify ability to create Donor() object """
    donor = repr(Donor())
    print(donor)
    assert donor.find("id=")
    assert donor.find("created=")

def test_sub_names():
    """
    verify we can create a donor from sub-name parts

    indirectly tests case conversion and full name attribute
    """
    donor = Donor(first_name="joe", last_name="smith", middle_name="q", suffix="iii")
    full_name = donor.full_name
    assert full_name == "Joe Q Smith, III"

def test_full_name():
    """ test ability to create a Donor from a full_name """
    donor = Donor(full_name="susan j adams")
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
    print_lines(3,out)
    output = out.getvalue()
    out.close()
    assert output == "\n\n\n"

def test_print_thank_you():
    """ verify the print_thank_you() function """
    a_donor = Donor( full_name= 'Mary Jo Smith, IV' )
    out = io.StringIO()
    print_thank_you(a_donor,"testfull",out)
    output = out.getvalue()
    out.close()
    assert "Dearest Mary Jo Smith, IV," in output

def test_thank_all_donors():
    """ verify the print_thank_you() function """
    test_donor_a = Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donors = Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)

    out = io.StringIO()
    thank_all_donors(test_donors,dest_override=out)
    output = out.getvalue()
    out.close()

    assert "Dearest Mary Jo Kline, III," in output
    assert "Dearest Joe Smith," in output

def test_donor_iter():
    """ verify the Donors object is iterable """
    test_donor_a = Donor( full_name= "Joe Smith", donation=100)
    test_donor_b = Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donor_c = Donor( full_name= "Adam Frank" )

    test_donors = Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)
    test_donors.add_donor(test_donor_c)

    counter = 0
    for full_name, id, last_name, first_name in test_donors:
        print(full_name, id, last_name, first_name)
        counter += 1

    assert counter == 3

def test_create_donors():
    """
    verify create_donors 

    verifies donor objects can be added via the constructor as
    well as via add_donor()
    """
    test_donor_a = Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donor_c = Donor( full_name= "Adam Frank" )

    test_donors = Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)
    test_donors.add_donor(test_donor_c)

    name_matches = [x[0] for x in test_donors.full_name_index]

    assert test_donors.number_donors == 3
    assert "Adam Frank" in name_matches

def test_list_donors():
    """ verify the list_donors() function """
    test_donor_a = Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donors = Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)
    out = io.StringIO()
    list_donors(test_donors,dest=out)
    output = out.getvalue()
    out.close()

    print(output)
    
    assert "Donor Name           | Total Given    | Num Gifts | Average Gift" in output
    assert "Joe Smith             $        250.00           2  $      125.00" in output
    assert "Mary Jo Kline, III    $      1,000.00           1  $    1,000.00" in output

def test_donor_repr():
    """ test repr values represent donor object """
    in_donor = Donor( id='f7f9a32c-defd-11e7-bee5-0800274b0a84', first_name='John', 
        middle_name='Q', last_name='Smith', suffix='III', 
        donations=[{'amount': 100.0, 'date': '2017-12-12Z'}], 
        created='2017-12-12T05:33:22.651546Z' )

    repr_str = repr(in_donor)
    out_donor = eval(repr_str)
    assert repr(in_donor) == repr(out_donor)

def test_donor_str():
    """ test str values represent donor object """
    in_donor = Donor( id='f7f9a32c-defd-11e7-bee5-0800274b0a84', first_name='John', 
        middle_name='Q', last_name='Smith', suffix='III', 
        donations=[{'amount': 100.0, 'date': '2017-12-12Z'}], 
        created='2017-12-12T05:33:22.651546Z' )

    str_str = str(in_donor)
    assert "id='f7f9a32c-defd-11e7-bee5-0800274b0a84'" in str_str
    assert "average_donations=100" in str_str
    assert "informal_name='John Q Smith'" in str_str
    assert "full_name='John Q Smith, III'" in str_str

def test_donors_repr():
    """ test repr values represent donors object """
    in_donors = Donors( Donor( id='902a4e3e-deff-11e7-bee5-0800274b0a84', 
        first_name='Maggie', last_name='Smith', 
        donations=[{'amount': 99.0, 'date': '2017-12-12Z'}], 
        created='2017-12-12T05:44:47.480878Z' ) )

    assert repr(in_donors) == str(in_donors)

def test_donors_str():
    """ test repr values represent donors object """
    in_donors = Donors( Donor( id='902a4e3e-deff-11e7-bee5-0800274b0a84', 
        first_name='Maggie', last_name='Smith', 
        donations=[{'amount': 99.0, 'date': '2017-12-12Z'}], 
        created='2017-12-12T05:44:47.480878Z' ) )

    repr_str = repr(in_donors)
    out_donors = eval(repr_str)
    assert repr(in_donors) == repr(out_donors)

def test_save_read_file():
    """
    verify save donors and read donors 

    we create a donors object, save it, read it, then examine the contents which
    indirectly tests both save and read
    """

    test_donor_a = Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donors = Donors(test_donor_a)
    test_donors.add_donor(test_donor_b)

    test_donor_file="test_donor_file"

    save_donor_file(test_donors,donor_file=test_donor_file)

    return_donors = load_donor_file(donor_file=test_donor_file)

    name_matches = [x[0] for x in return_donors.full_name_index]

    print(name_matches)

    assert "Joe Smith" in name_matches
    assert "Mary Jo Kline, III" in name_matches
    assert "Joe Jo Williams" not in name_matches

    os.remove(test_donor_file)

def test_bulk_donation():
    """ test we can add bulk donations on create """
    bar=Donor(full_name="maggie smith", 
        donations=[{'amount': 99.0, 'date': '2017-12-12Z'}, 
        {'amount': 100.0, 'date': '2017-12-12Z'}])

    assert bar.average_donations == 99.5

def test_match_donor():
    """ verify the match_donor search functions """
    test_donor_a = Donor( full_name= "Joe Smith", donation=100)
    test_donor_a.add_donation(150)
    test_donor_b = Donor( full_name= "Mary Jo Kline, III", donation= 1000)
    test_donors = Donors(test_donor_a)
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
    test_donor = Donor( full_name= "Joe Smith", donation=100)
    test_donor.add_donation(150)
    test_donor.add_donation(777.77)

    assert test_donor.number_donations == 3
    assert test_donor.total_donations ==  1027.77
    assert test_donor.average_donations == 342.59
