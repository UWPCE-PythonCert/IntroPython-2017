#!/usr/bin/env python3

"""
dictionary lab

"""
# dictionaries are ocmpised of keys and values, no order
# keys are immutable (unchangeable)
# keys can be: numbers, strings, tuples
# use for to iterate through keys
chris_dict = {'name':'Chris', 'city':'Seattle', 'cake':'chocolate'}
print(chris_dict)
make_a_copy = chris_dict.copy()

print(chris_dict.items())

item = chris_dict['name']
print(item)

# iterating over keys
for x in chris_dict:
    print(x)

for key in chris_dict.keys():
    print(key)

# iterating on everything (keys and values)
for k, v in chris_dict.items():
    print("%s: %s" % (k,v))

# delete cake key/value from dictionary
del chris_dict['cake']
print(chris_dict)

# pop pulls and removes a values
# .popitem pulls a random key/value pair
print(chris_dict.pop('name'))

print(make_a_copy)

chris_dict.update({'fruit':'mango'})
print(chris_dict)
print(chris_dict.keys())
print(chris_dict.values())

for key in chris_dict.items():
    if key == 'cake':
        print("cake: true")
    else:
        print('cake: false')

for k,v in chris_dict.items():
    if v == 'mango':
        print("mango: true")
    else:
        print('mango: false')




#dict.update{'fruit', 'mango'}
#print(dict)


# sets are un-ordered collections of values
# dictionaries with keys, not values
# s1((range(1,20))
#s2()
#s3()
#s4()
