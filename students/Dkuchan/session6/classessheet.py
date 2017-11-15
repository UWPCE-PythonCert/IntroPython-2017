# classessheet.py
""" This is a script to mess with classes. """
import math

class Person:

# This is an experimental class 
   
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.donations=[1,2,3,4,5,6,7]
        self.first_name = None
        self.last_name = None
        self.averagedon = None
        self.maxdon = None


def idaverages(dons):
    total=0
    for i in dons:
        total += i
        average = total/len(dons)
    return average

def idmaxdon(dons):
    maximum = max(dons)
    return maximum



dan=Person(1, 3)
print(dan.donations)
dan.donations.append(3)
print(dan.donations)
dan.averagedon = idaverages(dan.donations)
dan.maxdon=idmaxdon(dan.donations)
print(dan.maxdon)
print(dan.averagedon)
print(len(dan.donations))