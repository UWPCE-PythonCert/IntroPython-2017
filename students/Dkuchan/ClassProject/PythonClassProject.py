# PythonClassProject.py
''' This python program is written for the advanced python programming class
    it is a scouting program written for the First Robotics Competition based
    on the 2017 game FIRST Steamworks. '''




    '''Need to add a tuple for allowed users to baseline who does what'''



class Match:
    ''' A match is a collection of data which represents a match.
    Match is the primary class which is edited by the user.'''
    def__init__(self):


class Team:
    ''' Team is an object which contains data specific to a team
    it is not intended to be user editable but is user viewable'''

    def __init__(self):


class Roster:
    '''class which holds a list of teams, should only be updated
    passively or by admin'''

class Competition:
    ''' A competition is a collection of matches.  It is only intended
    to be changed by an admin or mentor.'''
    def __init__(self):



def logmatch():


def viewdbui():
    '''allows the user to select options about viewing DB'''


def updatedatabase():

def importdatabase():


def setupmonte():
    '''Allows the user to set parameters for
    the monte carlo analysis'''


def simulation(runs):
    '''Runs a monte carlo with the number of runs and imported params
    as designated in setupmonte()'''


def primaryUI():
    # This is the introductory user interface

    print('Welcome to the FRC Scouter Program')
    print()
    print()
    print('What would you like to do?')
    print('1 - Log a match')
    print('2 - View the Team Database')
    print('3 - Run a Monte Carlo Analysis')
    while True:
        userin = input('Please select 1-4: ')
        if userin == '1':
            logmatch()
        elif userin == '2':
            viewdbui()
        elif userin == '3':
            setupmonte()
        else:
            print('You did not select a valid option.')
