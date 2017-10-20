#!/usr/bin/env python

donor_names = ["Bill","Fred"]
donations= [[300,555],[240,422,1000]]
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
    while True:
        fullname = input("To send a thank you, "
            "select from one of these options: \n"
            "Enter a donor name (new or existing)\n"
            "Enter all to list existing donors \n"
            "Enter stop to return to main menu \n >")
        ## check for and remove anxillary quotes
        fullname = remove_inputquotes(fullname)
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
    while True:
        choice = input("To generate a summary report, \n"
            "type go now. To return to the main menu,\n"
            "type stop now>")
        choice = remove_inputquotes(choice)
        if choice == 'stop':
            break
        else:
            [name,total,number,ave]=[[],[],[],[]]
            for x in range(len(donors)):
                this_donor = donors[x]
                name.append(this_donor[0])
                total.append(sum(this_donor[1]))
                number.append(len(this_donor[1]))
                ave.append(round(total[x]/number[x]))
            report_data = list(zip(name,total,number,ave))
            report_data = sorted(report_data,key = lambda y:int(y[2]),reverse = True)
            print_table(report_data)
            






def print_letter(a_donor):
    fs = "Thank you, {}, for your generous gift of ${}."
    print(fs.format(a_donor[0],a_donor[1][-1]))

def remove_inputquotes(a_string):
    if a_string[0]==a_string[-1]=='"' or a_string[0]==a_string[-1]=="'":
        a_string = a_string[1:-1]
    return a_string

def print_table(list_data):
    headers=('Donor Name','Total Given','Num Gifts','Average Gift')
    num_headers = len(headers)
    fs1 = ' | '.join(num_headers*["{}"])
    width = len(fs1.format(*headers))
    fs2 = '    '.join(["{:8}","$      {:4d}","      {:2d}","$      {:4d}"])
    print(fs1.format(*headers))
    print(width*"-")
    for i in range(len(list_data)):
        entry = list_data[i]
        print(fs2.format(*entry))


if __name__=="__main__":
    print("starting...")
    mainloop()