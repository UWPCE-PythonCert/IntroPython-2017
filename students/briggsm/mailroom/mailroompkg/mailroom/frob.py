import os
import json
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

def save_json(filename, OutDirectory):
        '''Takes the Donar Directory list of Donor types and saves a JSON file using the mailroom data schema.
        @param filename: The relative path from the root directory of the package.
        @type: string
        @param OutDirectory: The DonorDirectory object populated with data from the JSON file.
        @type: DonorDirectory'''
        outdata = "{"
        for record in OutDirectory.donors:
            rec_string = '"{}" : {{"first_name": "{}", "last_name": "{}", "email": "{}", "donations": "{}"}},'.format(record.id, record.first_name, record.last_name, record.email, record.donations)
            outdata += rec_string
        outdata = outdata[:-1] + "}"
        fout = open(filename, "w")
        for line in outdata:
            fout.write(line)
        fout.close()


fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = fileDir + "\\data\\mailroomdata.json"
donor_directory = open_json(filename)
print(donor_directory)
save_json(filename, donor_directory)