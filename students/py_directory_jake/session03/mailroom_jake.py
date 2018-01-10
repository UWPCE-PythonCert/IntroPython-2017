#session 3 mailroom

"""
1. Send a Thank You, 2. Create a Report, 3. Quit
"""	
import sys


list_of_initial_donors = [['William Gates, III',10000],
						  ['Mark Zuckerberg',6000],
						  ['Jeff Bezos',8000],
						  ['Paul Allen',13000],
						  ['Satya Nadella',20000],
						  ['Jeff Bezos',3000]]

def report():
#	Donor Name                | Total Given | Num Gifts | Average Gift
#------------------------------------------------------------------
    name_list = []
    report_list = []
    print('\n{:<25} {:<15}  {:<15}   {:<15}'.format('Donor','Total ($)','AVG ($)','Number of Donations'))
    print('-'*85)
    for name in list_of_initial_donors:
        if [name[0]] not in name_list:
            name_list.append([name[0]]) #add name to reference index of duplicate people
            report_list.append([name[0]]) #add name to begin list of actual data
    for record in list_of_initial_donors:
        report_list[name_list.index([record[0]])].append(record[1]) #find report_list index USING name_list index for isolation
    for record in report_list: #record is in form [name, donate#1, #2, ...]
        print('{:<25} ${:<15.2f} ${:<15.2f}  {:<15}'.format(record[0], float(sum(record[1:])),float(sum(record[1:]) / (len(record) - 1)),len(record)-1))
    choices()


	

def list_add():
	clist = input("\nWould you like to see the list of donars? (type 'list' to observe. type 'menu' at anytime to return to the menu.)\n")
	if clist=='menu':
		choices()
		pass
	elif clist =='list':
		check_list()
		pass
	name_checked = input('\nWho is donating to our charity?\n')
	if name_checked == 'menu':
		choices()
		pass
	while True:
		try:
			donated_text = input('\nHow much are they donating?\n')
			if donated_text == 'menu':
				choices()
			donated_value = float(donated_text)
		except ValueError:
			print('\nPlease provide an numeric value.\n')
			continue
		break
	list_of_initial_donors.append([name_checked,donated_value])
	print(f'\nThank you! {name_checked} has donated ${donated_value} to a great cause!\n')
	choices()
	print(list_of_initial_donors)

def check_list():
	empty_list = []
	for i in list_of_initial_donors:
		if i[0] not in empty_list:
			empty_list.append(i[0])
	print(empty_list)
	


def choices():
	while True:
		try:
			choice = float(input('\n1. Send a Thank You\n2. Create a Report\n3. Quit\nWhat would you like to do?\n'))
		except ValueError:
			print('\nPlease select a value between 1 and 3.\n1 to Send a Thank you.\n2 to Create a Report\n3 to Quit the session')
			continue
		except TypeError:
			print('\nPlease select a value between 1 and 3.\n1 to Send a Thank you.\n2 to Create a Report\n3 to Quit the session')
			continue
		break
	if choice == 1:
			list_add()
	elif choice == 2:
			report()
	elif choice == 3:
		quit()

def quit():
	sys.exit()



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