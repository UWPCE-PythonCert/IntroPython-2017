#!/usr/bin/env python

"""
Script to make a "fake" collection of donors

This version use's Chris' OO solution, but you could adapt it
for your version of the code.
"""
from random import randint


def rand_name():
    return "".join([chr(randint(97, 122)) for i in range(randint(5, 10))])


def gen_name():
    name = " ".join((rand_name().capitalize(),
                     chr(randint(65, 90)) + ".",
                     rand_name().capitalize()))
    return name


def make_lots_of_donors(db, n=100):
    for i in range(n):
        name = gen_name()
        donor = db.add_donor(name)
        # Add a bunch of random donations
        num_don = randint(100, 200)
        donor.donations = [randint(10, 30) * 100 for i in range(num_don)]

    return db


if __name__ == "__main__":

    import mailroom
    db = mailroom.DonorDB()
    make_lots_of_donors(db, 100)
    print(db.generate_donor_report())




