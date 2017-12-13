import math
import functools



infile = 'donors.txt'
donor_objects = []


def read_donors():
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




        # donation = list(master_donor[i][1])
        # print(temp_name)
        # temp_name = Donor(name, donation)
        # print(temp_name.name)
        # print(temp_name.donation)
        # master_donor.append(temp_name)






class Donor(object):
    
    # name = ""
    # donations = []
    def __init__ (self, name, donations):
        
        self.name = name
        self.donations = donations

    def add_donation(self, money):

        self.donations.append(money)

    @property
    def total(self):
        return sum(self.donations)

    @property    
    def maxdonation(self):
        return max(self.donations)

        

    @property
    def namelength(self):
        return(len(self.name))

    @property
    def donation_count(self):
        return(len(self.donations))

    @property
    def average_donation(self):
        return(self.total/self.donation_count)






class Storage:


    def __init__(self):
        self.donors = []


    #need methods to add donors, add donation
    # @classmethod
    def add_donor(self, thing):
        self.donors.append(thing)



    def add_donation(self, name, new_donation):
        ind_temp = False

        for i, x in enumerate(self.donors):
            if (x.name).lower() == (name).lower():
                ind_temp = i
                self.donors[i].donations.append(new_donation)
                print(i)
                print("\nA donation of {} has been added to the history of {}".format(float(new_donation),name))
                
        if ind_temp == False:
            bah = []
            bah.append(new_donation)
            temp = Donor(name, bah)
            self.add_donor(temp)
            print(("\n{} has been added as a donor with their generous donation of ${:.2f}.\n"
                "Ain't that just swell?\n").format(name, float(new_donation)))


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
            donation_input()
        elif answer =='3':
            print_report()
        elif answer =='4':
            email_all()
        else:
            print("\nPlease enter a number between 1 and 5")

def list_donors():
    print('\n')
    for x in DB.donors:
        print(x.name)
    print('\n')

def donation_input():
    donor_name = input("Enter a donor's full name \n"
        "> ")
    donor_donation = float(input("Enter a donation amount \n> "))

    DB.add_donation(donor_name, donor_donation)

def print_report():

    DB.donors = sorted(DB.donors, key=lambda x: x.total, reverse=True)
    
    print("\n\n")
    print("{msg1: <20}|{msg2:<13}|{msg3:<14}|{msg4:<12}".format(msg1='Donor Name',
        msg2='Total Donated', msg3='Donation Count', msg4='Average Gift'))

    
    for x in DB.donors:
        print('{:<20}|{:>13.2f}|{:^14}|{:>12.2f}'.format(x.name,x.total,x.donation_count, x.average_donation))
        
        
    print("\n\n")


def email_all():
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

if __name__ == "__main__": 
    DB = Storage()
    # print(DB.donors)
    read_donors()
    # print(DB.donors)
    # print('\n')
    # for i, x in enumerate(DB.donors):
    #     print(i, x.name, x.donations, x.total)

    # DB.donors = sorted(DB.donors, key=lambda x: x.total, reverse=True)
    # print('\n')
    # for i, x in enumerate(DB.donors):
    #     print(i, x.name, x.donations, x.total)


    main_loop()
