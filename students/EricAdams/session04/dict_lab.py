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

