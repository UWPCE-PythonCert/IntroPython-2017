#!/usr/bin/env python

# cigar_party

def cigar_party(cigars, is_weekend):
    return (40 <= cigars <= 60) or (is_weekend and (cigars >= 40))

assert cigar_party(30, False) == False
assert cigar_party(50, False) -- True
assert cigar_party(70, True) == True


# date_fashion

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

assert date_fashion(5, 10) == 2
assert date_fashion(5, 2) == 0
assert date_fashion(5, 5) == 1


# squirrel_play

def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    else:
        return 60 <= temp <= 90

assert squirrel_play(70, False) == True
assert squirrel_play(95, False) == False
assert squirrel_play(95, True) == True


# caught_speeding

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif 60 < speed <= 80:
        return 1
    else:
        return 2

assert caught_speeding(60, False) == 0
assert caught_speeding(65, False) == 1
assert caught_speeding(65, True) == 0


#sorta_sum

def sorta_sum(a, b):
    if 10 <= (a + b) <= 19:
        return 20
    else:
        return a+b

assert sorta_sum(3, 4) == 7
assert sorta_sum(9, 4) == 20
assert sorta_sum(10, 11) == 21


# alarm_clock

def alarm_clock(day, vacation):
    if vacation and (1 <= day <=5):
        return 'off'
    elif vacation and (day == 0 or day == 6):
        return '10:00'
    elif not vacation and (1 <= day <=5):
        return '7:00'
    else:
        return '10:00'

assert alarm_clock(1, False) == '7:00'
assert alarm_clock(5, False) == '7:00'
assert alarm_clock(0, False) == '10:00'

# love6

def love6(a, b):
    return (a == 6) or (b == 6) or (a+b == 6) or abs(a-b) == 6

assert love6(6, 4) == True
assert love6(4, 5) == False
assert love6(1, 5) -- True


# in1to10

def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >=10
    else:
        return 1 <= n <= 10

assert in1to10(5, False) == True
assert in1to10(11, False) == False
assert in1to10(11, True) == True

#near_ten

def near_ten(num):
    return num%10 <= 2 or num%10 >= 8

assert near_ten(12) == True
assert near_ten(17) == False
assert near_ten(19) == True