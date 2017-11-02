#!/usr/bin/env python
# name, donation total, number of donations and average of donations

infile = 'donors.txt'

donors = {}

with open(infile) as donor_input:
    donor_input.readline()
    for line in donor_input:
        # line = line.strip()
        name_string = line.split('-')[0].strip()
        donation_string = line.split('-')[1].strip(' ').strip()
        donation_list = donation_string.split(',')
        
        donation_list = [float(x) for x in donation_list]

        # print(donation_list[0])
        

        # print(name_string.strip())
        # print(donation_list)
        # donors.setdefault(name_string,[]).append(donation_list)
        donors[name_string] = donation_list



def main_loop():

    while True:
        answer = str(input("Select from one of these options:\n"
              "(1) Send a Thank You\n"
              "(2) Create a Report\n"
              "(3) Send Letters To Everyone\n"
              "(4) quit\n"
              "> "))
        if answer =='4':
            break
        elif answer =='1':
            thank_you()
        elif answer =='2':
            print_report(donors)
        elif answer =='3':
            email_all(donors)
        else:
            print("\nPlease type 1, 2, or 3")

def email_all(donors):
    '''print to file an email for each donor in the dictionary'''
    print('\n')
    for x in donors:
        f = open(x+'.txt', 'w')
        f.write('Dear {name:},\n'
            'Thank you for your support. You have donated a total of ${total:.2f}.\n'
            'Thank you,\n'
            '-The Students-\n'.format(name=x, total=sum(donors[x])))
        f.close()
        print('Letter created for {}'.format(x))
    print('\n')

def print_report(donors):
        
    '''convert dictionary to list'''
    sort = list(donors.items())
    '''sort new list by sum of all donations'''    
    sort = sorted(sort, key=lambda x: sum(x[1]), reverse=True)
    print(sort)
    
    print("\n\n")
    print("{msg1: <20}|{msg2:<13}|{msg3:<14}|{msg4:<12}".format(msg1='Donor Name',
        msg2='Total Donated', msg3='Donation Count', msg4='Average Gift'))

    
    for x in sort:
        print('{:<20}|{:>13.2f}|{:^14}|{:>12.2f}'.format(x[0],sum(x[1][:]),len(x[1]),sum(x[1][:])/len(x[1])))
        
        
    print("\n\n")


def thank_you():
    '''takes in the name or 'list' command'''
    donor_input = input("Enter a donor's full name or type 'list' for all donors \n"
        "> ")
    
    '''if 'list' is chosen than the current list of donor names are printed,
    no order enforced'''
    if str.lower(donor_input) == 'list':
        print('\nList of donors: \n')
        for x in donors:
            print(x)
        print('\n')

    else: 

        donor_donation = float(input("Enter a donation amount \n > "))
        '''if the donor exists in the list, will fetch the index of that entry
        and add the donation to the donors list and increment the number of donations.
        I wanted to make sure the correctly capitalized name was kept and used
        donation converted to float for safety'''
        add_donation(donor_input, donor_donation)
        write_letter(donor_input, donor_donation)


def add_donation(name, donation):
    donors.setdefault(name,[]).append(donation)


def write_letter(name, donation):
    '''writes a brief letter to the donor with their most current donation'''
    print('\nDear {}, \n'
        'Thank you for your generous donation of ${:.2f}.\n'
        'We look forward to your continued support\n'
        '-= The Students =-\n'.format(name, donation))



if __name__ == "__main__": 
    print('starting...')
    main_loop()