#!/usr/bin/env python

''' global variables'''
donor_names = ["Margaret Atwood","Fred Armisen","Heinz the Baron Krauss von Espy"]
donations= [[300,555],[240,422,1000],[1500,2300]]
DONORS = list(zip(donor_names,donations))

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
    ''' Update donor records and print thank you notes.'''
    while True:
        fullname = input("To send a thank you, "
            "select from one of these options: \n"
            "Enter a donor name (new or existing)\n"
            "Enter all to list existing DONORS \n"
            "Enter menu to return to main menu \n >")
        fullname = remove_inputquotes(fullname)
        if fullname == 'menu':
            break
        if fullname.lower() == 'all':
            print("All Donors:")
            [print(x[0]) for x in DONORS]
        else:
            try: 
                i = [x[0] for x in DONORS].index(fullname)
                print("Existing Donor")
                amount = float(input("Donation amount: "))
                this_donor = DONORS[i]
                this_donor[1].append(amount)
                print_letter(this_donor)
            except ValueError:
                print("New Donor")
                amount = float(input("Donation amount: "))
                DONORS.append((fullname,[amount]))
                this_donor = DONORS[-1]
                print_letter(this_donor)


def print_report():
    ''' Pretty-print a table of donor statistics '''
    while True:
        choice = input("To generate a summary report, \n"
            "type run now.\n"
            "To return to the main menu,\n"
            "type menu now>")
        choice = remove_inputquotes(choice)
        if choice == 'menu':
            break
        else:
            [name,total,number,ave]=[[],[],[],[]]
            for x in range(len(DONORS)):
                this_donor = DONORS[x]
                name.append(this_donor[0])
                total.append(round(sum(this_donor[1])))
                number.append(len(this_donor[1]))
                ave.append(round(total[x]/number[x]))
            report_data = list(zip(name,total,number,ave))
            report_data = sorted(report_data,key = lambda y:int(y[1]),reverse = True)
            print_table(report_data)
            



def print_letter(a_donor):
    ''' Generate a formatted thank you note to a donor '''
    fs = "Thank you, {}, for your generosity and recent gift of ${}."
    print(fs.format(a_donor[0],a_donor[1][-1]))

def remove_inputquotes(a_string):
    '''check for and remove anxillary quotes'''
    if a_string[0]==a_string[-1]=='"' or a_string[0]==a_string[-1]=="'":
        a_string = a_string[1:-1]
    return a_string

def print_table(list_data):
    ''' Pretty-print the donor records '''
    headers=('Donor Name','Total Given','Num Gifts','Average Gift')
    fs1 = '|'.join(["{:<40}","{:<12}","{:<10}","{:<12}"])
    width = len(fs1.format(*headers))
    fs2 = ''.join(["{:<40}","${:^12.2f}","{:^12d}","${:^12.2f}"])
    print(fs1.format(*headers))
    print(width*"-")
    for i in range(len(list_data)):
        entry = list_data[i]
        print(fs2.format(*entry))


if __name__=="__main__":
    print("starting...")
    mainloop()