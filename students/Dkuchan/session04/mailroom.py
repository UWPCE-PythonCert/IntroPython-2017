#mailroom.py
#root data--------------------------------------

roster=[['Dan',100,200,300,400],['Abbey',100,200,300],["Megan",100,200,300,100,100],['Spencer',100,200,300],['Marylee',100,200,300]]        #roster is a matrix containing names in column 0 and donations in 1,2,or 3

#root data--------------------------------------

#function definition section--------------------

#A Note on the Thank you Section:  I would rather set this up to allow me to select numbers which correspond to names rather than having to type the name in correctly but that is not what the instruction say

            addname()       




                



'''
print(i+1,end="")
        print(": ",end="")
'''
#once we have a name look at available donations
# Query user, which donation would you like to thank them for?
# trigger thank you not generator
"""
"""
def thankyougen(desirednamepos,donationposselection):
    print("thanksyougen")
    print("Thank you " + roster[desirednamepos][donationposselection] + "for your generous donation of " + roster[desirednamepos][donationposselection] + ".")


"""
def reportcreator():
    print("ReportCreator")
   #identify the longest name
    i=0
    maxfl=0
    for i in range(0,len(roster)):
        fieldlen=len(roster[i][0])
        if fieldlen>maxfl:
            maxfl=fieldlen
            maxpos=i

    #identify longest donation 
    if maxfl<=10:
        print("Donor Name",end="")
        headerstring="Donor Name" + ' ' * (maxfl - 10) + '|' + " Total Given " + '|' + " Num Gifts " + '|' + " Average Gift "
    else:
        print(headerstring)
        print('-' * len(headerstring))
    
    i=0
    for i in range(0,len(roster)):
        j=1
        numgifts=len(roster[i])-1
        totaldonations=0
        for j in range(1,numgifts+1):
            totaldonations+=roster[i][j]
        averagedonations=totaldonations/numgifts
        print(roster(i,0) + ' ' * maxfl-10 + ' ' + '$' + {:.2f}.format(totaldonations) + ' ' * 6 + '|' + {:.0f}.format(numgifts) + ' ' + '$' + {:.2f}.format(averagedonations))

"""


#primary function calling loop
while True: #this loop is not robust to non integer input!!!! YET
    print("Welcome to Mailroom Script")
    print("What would you like to do?")
    print("1:Send a Thank You note")
    print("2:Create a report")
    print("3:Quit")
    userselection = input("Please enter desired option (1,2,3): ")
    userselection = int(userselection)
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
