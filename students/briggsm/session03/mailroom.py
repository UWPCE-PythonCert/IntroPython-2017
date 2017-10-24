'''Mail Program - Week 3
   Matt Briggs'''

menu = ["1. Add donation.",
        "2. Get donor history.",
        "3. Update donation.",
        "4. Delete donor.",
        "5. Thank donor.",
        "6. Print foundation report.",
        "7. Quit."
]

Donors = []
Bill = ["Bill", "Active", 5, 10, 100]
Donors.append(Bill)
Hanna = ["Hanna", "Active", 1000, 50, 150]
Donors.append(Hanna)
Jill = ["Jill", "Active", 4, 100, 700]
Donors.append(Jill)

def create_donation(donor_name, amount):
    '''Take a name and donation, add to the list if present, if not, add to donors'''
    for i in range(len(Donors)):
        if Donors[i][0] == donor_name:
            Donors[i][1] = "Active"
            Donors[i].append(amount)
            print("Donation added. {} gave {}".format(donor_name, amount))
            return 1

    new_donor = [donor_name, "Active", amount]
    Donors.append(new_donor)
    print("New donor added. {} gave {}".format(donor_name, amount))
    return 1

def read_donation(donor_name):
    '''Get the donation history for a person'''
    for i in range(len(Donors)):
        if Donors[i][0] == donor_name and Donors[i][1] == "Active":
            amounts = ""
            count = 0
            total = 0
            for y in range(2, (len((Donors[i])))):
                count += 1
                total += Donors[i][y]
                amounts += " {}) {}".format(count, Donors[i][y])
            print(
                "Summary: {} gave {} donations totaling {}.\nDonations: {}\n".format(donor_name, count, total, amounts))
            return 1

    print("An active donor with that name was not found.")
    return 0

def update_donation(donor_name, donation_index, updated_amount):
    '''Update a particular donation.'''
    for i in range(len(Donors)):
        if Donors[i][0] == donor_name and Donors[i][1] == "Active":
            Donors[i][donation_index] = updated_amount
            print("Donation updated. {} gave {}".format(donor_name, updated_amount))
            return 1

    print("An active donor with that name was not found.")
    return 0

def delete_donor(donor_name):
    '''Delete donor -- make their record inactive.'''
    for i in range(len(Donors)):
        if Donors[i][0] == donor_name and Donors[i][1] == "Active":
            Donors[i][1] = "Inactive"
            print("{} has been removed.".format(donor_name))
            return 1

    print("An active donor with that name was not found.")
    return 0

def read_thankyou(donor_name):
    '''Create a thank you email for a the last donation of the donor.'''
    for i in range(len(Donors)):
        if Donors[i][0] == donor_name and Donors[i][1] == "Active":
            donation_index = len(Donors[i])-1
            thankyou = '''
                Dear {},

                Thank you for your generous donation of $ {0:.2f}. Your
                support enables us to keep doing good in the world. Which means
                your money, earned through whatever means money is earned in
                the amounts you have earned, is now doing good. We thank you. The
                world thanks you.

                Regards,
                Foundation Against Suffering

                '''.format(donor_name, Donors[i][donation_index])
            print (thankyou)
            return 1

    print("An active donor with that name was not found.")
    return 0

def get_report_data():
    '''Get the stats for a person'''
    report = [["Donor Name", "Total Given", "Num Gift", "Average Gift"]]
    for i in range(len(Donors)):
        donor_name = Donors[i][0]
        amounts = ""
        count = 0
        total = 0
        for y in range(2, (len((Donors[i])))):
            count += 1
        total += Donors[i][y]
        amounts += " {}) {}".format(count, Donors[i][y])
        average = total / count
        report.append([donor_name, "$ {0:.2f}".format(total), count, "$ {0:.2f}".format(average)])
    return report

def get_maxlength(reportdata, column):
    '''With a list of lists and a column index, will return the maximum length of a line.'''
    maxlength = 0
    for a in range(len(reportdata)):
        celllength = len(str(reportdata[a][column]))
        if maxlength < celllength:
            maxlength = celllength
    return maxlength

def get_report_format(reportdata):
    '''With a list of lists, assesmbles a table version of the report.'''
    for a in range(len(reportdata)):
        row = ""
        for b in range(len(reportdata[a])):
            colno = len(reportdata[a])-1
            size = len(str(reportdata[a][b]))
            max = get_maxlength(reportdata, b)
            fill = max-size
            filler = " " * fill
            row += "{}{} | ".format(str(reportdata[a][b]), filler)
            if a == 1:
                print(("-" * max) + " | ", end="")
            if a == 1 and b == colno:
                print ("\n")
        print (row)

def read_report():
    '''Print a report for the entire organization history.'''
    reportdata = get_report_data()
    get_report_format(reportdata)
    return 1

def read_raw_report():
    '''Dump the table for testing.'''
    print("Raw report.\n{}".format(Donors))
    return 1

def mainloop():
    '''Central loop of the app.'''
    go = "Yes"
    while(go == "Yes"):
        print ("\n\n-----------\nMailroom\n-----------")
        for m in menu:
            print (m)
        choice = int(input("Chose an option. > "))
        if choice == 1:         # Add donation
            donor_name = input("Type the donor name. > ")
            amount = int(input("Type the amount of the donation. >"))
            create_donation(donor_name, amount)
            go = "Yes"
        elif choice == 2:       # Get donor history.
            donor_name = input("Type the donor name. > ")
            read_donation(donor_name)
            go = "Yes"
        elif choice == 3:         # Update donation
            donor_name = input("Type the donor name. > ")
            read_donation(donor_name)
            donation_rawindex = int(input("Type the index of the amount. > "))
            donation_index = donation_rawindex + 1
            updated_amount = int(input("Type the updated amount. > "))
            update_donation(donor_name, donation_index, updated_amount)
            go = "Yes"
        elif choice == 4:       # Delete donor.
            donor_name = input("Type the donor name. > ")
            delete_donor(donor_name)
            go = "Yes"
        elif choice == 5:         # Thank donor.
            donor_name = input("Type the donor name. > ")
            read_thankyou(donor_name)
            go = "Yes"
        elif choice == 6:       # Print foundation report.
            read_report()
            go = "Yes"
        elif choice == 7:        # Quit.
            print("-----------")
            go = "No"
        elif choice == 8:        # Test -- dump tables
            read_raw_report()
            go = "Yes"

if __name__ == "__main__":
    print ("Starting...")
    mainloop()