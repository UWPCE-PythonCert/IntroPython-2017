# classessheet.py
""" This is a script to mess with classes.
    The idea is to use this practice to create class "persons" for mail room """


class Donor:
    # This is an experimental class for donors in mailroom
    numdonors = 0
    rosterraw = []

    def __init__(self, name):

        self.first_name, self.last_name = list(name.split())
        self.donations = [1, 2, 3, 4, 5, 6, 7]
        self.fullname = str(self.first_name + ' ' + self.last_name)
        self.averagedon = sum(self.donations) / len(self.donations)
        self.maxdon = max(self.donations)
        Donor.numdonors += 1
        Donor.rosterraw.append(id(self))

    def updatecalcs(self):
        # Updates the average donation attribute after mods have been made to donations
        self.averagedon = sum(self.donations) / len(self.donations)
        self.maxdon = max(self.donations)

    def lastfirst(self):
        # creates a last name , first name string
        lastfirstname = '{}, {}'.format(self.last_name, self.first_name)
        return lastfirstname

    def appenddonations(self, newdon):
        ''' Adds a donation to the donations list
            Updates the average donations
            Updates the max donation '''
        self.donations.append(newdon)
        self.updatecalcs()

donor=[None, None]
donor[Donor.numdonors] = Donor('Dan Kuchan')
donor[Donor.numdonors]= Donor('Abbey Kuchan')
donor[Donor.numdonors]= Donor("Blabedy Blah")
print(donor[1].lastfirst())
print(donor[1].donations[::])
print(donor[1].averagedon)
donor1.appenddonations(1500)
print(donor[1].donations[::])
print(donor[1].averagedon)
print(donor[1].maxdon)
print(Donor.numdonors)
print(Donor.rosterraw)

