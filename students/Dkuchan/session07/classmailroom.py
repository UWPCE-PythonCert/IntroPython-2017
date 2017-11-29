#classmailroom.py

# classessheet.py
""" This is a script to mess with classes.
    The idea is to use this practice to create class "persons" for mail room """


class Donor:
    # This is an experimental class for donors in mailroom
    numdonors = 0
    rosterraw = []

    def __init__(self, name):

        self.first_name, self.last_name = list(name.split())
        self.donations = [1, 2, 3, 4, 5, 6, 7]
        self.fullname = str(self.first_name + ' ' + self.last_name)
        self.averagedon = sum(self.donations) / len(self.donations)
        self.maxdon = max(self.donations)
        self.totaldonations = sum(self.donations)
        Donor.numdonors += 1
        Donor.rosterraw.append(self)

    def updatecalcs(self):
        # Updates the average donation attribute after mods have been made to donations
        self.averagedon = sum(self.donations) / len(self.donations)
        self.maxdon = max(self.donations)

    def lastfirst(self):
        # creates a last name , first name string
        lastfirstname = '{}, {}'.format(self.last_name, self.first_name)
        return lastfirstname

    def appenddonations(self, newdon):
        ''' Adds a donation to the donations list
            Updates the average donations
            Updates the max donation '''
        self.donations.append(newdon)
        self.updatecalcs()


    def updatenames(self, newname):
        self.first_name, self.last_name = newname.split()
        self.fullname = str(self.first_name + ' ' + self.last_name)

donorlist = []
donorlist.append(Donor('Dan Kuchan'))
donorlist.append(Donor('Abbey Kuchan'))
donorlist.append(Donor('Blabedy Blah'))


def thanksUI():
    # Presents the user with a UI for the thank you note function.
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
    print()
    print()
    message = "Dear " + str(donorlist[nametarget].fullname) +", " + "\n" + "The Dan Kuchan Charitable Organization would like to offer its sincere thanks for your to date donation of $" + str(donorlist[nametarget].totaldonations) + "."
    print(message)
    print()
    print()
    userfront()

def addoner():
    print()
    print()
    newdonor = input("Please enter new Donor: ")
    donorlist.append(Donor(newdonor))
    print(str(donorlist[-1].fullname) + " has been added to the database.")
    updateUI()

def addonationUI():
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
    print()
    print()
    while True:
        try:
            donvalue = input("Please enter the ammount of the donation: ")
            donvalue = int(donvalue)
        except ValueError:
            print("You have made an invalid selection!")
            continue
        donorlist[nametarget].appenddonations(donvalue)
        updateUI()

def updatedonornameUI():
    print()
    print()
    print("You have chosen to update the name of an existing donor.")
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
            updatedonorname(userSelect)
        else:
            print("You have made an invalid selection!")
            continue


def updatedonorname(userSelection):
    print()
    print()
    print("You have selected the donor name " + donorlist[userSelection].fullname + " to be replaced.")
    newname = input("Please enter the new name: ")
    donorlist[userSelection].updatenames(newname)
    userfront()

def updateUI():
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
    print("You have chosen to view the database...")
    print("So here it is:")

def userfront():
    # Presents the user with a main menu.
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