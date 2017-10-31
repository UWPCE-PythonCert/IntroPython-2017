#! /usr/bin/env python
my_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(my_dict)
del my_dict['cake']
my_dict['fruit'] = 'Mango'
print(my_dict)
for key in my_dict:
    print(key)
print('cake' in my_dict.keys())
print('Mango' in my_dict.values())
# count = 0
print(my_dict)
for x in my_dict.keys():
    count = 0
    for y in my_dict[x]:
        if y == 't':
            count += 1
    my_dict[x] = count
print(my_dict)
s1 = []
s2 = set(s1)
s3 = set(s2)
s4 = set(s3)
for x in range(0, 20):
    if x % 2 == 0:
        s2.add(x)
    if x % 3 == 0:
        s3.add(x)
    if x % 4 == 0:
        s4.add(x)
print(s2)
print(s3)
print(s4)
z = s3.issubset(s2)
u = s4.issubset(s2)
print(z)
print(u)
p = set('Python')
p.add('i')
print(p)
m = frozenset('marathon')
print(m)
print(p.union(m))
print(p.intersection(m))
