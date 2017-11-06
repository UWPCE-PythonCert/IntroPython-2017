#!/usr/bin/env python

mydict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

def dict1():
    """ Dictionaries 1 tasks """

    # Display the dictionary
    print(mydict)
    # Delete the entry for "cake"
    mydict.pop('cake')
    # Display the dictionary
    print(mydict)
    # Add an entry for “fruit” with “Mango” and display the dictionary
    mydict['fruit'] = 'Mango'
    print(mydict)
    # Display the dictionary keys
    print(mydict.keys())
    # Display the dictionary values
    print(mydict.values())
    # Display whether or not “cake” is a key in the dictionary (i.e. False)
    print('cake' in mydict)
    # Display whether or not “Mango” is a value in the dictionary (i.e. True)
    print('Mango' in mydict.values())


def dict2():
    """ Dictionaries 2 tasks """

    # A new dictionary
    newdict = {}
    # Loop through mydict
    for item in mydict:
        # Assign new values to old keys, by counting how many 't's in the values
        newdict[item] = mydict[item].lower().count('t')
    # Print new dictionary
    print(newdict)


def sets1():
    """ Sets 1 tasks """
    
    # Build empty sets
    s2 = set()
    s3 = set()
    s4 = set()

    # Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4
    for n in range(21):
        if n%2 == 0:
            s2.update([n])
        if n%3 == 0:
            s3.update([n])
        if n%4 == 0:
            s4.update([n])

    # Display the sets
    print("s2 contains: ", s2)
    print("s3 contains: ", s3)
    print("s4 contains: ", s4)
    # Display if s3 is a subset of s2 (False)
    print(s3.issubset(s2))
    # Display if s4 is a subset of s2 (True)
    print(s4.issubset(s2))


def sets2():
    """ Sets 2 tasks """

    # Create a set with the letters in ‘Python’ and add ‘i’ to the set
    pset = set("Python")
    pset.add('i')
    print(pset)
    # Create a frozenset with the letters in ‘marathon’
    fs = frozenset("marathon")
    print(fs)
    # Print Union of two sets
    print(pset.union(fs))
    # Print Intersection of two sets
    print(pset.intersection(fs))

if __name__ == '__main__':
    """ Main function """

    dict1()
    dict2()
    sets1()
    sets2()
