#session 6 mailroom Python Flake8 Lint
#ctrl + ? comment blocks
#shift+tab over highlighted objects

"""
1. Send a Thank You, 2. Create a Report, 3. Quit
"""
import sys

#-----------------------------------------------------------------
# The main menu of this program.
#-----------------------------------------------------------------

def choices():
    """The main while loop, need refactoring"""
    dictswitch =    {'1':list_add, 
                     '2':report,
                     '3':send_letters_to_everyone,
                     '4':quit
                    }
    choice = input('\n(1) Send a Thank You\n(2) Create a Report\n(3) Send Letters to Everyone\n(4) Quit\nYou may type menu at anytime to return here.\n\nWhat would you like to do?\n')
    try:
        dictswitch[choice]()
    except KeyError:
        print('Please select a value between 1 and 4.\n1 to Send a Thank you.\n2 to Create a Report\n3 to Quit the session')
    finally:
        choices()
#-----------------------------------------------------------------
# Functional addtions to base donar list
#-----------------------------------------------------------------

dict_of_initial_donors = {'William Gates, III':[10000],
                          'Mark Zuckerberg':[6000],
                          'Jeff Bezos':[8000],
                          'Paul Allen':[13000],
                          'Satya Nadella':[20000]
                          }

#-----------------------------------------------------------------
# Adding a New Donar + Printing a Thank You to the Screen
#-----------------------------------------------------------------

def list_add():
    clist = input("Would you like to see the dict of donars? (type 'dict' to observe)\n")
    if clist == 'dict':
        print()
        check_dict()
        pass
    name_checked, donated_value = create_new_donor()
    add_donation(name_checked, donated_value)
    send_thank_you(name_checked, donated_value)

def add_donation(name_checked, donated_value):
    dict_of_initial_donors.setdefault(name_checked,[]).append(donated_value)
    print(donated_value in dict_of_initial_donors[name_checked])
    return donated_value in dict_of_initial_donors[name_checked]
   

def check_dict():
    [print(i) for i in dict_of_initial_donors.keys()]
    print()

#break out values for individuals testing
def create_new_donor():
    name_checked = input('\nWho is donating to our charity?\n').strip()
    donated_value = input('\nHow much are they donating?\n').strip()
    try:
        donated_value = float(donated_value)
    except ValueError:
        print('\nPlease provide an numeric value.')
    return name_checked, donated_value

def send_thank_you(name_checked, donated_value):
    email =(f'\nThank you! {name_checked} has donated ${donated_value} to a great cause!\n')
    print(email)
    return email

#-----------------------------------------------------------------
# The Report
#-----------------------------------------------------------------
#physical copy over

def report():
    header = (('\n{:<25} {:<15}  {:<15}   {:<15}\n'.format('Donor','Total ($)','AVG ($)','# of Donations')))
    line_break = ('-' * 75 + '\n')
    report_data = []
    for key, value in sorted(dict_of_initial_donors.items(),key=lambda i:sum(i[1]),reverse=True):
        donor = key
        total_donations = sum(value)
        average_donation = sum(value)/len(value)
        number_of_donations = len(value)
        report_data.append('{:<25} ${:<15.2f} ${:<15.2f}  {:<15}\n'.format(donor,
                                                                            total_donations,
                                                                            average_donation,
                                                                            number_of_donations))
    full_report = header + line_break + ''.join(report_data)
    print(full_report)
    return header

def quit():
    """quits the program"""
    sys.exit()

#-----------------------------------------------------------------
# Send Letters to Everyone
#-----------------------------------------------------------------

def send_letters_to_everyone():
    for key, value in sorted(dict_of_initial_donors.items(),key=lambda i:sum(i[1]),reverse=True):
        donor = key
        total_donations = sum(value)
        average_donation = sum(value)/len(value)
        number_of_donations = len(value)
        if number_of_donations > 1:
            s= 's'
        else:
            s = ''
        letter_output(donor, total_donations, number_of_donations, s)
    print('\nDonors have recieved their letter of total donations and thanks.')


def letter_output(donor, total_donations, number_of_donations, s):
    import os
    letter= f'\nDear {donor},'+f'\n\nThank you for your very kind donation of {total_donations} over {number_of_donations} donation{s}.'+f'\nYour generiosity has been put to very good use.'+f'\n\nSincerely,'+f'\nThe Team'
    if not os.path.exists('Donation_Letters'):
        os.mkdir('Donation_Letters')
    with open(os.path.join('Donation_Letters', donor + ".txt"), "w") as text_file:
        text_file.write(letter)
    return letter


    

#-----------------------------------------------------------------
# Intializer
#-----------------------------------------------------------------

if __name__ == '__main__':
    print('Intializing your choices!')
    choices()

