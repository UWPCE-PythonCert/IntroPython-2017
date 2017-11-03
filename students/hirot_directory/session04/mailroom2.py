#!/usr/bin/env python3

donor_names = ["William Gates III", "Mark Zuckerberg", "Jeff Bezos", "Paul Allen"]
donations = [[200, 500], [2000, 3000], [4000, 5000], [100, 150]]
donor_dict = dict(zip(donor_names, donations))

def thank_you():

    while True:

        if (str(input("Do you want to see the current donor list? if yes, type List: ")).upper() == "LIST"):

            print(donor_dict)

        new_donor = str(input("Full Name: "))
        new_donation = int(input("How much do you want to donate?: "))


        # compact codes (with Chris's help during coffee office hours)

        if (new_donor not in donor_dict):

            donor_dict[new_donor] = []
            print(donor_dict)


        donor_dict[new_donor].append(new_donation)
        print(donor_dict)


        '''

        # Alternative code:

        if (new_donor in donor_dict):

            donor_dict[new_donor].append(new_donation)
            print(donor_dict)

        else:

            donor_dict[new_donor] = [new_donation]
            print(donor_dict)
        '''
 

        if(input("Type 'exit' to end?").lower() == "exit"): 
            break


def print_report():


    print("{msg1: <50}| {msg2: <12}| " \

      "{msg3:<10}| {msg4: <12}".format(msg1="Donor Name",

                                       msg2="Total Given",

                                       msg3="Num Gifts",

                                       msg4="Average Gift"))


    for d in donor_dict:
        t = sum(donor_dict[d])
        n = len(donor_dict[d]) #list.count() is to count inside of the list (i.e. # by blue)
        a = t/n

        print("{d: <50} ${t: 12.2f}{n: 12d}{a: 14.2f}".format(d=d, t=t, n=n, a=a))


def mainloop():

    while True:

        answer = int(input("Select from one of these options:\n"
                           "(1) Send a Thank you\n"
                           "(2) Create a Report\n"
                           "(3) quit\n"
                           ))

        if answer == 3:
            break

        elif answer == 1:
            thank_you()

        elif answer == 2:
            print_report()

        else:
            print("please type 1, 2, or 3")


if __name__ == "__main__":
    print('starting...')
    mainloop()
