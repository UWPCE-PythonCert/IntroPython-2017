#! /usr/bin/env python

def exchange_first_last(sequence):
    new_seq = sequence[-1:] +sequence[1:-1] + sequence[:1]
    return new_seq

print(exchange_first_last((2,3,4,5)))



def every_other_item_rem(sequence):
    new_seq = sequence[0::2]
    return new_seq

print(every_other_item_rem("Yahoo and Google"))



def remove4(sequence):
    """With the first and last 4 items removed, and every other item in between"""
    return sequence[4:-4:2]

assert remove4(tuple(range(12))) == (4, 6)
print(remove4(tuple(range(12))))


def reversed_slice(sequence):
    new_seq = sequence[::-1]
    return new_seq

print(reversed_slice("Yahoo and Google"))



def reorg_third_slice(sequence):
    size = len(sequence) // 3
    new_seq = sequence[size:] + sequence[0:size]
    return new_seq

print(reorg_third_slice(tuple(range(12))))
