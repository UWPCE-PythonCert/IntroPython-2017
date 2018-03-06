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

    # number - Done
    # name - Done
    # matches played - Done
    # matches on red - Done in alliances list (0 for blue, 1 for red)
    # matches on blue - Done in alliances list (0 for blue, 1 for red)
    # matches in pos 1  - Done in fieldpos (1,2,3) left to right
    # matches in pos 2 - Done in fieldpos (1,2,3) left to right
    # matches in pos 3 - Done in fieldpos (1,2,3) left to right
    # most gears in a match - Done
    # least gears in a match - Done
    # average gears in a match - Done
    # most KPA in a match - Done
    # least KPA in a match - Done
    # average KPA in a match - Done
    # gears delivered in auto - Done (as dict) lets see if that was a good idea
    # gears delivered in auto pos 1
    # gears delivered in auto pos 2
    # gears delivered in auto pos 3
    # KPA in auto
    # number of climbs
    # number of pilots

    def __init__(self, num):
        self.number = num
        self.name = None
        self.matchesplayed = []
        self.gearsdelivered = []
        self.kpa = []
        self.pilot = []
        self.alliances = {}
        self.fieldpos = {}
        self.autogears = {}
        self.autogearsinpos = {}
        self.autokpa = {}
        self.autokpainpos = {}
        self.climb = {}
        self.matchwins = {}
    @property
    def nummatches(self):
        return(len(matchesplayed))

    @property
    def averagegears(self):
        return(sum(gearsdelivered) / len(gearsdelivered))

    @property
    def maxgearsdelivered(self):
        return(max(gearsdelivered))

    @property
    def mingearsdelivered(self):
        return(min(gearsdelivered))

    @property
    def averagekpa(self):
        return(sum(kpa) / len(kpa))

    @property
    def maxkpa(self):
        return(max(kpa))

    @property
    def minkpa(self):
        return(min(kpa))

    @property
    def autogearsinpos(self):
        # This creates a dictionsary with postion as Key and Autogears scored as value
        for i in range(1, 3):
            for j in self.matchesplayed:
                if self.fieldpos[j] == i:
                    autogearsinpos[i] = self.autogears[j]
        return autogearsinpos

     @property
    def autokpainpos(self):
        # This creates a dictionsary with postion as Key and Autogears scored as value
        for i in range(1, 3):
            for j in self.matchesplayed:
                if self.fieldpos[j] == i:
                    autokpainpos[i] = self.autokpa[j]
        return autokpainpos

    def fillmatches():
        self.matchesplayed = [matchlist[i].matchnumber for i in matchlist if matchlist[i].teamnumber == self.number]

    def fillgearsdelivered():
        self.gearsdelivered = [matchlist[i].gears for i in matchlist if matchlist[i].teamnumber == self.number]

    def fillkpa():
        self.kpa = [matchlist[i].kpa for i in matchlist if matchlist[i].teamnumber == self.number]

    def fillpilot():
        self.pilot = [matchlist[i].pilot for i in matchlist if matchlist[i].teamnumber == self.number and matchlist[i].pilot == 1]

    def fillalliances():
        self.alliances = {matchlist[i].matchnumber: matchlist[i].alliance for i in matchlist if matchlist[i].teamnumber == self.number}

    def fillfieldpos():
        self.fieldpos = {matchlist[i].matchnumber: matchlist[i].fieldpos for i in matchlist if matchlist[i].teamnumber == self.number}

    def fillautogears():
        self.autogears = {matchlist[i].matchnumber: matchlist[i].autogears for i in matchlist if matchlist[i].teamnumber == self.number}

    def fillautokpa():
        self.autokpa = {matchlist[i].matchnumber: matchlist[i].autokpa for i in matchlist if matchlist[i].teamnumber == self.number}
    
    def fillclimb():
        self.climb = {matchlist[i].matchnumber: matchlist[i].climb for i in matchlist if matchlist[i].teamnumber == self.number}

    def matchwins():
        self.matchwins = {matchlist[i].matchnumber: matchlist[i].win for i in matchlist if matchlist[i].teamnumber == self.number}



def updateteams():
    # This function is intended to refresh team objects with the latest match data.teamnumber

    


def readmatchfile():
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
            readmatchfile()
            for i in range(0,len(matchlist)):
                print(str(matchlist[i]))
        elif userin == '5':
            exit()
        else:
            print('You did not select a valid option.')


primaryUI()