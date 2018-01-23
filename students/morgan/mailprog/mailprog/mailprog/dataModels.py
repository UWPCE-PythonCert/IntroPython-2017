import csv
import copy









class Donor(object):

    def __init__(self, name , donations= None):
        self.name = name
        self.donations = donations
        self.i = 0

    def add_donation(self, money):
        self.donations.append(money)

    def __iter__(self):
        for item in self.donations:
            yield item

    def __next__(self):
        if self.i < len(self.donations):
            self.i += 1
            return self.donations[self.i]

    @property
    def total(self):
        return sum(self.donations)

    @property
    def maxdonation(self):
        return max(self.donations)

    @property
    def namelength(self):
        return (len(self.name))

    @property
    def donation_count(self):
        return (len(self.donations))

    @property
    def average_donation(self):
        return (self.total / self.donation_count)


class Storage:
    def __init__(self, donors = []):
        self.donors = donors
        self.user = ""



    def __iter__(self):
        return self.donors

    def list_donors(self):
        temp = []
        for x in self.donors:
            temp.append(x.name)
        return temp

    def record_user(func):
        print('record user is being called')

        def func_wrapper(self, *args, **kwargs):

            print('func wrapper called')
            if self.user == "":
                self.user = input("Please enter username. \n>")
            return func(self, *args, **kwargs)

        return func_wrapper

    @record_user
    def donation_input(self, donor_name, donor_donation = 0):
        # temp = self.record_user(self.add_donation(donor_name, donor_donation))
        self.add_donation(donor_name, donor_donation)
        print('donation input call', donor_name)
        print(self.user, 'log')

    def print_report(self):
        self.donors = sorted(self.donors, key=lambda x: x.total, reverse=True)
        print("\n\n")
        print("{msg1: <20}|{msg2:<13}|{msg3:<14}|{msg4:<12}".format(msg1='Donor Name', msg2='Total Donated',
                                                                    msg3='Donation Count', msg4='Average Gift'))
        for x in self.donors:
            print('{:<20}|{:>13.2f}|{:^14}|{:>12.2f}'.format(x.name, x.total, x.donation_count, x.average_donation))
        print("\n\n")

    def read_donors(self, infile, donor_objects):
        master_donor = []
        donor_input = []

        with open(infile) as don_list:
            reader = csv.reader(don_list, delimiter=',', quotechar='"')
            for x in reader:
                donor_input.append(x)

            for x in donor_input:
                if x[0].startswith("Donor Name"):
                    donor_input.remove(x)

            for line in donor_input:
                name_string = line[0]
                donation_string = line[1:]
                for x in donation_string:
                    x.strip(' ')
                donation_list = [float(x) for x in donation_string]
                temp = [name_string, donation_list]
                master_donor.append(temp)
                # donors[name_string.lower()] = [name_string, donation_list]

        for i, v in enumerate(master_donor):
            name = str(master_donor[i][0])
            donation = master_donor[i][1]
            temp_name = Donor(name, donation)
            donor_objects.append(temp_name)
            self.add_donor(temp_name)

    def email_all(self):
        '''print to file a customized email for each donor in the dictionary'''
        print('\n')
        for x in self.donors:
            f = open(x.name + '.txt', 'w')
            f.write('Dear {name:},\n'
                    'Thank you for your support. You have donated a total of ${total:.2f}.\n'
                    'Thank you,\n'
                    '-The Students-\n'.format(name=x.name, total=x.total))
            f.close()
            print('Letter created for {}'.format(x.name))
        print('\n')

    def add_donor(self, thing):
        self.donors.append(thing)


    # @record_user
    def add_donation(self, new_name, new_donation):
        ind_temp = False
        for i, x in enumerate(self.donors):
            if (x.name).lower() == (new_name).lower():
                ind_temp = i
                self.donors[i].donations.append(new_donation)
                print(i)
                print("\nA donation of {} has been added to the history of {}".format(float(new_donation), new_name))
        if ind_temp == False:
            bah = []
            bah.append(new_donation)
            temp = Donor(new_name, bah)
            self.add_donor(temp)
            print(("\n{} has been added as a donor with their generous donation of ${:.2f}.\n"
                   "Ain't that just swell?\n").format(new_name, float(new_donation)))

    @property
    def total_donations(self):
        total = 0
        for x in self.donors:
            total += x.total
        return total

    def challenge(self, factor, min_val = None, max_val = float('inf')):
        '''[name,[item1,item2]]'''
        if min_val is not float:
            min_val = 0
        if max_val is not float:
            max_val = float('inf')
        temp = copy.deepcopy(self.donors)
        # print(temp)

        for x in temp:
            x.donations = list(filter(lambda y: (min_val <= y <= max_val), x.donations))
            x.donations = list(map(lambda y:  y * factor, x.donations))
            # print(x)
        return Storage(temp)

