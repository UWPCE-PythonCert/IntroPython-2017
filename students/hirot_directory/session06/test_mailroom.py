#!/usr/bin/env python3

"""
Unit Test for mailroom6_3.py

"""

import pytest
import mailroom6_3 as mr


def test_donor_dict():
    """ Test to make sure we make put everything in a dictionary. """
    result = mr.donor_dict
    assert 'Paul Allen' in result.keys()
    assert 'Jeff Bezos' in result.keys()

