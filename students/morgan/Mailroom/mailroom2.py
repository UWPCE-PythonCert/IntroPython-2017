#!/usr/bin/env python
# name, donation total, number of donations and average of donations

infile = 'donors.txt'

donors = {}


def read_donors():
    with open(infile) as donor_input:
        '''imports donors from file and creates a dictionary with 'name':[donations]'''
        # donor_input.readline()
        # header_check = [w for line in open(infile) for w in line.split("\n")]
        # assert header_check[0] == "Donor Name - Donations with comma dilimiter"
        # print(header_check)

        donor_input = [w for line in open(infile) for w in line.rstrip('\n').split("\n")]
        donor_input.remove("Donor Name - Donations with comma dilimiter")

        # assert "Donor Name - Donations with comma dilimiter\n" in donor_input
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
            donors[name_string.lower()] = [name_string, donation_list]
    return donors



def main_loop():
    '''main question tree of what action to perform'''

    while True:
        answer = str(input("Select from one of these options:\n"
              "(1) List Donors\n"
              "(2) Add Donation\n"
              "(3) Create a Report\n"
              "(4) Send Letters To Everyone\n"
              "(5) quit\n"
              "> "))
        if answer =='5':
            break
        elif answer =='1':
            list_donors() 
        elif answer == '2':
            thank_you()
        elif answer =='3':
            print_report(donors)
        elif answer =='4':
            email_all(donors)
        else:
            print("\nPlease enter a number between 1 and 5")

def list_donors():
    print('\nList of donors: \n')
    for k,v in donors.items():
        print(v[0])
        # print(v[1])
        # print(sum(v[1]))
    print('\n')


def email_all(donors):
    '''print to file a customized email for each donor in the dictionary'''
    print('\n')
    for k,v in donors.items():
        f = open(v[0]+'.txt', 'w')
        f.write('Dear {name:},\n'
            'Thank you for your support. You have donated a total of ${total:.2f}.\n'
            'Thank you,\n'
            '-The Students-\n'.format(name=v[0], total=sum(v[1])))
        f.close()
        print('Letter created for {}'.format(v[0]))
    print('\n')

def print_report(donors):
    '''prints a list of the donors by descending total donated'''

    '''convert dictionary to list'''
    sort = list(donors.items())
    # print(sort)
    '''sort new list by sum of all donations'''    
    sort = sorted(sort, key=lambda x: sum(x[1][1]), reverse=True)
    # print(sort)
    
    print("\n\n")
    print("{msg1: <20}|{msg2:<13}|{msg3:<14}|{msg4:<12}".format(msg1='Donor Name',
        msg2='Total Donated', msg3='Donation Count', msg4='Average Gift'))

    
    for x in sort:
        # print (x)
        # print(sum(x[1][1]), len(x[1][1]))
        print('{:<20}|{:>13.2f}|{:^14}|{:>12.2f}'.format(x[1][0],sum(x[1][1]),len(x[1][1]),sum(x[1][1])/len(x[1][1])))
        
        
    print("\n\n")



def thank_you():
    '''receives input to 1) provide list of donors OR 2) add/update donor and donation'''
    donor_input = input("Enter a donor's full name \n"
        "> ")
    
    '''if 'list' is chosen than the current list of donor names are printed,
    no order enforced'''
    # if str.lower(donor_input) == 'list':
    #     print('\nList of donors: \n')
    #     for x in donors:
    #         print(x)
    #     print('\n')

    # else: 

    donor_donation = float(input("Enter a donation amount \n > "))
    '''if the donor exists in the list, will fetch the index of that entry
    and add the donation to the donors list and increment the number of donations.
    I wanted to make sure the correctly capitalized name was kept and used
    donation converted to float for safety'''
    add_donation(donor_input, donor_donation)
    write_letter(donor_input, donor_donation)


def add_donation(name, donation):

    donors.setdefault(name.lower(),[name,[]])
    # print(donors)
    donors[name.lower()][1].append(donation)


def write_letter(name, donation):
    '''print letter for name and donation as provided'''
    print('\nDear {}, \n'
        'Thank you for your generous donation of ${:.2f}.\n'
        'We look forward to your continued support\n'
        '-= The Students =-\n'.format(name, donation))



if __name__ == "__main__": 
    read_donors()
    print('starting...')
    main_loop()
