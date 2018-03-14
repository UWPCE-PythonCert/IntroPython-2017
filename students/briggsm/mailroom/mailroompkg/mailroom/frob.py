import os
import json
from prettytable import PrettyTable
import model as MD

def open_json(filename):
        '''Opens a JSON file using the mailroom data schema and returns a list of Donor types with the data.
        @param filename: The relative path from the root directory of the package.
        @type: string
        @return DonorDirectory: The DonorDirectory object populated with data from the JSON file.
        @rtype: DonorDirectory'''
        with open(filename) as f:
            read_data = f.read()
        record = json.loads(read_data)
        donor_directory = MD.DonorDirectory()
        for key, value in record.items():
            donor = MD.Donor()
            donor.id = key
            donor.first_name = value["first_name"]
            donor.last_name = value["last_name"]
            donor.email = value["email"]
            donor.donations = value["donations"]
            donor_directory.donors.append(donor)
        return donor_directory

def create_report(donor_directory):
    '''Create a pretty printed report to the console.
    @param donor_directory: The donor directory with donars.
    @type: DonorDirectory'''
    t = PrettyTable(["Donor","No.","Average","Total"])
    for record in donor_directory.donors:
        t.add_row([record.full_name, record.donation_number, record.average_donations, record.donations_total])
    print(t)


    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint("\nREPORT\nDonor\t\tNo\tAverage\tTotal\n")
    # for record in donor_directory.donors:
    #     pp.pprint("{}\t\t{}\t{}\t{}".format(
    #         record.full_name, record.donation_number, record.average_donations, record.donations_total))
    # pp.pprint("\n")

fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = fileDir + "\\mailroompkg\\mailroom\\data\\mailroomdata.json"
donor_directory = open_json(filename)
create_report(donor_directory)