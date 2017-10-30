def elements_reversed(seq):
    """ Return a copy of a sequence with the elements reversed
(just with slicing)
"""
    new_seq = seq[-1:0:-1] + seq[0:1]
    return new_seq


tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
string_1 = 'I love Python'
list_1 = [5, 8, 6, 10, 2, 4, 5, 15, 20]

assert elements_reversed(tuple_1) == (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
assert elements_reversed(string_1) == 'nohtyP evol I'
assert elements_reversed(list_1) == [20, 15, 5, 4, 2, 10, 6, 8, 5]
