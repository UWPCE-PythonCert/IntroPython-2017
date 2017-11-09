#! /usr/bin/env python
# comprehensions_lab.python


def count_evens(nums):
    """ Count the even numbers in a sequence using a one line comprehension
    """
    # comprehension = []
    # nums = [seq]
    # for result in nums:
    #     if result % 2 == 0
    #         comprehension.append(result)
    # print the length of comprehension

    # http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
    # Very cool explanation of the mapping of a for loop to a list
    # comprehension

    print('There are {0} evens in this seq'.format(
        len([result for result in nums if result % 2 == 0])))


if __name__ == "__main__":
    nums = [2, 3, 6, 5, 6, 12]
    count_evens(nums)
