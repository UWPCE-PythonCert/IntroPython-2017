#!/usr/bin/env python


from mailprog.ui import main_loop
from mailprog.dataModels import Storage


if __name__ == "__main__":
    infile = "mailprog/data/donors.csv"

    donor_objects = []

    DB = Storage()

    DB.read_donors(infile, donor_objects)

    main_loop(DB)


