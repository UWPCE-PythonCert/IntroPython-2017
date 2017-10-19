"""
Kathryn Egan

Write some functions that take a sequence as an
argument, and return a copy of that sequence:

- with the first and last items exchanged
- with every other item removed
- with the first and last 4 items removed, and every
other item in between
- with the elements reversed (just with slicing)
- with the middle third, then last third, then the
first third in the new order
"""


def exchange(items):
    """ Returns list with first and last positions
    transposed.
    Args:
        items (list) : list to alter
    Returns:
        list : items with first and last value transposed
    """
    if len(items) < 2:
        return items
    return items[-1:] + items[1:-1] + items[:1]


def remove_every_other(items):
    """ Returns a list with every other item removed.
    Args:
        items (list) : list of items to alter
    Returns:
        list : return items with every other value removed
    """
    return items[::2]


def first_last_removed(items):
    """ Returns a new list with the first and last
    four items removed and the rest with every other
    value removed. Returns list with every other
    element removed if length is <= 8.
    Args:
        items (list) : list of items to alter
    Returns:
        list : altered items
    """
    if len(items) <= 8:
        return items[::2]
    return items[4:-4:2]


def reverse_it(items):
    """ Returns a reversed version of the given items.
    Args:
        items (list) : list of items to reverse
    Returns:
        list : reversed items
    """
    return items[::-1]


def thirds(items):
    """ Returns a new list that is the middle and last
    thirds of the given items then the non-greedy
    first third. Original list if len is < 3.
    Args:
        items (list) : list of items
    Returns:
        list : middle and last followed by first third
    """
    if len(items) < 3:
        return items
    splice = len(items) // 3
    first = items[:splice]
    rest = items[splice:]
    return rest + first


def tuplify(items):
    """ Makes a tuple out of each string in
    the given list of items.
    Args:
        items (list of str) : list of strings
    Returns:
        list of tuples : list of strings as tuples
    """
    new_items = []
    for item in items:
        temp = []
        for piece in item:
            temp.append(piece)
        new_items.append(tuple(temp))
    return new_items


def listify(items):
    """ Makes a list out of each string in
    the given list of items.
    Args:
        items (list of str) : list of strings
    Returns:
        list of lists : list of strings as lists
    """
    new_items = []
    for item in items:
        temp = []
        for piece in item:
            temp.append(piece)
        new_items.append(temp)
    return new_items


def nothing(items):
    """ Returns given item as-is."""
    return items


# assign modules and their answers
tests = [
    '', 'a', 'ab', 'abc', 'abcd',
    'abcdefgh', 'abcdefghijklmnopqrstuvwxyz']
answers = {
    exchange: [
        '', 'a', 'ba', 'cba', 'dbca',
        'hbcdefga', 'zbcdefghijklmnopqrstuvwxya'],
    remove_every_other: [
        '', 'a', 'a', 'ac', 'ac', 'aceg', 'acegikmoqsuwy'],
    first_last_removed: [
        '', 'a', 'a', 'ac', 'ac', 'aceg', 'egikmoqsu'],
    reverse_it: [
        '', 'a', 'ba', 'cba', 'dcba', 'hgfedcba',
        'zyxwvutsrqponmlkjihgfedcba'],
    thirds: [
        '', 'a', 'ab', 'bca', 'bcda',
        'cdefghab', 'ijklmnopqrstuvwxyzabcdefgh']}
versions = {'STRING': nothing, 'TUPLE': tuplify, 'LIST': listify}

for module in answers:
    for test, answer in zip(tests, answers[module]):
        for version_name, versioner in versions.items():
            # convert test and answer to string, tuple, and list
            result = module(versioner(test))
            answer = versioner(answer)
            # verify that result and answer match
            if result != answer:
                print('*{} ERROR* in {}:'.format(
                    version_name, module.__name__))
                print('\tSYSTEM RESULT: {}'.format(result))
                print('\tANSWER: {}'.format(answer))
    else:
        print('passed {} module'.format(module.__name__))
