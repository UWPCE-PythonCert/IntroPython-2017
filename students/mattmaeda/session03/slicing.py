#!/usr/bin/python

def flip_first_and_last(seq):
    if len(seq) > 1:
        return seq[-1] + seq[1:-1] + seq[0]
    else:
        return seq


def every_other(seq):
    return seq[::2]


def four_off_ends_and_every_other(seq):
    if len(seq) <= 8:
        return []
    else:
        return seq[4:-4][::2]


def reversed_sliced(seq):
    return seq[::-1]


def flip_thirds(seq):
    if len(seq) % 3 != 0:
        return seq
    else:
        slice_idx = len(seq)//3
        return seq[slice_idx:-slice_idx] + seq[-slice_idx:] + seq[0:slice_idx]

if __name__ == "__main__":
    assert flip_first_and_last("abcd") == "dbca"
    assert flip_first_and_last("a") == "a"
    assert flip_first_and_last("") == ""

    assert every_other("ababab") == "aaa"
    assert every_other("") == ""
    assert every_other([]) == []
    assert every_other("a") == "a"

    assert four_off_ends_and_every_other("12345678") == []
    assert four_off_ends_and_every_other([1,2,3,4,5,6,7,8]) == []
    assert four_off_ends_and_every_other("123456789") == "5"
    assert four_off_ends_and_every_other("12345678901") == "57"

    assert reversed_sliced("1234") == "4321"
    assert reversed_sliced([1,2,3,4]) == [4,3,2,1]
    assert reversed_sliced([1]) == [1]
    assert reversed_sliced("") == ""

    assert flip_thirds("12") == "12"
    assert flip_thirds("123") == "231"
    assert flip_thirds("112233") == "223311"
    assert flip_thirds("112233444") == "233444112"

    print("All tests passed!")
