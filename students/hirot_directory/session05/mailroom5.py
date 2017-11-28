#!/usr/bin/env python3

"""

Mailroom5.py
session05: 
  Dictionary for the menu selections
  Comprehension
  Exception Handling
session06:
  Refactoring for unittest

"""

import sys

donor_names = ["William Gates III", "Mark Zuckerberg", "Jeff Bezos", "Paul Allen"]
donations = [[200, 500], [2000, 3000], [4000, 5000], [100, 150]]

donor_dict = { donor_names:donations for (donor_names, donations) in zip(donor_names, donations)}


def print_list():

    print("{msg1: <50}| {msg2: <12}| " \

          "{msg3:<10}| {msg4: <12}".format(msg1="Donor Name",

                                           msg2="Total Given",

                                           msg3="Num Gifts",

                                           msg4="Average Gift"))
    for d in donor_dict:
        t = sum(donor_dict[d])
        n = len(donor_dict[d]) 
        a = t / n

        print("{d: <50} ${t: 12.2f}{n: 12d}{a: 14.2f}".format(d=d, t=t, n=n, a=a))


def make_donation():
    donor_name = str(input("Full Name: "))
    new_donation = int(input("How much do you want to donate?: "))

    if (donor_name not in donor_dict):
        donor_dict[donor_name] = []

    donor_dict[donor_name].append(new_donation)
    print("Thank you for donation, Mr./Ms. {}! Your donation amount is USD ${}.".format(donor_name, new_donation))


def quit():
    print("quit function is called")

    try:
        selection = (input("Are you sure to quit? (Y or N) To return to main menu, please select 'N'.: ")).upper()
        if (selection == 'Y'):
            print("Good bye...")
            sys.exit()
        else:
          return True # refactoring

    except KeyError as k:
        print("Error happened. Error is ",type(k),"Please type 1, 2 or 3")


dict_choice = {'1': print_list, '2': make_donation, '3': quit} # refactoring


def thank_you_loop():
    while True:
        try: 
            choice = input("Select from one of these options:\n"
                          "(1) Show a list\n"
                          "(2) Enter a donation\n"  
                          "(3) Exit\n"
                          )
            result = dict_choice[choice]() # refactoring

            if result: # refactoring
              break

        except KeyError as k:
            print("Error happened. Error is ", type(k) , "Please type 1, 2 or 3")


def send_letters():
    try:
        for n, d in donor_dict.items():
            name = n.replace(" ", "_")
            f = open('{0}.txt'.format(name), 'wb')
            d = sum(d)
            text = "Dear Mr./Ms. {},\n\n    Thank you for your kind donation of USD ${}.\n    It will be put to very good use.\n\n          Sincerely,\n            -The Team".format(n, d).encode()
            f.write(text)
            f.close()

    except IOError as i:
        print("Sorry...Program crashed....Error type is...", type(i))

    else:
      print("letter drafts are in the folder for your review. Please review before mailing out.")


dict_answer = {'1': thank_you_loop, '2': print_list, '3': send_letters, '4': quit}


def mainloop():
    while True:
        try:
            answer = input("Select from one of these options:\n"
                               "(1) Send a Thank you\n"
                               "(2) Create a Report\n"
                               "(3) Send letters to everyone\n"
                               "(4) quit\n"
                               )
            dict_answer[answer]()

        except KeyError as k:
            print("Sorry...Program crashed....Error type is....", type(k), "Please type 1, 2 or 3")


if __name__ == "__main__":
    print('starting...')
    mainloop()
