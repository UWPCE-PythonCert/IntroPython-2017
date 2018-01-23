from mailprog.dataModels import Donor

def list_donors(DB):
    print('\n')
    for x in DB.donors:
        print(x.name)
    print('\n')

def donation_input(DB):
    donor_name = input("Enter a donor's full name \n"
        "> ")
    donor_donation = float(input("Enter a donation amount \n> "))

    DB.add_donation(donor_name, donor_donation)

def print_report(DB):

    DB.donors = sorted(DB.donors, key=lambda x: x.total, reverse=True)
    
    print("\n\n")
    print("{msg1: <20}|{msg2:<13}|{msg3:<14}|{msg4:<12}".format(msg1='Donor Name',
        msg2='Total Donated', msg3='Donation Count', msg4='Average Gift'))

    
    for x in DB.donors:
        print('{:<20}|{:>13.2f}|{:^14}|{:>12.2f}'.format(x.name,x.total,x.donation_count, x.average_donation))
        
        
    print("\n\n")


def email_all(DB):
    '''print to file a customized email for each donor in the dictionary'''
    print('\n')
    for x in DB.donors:
        f = open(x.name+'.txt', 'w')
        f.write('Dear {name:},\n'
            'Thank you for your support. You have donated a total of ${total:.2f}.\n'
            'Thank you,\n'
            '-The Students-\n'.format(name=x.name, total=x.total))
        f.close()
        print('Letter created for {}'.format(x.name))
    print('\n')


def read_donors(infile,DB, donor_objects):
    master_donor = []
    
    with open(infile) as donor_input:
        donor_input = [w for line in open(infile) for w in line.rstrip('\n').split("\n")]
        donor_input.remove("Donor Name - Donations with comma dilimiter")

        for line in donor_input:
            name_string = line.split('-')[0].strip()
            donation_string = line.split('-')[1].strip(" ").strip()
            donation_list = donation_string.split(',')

            donation_list = [float(x) for x in donation_list]


            temp = [name_string, donation_list]
            master_donor.append(temp)
            #donors[name_string.lower()] = [name_string, donation_list]
    
    
    
    # print(master_donor) 

    for i, v in enumerate(master_donor):
        # print(i)
        # print(str(temp_name))
        name = str(master_donor[i][0])
        # print(name)
        donation = master_donor[i][1]
        # print(donation)
        temp_name = Donor(name, donation)
        # print(temp_name.name, temp_name.donation)
        
        donor_objects.append(temp_name)
        DB.add_donor(temp_name)
