#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
 # test_mailroom.py

import mailroom_from_chb

import pytest


def test_get_donor_db():
    result = mailroom_from_chb.get_donor_db()
    assert result == ('william gates iii': ("William Gates III", [653772.32, 12.17]),
        'jeff bezos': ("Jeff Bezos", [877.33]),
        'paul allen': ("Paul Allen", [663.23, 43.87, 1.32]),
        'mark zuckerberg': ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),)
