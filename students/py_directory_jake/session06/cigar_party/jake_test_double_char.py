#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of cigars.
Return True if the party with the given values is successful,
or False otherwise.
"""


# you can change this import to test different versions
from jake_double_char import double_char
# from cigar_party import cigar_party2 as cigar_party
# from cigar_party import cigar_party3 as cigar_party


def test_1():
    assert double_char('Test') == 'TTeesstt'

def test_2():
    assert double_char('Japan') == 'JJaappaann'

def test_3():
    assert double_char('Hurricane') == 'HHuurrrriiccaannee'

