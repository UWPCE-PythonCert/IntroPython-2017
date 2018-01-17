# FRC SCOUTER
# frcscouter.py

class Competition():
    # this class holds information specific to a certain competition
    def __init__(self, cname):
        self.compname = cname
        self.teamroster = []


class Match():
    # this class holds information specific to a certain match
    def __init__(self, mnumber)
        self.teamnumber
        self.matchnum = mnumber
        self.alliance
        self.winloss
        self.pressure
        self.gears
        self.autogear
        self.replaylink


class Team():
    """ Collects team statistics.
    Including both in match statistics as well as persistant. """

    def __init__(self, tnumber):

        self.tnumber = tnumber
        self.tname
        self.pressure
        self.geardelivery
        self.autogear
        self.penalties
        self.climb
        self.wins
        self.losses
        self.matches
        self.runningaverage
        self.

class League():
    def __init__(self):


def welcomeUI():
    # Provides the user with an introductory UI
    print("Hello, Welcome to SCOUT")
    while True:
        try:
            userin = input("Please select a function: ")
            numtest = int(userin)
        except ValueError:
            print("You have made an invalid selection.")
            continue
        else:
            if userin == 1:
                scoutmatchUI()
            elif userin == 2:
                predictor()


            break

def scoutmatchUI():
    # Initial User Interface for match scouting
    print()
    print()
    print("You have chosen to scout a match.")
    print("Which team are you scouting?")

def scoutupdate():


def predictor():


def matchUI():

    ''' To log a match you need to do the following
        Get Userinput for match number
        Get Userinput for team number
        Get Userinput for alliance (this can be a 0 / 1)
        Get Userinput for field position
        Ask if the input data is correct let them update any of them directly
        If data is correct begin scouter
        say a = +1 kpa auto, s = -1
        q = +1 gear, w = -1 gear
        enter goes to teleop
        evaluate input - if q>1 q==1
        same keys for incriment
        add z for climb
        enter closes logging
        did your team win Y/N?
        evaluate input 
        output results for match
        ask if this is correct
        if not allow mod of any specific attribute
        if so update database and close go back to welcomUI
        '''


    print()
    print()
    print("You have chosen to scout a match.")
    


    while True:
        try:
            userin = input("Which match are you scouting?")
            numtest = int(userin)
        except ValueError:
            print("You have made an invalid selection.")
            continue
        else:
            match.matchnum = userin
            break
    print()
    print()

    while True:
        try:
            userin = input("Which team are you scouting?")
            numtest = int(userin)
        except ValueError:
            print("You have made an invalid selection.")
            continue
        else:
            match.teamnumber = userin
            break

def setmatchnum():
    while True:
        try:
            userin = input("Which match are you scouting?")
            numtest = int(userin)
        except ValueError:
            print("You must enter a number.")
            continue
        else:
            match.matchnum = userin
            break

