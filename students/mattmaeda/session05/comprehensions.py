#!/usr/bin/env python3

# Problems from
# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/comprehensions_lab.html#exercise-comprehensions

def count_evens(num_list):
    # http://codingbat.com/prob/p189616
    # Using a list comprehension, return the number of even integers in the
    # given list.
    return len([i for i in num_list if i % 2 == 0])


def dict_formatter(ref_dict):
    # dict/set problem 1
    #
    # Print the dict by passing it to a string format method, so that you get
    # something like:
    #
    # “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek
    # salad, and lasagna pasta”
    return "%(name)s is from %(city)s, and he likes %(cake)s cake, %(fruit)s " \
           "fruit, %(salad)s salad and %(pasta)s pasta" % {k: v for k, v in ref_dict.items()}


def int_to_hex_mapping(n):
    # dict/set problems 2 and 3
    #
    # Using a list comprehension, build a dictionary of numbers from zero to
    # fifteen and the hexadecimal equivalent (string is fine). (the hex()
    # function gives you the hexidecimal representation of a number as a string)
    #
    # Do the previous entirely with a dict comprehension – should be a one-liner
    return {i: hex(i)for i in range(n+1)}


def count_letter_a_in_dict(ref_dict):
    # dict/set problem 4
    #
    # Using the dictionary from item (1): Make a dictionary using the same keys
    # but with the number of ‘a’s in each value. You can do this either by
    # editing the dict in place, or making a new one. If you edit in place make
    # a copy first!
    return {k: v.count("a") for k,v in ref_dict.items()}


def set_comprehensions(divisors, max_range):
    # dict/set problem 5
    #
    # Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    # divisible 2, 3 and 4.
    #
    #   a. Do this with one set comprehension for each set.
    #   b. What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
    #       1. create a sequence that holds all the divisors you might want –
    #          could be 2,3,4, or could be any other arbitrary divisors.
    #       2. loop through that sequence to build the sets up – so no repeated
    #          code. you will end up with a list of sets – one set for each
    #          divisor in your sequence.
    #       3. The idea here is that when you see three (Or more!) lines of code
    #          that are almost identical, then you you want to find a way to
    #          generalize that code and have it act on a set of inputs, so the
    #          actual code is only written once.
    #   c. Extra credit: do it all as a one-liner by nesting a set comprehension
    #      inside a list comprehension. (OK, that may be getting carried away!)
    return [{i for i in range(max_range+1) if i % d == 0} for d in divisors]


if __name__ == "__main__":
    l = [1,2,3,4]
    assert count_evens(l) == 2

    l = [1,1,3,5]
    assert count_evens(l) == 0

    l = [2,22222,4,6,8]
    assert count_evens(l) == 5

    l = [0,1,3,5]
    assert count_evens(l) == 1

    food_prefs = {"name": "Chris",
                  "city": "Seattle",
                  "cake": "chocolate",
                  "fruit": "mango",
                  "salad": "greek",
                  "pasta": "lasagna"}

    assert dict_formatter(food_prefs) == "Chris is from Seattle, and he " \
                                         "likes chocolate cake, mango fruit, " \
                                         "greek salad, and lasagna pasta"

    assert int_to_hex_mapping(15) == {0: '0x0', 1: '0x1', 2: '0x2', 3: '0x3',
                                      4: '0x4', 5: '0x5', 6: '0x6', 7: '0x7',
                                      8: '0x8', 9: '0x9', 10: '0xa', 11: '0xb',
                                      12: '0xc', 13: '0xd', 14: '0xe', 15: '0xf'}


    assert count_letter_a_in_dict(food_prefs) == {"name": 0, "city": 1,
                                                  "cake": 1, "fruit": 1,
                                                  "salad": 0, "pasta": 3}

    assert set_comprehensions([2,3,4], 20) == [{0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20},
                                               {0, 3, 6, 9, 12, 15, 18},
                                               {0, 4, 8, 12, 16, 20}]
    print("All tests passed!")
