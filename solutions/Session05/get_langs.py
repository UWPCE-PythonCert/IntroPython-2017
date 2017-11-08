#!/usr/bin/env python

"""
script to determine what programming languages students came to this
class with

This version updated to use collections.Counter, to count and maintain
a set at the same time.

And comprehensions...

"""

import collections  # lots of neat stuff in there

file_path = '../../Examples/Session01/students.txt'

# use a counter to ensure unique values and keep track of count
all_langs = collections.Counter()

f = open(file_path)  # default read text mode

f.readline()   # read and toss the header

for line in f:
    # partition is more robust tha split() for mal-formed data.
    langs = line.partition(':')[2]
    for lang in [lang.strip().capitalize() for lang in langs.split(',')
                 if lang and (not lang[0].isupper())]:
        all_langs[lang] += 1


def sort_by_value(item):
    return item[1]


# print them our neatly, sorted by most popular language
for lang, count in sorted(all_langs.items(), key=sort_by_value, reverse=True):
    print("{:25}: {:d} students".format(lang, count))
