#!/usr/bin/env python3

"""

session06:
    Unit Test for mailroom5.py (in session05 folder)

"""

import pytest
import mailroom5 as mr


def test_donor_dict():
    """ Test to make sure we make put everything in a dictionary. """
    result = mr.donor_dict
    assert 'Paul Allen' in result.keys()

