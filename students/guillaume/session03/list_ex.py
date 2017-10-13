#!/usr/bin/env python
#
# creating and modifying a list
#

zoo = ["monkey", "tiger", "eagle", "parrot"]

print "The zoo has the following", len(zoo), "animals:", zoo

print "The 1. animal is", zoo[0]
print "The 2. animal is", zoo[1]
print "The 1. and 2. animals are", zoo[:2]
print "Animals 2. - 4. are", zoo[1:4]
print "The animals after the 2. one are", zoo[2:]
print "The last element is", zoo[-1]

new_animal = raw_input("Which animal would you like to add? ")
zoo.append(new_animal)
print "The zoo has the following", len(zoo), "animals:", zoo

new_animal = raw_input("Which animal should replace the monkey? ")
zoo[0] = new_animal
print "The zoo has the following", len(zoo), "animals:", zoo