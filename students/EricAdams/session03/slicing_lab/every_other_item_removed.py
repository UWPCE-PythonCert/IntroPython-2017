def every_other_item_removed(seq):
    """ Return a copy of a sequence with every other item
removed.
"""
    new_seq = seq[0::2]
    return new_seq


tuple_1 = (1, 2, 3, 4)
string_1 = ('I love Python')
list_1 = [5, 8, 6, 10]

assert every_other_item_removed(tuple_1) == (1, 3)
assert every_other_item_removed(string_1) == 'Ilv yhn'
assert every_other_item_removed(list_1) == [5, 6]
