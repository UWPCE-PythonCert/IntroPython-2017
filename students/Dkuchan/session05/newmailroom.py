#newmailroom.py
import time


roster = [['Dan', 100, 200, 300, 400], ['Abbey', 100, 200, 300], ["Megan", 100, 200, 300, 100, 100], ['Spencer', 100, 200, 300], ['Marylee', 100, 200, 300]]    



def identifyDon(nameloc):
    print()
    print()
    print()
    print("You have selected: " + roster[nameloc][0])
    print(roster[nameloc][0] + " has made " + str(len(roster[nameloc])-1) + " donations")
    for i in range(1, len(roster[nameloc])):
        print(str(i) + ": ",end="")
        print(roster[nameloc][i])
    print()
    print()
    while True:
        try:
            donationselect=input("For which donation would you like to thank " + roster[nameloc][0] +"? : ")
            donationselect=int(donationselect)
        except:
            print("You have made an invlaid selection.")
            continue
        if donationselect>=1 and donationselect<=len(roster[nameloc])-1:
            printthanks(nameloc,donationselect)
            break
        else:
            print("You have made an invalid selection.")
            continue
    print()
    print()





def createthankyou():
    print()
    print()
    print()
    print()



    while True:
        print("Whome would you like to thank?")
        for i in range(0, len(roster)):
            print(roster[i][0])
        print()
        selection = input("Please type the name of the donor you would like to thank: ")
        for i in range(0, len(roster)):
            if selection in roster[i]:
                nameloc=i
                identifyDon(nameloc)
                break
            else:
                print("You have entered a name that is not in the database.")

                
def printthanks(name,don):
    print()
    print()
    print()
    print("Dear " + str(roster[name][0]) + ",")
    print("The Dan Kuchan Charitable Society would like to thank you for your generous donation of $" + str(roster[name][don]) + ".",end="")
    print("  This changes the lives of many people.")
    print("Sincerely, Dan Kuchan")
    print()
    print()
    while True:
        userSelect=input("Woud you like to thank another person? (Y/N): ")
        if userSelect=='Y':
            createthankyou()
            break
        elif userSelect=='N':
            userinterface()
            break
        else:
            print("You have made an invalid selection.")
            continue
def queryroster(querytarget):
    for i in range(0,len(roster)):
        if querytarget in roster[i]:
            break
            return i
        else:
            return False

def newname():
    """Checks to see if a name is in the database.  If not it adds it.
    """




def datamod():
    print()
    print()
    print()
    print("You may either add a new entry to the roster or modify an existing entry.")
    print("1: Add new entry.")
    print("2: Modify existing entry.")
    while True:
        try:
            userSelect=input("Please make a selection: ")
            userSelect=int(userSelect)
        except:
            print("You have made an invalid selection.")
            continue
        if userSelect==1:
            print("You have chosen to add a new entry.")
            while True:
                userinput=input("Please enter the name you would like to add: ")
                if queryroster(userinput) != False:
                    print("This name is already in the database.  Please try again.")
                    continue
                else:
                    roster.append(userinput)
                    print(userinput + " has been added to the roster.")
                    break
"""

        elif userSelect==2:
            print("You have chosen to modify an existing entry.")
            for i in range(0, len(roster)):
            print(roster[i][0])
            print()
            while True:
                userinput=input("Please enter name to be modified.")
                for i in range(0,len(roster)):
                    if userinput in roster[i]:
                       nameloc=i
                    break
"""

"""
def adddonation(name, ammount):

    print("A donation of $ " + ammount + " was added to " + name + "'s file.")


def addperson(name):
    roster.append(name)
    print(name + " has been added to the database.")


def printthanks(name,don):
    print("Dear " + name + ",")
    print("The Dan Kuchan Charitable Society would like to thank you for your generous donation of $" + don + ".",end="")
    print("This changes the lives of many people.")
    print("Sincerely, Dan Kuchan")

def creatdb():
    #creates and fills out a form with names and donations
    
    #TODO Find the longest name and use len to get its length
    lngstNmln=0
    for j in range(0,len(roster)):
         if len(roster[j][0])>lngstNmln:
            lngstNmln=len(roster[j][0])
    whtSpcgen = lngstNml - 5
    
    print("Name" + " " * whtSpcgen + " | " + "Average Donation" + " | " + "Num Donations" + " | " + "Total Donations" + " | ") 
    for i in range(0, len(roster):
        print(roster[i][0] + " " + " | " + len(roster) - 1)

"""

def userinterface():
#This form creates the primary UI, takes user input and activates program functions
    print()
    print()
    print()
    print("Welcome to the Mailroom!")
    print("What would you like to do?")
    print("1:  Create a Thank You message.")
    print("2:  View the database.")
    print("3:  Modify the database")
    print("4:  Quit Program")

    while True:
        try:
            userSelect = input("Please enter the number of your selection: ")
            userSelect = int(userSelect)
        except ValueError:
            print("You have made an invalid selection!")
            continue
        if userSelect == 1:
            createthankyou()
            exit()
            break
        elif userSelect == 2:
        #creatdb()
            exit()
            break
        elif userSelect == 3:
            datamod()
        elif userSelect == 4:
            exit()
        else:
            print("You have made an invalid selection!")
            continue

userinterface()

