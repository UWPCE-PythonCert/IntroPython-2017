#!/usr/bin/env python3
#with the elements reversed (just with slicing)
def elements_reversed(seq):

     if isinstance(seq, tuple):
        seq = list(seq)
        seq=seq[::-1]
        print(tuple(seq))
        return tuple(seq)
     elif isinstance(seq, list):
        seq=seq[::-1]
        print(seq)
        return seq
     elif isinstance(seq, str):
        seq=seq[::-1]
        print(seq)
        return seq

if __name__ == "__main__":
    # some tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = [2, 54, 13, 12, 5, 32]
    assert elements_reversed(a_string) == "gnirts a si siht"
    assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert elements_reversed(a_list) == [32, 5, 12, 13, 54, 2]
    print("All tests passed")

