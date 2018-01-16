#!/usr/bin/env python

from ui import main_loop
from dataModels import Storage
from functions import read_donors



if __name__ == "__main__":
    infile = "data/donors.txt"
    donor_objects = []

    DB = Storage()

    read_donors(infile, DB, donor_objects)

    main_loop(DB)