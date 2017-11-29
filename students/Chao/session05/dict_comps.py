#!/usr/bin/env python

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

def sformat(**kwargs):
    """ input dict and return a formatted string """
    return "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta".format(**kwargs)

def hexcomps():
    """ Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine). """
    h1 = [hex(i) for i in range(16)]
    d1 = {i: j for i, j in enumerate(h1)}
    return d1

def hexcomps2():
    """ Do the previous entirely with a dict comprehension – should be a one-liner """
    dh = {i: hex(i) for i in range(16)}
    return dh

def counta():
    """ Build a new dictionary with food_prefs but replace values with number of a's in it """
    newdict = {i: j.count('a') for i, j in food_prefs.items()}
    return newdict

def seta():
    """ build sets with set comprehension """
    s2 = {i for i in range(21) if i%2 == 0}
    s3 = {i for i in range(21) if i%3 == 0}
    s4 = {i for i in range(21) if i%4 == 0}
    return "In seta(),  s2 = {}, s3 = {}, s4 = {}".format(s2, s3, s4)

def setb():
    """ A list of sets """
    ls = [{i for i in range(21) if i%j == 0} for j in range(2, 5)]
    return ls


if __name__ == '__main__':
    """ Main function """
    print(sformat(**food_prefs))
    print(hexcomps())
    print(hexcomps2())
    print(counta())
    print(seta())
    print(setb())
