#!/usr/bin/env python3

#Donors
#Data structure using a dictionary
#DonorDict = {"Michael Jordan" : [2321.42, 18.17],
#"Charles Homon" : [8776.33],
#"George Newton": [6233.23, 4.87, 1.0],
#"Julia Chen" : [1663.23, 4300.87, 10432.0]}
#"Alphos Yem" : [24.43, 42.6],

#data structure
donors = [("Michael Jordan", [2321.42, 18.17]),
          ("Charles Homon", [8776.33]),
          ("George Newton", [6233.23, 4.87, 1.0]),
          ("Julia Chen", [1663.23, 4300.87, 1044432.0]),
          ("Alphos Yem", [24.43, 42.6])
          ]



def mainloop():
    """Send a Thank, Create a Report, or quit"""
    while True:
        action = int(input("Please choose an action: \n(1) Send a Thank You, \n(2) Create a Report, \n(3) quit \n> " ))
        if action == 3:
            break
        elif action == 2:
            create_report()
        elif action == 1:
            send_thank_you(input("What is the donor's full name? \n> "))
        else:
            print("Please select a valid option 1, 2, 3!")

def addDonor(name):
    """Add a new Donor to the data structure with an empty donation history"""
    print(name + " is a new donor! We have added him to the Donor list")
    donors.append((name, []))
    #DonorDict[name] =

def donate(Donor):
    """Add a donation to the donation history"""
    donation = float(input("How much did " + Donor + " Donate? \n> "))
    for i in range(len(donors)):
        if Donor.lower() == donors[i][0].lower():
            donors[i][1].append(donation)
            print(donors[i][1])
    print("the donation has been added to the history")
    return donation

def sendEmail(Donor, donation):
    """Print an email for the donor selected and their most recent donation"""
    print(
        """Dear {:s},\n
           Thank you for your most recent donation of {:.2f} dollars.\n
    Please continue to support us in our endeavours in the future!\n
    With all the best, \n
           Fruit for the Poor
    """.format(Donor, donation))

def get_donor_name(data):
    """Create a set of just the donor names"""
    list = []
    for i in range(len(donors)):
        list += [donors[i][0]]
    return list

def send_thank_you(Donor):
    """Send a thank you to the donors"""
    if Donor.lower() == "list":
        for i in range(len(donors)):
            print(donors[i][0])
        #print(sorted(DonorDict.keys())
        Donor = input("What is the donor's full name? \n> ")
    if Donor in get_donor_name(donors):
        print("You have selected " + Donor)
        donation = donate(Donor)
        sendEmail(Donor, donation)
    else:
        addDonor(Donor)
        donation = donate(Donor)
        sendEmail(Donor, donation)

def topline():
    """Print the top two lines of the table"""
    print('{: <23s} | {:s} | {:s} | {:s}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-' * 66)

def formatData(name, history):
    """Format the data for the table"""
    total = sum(history)
    numGifts = len(history)
    Ave = float(total / numGifts)
    return '{: <23s} ${: >13.2f} {: >11d} ${: >13.2f}'.format(name, total, numGifts, Ave)

def create_report():
    """Create a report for the donors"""
    topline()
    for i in range(len(donors)):
        print(formatData(donors[i][0], donors[i][1]))



if __name__ == "__main__":
    mainloop()
