#!/usr/bin/env python3


dict = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}

print(dict)

dict.pop('cake')

print(dict)

dict['fruit'] = "Mango"

print(dict)

print(dict.keys())

print(dict.values())

print(dict.items())

if 'cake' in dict.keys():
    print("True")
else:
    print("False")

if "Mango" in dict.values():
    print("True")
else:
    print("False")

dict1 = {}

for key, value in dict.items():
    nt = 0
    for i in value:
        if i.lower() == 't':
            nt = nt + 1
    dict1[key] = nt

print(dict1)


s2 = set()
s3 = set()
s4 = set()

for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

set1 = set()
for i in "Python":
    set1.add(i)

set1.add('i')
print(set1)

set11 = ('m', 'a', 'r', 'a', 't', 'h','o','n')

fset = frozenset(set11)

print(set1.intersection(fset))
print(set1.union(fset))