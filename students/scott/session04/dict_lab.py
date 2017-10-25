#!/usr/bin/env python

d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d)
d.pop('cake')
print(d)
d['fruit'] = 'Mango'
print(d)
print(d.keys())
print(d.values())
print('cake' in d)
print('Mango' in d) #this returns false.....should return True


# I need to count the number of "t" in each key, and store that as the corresponding value for that key
# count doesn't seem to work.....I get a 'key error'


d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d)
#d.count('n')


for i in range(0,20):
    if i%2 == 0:
        print(i)


for i in range(0,20):
    if i%3 == 0:
        print(i)



for i in range(0,20):
    if i%4 == 0:
        print(i)

set2[(0,2,4,6,8,10,12,14,16,18,20)]
