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

    # bool winner - Done
    # match number - Done
    # team being tracked - Done
    # alliance color - Done
    # team position - Done
    # bool pilot in airship - Done
    # gears delivered - Done
    # KPA scored - Done
    # bool gear delivered in auto - Done
    # bool climb - Done
    # KPA in auto - Done

    def __init__(self, mnumber, teamnumber):
        self.matchnumber = mnumber
        self.team = teamnumber
        self.win = 1
        self.gears = None
        self.alliance = None
        self.fieldpos = None
        self.pilot = None
        self.autogears = None
        self.kpa = None
        self.autokpa = None
        self.climb = None
        self.penalties = None

    def __repr__(self):
        return '{}, {}: {}'.format(self.team, self.matchnumber, self.win)

    def __str__(self):
        return 'Match {}, Team {}'.format(self.matchnumber, self.team)


class Team:
    # Team is an object which contains data specific to a team
    # it is not intended to be user editable but is user viewable

    # number
    # name
    # matches played
    # matches on red
    # matches on blue
    # matches in pos 1
    # matches in pos 2
    # matches in pos 3
    # most gears in a match
    # least gears in a match
    # average gears in a match
    # most KPA in a match
    # least KPA in a match
    # average KPA in a match
    # gears delivered in auto
    # gears delivered in auto pos 1
    # gears delivered in auto pos 2
    # gears delivered in auto pos 3
    # KPA in auto
    # number of climbs
    # number of pilots

    def __init__(self, num):
        self.number = num
        self.name = None



def readfile():
    with open('MatchLedger.csv', 'r') as inputfile:
        csvreader = csv.reader(inputfile)
        next(inputfile)
        for line in csvreader:
            matchlist.append(Match(line[0], line[1]))
            for i in range(0, len(matchlist)):
                if matchlist[i].matchnumber == line[0] and matchlist[i].team == line[1]:
                    matchlist[i].alliance = line[2]
                    matchlist[i].fieldpos = line[3]
                    matchlist[i].win = line[4]
                    matchlist[i].pilot = line[5]
                    matchlist[i].gears = line[6]
                    matchlist[i].autogears = line[7]
                    matchlist[i].kpa = line[8]
                    matchlist[i].autokpa = line[9]
                    matchlist[i].climb = line[10]
                    matchlist[i].penalties = line[11]
    print("File has been read.")

def primaryUI():
    # This is the introductory user interface

    print('Welcome to the FRC Scouter Program')
    print()
    print()
    print('What would you like to do?')
    print('1 - Log a match')
    print('2 - View the Team Database')
    print('3 - Run a Monte Carlo Analysis')
    print('4 - Import a Match Database')
    print('5 - Exit Program')
    while True:
        userin = input('Please select 1-5: ')
        if userin == '1':
            logmatch()
        elif userin == '2':
            viewdbui()
        elif userin == '3':
            setupmonte()
        elif userin == '4':
            readfile()
            for i in range(0,len(matchlist)):
                print(str(matchlist[i]))
        elif userin == '5':
            exit()
        else:
            print('You did not select a valid option.')


primaryUI()