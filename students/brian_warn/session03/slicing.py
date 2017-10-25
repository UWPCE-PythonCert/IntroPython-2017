#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python

'''
TASKS
Write some functions that take a sequence as an argument,
and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed
with the first and last 4 items removed, and every other item in between
with the elements reversed (just with slicing)
with the middle third, then last third, then the first third in the new order
NOTE: These should work with ANY sequence – but you can use strings to test,
if you like.
'''

def exchange_first_last(seq):
    a_new_sequence = seq[-1:]+seq[1:-1]+seq[:1]
    return a_new_sequence

def every_other_removed(seq):
    a_new_sequence = seq[::2]
    return a_new_sequence

def items_reversed(seq):
    a_new_sequence = seq[::-1]
    return a_new_sequence

def first_last_four(seq):
    a_new_sequence = seq[5:-4]
    return a_new_sequence

def third_seqs(seq):
    ''' middle 1/3, last 1/3, first 1/3'''
    third = len(seq)//3
    middle_third_starting_number = third
    last_third_starting_number = len(seq) - third
    print("Sequence length: ", len(seq))
    print("third: ", third)
    print("third-1: ", third - 1)
    print("middle_third_starting_number: ", middle_third_starting_number)
    print("last_third_starting_number: ", last_third_starting_number)
    print("third+1: ", third + 1)
    mid_third_seq = seq[middle_third_starting_number:last_third_starting_number]
    last_third_seq = seq[last_third_starting_number:]
    first_third_seq = seq[:third]
    print("Middle 1/3 sequence is: ", mid_third_seq)
    print("Last 1/3 sequence is: ", last_third_seq)
    print("First 1/3 sequence is: ", first_third_seq)
    result = mid_third_seq + last_third_seq + first_third_seq
    return result

# Some tests and some outputs:
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

print("\nOriginal string:", a_string)
print("\nString with first and last items exchanged: ", exchange_first_last(a_string))
print("\nString with every other item removed: ", every_other_removed(a_string))
print("\nTuple with every other item removed: ", every_other_removed(a_tuple))
print("\nString with the first and last 4 items removed, print every other item in between: ",first_last_four(a_string))
print("\nReversed string result: ", items_reversed(a_string))
print("\nMiddle third, last third, first third: ", third_seqs(a_string))

# Some tests:
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert every_other_removed(a_tuple) == (2, 13, 5)
assert third_seqs(a_string) == "is a stringthis "