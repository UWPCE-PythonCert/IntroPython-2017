#!/usr/bin/env python

donor_names = ["Bill", "Fred"]
donations = [[200, 500], [2000, 3000]]

donors = list(zip(donor_names, donations))



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



