#!/usr/bin/env python

# # Using zip to create a data structure for the donor data
# donor_names = ["Bill", "Fred"]
# donations = [[200, 500], [2000, 3000]]
# donors = list(zip(donor_names, donations))

# However, in this case, unless that data is coming from elsewhere, you
# might as well simply hard code the data directly:

donors = [("William Gates, III", [653772.32, 12.17]),
          ("Jeff Bezos", [877.33]),
          ("Paul Allen", [663.23, 43.87, 1.32]),
          ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
          ]

# Either way, you end up with a list of tuples -- each tuple is one "record",
# and has the name as the zeroth element, and a list of donations as the other
# element.
# It's important the the list of donation is a mutable -- you need to be
# able to append new donations to it.


def thank_you():
    print("this is the thank you function")

def print_report():
    print("this is the print report function")


def mainloop():
    """
     “Send a Thank You”, “Create a Report” or “quit”)
     """
    #result = input("type something > ")
    #print("you typed: ", result)

    while True:
        answer = int(input("Select from one of these options:\n"
              "(1) Send a Thank You\n"
              "(2) Create a Report\n"
              "(3) quit\n"
              "> "))
        if answer == 3:
            break
        elif answer == 1:
            thank_you()
        elif answer == 2:
            print_report()
        else:
            print("Please type 1, 2, or 3")





if __name__ == "__main__":
    print('starting...')
    mainloop()



