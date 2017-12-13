#!/usr/bin/env python

import oomailroom as mr
import os.path


def test_donor_init():
    name = "Ada Lovelace"
    amt = 345
    d = mr.Donor(name)
    d.add_donation(amt)
    assert d.name == name
    assert d.donations == [345]

def test_name():
    name = "Ada Lovelace"
    amt = 345
    d = mr.Donor(name)
    d.add_donation(amt)
    assert d.name == name


def test_create_transactions():
    name = "Ada Lovelace"
    amt = 345
    d = mr.Donor(name)
    d.add_donation(amt)
    t = mr.Transactions()
    t.add_donor(name, amt)
    assert t.get_donor(name).name == name


def test_add_donors_to_transactions():
    name = "Ada Lovelace"
    amt = 345
    d = mr.Donor(name)
    d.add_donation(amt)
    name2 = "Marge Simpson"
    amt2 = 500
    d2 = mr.Donor(name2)
    d2.add_donation(amt2)
    t = mr.Transactions()
    t.add_donor(name, amt)
    t.add_donor(name2, amt2)
    assert t.get_donor(name).name == name
    assert t.get_donor(name2).name == name2
    assert t.get_donor(name).most_recent_donation == amt
    assert t.get_donor(name2).most_recent_donation == amt2



def test_add_donation():
    name = "Ada Lovelace"
    amt = 345
    d = mr.Donor(name)
    d.add_donation(amt)
    amt2 = 400
    d.add_donation(amt2)
    assert d.count_donations == 2
    assert d.sum_donations == 745
    assert d.most_recent_donation == 400
    assert d.average_donation == 372.50


def test_new_donor():
    name = "Ada Lovelace"
    amt = 345
    d = mr.Donor(name)
    d.add_donation(amt)
    name2 = "Marge Simpson"
    amt2 = 500
    d2 = mr.Donor(name2)
    d2.add_donation(amt2)
    t = mr.Transactions()
    t.add_donor(name, amt)
    assert t.get_donor(name2) is None
    t.add_donor(name2, amt2)
    assert t.get_donor(name2).name == name2
    assert t.get_donor(name2).most_recent_donation == amt2


def test_list_names():
    name = "Ada Lovelace"
    amt = 345
    d = mr.Donor(name)
    d.add_donation(amt)
    name2 = "Marge Simpson"
    amt2 = 500
    d2 = mr.Donor(name2)
    d2.add_donation(amt2)
    t = mr.Transactions()
    t.add_donor(name, amt)
    t.add_donor(name2, amt2)
    result = 'Donor Names:\n' + name + '\n' + name2
    print(t.list_names())
    assert t.list_names() == result


def test_generate_report_data():
    name, amt = ("Ada Lovelace", 345)
    d = mr.Donor(name)
    d.add_donation(amt)
    name2, amt2, amt3 = ("Marge Simpson", 500, 1000)
    d2 = mr.Donor(name2)
    d2.add_donation(amt2)
    t = mr.Transactions()
    t.add_donor(name, amt)
    t.add_donor(name2, amt2)
    t.add_donor(name2, amt3)
    result = [('Marge Simpson', 1500.0, 2, 750.0),
              ('Ada Lovelace', 345.0, 1, 345.0)]
    assert t.generate_report_data() == result


def test_setup_table():
    t = mr.Transactions()
    returnval = t.setup_table()
    assert returnval.startswith("Donor Name")
    assert "Total Given" in returnval
    assert "Num Gifts" in returnval
    assert "Average Gift" in returnval


def test_setup_body():
    name, amt = ("Ada Lovelace", 345)
    d = mr.Donor(name)
    d.add_donation(amt)
    name2, amt2, amt3 = ("Marge Simpson", 500, 1000)
    d2 = mr.Donor(name2)
    d2.add_donation(amt2)
    t = mr.Transactions()
    t.add_donor(name, amt)
    t.add_donor(name2, amt2)
    t.add_donor(name2, amt3)
    returnval = t.setup_body()
    nlines = returnval.count('\n')
    assert name in returnval
    assert name2 in returnval
    assert nlines == 2


def test_letter_string():
    name, amt = ("Ada Lovelace", 345)
    d = mr.Donor(name)
    d.add_donation(amt)
    result = "Thank you, Ada Lovelace, for your generosity and recent gift of $345.00."
    assert d.generate_letter() == result

