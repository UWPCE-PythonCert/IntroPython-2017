#!/usr/bin/env python

"""
Test code for saving data to/from json with json_save
"""

import pytest

from mailroom import data_dir
from mailroom.model import Donor, DonorDB


@pytest.fixture()
def sample_db():
    return DonorDB.load_from_file(data_dir / "sample_data.json")


def test_one_donor():
    """
    creates an new donor with a couple donations
    """
    donor = Donor("Fred Flintstone", [34, 56])

    # save to a dict:
    jd = donor.to_json_compat()

    # recreate it
    donor2 = Donor.from_json_dict(jd)

    assert donor == donor2
    # Just to be extra sure:
    assert donor.name == donor2.name
    assert donor.donations == donor2.donations


def test_donor_db(sample_db):
    # Save the sample_db to a dict:

    dbd = sample_db.to_json_compat()

    # recreate it
    db2 = DonorDB.from_json_dict(dbd)

    # See if it's the same:
    jeff_bezos = db2.find_donor('jeff bezos')
    jeff_bezos.add_donation(2000)

    print(jeff_bezos)

    print(db2.donor_data.keys())

    assert db2 == sample_db

    print(db2)

    assert False


