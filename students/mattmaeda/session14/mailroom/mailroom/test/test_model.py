#!/usr/bin/env python
"""
Unit tests for mailroom model
"""
import os
from unittest import mock
import pytest
from mailroom import model

TEST_LETTER = """
Dear Test User 1,

Thank you for your donation of $100.00.
"""

TEST_REPORT = """
Donor Name                                        | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------------------------------
Test User 2                                        $      300.00           2        150.00
Test User 1                                        $      150.00           2         75.00


"""

@pytest.fixture
def sample_db():
    """ Loads test db data """
    return model.DonorDB.load_from_file("mock_load_file.json")


def test_donor_init_none():
    """ Test donor init """
    donor = model.Donor("Test User")
    assert donor.name == "Test User"


def test_donor_init():
    """ Test donor init """
    donor = model.Donor("Test User", [100])
    assert donor.name == "Test User"
    assert donor.total_donations == 100


def test_donor_name():
    """ test donor name """
    donor = model.Donor("Test User")
    assert donor.name == "Test User"
    donor.name = "New Test User"
    assert donor.name == "New Test User"


def test_add_donation():
    """ test add donation """
    donor = model.Donor("Test User")
    donor.add_donation(100)
    assert 100 in donor.donations


def test_total_donation():
    """ test total donation """
    donor = model.Donor("Test User")
    donor.add_donation(100)
    donor.add_donation(150)
    assert donor.total_donations == 250


def test_avg_donation():
    """ test average donation """
    donor = model.Donor("Test User")
    donor.add_donation(50)
    donor.add_donation(100)
    assert donor.avg_donations == 75


def test_last_donation():
    """ test last donation """
    donor = model.Donor("Test User", [100])
    assert donor.last_donation == 100


def test_last_donation_none():
    """ test last donation no donation """
    donor = model.Donor("Test User")
    assert donor.last_donation is None


def test_num_donations():
    """ test number of donation """
    donor = model.Donor("Test User")
    donor.add_donation(50)
    donor.add_donation(100)
    assert donor.num_donations == 2


def test_db_init():
    """ test db init """
    database = model.DonorDB()
    size = len(database.donors)
    assert size == 0


def test_db_init_initial_list():
    """ Test db init with values """
    donor1 = model.Donor("Test User1")
    donor2 = model.Donor("Test User2")
    donors = [donor1, donor2]

    database = model.DonorDB(donors=donors)
    size = len(database.donors)
    assert size == 2


def test_db_load_from_file():
    """ test loading from file """
    database = sample_db()
    size = len(database.donors)
    assert size == 1


def test_db_save_to_file():
    """ test saving to file """
    donor1 = model.Donor("Test User1")
    donor2 = model.Donor("Test User2")
    donors = [donor1, donor2]

    database = model.DonorDB(donors=donors)
    database.save_to_file("test_output.json")
    assert os.path.exists("test_output.json")



def test_donors():
    """ Test geting database donors """
    donor1 = model.Donor("Test User1")
    donor2 = model.Donor("Test User2")
    donors = [donor1, donor2]

    database = model.DonorDB(donors=donors)
    donor_list = database.donors
    assert "Test User1" in [d.name for d in donor_list]


def test_add_donor():
    """ Test geting database donor list """
    donor1 = model.Donor("Test User1")
    donor2 = model.Donor("Test User2")
    donors = [donor1, donor2]

    database = model.DonorDB(donors=donors)
    donor_list = database.donors
    assert donor1 in donor_list

    donor3 = database.add_donor("Test User3")
    donor_list = database.donors
    size = len(donor_list)
    assert size == 3
    assert donor3 in donor_list


def test_send_letter():
    """ test sending thank you letter """
    donor1 = model.Donor("Test User 1")
    donor1.add_donation(100)
    database = model.DonorDB()
    letter = database.send_letter(donor1)
    assert TEST_LETTER == letter


def test_donor_report():
    """ test donor report generation """
    donor1 = model.Donor("Test User 1")
    donor1.add_donation(100)
    donor1.add_donation(50)
    donor2 = model.Donor("Test User 2")
    donor2.add_donation(250)
    donor2.add_donation(50)
    database = model.DonorDB(donors=[donor1, donor2])
    report = database.get_donor_report()

    assert TEST_REPORT == report
