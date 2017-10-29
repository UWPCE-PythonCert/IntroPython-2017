#!/usr/bin/env python3
#with the first and last 4 items removed, and every other item in between
def first_last_four_removed(seq):
    if isinstance(seq, tuple):
        seq = list(seq)
        del seq[-4:]
        del seq[:-4]
        #seq.pop(0)
        return tuple(seq)
    elif isinstance(seq, list):
        del seq[-4:]
        del seq[:-4]
        #seq.pop(0)
        return seq
    elif isinstance(seq, str):
        seq=seq[1:-4]
        return seq

if __name__ == "__main__":
    # some tests
    a_string = "this is a string this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32,2, 54, 13, 12, 5, 3)
    a_list = [2, 54, 13, 12, 5, 32,2, 54, 13, 12, 5, 3]
    assert first_last_four_removed(a_string) == "his is a string this is a st"
    assert first_last_four_removed(a_tuple) == (5, 32, 2, 54)
    assert first_last_four_removed(a_list) == [5, 32, 2, 54]
    print("All tests passed")

