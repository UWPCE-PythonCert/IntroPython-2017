


infile = "mailprog/data/donors.txt"


def main_loop(DB):
    '''main question tree of what action to perform'''

    while True:
        answer = str(input("Select from one of these options:\n"
              "(1) List Donors\n"
              "(2) Add Donation\n"
              "(3) Create a Report\n"
              "(4) Send Letters To Everyone\n"
              "(5) quit\n"
              "(6) for multiplier funciton\n"
              "> "))
        if answer == '5':
            break
        elif answer == '1':
            temp = DB.list_donors()
            print('\n')
            for x in temp:
                print(x)
            print('\n')
        elif answer == '2':
            donor_name = input("Enter a donor's full name \n"
                           "> ")
            donor_donation = float(input("Enter a donation amount \n> "))

            DB.donation_input(donor_name, donor_donation)

            # temp = record_user(DB.add_donation(donor_name, donor_donation))

        elif answer == '3':
            DB.print_report()
        elif answer == '4':
            DB.email_all()
        elif answer == '6':
            factor = float(input("What is the multiplier? \n>"))
            min_don = input("What is the minimum donation amount? Blank for $0. \n>")
            max_don = input("What is the maximum donation amount? Blank for None. \n>")
            new_db = (DB.challenge(factor, min_don, max_don))
            # print(new_db)
            print("Donations after being multiplied")
            for x in new_db.donors:
                print(x.name, x.donations, '{:.2f} new'.format(x.total))

            # for x in new_db:
            #     print(x.donations, 'new')
            print("\n Original donation amounts")
            for x in DB.donors:
                print(x.name, x.donations, "{:.2f} old".format(x.total))
            # new_db.print_report()
            print("\n")

        else:
            print("\nPlease enter a number between 1 and 6")






