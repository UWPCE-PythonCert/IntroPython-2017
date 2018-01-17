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
