from mailprog.functions import list_donors, donation_input, print_report, email_all



infile = "mailprog/data/donors.txt"
donor_objects = []

def main_loop(DB):
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
            list_donors(DB) 
        elif answer == '2':
            donation_input(DB)
        elif answer =='3':
            print_report(DB)
        elif answer =='4':
            email_all(DB)
        else:
            print("\nPlease enter a number between 1 and 5")



