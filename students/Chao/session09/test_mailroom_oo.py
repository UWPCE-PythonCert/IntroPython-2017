#!/usr/bin/env python

from mailroom_oo import Donor

def test_init():
    Donor('John Doe', 450)
    assert True

def test_name_amount():
    d = Donor('John Doe', 450)
    assert d.name == 'John Doe'
    assert d.amount[0] == 450

def test_new_donation():
    d = Donor('John Doe', 450)
    d.new_donation(50)
    d.new_donation(15)
    assert d.amount[1] == 50
    assert d.amount[2] == 15

def test_total_donation():
    d = Donor('John Doe', 450)
    d.new_donation(50)
    d.new_donation(15)
    assert d.total_donation == 515