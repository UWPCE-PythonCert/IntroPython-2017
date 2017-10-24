#!/usr/bin/env python

# first_last6

def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

assert first_last6([1, 2, 6]) == True
assert first_last6([6, 1, 2, 3]) == True
assert first_last6([13, 6, 1, 2, 3]) == False

# same_first_last

def same_first_last(nums):
    return len(nums) >= 1 and (nums[0] == nums[-1])
assert same_first_last([1, 2, 3]) == False
assert same_first_last([1, 2, 3, 1]) == True
assert same_first_last([1, 2, 1]) == True


# make_pi

def make_pi():
    return [3, 1, 4]
assert make_pi() == [3, 1, 4]


# common_end

def common_end(a, b):
    return (a[0] == b[0]) or (a[-1] == b[-1])
assert common_end([1, 2, 3], [7, 3]) == True
assert common_end([1, 2, 3], [7, 3, 2]) == False
assert common_end([1, 2, 3], [1, 3]) == True


# sum3

def sum3(nums):
    return sum(nums)

assert sum3([1, 2, 3]) == 6
assert sum3([5, 11, 2]) == 18
assert sum3([7, 0, 0]) == 7


# rotate_left3

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

assert rotate_left3([1, 2, 3]) == [2, 3, 1]
assert rotate_left3([5, 11, 9]) == [11, 9, 5]
assert rotate_left3([7, 0, 0]) == [0, 0, 7]


# reverse3

def reverse3(nums):
    return nums[::-1]

assert reverse3([1, 2, 3]) == [3, 2, 1]
assert reverse3([5, 11, 9]) == [9, 11, 5]
assert reverse3([7, 0, 0]) == [0, 0, 7]


# max_end3

def max_end3(nums):
    return [max(nums[0], nums[-1])] * 3
assert max_end3([1, 2, 3]) == [3, 3, 3]
assert max_end3([11, 5, 9]) == [11, 11, 11]
assert max_end3([2, 11, 3]) == [3, 3, 3]


# sum2

def sum2(nums):
    if len(nums) == 0:
    	return 0
    elif len(nums) < 2:
    	return sum(nums)
    else:
    	return nums[0] + nums[1]

assert sum2([1, 2, 3]) == 3
assert sum2([1, 1]) == 2
assert sum2([1, 1, 1, 1]) == 2


#middle_way

def middle_way(a, b):
    return [a[1], b[1]]

assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]
assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]
assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]


# make_ends

def make_ends(nums):
    return [nums[0], nums[-1]]

assert make_ends([1, 2, 3]) == [1, 3]
assert make_ends([1, 2, 3, 4]) == [1, 4]
assert make_ends([7, 4, 6, 2]) == [7, 2]


# has23

def has23(nums):
    return nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3

assert has23([2, 5]) == True
assert has23([4, 3]) == True
assert has23([4, 5]) == False