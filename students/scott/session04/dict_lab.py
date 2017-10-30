#!/usr/bin/env python

import sys

d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d)



d.pop('cake')
print(d)
d['fruit'] = 'Mango'
print(d)
print(d.keys())
print(d.values())
print('cake' in d)
print('Mango' in d.values()) #this returns false.....should return True, I think I fixed it by referring to d.values()


# I need to count the number of "t" in each key, and store that as the corresponding value for that key
# count doesn't seem to work.....I get a 'key error'



d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d)
#d.count('n')




set2 = set()
for i in range(0,20):
    if i%2 == 0:
        set2.add(i)
print(set2)


set3 = set()
for i in range(0,20):
    if i%3 == 0:
        set3.add(i)
print(set3)


set4 = set()
for i in range(0,20):
    if i%4 == 0:
        set4.add(i)
print(set4)

print(set3.issubset(set2))
print(set4.issubset(set2))


letters = set('Python')
print(letters)
letters.add('i')
print(letters)

no_changey = frozenset(('marathon'))
print(no_changey)

print(letters.union(no_changey))
print(letters.intersection(no_changey))
