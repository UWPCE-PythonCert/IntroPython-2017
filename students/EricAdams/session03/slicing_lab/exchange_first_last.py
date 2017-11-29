def exchange_first_last(seq):
    """Return a copy of a sequence with the first and last items
exchanged.
"""
    copy_seq = seq[-1:] + seq[1:-1] + seq[0:1]
    return copy_seq


tuple_1 = (1, 2, 3, 4)
string_1 = ('I love Python')
list_1 = [5, 8, 6, 10]

assert exchange_first_last(tuple_1) == (4, 2, 3, 1)
assert exchange_first_last(string_1) == 'n love PythoI'
assert exchange_first_last(list_1) == [10, 8, 6, 5]
