#!/usr/bin/env python3

"""
Kathryn Egan
"""

dic = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'}

print(dic)
dic.pop('cake')
print(dic)
dic['fruit'] = 'Mango'
print(dic)
print('Dictionary keys: {}'.format(dic.keys()))
print('Dictionary values: {}'.format(dic.values()))
print('"cake" in dictionary keys: {}'.format('cake' in dic))
print('"Mango" in dictionary values: {}'.format('Mango' in dic.values()))

t_dict = {key: value.lower().count('t') for key, value in dic.items()}

s2 = {i for i in range(21) if i % 2 == 0}
s3 = {i for i in range(21) if i % 3 == 0}
s4 = {i for i in range(21) if i % 4 == 0}
print('s2:{}'.format(s2))
print('s3:{}'.format(s3))
print('s4:{}'.format(s4))

print('s3 is subset of s2:{}'.format(s3.intersection(s2) == s3))
print('s4 is subset of s2:{}'.format(s4.intersection(s2) == s4))

python = set([char for char in 'Python'])
python.add('i')
marathon = frozenset([char for char in 'marathon'])

print('"Python" and "marathon" union: {}'.format(python.union(marathon)))
print('"Python" and "marathon" intersection: {}'.format(python.intersection(marathon)))
