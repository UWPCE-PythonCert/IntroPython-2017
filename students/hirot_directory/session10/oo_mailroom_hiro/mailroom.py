#!/usr/bin/env python3

import sys


def request_donation():
    donor_name = str(input("Full Name: "))
    new_donation = int(input("How much do you want to donate?: "))
    if (new_donation > 0):
        print("Thank you for donation, Mr./Ms. {}! Your donation amount is USD ${}.".format(donor_name, new_donation))
    return Donor(donor_name, new_donation)


def select_submenu():
    choice = int(input("Select from one of these options:\n"
                       "(1) Show a list\n"
                       "(2) Enter a donation\n"
                       "(3) Exit\n"))
    return choice


def select_mainmenu():
    answer = int(input("Select from one of these options:\n"
                       "(1) Send a Thank you\n"
                       "(2) Create a Report\n"
                       "(3) Send letters to everyone\n"
                       "(4) quit\n"))
    return answer


def select_quit():
    selection = (input("Are you sure to quit? (Y or N) To return to main menu, please select 'N'.: ")).upper()
    return selection


def mainloop():
    while True:
        try:
            answer = select_mainmenu()
            dict_answer[answer]()

        except ValueError as e:
            print("Error happened. Error is ", type(e), "Please type 1, 2 or 3")
        except KeyError as k:
            print("Error happened. Error is ", type(k), "Please type 1, 2 or 3")


def thank_you_loop():
    while True:
        try:
            choice = select_submenu()
            dict_choice[choice]()

        except ValueError as e:
            print("Error happened. Error is ", type(e) , "Please type 1, 2 or 3")
        except KeyError as k:
            print("Error happened. Error is ", type(k) , "Please type 1, 2 or 3")


def quit():
    print("quit function is called")

    try:
        selection = select_quit()
        if (selection == 'Y'):
            print("Good bye...")
            sys.exit()
        else:
            return mainloop()

    except ValueError as e:
        print("Error happened. Error is ", type(e), "Please type 1, 2 or 3")
    except KeyError as k:
        print("Error happened. Error is ", type(k), "Please type 1, 2 or 3")


def make_sample_db():

    donor_names = ["William Gates III", "Mark Zuckerberg", "Jeff Bezos", "Paul Allen"]
    donations = [[200, 500], [2000, 3000], [4000, 5000], [100, 150]]

    sample_db = {}

    for name, donation in zip(donor_names, donations):
        sample_db[name] = donation

    return sample_db

    # return [Donor("William Gates III", [653772.32, 12.17]),
    #         Donor("Jeff Bezos", [877.33]),
    #         Donor("Paul Allen", [663.23, 43.87, 1.32]),
    #         Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
    #         ]


def find_donor(name):
    if name in make_sample_db().sample_db.keys():
        return name
    else:
        return None

    # return self.donor_data.get(Donor.normalize_name(name))

# db = DonorDB(make_sample_db())


class DonorDB():

    def __init__(self):

        self.all_donors = {}

        # self.all_donors = [Donor(name, donations)
        #                    for name, donations in zip(self.donor_names, self.donations)]




    def add_donor(self, name):
        donor = Donor(name)
        self.all_donors[name] = donor
        return donor


    def print_list(self):

        print("{msg1: <50}| {msg2: <12}| "

              "{msg3:<10}| {msg4: <12}".format(msg1="Donor Name",

                                               msg2="Total Given",

                                               msg3="Num Gifts",

                                               msg4="Average Gift"))
        for donor in self.all_donors:
            for key in donor.donor_dict:
                print(donor.donor_dict)
                t = sum(donor.donor_dict[key])
                n = len(donor.donor_dict[key])
                a = t / n

        print("{d: <50} ${t: 12.2f}{n: 12d}{a: 14.2f}".format(d=donor, t=t, n=n, a=a))

    def create_report(self):
        print("{msg1: <50}| {msg2: <12}| "

              "{msg3:<10}| {msg4: <12}".format(msg1="Donor Name",

                                               msg2="Total Given",

                                               msg3="Num Gifts",

                                               msg4="Average Gift"))
        for d in self.donor_dict:
            t = sum(self.donor_dict[d])
            n = len(self.donor_dict[d])
            a = t / n

            print("{d: <50} ${t: 12.2f}{n: 12d}{a: 14.2f}".format(d=d, t=t, n=n, a=a))

    def send_letters(self):
        try:
            for n, d in self.donor_dict.items():
                name = n.replace(" ", "_")
                f = open('{0}.txt'.format(name), 'wb')
                d = sum(d)
                text = ("Dear Mr./Ms. {},\n\n"
                        "    Thank you for your kind donation of USD ${}.\n"
                        "    It will be put to very good use.\n\n"
                        "          Sincerely,\n"
                        "            -The Team").format(n, d).encode()
                f.write(text)
                f.close()

        except IOError as i:
            print("Error code is", i)
        print("letter drafts are in the folder for your review."
              " Please review before mailing out.")


class Donor():

    def __init__(self, donor_name, donations=()):
        self.name = donor_name.strip()
        self.donations = list(donations)

    def make_donation(self, new_donation):

        self.donations.append(new_donation)

    @property
    def last_donation(self):
        try:
            return self.donations[-1]

        except IndexError:
            return None


dict_answer = {1: thank_you_loop,
               2: DonorDB().create_report,
               3: DonorDB().send_letters,
               4: quit}
dict_choice = {1: DonorDB().print_list,
               2: request_donation,
               3: quit}


if __name__ == "__main__":
    print('starting...')
    mainloop()
