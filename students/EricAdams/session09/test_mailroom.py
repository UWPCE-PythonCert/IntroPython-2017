#! /usr/bin/env python

# test_mailroom.py
# Perform unit testing on the object oriented version of mailroom.py

import mailroom as mr
import os


def test_list_donor():
    '''
    list_donor() returns a list of correctly
    '''
    donor_obj = mr.Donor()
    listing = donor_obj.list_donors()
    assert listing.startswith("Donor list:\n")
    assert "Jeff Bezos" in listing
    assert len(listing.split('\n')) == 5


def test_find_donor():
    """ checks a donor that is there, but with odd case and spaces"""
    donor_obj = mr.Donor()
    donor = donor_obj.find_donor("jefF beZos ")
    assert donor[0] == "Jeff Bezos"


def test_find_donor_not():
    '''test one that's not there
    '''
    donor_obj = mr.Donor()
    donor = donor_obj.find_donor("Jeff Bzos")
    assert donor is None


def test_gen_letter():
    """ test the donor letter
     """
    # create a sample donor
    donor_obj = mr.Donor()
    donor = ("Fred Flintstone", [432.45, 65.45, 230.0])
    letter = donor_obj.gen_letter(donor)
    assert letter.startswith("Dear Fred Flintstone")
    assert letter.endswith("-The Team\n")
    assert "donation of $230.00" in letter


def test_add_donor():
    donor_obj = mr.Donor()
    name = "Fred Flintstone  "
    donor = donor_obj.add_donor(name)
    donor[1].append(300)
    assert donor[0] == "Fred Flintstone"
    assert donor[1] == [300]
    assert donor_obj.find_donor(name) == donor


def test_generate_donor_report():
    donor_obj = mr.Donor()
    report = donor_obj.generate_donor_report()
    print(report)  # printing so you can see it if it fails
    # this is pretty tough to test
    # these are not great, because they will fail if unimportant parts of the
    # report are changed.
    # but at least you know that codes working now.
    assert report.startswith(
        "Donor Name                | Total Given | Num Gifts | Average Gift")

    assert "Jeff Bezos                  $    877.33           1   $     877.33" in report
    # assert False


def test_save_letters_to_disk():
    """
    This only tests that the files get created, but that's a start

    Note that the contents of the letter was already
    tested with test_gen_letter
    """
    donor_obj = mr.Donor()
    donor_obj.save_letters_to_disk()

    assert os.path.isfile('Jeff_Bezos.txt')
    assert os.path.isfile('William_Gates_III.txt')
    # check that it'snot empty:
    with open('William_Gates_III.txt') as f:
        size = len(f.read())
    assert size > 0
