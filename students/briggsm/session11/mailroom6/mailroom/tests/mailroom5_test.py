'''Test for Mailroom5'''

import json
import mock
from mailroom5 import Donor
import mailroom5 as M5

persistantdata = "mailroomdata_try.json"
maildata = M5.open_json(persistantdata)


def test_donor_init():
    d = Donor()

    assert d.Name == "Name me"


def test_add_donationfunctions():
    d = Donor("Test")
    d + 5
    d + 1

    assert d.Donations == [5, 1]
    assert d.DonationNumber == 2
    assert d.DonationTotal == 6
    assert d.AverageDonations == 3


def test_open_json():
    filename = "mailroomdata_try.json"
    records = M5.open_json(filename)

    assert records["Fanny Pepper"].Donations == [10.0, 20.0, 30.0]
    assert records["Jo Fang"].Donations == [50.0]
    assert records["John Dill"].Donations == [10.0, 20.0, 30.0]


def test_write_json():
    filename = "mailroomdata_try.json"
    jsonrecords = json.loads('''
    {"John Dill": [10.0, 20.0, 30.0], 
    "Sarah Pickle": [10.0, 20.0, 30.0], 
    "Ornett Salt": [10.0, 20.0, 30.0], 
    "Fanny Pepper": [10.0, 20.0, 30.0], 
    "Jo Fang": [50.0]}
    ''')
    objrecords = {}
    for key, value in jsonrecords.items():
        record = Donor(key, value)
        objrecords[key] = record
    M5.write_json(objrecords, filename)
    inrecords = M5.open_json(filename)

    assert inrecords["Fanny Pepper"].Donations == [10.0, 20.0, 30.0]
    assert inrecords["Jo Fang"].Donations == [50.0]
    assert inrecords["John Dill"].Donations == [10.0, 20.0, 30.0]



def test_make_thanks():
    '''Takes the name and donation and return a thank you text.'''
    assert M5.make_thanks(name="Ed", donation=100) == '''
    Dear Ed,

    Thank you for your generous donation of $ 100. Your
    support enables us to keep doing good in the world. Which means
    your money, earned through whatever means money is earned in
    the amounts you have earned, is now doing good. We thank you. The
    world thanks you.

    Regards,
    Foundation Against Suffering

    '''

# To do ... more tests