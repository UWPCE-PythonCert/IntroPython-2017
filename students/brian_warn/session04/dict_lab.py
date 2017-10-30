#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# dict_lab.py
''' Lab Assignment:
Dictionaries 1 -->
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).

Dictionaries 2 -->
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value. (upper and lower case?).

Sets  -->
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).

Sets 2 -->
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’
display the union and intersection of the two sets.

'''

# Dictionaries 1

info_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chocolate'}
info_dict2 = info_dict.copy()

print(info_dict)
del(info_dict['cake'])
print("After deletion, dictionary is now: ", info_dict)

# Show keys
show_keys = info_dict.keys()
print("Keys are: ", show_keys)

vals = info_dict.values()
print("Values are: ", vals)

# Output vals by themselves:

for n, v in info_dict.items():
    print(v)

# Check for 'cake' key:
if 'cake' in info_dict:
    print("True")
else:
    print("False")

# Add fruit:Mango
info_dict['fruit'] = 'Mango'

# Check for 'Mango' value:
if 'Mango' in info_dict.values():
    print("True")
else:
    print("False")

# Dictionaries 2
# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value. (upper and lower case?).
# Approach: Create a new dictionary. Loop through each key checking each value for 't'.  If 't' is present, then increment the number value for the key in the new dictionary.

print("\nDictionary 2 ...\n")
print("info_dict2 is: ", info_dict2)
dict_letters = {}

for k, v in info_dict2.items():
    print(k, v)
    if k not in dict_letters:
        dict_letters[k] = 0
        print("first occurrence of", k.strip() , "in dict_letters.")
        for ltr in v:
            print("ltr is: ", ltr)
            if ltr == 't':
                print("incrementing t")
                dict_letters[k] += 1
            else:
                continue

for k, v in dict_letters.items():
    print("Count of 't' for", k, "key is:", v)

# Create sets s2, s3 and s4 that contain numbers from zero 
# through twenty, divisible 2, 3 and 4.
# Display the sets.
# Display if s3 is a subset of s2 (False)
# and if s4 is a subset of s2 (True).

s2 = set()
s3 = set()
s4 = set()

for i in range(0,20):
    if i%2 == 0:
        s2.add(i)
    if i%3 == 0:
        s3.add(i)
    if i%4 == 0:
        s4.add(i)

print("s2 is:", s2)
print("s3 is:", s3)
print("s4 is:", s4)

test = s3.issubset(s2)
print(test)
test = s4.issubset(s2)
print(test)

# Sets 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
# Create a frozenset with the letters in ‘marathon’
# display the union and intersection of the two sets.

set1 = set('Python')
set1.add('i')

print(set1)

set2 = frozenset('marathon')
print("set2: ", set2)

set3 = set1.union(set2)

print("set3:", set3)
