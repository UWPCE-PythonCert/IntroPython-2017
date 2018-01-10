#session 5 mailroom

"""
1. Send a Thank You, 2. Create a Report, 3. Quit
"""
import sys

dict_of_initial_donors = {'William Gates, III':[10000],
                          'Mark Zuckerberg':[6000],
                          'Jeff Bezos':[8000],
                          'Paul Allen':[13000],
                          'Satya Nadella':[20000]
                          }

def report():
#   Donor Name                | Total Given | Num Gifts | Average Gift
#------------------------------------------------------------------
    print('\n{:<25} {:<15}  {:<15}   {:<15}'.format('Donor','Total ($)','AVG ($)','# of Donations'))
    print('-'*75)
    for key, value in sorted(dict_of_initial_donors.items(),key=lambda i:sum(i[1]),reverse=True):
        print('{:<25} ${:<15.2f} ${:<15.2f}  {:<15}'.format(key, sum(value), sum(value)/len(value),len(value)))
    choices()

def list_add():
    clist = input("Would you like to see the dict of donars? (type 'dict' to observe)\n")
    if clist == 'menu':
        choices()
    elif clist == 'dict':
        print()
        check_dict()
        pass
    name_checked = input('\nWho is donating to our charity?\n')
    if name_checked == 'menu':
        print()
        choices()
    while True:
        donated_value = input('\nHow much are they donating?\n')
        if donated_value == 'menu':
            print()
            choices()
        try:
            donated_value = float(donated_value)
        except ValueError:
            print('\nPlease provide an numeric value.')
            continue
        break
    dict_of_initial_donors.setdefault(name_checked,[]).append(donated_value)
    print(f'Thank you! {name_checked} has donated ${donated_value} to a great cause!')
    print(dict_of_initial_donors)
    choices()
   

def check_dict():
    [print(i) for i in dict_of_initial_donors.keys()]
    print()

def quit():
    sys.exit()

def choices():
    while True:
        try:
            choice = float(input('\n(1) Send a Thank You\n(2) Create a Report\n(3) Quit\nYou may type menu at anytime to return here.\n\nWhat would you like to do?\n'))
        except ValueError:
            print('Please select a value between 1 and 3.\n1 to Send a Thank you.\n2 to Create a Report\n3 to Quit the session')
            continue
        break
    if choice == 1:
        list_add()
    elif choice == 2:
        report()
    elif choice == 3:
        quit()


if __name__ == '__main__':
    choices()