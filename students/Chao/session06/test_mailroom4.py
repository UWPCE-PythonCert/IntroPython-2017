#!/usr/bin/env python

import mailroom4
from mailroom4 import donor_list, add_donor, add_donation, email, gen_report, email_all
import os.path

def test_donor_list():
    """ Test donor list function """
    dl = donor_list()
    assert 'John Doe' in dl
    assert 'Jane Doe' in dl

def test_add_donor():
    """ Test add_donor function """
    add_donor('Test Donor')
    assert 'Test Donor' in mailroom4.donors
    mailroom4.donors.pop('Test Donor')

def test_add_donation():
    """ Test add_donation function """
    add_donation('Jane Doe', 123.22)
    assert mailroom4.donors.get('Jane Doe')[-1] == 123.22

def test_email():
    """ Test email function """
    m = email('John Doe').strip()
    assert m.startswith('Dear')
    assert m.endswith('Management')
    assert 'donation of $700' in m

def test_gen_report():
    """ Test gen_report function """
    r = gen_report('John Doe')
    assert r.startswith('* John Doe')
    assert r.endswith('426.17 *')
    assert '852.33' in r
    assert ' 2 ' in r

def test_email_all():
    """ Test email_all function """
    email_all()
    assert os.path.isfile('John_Doe.txt')
    assert os.path.isfile('Jane_Doe.txt')
