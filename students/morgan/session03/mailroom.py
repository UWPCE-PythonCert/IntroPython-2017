#!/usr/bin/env python
# name, donation total, number of donations and average of donations


# def thanks(x):


# def report(x):



# donar_list[
# [john, 1234, 5, <need to refactor average after donation> ],
# [],
# ]

def main_loop():
    
    '''this is the version I was originally using before reading through the file
    from chris and realizing it's the same but morce concise'''
    # answer = input("Select from one of the following options?\n"
    #         "(1) Send a Thank You\n"
    #         "(2) Make a Report\n"
    #         "(3) Quit\n"
    #         ">")

    # if answer == 1 or answer == '1':
    #     #send letter 
    #     print(1)
    #     thank_you()
    # elif answer == 2 or answer == '2':
    #     #make report
    #     print(2)
    #     main_loop()
    # elif answer == 3 or answer == '3':
    #     #quit
    #     print(3)
    #     quit()
    # else:
    #     answer == None
    #     print('\nPlease Enter a valid option\n')
    #     main_loop()

    while True:
        answer = input("Select from one of these options:\n"
              "(1) Send a Thank You\n"
              "(2) Create a Report\n"
              "(3) quit\n"
              "> ")
        if answer == 3 or answer =='3':
            break
        elif answer == 1 or answer =='1':
            thank_you()
        elif answer == 2 or answer =='2':
            print_report()
        else:
            print("Please type 1, 2, or 3")
            

    # while user_input != quit

def thank_you():
    '''takes in the name or 'list' command'''
    donor_input = input("Enter a donor's full name or type 'list' for all donors \n"
        "> ")
    
    '''if 'list' is chosen than the current list of donor names are printed'''
    if str.lower(donor_input) == 'list':
        print('List of donors: \n')
        for row in donor_list:
            print(row[0]+'\n')
   
    elif name_in_list(donor_input) is False:
        '''if the donor is not on the current list, it will be added to the list
    with the donation amount, the number of  donations set to 1 and a
    thank you leter generated'''
        print('your mom')
        donor_donation = float(input('Enter donation amount \n'
            '> '))
        add_donor(donor_input, donor_donation)
        write_letter(donor_input, donor_donation)

    elif name_in_list(donor_input):
        # print('wwop!')
        proper_name = donor_list[name_in_list(donor_input)][0]
        donor_donation = input('Enter donation amout \n'
            '> ')
        add_donation(proper_name, donor_donation)
        write_letter(proper_name, donor_donation)

    

    # for row in donor_list:
        # if row[0] == donor_input:
            # print(row, row[0])

def write_letter(name, donor_donation):
    '''writes a brief letter to the donor with their most current donation'''
    print('Dear {}, \n'
        'Thank you for your generous donation of ${}.\n'
        'We look forward to your continued support\n'
        '-= The Students =-\n'.format(name, donor_donation))

def name_in_list(name):
    '''searches the list of donors and returns the index for that donor's entry
    or False if does not exist in donor list'''

    for x in donor_list:
        if str.lower(x[0]) == str.lower(name):
            # print('true',x[0])
            # print(donor_list.index(x))
            return donor_list.index(x)
    # print('false')
    return False   

def add_donor(name, donation):

    donor_list.append([name,donation,1])
    

def add_donation(name, donation):

    for x in donor_list:
        if str.lower(x[0]) == str.lower(name):
            x[1] += float(donation)
            x[2] += 1
            # print(x)
            # return x
    # #prompt for full name
    # if str.lower(donor) == 'list':
    #     print('List of donors: \n')
    #     while x < len(donor_list):
    #         print(donor_list[x][0]+'\n')
    #         x += 1
    #     thank_you()
    # elif donor in donor_list[0][0]:

    #     print('found it')  
    #add new name by typing it
    #if 'list', provide list of names

if __name__ == "__main__": 

    donor_list = [
    ['William Gates, III', 653784.49, 2],
    # 32682.24
    ['Mark Zuckerberg', 16396.10, 3],
    # 5465.37
    ['Jeff Bezos', 877.33, 1],
    # 877.33
    ['Paul Allen', 708.42, 3],
    # 236.14
    ['dude',200.00, 2]
    # 100
    ]

    
        


    # print(donor_list)

    print('starting...')
    main_loop()

    

    