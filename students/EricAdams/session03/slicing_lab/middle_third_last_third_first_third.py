def middle_third_last_third_first_third(seq):
    """ Return a copy of a sequence with the middle third,
then last third, then the first third in the new order
"""
    # slice index of last first_third_seq element
    one_third_len = len(
        seq) // 3
    # slice index of last middle_third_seq element
    two_third_len = 2 * one_third_len
    first_third_seq = seq[0:one_third_len]
    middle_third_seq = seq[one_third_len:(two_third_len)]
    last_third_seq = seq[two_third_len:]
    new_seq = middle_third_seq + last_third_seq + first_third_seq
    return new_seq


tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
string_1 = 'I love Python'
list_1 = [5, 8, 6, 10, 2, 4, 5, 15, 20]


assert(middle_third_last_third_first_third(
    tuple_1)) == (5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4)
assert(middle_third_last_third_first_third(string_1)) == 've PythonI lo'
assert(middle_third_last_third_first_third(
    list_1)) == [10, 2, 4, 5, 15, 20, 5, 8, 6]
