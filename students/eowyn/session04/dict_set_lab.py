#!/usr/bin/env python

def dictionaries_one():
    '''
    Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
    Display the dictionary.
    Delete the entry for “cake”.
    Display the dictionary.
    Add an entry for “fruit” with “Mango” and display the dictionary.
    Display the dictionary keys.
    Display the dictionary values.
    Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    Display whether or not “Mango” is a value in the dictionary (i.e. True).
    '''
    info = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
    print(info.items())
    del info["cake"]
    print(info.items())
    info["fruit"] = "Mango"
    print(info.items())
    print(info.keys())
    print(info.values())
    print("cake" in info)
    print("Mango" in info.values())

def dictionaries_two():
    '''
    Using the dictionary from item 1: Make a dictionary using the 
    same keys but with the number of ‘t’s in each value as the 
    value. (upper and lower case?).'''
    info = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
    infocount = {}
    for item in info:
        infocount[item] = info[item].lower().count("t")
    print(infocount.items())

def sets_one():
    '''
    Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    divisible 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
    '''
    base = range(0,20)
    s2 = set([i for i in base if i%2==0])
    s3 = set([i for i in base if i%3==0])
    s4 = set([i for i in base if i%4==0])
    print("Divisible by 2: ", s2)
    print("Divisible by 3: ", s3)
    print("Divisible by 4: ", s4)
    print("S3 is a subset of S2: ",s3.issubset(s2))
    print("S4 is a subset of S2: ",s4.issubset(s2))

def sets_two():
    '''
    Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    Create a frozenset with the letters in ‘marathon’
    display the union and intersection of the two sets.
    '''
    pset = set('Python')
    pset.add('i')  # why can't I do both in one line?
    fset = frozenset('marathon')
    print("Union: ",pset.union(fset))
    print("Intersection: ",pset.intersection(fset))


if __name__ == "__main__":
    print("Dictionaries One")
    dictionaries_one()
    print("Dictionaries Two")
    dictionaries_two()
    print("Sets One")
    sets_one()
    print("Sets Two")
    sets_two()

