#!/usr/bin/env python

donor_names = ["Bill","Fred"]
donations= [[300,555],[240,422]]
donors = list(zip(donor_names,donations))
# donors[0][1].append(600) is Bill's donations plus a new donation
# YOU'D HAVE TO FIND THE INDEX OF BILL
# for donor in enumerate(donors):
#     if donor[0].lower()=="fred":
#          this_donor = donor -> new object pointing to list so if you change it it'll change in data structure
# this_donor[1].append(6000) changes the master list
# make a function to find donor by name and return donor object
# 
def mainloop():
    ''' main interactive loop 
    "send a thank you" "create a report" or "quit"
    '''
    while True:
      answer = int(input("Select from one of these options: \n"
          "(1) Send a Thank You\n"
          "(2) Create a Report\n" 
          "(3) Quit\n>"))
      if answer == 3:
        break
      elif answer == 1:
        thank_you()
      elif answer == 2:
        print_report()
      else:
        print("Please type 1, 2, or 3")

def thank_you():
    print("this is the thank you function")
    while True:
        fullname = input("To send a thank you, "
            "select from one of these options: \n"
            "Enter a donor name (new or existing)\n"
            "Enter all to list existing donors \n"
            "Enter stop to return to main menu \n >")
        ## check for and remove anxillary quotes
        if fullname[0]==fullname[-1]=='"' or fullname[0]==fullname[-1]=="'":
            fullname = fullname[1:-1]
        if fullname == 'stop':
            break
        if fullname.lower() == 'all':
            print("All Donors:")
            [print(x[0]) for x in donors]
        else:
            try: 
                i = [x[0] for x in donors].index(fullname)
                print("Existing Donor")
                amount = float(input("Donation amount: "))
                this_donor = donors[i]
                this_donor[1].append(amount)
                print_letter(this_donor)
            except ValueError:
                print("New Donor")
                amount = float(input("Donation amount: "))
                donors.append((fullname,[amount]))
                this_donor = donors[-1]
                print_letter(this_donor)


def print_report():
    print("this is the print report function")


def print_letter(a_donor):
    fs = "Thank you, {}, for your generous gift of ${}."
    print(fs.format(a_donor[0],a_donor[1][-1]))


if __name__=="__main__":
    print("starting...")
    mainloop()