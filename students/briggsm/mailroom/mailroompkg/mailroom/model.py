'''
The object model for the mailroom application.
'''
import uuid
import json
from prettytable import PrettyTable

class Person():
    '''A person in the context of the application.'''

    def __init__(self):
        '''Creates a Person object.
        @param first_name: The first name of the person.
        @type first_name: string
        @param last_name: The last name of the person.
        @type first_name: string
        @param email: The email of the person, for example, matt@mattbriggs.com
        @type email: string'''
        self.id = str(uuid.uuid4())
        self.first_name = ""
        self.last_name = ""
        self.email = ""

    @property
    def full_name(self):
        '''Contains the full name of the person.
        @return: fullname
        @rtype: string'''
        return self.first_name + " " + self.last_name


class Donor(Person):
    '''A person who gives money. A subtype of Person.'''
    def __init__(self, donations=[]):
        '''Creates a Donor, a Person of type donor.
        @param donations: A list of Donor objects.
        @type donations: list'''
        self.id = str(uuid.uuid4())
        self.donations = donations

    @property
    def donation_number(self):
        '''Contains the number of donations.
        @return donation_number: Returns the number of donations.
        @retype: int'''
        return int(len(self.donations))

    @property
    def donations_total(self):
        '''Contains the total donations.
        @return donation_total: The total number of donations.
        @retype: float'''
        return sum(self.donations)

    @property
    def average_donations(self):
        '''Contains the average number of donations.
        @return average_donations: The average number of donations
        @rtype: float'''
        if self.donation_number > 0:
            return float(self.donations_total/self.donation_number)
        else:
            return 0


class DonorDirectory():
    '''The list of donars.'''
    def __init__(self, donors=[]):
        '''Create a donor directory.'
        @param donors: A list of donors.
        @param type: list'''
        self.donors = donors
        
    def set_donors(self, donors):
        '''With a list containing donors, create the list of Donors.
        @param donors: A list of donors.
        @param type: list'''
        self.donors = donors

    def add_donor(self, donor):
        '''Add a Donor to the list of Donors.
        @param donor: A Donor object.
        @param type: Donor'''
        self.donors.append(donor)

    @property
    def total_donors(self):
        '''Contains the number of donors.
        @return: The number of donors.
        @rtype: int'''
        return int(len(self.donors)+1)

    @property
    def donations_total(self):
        '''Contains the total dollar figure of donations.
        @return donations_total: The total dollar figure of donations
        @rtype: int'''
        total = 0
        for i, val in enumerate(self.donors):
            total = total + val.donation_total
        return int(total)

    @property
    def average_donations(self):
        '''Contains the total average figure of donations.
        @return average_donations: total average figure of donations
        @rtype: float'''
        total = 0
        for i, val in enumerate(self.donors):
            total = total + val.donation_total
        return float(total/len(self.donors)+1)


class Letter():
    '''The thank you letter sent to a donor from the person for a donation.'''
    def __init__(self):
        '''Initialized with the text attribute.'''
        self.text = ""

    def create_letter(self, addressed_to, email_to, written_by, amount):
        '''The thank you letter sent to a donor from the person for a donation.
        @param addressed_to: The full name of the donor.
        @type: string
        @param  email_to: The email address of the donor.
        @type: string
        @param written_by: The name of the person writing the letter.
        @type: string
        @param amount: The amount of the donation.
        @type: float
        @return text: The complete text of the letter.
        @rtype: string'''
        text = '''
    Dear {} at {},

    Thank you for your generous donation of $ {}. Your
    support enables us to keep doing good in the world. Which means
    your money, earned through whatever means money is earned in
    the amounts you have earned, is now doing good. We thank you. The
    world thanks you.

    Regards,
    {}
    Foundation Against Suffering

    '''.format(addressed_to, email_to, amount, written_by)
        self.text = text
        return text


class Report():
    '''The report on the current state of donars and donations.'''
    def __init__(self):
        '''Set up the report data structures.
        @param PreparedReport: The text of the final report.
        @type: string
        @param Report: The report as a list of lists 
        @type: list''' 
    
    def create_report(self, donor_directory):
        '''Create a pretty printed report to the console.
        @param donor_directory: The donor directory with donars.
        @type: DonorDirectory'''
        '''Create a pretty printed report to the console.
        @param donor_directory: The donor directory with donars.
        @type: DonorDirectory'''
        t = PrettyTable(["Donor","No.","Average","Total"])
        for record in donor_directory.donors:
            t.add_row([record.full_name, record.donation_number, record.average_donations, record.donations_total])
        print(t)

class UI():
    '''The command line user interface that handles interactions between the 
    person and the donor.'''
    def __init__(self):
        '''Set up the UI.
        @param app_name: The name of the command-line interface.
        @type: string
        @param menu: The menu choices for the command-line interface.
        @type: dict
        @param active_user: The name of the current active user.
        @type: string
        @param interface: The text for the command-line interface banner.
        @type: string''' 
        self.app_name = "Base App"
        self.menu = {}
        self.active_user = "No one signed in."
        self.interface = ""
    def display_menu(self):
        pass


class Utilities():
    '''An object for handling tasks in the app.'''
    def open_json(self, filename):
            '''Opens a JSON file using the mailroom data schema and returns a 
            list of Donor types with the data.
            @param filename: The relative path from the root directory of the
            package.
            @type: string
            @return DonorDirectory: The DonorDirectory object populated with 
            data from the JSON file.
            @rtype: DonorDirectory'''
            with open(filename) as f:
                read_data = f.read()
            record = json.loads(read_data)
            donor_directory = DonorDirectory()
            for key, value in record.items():
                donor = Donor()
                donor.id = key
                donor.first_name = value["first_name"]
                donor.last_name = value["last_name"]
                donor.email = value["email"]
                donor.donations = list(value["donations"])
                donor_directory.donors.append(donor)
            return donor_directory


    def save_json(self, donor_directory, filename):
            '''Takes the Donor Directory list of Donor types and saves a JSON 
            file using the mailroom data schema.
            @param donor_directory: The DonorDirectory object populated with 
            data from the JSON file.
            @type: DonorDirectory
            @param filename: The relative path from the root directory of the 
            package.
            @type: string'''
            outdata = "{"
            for record in donor_directory.donors:
                rec_string = '"{}" : {{"first_name": "{}", "last_name": "{}", "email": "{}", "donations": {}}},'.format(record.id, record.first_name, record.last_name, record.email, record.donations)
                outdata += rec_string
            outdata = outdata[:-1] + "}"
            fout = open(filename, "w")
            for line in outdata:
                fout.write(line)
            fout.close()
            
    def spill_records(self, donor_records):
        '''Takes a DonorDirectory object and writes the contents to the console.
        @param donor_records: DonorDirectory object with a list of donors.
        @type: DonorDirectory'''
        print("Here is your data.")
        for record in donor_records.donors:
            print('''
id: {}
first_name: {}
last_name: {}
email: {}
donations: {}
----------
'''.format(record.id, record.first_name, record.last_name, record.email, record.donations))
