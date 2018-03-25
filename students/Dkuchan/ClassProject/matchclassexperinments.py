
import csv

matchlist = []

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


#matchlist.append(Match(1,4469))
#matchlist.append(Match(2,4469))

# def creatematch(matchnumber, teamnumber):
# check to see if this entry is already in the list
#for i in range (0, len(matchlist)):
 #   if matchlist[i].matchnumber == matchnumber:
#if entry is not in the list create a new match
#matchlist.append(Match(matchnumber,teamnumber))


def interimupdater(mnumber, teamnumber):

    # this is intended to be the match input area
    # It is an interrim solution to be able to add data to the match class
    # until I am able to come up with a WXpython interface.teamnumber
    # CURRENTLY IT IS NOT ROBUST TO FAILURES
    found = 0
    for i in range(0, len(matchlist)):
        if matchlist[i].matchnumber == mnumber and matchlist[i].team == teamnumber:
            found = 1
            print("Please enter the requested information for match " + str(mnumber) + " team number " + str(teamnumber) + ":")
            print()
            userin = input('Please enter gears placed: ')
            matchlist[i].gears = userin
            print()
            userin = input('Please enter win loss (0/1): ')
            matchlist[i].win = userin
            print()
            userin = input('Please enter alliance (Red/Blue): ')
            matchlist[i].alliance = userin
    if found == 0:
        print("Im sorry we were unable to locate that match file.")

#def dumptofile():

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

def updategears(mnumber, teamnumber, gears):
    found = 0
    for i in range (0, len(matchlist)):
        if matchlist[i].matchnumber == mnumber and matchlist[i].team == teamnumber:
            matchlist[i].gears = gears
            found = 1
    if found == 0:
        print("Target Not Found - No Updates Made")

'''
for i in range (0, len(matchlist)):
    print(str(matchlist[i]))
    print()
    print()
    print(repr(matchlist[i]))

interimupdater(1, 4466)

for i in range(0, len(matchlist)):
    print(matchlist[i].gears)

    '''
readfile()
for i in range(0, len(matchlist)):
    print(str(matchlist[i]))
    print()
    print()
    print(matchlist[i].gears)