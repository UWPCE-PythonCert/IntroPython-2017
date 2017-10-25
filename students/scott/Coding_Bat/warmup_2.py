#!/usr/bin/env python

# string_times

def string_times(str, n):
    return str * n
assert string_times('Hi', 2)== 'HiHi'
assert string_times('Hi', 3) == 'HiHiHi'
assert string_times('Hi', 1) == 'Hi'


# front_times

def front_times(str, n):
    if len(str) < 3:
        return str*n
    else:
        return str[0:3] * n
assert front_times('Chocolate', 2) == 'ChoCho'
assert front_times('Chocolate', 3) == 'ChoChoCho'
assert front_times('Abc', 3) == 'AbcAbcAbc'

# string_bits

def string_bits(str):
    return str[::2]
assert string_bits('Hello') == 'Hlo'
assert string_bits('Hi') == 'H'
assert string_bits('Heeololeo') == 'Hello'

# string_splosion

def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i+1]
    return result
assert string_splosion('Code') == 'CCoCodCode'
assert string_splosion('abc') == 'aababc'
assert string_splosion('ab') == 'aab'

# last2

def last2(str):    
    count = 0
    for i in range(len(str)-2):
        if str[i:i+2] == str[-2:]:
            count += 1  
    return count

assert last2('hixxhi') == 1
assert last2('xaxxaxaxx') == 1
assert last2('axxxaaxx') == 2

#array_count9

def array_count9(nums):
    return nums.count(9)

assert array_count9([1, 2, 9]) == 1
assert array_count9([1, 9, 9]) == 2
assert array_count9([1, 9, 9, 3, 9]) == 3


# array_front9

def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    
    for i in range(end):
        if nums[i] == 9:
            return True
    return False

assert array_front9([1, 2, 9, 3, 4]) == True
assert array_front9([1, 2, 3, 4, 9]) == False
assert array_front9([1, 2, 3, 4, 5]) == False

# array123

def array123(nums):
    for i in range(len(nums)-2):
        if (nums[i]==1) and (nums[i+1]==2) and (nums[i+2]==3):
        	return True
    return False

assert array123([1, 1, 2, 3, 1]) == True
assert array123([1, 1, 2, 4, 1]) == False
assert array123([1, 1, 2, 1, 2, 3]) == True

# string_match

def string_match(a, b):

    short = min(len(a), len(b))
    count = 0
    
    for i in range(short-1):
        a_bit = a[i:i+2]
        b_bit = b[i:i+2]
        if a_bit == b_bit:
            count = count + 1

    return count

assert string_match('xxcaazz', 'xxbaaz') == 3
assert string_match('abc', 'abc') == 2
assert string_match('abc', 'axc') == 0