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
        self.matchnum = mnumber
        self.redalliance
        self.bluealliance
        self.winner
        self.loser
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


def 