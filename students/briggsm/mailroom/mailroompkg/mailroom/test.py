import model as MD
import os
import pprint


fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = fileDir + "\\data\\mailroomdata.json"
utility = MD.Utilities()
donor_records = utility.open_json(filename)



for i, val in enumerate(donor_records.donors):
    try:
        print(val.full_name)
    except:
        print("Error 1")
    try:
        print(val.donation_number)
    except:
        print("Error 2")
    try:
        print(val.average_donations)
    except:
        print("Error 3")
    try:
        print(val.donations_total)
    except:
        print("Error 4")


report = MD.Report()
report.create_report(donor_records)


