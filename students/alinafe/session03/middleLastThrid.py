#!/usr/bin/env python3
#with the middle third, then last third, then the first third in the new order
def middle_third_last_third(seq):

    if type(seq) is tuple:
        seq = list(seq)
        del seq[1:6:2]
        print(tuple(seq))
        return tuple(seq)
    if type(seq) is list:
        del seq[1:6:2]
        print(seq)
        return seq
    else:
        seq=seq[::2]
        print(seq)
        return seq

if __name__ == "__main__":
    # some tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = [2, 54, 13, 12, 5, 32]
    assert middle_third_last_third(a_string) == "ti sasrn"
    assert middle_third_last_third(a_tuple) == (2,13, 5)
    assert middle_third_last_third(a_list) == [2, 13, 5]
    print("All tests passed")

