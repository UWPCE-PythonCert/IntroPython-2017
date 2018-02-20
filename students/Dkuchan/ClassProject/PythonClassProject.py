# PythonClassProject.py
''' This python program is written for the advanced python programming class
    it is a scouting program written for the First Robotics Competition based
    on the 2017 game FIRST Steamworks. '''




'''Need to add a tuple for allowed users to baseline who does what'''



import math
import os
import csv

matchlist = []
monteblue = [0, 0, 0]
montered = [0, 0, 0]


class Match:

    # A match is a collection of data which represents a match.
    # Match is the primary class which is edited by the user.


    # bool winner
    # match number
    # team being tracked
    # alliance color
    # team position
    # bool pilot in airship
    # gears delivered
    # KPA scored
    # bool gear delivered in auto
    # bool climb
    # KPA in auto

    def __init__(self, mnumber, teamnumber):
        self.matchnumber = mnumber
        self.team = teamnumber

    
    def __repr__(self):
            return '{}, {}: {}'.format(self.team, self.matchnumber, self.win)

    def __str__(self):
            return 'Match {}, Team {}'.format(self.matchnumber, self.teamnumber)

    @property





matchlist.append(Match(1,4469))
matchlist.append(Match(2,4469))

for i in range (0, len(matchlist)):
    print(matchlist[i].matchnumber)



def primaryUI():
    # This is the introductory user interface

    print('Welcome to the FRC Scouter Program')
    print()
    print()
    print('What would you like to do?')
    print('1 - Log a match')
    print('2 - View the Team Database')
    print('3 - Run a Monte Carlo Analysis')
    print('4 - Exit Program')
    while True:
        userin = input('Please select 1-4: ')
        if userin == '1':
            logmatch()
        elif userin == '2':
            viewdbui()
        elif userin == '3':
            setupmonte()
        elif userin == '4':
            exit()
        else:
            print('You did not select a valid option.')


primaryUI()