#!/usr/bin/env python
# name, donation total, number of donations and average of donations


# def thanks(x):


# def report(x):



# donar_list[
# [john, 1234, 5, <need to refactor average after donation> ],
# [],
# ]

def main_loop():
    answer = input("Select from one of the following options?\n"
            "(1) Send a Thank You\n"
            "(2) Make a Report\n"
            "(3) Quit\n"
            ">")

    if answer == 1 or answer == '1':
        #send letter 
        print(1)
        main_loop()
    elif answer == 2 or answer == '2':
        #make report
        print(2)
        main_loop()
    elif answer == 3 or answer == '3':
        #quit
        print(3)
        quit()
    else:
        answer == None
        print('\nPlease Enter a valid option\n')
        main_loop()

    # while user_input != quit

def thank_you():
    donor = input("Enter a donor's full name or type 'list' for all donors")
    #prompt for full name
    #add new name by typing it
    #if 'list', provide list of names

if __name__ == "__main__": 

    donor_list = [
    ['William Gates, III', 653784.49, 2, 32682.24],
    ['Mark Zuckerberg', 16396.10, 3, 5465.37],
    ['Jeff Bezos', 877.33, 1, 877.33],
    ['Paul Allen', 708.42, 3, 236.14]
    ]

    print(donor_list)

    print('starting...')
    main_loop()

    

    