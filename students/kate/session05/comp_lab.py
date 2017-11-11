#!/usr/bin/env python3

"""
comprehensions lab
"""

#
feast = ['lambs', 'sloths', 'orangutans','breakfast cereals', 'fruit bats']

# comprehension to capitalize
comp1 = [delicacy.capitalize() for delicacy in feast]
print("comp1")
print(comp1[0])

# comprehension for length of list
comp2 = [delicacy for delicacy in feast if len(delicacy) > 6]
print("Comp2")
print(comp2[0])

# comprehension for tuples
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comp3 = [ skit * number for number, skit in list_of_tuples ]
print("comp3")
print(comp3[2])

# double list comprehensions
eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comp4 = \
[ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]
print("comp4")
print(comp4[0])

# set comnprehension
comp5 = { c for c in 'aabbbcccc'}
print("comp5")
print(comp5)


# dictionaries and comprehensions
dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}
print("dict comprehension")
print(dict_comprehension)
print('first' in dict_comprehension) # output is false
print('FIRST' in dict_comprehension) # output is true
print(len(dict_of_weapons)) # output is 5
print(len(dict_comprehension)) # output is 4
