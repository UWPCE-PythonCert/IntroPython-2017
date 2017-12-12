"""
create data structure for donors
	-dictionary
	-needs to be "searchable" so key.lower() may be best
"""


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


    #  = [name_string, (donation1, donation2)]
    # name_string.lower() = 