#!/usr/bin/env python3

"""
dictionary lab

"""

# dictionaries are ocmpised of keys and values, no order
# keys are immutable (unchangeable)
# keys can be: numbers, strings, tuples
# use for to iterate through keys

#dicitonary 1
print(" \n" + "*" * 10)
chris_dict = {'name':'Chris', 'city':'Seattle', 'cake':'chocolate'}
print("chris_dict")
print(chris_dict)
make_a_copy = chris_dict.copy()

print(" \n" + "*" * 10)
print("chris_dict items")
print(chris_dict.items())
thing = chris_dict['name']
print(thing)


# iterating over keys
print(" \n" + "*" * 10)
print("iterating over keys")
for x in chris_dict:
    print(x)

print(" \n" + "*" * 10)
print("print iterating through keys")
for key in chris_dict.keys():
    print(key)

print(" \n" + "*" * 10)
print("iterating over keys and values")
# iterating on everything (keys and values)
for k, v in chris_dict.items():
    print("%s: %s" % (k,v))

print(" \n" + "*" * 10)
print("delete an item(cake), print remaining list item")
# delete cake key/value from dictionary
del chris_dict['cake']
print(chris_dict)

print(" \n" + "*" * 10)
print("remove and display an item(name)")
# pop pulls and removes a values
# .popitem pulls a random key/value pair
print(chris_dict.pop('name'))

print(" \n" + "*" * 10)
print("print copy from earlier, the original list without del and pop")
print(make_a_copy)

print(" \n" + "*" * 10)
print("add fruit:mango to dict")
# add fruit/mango to dictionary
chris_dict.update({'fruit':'mango'})
print(chris_dict)
print(chris_dict.keys())
print(chris_dict.values())

print(" \n" + "*" * 10)
print("verify cake")
for key in chris_dict.items():
    if key == 'cake':
        print("cake: true")
    else:
        print('cake: false')

print(" \n" + "*" * 10)
print("verify mango")
for k,v in chris_dict.items():
    if v == 'mango':
        print("mango: true")
    else:
        print('mango: false')

# dictionary 2
# create a new dictionary tracking the letter t
print(" \n" + "*" * 10)
print("new dictionary, the letter 't'")
new_dict = {}
for key in chris_dict:
	old_value=chris_dict[key].lower()
	new_dict[key]=old_value.count("t")
print(new_dict)


# sets are un-ordered collections of values
# dictionaries with keys, not values
# s1((range(1,20))
#s2()
#s3()
#s4()
