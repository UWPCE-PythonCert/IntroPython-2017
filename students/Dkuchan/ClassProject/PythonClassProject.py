# PythonClassProject.py
''' This python program is written for the advanced python programming class
    it is a scouting program written for the First Robotics Competition based
    on the 2017 game FIRST Steamworks. '''




'''Need to add a tuple for allowed users to baseline who does what'''



import math
import os
import csv
import random

matchlist = []
monteblue = [0, 0, 0]
montered = [0, 0, 0]


class Match:

    # A match is a collection of data which represents a match FOR A SINGLE TEAM.
    # Match is the primary class which is edited by the user.
    # it is important to note that this is intended to log a section of a match and 
    # a single instance does not contain the entire dataset for a real life match.
    # The reason for this is because a single person will not 
    # log more than one team in a match.  

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

    #def __iter__(self):


class Team:    # Team is an object which contains data specific to a team
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

   # def __repr__(self):
    #    return '{}, {}: {}'.format(self.team, self.matchnumber, self.win)

    def __str__(self):
        return 'Team {}, Team {}'.format(self.number, self.name)

    def fillmatches(self):
        for i in range(0, len(matchlist)):   # I wanted to do this in a list
            if int(matchlist[i].team) == int(self.number):  # did your team play in this match
                self.matchesplayed.append(matchlist[i].matchnumber)  # if so append the list comprehensions but I is a match type variable

    def fillmatchwins(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if int(matchlist[i].team) == int(self.number):  #did your team play in this match
                if int(matchlist[i].win) == 1:
                    self.matchwins.update({int(matchlist[i].matchnumber): int(matchlist[i].win)})
    @property
    def nummatches(self):
        return len(self.matchesplayed)

    @property
    def averagegears(self):
        return sum(self.gearsdelivered) / len(self.gearsdelivered)

    @property
    def maxgearsdelivered(self):
        return max(self.gearsdelivered)

    @property
    def mingearsdelivered(self):
        return min(self.gearsdelivered)

    @property
    def averagekpa(self):
        return sum(self.kpa) / len(self.kpa)

    @property
    def maxkpa(self):
        return max(self.kpa)

    @property
    def minkpa(self):
        return min(self.kpa)

#    @property
 #   def autogearsinpos(self):
        # This creates a dictionsary with postion as Key and Autogears scored as value DOES NOT WORK YET
  #      for i in range(1, 3):
   #         for j in self.matchesplayed:
    #            if self.fieldpos[j] == i:
     #               self.autogearsinpos[i] = self.autogears[j]
      #  return self.autogearsinpos

    #@property
    #def autokpainpos(self):
        # This creates a dictionsary with postion as Key and Autogears scored as value
     #   for i in range(1, 3):
      #      for j in self.matchesplayed:
       #         if self.fieldpos[j] == i:
        #            autokpainpos[i] = self.autokpa[j]
        #return autokpainpos

    


                    #self.matchwins = {matchlist[i].matchnumber: matchlist[i].win for i in matchlist if matchlist[i].teamnumber == self.number}        
       # self.matchesplayed = [int(matchlist[i].matchnumber) for i in matchlist if int(matchlist[i].teamnumber) == self.number]


    def fillgearsdelivered(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if int(matchlist[i].team) == int(self.number):  #did your team play in this match
                self.gearsdelivered = matchlist[i].gears

       # self.gearsdelivered = [matchlist[i].gears for i in matchlist if matchlist[i].teamnumber == self.number]

    def fillkpa(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if int(matchlist[i].team) == int(self.number):  #did your team play in this match
                self.kpa = matchlist[i].kpa

       # self.kpa = [matchlist[i].kpa for i in matchlist if matchlist[i].teamnumber == self.number]

    def fillpilot(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if int(matchlist[i].team) == int(self.number):  #did your team play in this match
                self.pilot = matchlist[i].pilot

       # self.pilot = [matchlist[i].pilot for i in matchlist if matchlist[i].teamnumber == self.number and matchlist[i].pilot == 1]

    def fillalliances(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if int(matchlist[i].team) == int(self.number):  #did your team play in this match
                self.alliances = matchlist[i].alliance

      #  self.alliances = {matchlist[i].matchnumber: matchlist[i].alliance for i in matchlist if matchlist[i].teamnumber == self.number}

    def fillfieldpos():

        self.fieldpos = {matchlist[i].matchnumber: matchlist[i].fieldpos for i in matchlist if matchlist[i].teamnumber == self.number}

    def fillautogears(self):

        self.autogears = {matchlist[i].matchnumber: matchlist[i].autogears for i in matchlist if matchlist[i].teamnumber == self.number}

    def fillautokpa():
        self.autokpa = {matchlist[i].matchnumber: matchlist[i].autokpa for i in matchlist if matchlist[i].teamnumber == self.number}
    
    def fillclimb():
        self.climb = {matchlist[i].matchnumber: matchlist[i].climb for i in matchlist if matchlist[i].teamnumber == self.number}


def testmatchfidelity(matchnumber):
    # Tests to see if there are 6 teams in a match teamnumber.
    # Tests to make sure there are no repeats in teams.
    matchcount = 0
    teamvar = None
    teamslist = []
    for i in range(0, len(matchlist)):
        if matchlist[i].matchnumber == matchnumber:
            matchcount+=1
            teamslist.append(int(matchlist[i].team))
    print("There are " + len(teamslist) + "/6 logs in the database for match " + matchnumber + ".")
    for i in teamlist:
        checkteamnum = teamslist[i]
        teaminmatch = 0
        for j in teamlist:
            if teamlist[j] == checkteamnum:
                teaminmatch += 1
        if teaminmatch > 1:
            print("Team " + str(checkteamnum) + "appears " + teaminmatch + "time(s) in match " + matchnumber + ".")
        else:
            print("This match is complete.")

# def updateteams():
    # This function is intended to refresh team objects with the latest match data.teamnumber

def teamcomparisonUI()
    print()
    print("Welcome to the Team Comparison Tool"):
    print("Which teams would you like to compare?: ")
    print()

def compareteams():



def readmatchfile():
    with open('MatchLedger.csv', 'r') as inputfile:
        csvreader = csv.reader(inputfile)
        next(inputfile)
        for line in csvreader:
            matchlist.append(Match(line[0], line[1]))
            for i in range(0, len(matchlist)):
                if matchlist[i].matchnumber == line[0] and matchlist[i].team == line[1]:    #why did I do this?  To check for quality?
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
    testingthing()
    primaryUI()

def outputmatchdata(matchnumber):
    for i in range(0, len(matchlist)):
        if matchlist[i].matchnumber == matchnumber:
            print("")


def produceinsights(teamnum):
    # This function calls multiple functions to provide a report
    # containing statistical outcomes that are applicable
    # to the specified team.
    pass


def doesteamexist(team):
    # looks through a list of teams and checks whether the team exists.
    existance = False
    for i in range(0, len teamlist):
        if team == teamlist[i]:
            existance = True
    return existance


def duplicatecheck(team, array):
    # takes a team and an array, checks if it occurs more than once
    duplicatestat = False
    if array.count(team) > 1:
        duplicatestat = True
    return duplicatestat

def setupmonteUI()
    # this function brings up the UI for setting up a monte carlo analysis.
    setupuserin = None
    teamarray = []
    alliancemessage = 
    print()
    print("Welcome to the Monte Carlo Setup")
    print("")
    for i in range(1, 2):
        if i == 1:
            alliancemessage == 'Blue'
        else:
            alliancemessage == 'Red'
        for j in range(1, 3):
            while True:
            setupuserin = input("Please select a team for the {} Alliance in field pos {})".format(alliancemessage, j))
            teamcheck = doesteamexist(setupuserin)
            if teamcheck is False:
                print("Team {} not found.".format(setupuserin))
                print("Please enter a valid team.")
                continue
            elif duplicatecheck(setupuserin,teamarray) is True:
                print("Team {} is already assigned to an alliance.".format(setupuserin))
                print("Please enter a valid team.")
                continue
            else:
                teamarray.append(setupuserin)
                break
    print("You have set up the following match.")
    print(teamarray)


    

    # monte carlo should run 10000 times.  
    # MVP is to only work on gear points.

def testingthing():
    # interrogates a team object to make sure it is correctly passing data

    team1 = Team(4469)
    team1.fillmatches()
    team1.fillmatchwins()
    print(matchlist[3].team)
    #print(team1.number)
    print(team1.matchesplayed)
    print(team1.matchwins)
    print(team1.nummatches)


def logmatch():
    print()
    print("This Module Doesnt Exist at Ths Time")
    print("In this program it is spoofed by a match list.")
    print()
    primaryUI()

def showteamsUI():
    print()
    print("Teams in the Database:")
    print()
    viewdbUI()

def showmatchesUI():
    print()
    if len(matchlist) >= 1:
        for i in range(0, len(matchlist)):
            print(str(i) + " - " + str(matchlist[i]))
    else:
        print("There are no matches in the database.")
        print("This likely means you need to import a database.")
    print()
    viewdbUI()

def viewdbUI():
    print()
    print("Welcome to the Database Viewer.")
    print()
    print("1 - Look up a Team.")
    print("2 - Look up a Match")
    print("3 - Test Match Fidelity")
    print("4 - Go back to Home Screen")
    while True:
        userin = input("Please make a selection: ")
        if userin == '1':
            showteamsUI()
        elif userin == '2':
            showmatchesUI()
        elif userin == '3':
            testmatchfidelity()
        elif userin == '4':
            primaryUI()
        else:
            print("Please make a valid selection.")
            viewdbUI()

def primaryUI():
    # This is the introductory user interface

    print('Welcome to the FRC Scouter Program')
    print()
    print()
    print('What would you like to do?')
    print('1 - Log a match')
    print('2 - View the Database')
    print('3 - Run a Monte Carlo Analysis')
    print('4 - Import a Match Database')
    print('5 - Exit Program')
    while True:
        userin = input('Please select 1-5: ')
        if userin == '1':
            logmatch()
        elif userin == '2':
            viewdbUI()
        elif userin == '3':
            setupmonte()
        elif userin == '4':
            readmatchfile()
            #for i in range(0,len(matchlist)):
                #print(str(matchlist[i]))
        elif userin == '5':
            exit()
        else:
            print('You did not select a valid option.')
            primaryUI()

primaryUI()
