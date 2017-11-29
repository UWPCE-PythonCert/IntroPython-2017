#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
 # test_mailroom.py

import mailroom_from_chb as mr

import pytest


def test_get_donor_db():
    result = mr.get_donor_db()
    assert result == {'william gates iii': ("William Gates III", [653772.32, 12.17]),
        'jeff bezos': ("Jeff Bezos", [877.33]),
        'paul allen': ("Paul Allen", [663.23, 43.87, 1.32]),
        'mark zuckerberg': ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),}

def test_list_donors():
    result = mr.list_donors()
    assert result == ["Donor list:"]
