
def first_and_last_four_and_every_other_between(seq):
""" Return a copy of a sequence with the first and
last 4 items removed, and every other item in between.
"""
    new_seq = seq[1:-4:2]
    return new_seq

tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
string_1 = ('I love Python')
list_1 = [5, 8, 6, 10, 2, 4, 5, 15, 20]

assert first_and_last_four_and_every_other_between(tuple_1) == (2, 4, 6)
assert first_and_last_four_and_every_other_between(string_1) == ' oeP'
assert first_and_last_four_and_every_other_between(list_1) == [8, 10]