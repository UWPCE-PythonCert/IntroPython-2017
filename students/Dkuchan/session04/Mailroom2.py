#Mailroom2.py
#my first mail room was so stupid i started over.

roster=[['Dan',100,200,300,400],['Abbey',100,200,300],["Megan",100,200,300,100,100],['Spencer',100,200,300],['Marylee',100,200,300]]


def rootUI():
    while True: #this loop is not robust to non integer input!!!! YET
        print("Welcome to Mailroom Script")
        print("What would you like to do?")
        print()
        print("1:Send a Thank You note")
        print("2:Create a report")
        print("3:Quit")
        userselection = input("Please enter desired option (1,2,3): ")
        try:
            userselection = int(userselection)
        except ValueError:
            print("Please enter 1,2, or 3")
            prootUI()





        if userselection == 1 or userselection == 2 or userselection == 3:
            break
        else:
            print("Please enter 1,2, or 3")
            continue

    if userselection == 1:
        thankyouUI()
    elif userselection == 2:
        reportcreator()
    elif userselection == 3:
        print("Quit")
        exit()

rootUI()