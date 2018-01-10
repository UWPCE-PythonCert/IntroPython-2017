#session 3 mailroom

"""
1. Send a Thank You, 2. Create a Report, 3. Quit
"""

list_of_initial_donors = [['William Gates, III',10000],
                          ['Mark Zuckerberg',6000],
                          ['Jeff Bezos',8000],
                          ['Paul Allen',13000],
                          ['Satya Nadella',20000],
                          ['Jeff Bezos',3000]]

def list_add():
    clist = input("Would you like to see the list of donars? (type 'list' to observe)\n")
    if clist == 'menu':
        choices()
    elif clist == 'list':
        check_list()
        pass
    name_checked = input('Who is donating to our charity?\n')
    if name_checked == 'menu':
        choices()
    while True:
        donated_value = input('How much are they donating?\n')
        if donated_value == 'menu':
            choices()
        try:
            donated_value = float(donated_value)
        except ValueError:
            print('Please provide an numeric value.')
            continue
        break
    list_of_initial_donors.append([name_checked,donated_value])
    print(f'Thank you! {name_checked} has donated {donated_value} to a great cause!')
    choices()
    print(list_of_initial_donors)

def check_list():
    empty_list = []
    for i in list_of_initial_donors:
        if i[0] not in empty_list:
            empty_list.append(i[0])
    print(empty_list)

def report():
    name_list = []
    report_list = []
    for name in list_of_initial_donors:
        if [name[0]] not in name_list:
            name_list.append([name[0]]) #add name to reference index of duplicate people
            report_list.append([name[0]]) #add name to begin list of actual data
    for record in list_of_initial_donors:
        report_list[name_list.index([record[0]])].append(record[1]) #find report_list index USING name_list index for isolation
    for record in report_list: #record is in form [name, donate#1, #2, ...]
        print(record[0]) #for each name, index 0 of sublist is name
        print(sum(record[1:])) #after index 0, all entries are donations to sum
        print(sum(record[1:]) / (len(record) - 1)) #and then to average
    choices()

def choices():
    while True:
        try:
            choice = float(input('1. Send a Thank You\n2. Create a Report\n3. Quit\nWhat would you like to do?\n'))
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

"""
def check_exist():
   ...:     name_checked = input('Who is donating to our charity?\n')
   ...:     for i in list_of_initial_donors:
   ...:         if name_checked == i[0]:
   ...:             print(i[0], True)
   ...:         print(i[0],False)

donor_actuals=[]
for occurence

def mainloop():
                answer = int(input('(1) Select from of these optsions:\n"
                                  '(2) Create a Report\n'
                                  '(3) quit\n')


if __name__ == "__main__":
                print('starting...')
"""
