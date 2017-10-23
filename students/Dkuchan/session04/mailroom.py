#mailroom.py
#root data--------------------------------------

roster=[['Dan',100,200,300],['Abbey',100,200,300],["Megan",100,200,300],['Spencer',100,200,300],['Marylee',100,200,300]]        #roster is a matrix containing names in column 0 and donations in 1,2,or 3

#root data--------------------------------------

#function definition section--------------------

#A Note on the Thank you Section:  I would rather set this up to allow me to select numbers which correspond to names rather than having to type the name in correctly but that is not what the instruction say
def thankyouUI():
    print("You have chosen to create a thank you note")
    print("Here are the names in the database")
    numnames=len(roster)
    for i in range(0,numnames):
        print(roster(i))
thankyouselection=input("To whome would you like to send a note?: ")
    j=0
    for j in range(0,numnames):
        if thankyouselection in roster:
            desirednamepos=roster.index(roster(j,0))
        else namequery=input("You have entered a name that is not in the database, would you like to add it (Y/N): ")
            if namequery=='Y':
                #add name to roster in next available position
            elif namequery=='N':
                #take the user back to the name input because they made a typo
            else:
                #you have not entered a "Y" or an "N", please do so: 

#once we have a name look at available donations
# Query user, which donation would you like to thank them for?
# trigger thank you not generator

def thankyougen(X,Y)
    print"Thank you " + roster(X,0) + "for your generous donation of " + roster(X,Y) + "."


while true:
    try:



#def createreport():



#def quitter():








#function definition section--------------------
#thankyou()



#primary function calling loop
while true:
    try:
        print("Welcome to Mailroom Script")
        print("What would you like to do?")
        print("1:Send a Thank You note")
        print("2:Create a report")
        print("3:Quit")
        userselection=input("Please enter desired option (1,2,3): ")
            if userselction!=1 or userselction!=2 or userselction!=3:
                print("Please enter 1,2 or 3")
                userselection=input("Please enter desired option (1,2,3): ")
            elif userselection=1:
                thankyou()
            elif userselection=2:
                createreport()
            elif userselection=3:
                quit()





    break