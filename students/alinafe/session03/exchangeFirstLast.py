#!/usr/bin/env python3
#with the first and last items exchanged.
def exchange_first_last(seq):

    if isinstance(seq, tuple):
        seq=list(seq)
        seq += [seq.pop(0)]
        seq.insert(0, seq.pop(-2))
        return tuple(seq)
    elif isinstance(seq, list):
        seq += [seq.pop(0)]
        seq.insert(0, seq.pop(-2))
        return seq
    elif isinstance(seq, str):
        seq=seq[-1]+seq[1:-1]+seq[0]
        return seq

print(exchange_first_last(1))
if __name__ == "__main__":
    # some tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = [2, 54, 13, 12, 5, 32]
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_list) == [32, 54, 13, 12, 5, 2]
    print("All tests passed")
