#!/usr/bin/env python
# name, donation total, number of donations and average of donations


def main_loop():

    while True:
        answer = str(input("Select from one of these options:\n"
              "(1) Send a Thank You\n"
              "(2) Create a Report\n"
              "(3) quit\n"
              "> "))
        if answer =='3':
            break
        elif answer =='1':
            thank_you()
        elif answer =='2':
            print_report(donor_list)
        else:
            print("\nPlease type 1, 2, or 3")
            

    

def print_report(donors):
    '''need the list of donors sorted before I can print them accurately,
    found the sorted function while looking for a way to do this'''
    donors = sorted(donors, key=lambda x: x[1], reverse=True)

    print("\n\n")
    print("{msg1: <50}|{msg2:<13}|{msg3:<14}|{msg4:<12}".format(msg1='Donor Name',
        msg2='Total Donated', msg3='Donation Count', msg4='Average Gift'))

    for x in donors:
        print('{:<50}|{:>12.2f}|{:^14}|{:>12.2f}'.format(x[0],x[1],x[2],x[1]/x[2]))

    print("\n\n")


def thank_you():
    '''takes in the name or 'list' command'''
    donor_input = input("Enter a donor's full name or type 'list' for all donors \n"
        "> ")
    
    '''if 'list' is chosen than the current list of donor names are printed,
    no order enforced'''
    if str.lower(donor_input) == 'list':
        print('List of donors: \n')
        for row in donor_list:
            print(row[0]+'\n')
   
    elif name_in_list(donor_input) is False:
        '''if the donor is not on the current list, it will be added to the list
    with the donation amount, the number of  donations set to 1 and a
    thank you leter generated. donation converted to float for safety'''
        donor_donation = float(input('Enter donation amount \n> '))
        add_donor(donor_input, donor_donation)
        write_letter(donor_input, donor_donation)

    elif name_in_list(donor_input):
        '''if the donor exists in the list, will fetch the index of that entry
        and add the donation to the donors list and increment the number of donations.
        I wanted to make sure the correctly capitalized name was kept and used
        donation converted to float for safety'''
        proper_name = donor_list[name_in_list(donor_input)][0]
        donor_donation = float(input('Enter donation amout \n> '))
        add_donation(proper_name, donor_donation)
        write_letter(proper_name, donor_donation)

    


def write_letter(name, donor_donation):
    '''writes a brief letter to the donor with their most current donation'''
    print('\nDear {}, \n'
        'Thank you for your generous donation of ${:.2f}.\n'
        'We look forward to your continued support\n'
        '-= The Students =-\n'.format(name, donor_donation))

def name_in_list(name):
    '''searches the list of donors and returns the index for that donor's entry
    or False if does not exist in donor list'''

    for x in donor_list:
        if str.lower(x[0]) == str.lower(name):
            return donor_list.index(x)
    return False   

def add_donor(name, donation):
    '''appends the donor to the list of donors. Only used when they don't exist yet
    could have kept this in the main thank-you function but wanted to clean that up
    as much as I could'''
    donor_list.append([name,donation,1])
    

def add_donation(name, donation):

    '''adds the donation to the matching donor from the existing list, made it
    case insensitive but still needs to be string literal match of name'''

    for x in donor_list:
        if str.lower(x[0]) == str.lower(name):
            x[1] += float(donation)
            x[2] += 1
            

if __name__ == "__main__": 

    '''could use a dictionary here but wanted to play with formatting a list'''

    donor_list = [
    ['William Gates, III', 653784.49, 2],
    # 32682.24
    ['Mark Zuckerberg', 16396.10, 3],
    # 5465.37
    ['Jeff Bezos', 877.33, 1],
    # 877.33
    ['dude',200.00, 2],
    # 100
    ['Paul Allen', 708.42, 3]
    # 236.14
    ]
     
    print('starting...')
    main_loop()

    

    