#!/usr/bin/env python
# Description: Write some functions that take a sequence as an argument, and return a copy of that sequence:
# with the first and last items exchanged.
# with every other item removed
# with the first and last 4 items removed, and every other item in between
# with the elements reversed (just with slicing)
# with the middle third, then last third, then the first third in the new order
# Comments: Execute in Python3.6
# Last modified on 10/22/2017 by davidkan@


def show_current_string():

    a_string = "hello there this is a string for this slicing lab"

    return  a_string


def show_first_last(seq):

    a_list = seq.split(' ')

    return (' '.join(a_list[::len(a_list) - 1]))


def exchange_first_last(seq):

    a_list = seq.split(' ')

    first_word = a_list[0]
    last_word = a_list[-1]
    words_between = ' '.join(a_list[1:-1])

    return (' '.join([last_word, words_between, first_word]))


def remove_every_other_items(seq):

    a_list = seq.split(' ')

    return (' '.join(a_list[::2]))


def remove_every_other_items_in_between(seq):

    a_list = seq.split(' ')

    return (' '.join(a_list[1:5][::2]))


def reverse_elements(seq):

    a_list = seq.split(' ')

    return  (' '.join(a_list[::-1]))


def get_thirds(seq):

    a_list = seq.split(' ')
    index = len(a_list) // 3

    middle_third = ' '.join(a_list[index:-index])
    last_third = ' '.join(a_list[-index:])
    first_third = ' '.join(a_list[:index])

    return (' '.join([middle_third, last_third, first_third]))


if __name__ == '__main__':

    a_string = show_current_string()
    exchage_result = exchange_first_last(a_string)
    first_last_result = show_first_last(a_string)
    every_other_result = remove_every_other_items(a_string)
    item_in_between_result = remove_every_other_items_in_between(a_string)
    reverse_result = reverse_elements(a_string)
    third_result = get_thirds(a_string)

    print("Current string: {}\n".format(a_string))
    print("First and last item: {}\n".format(first_last_result))
    print("First and last item exchange: {}\n".format(exchage_result))
    print("Every other item removed: {}\n".format(every_other_result))
    print("First and last 4 items removed, and every other item in between: {}\n".format(item_in_between_result))
    print("The elements reversed (just with slicing): {}\n".format(reverse_result))
    print("The middle third, then last third, then the first third in the new order: {}\n".format(third_result))
