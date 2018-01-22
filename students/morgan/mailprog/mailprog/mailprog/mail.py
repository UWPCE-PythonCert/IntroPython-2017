#!/usr/bin/env python


from ui import main_loop
from dataModels import Storage

# from mailprog.functions import read_donors

if __name__ == "__main__":
    infile = "data/donors.csv"
    # infile = "data/donors.txt"
    donor_objects = []

    DB = Storage()

    DB.read_donors(infile, donor_objects)

    # for x in DB.donors:
    #     print(x.name)

    main_loop(DB)


