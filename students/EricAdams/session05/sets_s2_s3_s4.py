"""
file sets_s2_s3_s4.py
Create sets s2, s3 and s4 that contain numbers from zero through twenty,
divisible 2, 3 and 4.

Do this with one set comprehension for each set.
What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
create a sequence that holds all the divisors you might want –
could be 2,3,4, or could be any other arbitrary divisors.
loop through that sequence to build the sets up – so no repeated code. you
will end up with a list of sets – one set for each divisor in your sequence.
The idea here is that when you see three (Or more!) lines of code that are
almost identical, then you you want to find a way to generalize that code
and have it act on a set of inputs, so the actual code is only written once.
Extra credit: do it all as a one-liner by nesting a set comprehension inside
a list comprehension.
"""

s2 = {y for y in range(0, 21) if y % 2 == 0}
s3 = {y for y in range(0, 21) if y % 3 == 0}
s4 = {y for y in range(0, 21) if y % 4 == 0}


def numbers_divisible_by_a_seq_of_divisors(seq):
    """ Create a list of sequences each sequence member divisible
     by a list of divisors.
    :param a list of divisors, (integers).
    :return a list of sets.
    """
    list_of_sets_of_sequences = []
    # s = set()
    for divisor in seq:
        s = set()
        for y in range(0, 21):
            if y % divisor == 0:
                s.add(y)
        list_of_sets_of_sequences.append(s.copy)
    for i in range(0, len(seq)):
        print('Set of numbers divisible by {} is {}'.format(
            seq[i], list_of_sets_of_sequences[i]()))


numbers_divisible_by_a_seq_of_divisors([2, 4, 5])
