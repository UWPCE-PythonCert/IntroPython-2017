"""
Week 4 Lab 2:
1. Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
2. Display the sets.
3. Display if s3 is a subset of s2 and if s4 is a subset of s2.

4. Create a set with the letters in ‘Python’ and add ‘i’ to the set.
5. Create a frozenset with the letters in ‘marathon’
6. Display the union and intersection of the two sets in Item 4 and Item 5.

"""

set2 = set()
for i in set(range(21)):
    if i % 2 == 0:
        set2.add(i)
print("\nSet divisible by 2:", set2)

set3 = set()
for i in set(range(21)):
    if i % 3 == 0:
        set3.add(i)
print("\nSet divisible by 3:", set3)

set4 = set()
for i in set(range(21)):
    if i % 4 == 0:
        set4.add(i)
print("\nSet divisible by 4:", set4)

print("\nIs set3 is a subset of set2:", set3.issubset(set2))
print("\nIs set4 is a subset of set2:", set4.issubset(set2))

#adding 'i' to set python
setpython = set('python')
setpython.add('i')

#create frozenset letter for 'marathon'
fs = frozenset('marathon')
print("\nFrozenset for 'marathon':", fs)

print("\nUnion set for python and marathon", setpython.union(fs))
print("\nIntersection set for python and marathon:", setpython.intersection(fs))
