#!/usr/bin/env python3

#Donors
#Data structure using a dictionary
DonorDict = {"Michael Jordan" : [2321.42, 18.17],
"Charles Homon" : [8776.33],
"George Newton": [6233.23, 4.87, 1.0],
"Julia Chen" : [1663.23, 4300.87, 10432.0],
"Alphos Yem" : [24.43, 42.6]}


def mainloop():
    """Send a Thank, Create a Report, or quit"""
    main_menu = {1: send_thank_you, 2: create_report, 3: send_letters, 4: quit}
    while True:
        try:
            action = int(input("Please choose an action: \n(1) Send a Thank You,\n(2) Create a Report,\n(3) Send Letters to Everyone,\n(4) Quit \n> " ))
        except ValueError:
            print('Please input a valid number!')
        #try:
        main_menu.get(action)()
        #except (TypeError, UnboundLocalError):
        #    pass


def quit():
    """Quit the program"""
    print("You have quit the program!")
    exit(0)


def addDonor(Donor):
    """Add a new Donor to the data structure with an empty donation history"""
    print(Donor + " is a new donor! We have added him to the Donor list")
    DonorDict[Donor] = []
    DonorDict[Donor].append(donate(Donor))


def donate(Donor):
    """Add a donation to the donation history"""
    try:
        donation = float(input("How much did " + Donor + " Donate? \n> "))
    except (ValueError):
        print("Please input a valid number!")
    print("the donation has been added to the history")
    return donation


def letter(Donor):
    """Print an email for the donor selected and their most recent donation"""
    total  = sum(DonorDict[Donor])
    Letter = """Dear {:s},\n
           Thank you for your most recent donation of {:.2f} dollars.\n
    Please continue to support us in our endeavours in the future!\n
    Your total donation to date is {:.2f}\n
    With all the best, \n
           The Team
    """.format(Donor, DonorDict[Donor][-1], total)
    return Letter


def send_thank_you():
    """Send a thank you to the donors"""
    print("You have selected to send a Thank You!\n")
    try:
        Donor = input("What is the donor's full name? \n> ")
    except TypeError:
        print("Please input a valid name!")
    if Donor.lower() == 'list':
        print(sorted(DonorDict.keys()))
    elif Donor in DonorDict:
        print("You have selected " + Donor)
        DonorDict[Donor].append(donate(Donor))
        print(letter(Donor))
    else:
        addDonor(Donor)


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
    for name, history in DonorDict.items():
        print(formatData(name, history))


def send_letters():
    """Send letters to the donors, either to file or print to screen"""
    try:
        action = int(input("Would you like to: (1) Write to a file? or (2) Print to screen? \n> "))
    except ValueError:
        print('Please input a valid number!')
    if action == 1:
        filelist = get_text_file_name()
        for outfile, name in zip(filelist, sorted(DonorDict)):
            with open(outfile, 'w') as f:
                f.write(letter(name))
    elif action == 2:
        for name in DonorDict:
            print(letter(name))

def get_text_file_name():
    """Format the DonorDict for printing to an outfile"""
    return [name.replace(' ', '_') + '.txt' for name in sorted(DonorDict)]

if __name__ == "__main__":
    mainloop()
