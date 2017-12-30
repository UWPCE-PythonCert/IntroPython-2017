#!/usr/bin/env python3

import sys


class Donor():


    def __init__(self):
        self.donor_names = ["William Gates III", "Mark Zuckerberg", "Jeff Bezos", "Paul Allen"]
        self.donations = [[200, 500], [2000, 3000], [4000, 5000], [100, 150]]
        self.donor_dict = {self.donor_names:self.donations for (self.donor_names, self.donations) in zip(self.donor_names, self.donations)}
        self.dict_answer = {1: self.thank_you_loop, 2: self.create_report, 3: self.send_letters, 4: self.quit}
        self.dict_choice = {1: self.print_list, 2: self.make_donation, 3: self.quit}


    @staticmethod
    def add_donor():
        donor_name = str(input("Full Name: "))
        return donor_name


    @staticmethod
    def add_donation():
        new_donation = int(input("How much do you want to donate?: "))
        return new_donation


    @staticmethod
    def select_submenu():
        choice = int(input("Select from one of these options:\n"
                              "(1) Show a list\n"
                              "(2) Enter a donation\n"  
                              "(3) Exit\n"
                              ))
        return choice


    @staticmethod
    def select_mainmenu():

        answer = int(input("Select from one of these options:\n"
                                   "(1) Send a Thank you\n"
                                   "(2) Create a Report\n"
                                   "(3) Send letters to everyone\n"
                                   "(4) quit\n"
                                   ))
        return answer

    @staticmethod
    def select_quit():

        selection = (input("Are you sure to quit? (Y or N) To return to main menu, please select 'N'.: ")).upper()
        return selection


    def print_list(self):

        print("{msg1: <50}| {msg2: <12}| " \

              "{msg3:<10}| {msg4: <12}".format(msg1="Donor Name",

                                               msg2="Total Given",

                                               msg3="Num Gifts",

                                               msg4="Average Gift"))
        for d in self.donor_dict:
            t = sum(self.donor_dict[d])
            n = len(self.donor_dict[d])
            a = t / n

            print("{d: <50} ${t: 12.2f}{n: 12d}{a: 14.2f}".format(d=d, t=t, n=n, a=a))


    def make_donation(self):
        donor_name = self.add_donor()
        new_donation = self.add_donation()

        if (donor_name not in self.donor_dict):
            self.donor_dict[donor_name] = []

        self.donor_dict[donor_name].append(new_donation)
        print("Thank you for donation, Mr./Ms. {}! Your donation amount is USD ${}.".format(donor_name, new_donation))


    def quit(self):
        print("quit function is called")

        try:
            selection = self.select_quit()
            if (selection == 'Y'):
                print("Good bye...")
                sys.exit()
            else:
                return self.mainloop()

        except ValueError as e:
            print("Error happened. Error is ",type(e),"Please type 1, 2 or 3")
        except KeyError as k:
            print("Error happened. Error is ",type(k),"Please type 1, 2 or 3")


    def thank_you_loop(self):
        while True:
            try: 
                choice = self.select_submenu()
                self.dict_choice[choice]()

            except ValueError as e:
                print("Error happened. Error is ", type(e) , "Please type 1, 2 or 3")
            except KeyError as k:
                print("Error happened. Error is ", type(k) , "Please type 1, 2 or 3")


    def create_report(self):
        print("{msg1: <50}| {msg2: <12}| " \

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
                text = "Dear Mr./Ms. {},\n\n    Thank you for your kind donation of USD ${}.\n    It will be put to very good use.\n\n          Sincerely,\n            -The Team".format(n, d).encode()
                f.write(text)
                f.close()

        except IOError as i:
            print("Error code is", i)
        print("letter drafts are in the folder for your review. Please review before mailing out.")


    def mainloop(self):
        while True:
            try:
                answer = self.select_mainmenu()
                self.dict_answer[answer]()

            except ValueError as e:
                print("Error happened. Error is ", type(e), "Please type 1, 2 or 3")
            except KeyError as k:
                print("Error happened. Error is ", type(k), "Please type 1, 2 or 3")


if __name__ == "__main__":
    print('starting...')
    Donor().mainloop()