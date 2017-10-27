#!/usr/bin/env python3
import copy

#    Create a dictionary containing “name”, “city”, and “cake” for “Chris” from
#    “Seattle” who likes “Chocolate”.
#    Display the dictionary.
#    Delete the entry for “cake”.
#    Display the dictionary.
#    Add an entry for “fruit” with “Mango” and display the dictionary.
#    Display the dictionary keys.
#    Display the dictionary values.
#    Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
#    Display whether or not “Mango” is a value in the dictionary (i.e. True).
master = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
}

print("#" * 5)
print("Original dictionary")
print(master)

print("#" * 5)
print("Delete cake")
del master["cake"]
print(master)

print("#" * 5)
print("Add fruit")
master["fruit"] = "Mango"
print(master)

print("#" * 5)
print("Print keys")
print(master.keys())

print("#" * 5)
print("Print values")
print(master.values())

print("#" * 5)
print("Print if 'cake' is a key in the dictionary")
print("cake" in master)

print("#" * 5)
print("Print if 'Mango' is a value  in the dictionary")
print("Mango" in master.values())
