#!/usr/bin/env python


infile ="student.txt"

all_langs = []
with open(infile) as students:
    students.readline()
    for line in students:
        line = line.strip()
        langs = line.strip(":")[1].split(",")
        if langs 
