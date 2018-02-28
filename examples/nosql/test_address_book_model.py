#!/usr/bin/env python

"""
test code for address book model code
if testing mongo, remember to start database first
$ mongod --dbpath=mongo_data/
"""

import pytest

import ZODB

# import address_book_model as model
# import address_book_zodb as model
import address_book_mongo as model


@pytest.fixture
def a_book():
    return model.create_sample()


def test_name_search(a_book):
    """find a single person by first name"""

    people = a_book.find_people('chris')

    assert len(people) == 1
    assert people[0].first_name == 'Chris'
    assert people[0].last_name == 'Barker'


def test_name_search2(a_book):
    people = a_book.find_people('barKer')
    first_names = [p.first_name for p in people]

    assert 'Chris' in first_names
    assert 'Emma' in first_names
    assert 'Donna' in first_names


def test_zip_search(a_book):
    locations = a_book.find_zip_codes(98105)

    assert len(locations) == 1
    assert locations[0].name == 'Python Certification Program'


def test_state_search(a_book):
    locations = a_book.find_state('WA')
    names = [l.name for l in locations]

    assert "The Barkers" in names
    assert "Python Certification Program" in names


# def test_household():
#     house = model.household()


# def test_add_person_to_household(a_book):
#     sassy = model.Person(first_name="Sassy",
#                    last_name="Barker"
#                    )

#     print(a_book.households)
#     house = a_book.locations[0]
#     house.people.append(sassy)


#     db = ZODB.DB('address_book_zodb.fs')
#     connection = db.open()
#     root = connection.root
#     a_book = root.address_book

#     house = a_book.households[0]
#     print(house)

#     assert False




