class Donor():
    '''The Donor object contains the donor properties for the donor in the mailroom app.'''
    def __init__(self, name="Name me", amount=[]):
        self.Name = "Name me"
        self.Donations = amount


    @property
    def DonationNumber(self):
        '''Contains the number of donations.'''
        return len(self.Donations)


    @property
    def DonationTotal(self):
        '''Contains the total donations.'''
        return sum(self.Donations)


    @property
    def AverageDonations(self):
        '''Contains the average number of donations.'''
        return self.DonationTotal/self.DonationNumber


    def __add__(self, amount=0):
        '''Add a donation.'''
        self.Donations.append(amount)
