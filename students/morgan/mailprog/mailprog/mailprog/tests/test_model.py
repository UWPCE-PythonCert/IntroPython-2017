from mailprog import dataModels, ui
import os







"""Donor class tests"""
def test_create_donor():
    bob = dataModels.Donor("Robert Dunbar", 1)
    assert bob.name == "Robert Dunbar"
    assert bob.donations == 1

def test_add_donation():
    bob = dataModels.Donor("bobbert", [50])
    bob.add_donation(10)
    assert bob.total == 60


def test_max_donation():
    bob = dataModels.Donor("bobbert", [50])
    bob.add_donation(10)
    assert bob.maxdonation == 50

def test_namelength():
    bob = dataModels.Donor("bobbert", [50])
    assert bob.namelength == 7

def test_donation_count():
    bob = dataModels.Donor("bobbert", [50])
    bob.add_donation(10)
    assert bob.donation_count == 2

def test_average_donation():
    bob = dataModels.Donor("bobbert", [50])
    bob.add_donation(10)
    assert bob.average_donation == 30



"""Storage class tests"""
def test_add_donor():
    DB = dataModels.Storage()
    bob = dataModels.Donor("bobbert", [50])
    timmy = dataModels.Donor("Tim Tam", [10])
    DB.add_donor(bob)
    DB.add_donor(timmy)
    assert len(DB.donors) == 2

def test_list_donors():
    DB = dataModels.Storage()
    bob = dataModels.Donor("bobbert", [50])
    timmy = dataModels.Donor("Tim Tam", [10])
    DB.add_donor(bob)
    DB.add_donor(timmy)
    blurb = DB.list_donors()
    assert blurb == ['bobbert','Tim Tam']

def test_donation_input():
    DB = dataModels.Storage()
    bob = dataModels.Donor("bobbert", [50])
    DB.add_donor(bob)
    DB.add_donation("BOBBERT", 10)
    assert bob.donation_count == 2


def test_read_donors():
    donor_objects = []
    infile = os.path.join(os.path.dirname(__file__),"test_donors.csv")
    DB = dataModels.Storage()
    DB.read_donors(infile, donor_objects)
    assert len(DB.list_donors()) == 2


