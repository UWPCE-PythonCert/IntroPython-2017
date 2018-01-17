#classmailroom.py

# classessheet.py
""" This is a script to mess with classes.
    The idea is to use this practice to create class "persons" for mail room """
# import os


class Donor:
    # This is an experimental class for donors in mailroom
    def __init__(self, name):

        self.first_name, self.last_name = list(name.split())
        self.donations = [1, 2, 3, 4, 5, 6, 7]
        # self.fullname = str(self.first_name + ' ' + self.last_name)
        # self.averagedon = sum(self.donations) / len(self.donations)
        # self.maxdon = max(self.donations)
        # self.totaldonations = sum(self.donations)

    @property
    def totaldonations(self):
        return(sum(self.donations))

    @property
    def maxdon(self):
        return(max(self.donations))

    @property
    def averagedon(self):
        return(self.totaldonations / len(self.donations))

    @property
    def namelen(self):
        return(len(str(self.fullname)))

    @property
    def lastfirst(self):
        return ('{}, {}'.format(self.last_name, self.first_name))

    @property
    def fullname(self):
        return(str(self.first_name + ' ' + self.last_name))

    def updatenames(self, name):
        self.first_name, self.last_name = list(name.split())


donorlist = []
donorlist.append(Donor('Dan Kuchan'))
donorlist.append(Donor('Abbey Kuchan'))
donorlist.append(Donor('Blabedy Blah'))
donorlist.append(Donor('Brandon Butsick'))
donorlist.append(Donor('Megan Kuchan'))
donorlist.append(Donor('Chris Jaeger'))

def longestname():
    # Finds the longest name and returns its length.
    length = 0
    for i in range(0, len(donorlist)):
        if donorlist[i].namelen >= length:
            length = donorlist[i].namelen
    return length


def thanksUI():
    # Presents the user with a UI to select which donor gets a thank you note.
    print()
    print()
    print("You have chosen to send a thank you note.")
    print("Whome would you like to thank?")
    for i in range(0, len(Donor.rosterraw)):
        optionstrng = str(i) + ' : ' + str(donorlist[i].fullname)
        print(optionstrng)
    while True:
        try:
            userSelect = input("Please enter the number of your selection: ")
            userSelect = int(userSelect)
        except ValueError:
            print("You have made an invalid selection!")
            continue
        if userSelect < len(donorlist):  # is user input in range?
            createthanks(userSelect)
        else:
            print("You have made an invalid selection!")
            continue


def createthanks(nametarget):
    # Creates a thank you note for the donor that is passed in.
    print()
    print()
    message = "Dear " + str(donorlist[nametarget].fullname) +", " + "\n" + "The Dan Kuchan Charitable Organization would like to offer its sincere thanks for your to date donation of $" + str(donorlist[nametarget].totaldonations) + "."
    print(message)
    print()
    print()
    userfront()


def addoner():
    # Adds a donor to the donor database.
    print()
    print()
    newdonor = input("Please enter new Donor: ")
    donorlist.append(Donor(newdonor))
    print(str(donorlist[-1].fullname) + " has been added to the database.")
    updateUI()


def addonationUI():
    # Presents the user with a UI to allow them to select which donor is affected by the donation update.
    print()
    print()
    print("You have chosen to add a donation to an existing donor.")
    print("Please select an existing donor.")

    for i in range(0, len(Donor.rosterraw)):
        optionstrng = str(i) + ' : ' + str(donorlist[i].fullname)
        print(optionstrng)
    while True:
        try:
            userSelect = input("Please enter the number of your selection: ")
            userSelect = int(userSelect)
        except ValueError:
            print("You have made an invalid selection!")
            continue
        if userSelect < len(donorlist):  # is user input in range?
            addonation(userSelect)
        else:
            print("You have made an invalid selection!")
            continue


def addonation(nametarget):
    # Executes the update to the users donations.
    print()
    print()
    while True:
        try:
            donvalue = input("Please enter the ammount of the donation: ")
            donvalue = int(donvalue)
        except ValueError:
            print("You have made an invalid selection!")
            continue
        donorlist[nametarget].donations.append(donvalue)
        updateUI()


def updatedonornameUI():
    # Presents the user with a UI to allow them to select which name they want to update.
    print()
    print()
    print("You have chosen to update the name of an existing donor.")
    print("Please select an existing donor.")

    for i in range(0, len(donorlist)):
        optionstrng = str(i) + ' : ' + str(donorlist[i].fullname)
        print(optionstrng)
    while True:
        try:
            userSelect = input("Please enter the number of your selection: ")
            userSelect = int(userSelect)
        except ValueError:
            print("You have made an invalid selection!")
            continue
        if userSelect < len(donorlist):  # is user input in range?
            updatedonorname(userSelect)
        else:
            print("You have made an invalid selection!")
            continue


def updatedonorname(userSelection):
    # Executes the update to the Donor class name by calling class method updatenames()
    print()
    print()
    print("You have selected the donor name " + donorlist[userSelection].fullname + " to be replaced.")
    newname = input("Please enter the new name: ")
    donorlist[userSelection].updatenames(newname)
    userfront()


def updateUI():
    # Presents the user with a UI to select what data they want to change.
    print()
    print()
    print("You have chosen to update the database.")
    print("You have the following options:")
    print("1:  Add a donor.")
    print("2:  Add a donation to an existing donor.")
    print("3:  Change the name of an existing donor.")
    print("4:  Return to main menu.")
    while True:
        try:
            userSelect = input("Please enter the number of your selection: ")
            userSelect = int(userSelect)
        except ValueError:
            print("You have made an invalid selection!")
            continue
        if userSelect == 1:
            addoner()
            break
        elif userSelect == 2:
            addonationUI()
            break
        elif userSelect == 3:
            updatedonornameUI()
        elif userSelect == 4:
            userfront()
        else:
            print("You have made an invalid selection!")
            continue


def viewDBUI():
    # Draws a spreadsheet to show the contents of the database.
    print("You have chosen to view the database...")
    print("So here it is:")
    columntitles = "Donor Name" + (' ' * (longestname() + 5 - 10)) + " | " + "Total Given | Num Gifts | Average Gift"
    print(columntitles)
    for i in donorlist:
        datastring = str(i.fullname) + (" " * (longestname() + 6 - i.namelen)) + " $ " + "{:.2f}".format(i.totaldonations) + "      " + str(len(i.donations)) + " $ " + str(i.averagedon)
        print(datastring)
    print()
    print("Returning to Main Menu")
    print()
    userfront()


def userfront():
    # Presents the user with a main menu.
    # USE DEDENT TO FORM THESE UI LINES
    print()
    print()
    print("Hello welcome to the mailroom.")
    print("What would you like to do?")
    print("1:  Write a Thank You Note")
    print("2:  Update the Donor Roster")
    print("3:  View the database")
    print("4:  Quit")

    while True:
        try:
            userSelect = input("Please enter the number of your selection: ")
            userSelect = int(userSelect)
        except ValueError:
            print("You have made an invalid selection!")
            continue
        if userSelect == 1:
            thanksUI()
            break
        elif userSelect == 2:
            updateUI()
            break
        elif userSelect == 3:
            viewDBUI()
        elif userSelect == 4:
            exit()
        else:
            print("You have made an invalid selection!")
            continue


userfront()