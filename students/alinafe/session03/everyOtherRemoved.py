#!/usr/bin/env python3
#with every other item removed
def every_other_removed(seq):

    if type(seq) is tuple:
        seq = list(seq)
        #seq[1:6:2] = []
        del seq[1:6:2]
        print(tuple(seq))
        return tuple(seq)
    elif type(seq) is list:
        del seq[1:6:2]
        print(seq)
        return seq
    if type(seq) is str:
        seq=seq[::2]
        print(seq)
        return seq

if __name__ == "__main__":
    # some tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = [2, 54, 13, 12, 5, 32]
    assert every_other_removed(a_string) == "ti sasrn"
    assert every_other_removed(a_tuple) == (2,13, 5)
    assert every_other_removed(a_list) == [2, 13, 5]
    print("All tests passed")

