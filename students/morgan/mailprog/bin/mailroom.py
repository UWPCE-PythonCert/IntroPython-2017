#!/usr/bin/env python

import sys
from mailprog.ui import main_loop
from mailprog.dataModels import Storage
from mailprog.functions import read_donors



if __name__ == "__main__":
    infile = "mailprog/data/donors.txt"
    donor_objects = []

    DB = Storage()

    read_donors(infile, DB, donor_objects)

    main_loop(DB)