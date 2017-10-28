#! /usr/bin/env Python
"""
It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.

You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
"""

from time import sleep
import pprint

if __name__ == '__main__':
    objFileName = "C:\Files\donate.txt"
    strData = ""
    dicRow = {}
    lstTable = []

# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",") # readline() reads a line of the data into 2 elements
    dicRow = {"Name":strData[0].strip(), "Total":strData[1].strip(), "Num":strData[2].strip()}
    lstTable.append(dicRow)
objFile.close()

# Display a menu of choices to the user
while(True):
    print ("""
    Menu of Actions
    1) Send a Thank You
    2) Create a Report
    3) quit
    """)
    strChoice = str(input("choose from a menu of 3 actions [1 to 3] - "))
    print()#adding a new line

    if (strChoice.strip() == '1'):
        #   print("Donor Name                | Total Given | Num Gifts | Average Gift\n------------------------------------------------------------------")

                while(True):
                    strName = str(input("What is Donor Name? (type list or back for menu)- ")).strip()
                    print()#adding a new line
                    if (strName.strip() == 'list'):
                        print("Donor Name | Total Given | Num Gifts | Average Gift\n------------------------------------------------------------------")
                        #        for dicRow in lstTable:
                        #            print(dicRow)
                                        #4a Show the current items in the table
                        for row in lstTable:
                            print ("{}, ${:.2f}, {}, ${:.2f}".format(row["Name"], float(row["Total"]), row["Num"], float(row["Total"])/int(row["Num"])))
                            continue #to show the menu
                        #            Total = float(row["Total"])
                        #            Num = int(row["Num"])
                        #            Ave = (Total/Num)
                        #            print(Ave)
                        #            print(row["Name"] + '         $' + row["Total"] + row["Num"]  + '  $' + "{:.2f}".format(str(float(row["Total"])/int(row["Num"]))))
                        #            print(row["Name"] + '         $' + row["Total"] + row["Num"]  + '  $' + "{:.2f}".format(float(row["Total"])/int(row["Num"])))
                        #            print ("{}, ${:.2f}, {:.2f}, ${:.2f}".format(row["Name"], row["Total"], row["Num"], float(row["Total"])/int(row["Num"])))

        #                        print()#adding a new line

                    elif (strName.strip() == 'back'):
                        break #and Exit the program
                    else:
                        for row in lstTable:

        #                    print("list: " + row["Name"])
                            if (strName == row["Name"]):
                                print("name is in the list, use " + row["Name"] + " who already donated total $" + str(row["Total"]) + " of " + str(row["Num"]) + " donations")

#                                floatTotal = float(input("What is the Total Given? - ")).strip()
                                floatTotal = float(input("What is the Total Given? - "))

                                floatTotal = float(floatTotal) + float(row["Total"])
                                print(floatTotal)
#                                intNum = int(input("How many Number of Gifts? - ")).strip()
                                intNum = int(input("How many Number of Gifts? - "))
                                intNum = int(intNum) + int(row["Num"])
                                print(intNum)
                                dicRow = {"Name":strName,"Total":floatTotal,"Num":intNum}
                                lstTable.append(dicRow)
#                                lstTable.append(dicRow)
                                print("Donor Name | Total Given | Num Gifts | Average Gift\n------------------------------------------------------------------")
                                for row in lstTable:

                                                        #            Total = float(row["Total"])
                                                        #            Num = int(row["Num"])
                                                        #            Ave = (Total/Num)
                                                        #            print(Ave)
                                                        #            print(row["Name"] + '         $' + row["Total"] + row["Num"]  + '  $' + "{:.2f}".format(str(float(row["Total"])/int(row["Num"]))))
                                                        #            print(row["Name"] + '         $' + row["Total"] + row["Num"]  + '  $' + "{:.2f}".format(float(row["Total"])/int(row["Num"])))
                                                        #            print ("{}, ${:.2f}, {:.2f}, ${:.2f}".format(row["Name"], row["Total"], row["Num"], float(row["Total"])/int(row["Num"])))
                                    print ("{}, ${:.2f}, {}, ${:.2f}".format(row["Name"], float(row["Total"]), row["Num"], float(row["Total"])/int(row["Num"])))
                            break #to show the menu

                        else:
                            floatTotal = str(input("What is the Total Given? - ")).strip()
                            intNum = str(input("How many Number of Gifts? - ")).strip()
                            dicRow = {"Name":strName,"Total":floatTotal,"Num":intNum}
                            lstTable.append(dicRow)
                            print("Donor Name | Total Given | Num Gifts | Average Gift\n------------------------------------------------------------------")
        #                while(strName == row["Name"]):
        #                    print("We already have".strName)
        #                else:
        #                    print("We don't have".strName)



        #                for row in lstTable:
        #                    if (strName == row["Name"]):

        #
        #                        break
        #                    else:
        #                strName = str(input("What is Donor Name? - ")).strip()


                        #        for dicRow in lstTable:
                        #            print(dicRow)
                                        #4a Show the current items in the table
                            for row in lstTable:
                        #            Total = float(row["Total"])
                        #            Num = int(row["Num"])
                        #            Ave = (Total/Num)
                        #            print(Ave)
                        #            print(row["Name"] + '         $' + row["Total"] + row["Num"]  + '  $' + "{:.2f}".format(str(float(row["Total"])/int(row["Num"]))))
                        #            print(row["Name"] + '         $' + row["Total"] + row["Num"]  + '  $' + "{:.2f}".format(float(row["Total"])/int(row["Num"])))
                        #            print ("{}, ${:.2f}, {:.2f}, ${:.2f}".format(row["Name"], row["Total"], row["Num"], float(row["Total"])/int(row["Num"])))
                                print ("{}, ${:.2f}, {}, ${:.2f}".format(row["Name"], float(row["Total"]), row["Num"], float(row["Total"])/int(row["Num"])))

                            print()#adding a new line
                        continue #to show the menu





    elif(strChoice == '2'):
        print("Donor Name                | Total Given | Num Gifts | Average Gift\n------------------------------------------------------------------")
        for row in lstTable:
#            print(row["Name"] + '         $' + row["Total"] + '  $' + row["Num"] )
            print ("{}, ${:.2f}, {}, ${:.2f}".format(row["Name"], float(row["Total"]), row["Num"], float(row["Total"])/int(row["Num"])))
            continue #to show the menu

    elif (strChoice == '3'):
        break #and Exit the program
    else:
        print("Please type 1, 2 or 3!")
        sleep(1)
