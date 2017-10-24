#!/usr/bin/env python

# sleep_in

def sleep_in(weekday, vacation):
    return not weekday or vacation


assert sleep_in(False, False) is True
assert sleep_in(True, False) is False
assert sleep_in(False, True) is True


# monkey_trouble

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

assert monkey_trouble(True, True) is True
assert monkey_trouble(False, False) is True
assert monkey_trouble(True, False) is False

# sum_double

def sum_double(a, b):
    if a == b:
        return (a+b)*2
    else:
        return (a+b)

assert sum_double(1, 2) == 3
assert sum_double(3, 2) == 5
assert sum_double(2, 2) == 8

# diff21

def diff21(n):
    if n > 21:
        return abs(b-21) * 2
    else:
        return abs(n-21)
diff21(19) == 2
diff21(10) == 11
diff21(21) == 0


# parrot_trouble

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)
assert parrot_trouble(True, 6) is True
assert parrot_trouble(True, 7) is False
assert parrot_trouble(False, 6) is False


# makes10

def makes10(a, b):
    return (a == 10) or (b == 10) or ((a+b) == 10)

assert makes10(9, 10) is True
assert makes10(9, 9) is False
assert makes10(1, 9) is True


# near_hundred

def near_hundred(n):
    return (abs(n-100) <= 10) or (abs(n-200) <= 10)

assert near_hundred(93) is True
assert near_hundred(90) is True
assert near_hundred(89) is False

# pos_neg

def pos_neg(a, b, negative):
    if negative is True:
        return (a < 0 and b < 0)
    else:
        return ((a<0 and b>0) or (a>0 and b<0))

assert pos_neg(1, -1, False) is True
assert pos_neg(-1, 1, False) is True
assert pos_neg(-4, -5, True) is True


# not_string

def not_string(str):
    if str[0:3] == 'not':
        return str
    else:
        return 'not ' + str


assert not_string('candy') == 'not candy'
assert not_string('x') == 'not x'
assert not_string('not bad') == 'not bad'


# missing_char

def missing_char(str, n):
    return str[:n] + str[n+1:]

assert missing_char('kitten', 1) == 'ktten'
assert missing_char('kitten', 0) == 'itten'
assert missing_char('kitten', 4) == 'kittn'

# front_back

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[len(str)-1:] + str[1:-1] + str[0]

assert front_back('code') == 'eodc'
assert front_back('a') == 'a'
assert front_back('ab') == 'ba'

# front3

def front3(str):
    if len(str) < 3:
        return str
    else:
        return 3* str[0:3]

assert front3('Java') == 'JavJavJav'
assert front3('Chocolate') == 'ChoChoCho'
assert front3('abc') == 'abcabcabc'