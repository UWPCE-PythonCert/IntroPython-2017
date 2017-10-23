#!/usr/bin/env python3


#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
person={"name":"Chris", "city":"Seattle", "cake":"Chocolate"}

#Display the dictionary.
print(person)

#Delete the entry for “cake”.
person.pop('cake')

#Display the dictionary.
print(person)

#Add an entry for “fruit” with “Mango” and display the dictionary.
person['fruit'] = "Mango"

#Display the dictionary keys.
person.keys()

#Display the dictionary values.
person.values()

#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
"cake" in "person"

#Display whether or not “Mango” is a value in the dictionary (i.e. True).
"Mango" in person.values()

#Using the dictionary from item 1: Make a dictionary using the same keys but with the
# number of ‘t’s in each value as the value. (upper and lower case?).


#Display the sets.

#Display if s3 is a subset of s2 (False)

#and if s4 is a subset of s2 (True).

#Create a set with the letters in ‘Python’ and add ‘i’ to the set.

#Create a frozenset with the letters in ‘marathon’

#display the union and intersection of the two sets.