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
teamlist = []   #HOLDS THE TEAM NUMBERS BECAUSE I COULD NOT GET A DIRECT LIST CREATION TO WORK
teamlist2 = []  #HOLDS THE TEAM OBJECTS
montelist = []
teamdict = {}
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

class MonteResult(Match):
    # this class is intended to contain results for monte carlo runs
    # it is a sublcass of Match as a monte run is just simulated Matches
    # functions of match are not all used at this point.  perhaps with future updates

    def __init__(self, bluescore, redscore, runnum):
        self.run = None
        self.bluescore = None
        self.redscore = None
        self.winner = None

    def __str__(self):
        return "Match {}, Winner {}, BlueScore: {}, RedScore: {}".format(self.run, self.winner, self.bluescore, self.redscore)


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
        self.alliances = []
        self.fieldpos = []
        self.autogears = []
        self.autogearsinpos = []
        self.autokpa = []
        self.autokpainpos = []
        self.climb = []
        self.matchwins = []

   # def __repr__(self):
    #    return '{}, {}: {}'.format(self.team, self.matchnumber, self.win)

    def __str__(self):
        return 'Team Number: {}, Team Name: {}'.format(self.number, self.name)

    def fillmatches(self):
        for i in range(0, len(matchlist)):   # I wanted to do this in a list
            if int(matchlist[i].team) == int(self.number):  # did your team play in this match
                self.matchesplayed.append(matchlist[i].matchnumber)  # if so append the list comprehensions but I is a match type variable

    def fillmatchwins(self):
        for i in range(0, len(matchlist)):   # I wanted to do this in a list
            if matchlist[i].team == self.number:  # did your team play in this match
                if int(matchlist[i].win) == 1:
                    self.matchwins.append(int(matchlist[i].win))
    @property
    def nummatches(self):
        return len(self.matchesplayed)

    @property
    def averagegears(self):
        return (sum(self.gearsdelivered) / len(self.gearsdelivered))

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

    @property
    def climbpercent(self):
        return (len(self.climb) / len(self.matchesplayed) * 100)

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
            if matchlist[i].team == self.number:  #did your team play in this match
                self.gearsdelivered.append(int(matchlist[i].gears))

       # self.gearsdelivered = [matchlist[i].gears for i in matchlist if matchlist[i].teamnumber == self.number]

    def fillkpa(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if matchlist[i].team == self.number:  #did your team play in this match
                self.kpa.append(int(matchlist[i].kpa))

       # self.kpa = [matchlist[i].kpa for i in matchlist if matchlist[i].teamnumber == self.number]

    def fillpilot(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if matchlist[i].team == self.number:  #did your team play in this match
                self.pilot.append(int(matchlist[i].pilot))

       # self.pilot = [matchlist[i].pilot for i in matchlist if matchlist[i].teamnumber == self.number and matchlist[i].pilot == 1]

    def fillalliances(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if matchlist[i].team == self.number:  #did your team play in this match
                self.alliances.append(matchlist[i].alliance)

      #  self.alliances = {matchlist[i].matchnumber: matchlist[i].alliance for i in matchlist if matchlist[i].teamnumber == self.number}

    def fillfieldpos(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if matchlist[i].team == self.number:  #did your team play in this match
                self.fieldpos.append(int(matchlist[i].fieldpos))
       # self.fieldpos = {matchlist[i].matchnumber: matchlist[i].fieldpos for i in matchlist if matchlist[i].teamnumber == self.number}

    def fillautogears(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if matchlist[i].team == self.number:  #did your team play in this match
                self.autogears.append(int(matchlist[i].autogears))
       # self.autogears = {matchlist[i].matchnumber: matchlist[i].autogears for i in matchlist if matchlist[i].teamnumber == self.number}

    def fillautokpa(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if matchlist[i].team == self.number:  #did your team play in this match
                self.autokpa.append(int(matchlist[i].autokpa))
       # self.autokpa = {matchlist[i].matchnumber: matchlist[i].autokpa for i in matchlist if matchlist[i].teamnumber == self.number}
    
    def fillclimb(self):
        for i in range(0, len(matchlist)):   #I wanted to do this in a list 
            if matchlist[i].team == self.number:  #did your team play in this match
                self.climb.append(int(matchlist[i].climb))
       # self.climb = {matchlist[i].matchnumber: matchlist[i].climb for i in matchlist if matchlist[i].teamnumber == self.number}


def testfidelityUI():
    print()
    print()
    print("You have chosen to test a matches fidelity.")
    print("These matches are currently in the database.")
    showmatchesUI()
    print("Which match would you like to test?")


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


def teamcomparisonUI():
    # this function creates a comparison of 2 teams for quick reference.
    print()
    print("Welcome to the Team Comparison Tool")
    print("Which teams would you like to compare?: ")
    print()


def populateteamdict():
    # this function creates a dict where the key is
    # the team number (string) and the value is the team object.
    for i in range(0, len(teamlist)):
        teamdict.update({teamlist[i]: teamlist2[i]})


def fillteamstats():
    # this function pulls team data from the matchlist data
    for i in teamdict:
        teamdict[i].fillmatches()
        teamdict[i].fillmatchwins()
        teamdict[i].fillgearsdelivered()
        teamdict[i].fillkpa()
        teamdict[i].fillpilot()
        teamdict[i].fillalliances()
        teamdict[i].fillfieldpos()
        teamdict[i].fillautogears()
        teamdict[i].fillautokpa()
        teamdict[i].fillclimb()


def createteamlist():
    # This very Janky function creates a list of team numbers, a matching list of team objects and calls the teamdict function
    # I really dont like this function it is not really necessary and poorly concieved but I could not get the "elegant" way
    # to work right and I needed something that worked in this case.
    for i in range(0,len(matchlist)):
        testteamnum = matchlist[i].team
        if testteamnum not in teamlist:
            teamlist.append(testteamnum)
    for j in range(0,len(teamlist)):    #I THINK THIS IS SUPER JANKY BUT I COULD NOT GET A DIRECT CLASS LIST CREATION TO WORK! :(
        teamlist2.append(Team(teamlist[j]))
    populateteamdict()
    fillteamstats()

def readmatchfile():
    # this function imports a match file CSV
    # in the future I would like this to be done in a database.
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

    print()
    print()
    print("File has been read.")
    print()
    print()
    createteamlist()
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
    for i in range(0, len(teamlist)):
        if team == str(teamlist[i]):
            existance = True
    return existance


def duplicatecheck(team, array):
    # takes a team and an array, checks if it occurs more than once
    duplicatestat = False
    if array.count(team) >= 1:
        duplicatestat = True
    return duplicatestat

def executemonte(matchsetuparray, runs=100000, factor = .2, rangemin = -1, rangemax = 1):
    # this functions executes a monte carlo run.
    # it is nominally called from the setupmonteUI fnc.
    # currently this monte carlo ONLY works on gear scores
    grossresults = []   #this will be a memory hog try to think of how to use a generator
    #create array with team's average score
    bluewin = 0
    tie = 0
    percentconversion = runs / 100
    for i in range(0, runs):
        scores = [None, None, None, None, None, None]
        for j in range(0, len(scores)):
            roll = random.randint(rangemin, rangemax)  # creates a random number between the range bounds
            scores[j] = roll * teamdict[matchsetuparray[j]].averagegears  # adds roll value to average 
        for k in range(0, len(scores)):  # prevents a negative score
            if scores[k] <= 0:
                scores[k] = 0
        bluescore = scores[0] + scores[1] + scores[2]   #needed to sum half the array each
        redscore = scores[3] + scores[4] + scores[5]
        if bluescore > redscore:    # who won?
            bluewin += 1
        elif bluescore == redscore:  # if nobody won
            tie += 1
        print("Red: {}, Blue: {}".format(redscore, bluescore))
    blueresults = bluewin / percentconversion
    tieresults = tie / percentconversion
    print("Blue Wins {} percent of the time.".format(blueresults))
    print("Red Wins {} percent of the time.".format((runs - bluewin - tie) / percentconversion))
    print("Game ties {} percent of the time.".format(tieresults))
    primaryUI()

        #montescores.append(MonteResult(bluescore, redscore, i)) #creates an instance of monte match.monte
        #dump detailed result file.


def showteamdata(teamnumber):
    print()
    print()
    print(str(teamdict[teamnumber]))
    print("Matches Played: {}".format(teamdict[teamnumber].nummatches))
    print("Wins: {}, Losses: {}".format(len(teamdict[teamnumber].matchwins), teamdict[teamnumber].nummatches - len(teamdict[teamnumber].matchwins)))
    print("Total Gears Delivered: {}".format(sum(teamdict[teamnumber].gearsdelivered)))
    print("Most Gears Delivered in one match: {}".format(teamdict[teamnumber].maxgearsdelivered))
    print("Fewest Gears Delivered in one match: {}".format(teamdict[teamnumber].mingearsdelivered))
    print("Average Gears Delivered per match: {}".format(teamdict[teamnumber].averagegears))
    print("KPA Delivered: {}".format(sum(teamdict[teamnumber].kpa)))
    print("Most KPA Delivered: {}".format(teamdict[teamnumber].maxkpa))
    print("Lowest KPA Delivered: {}".format(teamdict[teamnumber].minkpa))
    print("Average KPA Delivered: {}".format(teamdict[teamnumber].averagekpa))
    print("Total Climbs: {}".format(sum(teamdict[teamnumber].climb)))
    print("Climb Percentage: {}".format(teamdict[teamnumber].climbpercent))
    print()
    print()
    #    self.kpa = []
     #   self.pilot = []
      #  self.alliances = []
       # self.fieldpos = []
#        self.autogears = []
 #       self.autogearsinpos = []
  #      self.autokpa = []
   #     self.autokpainpos = []
    #    self.climb = []
     #   self.matchwins = []


def dumpmontedata():
    # This function displays monte carlo run data
    print()
    print("Monte Carlo Run data.")
    print()
    for i in range(0, len(montelist)):
        print("MonteMatch {} : {}".format(i, str(montelist[i])))


def setupmonteUI():
    setupuserin = None
    teamarray = []
    print()
    print()
    print("Welcome to the Monte Carlo Setup")
    # print(str(teamlist))
    print()
    teamcheck = None
    for i in range(1, 3):
        if i == 1:
            alliancemessage = 'Blue'
        else:
            alliancemessage = 'Red'
        for j in range(1, 4):
            setupuserin = None
            while True:
                print()
                print()
                print("Teams in the Database Include: {}".format(teamlist))
                setupuserin = input("Please select a team for the {} Alliance in field pos {}: ".format(alliancemessage, j))
                teamcheck = doesteamexist(setupuserin)
                dupcheck = duplicatecheck(setupuserin, teamarray)
                # print("Team Check:{}".format(teamcheck))
                # print("Dupicate Check: {}".format(dupcheck))
                if teamcheck is False:
                    print("Team {} not found.".format(setupuserin))
                    print("Please enter a valid team.")
                    continue
                if dupcheck is True:
                    print("Team {} is already assigned to an alliance.".format(setupuserin))
                    print("Please enter a valid team.")
                    continue
                if teamcheck is True and dupcheck is False:
                    teamarray.append(setupuserin)
                    print("The following teams are in your match: {}".format(teamarray))
                    break
    print("You have set up the following match.")
    print(teamarray)
    print()
    print()
    executemonte(teamarray)


    # monte carlo should run 10000 times.  
    # MVP is to only work on gear points.

def testingthing():
    # interrogates a team object to make sure it is correctly passing data

    for i in range(0, len(matchlist)):
        print(matchlist[i].team)


def logmatch():
    # this would nominally bring up a GUI for logging a match. 
    # upon closing the logger it will update the database or CSV file
    # it will also add a match object with the match data for use in team stats
    # it does not do anything right now.
    print()
    print("Sorry! but this module doesnt exist at ths time")
    print("In this program it is spoofed by a match list.")
    print("The intention was to use WX python for this interface")
    print("Unfortunately I had to brutally descope to make this work.")
    print()
    primaryUI()


def showteamsUI():
    print()
    print()

    if len(teamdict) < 1:
        print("There are no teams in the database.")
        print("This likely means you need to import a database.")
        viewdbUI()
    else:
        print("There are several teams in the Database:")
        for i in teamdict:
            print(teamdict[i])
        while True:
            userin = input("Please enter the number of the team you would like to view:")
            if doesteamexist(userin) is True:
                showteamdata(userin)
                break
            else:
                print("You have entered and invalid team.  Please try again.")
                continue
    print()
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
    # this function is the UI for the database viewer.
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
            testfidelityUI()
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
#    print('6 - Test FunctionCall')
    while True:
        userin = input('Please select 1-5: ')
        if userin == '1':
            logmatch()
        elif userin == '2':
            viewdbUI()
        elif userin == '3':
            setupmonteUI()
        elif userin == '4':
            readmatchfile()
        elif userin == '5':
            exit()
#        elif userin == '6':
#            populateteamdict()
        else:
            print('You did not select a valid option.')
            primaryUI()

primaryUI()
