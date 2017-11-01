#!/usr/bin/env python

person = { "name": "Chris", "city": "Seattle", "cake": "Chocolate" }

del person["cake"]

person["fruit"] = "Mango"

# print dict
print(person)

# print keys
print(person.keys())

# print data
print(person.values())

# haz cake?!
print("cake" in person)

# has mangos?
print( "Mango" in person.values() )

# create a new dict from old
new_dict = {}
for key in person:
	old_value=person[key].lower()
	new_dict[key]=old_value.count("t")
print(new_dict)

# for convience create a dict for the sets
s = { 2: set(), 3: set(), 4: set() }

# loop through the combinations and build up the sets
for item in range(21):
	for entry in range(2,5):
		if item % entry == 0:
			s[entry].add(item)

# print sets
for item in range(2,5):
	print(item,s[item])

# some tests
print("s3 is a subset of s2:", s[2].issubset(s[3]))
print("s4 is a subset of s2:", s[4].issubset(s[2]))

pyset = set("Python")
pyset.add("i")
pyset.add("i") # just verifying you don't get an error if it's already there
print(pyset)

brrset = frozenset("marathon")
print(brrset)

print("union:",pyset.union(brrset))
print("intersection:",pyset.intersection(brrset))
